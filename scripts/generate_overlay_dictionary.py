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
    "Cloud Storage",
    "Copied!",
    "Create Project",
    "Danger Zone",
    "Data Import",
    "Data Manager",
    "Delete Project",
    "Docs",
    "Drop All Tabs",
    "Email Preferences",
    "Export",
    "Export data",
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
    "Log In",
    "Log Out",
    "Log in",
    "Members",
    "Membership Info",
    "My Account",
    "Optional description of your project",
    "Organization",
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
    "Sign Up",
    "Sign up",
    "Slack Community",
    "Submit",
    "Tools",
    "Webhooks",
    "Workspace",
    "You can export dataset in one of the following formats:",
}

EXACT_BLOCKLIST = {"base.html", "simple.html", "favicon.ico", "history.back()", "location.reload()", "noopener noreferrer"}
PHRASE_BLOCKLIST = (
    "toBe(",
    "describe(",
    "expect(",
    "should ",
    "className",
    "cursor:",
    "display:",
    "margin:",
    "padding:",
    "background=",
    "strokeLinecap",
    "viewBox",
    "rgba(",
    "calc(",
    "lsf-",
    "LabelStudio",
    "Content-Type",
    "Cache-Control",
    "DOMContentLoaded",
)
REGEX_BLOCKLIST = [
    re.compile(r"^#?[0-9A-Fa-f]{3,8}$"),
    re.compile(r"^(ctrl|alt|shift|cmd)\+", re.IGNORECASE),
    re.compile(r"^[#.].+"),
    re.compile(r"^[a-z0-9_.-]+$"),
    re.compile(r"^[A-Z0-9_:-]+$"),
    re.compile(r"^[a-z]+(?:[A-Z][a-z0-9]+)+$"),
    re.compile(r"^\d"),
    re.compile(r"[{}[\]<>]"),
    re.compile(r"\.(svg|png|jpg|jpeg|gif|json|css|scss|tsx|jsx|js|py|md|yml|yaml)$", re.IGNORECASE),
    re.compile(r"^https?://", re.IGNORECASE),
    re.compile(r"\b(?:spec|story|storybook|mock|fixture|snapshot|test)\b", re.IGNORECASE),
    re.compile(r"\b(?:px|rem|em|vh|vw|deg|ms)\b", re.IGNORECASE),
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
    "keyboard",
    "label",
    "learn",
    "member",
    "name",
    "option",
    "password",
    "project",
    "save",
    "select",
    "setting",
    "storage",
    "submit",
    "task",
    "template",
    "token",
    "workspace",
)
KIND_SCORES = {"attributes": 3, "groups": 2, "html": 2, "quoted": 1, "titles": 3}
PRIORITY_SCORES = {"high": 3, "medium": 1, "low": 0}


def normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def is_sentence_like(text: str) -> bool:
    words = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)?", text)
    return len(words) >= 5 and bool(re.search(r"\b(?:a|an|the|for|and|your|you|with|to|of|in|on)\b", text.lower()))


def looks_like_code_fragment(text: str) -> bool:
    if any(token in text for token in ("`", "=>", "&&", "||", "::")):
        return True
    if re.search(r"[;=]{1,}|[?]\s", text):
        return True
    punctuation = sum(1 for ch in text if ch in "(){}[]=<>`")
    letters = sum(1 for ch in text if ch.isalpha())
    return punctuation >= 3 and letters < max(6, punctuation * 3)


def is_blocked(text: str) -> bool:
    if text in EXACT_BLOCKLIST:
        return True
    lowered = text.lower()
    for phrase in PHRASE_BLOCKLIST:
        if phrase.lower() in lowered:
            return True
    for pattern in REGEX_BLOCKLIST:
        if pattern.search(text):
            return True
    if ":" in text and " " not in text and text not in ALWAYS_INCLUDE:
        return True
    if any(ch in text for ch in ("=", "{", "}", "[", "]")) or looks_like_code_fragment(text):
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
    elif len(text) <= 140:
        score += 1
    if text[:1].isupper():
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
    source = normalize(str(entry.get("source", "")))
    kinds = [normalize(str(kind)) for kind in entry.get("kinds", []) if normalize(str(kind))]
    files = [normalize(str(path)) for path in entry.get("files", []) if normalize(str(path))]
    contexts = [ctx for ctx in entry.get("contexts", []) if ctx]
    occurrences = int(entry.get("occurrences", 1) or 1)
    priority = normalize(str(entry.get("priority", "low"))).lower() or "low"
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
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for raw_entry in payload.get("entries", []):
        module_name = normalize(str(raw_entry.get("module", "generic"))) or "generic"
        if module_name not in MODULE_ORDER:
            module_name = "generic"
        entry = enrich_entry(module_name, raw_entry)
        if entry["source"] and int(entry["score"]) >= min_score:
            grouped[module_name].append(entry)
    selected: dict[str, list[dict[str, object]]] = {}
    for module_name in MODULE_ORDER:
        entries = grouped.get(module_name, [])
        entries.sort(key=lambda item: ({"high": 0, "medium": 1, "low": 2}.get(str(item["priority"]), 3), -int(item["score"]), str(item["source"]).lower()))
        if entries:
            selected[module_name] = entries
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate high-confidence Label Studio overlay dictionary candidates.")
    parser.add_argument("scan_json", help="Path to extracted scan JSON file.")
    parser.add_argument("--output-json", required=True, help="Path to write filtered candidate JSON.")
    parser.add_argument("--min-score", type=int, default=4, help="Minimum score for keeping a candidate.")
    args = parser.parse_args()
    payload = json.loads(Path(args.scan_json).read_text(encoding="utf-8"))
    candidates = choose_candidates(payload, min_score=args.min_score)
    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps({"meta": {"source": str(Path(args.scan_json).resolve()), "min_score": args.min_score, "total_candidates": sum(len(entries) for entries in candidates.values())}, "modules": candidates}, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
