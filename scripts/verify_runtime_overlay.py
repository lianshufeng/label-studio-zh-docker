#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


FOCUS_AREAS = {
    "login": {
        "required": [
            "A full-fledged open source solution for data labeling",
            "Log in",
            "Keep me logged in this browser",
            "Sign up",
        ],
        "match": ["login", "signup", "user_login", "user_signup"],
    },
    "home": {
        "required": ["Home", "Projects", "Create Project"],
        "match": ["home", "dashboard", "projects"],
    },
    "data_manager": {
        "required": ["Data Manager", "Import", "Export"],
        "match": ["data_manager", "task", "tasks"],
    },
    "project_settings": {
        "required": ["Settings", "Labeling Setup", "Save and Leave"],
        "match": ["settings", "project"],
    },
    "account_settings": {
        "required": ["My Account", "Access Token", "Personal Access Token"],
        "match": ["accountsettings", "account", "token"],
    },
    "hotkeys": {
        "required": ["Hotkeys", "Tools"],
        "match": ["hotkeys", "keyboard", "shortcut"],
    },
}


def normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def build_translation_lookup(payload: dict[str, object]) -> dict[str, dict[str, object]]:
    lookup: dict[str, dict[str, object]] = {}
    for entries in payload.get("modules", {}).values():
        for entry in entries:
            source = normalize(str(entry.get("source", "")))
            if source:
                lookup[source.casefold()] = entry
    return lookup


def matches_area(item: dict[str, object], markers: list[str]) -> bool:
    haystacks = [str(item.get("source", "")).lower()]
    haystacks.extend(str(path).lower() for path in item.get("files", []))
    combined = " ".join(haystacks)
    return any(marker in combined for marker in markers)


def summarize_area(spec: dict[str, object], translation_lookup: dict[str, dict[str, object]], high_priority_items: list[dict[str, object]], untranslated_items: list[dict[str, object]]) -> dict[str, object]:
    required_checks = []
    missing_required = []
    translated_count = 0
    for source in spec["required"]:
        entry = translation_lookup.get(source.casefold())
        translated = bool(entry and entry.get("status") == "approved" and normalize(str(entry.get("target", ""))))
        if translated:
            translated_count += 1
        else:
            missing_required.append(source)
        required_checks.append(
            {
                "source": source,
                "target": entry.get("target", "") if entry else "",
                "translated": translated,
                "status": entry.get("status", "missing") if entry else "missing",
                "translation_source": entry.get("translation_source", "") if entry else "",
            }
        )
    high_priority_missing = [item for item in high_priority_items if matches_area(item, spec["match"])]
    runtime_untranslated = [item for item in untranslated_items if matches_area(item, spec["match"])]
    return {
        "ready": not missing_required and not high_priority_missing,
        "required_total": len(spec["required"]),
        "required_translated": translated_count,
        "missing_required": missing_required,
        "required_checks": required_checks,
        "high_priority_missing": high_priority_missing[:50],
        "runtime_untranslated": runtime_untranslated[:50],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify runtime overlay coverage for focus areas.")
    parser.add_argument("--translations-json", required=True, help="Merged translations JSON.")
    parser.add_argument("--high-priority-report", required=True, help="High priority missing JSON.")
    parser.add_argument("--untranslated-report", required=True, help="Runtime untranslated JSON.")
    parser.add_argument("--output", required=True, help="Coverage report output JSON.")
    args = parser.parse_args()

    translations = json.loads(Path(args.translations_json).read_text(encoding="utf-8"))
    high_priority = json.loads(Path(args.high_priority_report).read_text(encoding="utf-8"))
    untranslated = json.loads(Path(args.untranslated_report).read_text(encoding="utf-8"))
    translation_lookup = build_translation_lookup(translations)

    areas = {
        name: summarize_area(spec, translation_lookup, high_priority.get("items", []), untranslated.get("items", []))
        for name, spec in FOCUS_AREAS.items()
    }
    areas_with_required_gaps = [name for name, area in areas.items() if area["missing_required"]]
    areas_with_residual_english = [name for name, area in areas.items() if area["runtime_untranslated"]]
    payload = {
        "meta": {
            "translations": str(Path(args.translations_json).resolve()),
            "high_priority_report": str(Path(args.high_priority_report).resolve()),
            "untranslated_report": str(Path(args.untranslated_report).resolve()),
        },
        "summary": {
            "focus_area_total": len(FOCUS_AREAS),
            "areas_with_required_gaps": areas_with_required_gaps,
            "areas_with_residual_english": areas_with_residual_english,
            "all_focus_areas_ready": not areas_with_required_gaps and not areas_with_residual_english,
        },
        "areas": areas,
    }
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
