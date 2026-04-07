#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


TEXT_FILE_SUFFIXES = {".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".yml", ".yaml"}
SKIP_DIR_NAMES = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".next",
    ".cache",
    "coverage",
}

TITLE_RE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)
GROUP_RE = re.compile(r"^group:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)
QUOTED_RE = re.compile(r"""(?P<q>["'])(?P<text>[^"'\\\n][^\\\n]{1,160}?)(?P=q)""")
TAG_TEXT_RE = re.compile(r">([^<>{}\n][^<>{}]{1,160}?)<")
ATTR_RE = re.compile(
    r"""(?:placeholder|title|aria-label|label|description|helpText|tooltip|emptyMessage|caption|heading|text)\s*[:=]\s*(?P<q>["'])(?P<text>[^"'\\\n][^\\\n]{1,160}?)(?P=q)"""
)
MODULE_RULES = [
    ("auth", ("users", "login", "signup", "sign-up", "sign_in", "sign-in", "password", "account")),
    ("home", ("home", "dashboard", "welcome", "starter", "empty-state", "empty_state", "onboarding")),
    ("projects", ("projects", "project", "createproject", "projectlist")),
    ("import_export", ("import", "export", "upload", "download")),
    ("data_manager", ("data_manager", "datamanager", "tasksummary", "taskstore", "tasks")),
    ("labeling", ("annotation", "annotations", "labeling", "region", "relation", "predictions", "draft")),
    ("settings", ("settings", "preferences", "hotkeys", "accountsettings", "generalsettings")),
    ("organization", ("organizations", "organization", "members", "people", "workspace", "invite")),
    ("storage", ("storage", "storages", "io_storages", "cloud", "localfiles")),
    ("webhooks", ("webhooks", "webhook")),
    ("templates", ("annotation_templates", "template")),
]


def should_keep(text: str) -> bool:
    text = " ".join(text.split()).strip()
    if len(text) < 3:
        return False
    if text.startswith(("/", "$", "{", "http://", "https://", "data:")):
        return False
    if re.search(r"[{}\[\]<>]", text):
        return False
    if re.search(r"[/\\@]", text):
        return False
    if re.search(r"\.(svg|png|jpg|jpeg|gif|json|scss|css|tsx|ts|jsx|js|py|md|yml|yaml)$", text, re.IGNORECASE):
        return False
    if re.fullmatch(r"[\W\d_]+", text):
        return False
    if not re.search(r"[A-Za-z]", text):
        return False
    return True


def normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def detect_module(path: Path) -> str:
    lowered = "/".join(part.lower() for part in path.parts)
    for module_name, markers in MODULE_RULES:
        if any(marker in lowered for marker in markers):
            return module_name
    return "generic"


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_FILE_SUFFIXES:
            continue
        yield path


def add_value(bucket: dict[str, set[str]], key: str, value: str) -> None:
    if should_keep(value):
        bucket[key].add(value)


def add_module_value(module_bucket: dict[str, dict[str, set[str]]], module_name: str, kind: str, value: str) -> None:
    if should_keep(value):
        module_bucket[module_name][kind].add(value)


def extract_annotation_templates(
    root: Path,
    bucket: dict[str, set[str]],
    module_bucket: dict[str, dict[str, set[str]]],
) -> None:
    templates_root = root / "label_studio" / "annotation_templates"
    if not templates_root.exists():
        return

    for config_path in templates_root.rglob("config.y*ml"):
        text = config_path.read_text(encoding="utf-8", errors="ignore")
        for match in TITLE_RE.finditer(text):
            value = normalize(match.group(1))
            add_value(bucket, "template_titles", value)
            add_module_value(module_bucket, "templates", "titles", value)
        for match in GROUP_RE.finditer(text):
            value = normalize(match.group(1))
            add_value(bucket, "template_groups", value)
            add_module_value(module_bucket, "templates", "groups", value)


def extract_candidate_strings(
    root: Path,
    bucket: dict[str, set[str]],
    module_bucket: dict[str, dict[str, set[str]]],
) -> None:
    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        module_name = detect_module(path)

        for match in QUOTED_RE.finditer(text):
            value = normalize(match.group("text"))
            add_value(bucket, "candidate_strings", value)
            add_module_value(module_bucket, module_name, "quoted", value)

        for match in ATTR_RE.finditer(text):
            value = normalize(match.group("text"))
            add_value(bucket, "attribute_text", value)
            add_module_value(module_bucket, module_name, "attributes", value)

        if path.suffix.lower() in {".html", ".htm"}:
            for match in TAG_TEXT_RE.finditer(text):
                value = normalize(match.group(1))
                add_value(bucket, "html_text", value)
                add_module_value(module_bucket, module_name, "html", value)


def build_output(
    bucket: dict[str, set[str]],
    module_bucket: dict[str, dict[str, set[str]]],
) -> dict[str, object]:
    output: dict[str, list[str]] = {}
    for key, values in bucket.items():
        output[key] = sorted(values, key=lambda s: s.lower())

    all_strings = set()
    for values in bucket.values():
        all_strings.update(values)

    modules_output: dict[str, dict[str, list[str]]] = {}
    for module_name, parts in module_bucket.items():
        module_values = set()
        serialized_parts: dict[str, list[str]] = {}
        for part_name, part_values in parts.items():
            sorted_values = sorted(part_values, key=lambda s: s.lower())
            serialized_parts[part_name] = sorted_values
            module_values.update(part_values)
        serialized_parts["all"] = sorted(module_values, key=lambda s: s.lower())
        modules_output[module_name] = serialized_parts

    return {
        "all_strings": sorted(all_strings, key=lambda s: s.lower()),
        "template_groups": output.get("template_groups", []),
        "template_titles": output.get("template_titles", []),
        "candidate_strings": output.get("candidate_strings", []),
        "attribute_text": output.get("attribute_text", []),
        "html_text": output.get("html_text", []),
        "modules": modules_output,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Label Studio UI strings from source code.")
    parser.add_argument("source_root", help="Label Studio source root, e.g. label-studio-1.23.0")
    parser.add_argument(
        "--output",
        help="Write extracted strings to JSON file. Defaults to stdout.",
    )
    args = parser.parse_args()

    root = Path(args.source_root).resolve()
    if not root.exists():
        raise SystemExit(f"source root not found: {root}")

    bucket: dict[str, set[str]] = defaultdict(set)
    module_bucket: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    extract_annotation_templates(root, bucket, module_bucket)
    extract_candidate_strings(root, bucket, module_bucket)

    payload = build_output(bucket, module_bucket)

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
