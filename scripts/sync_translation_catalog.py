#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BUILTIN_TERMS = {
    "A full-fledged open source solution for data labeling": "一个功能完整的数据标注开源方案",
    "Access Token": "访问令牌",
    "Add Source Storage": "添加源存储",
    "Add Target Storage": "添加目标存储",
    "Add URL": "添加 URL",
    "Add Webhook": "添加 Webhook",
    "Add your first cloud storage": "添加你的第一个云存储",
    "Add your first webhook": "添加你的第一个 Webhook",
    "Account & Settings": "账户与设置",
    "Account Settings": "账户设置",
    "API Documentation": "API 文档",
    "Available on Label Studio Enterprise": "Label Studio 企业版可用",
    "Account Key": "账户密钥",
    "API Tokens Settings": "API 令牌设置",
    "ASR Hypotheses Selection": "ASR 假设选择",
    "Activity Recognition": "活动识别",
    "Add filter for long list of labels": "为长标签列表添加筛选",
    "Add label names": "添加标签名称",
    "Add labels": "添加标签",
    "Add machine learning model": "添加机器学习模型",
    "Add storage": "添加存储",
    "Add any notes or edge cases...": "添加任何备注或边界情况...",
    "All hotkeys and settings have been reset to defaults and saved": "所有快捷键和设置都已重置为默认值并保存",
    "Allows continuous region creation using the selected label": "允许使用所选标签连续创建区域",
    "Amazon S3 with IAM Role is available in Label Studio Enterprise.": "带 IAM Role 的 Amazon S3 在 Label Studio 企业版中可用。",
    "Annotations completed by you": "由你完成的标注",
    "Apply your AWS spend to Label Studio Enterprise": "将你的 AWS 承诺消费用于 Label Studio 企业版",
    "Assign roles to your team using Label Studio Enterprise and control access to sensitive data at the project and workspace levels.": "使用 Label Studio 企业版为团队分配角色，并在项目和工作区级别控制对敏感数据的访问。",
    "Auto-Label Tasks": "自动标注任务",
    "Automatic Speech Recognition": "自动语音识别",
    "Automatic Speech Recognition using Segments": "使用片段的自动语音识别",
    "Automatically selects newly created regions": "自动选择新创建的区域",
    "Azure Blob Storage": "Azure Blob 存储",
    "Azure Blob Storage with Service Principal is available in Label Studio Enterprise.": "带 Service Principal 的 Azure Blob 存储在 Label Studio 企业版中可用。",
    "Back to projects": "返回项目",
    "Before you can annotate the data, set up labeling configuration": "在标注数据前，请先设置标注配置",
    "Cancel": "取消",
    "Cancel project creation": "取消项目创建",
    "Can't find an export format?": "找不到导出格式？",
    "Check your storage settings. You may need to recreate this dataset": "请检查你的存储设置。你可能需要重新创建此数据集",
    "Choose a dataset from your computer to get started": "从你的电脑选择一个数据集以开始使用",
    "Choose how to interpret your data from storage": "选择如何解析来自存储的数据",
    "Choose your cloud storage provider": "选择你的云存储提供商",
    "Cloud Storage": "云存储",
    "Cloud Storage documentation (opens in a new tab)": "云存储文档（在新标签页中打开）",
    "Configure Import Settings & Preview Data": "配置导入设置并预览数据",
    "Configure data": "配置数据",
    "Configure settings": "配置设置",
    "Configure your AWS S3 connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 AWS S3 连接",
    "Configure your Azure Blob Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Azure Blob 存储连接",
    "Configure your Azure Blob Storage connection using Service Principal authentication for enhanced security (proxy only)": "使用 Service Principal 身份验证配置你的 Azure Blob 存储连接以增强安全性（仅代理）",
    "Configure your Databricks Unity Catalog Volumes connection with all required settings (proxy only)": "使用所有必需设置配置你的 Databricks Unity Catalog Volumes 连接（仅代理）",
    "Configure your Google Cloud Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Google Cloud Storage 连接",
    "Configure your Google Cloud Storage connection with Workload Identity Federation authentication (proxy only)": "使用 Workload Identity Federation 身份验证配置你的 Google Cloud Storage 连接（仅代理）",
    "Configure your local file storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的本地文件存储连接",
    "Configure your Redis storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Redis 存储连接",
    "Connect Cloud Storage": "连接云存储",
    "Connect your cloud storage or upload files from your computer": "连接你的云存储或从电脑上传文件",
    "Copied!": "已复制！",
    "Create a Model": "创建模型",
    "Create Account": "创建账户",
    "Create a copy of the selected region": "创建所选区域的副本",
    "Create a relation between selected regions": "在所选区域之间创建关系",
    "Create custom template": "创建自定义模板",
    "Create Region Relation": "创建区域关系",
    "Create one and start labeling your data.": "创建一个并开始标注你的数据。",
    "Create Project": "创建项目",
    "Create your first project": "创建你的第一个项目",
    "Data Manager": "数据管理",
    "Database Number (db)": "数据库编号（db）",
    "Dataset URL": "数据集 URL",
    "If the Data Manager is not loading, dropping all Data Manager tabs can help.": "如果数据管理未加载，清空所有数据管理标签页可能会有所帮助。",
    "Databricks Files (UC Volumes) is available in Label Studio Enterprise.": "Databricks Files（UC Volumes）在 Label Studio 企业版中可用。",
    "Danger Zone": "危险区域",
    "Delete All Regions": "删除所有区域",
    "Delete ML Backend": "删除机器学习后端",
    "Delete Project": "删除项目",
    "Deleting a project removes all tasks, annotations, and project data from the database.": "删除项目会从数据库中移除所有任务、标注和项目数据。",
    "Delete Selected Region": "删除所选区域",
    "Delete Segment": "删除片段",
    "Deleting storage": "正在删除存储",
    "Delete currently selected region": "删除当前选中的区域",
    "Delete selected segment": "删除所选片段",
    "Did you know?": "你知道吗？",
    "Display labels:": "显示标签：",
    "Display region label names": "显示区域标签名称",
    "Docs": "文档",
    "Documentation": "文档",
    "Drop All Tabs": "清空所有标签页",
    "E-mail": "电子邮箱",
    "Edit": "编辑",
    "Edit metadata for selected region": "编辑所选区域元数据",
    "Edit Region Metadata": "编辑区域元数据",
    "Enable increased token authentication security": "启用增强的令牌认证安全性",
    "Enable labeling hotkeys": "启用标注快捷键",
    "Enable legacy access tokens, these do not expire": "启用旧版访问令牌，这些令牌不会过期",
    "Enables quick selection of labels using hotkeys": "支持使用快捷键快速选择标签",
    "Email Preferences": "邮件偏好",
    "Enterprise Feature": "企业版功能",
    "Enterprise feature - Available in Label Studio Enterprise": "企业版功能，Label Studio 企业版可用",
    "Error occurred while loading data": "加载数据时发生错误",
    "Error occurred when loading data": "加载数据时发生错误",
    "Error loading settings.": "加载设置时出错。",
    "Failed to load data": "加载数据失败",
    "Failed to save imported hotkeys": "保存导入的快捷键失败",
    "Files to import": "要导入的文件",
    "Finish import": "完成导入",
    "Export": "导出",
    "Export data": "导出数据",
    "First Name": "名",
    "Freeform Metadata": "自由格式元数据",
    "Google Project ID": "Google 项目 ID",
    "Google Cloud Storage": "Google Cloud Storage",
    "Google Cloud Storage with Workload Identity Federation is available in Label Studio Enterprise.": "带 Workload Identity Federation 的 Google Cloud Storage 在 Label Studio 企业版中可用。",
    "Great news!": "好消息！",
    "Grid settings": "网格设置",
    "Group by Label": "按标签分组",
    "Go Back": "返回",
    "Go to Home": "前往首页",
    "Home": "首页",
    "Heidi doesn't see any projects here!": "Heidi 在这里没有看到任何项目！",
    "How did you hear about Label Studio?": "你是如何了解到 Label Studio 的？",
    "It looks like your team is growing!": "看起来你的团队正在壮大！",
    "Human Signal Logo": "Human Signal 标志",
    "Hotkeys": "快捷键",
    "Import Data": "导入数据",
    "Import data to get your project started": "导入数据以开始你的项目",
    "Import": "导入",
    "import preannotated data": "导入预标注数据",
    "Import your data": "导入你的数据",
    "Import your data and set up the labeling interface to start annotating": "导入数据并设置标注界面以开始标注",
    "Import your data from cloud storage providers": "从云存储提供商导入你的数据",
    "Invite Members": "邀请成员",
    "Keypoint Labeling": "关键点标注",
    "Keep me logged in this browser": "在此浏览器中保持登录",
    "Label": "标签",
    "Label All Tasks": "标注所有任务",
    "Label Studio": "Label Studio",
    "Label Studio Enterprise": "Label Studio 企业版",
    "Label Studio Logo": "Label Studio 标志",
    "Label Studio Playground": "Label Studio Playground",
    "Label Studio Version: Community": "Label Studio 版本：社区版",
    "Label Tasks As Displayed": "按显示顺序标注任务",
    "Label the video:": "标注视频：",
    "Label timeline spans:": "标注时间片段：",
    "Labels": "标签",
    "Labeling Setup": "标注设置",
    "Labeling": "标注",
    "Labeling hotkeys": "标注快捷键",
    "Labeling Interface Settings": "标注界面设置",
    "Labeling Instructions": "标注说明",
    "LabelStud.io Blog": "LabelStud.io 博客",
    "Learn more": "了解更多",
    "Learn, explore and get help": "学习、探索并获取帮助",
    "Learn more about machine learning models (opens in new window)": "了解更多机器学习模型（在新窗口中打开）",
    "Learn more about cloud storage (opens in new window)": "了解更多云存储信息（在新窗口中打开）",
    "Learn more about cloud storage troubleshooting": "了解更多云存储故障排查信息",
    "Learn more about video format support (opens in a new tab)": "了解更多视频格式支持信息（在新标签页中打开）",
    "Last Name": "姓",
    "Last Activity": "最后活动时间",
    "Legacy Tokens": "旧版令牌",
    "Light": "浅色",
    "Local Storage documentation": "本地存储文档",
    "Log In": "登录",
    "Log Out": "退出登录",
    "Log in": "登录",
    "Membership Info": "成员信息",
    "Model Settings": "模型设置",
    "Multi-image labeling documentation (opens in a new tab)": "多图标注文档（在新标签页中打开）",
    "Multi-page document annotation": "多页文档标注",
    "My Account": "我的账户",
    "Named Entity Recognition": "命名实体识别",
    "No data available": "没有可用数据",
    "No predictions uploaded yet": "尚未上传任何预测结果",
    "No sample task data available.": "没有可用的示例任务数据。",
    "No tasks available for review or labeling": "没有可供审核或标注的任务",
    "OCR Labeling for PDFs": "PDF OCR 标注",
    "Optional description of your project": "项目可选描述",
    "Organization": "组织",
    "Personal Access Token": "个人访问令牌",
    "Personal Access Tokens": "个人访问令牌",
    "Personal Info": "个人信息",
    "People": "成员",
    "Perform these actions at your own risk. Actions you take on this page can't be reverted. Make sure your data is backed up.": "执行这些操作需自行承担风险。你在此页面执行的操作无法撤销。请先确认你的数据已备份。",
    "Playback Settings": "播放设置",
    "Please enter JSON data to import": "请输入要导入的 JSON 数据",
    "Polygon labeling": "多边形标注",
    "Predictions Settings": "预测设置",
    "Project Name": "项目名称",
    "Project options": "项目选项",
    "Project has been deleted or not yet created.": "项目已被删除或尚未创建。",
    "Project was deleted or not yet created": "项目已被删除或尚未创建",
    "Projects": "项目",
    "Read more about supported export formats in the Documentation.": "在文档中了解更多支持的导出格式。",
    "Redis Storage": "Redis 存储",
    "Refresh data": "刷新数据",
    "Remember Selected Tool": "记住所选工具",
    "Release Notes": "发布说明",
    "Resources": "资源",
    "Reset Cache": "重置缓存",
    "Reset Hotkeys to Defaults?": "将快捷键重置为默认值？",
    "Response Selection": "响应选择",
    "Saved!": "已保存！",
    "Save and Leave": "保存并离开",
    "Save changes": "保存更改",
    "Save configuration": "保存配置",
    "Save machine learning form": "保存机器学习表单",
    "Save machine learning settings": "保存机器学习设置",
    "Sample config to label with bboxes": "用于框选标注的示例配置",
    "See all templates": "查看所有模板",
    "See docs on importing data": "查看导入数据文档",
    "Select an option": "选择一个选项",
    "Select label and click on image to start": "选择标签并点击图像开始",
    "Select label and click the image to start": "选择标签并点击图像开始",
    "Select all text in current phrase and create annotation": "选择当前短语中的全部文本并创建标注",
    "Session token (optional)": "会话令牌（可选）",
    "Session Token": "会话令牌",
    "Settings": "设置",
    "Sign Up": "注册",
    "Sign up": "注册",
    "Skip": "跳过",
    "Shortcuts for common annotation tasks like submit, skip, undo and redo": "用于提交、跳过、撤销和重做等常见标注任务的快捷键",
    "Shortcuts for controlling tools panel when labeling images": "标注图像时控制工具面板的快捷键",
    "Shortcuts for manipulating time series data regions": "操作时间序列数据区域的快捷键",
    "Shortcuts for navigating and managing tasks in Project's Data Manager": "在项目数据管理中导航和管理任务的快捷键",
    "Show hotkeys on labels": "在标签上显示快捷键",
    "Show labels hotkey tooltips": "显示标签快捷键提示",
    "Show labels inside the regions": "在区域内部显示标签",
    "Show region labels": "显示区域标签",
    "Simplify project management by organizing projects into workspaces.": "通过将项目组织到工作区中来简化项目管理。",
    "Slack Community": "Slack 社区",
    "Source Cloud Storage": "源云存储",
    "Spectrogram Settings": "频谱图设置",
    "Start labeling tasks": "开始标注任务",
    "Start labeling and track your results": "开始标注并跟踪你的结果",
    "Start Training": "开始训练",
    "Storage Sync Error Log": "存储同步错误日志",
    "Storage options": "存储选项",
    "Storage Type": "存储类型",
    "Structured Data Parsing": "结构化数据解析",
    "Submit": "提交",
    "Submit Annotation": "提交标注",
    "Submit the current annotation": "提交当前标注",
    "Sync Storage": "同步存储",
    "Tabular Data": "表格数据",
    "Target Cloud Storage": "目标云存储",
    "Task Data": "任务数据",
    "Template parsing error:": "模板解析错误：",
    "The number of days, after creation, that the token will be valid for. After this time period a user will need to create a new access token": "令牌创建后可生效的天数。超过该时间后，用户需要重新创建新的访问令牌。",
    "Tasks imported to this project will appear here": "导入到此项目的任务将显示在这里",
    "Tasks you've labeled will appear here": "你已标注的任务将显示在这里",
    "There's an Enterprise version of Label Studio packed with more features and automation to label data faster while ensuring the highest quality.": "Label Studio 企业版提供了更多功能和自动化能力，可更快地标注数据并确保最高质量。",
    "This template requires more data then you have for now": "此模板当前需要比你现有更多的数据",
    "Total tasks in the project": "项目中的任务总数",
    "Tools": "工具",
    "Try Label Studio Starter Cloud, optimized for small teams and projects.": "试试为小团队和项目优化的 Label Studio Starter Cloud。",
    "You can connect ML models using the backend SDK to save time with pre-labeling or active learning.": "你可以通过后端 SDK 连接 ML 模型，利用预标注或主动学习来节省时间。",
    "Use cloud or database storage as the source for your labeling tasks or the target of your completed annotations.": "使用云存储或数据库存储作为标注任务的数据源，或作为已完成标注的目标存储。",
    "Uh oh, this page doesn’t exist.": "哎呀，这个页面不存在。",
    "Video format support depends on your browser. Click to learn more.": "视频格式支持取决于你的浏览器。点击了解更多。",
    "Welcome 👋": "欢迎 👋",
    "Webhooks": "网络钩子",
    "Want to simplify and secure logging in?": "想让登录更简单、更安全吗？",
    "Would you like to save them before leaving?": "你想在离开前保存吗？",
    "Share knowledge with the community": "与社区分享经验",
    "Join the community": "加入社区",
    "Have questions or a tip to share with other Label Studio users? Join the community slack channel for the latest updates.": "如有问题或想向其他 Label Studio 用户分享经验，请加入社区 Slack 频道获取最新动态。",
    "Label Studio Enterprise is now available on the AWS Marketplace so you can use your committed spend to streamline data labeling workflows.": "Label Studio 企业版现已上架 AWS Marketplace，你可以使用已承诺的 AWS 消费额度来简化数据标注工作流。",
    "Here’s a few things you can try:": "你可以尝试以下操作：",
    "Let's get you started.": "让我们开始吧。",
    "Email": "电子邮箱",
    "Add Members": "添加成员",
    "Enable Single Sign-On for your team using SAML, SCIM2 or LDAP with Label Studio Enterprise.": "使用 Label Studio 企业版的 SAML、SCIM2 或 LDAP 为你的团队启用单点登录。",
    "Workspace": "工作区",
    "When pre-signed URLs are enabled, all data bypasses the platform and user browsers directly read data from storage": "启用预签名 URL 后，所有数据都绕过平台，用户浏览器将直接从存储读取数据",
    "Write instructions to help users complete labeling tasks.": "编写说明以帮助用户完成标注任务。",
    "You have unsaved changes": "你有未保存的更改",
    "You have unsaved changes.": "你有未保存的更改。",
    "You must upgrade your plan to import data": "你必须升级套餐才能导入数据",
    "Your labeling configuration is empty. It is required to label your data.": "你的标注配置为空。标注数据前必须先完成配置。",
    "Your redis password": "你的 Redis 密码",
    "Your storage account key": "你的存储账户密钥",
    "Actions": "操作",
    "Annotation": "标注",
    "Annotation Settings": "标注设置",
    "Browse Templates": "浏览模板",
    "By Time": "按时间",
    "Code": "代码",
    "Color": "颜色",
    "Columns": "列",
    "Combine automation plus human supervision to evaluate and ensure LLM quality in the Enterprise platform.": "在企业版平台中结合自动化与人工监督，评估并确保 LLM 质量。",
    "Connect Model": "连接模型",
    "Configure the labeling interface with tags. See all tags.": "使用标签配置标注界面。查看所有标签。",
    "Description": "描述",
    "Enterprise": "企业版",
    "Enable and select which set of predictions to use for prelabeling.": "启用并选择要用于预标注的那组预测结果。",
    "Evaluate GenAI models": "评估 GenAI 模型",
    "Filters": "筛选",
    "History": "历史",
    "Info": "信息",
    "Labeling Interface": "标注界面",
    "Labeled regions will appear here": "已标注区域将显示在这里",
    "Let's connect your first model": "让我们连接你的第一个模型",
    "Manual": "手动",
    "Model": "模型",
    "No model or predictions available": "没有可用的模型或预测",
    "Predictions": "预测",
    "Preview": "预览",
    "Prelabeling": "预标注",
    "Recent Projects": "最近项目",
    "Regions": "区域",
    "Relations": "关系",
    "Save time with Auto-Labeling": "使用自动标注节省时间",
    "Select which predictions or which model you want to use:": "选择你要使用的预测结果或模型：",
    "Sequential sampling": "顺序采样",
    "Show before labeling": "标注前显示",
    "Task Sampling": "任务采样",
    "Tasks are ordered by Task ID": "任务按任务 ID 排序",
    "Tasks are chosen according to model uncertainty score (active learning mode).": "任务会根据模型不确定性分数进行选择（主动学习模式）。",
    "Tasks are chosen with uniform random": "任务以均匀随机方式选择",
    "The instruction field supports HTML markup and it allows use of images, iframes (pdf).": "说明字段支持 HTML 标记，并允许使用图片、iframe（PDF）。",
    "Use automation to instantly label large-scale datasets without sacrificing quality in the Enterprise platform.": "使用自动化可即时标注大规模数据集，同时在企业版平台中不牺牲质量。",
    "Use predictions to prelabel tasks": "使用预测结果对任务进行预标注",
    "using this panel": "使用此面板",
    "View All": "查看全部",
    "Visual": "可视化",
    "Computer Vision": "计算机视觉",
    "Natural Language Processing": "自然语言处理",
    "Audio/Speech Processing": "音频/语音处理",
    "Conversational AI": "对话式 AI",
    "Ranking & Scoring": "排序与打分",
    "Time Series Analysis": "时间序列分析",
    "Community Contributions": "社区贡献",
    "Custom template": "自定义模板",
    "Semantic Segmentation with Polygons": "多边形语义分割",
    "Semantic Segmentation with Masks": "掩码语义分割",
    "Object Detection with Bounding Boxes": "边界框目标检测",
    "Image Captioning": "图像描述",
    "Visual Genome": "视觉基因组",
    "Select text to correct": "选择要纠正的文本",
    "Incorrect Amount": "金额错误",
    "Incorrect Name": "名称错误",
    "Typo": "错别字",
    "Order by": "排序方式",
    "Default": "默认",
    "Description": "描述",
    "Color": "颜色",
    "Random sampling": "随机采样",
    "Uncertainty sampling": "不确定性采样",
    "You can increase the quality of your labeled data with reviewer workflows and task agreement scores using Label Studio Enterprise.": "你可以使用 Label Studio 企业版的审核流程和任务一致性评分来提高标注数据质量。",
}

AUTO_PHRASES = [
    ("A full-fledged open source solution for data labeling", "一个功能完整的数据标注开源方案"),
    ("You can export dataset in one of the following formats:", "你可以以下列格式之一导出数据集："),
    ("Customize your keyboard shortcuts to speed up your workflow.", "自定义键盘快捷键以加快工作流程。"),
    ("Click on any hotkey below to assign a new key combination that works best for you.", "点击下方任意快捷键即可分配最适合你的新按键组合。"),
    ("Manage your access tokens securely", "安全管理你的访问令牌"),
    ("Token Expiry Date", "令牌过期时间"),
    ("New Auth Token", "新认证令牌"),
    ("Revoke Token", "吊销令牌"),
    ("Hotkeys imported successfully", "快捷键导入成功"),
    ("Import Error", "导入错误"),
    ("Email Preferences", "邮件偏好"),
    ("Membership Info", "成员信息"),
    ("Cloud Storage", "云存储"),
    ("Delete Project", "删除项目"),
    ("Export data", "导出数据"),
    ("Create Project", "创建项目"),
    ("Create Account", "创建账户"),
    ("Project Name", "项目名称"),
    ("Optional description of your project", "项目可选描述"),
    ("Personal Access Token", "个人访问令牌"),
    ("Access Token", "访问令牌"),
    ("Account Settings", "账户设置"),
    ("Account & Settings", "账户与设置"),
    ("My Account", "我的账户"),
    ("Personal Info", "个人信息"),
    ("Danger Zone", "危险区域"),
    ("Drop All Tabs", "清空所有标签页"),
    ("Data Manager", "数据管理"),
    ("Labeling Setup", "标注设置"),
    ("Save and Leave", "保存并离开"),
    ("Keep me logged in this browser", "在此浏览器中保持登录"),
    ("Select an option", "选择一个选项"),
    ("Learn more", "了解更多"),
    ("Log Out", "退出登录"),
    ("Log In", "登录"),
    ("Log in", "登录"),
    ("Sign Up", "注册"),
    ("Sign up", "注册"),
    ("Settings", "设置"),
    ("Projects", "项目"),
    ("Workspace", "工作区"),
    ("Home", "首页"),
    ("Hotkeys", "快捷键"),
    ("Import", "导入"),
    ("Export", "导出"),
    ("Submit", "提交"),
    ("Cancel", "取消"),
    ("Tools", "工具"),
    ("Docs", "文档"),
    ("Webhooks", "网络钩子"),
]

ALLOWED_ENGLISH_TOKENS = {
    "api",
    "apis",
    "csv",
    "gcs",
    "gpu",
    "html",
    "http",
    "https",
    "id",
    "ids",
    "json",
    "jwt",
    "label",
    "llm",
    "ocr",
    "pdf",
    "s3",
    "sdk",
    "sql",
    "studio",
    "ui",
    "url",
    "webhook",
    "webhooks",
    "xml",
}

WORD_MAP = {
    "access": "访问",
    "account": "账户",
    "all": "所有",
    "api": "API",
    "auth": "认证",
    "cancel": "取消",
    "cloud": "云",
    "copied": "已复制",
    "create": "创建",
    "danger": "危险",
    "data": "数据",
    "delete": "删除",
    "description": "描述",
    "docs": "文档",
    "drop": "清空",
    "email": "邮件",
    "error": "错误",
    "export": "导出",
    "general": "常规",
    "home": "首页",
    "hotkeys": "快捷键",
    "import": "导入",
    "info": "信息",
    "json": "JSON",
    "leave": "离开",
    "log": "登录",
    "membership": "成员",
    "my": "我的",
    "name": "名称",
    "new": "新",
    "option": "选项",
    "optional": "可选",
    "out": "退出",
    "personal": "个人",
    "preferences": "偏好",
    "project": "项目",
    "projects": "项目",
    "revoke": "吊销",
    "save": "保存",
    "select": "选择",
    "settings": "设置",
    "sign": "注册",
    "storage": "存储",
    "submit": "提交",
    "tabs": "标签页",
    "token": "令牌",
    "tools": "工具",
    "webhooks": "网络钩子",
    "workspace": "工作区",
    "zone": "区域",
}

SEEDED_ENTRIES = {
    "auth": [
        {
            "source": "Reset to Defaults",
            "target": "恢复默认",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Annotation Actions",
            "target": "标注操作",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus Previous Task",
            "target": "聚焦上一任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Move focus to the previous task",
            "target": "将焦点移动到上一任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus Next Task",
            "target": "聚焦下一任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Move focus to the next task",
            "target": "将焦点移动到下一任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus Closed Task",
            "target": "聚焦已关闭任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus on the closed task column",
            "target": "聚焦到已关闭任务列",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus Open Task",
            "target": "聚焦开放任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus on the open task column",
            "target": "聚焦到开放任务列",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Toggle Bulk Sidebar",
            "target": "切换批量侧边栏",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Minimize or expand bulk actions sidebar",
            "target": "最小化或展开批量操作侧边栏",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Skip Task",
            "target": "跳过任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Skip the current task",
            "target": "跳过当前任务",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Undo",
            "target": "撤销",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Undo last action",
            "target": "撤销上一步操作",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Redo",
            "target": "重做",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Redo previously undone action",
            "target": "重做刚刚撤销的操作",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Region Management",
            "target": "区域管理",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Shortcuts for creating, selecting and manipulating annotation regions",
            "target": "用于创建、选择和操作标注区域的快捷键",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Remove all regions",
            "target": "删除所有区域",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Focus First Region",
            "target": "聚焦第一个区域",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Move focus to the first focusable region",
            "target": "将焦点移动到第一个可聚焦区域",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Audio Controls",
            "target": "音频控制",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Shortcuts for controlling audio playback and navigation",
            "target": "用于控制音频播放与导航的快捷键",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Video Controls",
            "target": "视频控制",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Shortcuts for controlling video playback and navigation",
            "target": "用于控制视频播放与导航的快捷键",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Time Series Controls",
            "target": "时间序列控制",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Image Gallery Navigation",
            "target": "图库导航",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Shortcuts for navigating between images in multi-image tasks",
            "target": "用于在多图任务中切换图像的快捷键",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Paragraph Navigation",
            "target": "段落导航",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Shortcuts for navigating phrases and regions in paragraph/dialogue view",
            "target": "用于在段落/对话视图中切换短语和区域的快捷键",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
    ],
    "projects": [
        {
            "source": "Audio/Speech Processing",
            "target": "音频/语音处理",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Chat",
            "target": "聊天",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Videos",
            "target": "视频",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Generative AI",
            "target": "生成式 AI",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Optical Character Recognition",
            "target": "光学字符识别",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Image Classification",
            "target": "图像分类",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Inventory Tracking",
            "target": "库存跟踪",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Visual Question Answering",
            "target": "视觉问答",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Medical Image Classification with Bounding Boxes",
            "target": "带边界框的医学图像分类",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "See the documentation to contribute a template.",
            "target": "查看文档以贡献模板。",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Browse Templates",
            "target": "浏览模板",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Code",
            "target": "代码",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Visual",
            "target": "可视化",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Preview",
            "target": "预览",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "History",
            "target": "历史",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Relations",
            "target": "关系",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Info",
            "target": "信息",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
        {
            "source": "Manual",
            "target": "手动",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        },
    ],
    "settings": [
        {
            "source": "Tools",
            "target": "工具",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        }
    ],
    "organization": [
        {
            "source": "Email",
            "target": "电子邮箱",
            "status": "approved",
            "priority": "high",
            "translation_source": "catalog-manual",
            "score": 100,
            "files": [],
            "contexts": [],
        }
    ]
}


def normalize(text: str) -> str:
    return " ".join(text.split()).strip()


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def build_catalog_lookup(catalog: dict[str, object]) -> tuple[dict[tuple[str, str], dict[str, object]], dict[str, dict[str, object]]]:
    by_module: dict[tuple[str, str], dict[str, object]] = {}
    global_by_source: dict[str, dict[str, object]] = {}
    for module_name, entries in catalog.get("modules", {}).items():
        for entry in entries:
            source = normalize(str(entry.get("source", "")))
            if not source:
                continue
            by_module[(str(module_name), source.casefold())] = entry
            global_by_source.setdefault(source.casefold(), entry)
    return by_module, global_by_source


def apply_phrase_map(text: str) -> tuple[str, int]:
    translated = text
    replacements = 0
    for source, target in AUTO_PHRASES:
        if source not in translated:
            continue
        translated = translated.replace(source, target)
        replacements += 1
    return translated, replacements


def join_translated_parts(parts: list[str]) -> str:
    text = "".join(parts)
    return cleanup_translation(text)


def cleanup_translation(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"([\u4e00-\u9fff])\s+([\u4e00-\u9fff])", r"\1\2", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+([A-Z0-9])", r"\1 \2", text)
    text = re.sub(r"([A-Z0-9])\s+([\u4e00-\u9fff])", r"\1 \2", text)
    text = text.replace("导入 快捷键", "导入快捷键")
    text = text.replace("云存储 设置", "云存储设置")
    text = text.replace("网络钩子 设置", "网络钩子设置")
    text = text.replace("已复制!", "已复制！")
    return text


def auto_translate_short_phrase(source: str) -> str | None:
    if len(source.split()) > 6:
        return None
    parts = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|[^A-Za-z]+", source)
    translated_parts: list[str] = []
    translated_any = False
    for part in parts:
        if re.fullmatch(r"[A-Za-z]+(?:'[A-Za-z]+)?", part):
            key = part.casefold()
            if key in WORD_MAP:
                translated_parts.append(WORD_MAP[key])
                translated_any = True
            elif key in ALLOWED_ENGLISH_TOKENS:
                translated_parts.append(part.upper() if key in {"api", "json", "jwt"} else part)
            else:
                return None
        else:
            translated_parts.append(part)
    if not translated_any:
        return None
    return join_translated_parts(translated_parts)


def auto_translate(source: str, priority: str) -> tuple[str, str] | None:
    normalized = normalize(source)
    if normalized in BUILTIN_TERMS:
        return BUILTIN_TERMS[normalized], "builtin-terms"
    if priority not in {"high", "medium"}:
        return None
    if any(marker in normalized for marker in ("{", "}", "[", "]", "=>", "http://", "https://")):
        return None
    translated, replacements = apply_phrase_map(normalized)
    if replacements > 0 and translated != normalized:
        leftovers = [token.casefold() for token in re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", translated)]
        unknown = [token for token in leftovers if token not in ALLOWED_ENGLISH_TOKENS]
        if not unknown:
            return cleanup_translation(translated), "auto-phrases"
    short_phrase = auto_translate_short_phrase(normalized)
    if short_phrase:
        return short_phrase, "auto-words"
    return None


def merge_entry(module_name: str, entry: dict[str, object], catalog_by_module: dict[tuple[str, str], dict[str, object]], catalog_global: dict[str, dict[str, object]]) -> dict[str, object]:
    source = normalize(str(entry.get("source", "")))
    existing = catalog_by_module.get((module_name, source.casefold())) or catalog_global.get(source.casefold())
    merged = dict(entry)
    if existing:
        existing_source = str(existing.get("translation_source", "catalog"))
        refreshed = auto_translate(source, str(entry.get("priority", "low"))) if existing_source.startswith("auto-") else None
        if refreshed:
            merged["target"], merged["translation_source"] = refreshed
            merged["status"] = "approved"
        else:
            merged["target"] = existing.get("target", "")
            merged["status"] = existing.get("status", "approved")
            merged["translation_source"] = existing_source
    elif source in BUILTIN_TERMS:
        merged["target"] = BUILTIN_TERMS[source]
        merged["status"] = "approved"
        merged["translation_source"] = "builtin-terms"
    else:
        auto_result = auto_translate(source, str(entry.get("priority", "low")))
        if auto_result:
            merged["target"], merged["translation_source"] = auto_result
            merged["status"] = "approved"
        else:
            merged["target"] = ""
            merged["status"] = "pending"
            merged["translation_source"] = "missing"
    return merged


def build_reports(modules: dict[str, list[dict[str, object]]]) -> tuple[dict[str, object], dict[str, object]]:
    missing: list[dict[str, object]] = []
    high_priority: list[dict[str, object]] = []
    for entries in modules.values():
        for entry in entries:
            if entry.get("status") == "approved" and normalize(str(entry.get("target", ""))):
                continue
            item = {
                "source": entry.get("source", ""),
                "priority": entry.get("priority", "low"),
                "score": entry.get("score", 0),
                "files": entry.get("files", []),
                "contexts": entry.get("contexts", []),
            }
            missing.append(item)
            if item["priority"] == "high":
                high_priority.append(item)
    missing.sort(key=lambda item: (-int(item.get("score", 0)), str(item.get("source", "")).lower()))
    high_priority.sort(key=lambda item: (-int(item.get("score", 0)), str(item.get("source", "")).lower()))
    return {"total": len(missing), "items": missing}, {"total": len(high_priority), "items": high_priority}


def merge_seeded_entries(modules: dict[str, list[dict[str, object]]]) -> dict[str, list[dict[str, object]]]:
    for module_name, seeded_entries in SEEDED_ENTRIES.items():
        bucket = modules.setdefault(module_name, [])
        existing_by_source = {normalize(str(entry.get("source", ""))).casefold(): entry for entry in bucket}
        for entry in seeded_entries:
            source_key = normalize(str(entry["source"])).casefold()
            existing = existing_by_source.get(source_key)
            if existing is None:
                bucket.append(dict(entry))
                existing_by_source[source_key] = bucket[-1]
                continue
            if existing.get("status") != "approved" or not normalize(str(existing.get("target", ""))):
                existing.update(dict(entry))
    return modules


def build_catalog_payload(modules: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    catalog_modules: dict[str, list[dict[str, object]]] = {}
    for module_name, entries in modules.items():
        approved = []
        for entry in entries:
            target = normalize(str(entry.get("target", "")))
            if entry.get("status") != "approved" or not target:
                continue
            approved.append(
                {
                    "source": entry.get("source", ""),
                    "target": target,
                    "status": "approved",
                    "priority": entry.get("priority", "low"),
                    "translation_source": entry.get("translation_source", "catalog"),
                }
            )
        if approved:
            approved.sort(key=lambda item: str(item["source"]).lower())
            catalog_modules[module_name] = approved
    return {"meta": {"generated_by": "scripts/sync_translation_catalog.py", "translation_first": True}, "modules": catalog_modules}


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync overlay candidates with translation catalog.")
    parser.add_argument("dictionary_json", help="Path to filtered candidate dictionary JSON.")
    parser.add_argument("--catalog", required=True, help="Path to translation catalog JSON.")
    parser.add_argument("--output-json", required=True, help="Path to merged translations JSON.")
    parser.add_argument("--missing-report", required=True, help="Path to all missing translations report.")
    parser.add_argument("--high-priority-report", required=True, help="Path to high priority missing report.")
    args = parser.parse_args()

    dictionary_path = Path(args.dictionary_json).resolve()
    catalog_path = Path(args.catalog).resolve()
    payload = load_json(dictionary_path)
    catalog = load_json(catalog_path)
    catalog_by_module, catalog_global = build_catalog_lookup(catalog)

    merged_modules: dict[str, list[dict[str, object]]] = {}
    for module_name, entries in payload.get("modules", {}).items():
        merged_modules[str(module_name)] = [merge_entry(str(module_name), dict(entry), catalog_by_module, catalog_global) for entry in entries]

    merged_modules = merge_seeded_entries(merged_modules)

    translations_payload = {
        "meta": {"source": str(dictionary_path), "catalog": str(catalog_path), "synced": True, "translation_first": True},
        "modules": merged_modules,
    }
    missing_report, high_priority_report = build_reports(merged_modules)
    catalog_payload = build_catalog_payload(merged_modules)

    output_json = Path(args.output_json).resolve()
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(translations_payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(json.dumps(catalog_payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    Path(args.missing_report).resolve().write_text(json.dumps(missing_report, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    Path(args.high_priority_report).resolve().write_text(json.dumps(high_priority_report, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
