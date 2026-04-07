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

HIGH_PRIORITY_KEYWORDS = (
    "account",
    "api",
    "cloud",
    "create",
    "data manager",
    "delete",
    "docs",
    "email",
    "export",
    "home",
    "hotkey",
    "import",
    "label",
    "log ",
    "member",
    "password",
    "project",
    "save",
    "setting",
    "storage",
    "submit",
    "token",
    "webhook",
    "workspace",
)

BUILTIN_TERM_MAP = {
    "Access Token": "访问令牌",
    "Account": "账户",
    "Accounts": "账户",
    "Add": "添加",
    "A full-fledged open source solution for data labeling": "一个功能完整的数据标注开源方案",
    "All": "全部",
    "Annotation": "标注",
    "Annotations": "标注",
    "Apply": "应用",
    "Audio Controls": "音频控制",
    "Back": "返回",
    "Back to projects": "返回项目列表",
    "Browser": "浏览器",
    "Cancel": "取消",
    "Check": "检查",
    "Cloud Storage": "云存储",
    "Columns": "列",
    "Color": "颜色",
    "Community": "社区版",
    "Compact": "紧凑",
    "Compact density": "紧凑密度",
    "Comfortable density": "舒适密度",
    "Controls": "控制",
    "Connect": "连接",
    "Continue": "继续",
    "Create": "创建",
    "Create new project": "创建新项目",
    "Copy your new access token from below and keep it secure.": "请从下方复制新的访问令牌并妥善保管。",
    "Current": "当前",
    "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.": "自定义键盘快捷键以提升工作效率。点击下方任意快捷键即可分配更适合您的新组合键。",
    "Cycle Regions": "循环切换区域",
    "Data": "数据",
    "Data Manager": "数据管理",
    "Default": "默认",
    "Delete": "删除",
    "Delete Segment": "删除片段",
    "Decrease Tool Size": "减小工具大小",
    "Density": "密度",
    "Deselect": "取消选择",
    "Description": "描述",
    "Docs": "文档",
    "Documentation": "文档",
    "Download": "下载",
    "E-mail": "邮箱",
    "Edit": "编辑",
    "Edit Region Metadata": "编辑区域元数据",
    "Email": "邮箱",
    "Enterprise": "企业版",
    "Duplicate Region": "复制区域",
    "Exit Region Mode": "退出区域模式",
    "Export": "导出",
    "Extend Left": "向左扩展",
    "Extend Left (Large)": "大幅向左扩展",
    "Extend Right": "向右扩展",
    "Extend Right (Large)": "大幅向右扩展",
    "Filter": "筛选",
    "Filters": "筛选",
    "First": "第一个",
    "First Name": "名字",
    "First Frame": "第一帧",
    "Focus": "聚焦",
    "Focus First Region": "聚焦第一个区域",
    "Full Name": "姓名",
    "Gallery": "图库",
    "Go to Home": "返回首页",
    "Go to": "前往",
    "Great news!": "好消息！",
    "Grid": "网格",
    "Group": "分组",
    "Hop Backward": "快速后退",
    "Hop Forward": "快速前进",
    "Hide": "隐藏",
    "Home": "首页",
    "Hotkeys": "快捷键",
    "Import": "导入",
    "Import your data": "导入数据",
    "Info": "信息",
    "Image": "图片",
    "Image Gallery Navigation": "图库导航",
    "Images": "图片",
    "Increase Tool Size": "增大工具大小",
    "Invite": "邀请",
    "Keep me logged in this browser": "在此浏览器中保持登录",
    "Label": "标注",
    "Labeling": "标注",
    "Labeling Config": "标注配置",
    "Label Studio Version: Community": "Label Studio 版本：社区版",
    "Labels": "标签",
    "Last Name": "姓氏",
    "Last Frame": "最后一帧",
    "Learn more": "了解更多",
    "Light": "浅色",
    "List": "列表",
    "Log in": "登录",
    "Log In": "登录",
    "Log out": "退出登录",
    "Log Out": "退出登录",
    "Lock": "锁定",
    "Lock Region": "锁定区域",
    "Member": "成员",
    "Members": "成员",
    "Menu": "菜单",
    "Move Tool": "移动工具",
    "Next": "下一步",
    "Next Image": "下一张图片",
    "Next Keyframe": "下一个关键帧",
    "Next Phrase": "下一个短语",
    "Next Region in Phrase": "短语中的下一区域",
    "Name": "名称",
    "New": "新建",
    "Open": "打开",
    "Open New Tab": "打开新标签页",
    "(opens in a new tab)": "（在新标签页中打开）",
    "Options": "选项",
    "Organization": "组织",
    "Organizations": "组织",
    "Order by": "排序方式",
    "Pan Image": "平移图像",
    "Paragraph Navigation": "段落导航",
    "Password": "密码",
    "Personal Info": "个人信息",
    "Phone": "电话",
    "Play / Pause Audio": "播放 / 暂停音频",
    "Play / Pause Video": "播放 / 暂停视频",
    "Predictions:": "预测：",
    "Previous": "上一步",
    "Previous Image": "上一张图片",
    "Previous Keyframe": "上一个关键帧",
    "Previous Phrase": "上一个短语",
    "Previous Region in Phrase": "短语中的上一区域",
    "Project": "项目",
    "Projects": "项目",
    "Redis Storage": "Redis 存储",
    "Recent Projects": "最近项目",
    "Redo": "重做",
    "Redo previously undone action": "重做刚刚撤销的操作",
    "Region": "区域",
    "Region Management": "区域管理",
    "Regions": "区域",
    "Remove": "移除",
    "Remove all regions": "删除所有区域",
    "Rectangle Tool": "矩形工具",
    "Resources": "资源",
    "Reset Hotkeys to Defaults?": "要将快捷键恢复为默认设置吗？",
    "Rewind 1 Second": "回退 1 秒",
    "Rotate Left": "向左旋转",
    "Rotate Right": "向右旋转",
    "Save": "保存",
    "Save changes": "保存更改",
    "Save General Settings": "保存常规设置",
    "Search": "搜索",
    "Seek Backward": "向后跳转",
    "Seek Forward": "向前跳转",
    "See docs on importing data": "查看导入数据文档",
    "See all templates": "查看所有模板",
    "Select": "选择",
    "Selected": "所选",
    "Settings": "设置",
    "Show": "显示",
    "Show or hide all regions": "显示或隐藏所有区域",
    "Show or hide the selected region": "显示或隐藏所选区域",
    "Shortcuts for controlling audio playback and navigation": "控制音频播放与导航的快捷方式",
    "Shortcuts for controlling tools panel when labeling images": "标注图像时控制工具面板的快捷方式",
    "Shortcuts for controlling video playback and navigation": "控制视频播放与导航的快捷方式",
    "Shortcuts for navigating between images in multi-image tasks": "在多图任务中切换图片的快捷方式",
    "Shortcuts for navigating phrases and regions in paragraph/dialogue view": "在段落/对话视图中切换短语和区域的快捷方式",
    "Shrink Left": "向左收缩",
    "Shrink Left (Large)": "大幅向左收缩",
    "Shrink Right": "向右收缩",
    "Shrink Right (Large)": "大幅向右收缩",
    "Sign in": "登录",
    "Sign In": "登录",
    "Sign up": "注册",
    "Sign Up": "注册",
    "Sidebar": "侧边栏",
    "Skip": "跳过",
    "Skip Task": "跳过任务",
    "Sort": "排序",
    "Sort descending": "降序排序",
    "Storage": "存储",
    "Step Back": "后退一步",
    "Step Forward": "前进一步",
    "Submitted annotations:": "已提交标注：",
    "Submit": "提交",
    "3-Point Rectangle": "三点矩形",
    "Switch to grid view": "切换到网格视图",
    "Switch to list view": "切换到列表视图",
    "Task": "任务",
    "Tasks:": "任务：",
    "Tasks": "任务",
    "Template": "模板",
    "Templates": "模板",
    "Tab": "标签页",
    "Tab options": "标签页选项",
    "This": "此",
    "Time Series Controls": "时间序列控制",
    "Token": "令牌",
    "Toggle": "切换",
    "Toggle All Region Visibility": "切换所有区域可见性",
    "Toggle Bulk Sidebar": "切换批量操作侧边栏",
    "Toggle Region Visibility": "切换区域可见性",
    "Tool": "工具",
    "Tools": "工具",
    "Try Label Studio Starter Cloud, optimized for small teams and projects.": "试试 Label Studio Starter Cloud，它针对小型团队和项目做了优化。",
    "Undo": "撤销",
    "Undo last action": "撤销上一步操作",
    "Unknown": "未知",
    "Unknown error": "未知错误",
    "Unselect Region": "取消选择区域",
    "Upload": "上传",
    "Upload Image": "上传图片",
    "Version": "版本",
    "Video Controls": "视频控制",
    "View": "视图",
    "View All": "查看全部",
    "Visibility": "可见性",
    "Welcome 👋": "欢迎 👋",
    "Webhooks": "Webhook 回调",
    "Workspace": "工作区",
    "Auto Detect": "自动检测",
    "Brush Tool": "画笔工具",
    "Ellipse Tool": "椭圆工具",
    "Eraser Tool": "橡皮擦工具",
    "Key Point Tool": "关键点工具",
    "Magic Wand": "魔棒工具",
    "Polygon Tool": "多边形工具",
    "Zoom In": "放大",
    "Zoom Out": "缩小",
    "Zoom to 100%": "缩放至 100%",
    "Zoom to Fit": "缩放至适应",
    "Zoom": "缩放",
}

ALLOWED_RESIDUAL_TOKENS = {
    "AI",
    "API",
    "BIO",
    "COCO",
    "CPU",
    "CSV",
    "GCS",
    "GPU",
    "HTML",
    "HTTP",
    "HTTPS",
    "ID",
    "JSON",
    "JPEG",
    "JPG",
    "LLM",
    "ML",
    "NER",
    "OCR",
    "PDF",
    "PNG",
    "RLHF",
    "S3",
    "SDK",
    "UI",
    "URL",
    "VOC",
    "WAV",
    "Webhook",
    "Webhooks",
    "XML",
    "YOLO",
}

CODE_TOKEN_RE = re.compile(
    r"\b(?:const|let|var|function|return|import|export|extends|interface|type|props?|state|async|await|null|undefined)\b"
)


def normalize(text: str) -> str:
    return " ".join(str(text).split()).strip()


def is_placeholder(value: str) -> bool:
    if not value:
        return True
    compact = value.replace(" ", "")
    return bool(re.fullmatch(r"[?？]+", compact) or "??" in compact or "�" in compact)


def normalize_key(text: str) -> str:
    return normalize(text).casefold()


def contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def is_untranslated_target(source: str, target: str) -> bool:
    return normalize_key(source) == normalize_key(target) and not contains_chinese(target)


def looks_like_ui_text(source: str) -> bool:
    if not re.search(r"[A-Za-z]", source):
        return False
    if source.startswith(("\"", "'", "`", "!", "*", "-", "?", "(", ")", "{", "}", "[", "]", ",", ".")):
        return False
    if "`" in source or "=>" in source or "&&" in source or "||" in source or "::" in source:
        return False
    if re.search(r"[;=]{1,}|[?]\s", source):
        return False
    if CODE_TOKEN_RE.search(source):
        return False

    punctuation = sum(1 for ch in source if ch in "(){}[]=<>`")
    letters = sum(1 for ch in source if ch.isalpha())
    return not (punctuation >= 3 and letters < max(6, punctuation * 3))


def load_payload(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_lookup(payload: dict[str, object]) -> dict[str, dict[str, dict[str, str]]]:
    modules = payload.get("modules", {})
    lookup: dict[str, dict[str, dict[str, str]]] = {module: {} for module in MODULE_ORDER}
    lookup["*"] = {}

    for module_name, entries in modules.items():
        for entry in entries:
            source = normalize(entry.get("source", ""))
            target = normalize(entry.get("target", ""))
            if not source or is_placeholder(target) or is_untranslated_target(source, target):
                continue
            record = {
                "target": target,
                "status": normalize(entry.get("status", "approved")).lower() or "approved",
                "translation_source": normalize(entry.get("translation_source", "catalog")) or "catalog",
            }
            lookup.setdefault(module_name, {})[normalize_key(source)] = record
            lookup["*"].setdefault(normalize_key(source), record)

    return lookup


def build_term_map(payload: dict[str, object]) -> dict[str, str]:
    term_map = dict(BUILTIN_TERM_MAP)
    modules = payload.get("modules", {})

    for entries in modules.values():
        for entry in entries:
            source = normalize(entry.get("source", ""))
            target = normalize(entry.get("target", ""))
            if not source or is_placeholder(target) or is_untranslated_target(source, target):
                continue
            if len(source.split()) <= 5 and len(source) <= 48:
                term_map.setdefault(source, target)

    return term_map


def build_auto_translation_rules(term_map: dict[str, str]) -> tuple[dict[str, str], list[tuple[re.Pattern[str], str, str]]]:
    exact_terms: dict[str, str] = {}
    phrase_rules: list[tuple[re.Pattern[str], str, str]] = []

    for raw_source, target in sorted(term_map.items(), key=lambda item: len(normalize(item[0])), reverse=True):
        phrase = normalize(raw_source)
        replacement = normalize(target)
        if not phrase or not replacement:
            continue

        exact_terms.setdefault(phrase, replacement)
        phrase_rules.append(
            (
                re.compile(rf"(?<![A-Za-z]){re.escape(phrase)}(?![A-Za-z])", re.IGNORECASE),
                phrase,
                replacement,
            )
        )

    return exact_terms, phrase_rules


def cleanup_auto_translation(text: str) -> str:
    cleaned = normalize(text)
    cleaned = re.sub(r"\s+([，。！？：；、）】」》])", r"\1", cleaned)
    cleaned = re.sub(r"([（【「《])\s+", r"\1", cleaned)
    cleaned = re.sub(r"([\u4e00-\u9fff])\s+([\u4e00-\u9fff])", r"\1\2", cleaned)
    return cleaned


def has_only_allowed_residual_english(text: str) -> bool:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+/.-]*", text)
    for token in tokens:
        if token in ALLOWED_RESIDUAL_TOKENS:
            continue
        if token.upper() in ALLOWED_RESIDUAL_TOKENS:
            continue
        if len(token) == 1:
            continue
        return False
    return True


def auto_translate(
    source: str,
    exact_terms: dict[str, str],
    phrase_rules: list[tuple[re.Pattern[str], str, str]],
) -> tuple[str, list[str]]:
    normalized_source = normalize(source)
    exact_target = normalize(exact_terms.get(normalized_source, ""))
    if exact_target and contains_chinese(exact_target):
        return cleanup_auto_translation(exact_target), [normalized_source]

    translated = normalized_source
    applied: list[str] = []

    for pattern, phrase, replacement in phrase_rules:
        if pattern.search(translated):
            translated = pattern.sub(replacement, translated)
            applied.append(phrase)

    translated = cleanup_auto_translation(translated)
    if translated == normalized_source:
        return "", []
    if not contains_chinese(translated):
        return "", []
    if not has_only_allowed_residual_english(translated):
        return "", []

    return translated, applied


def is_high_priority(module_name: str, source: str) -> bool:
    if not looks_like_ui_text(source):
        return False
    if module_name != "generic":
        return True
    lowered = source.lower()
    return any(keyword in lowered for keyword in HIGH_PRIORITY_KEYWORDS)


def sync_modules(
    candidates_payload: dict[str, object],
    catalog_payload: dict[str, object],
    catalog_lookup: dict[str, dict[str, dict[str, str]]],
    term_map: dict[str, str],
) -> tuple[dict[str, list[dict[str, object]]], dict[str, list[dict[str, object]]], dict[str, list[dict[str, object]]]]:
    modules = candidates_payload.get("modules", {})
    catalog_modules = catalog_payload.get("modules", {})
    exact_terms, phrase_rules = build_auto_translation_rules(term_map)

    synced: dict[str, list[dict[str, object]]] = OrderedDict()
    missing: dict[str, list[dict[str, object]]] = OrderedDict()
    high_priority: dict[str, list[dict[str, object]]] = OrderedDict()

    for module_name in MODULE_ORDER:
        module_entries = modules.get(module_name, [])
        result_entries: list[dict[str, object]] = []
        module_missing: list[dict[str, object]] = []
        module_high_priority: list[dict[str, object]] = []
        seen: set[str] = set()

        for entry in module_entries:
            source = normalize(entry.get("source", ""))
            if not source:
                continue
            dedupe_key = source.casefold()
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)

            module_record = catalog_lookup.get(module_name, {}).get(normalize_key(source))
            global_record = catalog_lookup["*"].get(normalize_key(source))

            target = ""
            status = "pending"
            translation_source = ""

            if module_record:
                target = normalize(module_record.get("target", ""))
                status = normalize(module_record.get("status", "approved")).lower() or "approved"
                translation_source = normalize(module_record.get("translation_source", "catalog")) or "catalog"
            elif global_record:
                target = normalize(global_record.get("target", ""))
                status = normalize(global_record.get("status", "approved")).lower() or "approved"
                translation_source = normalize(global_record.get("translation_source", "catalog-global")) or "catalog-global"
            else:
                auto_target, applied_terms = auto_translate(source, exact_terms, phrase_rules)
                if auto_target:
                    target = auto_target
                    status = "auto"
                    translation_source = "builtin-terms" if applied_terms else "auto"

            record = {
                "source": source,
                "target": target,
                "status": status,
                "priority": normalize(entry.get("priority", "low")).lower() or "low",
                "score": int(entry.get("score", 0) or 0),
                "occurrences": int(entry.get("occurrences", 1) or 1),
                "kinds": entry.get("kinds", []),
                "files": entry.get("files", []),
                "contexts": entry.get("contexts", []),
                "translation_source": translation_source,
            }
            result_entries.append(record)

            if not record["target"]:
                report_item = {
                    "source": source,
                    "priority": record["priority"],
                    "score": record["score"],
                    "files": record["files"][:5],
                    "contexts": record["contexts"][:3],
                }
                module_missing.append(report_item)
                if is_high_priority(module_name, source):
                    module_high_priority.append(report_item)

        # Keep translated manual entries so runtime overlay can cover UI text
        # that the current source scan did not collect.
        for entry in catalog_modules.get(module_name, []):
            source = normalize(entry.get("source", ""))
            target = normalize(entry.get("target", ""))
            if not source or is_placeholder(target) or is_untranslated_target(source, target):
                continue
            dedupe_key = source.casefold()
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            result_entries.append(
                {
                    "source": source,
                    "target": target,
                    "status": normalize(entry.get("status", "approved")).lower() or "approved",
                    "priority": normalize(entry.get("priority", "low")).lower() or "low",
                    "score": int(entry.get("score", 0) or 0),
                    "occurrences": int(entry.get("occurrences", 1) or 1),
                    "kinds": entry.get("kinds", []),
                    "files": entry.get("files", []),
                    "contexts": entry.get("contexts", []),
                    "translation_source": normalize(entry.get("translation_source", "catalog-manual")) or "catalog-manual",
                }
            )

        if result_entries:
            synced[module_name] = result_entries
        if module_missing:
            missing[module_name] = module_missing
        if module_high_priority:
            high_priority[module_name] = module_high_priority

    return synced, missing, high_priority


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync latest candidate dictionary into the translation catalog.")
    parser.add_argument("candidate_json", help="Path to generated candidate dictionary JSON.")
    parser.add_argument("--catalog", required=True, help="Path to checked-in translation catalog JSON.")
    parser.add_argument("--output-json", required=True, help="Path to write merged translations JSON.")
    parser.add_argument("--missing-report", required=True, help="Path to write all missing translations report.")
    parser.add_argument(
        "--high-priority-report",
        required=True,
        help="Path to write high-priority missing translations report.",
    )
    args = parser.parse_args()

    candidate_path = Path(args.candidate_json).resolve()
    catalog_path = Path(args.catalog).resolve()

    candidates_payload = load_payload(candidate_path)
    catalog_payload = load_payload(catalog_path)
    catalog_lookup = build_lookup(catalog_payload)
    term_map = build_term_map(catalog_payload)

    synced_modules, missing_modules, high_priority_modules = sync_modules(
        candidates_payload,
        catalog_payload,
        catalog_lookup,
        term_map,
    )

    write_json(
        Path(args.output_json).resolve(),
        {
            "meta": {
                "source": str(candidate_path),
                "catalog": str(catalog_path),
                "synced": True,
                "translation_first": True,
            },
            "modules": synced_modules,
        },
    )

    write_json(
        Path(args.missing_report).resolve(),
        {
            "total": sum(len(values) for values in missing_modules.values()),
            "items": [item for values in missing_modules.values() for item in values],
            "modules": missing_modules,
        },
    )

    write_json(
        Path(args.high_priority_report).resolve(),
        {
            "total": sum(len(values) for values in high_priority_modules.values()),
            "items": [item for values in high_priority_modules.values() for item in values],
            "modules": high_priority_modules,
        },
    )


if __name__ == "__main__":
    main()
