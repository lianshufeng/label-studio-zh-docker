#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path


MODULE_ORDER = [
    "auth",
    "home",
    "projects",
    "import_export",
    "data_manager",
    "labeling",
    "settings",
    "storage",
    "webhooks",
    "organization",
    "templates",
    "generic",
]


def normalize(text: str) -> str:
    return " ".join(str(text).split()).strip()


def is_placeholder(value: str) -> bool:
    if not value:
        return True
    compact = value.replace(" ", "")
    return bool(re.fullmatch(r"[?？]+", compact) or "??" in compact or "�" in compact)


def contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def is_untranslated_target(source: str, target: str) -> bool:
    return normalize(source).casefold() == normalize(target).casefold() and not contains_chinese(target)


def load_payload(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_module_maps(payload: dict[str, object]) -> OrderedDict[str, OrderedDict[str, str]]:
    modules = payload.get("modules", {})
    module_maps: OrderedDict[str, OrderedDict[str, str]] = OrderedDict()

    for module_name in MODULE_ORDER:
        entries = modules.get(module_name, [])
        translated: OrderedDict[str, str] = OrderedDict()
        for entry in entries:
            source = normalize(entry.get("source", ""))
            target = normalize(entry.get("target", ""))
            status = normalize(entry.get("status", "approved")).lower() or "approved"
            if not source or is_placeholder(target) or is_untranslated_target(source, target) or status == "pending":
                continue
            if source not in translated:
                translated[source] = target
        if translated:
            module_maps[module_name] = translated

    return module_maps


def render_module_maps(module_maps: OrderedDict[str, OrderedDict[str, str]]) -> str:
    lines = ["var MODULE_MAPS = {"]
    module_names = list(module_maps.keys())
    for module_index, module_name in enumerate(module_names):
        lines.append(f"  {module_name}: {{")
        entries = list(module_maps[module_name].items())
        for entry_index, (source, target) in enumerate(entries):
            comma = "," if entry_index < len(entries) - 1 else ""
            lines.append(f"    {json.dumps(source, ensure_ascii=False)}: {json.dumps(target, ensure_ascii=False)}{comma}")
        module_comma = "," if module_index < len(module_names) - 1 else ""
        lines.append(f"  }}{module_comma}")
    lines.append("};")
    return "\n".join(lines)


def render_overlay_js(module_maps: OrderedDict[str, OrderedDict[str, str]]) -> str:
    module_maps_js = render_module_maps(module_maps)
    return f"""(function () {{
  "use strict";

  var config = window.LS_ZH_OVERLAY || {{}};

  if (config.enabled === false) {{
    return;
  }}

  {module_maps_js}

  var SKIP_TAGS = {{
    SCRIPT: true,
    STYLE: true,
    CODE: true,
    PRE: true,
    TEXTAREA: true
  }};

  var ATTRIBUTES = [
    "placeholder",
    "title",
    "aria-label",
    "aria-placeholder",
    "alt",
    "data-tooltip",
    "data-title",
    "value"
  ];

  var EXACT_MAP = Object.create(null);
  var NORMALIZED_MAP = Object.create(null);
  var PHRASE_RULES = [];

  Object.keys(MODULE_MAPS).forEach(function (moduleName) {{
    var moduleMap = MODULE_MAPS[moduleName] || {{}};
    Object.keys(moduleMap).forEach(function (source) {{
      var target = moduleMap[source];
      if (!(source in EXACT_MAP)) {{
        EXACT_MAP[source] = target;
      }}

      var normalizedSource = normalizeSpaces(source);
      if (!(normalizedSource in NORMALIZED_MAP)) {{
        NORMALIZED_MAP[normalizedSource] = target;
      }}

      if (source.length >= 8 && source.length <= 120 && source.indexOf(" ") !== -1) {{
        PHRASE_RULES.push([source, target]);
      }}
    }});
  }});

  PHRASE_RULES.sort(function (a, b) {{
    return b[0].length - a[0].length;
  }});

  function normalizeSpaces(text) {{
    return String(text || "").replace(/\\s+/g, " ").trim();
  }}

  function shouldSkipElement(element) {{
    if (!element) {{
      return false;
    }}

    if (SKIP_TAGS[element.tagName]) {{
      return true;
    }}

    if (element.closest("script, style, code, pre, textarea")) {{
      return true;
    }}

    return !!element.closest([
      '[data-region="true"]',
      '[data-testid="task-content"]',
      '[class*="task-text"]',
      '[class*="task-preview"]',
      '[class*="annotation-text"]',
      '[class*="htx-text"]',
      '[class*="lsf-richtext"]'
    ].join(", "));
  }}

  function translateValue(value) {{
    if (!value) {{
      return value;
    }}

    var exact = EXACT_MAP[value];
    if (exact) {{
      return exact;
    }}

    var normalized = normalizeSpaces(value);
    if (!normalized) {{
      return value;
    }}

    var normalizedExact = NORMALIZED_MAP[normalized];
    if (normalizedExact) {{
      return value.replace(normalized, normalizedExact);
    }}

    var nextValue = value;
    PHRASE_RULES.forEach(function (pair) {{
      var source = pair[0];
      var target = pair[1];
      if (nextValue.indexOf(source) !== -1) {{
        nextValue = nextValue.split(source).join(target);
      }}
    }});

    return nextValue;
  }}

  function processTextNode(node) {{
    if (!node || !node.parentElement || shouldSkipElement(node.parentElement)) {{
      return;
    }}

    var nextValue = translateValue(node.nodeValue);
    if (nextValue !== node.nodeValue) {{
      node.nodeValue = nextValue;
    }}
  }}

  function processAttributes(element) {{
    if (!(element instanceof Element) || shouldSkipElement(element)) {{
      return;
    }}

    ATTRIBUTES.forEach(function (attr) {{
      if (!element.hasAttribute(attr)) {{
        return;
      }}

      var currentValue = element.getAttribute(attr);
      var nextValue = translateValue(currentValue);
      if (nextValue !== currentValue) {{
        element.setAttribute(attr, nextValue);
        if (attr === "value" && "value" in element) {{
          element.value = nextValue;
        }}
      }}
    }});
  }}

  function walk(root) {{
    if (!root) {{
      return;
    }}

    if (root.nodeType === Node.TEXT_NODE) {{
      processTextNode(root);
      return;
    }}

    if (root.nodeType !== Node.ELEMENT_NODE || shouldSkipElement(root)) {{
      return;
    }}

    processAttributes(root);

    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {{
      acceptNode: function (node) {{
        if (!node.parentElement || shouldSkipElement(node.parentElement)) {{
          return NodeFilter.FILTER_REJECT;
        }}

        return NodeFilter.FILTER_ACCEPT;
      }}
    }});

    while (walker.nextNode()) {{
      processTextNode(walker.currentNode);
    }}

    root.querySelectorAll("*").forEach(processAttributes);
  }}

  var observer = new MutationObserver(function (mutations) {{
    mutations.forEach(function (mutation) {{
      if (mutation.type === "characterData") {{
        processTextNode(mutation.target);
        return;
      }}

      if (mutation.type === "attributes") {{
        processAttributes(mutation.target);
        return;
      }}

      mutation.addedNodes.forEach(function (node) {{
        walk(node);
      }});
    }});
  }});

  function applyOverlay() {{
    walk(document.body);
  }}

  function hookHistory(methodName) {{
    var original = history[methodName];
    if (typeof original !== "function") {{
      return;
    }}

    history[methodName] = function () {{
      var result = original.apply(this, arguments);
      window.setTimeout(applyOverlay, 0);
      return result;
    }};
  }}

  hookHistory("pushState");
  hookHistory("replaceState");

  window.addEventListener("popstate", function () {{
    window.setTimeout(applyOverlay, 0);
  }});

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", applyOverlay, {{ once: true }});
  }} else {{
    applyOverlay();
  }}

  observer.observe(document.documentElement, {{
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ATTRIBUTES
  }});
}})();
"""


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build final Label Studio zh overlay JS from translated catalog.")
    parser.add_argument("translations_json", help="Path to synced translations JSON.")
    parser.add_argument("--output-js", required=True, help="Path to write final overlay JS.")
    parser.add_argument(
        "--untranslated-report",
        required=True,
        help="Path to write untranslated entries report derived from the merged translations file.",
    )
    args = parser.parse_args()

    translations_path = Path(args.translations_json).resolve()
    payload = load_payload(translations_path)
    module_maps = collect_module_maps(payload)

    untranslated_modules: OrderedDict[str, list[dict[str, object]]] = OrderedDict()
    for module_name in MODULE_ORDER:
        entries = payload.get("modules", {}).get(module_name, [])
        missing: list[dict[str, object]] = []
        for entry in entries:
            source = normalize(entry.get("source", ""))
            target = normalize(entry.get("target", ""))
            if source and is_placeholder(target):
                missing.append(
                    {
                        "source": source,
                        "priority": normalize(entry.get("priority", "low")).lower() or "low",
                        "score": int(entry.get("score", 0) or 0),
                        "files": entry.get("files", [])[:5],
                        "contexts": entry.get("contexts", [])[:3],
                    }
                )
        if missing:
            untranslated_modules[module_name] = missing

    output_js_path = Path(args.output_js).resolve()
    output_js_path.parent.mkdir(parents=True, exist_ok=True)
    output_js_path.write_text(render_overlay_js(module_maps), encoding="utf-8", newline="\n")

    write_json(
        Path(args.untranslated_report).resolve(),
        {
            "total": sum(len(values) for values in untranslated_modules.values()),
            "items": [item for values in untranslated_modules.values() for item in values],
            "modules": untranslated_modules,
        },
    )


if __name__ == "__main__":
    main()
