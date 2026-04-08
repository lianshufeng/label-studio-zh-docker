#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
    return " ".join(text.split()).strip()


def load_modules(translations: dict[str, object]) -> tuple[dict[str, dict[str, str]], list[dict[str, object]]]:
    module_maps: dict[str, dict[str, str]] = {}
    untranslated: list[dict[str, object]] = []
    for module_name in MODULE_ORDER:
        entries = translations.get("modules", {}).get(module_name, [])
        module_map: dict[str, str] = {}
        for entry in entries:
            source = normalize(str(entry.get("source", "")))
            target = normalize(str(entry.get("target", "")))
            if entry.get("status") == "approved" and source and target:
                module_map[source] = target
            else:
                untranslated.append(
                    {
                        "source": source,
                        "priority": entry.get("priority", "low"),
                        "score": entry.get("score", 0),
                        "files": entry.get("files", []),
                        "contexts": entry.get("contexts", []),
                    }
                )
        if module_map:
            module_maps[module_name] = dict(sorted(module_map.items(), key=lambda item: item[0].lower()))
    untranslated.sort(key=lambda item: (-int(item.get("score", 0)), str(item.get("source", "")).lower()))
    return module_maps, untranslated


def render_js(module_maps: dict[str, dict[str, str]]) -> str:
    payload = json.dumps(module_maps, ensure_ascii=False, indent=2)
    return f"""(function () {{
  var config = window.LS_ZH_OVERLAY || {{}};
  if (config.enabled === false) {{
    return;
  }}

  var MODULE_MAPS = {payload};
  var ATTRIBUTE_NAMES = ["placeholder", "title", "aria-label", "aria-placeholder", "alt", "data-tooltip", "data-title", "value"];
  var SKIP_TAGS = {{ SCRIPT: true, STYLE: true, CODE: true, PRE: true, TEXTAREA: true }};
  var exactMap = Object.create(null);
  var normalizedMap = Object.create(null);
  var phrasePairs = [];

  Object.keys(MODULE_MAPS).forEach(function (moduleName) {{
    var moduleMap = MODULE_MAPS[moduleName];
    Object.keys(moduleMap).forEach(function (source) {{
      var target = moduleMap[source];
      exactMap[source] = target;
      normalizedMap[normalizeText(source)] = target;
      if (source.length >= 12 && source.indexOf("{{") === -1 && source.indexOf("${{") === -1) {{
        phrasePairs.push([source, target]);
      }}
    }});
  }});

  phrasePairs.sort(function (left, right) {{
    return right[0].length - left[0].length;
  }});

  function normalizeText(text) {{
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
    return !!element.closest("[data-no-translate], [data-translation-skip], .task-text, .lsf-task-data");
  }}

  function translateText(text) {{
    if (!text) {{
      return text;
    }}
    var trimmed = text.trim();
    if (!trimmed) {{
      return text;
    }}
    var translated = exactMap[trimmed] || normalizedMap[normalizeText(trimmed)] || null;
    if (translated) {{
      return text.replace(trimmed, translated);
    }}
    var updated = text;
    phrasePairs.forEach(function (pair) {{
      if (updated.indexOf(pair[0]) !== -1) {{
        updated = updated.split(pair[0]).join(pair[1]);
      }}
    }});
    updated = updated.replace(/\\b1 minute ago\\b/g, "1 分钟前");
    updated = updated.replace(/\\b(\\d+)\\s+minutes ago\\b/g, "$1 分钟前");
    updated = updated.replace(/\\b1 hour ago\\b/g, "1 小时前");
    updated = updated.replace(/\\b(\\d+)\\s+hours ago\\b/g, "$1 小时前");
    updated = updated.replace(/\\bless than a minute ago\\b/g, "刚刚");
    updated = updated.replace(/\\bseconds ago\\b/g, "几秒前");
    updated = updated.replace(/\\b(\\d+) of (\\d+) Tasks \\(([^)]+)\\)/g, "$1 / $2 任务 ($3)");
    updated = updated.replace(/\\bTasks:\\s*([0-9]+\\s*\\/\\s*[0-9]+)\\b/g, "任务：$1");
    updated = updated.replace(/\\bSubmitted annotations:\\s*(\\d+)\\b/g, "已提交标注：$1");
    updated = updated.replace(/\\bPredictions:\\s*(\\d+)\\b/g, "预测：$1");
    updated = updated.replace(/\\(opens in a new tab\\)/g, "(在新标签页中打开)");
    updated = updated.replace(/^Home \\| Label Studio$/g, "首页 | Label Studio");
    updated = updated.replace(/^Projects \\| Label Studio$/g, "项目 | Label Studio");
    updated = updated.replace(/^Create new project$/g, "创建新项目");
    updated = updated.replace(/^Cancel project creation$/g, "取消项目创建");
    updated = updated.replace(/^Description$/g, "描述");
    updated = updated.replace(/^Optional description of your project$/g, "项目可选描述");
    updated = updated.replace(/\bSee all tags\b/g, "查看所有标签");
    updated = updated.replace(/\bSee all\b/g, "查看全部");
    updated = updated.replace(/\bAdd Webhook\b/g, "添加网络钩子");
    updated = updated.replace(/\bAdd your first Webhook\b/g, "添加你的第一个网络钩子");
    updated = updated.replace(
      /You can control access to specific projects and workspaces for internal team members and external annotators using Label Studio 企业版\\./g,
      "使用 Label Studio 企业版，你可以为内部团队成员和外部标注员控制特定项目和工作区的访问权限。"
    );
    updated = updated.replace(/^Invite Members$/g, "邀请成员");
    updated = updated.replace(/^Reset Link$/g, "重置链接");
    updated = updated.replace(/^Copy link$/g, "复制链接");
    updated = updated.replace(/^Legacy Token$/g, "旧版令牌");
    updated = updated.replace(/^Upload Image$/g, "上传图片");
    updated = updated.replace(/^Phone$/g, "电话");
    updated = updated.replace(
      /Invite members to join your Label Studio instance\. People that you invite have full access to all of your projects\. Learn more\./g,
      "邀请成员加入你的 Label Studio 实例。你邀请的人将拥有你所有项目的完整访问权限。了解更多。"
    );
    return updated;
  }}

  function translateDocumentTitle() {{
    if (!document.title) {{
      return;
    }}
    var nextTitle = translateText(document.title);
    if (nextTitle !== document.title) {{
      document.title = nextTitle;
    }}
  }}

  function processTextNode(node) {{
    if (!node || !node.parentElement || shouldSkipElement(node.parentElement)) {{
      return;
    }}
    var nextValue = translateText(node.nodeValue);
    if (nextValue !== node.nodeValue) {{
      node.nodeValue = nextValue;
    }}
  }}

  function processAttributes(element) {{
    if (!(element instanceof Element) || shouldSkipElement(element)) {{
      return;
    }}
    ATTRIBUTE_NAMES.forEach(function (attr) {{
      if (!element.hasAttribute(attr)) {{
        return;
      }}
      var currentValue = element.getAttribute(attr);
      var nextValue = translateText(currentValue);
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
    var elementWalker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT);
    while (elementWalker.nextNode()) {{
      processAttributes(elementWalker.currentNode);
    }}
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
  }}

  function applyOverlay() {{
    translateDocumentTitle();
    walk(document.body);
  }}

  function scheduleApplyOverlay() {{
    [0, 120, 400, 1000].forEach(function (delay) {{
      window.setTimeout(applyOverlay, delay);
    }});
  }}

  function hookHistory(methodName) {{
    var original = history[methodName];
    history[methodName] = function () {{
      var result = original.apply(this, arguments);
      scheduleApplyOverlay();
      return result;
    }};
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

  hookHistory("pushState");
  hookHistory("replaceState");
  window.addEventListener("popstate", function () {{
    scheduleApplyOverlay();
  }});

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", scheduleApplyOverlay, {{ once: true }});
  }} else {{
    scheduleApplyOverlay();
  }}

  observer.observe(document.documentElement, {{
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ATTRIBUTE_NAMES
  }});
}})();
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build runtime overlay JS from translations.")
    parser.add_argument("translations_json", help="Path to merged translations JSON.")
    parser.add_argument("--output-js", required=True, help="Path to output runtime JS.")
    parser.add_argument("--untranslated-report", required=True, help="Path to untranslated report JSON.")
    args = parser.parse_args()
    payload = json.loads(Path(args.translations_json).read_text(encoding="utf-8"))
    module_maps, untranslated = load_modules(payload)
    output_js = Path(args.output_js).resolve()
    output_js.parent.mkdir(parents=True, exist_ok=True)
    output_js.write_text(render_js(module_maps), encoding="utf-8", newline="\n")
    Path(args.untranslated_report).resolve().write_text(json.dumps({"total": len(untranslated), "items": untranslated}, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
