#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path


FOCUS_AREAS = OrderedDict(
    {
        "login": {
            "required_phrases": [
                "A full-fledged open source solution for data labeling",
                "Log in",
                "Keep me logged in this browser",
                "Sign up",
            ],
            "file_markers": [
                "user_login",
                "user_base",
                "signup",
                "users/templates/users",
            ],
        },
        "home": {
            "required_phrases": [
                "Welcome 👋",
                "Recent Projects",
                "View All",
                "Resources",
                "Label Studio Version: Community",
            ],
            "modules": ["home"],
            "file_markers": ["homepage", "home/"],
        },
        "data_manager": {
            "required_phrases": [
                "Columns",
                "Filters",
                "Order by",
                "Comfortable density",
                "Switch to list view",
                "Switch to grid view",
            ],
            "modules": ["data_manager"],
            "file_markers": ["datamanager", "data_manager"],
        },
        "project_settings": {
            "required_phrases": [
                "Save General Settings",
                "Webhooks",
                "Color",
            ],
            "file_markers": [
                "projectsettings",
                "generalsettings",
                "projects/",
                "webhooks",
            ],
        },
        "account_settings": {
            "required_phrases": [
                "Upload Image",
                "E-mail",
                "Phone",
            ],
            "file_markers": [
                "personal-info",
                "email-preferences",
                "membership-info",
                "accountsettings/sections",
            ],
        },
        "hotkeys": {
            "required_phrases": [
                "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.",
                "Tools",
                "Shortcuts for controlling audio playback and navigation",
                "Shortcuts for controlling video playback and navigation",
                "Shortcuts for navigating between images in multi-image tasks",
                "Shortcuts for navigating phrases and regions in paragraph/dialogue view",
            ],
            "file_markers": [
                "hotkeys",
                "usehotkeys",
                "hotkeysmanager",
                "accountsettings",
            ],
        },
    }
)


def normalize(text: str) -> str:
    return " ".join(str(text).split()).strip()


def normalize_key(text: str) -> str:
    return normalize(text).casefold()


def contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def is_placeholder(value: str) -> bool:
    if not value:
        return True
    compact = value.replace(" ", "")
    return bool(re.fullmatch(r"[?？]+", compact) or "??" in compact or "�" in compact)


def is_effectively_translated(source: str, target: str) -> bool:
    if is_placeholder(target):
        return False
    if contains_chinese(target):
        return True
    return normalize_key(source) != normalize_key(target)


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_translation_entries(payload: dict[str, object]) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    for module_name, module_entries in payload.get("modules", {}).items():
        for entry in module_entries:
            item = dict(entry)
            item.setdefault("module", module_name)
            entries.append(item)
    return entries


def flatten_report_items(payload: dict[str, object]) -> list[dict[str, object]]:
    if isinstance(payload.get("items"), list):
        return [dict(item) for item in payload["items"]]

    items: list[dict[str, object]] = []
    for module_name, module_entries in payload.get("modules", {}).items():
        for entry in module_entries:
            item = dict(entry)
            item.setdefault("module", module_name)
            items.append(item)
    return items


def entry_files(entry: dict[str, object]) -> list[str]:
    files = [normalize(path) for path in entry.get("files", []) if normalize(path)]
    for context in entry.get("contexts", []) or []:
        file_name = normalize(context.get("file", ""))
        if file_name and file_name not in files:
            files.append(file_name)
    return files


def matches_area(area: dict[str, object], entry: dict[str, object]) -> bool:
    source = normalize(entry.get("source", ""))
    if not source:
        return False

    required_keys = {normalize_key(text) for text in area.get("required_phrases", [])}
    if normalize_key(source) in required_keys:
        return True

    files_blob = " ".join(path.lower() for path in entry_files(entry))
    file_markers = area.get("file_markers", [])
    if file_markers and any(marker.lower() in files_blob for marker in file_markers):
        return True

    modules = area.get("modules", [])
    module_name = normalize(entry.get("module", "")).lower()
    if modules and module_name in {name.lower() for name in modules}:
        return True

    return False


def build_required_report(
    required_phrases: list[str],
    translations_index: dict[str, dict[str, object]],
) -> tuple[list[dict[str, object]], list[str]]:
    required: list[dict[str, object]] = []
    missing: list[str] = []

    for phrase in required_phrases:
        record = translations_index.get(normalize_key(phrase), {})
        target = normalize(record.get("target", ""))
        translated = bool(record) and is_effectively_translated(phrase, target)
        required.append(
            {
                "source": phrase,
                "target": target,
                "translated": translated,
                "status": normalize(record.get("status", "")),
                "translation_source": normalize(record.get("translation_source", "")),
            }
        )
        if not translated:
            missing.append(phrase)

    return required, missing


def summarize_items(area: dict[str, object], items: list[dict[str, object]]) -> list[dict[str, object]]:
    matched = [item for item in items if matches_area(area, item)]
    matched.sort(key=lambda item: (-int(item.get("score", 0) or 0), normalize(item.get("source", ""))))

    summary: list[dict[str, object]] = []
    for item in matched[:12]:
        summary.append(
            {
                "source": normalize(item.get("source", "")),
                "priority": normalize(item.get("priority", "")),
                "score": int(item.get("score", 0) or 0),
                "files": entry_files(item)[:4],
            }
        )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit overlay coverage for key Label Studio pages.")
    parser.add_argument(
        "--translations-json",
        default=".tmp/label-studio-1.23.0-translations.json",
        help="Path to merged translations JSON.",
    )
    parser.add_argument(
        "--high-priority-report",
        default=".tmp/label-studio-1.23.0-high-priority-missing.json",
        help="Path to high-priority missing report.",
    )
    parser.add_argument(
        "--untranslated-report",
        default=".tmp/label-studio-1.23.0-untranslated-overlay.json",
        help="Path to untranslated runtime report.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write JSON report. Defaults to stdout.",
    )
    args = parser.parse_args()

    translations_path = Path(args.translations_json).resolve()
    high_priority_path = Path(args.high_priority_report).resolve()
    untranslated_path = Path(args.untranslated_report).resolve()

    translations_payload = load_json(translations_path)
    high_priority_payload = load_json(high_priority_path)
    untranslated_payload = load_json(untranslated_path)

    translation_entries = flatten_translation_entries(translations_payload)
    translations_index = {
        normalize_key(entry.get("source", "")): entry
        for entry in translation_entries
        if normalize(entry.get("source", ""))
    }
    high_priority_items = flatten_report_items(high_priority_payload)
    untranslated_items = flatten_report_items(untranslated_payload)

    areas_report: OrderedDict[str, dict[str, object]] = OrderedDict()
    required_gap_areas: list[str] = []
    residual_gap_areas: list[str] = []

    for area_name, area in FOCUS_AREAS.items():
        required, missing_required = build_required_report(area["required_phrases"], translations_index)
        high_priority_missing = summarize_items(area, high_priority_items)
        runtime_untranslated = summarize_items(area, untranslated_items)
        ready = not missing_required and not high_priority_missing

        if missing_required:
            required_gap_areas.append(area_name)
        if high_priority_missing or runtime_untranslated:
            residual_gap_areas.append(area_name)

        areas_report[area_name] = {
            "ready": ready,
            "required_total": len(required),
            "required_translated": len(required) - len(missing_required),
            "missing_required": missing_required,
            "required_checks": required,
            "high_priority_missing": high_priority_missing,
            "runtime_untranslated": runtime_untranslated,
        }

    payload = {
        "meta": {
            "translations": str(translations_path),
            "high_priority_report": str(high_priority_path),
            "untranslated_report": str(untranslated_path),
        },
        "summary": {
            "focus_area_total": len(FOCUS_AREAS),
            "areas_with_required_gaps": required_gap_areas,
            "areas_with_residual_english": residual_gap_areas,
            "all_focus_areas_ready": not required_gap_areas and not residual_gap_areas,
        },
        "areas": areas_report,
    }

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
