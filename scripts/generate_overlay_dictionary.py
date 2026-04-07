#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
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

ALWAYS_INCLUDE = {
    "Access Token",
    "Account & Settings",
    "API Documentation",
    "Copied!",
    "Create Project",
    "3-Point Rectangle",
    "Data Import",
    "Docs",
    "Data Manager",
    "Delete Project",
    "Danger Zone",
    "Email Preferences",
    "Export data",
    "Export",
    "General",
    "Home",
    "Hotkeys",
    "Import",
    "Instructions",
    "JSON-MIN",
    "Labeling Interface",
    "Labeling Setup",
    "Learn more",
    "Light",
    "Log in",
    "Log In",
    "Log Out",
    "Membership Info",
    "My Account",
    "Organization",
    "Members",
    "Optional description of your project",
    "Password",
    "Personal Access Token",
    "Personal Info",
    "Project Name",
    "Projects",
    "Reset Cache",
    "Reset to Defaults",
    "Save and Leave",
    "Select an option",
    "Settings",
    "Slack Community",
    "Sign up",
    "Sign Up",
    "Submit",
    "You can export dataset in one of the following formats:",
    "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.",
    "Workspace",
    "Webhooks",
    "Drop All Tabs",
    "Cloud Storage",
}

EXACT_BLOCKLIST = {
    "base.html",
    "simple.html",
    "favicon.ico",
    "history.back()",
    "location.reload()",
    "noopener noreferrer",
}

PHRASE_BLOCKLIST = (
    "toBe(",
    "describe(",
    "expect(",
    "should ",
    "handles ",
    "handle ",
    "should render",
    "should call",
    "returns ",
    "creates ",
    "adds ",
    "filters ",
    "calls ",
    "renders ",
    "accepts ",
    "sets ",
    "works with",
    "when no ",
    "when not ",
    "when project",
    "className",
    "cursor:",
    "display:",
    "margin:",
    "padding:",
    "background=",
    "pointSize",
    "strokeLinecap",
    "viewBox",
    "rgba(",
    "calc(",
    "userpic",
    "selected.",
    "field.",
    "dm.",
    "lsf-",
    "LabelStudio",
    "child-field",
    "project-form field",
    "ui divider",
    "ui form",
    "ui grid",
    "class=",
    "fill=",
    "viewBox",
    "Content-Type",
    "Cache-Control",
    "DOMContentLoaded",
    "Jane Doe",
    "John Doe",
    "Human Signal Logo",
    "example fetch",
    "Example fetch",
    "Example CURL",
    "example_code",
    "field field",
    "min-width:",
    "max-width:",
    "position:",
    "overflow-",
    "hover:",
    "focus:",
    "transition-",
)

REGEX_BLOCKLIST = [
    re.compile(r"^#?[0-9A-Fa-f]{3,8}$"),
    re.compile(r"^(ctrl|alt|shift|cmd)\+", re.IGNORECASE),
    re.compile(r"^[#.].+"),
    re.compile(r"^[a-z0-9_.-]+$"),
    re.compile(r"^[A-Z0-9_:-]+$"),
    re.compile(r"^[a-z]+(?:[A-Z][a-z0-9]+)+$"),
    re.compile(r"^\d"),
    re.compile(r"^[Mm]\d"),
    re.compile(r"\.(svg|png|jpg|jpeg|gif|json|css|scss|tsx|jsx|js|py|md|yml|yaml)$", re.IGNORECASE),
    re.compile(r"^(true|false|null|undefined)$", re.IGNORECASE),
    re.compile(r"^https?://", re.IGNORECASE),
    re.compile(r"[{}[\]<>]"),
    re.compile(r"(?:^|[ /])(?:flex|grid|border|rounded|gap|text-|bg-|px-|py-|pt-|pb-|pl-|pr-|mt-|mb-|ml-|mr-|w-|h-)\S*"),
    re.compile(r"^(?:!?[a-z0-9]+(?:-[a-z0-9]+)+)(?:\s+(?:!?[a-z0-9]+(?:-[a-z0-9]+)+))*$", re.IGNORECASE),
    re.compile(r"^(?=.*[-_])[a-z0-9_-]+(?:\s+[a-z0-9_-]+)+$", re.IGNORECASE),
    re.compile(r"^[A-Za-z]{1,4}\s+\d{2},\s+\d{4}(?:\s+[A-Za-z:]+)*$"),
    re.compile(r"^[A-Za-z]\s+j,\s+Y$"),
    re.compile(r"\b(?:yyyy|yy|dd|MM|MMM|HH:mm|KK:mm|hh:mm|mm:ss|M j, Y)\b"),
    re.compile(r"\b(?:px|rem|em|vh|vw|deg|ms)\b", re.IGNORECASE),
    re.compile(r"\b(?:spec|story|storybook|mock|fixture|snapshot|test)\b", re.IGNORECASE),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"--"),
]

BOOST_WORDS = (
    "add ",
    "allow",
    "annotation",
    "api",
    "button",
    "cancel",
    "cloud",
    "copy",
    "create",
    "data",
    "delete",
    "description",
    "documentation",
    "email",
    "empty",
    "error",
    "export",
    "file",
    "filter",
    "import",
    "invite",
    "label",
    "learn",
    "hotkey",
    "keyboard",
    "log ",
    "member",
    "name",
    "option",
    "password",
    "project",
    "save",
    "select",
    "setting",
    "storage",
    "docs",
    "submit",
    "task",
    "template",
    "token",
    "workspace",
)

KIND_SCORES = {
    "attributes": 3,
    "groups": 2,
    "html": 2,
    "quoted": 1,
    "titles": 3,
}

PRIORITY_SCORES = {
    "high": 3,
    "medium": 1,
    "low": 0,
}

CODE_TOKEN_RE = re.compile(
    r"\b(?:const|let|var|function|return|import|export|extends|interface|type|props?|state|async|await|null|undefined)\b"
)
CLASSLIKE_PATTERNS = {REGEX_BLOCKLIST[13], REGEX_BLOCKLIST[14]}


def normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def is_sentence_like(text: str) -> bool:
    words = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)?", text)
    if len(words) < 5:
        return False
    lowered = text.lower()
    return bool(re.search(r"\b(?:a|an|the|for|and|your|you|with|to|of|in|on)\b", lowered))


def looks_like_code_fragment(text: str) -> bool:
    if "`" in text or "=>" in text or "&&" in text or "||" in text or "::" in text:
        return True
    if re.search(r"[;=]{1,}|[?]\s", text):
        return True
    if CODE_TOKEN_RE.search(text):
        return True
    if text.startswith(("!", "*", "-", "?", "(", ")", "{", "}", "[", "]", ",", ".")):
        return True

    punctuation = sum(1 for ch in text if ch in "(){}[]=<>`")
    letters = sum(1 for ch in text if ch.isalpha())
    return punctuation >= 3 and letters < max(6, punctuation * 3)


def is_blocked(text: str) -> bool:
    if text in EXACT_BLOCKLIST:
        return True

    lowered = text.lower()
    sentence_like = is_sentence_like(text)
    for phrase in PHRASE_BLOCKLIST:
        if phrase.lower() in lowered:
            return True

    for pattern in REGEX_BLOCKLIST:
        if sentence_like and pattern in CLASSLIKE_PATTERNS:
            continue
        if pattern.search(text):
            return True

    if ":" in text and " " not in text and text not in ALWAYS_INCLUDE:
        return True

    if any(ch in text for ch in ("=", "{", "}", "[", "]")):
        return True
    if looks_like_code_fragment(text):
        return True

    return False


def score_text(module_name: str, text: str) -> int:
    if text in ALWAYS_INCLUDE:
        return 100

    if is_blocked(text):
        return -100

    score = 0
    lowered = text.lower()

    if 3 <= len(text) <= 80:
        score += 2
    if 80 < len(text) <= 140:
        score += 1

    if text[0].isupper():
        score += 2
    if re.search(r"[?.!:]$", text):
        score += 1
    if re.search(r"\b(you|your|project|task|tasks|data|storage|label|settings|workspace|member|template)\b", lowered):
        score += 2
    if re.search(r"\b(create|import|export|delete|save|copy|select|connect|configure|invite|review|label|begin|start|choose)\b", lowered):
        score += 2
    if module_name == "templates":
        score += 2

    for word in BOOST_WORDS:
        if word in lowered:
            score += 1

    words = text.split()
    if 1 <= len(words) <= 12:
        score += 2
    if len(words) > 18:
        score -= 2

    return score


def enrich_entry(module_name: str, entry: dict[str, object]) -> dict[str, object]:
    source = normalize(entry.get("source", ""))
    kinds = [normalize(kind) for kind in entry.get("kinds", []) if normalize(kind)]
    files = [normalize(path) for path in entry.get("files", []) if normalize(path)]
    contexts = [ctx for ctx in entry.get("contexts", []) if ctx]
    occurrences = int(entry.get("occurrences", 1) or 1)
    priority = normalize(entry.get("priority", "low")).lower() or "low"

    score = score_text(module_name, source)
    score += min(max(occurrences - 1, 0), 4)
    score += PRIORITY_SCORES.get(priority, 0)
    for kind in kinds:
        score += KIND_SCORES.get(kind, 0)
    if len(files) > 1:
        score += 1

    return {
        "source": source,
        "target": "",
        "status": "pending",
        "module": module_name,
        "priority": priority,
        "score": score,
        "occurrences": occurrences,
        "kinds": kinds,
        "files": files[:8],
        "contexts": contexts[:6],
    }


def choose_candidates(payload: dict[str, object], *, min_score: int) -> dict[str, list[dict[str, object]]]:
    selected: dict[str, list[dict[str, object]]] = {}
    structured_entries = payload.get("entries", [])

    if structured_entries:
        grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
        for raw_entry in structured_entries:
            module_name = normalize(raw_entry.get("module", "generic")) or "generic"
            if module_name not in MODULE_ORDER:
                module_name = "generic"
            entry = enrich_entry(module_name, raw_entry)
            if entry["source"] and int(entry["score"]) >= min_score:
                grouped[module_name].append(entry)

        for module_name in MODULE_ORDER:
            entries = grouped.get(module_name, [])
            entries.sort(
                key=lambda item: (
                    {"high": 0, "medium": 1, "low": 2}.get(str(item["priority"]), 3),
                    -int(item["score"]),
                    str(item["source"]).lower(),
                )
            )
            if entries:
                selected[module_name] = entries
        return selected

    modules = payload.get("modules", {})
    for module_name in MODULE_ORDER:
        module_payload = modules.get(module_name, {})
        values = module_payload.get("all", [])
        kept: list[dict[str, object]] = []
        seen: set[str] = set()

        for raw in values:
            text = normalize(raw)
            dedupe_key = text.casefold()
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)

            entry = enrich_entry(
                module_name,
                {
                    "source": text,
                    "priority": "high" if text in ALWAYS_INCLUDE else "medium",
                    "occurrences": 1,
                    "kinds": [],
                    "files": [],
                    "contexts": [],
                },
            )
            if int(entry["score"]) >= min_score:
                kept.append(entry)

        if kept:
            selected[module_name] = kept

    return selected


def build_translation_stub(candidates: dict[str, list[dict[str, object]]]) -> dict[str, list[dict[str, object]]]:
    return {module_name: entries for module_name, entries in candidates.items() if entries}


def render_js_stub(stub: dict[str, list[dict[str, str]]]) -> str:
    lines = ["var MODULE_MAPS = {"]
    for index, module_name in enumerate(MODULE_ORDER):
        entries = stub.get(module_name)
        if not entries:
            continue
        if index:
            lines[-1] = lines[-1] + ""
        lines.append(f"  {module_name}: {{")
        for item_index, entry in enumerate(entries):
            source = entry["source"]
            target = entry["target"]
            comma = "," if item_index < len(entries) - 1 else ""
            lines.append(f'    {json.dumps(source, ensure_ascii=False)}: {json.dumps(target, ensure_ascii=False)}{comma}')
        lines.append("  },")
    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("};")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate high-confidence Label Studio overlay dictionary candidates.")
    parser.add_argument("scan_json", help="Path to extracted scan JSON file.")
    parser.add_argument("--output-json", required=True, help="Path to write filtered candidate JSON.")
    parser.add_argument("--output-js", help="Optional path to write a JS MODULE_MAPS stub.")
    parser.add_argument("--min-score", type=int, default=4, help="Minimum score for keeping a candidate.")
    args = parser.parse_args()

    scan_path = Path(args.scan_json).resolve()
    payload = json.loads(scan_path.read_text(encoding="utf-8"))

    candidates = choose_candidates(payload, min_score=args.min_score)
    stub = build_translation_stub(candidates)

    output_json = Path(args.output_json).resolve()
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(
            {
                "meta": {
                    "source": str(scan_path),
                    "min_score": args.min_score,
                    "total_candidates": sum(len(entries) for entries in stub.values()),
                },
                "modules": stub,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
        newline="\n",
    )

    if args.output_js:
        output_js = Path(args.output_js).resolve()
        output_js.parent.mkdir(parents=True, exist_ok=True)
        output_js.write_text(render_js_stub(stub), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
