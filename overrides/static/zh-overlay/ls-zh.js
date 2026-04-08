(function () {
  var config = window.LS_ZH_OVERLAY || {};
  if (config.enabled === false) {
    return;
  }

  var MODULE_MAPS = {
  "auth": {
    "A full-fledged open source solution for data labeling": "一个功能完整的数据标注开源方案",
    "Access Token": "访问令牌",
    "Account & Settings": "账户与设置",
    "All hotkeys and settings have been reset to defaults and saved": "所有快捷键和设置都已重置为默认值并保存",
    "Annotation Actions": "标注操作",
    "Annotations completed by you": "由你完成的标注",
    "Audio Controls": "音频控制",
    "Auto-Label Tasks": "自动标注任务",
    "Cancel": "取消",
    "Copied!": "已复制！",
    "Create a copy of the selected region": "创建所选区域的副本",
    "Create a relation between selected regions": "在所选区域之间创建关系",
    "Create Account": "创建账户",
    "Create New Token": "创建新 令牌",
    "Create Region Relation": "创建区域关系",
    "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.": "自定义键盘快捷键以加快工作流程。 点击下方任意快捷键即可分配最适合你的新按键组合。",
    "Data Manager": "数据管理",
    "Delete All Regions": "删除所有区域",
    "Delete currently selected region": "删除当前选中的区域",
    "Delete Segment": "删除片段",
    "Delete Selected Region": "删除所选区域",
    "Delete selected segment": "删除所选片段",
    "Did you know?": "你知道吗？",
    "Docs": "文档",
    "Documentation": "文档",
    "E-mail": "电子邮箱",
    "Edit metadata for selected region": "编辑所选区域元数据",
    "Edit Region Metadata": "编辑区域元数据",
    "Email Preferences": "邮件偏好",
    "Export": "导出",
    "Failed to save imported hotkeys": "保存导入的快捷键失败",
    "First Name": "名",
    "Focus Closed Task": "聚焦已关闭任务",
    "Focus First Region": "聚焦第一个区域",
    "Focus Next Task": "聚焦下一任务",
    "Focus on the closed task column": "聚焦到已关闭任务列",
    "Focus on the open task column": "聚焦到开放任务列",
    "Focus Open Task": "聚焦开放任务",
    "Focus Previous Task": "聚焦上一任务",
    "Great news!": "好消息！",
    "Hotkeys imported successfully": "快捷键导入成功",
    "Hotkeys JSON": "快捷键 JSON",
    "How did you hear about Label Studio?": "你是如何了解到 Label Studio 的？",
    "Human Signal Logo": "Human Signal 标志",
    "Image Gallery Navigation": "图库导航",
    "Import": "导入",
    "Import Error": "导入错误",
    "Import Hotkeys": "导入快捷键",
    "Keep me logged in this browser": "在此浏览器中保持登录",
    "Label Studio": "Label Studio",
    "Label Studio Logo": "Label Studio 标志",
    "Last Name": "姓",
    "Learn more": "了解更多",
    "Log in": "登录",
    "Manage your access tokens securely": "安全管理你的访问令牌",
    "Membership Info": "成员信息",
    "Minimize or expand bulk actions sidebar": "最小化或展开批量操作侧边栏",
    "Move focus to the first focusable region": "将焦点移动到第一个可聚焦区域",
    "Move focus to the next task": "将焦点移动到下一任务",
    "Move focus to the previous task": "将焦点移动到上一任务",
    "My Account": "我的账户",
    "New Auth Token": "新认证令牌",
    "Paragraph Navigation": "段落导航",
    "Personal Access Token": "个人访问令牌",
    "Personal Info": "个人信息",
    "Please enter JSON data to import": "请输入要导入的 JSON 数据",
    "Redo": "重做",
    "Redo previously undone action": "重做刚刚撤销的操作",
    "Region Management": "区域管理",
    "Remove all regions": "删除所有区域",
    "Reset Hotkeys to Defaults?": "将快捷键重置为默认值？",
    "Reset to Defaults": "恢复默认",
    "Revoke Token": "吊销令牌",
    "Save": "保存",
    "See all templates": "查看所有模板",
    "Select all text in current phrase and create annotation": "选择当前短语中的全部文本并创建标注",
    "Select an option": "选择一个选项",
    "Shortcuts for common annotation tasks like submit, skip, undo and redo": "用于提交、跳过、撤销和重做等常见标注任务的快捷键",
    "Shortcuts for controlling audio playback and navigation": "用于控制音频播放与导航的快捷键",
    "Shortcuts for controlling tools panel when labeling images": "标注图像时控制工具面板的快捷键",
    "Shortcuts for controlling video playback and navigation": "用于控制视频播放与导航的快捷键",
    "Shortcuts for creating, selecting and manipulating annotation regions": "用于创建、选择和操作标注区域的快捷键",
    "Shortcuts for manipulating time series data regions": "操作时间序列数据区域的快捷键",
    "Shortcuts for navigating and managing tasks in Project's Data Manager": "在项目数据管理中导航和管理任务的快捷键",
    "Shortcuts for navigating between images in multi-image tasks": "用于在多图任务中切换图像的快捷键",
    "Shortcuts for navigating phrases and regions in paragraph/dialogue view": "用于在段落/对话视图中切换短语和区域的快捷键",
    "Sign up": "注册",
    "Skip Task": "跳过任务",
    "Skip the current task": "跳过当前任务",
    "Submit Annotation": "提交标注",
    "Submit the current annotation": "提交当前标注",
    "There's an Enterprise version of Label Studio packed with more features and automation to label data faster while ensuring the highest quality.": "Label Studio 企业版提供了更多功能和自动化能力，可更快地标注数据并确保最高质量。",
    "Time Series Controls": "时间序列控制",
    "Toggle Bulk Sidebar": "切换批量侧边栏",
    "Token Expiry Date": "令牌过期时间",
    "Undo": "撤销",
    "Undo last action": "撤销上一步操作",
    "Video Controls": "视频控制"
  },
  "home": {
    "* Create New Project *": "* 创建新 项目 *",
    "* Import Project *": "* 导入项目 *",
    "API Documentation": "API 文档",
    "Azure Blob Storage": "Azure Blob 存储",
    "Choose a dataset from your computer to get started": "从你的电脑选择一个数据集以开始使用",
    "Connect Cloud Storage": "连接云存储",
    "Connect your cloud storage or upload files from your computer": "连接你的云存储或从电脑上传文件",
    "Create new project": "创建新 项目",
    "Create Project": "创建项目",
    "Create your first project": "创建你的第一个项目",
    "Documentation": "文档",
    "Error occurred while loading data": "加载数据时发生错误",
    "Failed to load data": "加载数据失败",
    "Google Cloud Storage": "Google Cloud Storage",
    "Home": "首页",
    "Import": "导入",
    "Import Data": "导入数据",
    "Import data to get your project started": "导入数据以开始你的项目",
    "Import your data": "导入你的数据",
    "Import your data and set up the labeling interface to start annotating": "导入数据并设置标注界面以开始标注",
    "Invite Members": "邀请成员",
    "Label All Tasks": "标注所有任务",
    "Label Studio Version: Community": "Label Studio 版本：社区版",
    "LabelStud.io Blog": "LabelStud.io 博客",
    "Learn, explore and get help": "学习、探索并获取帮助",
    "Let's get you started.": "让我们开始吧。",
    "No data available": "没有可用数据",
    "No tasks available for review or labeling": "没有可供审核或标注的任务",
    "Recent Projects": "最近项目",
    "Redis Storage": "Redis 存储",
    "Release Notes": "发布说明",
    "Resources": "资源",
    "See docs on importing data": "查看导入数据文档",
    "Slack Community": "Slack 社区",
    "Start labeling tasks": "开始标注任务",
    "Tasks imported to this project will appear here": "导入到此项目的任务将显示在这里",
    "Tasks you've labeled will appear here": "你已标注的任务将显示在这里",
    "View All": "查看全部",
    "Welcome 👋": "欢迎 👋"
  },
  "projects": {
    ", import:": ", 导入:",
    "Add filter for long list of labels": "为长标签列表添加筛选",
    "Add label names": "添加标签名称",
    "Add labels": "添加标签",
    "Add URL": "添加 URL",
    "Audio/Speech Processing": "音频/语音处理",
    "Browse templates": "浏览模板",
    "Cancel": "取消",
    "Cancel import": "取消导入",
    "Cancel project creation": "取消项目创建",
    "Chat": "聊天",
    "Cloud Storage": "云存储",
    "Cloud Storage documentation (opens in a new tab)": "云存储文档（在新标签页中打开）",
    "Code": "代码",
    "Computer Vision": "计算机视觉",
    "Configure data": "配置数据",
    "Configure settings": "配置设置",
    "Create": "创建",
    "Create custom template": "创建自定义模板",
    "Create new project": "创建新 项目",
    "Create one and start labeling your data.": "创建一个并开始标注你的数据。",
    "Create Project": "创建项目",
    "Custom template": "自定义模板",
    "Data Import": "数据导入",
    "Dataset URL": "数据集 URL",
    "delete label": "删除 label",
    "Display labels:": "显示标签：",
    "Enterprise feature - Available in Label Studio Enterprise": "企业版功能，Label Studio 企业版可用",
    "Finish import": "完成导入",
    "Generative AI": "生成式 AI",
    "Heidi doesn't see any projects here!": "Heidi 在这里没有看到任何项目！",
    "History": "历史",
    "Image Classification": "图像分类",
    "Import data": "导入数据",
    "import preannotated data": "导入预标注数据",
    "Info": "信息",
    "Inventory Tracking": "库存跟踪",
    "Label": "标签",
    "Labeling Setup": "标注设置",
    "Labels": "标签",
    "Learn more": "了解更多",
    "Learn more about video format support (opens in a new tab)": "了解更多视频格式支持信息（在新标签页中打开）",
    "Manual": "手动",
    "Medical Image Classification with Bounding Boxes": "带边界框的医学图像分类",
    "Multi-image labeling documentation (opens in a new tab)": "多图标注文档（在新标签页中打开）",
    "Named entity recognition": "命名实体识别",
    "New project": "新项目",
    "No sample task data available.": "没有可用的示例任务数据。",
    "Optical Character Recognition": "光学字符识别",
    "Optional description of your project": "项目可选描述",
    "Organization": "组织",
    "Polygon labeling": "多边形标注",
    "Preview": "预览",
    "Project Name": "项目名称",
    "Project options": "项目选项",
    "Projects": "项目",
    "Relations": "关系",
    "Sample config to label with bboxes": "用于框选标注的示例配置",
    "Save": "保存",
    "Save and Leave": "保存并离开",
    "Save changes": "保存更改",
    "Save configuration": "保存配置",
    "Saved!": "已保存！",
    "See the documentation to contribute a template.": "查看文档以贡献模板。",
    "Select an option": "选择一个选项",
    "Select label and click on image to start": "选择标签并点击图像开始",
    "Sequential sampling": "顺序采样",
    "Settings": "设置",
    "Simplify project management by organizing projects into workspaces.": "通过将项目组织到工作区中来简化项目管理。",
    "Template parsing error:": "模板解析错误：",
    "This template requires more data then you have for now": "此模板当前需要比你现有更多的数据",
    "Uncertainty sampling": "不确定性采样",
    "Video format support depends on your browser. Click to learn more.": "视频格式支持取决于你的浏览器。点击了解更多。",
    "Videos": "视频",
    "Visual": "可视化",
    "Visual Question Answering": "视觉问答",
    "Workspace": "工作区",
    "Would you like to save them before leaving?": "你想在离开前保存吗？",
    "You have unsaved changes.": "你有未保存的更改。",
    "Your labeling configuration is empty. It is required to label your data.": "你的标注配置为空。标注数据前必须先完成配置。"
  },
  "import_export": {
    "Can't find an export format?": "找不到导出格式？",
    "Copied": "已复制",
    "Copied!": "已复制！",
    "Export": "导出",
    "Export data": "导出数据",
    "Label Studio Enterprise": "Label Studio 企业版",
    "Read more about supported export formats in the Documentation.": "在文档中了解更多支持的导出格式。",
    "You can export dataset in one of the following formats:": "你可以以下列格式之一导出数据集："
  },
  "data_manager": {
    "Back to projects": "返回项目",
    "Before you can annotate the data, set up labeling configuration": "在标注数据前，请先设置标注配置",
    "Check your storage settings. You may need to recreate this dataset": "请检查你的存储设置。你可能需要重新创建此数据集",
    "Columns": "列",
    "Copied!": "已复制！",
    "Data": "数据",
    "Default": "默认",
    "Error occurred when loading data": "加载数据时发生错误",
    "Filters": "筛选",
    "Focus previous task": "聚焦上一任务",
    "Grid settings": "网格设置",
    "label all": "label 所有",
    "Label Tasks As Displayed": "按显示顺序标注任务",
    "Labeling": "标注",
    "Labeling Instructions": "标注说明",
    "Order by": "排序方式",
    "Project has been deleted or not yet created.": "项目已被删除或尚未创建。",
    "Project ID:": "项目 ID:",
    "Project was deleted or not yet created": "项目已被删除或尚未创建",
    "Refresh data": "刷新数据",
    "Save": "保存",
    "Saved!": "已保存！",
    "Settings": "设置",
    "Task Data": "任务数据",
    "Total tasks in the project": "项目中的任务总数",
    "You have unsaved changes": "你有未保存的更改",
    "You must upgrade your plan to import data": "你必须升级套餐才能导入数据"
  },
  "labeling": {
    "Add any notes or edge cases...": "添加任何备注或边界情况...",
    "Annotation": "标注",
    "Annotation Settings": "标注设置",
    "Cancel": "取消",
    "Delete": "删除",
    "Delete selected region": "删除所选区域",
    "Enable and select which set of predictions to use for prelabeling.": "启用并选择要用于预标注的那组预测结果。",
    "Enterprise": "企业版",
    "Incorrect Amount": "金额错误",
    "Incorrect Name": "名称错误",
    "Labeling Instructions": "标注说明",
    "Labeling Interface": "标注界面",
    "Labeling Interface Settings": "标注界面设置",
    "Learn more": "了解更多",
    "Model": "模型",
    "No model or predictions available": "没有可用的模型或预测",
    "No predictions uploaded yet": "尚未上传任何预测结果",
    "Organization": "组织",
    "Predictions": "预测",
    "Predictions Settings": "预测设置",
    "Prelabeling": "预标注",
    "Regions": "区域",
    "Save": "保存",
    "Saved!": "已保存！",
    "Select label and click the image to start": "选择标签并点击图像开始",
    "Select text to correct": "选择要纠正的文本",
    "Select which predictions or which model you want to use:": "选择你要使用的预测结果或模型：",
    "Show before labeling": "标注前显示",
    "The instruction field supports HTML markup and it allows use of images, iframes (pdf).": "说明字段支持 HTML 标记，并允许使用图片、iframe（PDF）。",
    "Typo": "错别字",
    "Use predictions to prelabel tasks": "使用预测结果对任务进行预标注",
    "Write instructions to help users complete labeling tasks.": "编写说明以帮助用户完成标注任务。"
  },
  "settings": {
    "Account Key": "账户密钥",
    "Account Name": "账户名称",
    "Actions": "操作",
    "Add machine learning model": "添加机器学习模型",
    "Add Source Storage": "添加源存储",
    "Add storage": "添加存储",
    "Add Target Storage": "添加目标存储",
    "Add your first cloud storage": "添加你的第一个云存储",
    "Allows continuous region creation using the selected label": "允许使用所选标签连续创建区域",
    "Amazon S3 with IAM Role is available in Label Studio Enterprise.": "带 IAM Role 的 Amazon S3 在 Label Studio 企业版中可用。",
    "Annotation settings": "标注设置",
    "Automatically selects newly created regions": "自动选择新创建的区域",
    "Available on Label Studio Enterprise": "Label Studio 企业版可用",
    "Azure Blob Storage": "Azure Blob 存储",
    "Azure Blob Storage with Service Principal is available in Label Studio Enterprise.": "带 Service Principal 的 Azure Blob 存储在 Label Studio 企业版中可用。",
    "Cancel": "取消",
    "Cloud Storage": "云存储",
    "Cloud Storage Settings": "云存储设置",
    "Configure your AWS S3 connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 AWS S3 连接",
    "Configure your Azure Blob Storage connection using Service Principal authentication for enhanced security (proxy only)": "使用 Service Principal 身份验证配置你的 Azure Blob 存储连接以增强安全性（仅代理）",
    "Configure your Azure Blob Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Azure Blob 存储连接",
    "Configure your Databricks Unity Catalog Volumes connection with all required settings (proxy only)": "使用所有必需设置配置你的 Databricks Unity Catalog Volumes 连接（仅代理）",
    "Configure your Google Cloud Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Google Cloud Storage 连接",
    "Configure your Google Cloud Storage connection with Workload Identity Federation authentication (proxy only)": "使用 Workload Identity Federation 身份验证配置你的 Google Cloud Storage 连接（仅代理）",
    "Configure your local file storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的本地文件存储连接",
    "Configure your Redis storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Redis 存储连接",
    "Connect Model": "连接模型",
    "Copied!": "已复制！",
    "Danger Zone": "危险区域",
    "Data Manager": "数据管理",
    "Database Number (db)": "数据库编号（db）",
    "Databricks Files (UC Volumes) is available in Label Studio Enterprise.": "Databricks Files（UC Volumes）在 Label Studio 企业版中可用。",
    "Delete ML Backend": "删除机器学习后端",
    "Delete Project": "删除项目",
    "Deleting a project removes all tasks, annotations, and project data from the database.": "删除项目会从数据库中移除所有任务、标注和项目数据。",
    "Deleting storage": "正在删除存储",
    "Display region label names": "显示区域标签名称",
    "Drop All Tabs": "清空所有标签页",
    "Edit": "编辑",
    "Enable increased token authentication security": "启用增强的令牌认证安全性",
    "Enable labeling hotkeys": "启用标注快捷键",
    "Enable legacy access tokens, these do not expire": "启用旧版访问令牌，这些令牌不会过期",
    "Enables quick selection of labels using hotkeys": "支持使用快捷键快速选择标签",
    "Enterprise Feature": "企业版功能",
    "Error loading settings.": "加载设置时出错。",
    "General": "常规",
    "General Settings": "常规设置",
    "Google Cloud Storage": "Google Cloud Storage",
    "Google Cloud Storage with Workload Identity Federation is available in Label Studio Enterprise.": "带 Workload Identity Federation 的 Google Cloud Storage 在 Label Studio 企业版中可用。",
    "Google Project ID": "Google 项目 ID",
    "Hotkeys": "快捷键",
    "If the Data Manager is not loading, dropping all Data Manager tabs can help.": "如果数据管理未加载，清空所有数据管理标签页可能会有所帮助。",
    "Labeling hotkeys": "标注快捷键",
    "Labeling Interface Settings": "标注界面设置",
    "Learn more": "了解更多",
    "Learn more about cloud storage (opens in new window)": "了解更多云存储信息（在新窗口中打开）",
    "Learn more about cloud storage troubleshooting": "了解更多云存储故障排查信息",
    "Learn more about machine learning models (opens in new window)": "了解更多机器学习模型（在新窗口中打开）",
    "Legacy Tokens": "旧版令牌",
    "Let's connect your first model": "让我们连接你的第一个模型",
    "Local Storage documentation": "本地存储文档",
    "Model": "模型",
    "Model Settings": "模型设置",
    "Name": "名称",
    "Perform these actions at your own risk. Actions you take on this page can't be reverted. Make sure your data is backed up.": "执行这些操作需自行承担风险。你在此页面执行的操作无法撤销。请先确认你的数据已备份。",
    "Personal Access Tokens": "个人访问令牌",
    "Project Name": "项目名称",
    "Redis Storage": "Redis 存储",
    "Remember Selected Tool": "记住所选工具",
    "Reset Cache": "重置缓存",
    "Save": "保存",
    "Save Changes": "保存更改",
    "Save general settings": "保存常规设置",
    "Save machine learning form": "保存机器学习表单",
    "Save machine learning settings": "保存机器学习设置",
    "Save storage settings": "保存存储设置",
    "Saved!": "已保存！",
    "Select an option": "选择一个选项",
    "Session Token": "会话令牌",
    "Session token (optional)": "会话令牌（可选）",
    "Settings": "设置",
    "Show hotkeys on labels": "在标签上显示快捷键",
    "Show labels hotkey tooltips": "显示标签快捷键提示",
    "Show labels inside the regions": "在区域内部显示标签",
    "Show region labels": "显示区域标签",
    "Simplify project management by organizing projects into workspaces.": "通过将项目组织到工作区中来简化项目管理。",
    "Source Cloud Storage": "源云存储",
    "Start Training": "开始训练",
    "Storage options": "存储选项",
    "Storage Sync Error Log": "存储同步错误日志",
    "Storage Type": "存储类型",
    "Sync Storage": "同步存储",
    "Target Cloud Storage": "目标云存储",
    "Task Sampling": "任务采样",
    "Tasks are chosen according to model uncertainty score (active learning mode).": "任务会根据模型不确定性分数进行选择（主动学习模式）。",
    "Tasks are chosen with uniform random": "任务以均匀随机方式选择",
    "Tasks are ordered by Task ID": "任务按任务 ID 排序",
    "The number of days, after creation, that the token will be valid for. After this time period a user will need to create a new access token": "令牌创建后可生效的天数。超过该时间后，用户需要重新创建新的访问令牌。",
    "Tools": "工具",
    "Uncertainty sampling": "不确定性采样",
    "Use cloud or database storage as the source for your labeling tasks or the target of your completed annotations.": "使用云存储或数据库存储作为标注任务的数据源，或作为已完成标注的目标存储。",
    "When pre-signed URLs are enabled, all data bypasses the platform and user browsers directly read data from storage": "启用预签名 URL 后，所有数据都绕过平台，用户浏览器将直接从存储读取数据",
    "Workspace": "工作区",
    "Your redis password": "你的 Redis 密码",
    "Your storage account key": "你的存储账户密钥"
  },
  "storage": {
    "Azure Blob Storage": "Azure Blob 存储",
    "Choose how to interpret your data from storage": "选择如何解析来自存储的数据",
    "Choose your cloud storage provider": "选择你的云存储提供商",
    "Configure Import Settings & Preview Data": "配置导入设置并预览数据",
    "Files to import": "要导入的文件",
    "Google Cloud Storage": "Google Cloud Storage",
    "Import your data from cloud storage providers": "从云存储提供商导入你的数据",
    "Save": "保存",
    "Select an option": "选择一个选项",
    "Videos": "视频",
    "When pre-signed URLs are enabled, all data bypasses the platform and user browsers directly read data from storage": "启用预签名 URL 后，所有数据都绕过平台，用户浏览器将直接从存储读取数据"
  },
  "webhooks": {
    "Add Webhook": "添加 Webhook",
    "Add your first webhook": "添加你的第一个 Webhook",
    "Cancel": "取消",
    "Delete": "删除",
    "Delete Webhook": "删除 Webhook",
    "Edit": "编辑",
    "Learn more": "了解更多",
    "New Webhook": "新 Webhook",
    "Save Changes": "保存更改",
    "Webhooks": "网络钩子",
    "Webhooks Settings": "网络钩子设置"
  },
  "organization": {
    "Add Members": "添加成员",
    "API Token Settings": "API 令牌设置",
    "API Tokens Settings": "API 令牌设置",
    "Copied!": "已复制！",
    "Create a Model": "创建模型",
    "Email": "电子邮箱",
    "Invite members": "邀请成员",
    "Last Activity": "最后活动时间",
    "Learn more": "了解更多",
    "Organization": "组织",
    "People": "成员"
  },
  "templates": {
    "Activity Recognition": "活动识别",
    "ASR Hypotheses Selection": "ASR 假设选择",
    "Automatic Speech Recognition": "自动语音识别",
    "Automatic Speech Recognition using Segments": "使用片段的自动语音识别",
    "Chat": "聊天",
    "Community Contributions": "社区贡献",
    "Computer Vision": "计算机视觉",
    "Conversational AI": "对话式 AI",
    "Freeform Metadata": "自由格式元数据",
    "Generative AI": "生成式 AI",
    "Go Back": "返回",
    "Go to Home": "前往首页",
    "Here’s a few things you can try:": "你可以尝试以下操作：",
    "Image Captioning": "图像描述",
    "Image Classification": "图像分类",
    "Inventory Tracking": "库存跟踪",
    "Keypoint Labeling": "关键点标注",
    "Label Studio": "Label Studio",
    "Light": "浅色",
    "Medical Image Classification with Bounding Boxes": "带边界框的医学图像分类",
    "Multi-page document annotation": "多页文档标注",
    "Named Entity Recognition": "命名实体识别",
    "Natural Language Processing": "自然语言处理",
    "Object Detection with Bounding Boxes": "边界框目标检测",
    "OCR Labeling for PDFs": "PDF OCR 标注",
    "Optical Character Recognition": "光学字符识别",
    "Ranking & Scoring": "排序与打分",
    "Response Selection": "响应选择",
    "Semantic Segmentation with Masks": "掩码语义分割",
    "Semantic Segmentation with Polygons": "多边形语义分割",
    "Structured Data Parsing": "结构化数据解析",
    "Tabular Data": "表格数据",
    "Time Series Analysis": "时间序列分析",
    "Uh oh, this page doesn’t exist.": "哎呀，这个页面不存在。",
    "Videos": "视频",
    "Visual Genome": "视觉基因组",
    "Visual Question Answering": "视觉问答"
  },
  "generic": {
    "Apply your AWS spend to Label Studio Enterprise": "将你的 AWS 承诺消费用于 Label Studio 企业版",
    "Assign roles to your team using Label Studio Enterprise and control access to sensitive data at the project and workspace levels.": "使用 Label Studio 企业版为团队分配角色，并在项目和工作区级别控制对敏感数据的访问。",
    "By Time": "按时间",
    "Cancel delete": "取消删除",
    "Combine automation plus human supervision to evaluate and ensure LLM quality in the Enterprise platform.": "在企业版平台中结合自动化与人工监督，评估并确保 LLM 质量。",
    "Copied": "已复制",
    "Copied!": "已复制！",
    "data()": "数据()",
    "Delete": "删除",
    "Did you know?": "你知道吗？",
    "Docs": "文档",
    "Edit": "编辑",
    "Enable Single Sign-On for your team using SAML, SCIM2 or LDAP with Label Studio Enterprise.": "使用 Label Studio 企业版的 SAML、SCIM2 或 LDAP 为你的团队启用单点登录。",
    "Enterprise": "企业版",
    "Evaluate GenAI models": "评估 GenAI 模型",
    "First name": "名",
    "Go back": "返回",
    "Group by Label": "按标签分组",
    "Home": "首页",
    "It looks like your team is growing!": "看起来你的团队正在壮大！",
    "Join the community": "加入社区",
    "Label Studio": "Label Studio",
    "Label Studio Enterprise is now available on the AWS Marketplace so you can use your committed spend to streamline data labeling workflows.": "Label Studio 企业版现已上架 AWS Marketplace，你可以使用已承诺的 AWS 消费额度来简化数据标注工作流。",
    "Label Studio Logo": "Label Studio 标志",
    "Label Studio Playground": "Label Studio Playground",
    "Label the video:": "标注视频：",
    "Label timeline spans:": "标注时间片段：",
    "Labeled regions will appear here": "已标注区域将显示在这里",
    "Labeling Instructions": "标注说明",
    "Last name": "姓",
    "Learn more": "了解更多",
    "Log Out": "退出登录",
    "Model": "模型",
    "Organization": "组织",
    "Playback Settings": "播放设置",
    "Projects": "项目",
    "Redo": "重做",
    "Save": "保存",
    "Save time with Auto-Labeling": "使用自动标注节省时间",
    "Saved!": "已保存！",
    "Select an option": "选择一个选项",
    "Sequential sampling": "顺序采样",
    "Settings": "设置",
    "Share knowledge with the community": "与社区分享经验",
    "Slack Community": "Slack 社区",
    "Spectrogram Settings": "频谱图设置",
    "Start labeling and track your results": "开始标注并跟踪你的结果",
    "Submit annotation": "提交标注",
    "Try Label Studio Starter Cloud, optimized for small teams and projects.": "试试为小团队和项目优化的 Label Studio Starter Cloud。",
    "Undo": "撤销",
    "Use automation to instantly label large-scale datasets without sacrificing quality in the Enterprise platform.": "使用自动化可即时标注大规模数据集，同时在企业版平台中不牺牲质量。",
    "using this panel": "使用此面板",
    "Want to simplify and secure logging in?": "想让登录更简单、更安全吗？",
    "You can connect ML models using the backend SDK to save time with pre-labeling or active learning.": "你可以通过后端 SDK 连接 ML 模型，利用预标注或主动学习来节省时间。",
    "You can increase the quality of your labeled data with reviewer workflows and task agreement scores using Label Studio Enterprise.": "你可以使用 Label Studio 企业版的审核流程和任务一致性评分来提高标注数据质量。"
  }
};
  var ATTRIBUTE_NAMES = ["placeholder", "title", "aria-label", "aria-placeholder", "alt", "data-tooltip", "data-title", "value"];
  var SKIP_TAGS = { SCRIPT: true, STYLE: true, CODE: true, PRE: true, TEXTAREA: true };
  var exactMap = Object.create(null);
  var normalizedMap = Object.create(null);
  var phrasePairs = [];

  Object.keys(MODULE_MAPS).forEach(function (moduleName) {
    var moduleMap = MODULE_MAPS[moduleName];
    Object.keys(moduleMap).forEach(function (source) {
      var target = moduleMap[source];
      exactMap[source] = target;
      normalizedMap[normalizeText(source)] = target;
      if (source.length >= 12 && source.indexOf("{") === -1 && source.indexOf("${") === -1) {
        phrasePairs.push([source, target]);
      }
    });
  });

  phrasePairs.sort(function (left, right) {
    return right[0].length - left[0].length;
  });

  function normalizeText(text) {
    return String(text || "").replace(/\s+/g, " ").trim();
  }

  function shouldSkipElement(element) {
    if (!element) {
      return false;
    }
    if (SKIP_TAGS[element.tagName]) {
      return true;
    }
    if (element.closest("script, style, code, pre, textarea")) {
      return true;
    }
    return !!element.closest("[data-no-translate], [data-translation-skip], .task-text, .lsf-task-data");
  }

  function translateText(text) {
    if (!text) {
      return text;
    }
    var trimmed = text.trim();
    if (!trimmed) {
      return text;
    }
    var translated = exactMap[trimmed] || normalizedMap[normalizeText(trimmed)] || null;
    if (translated) {
      return text.replace(trimmed, translated);
    }
    var updated = text;
    phrasePairs.forEach(function (pair) {
      if (updated.indexOf(pair[0]) !== -1) {
        updated = updated.split(pair[0]).join(pair[1]);
      }
    });
    updated = updated.replace(/\b1 minute ago\b/g, "1 分钟前");
    updated = updated.replace(/\b(\d+)\s+minutes ago\b/g, "$1 分钟前");
    updated = updated.replace(/\b1 hour ago\b/g, "1 小时前");
    updated = updated.replace(/\b(\d+)\s+hours ago\b/g, "$1 小时前");
    updated = updated.replace(/\bless than a minute ago\b/g, "刚刚");
    updated = updated.replace(/\bseconds ago\b/g, "几秒前");
    updated = updated.replace(/\b(\d+) of (\d+) Tasks \(([^)]+)\)/g, "$1 / $2 任务 ($3)");
    updated = updated.replace(/\bTasks:\s*([0-9]+\s*\/\s*[0-9]+)\b/g, "任务：$1");
    updated = updated.replace(/\bSubmitted annotations:\s*(\d+)\b/g, "已提交标注：$1");
    updated = updated.replace(/\bPredictions:\s*(\d+)\b/g, "预测：$1");
    updated = updated.replace(/\(opens in a new tab\)/g, "(在新标签页中打开)");
    return updated;
  }

  function translateDocumentTitle() {
    if (!document.title) {
      return;
    }
    var nextTitle = translateText(document.title);
    if (nextTitle !== document.title) {
      document.title = nextTitle;
    }
  }

  function processTextNode(node) {
    if (!node || !node.parentElement || shouldSkipElement(node.parentElement)) {
      return;
    }
    var nextValue = translateText(node.nodeValue);
    if (nextValue !== node.nodeValue) {
      node.nodeValue = nextValue;
    }
  }

  function processAttributes(element) {
    if (!(element instanceof Element) || shouldSkipElement(element)) {
      return;
    }
    ATTRIBUTE_NAMES.forEach(function (attr) {
      if (!element.hasAttribute(attr)) {
        return;
      }
      var currentValue = element.getAttribute(attr);
      var nextValue = translateText(currentValue);
      if (nextValue !== currentValue) {
        element.setAttribute(attr, nextValue);
        if (attr === "value" && "value" in element) {
          element.value = nextValue;
        }
      }
    });
  }

  function walk(root) {
    if (!root) {
      return;
    }
    if (root.nodeType === Node.TEXT_NODE) {
      processTextNode(root);
      return;
    }
    if (root.nodeType !== Node.ELEMENT_NODE || shouldSkipElement(root)) {
      return;
    }
    processAttributes(root);
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        if (!node.parentElement || shouldSkipElement(node.parentElement)) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    while (walker.nextNode()) {
      processTextNode(walker.currentNode);
    }
  }

  function applyOverlay() {
    translateDocumentTitle();
    walk(document.body);
  }

  function hookHistory(methodName) {
    var original = history[methodName];
    history[methodName] = function () {
      var result = original.apply(this, arguments);
      window.setTimeout(applyOverlay, 0);
      return result;
    };
  }

  var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.type === "characterData") {
        processTextNode(mutation.target);
        return;
      }
      if (mutation.type === "attributes") {
        processAttributes(mutation.target);
        return;
      }
      mutation.addedNodes.forEach(function (node) {
        walk(node);
      });
    });
  });

  hookHistory("pushState");
  hookHistory("replaceState");
  window.addEventListener("popstate", function () {
    window.setTimeout(applyOverlay, 0);
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyOverlay, { once: true });
  } else {
    applyOverlay();
  }

  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ATTRIBUTE_NAMES
  });
})();
