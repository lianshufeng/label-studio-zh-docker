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
    "Annotations Submitted": "已提交标注",
    "Audio Controls": "音频控制",
    "Auto Detect": "自动检测",
    "Auto-Label Tasks": "自动标注任务",
    "Brush Tool": "画笔工具",
    "Cancel": "取消",
    "Copied!": "已复制！",
    "Create a copy of the selected region": "创建所选区域的副本",
    "Create a relation between selected regions": "在所选区域之间创建关系",
    "Create Account": "创建账户",
    "Create New Token": "创建新 令牌",
    "Create Region Relation": "创建区域关系",
    "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.": "自定义键盘快捷键以加快工作流程。 点击下方任意快捷键即可分配最适合你的新按键组合。",
    "Cycle Regions": "循环切换区域",
    "Data Manager": "数据管理",
    "Decrease Tool Size": "减小工具大小",
    "Delete All Regions": "删除所有区域",
    "Delete currently selected region": "删除当前选中的区域",
    "Delete Segment": "删除片段",
    "Delete Selected Region": "删除所选区域",
    "Delete selected segment": "删除所选片段",
    "Did you know?": "你知道吗？",
    "Docs": "文档",
    "Documentation": "文档",
    "Draw a rotated rectangle using 3-point selection": "使用三点选择绘制旋转矩形",
    "Duplicate Region": "复制区域",
    "E-mail": "电子邮箱",
    "Edit metadata for selected region": "编辑所选区域元数据",
    "Edit Region Metadata": "编辑区域元数据",
    "Ellipse Tool": "椭圆工具",
    "Email Preferences": "邮件偏好",
    "Eraser Tool": "橡皮擦工具",
    "Exit Region Mode": "退出区域模式",
    "Export": "导出",
    "Extend Left": "向左扩展",
    "Extend Right": "向右扩展",
    "Extend the region to the left": "向左扩展区域",
    "Extend the region to the right": "向右扩展区域",
    "Failed to save imported hotkeys": "保存导入的快捷键失败",
    "First Frame": "第一帧",
    "First Name": "名",
    "Focus Closed Task": "聚焦已关闭任务",
    "Focus First Region": "聚焦第一个区域",
    "Focus Next Task": "聚焦下一任务",
    "Focus on the closed task column": "聚焦到已关闭任务列",
    "Focus on the open task column": "聚焦到开放任务列",
    "Focus Open Task": "聚焦开放任务",
    "Focus Previous Task": "聚焦上一任务",
    "Great news!": "好消息！",
    "Hop Backward": "快速向后跳转",
    "Hop backward quickly": "快速向后跳转",
    "Hop Forward": "快速向前跳转",
    "Hop forward quickly": "快速向前跳转",
    "Hotkeys imported successfully": "快捷键导入成功",
    "Hotkeys JSON": "快捷键 JSON",
    "How did you hear about Label Studio?": "你是如何了解到 Label Studio 的？",
    "Human Signal Logo": "Human Signal 标志",
    "Image Gallery Navigation": "图库导航",
    "Import": "导入",
    "Import Error": "导入错误",
    "Import Hotkeys": "导入快捷键",
    "Increase Tool Size": "增大工具大小",
    "Jump to first frame": "跳转到第一帧",
    "Jump to last frame": "跳转到最后一帧",
    "Jump to next keyframe": "跳转到下一个关键帧",
    "Jump to previous keyframe": "跳转到上一个关键帧",
    "Keep me logged in this browser": "在此浏览器中保持登录",
    "Key Point Tool": "关键点工具",
    "Label Studio": "Label Studio",
    "Label Studio Logo": "Label Studio 标志",
    "Last Frame": "最后一帧",
    "Last Name": "姓",
    "Learn more": "了解更多",
    "Legacy Token": "旧版令牌",
    "Lock Region": "锁定区域",
    "Log in": "登录",
    "Magic Wand": "魔棒工具",
    "Manage your access tokens securely": "安全管理你的访问令牌",
    "Membership Info": "成员信息",
    "Minimize or expand bulk actions sidebar": "最小化或展开批量操作侧边栏",
    "Move focus to the first focusable region": "将焦点移动到第一个可聚焦区域",
    "Move focus to the next task": "将焦点移动到下一任务",
    "Move focus to the previous task": "将焦点移动到上一任务",
    "Move Tool": "移动工具",
    "My Account": "我的账户",
    "My role": "我的角色",
    "Navigate to the next phrase in paragraph view": "在段落视图中导航到下一短语",
    "Navigate to the next region within current phrase": "导航到当前短语中的下一个区域",
    "Navigate to the previous phrase in paragraph view": "在段落视图中导航到上一短语",
    "Navigate to the previous region within current phrase": "导航到当前短语中的上一个区域",
    "New Auth Token": "新认证令牌",
    "Next Image": "下一张图像",
    "Next Keyframe": "下一个关键帧",
    "Next Phrase": "下一短语",
    "Next Region in Phrase": "短语中的下一个区域",
    "Owner": "所有者",
    "Pan around the image": "在图像中平移",
    "Pan Image": "平移图像",
    "Paragraph Navigation": "段落导航",
    "Personal Access Token": "个人访问令牌",
    "Personal Info": "个人信息",
    "Please enter JSON data to import": "请输入要导入的 JSON 数据",
    "Polygon Tool": "多边形工具",
    "Previous Image": "上一张图像",
    "Previous Keyframe": "上一个关键帧",
    "Previous Phrase": "上一短语",
    "Previous Region in Phrase": "短语中的上一个区域",
    "Projects contributed to": "参与项目数",
    "Rectangle Tool": "矩形工具",
    "Redo": "重做",
    "Redo previously undone action": "重做刚刚撤销的操作",
    "Region Management": "区域管理",
    "Registration date": "注册日期",
    "Remove all regions": "删除所有区域",
    "Reset Hotkeys to Defaults?": "将快捷键重置为默认值？",
    "Reset to Defaults": "恢复默认",
    "Revoke Token": "吊销令牌",
    "Rewind 1 Second": "快退 1 秒",
    "Rewind the audio by 1 second": "将音频快退 1 秒",
    "Rotate Left": "向左旋转",
    "Rotate Right": "向右旋转",
    "Rotate the image 90° to the left": "将图像向左旋转 90°",
    "Rotate the image 90° to the right": "将图像向右旋转 90°",
    "Save": "保存",
    "See all templates": "查看所有模板",
    "Seek Backward": "向后定位",
    "Seek Forward": "向前定位",
    "Seek video backward": "向后定位视频",
    "Seek video forward": "向前定位视频",
    "Select All and Annotate": "全选并标注",
    "Select all text in current phrase and create annotation": "选择当前短语中的全部文本并创建标注",
    "Select an option": "选择一个选项",
    "Select the brush tool": "选择画笔工具",
    "Select the ellipse tool": "选择椭圆工具",
    "Select the eraser tool": "选择橡皮擦工具",
    "Select the key point annotation tool": "选择关键点标注工具",
    "Select the magic wand tool for smart region selection": "选择魔棒工具进行智能区域选择",
    "Select the move tool to reposition annotations": "选择移动工具以重新定位标注",
    "Select the polygon annotation tool": "选择多边形标注工具",
    "Select the rectangle annotation tool": "选择矩形标注工具",
    "Shortcuts for common annotation tasks like submit, skip, undo and redo": "用于提交、跳过、撤销和重做等常见标注任务的快捷键",
    "Shortcuts for controlling audio playback and navigation": "用于控制音频播放与导航的快捷键",
    "Shortcuts for controlling tools panel when labeling images": "标注图像时控制工具面板的快捷键",
    "Shortcuts for controlling video playback and navigation": "用于控制视频播放与导航的快捷键",
    "Shortcuts for creating, selecting and manipulating annotation regions": "用于创建、选择和操作标注区域的快捷键",
    "Shortcuts for manipulating time series data regions": "操作时间序列数据区域的快捷键",
    "Shortcuts for navigating and managing tasks in Project's Data Manager": "在项目数据管理中导航和管理任务的快捷键",
    "Shortcuts for navigating between images in multi-image tasks": "用于在多图任务中切换图像的快捷键",
    "Shortcuts for navigating phrases and regions in paragraph/dialogue view": "用于在段落/对话视图中切换短语和区域的快捷键",
    "Shrink Left": "向左收缩",
    "Shrink Right": "向右收缩",
    "Shrink the region from the left": "从左侧收缩区域",
    "Shrink the region from the right": "从右侧收缩区域",
    "Sign up": "注册",
    "Skip Task": "跳过任务",
    "Skip the current task": "跳过当前任务",
    "Step Back": "后退一帧",
    "Step back one frame": "后退一帧",
    "Step Forward": "前进一帧",
    "Step forward one frame": "前进一帧",
    "Submit Annotation": "提交标注",
    "Submit the current annotation": "提交当前标注",
    "Subscribe to HumanSignal news and tips from Heidi": "订阅 Heidi 的 HumanSignal 新闻和提示",
    "There's an Enterprise version of Label Studio packed with more features and automation to label data faster while ensuring the highest quality.": "Label Studio 企业版提供了更多功能和自动化能力，可更快地标注数据并确保最高质量。",
    "Time Series Controls": "时间序列控制",
    "Toggle All Region Visibility": "切换所有区域可见性",
    "Toggle audio playback": "切换音频播放",
    "Toggle Bulk Sidebar": "切换批量侧边栏",
    "Toggle Region Visibility": "切换区域可见性",
    "Toggle video playback": "切换视频播放",
    "Token Expiry Date": "令牌过期时间",
    "Undo": "撤销",
    "Undo last action": "撤销上一步操作",
    "Unselect Region": "取消选择区域",
    "Use the auto-detect tool to automatically suggest regions": "使用自动检测工具自动建议区域",
    "User ID": "用户 ID",
    "Video Controls": "视频控制",
    "View next image": "查看下一张图像",
    "View previous image": "查看上一张图像",
    "Zoom In": "放大",
    "Zoom in on the image": "放大图像",
    "Zoom Out": "缩小",
    "Zoom out of the image": "缩小图像",
    "Zoom to 100%": "缩放至 100%",
    "Zoom to actual image size (100%)": "缩放到图像实际大小（100%）",
    "Zoom to Fit": "缩放至适合",
    "Zoom to fit the full image in view": "缩放以完整显示整张图像"
  },
  "home": {
    "* Create New Project *": "* 创建新 项目 *",
    "* Import Project *": "* 导入项目 *",
    "API Documentation": "API 文档",
    "Azure Blob Storage": "Azure Blob 存储",
    "Choose a dataset from your computer to get started": "从你的电脑选择一个数据集以开始使用",
    "Connect Cloud Storage": "连接云存储",
    "Connect your cloud storage or upload files from your computer": "连接你的云存储或从电脑上传文件",
    "Create new project": "创建新项目",
    "Create Project": "创建项目",
    "Create your first project": "创建你的第一个项目",
    "Documentation": "文档",
    "Error occurred while loading data": "加载数据时发生错误",
    "Failed to load data": "加载数据失败",
    "Google Cloud Storage": "Google Cloud Storage",
    "Home": "首页",
    "Home | Label Studio": "首页 | Label Studio",
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
    "Welcome 👋": "欢迎 👋",
    "You can save time managing infrastructure and upgrades, plus access more features for automation, quality, and team management, by using the Enterprise cloud service.": "使用企业云服务，你可以节省基础设施与升级维护时间，并获得更多自动化、质量管理和团队管理功能。"
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
    "Create new project": "创建新项目",
    "Create one and start labeling your data.": "创建一个并开始标注你的数据。",
    "Create Project": "创建项目",
    "Custom template": "自定义模板",
    "Data Import": "数据导入",
    "Dataset URL": "数据集 URL",
    "delete label": "删除 label",
    "Description": "描述",
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
    "Projects | Label Studio": "项目 | Label Studio",
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
    "You can control access to specific projects and workspaces for internal team members and external annotators using Label Studio Enterprise.": "使用 Label Studio 企业版，你可以为内部团队成员和外部标注员控制特定项目和工作区的访问权限。",
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
    "Rename": "重命名",
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
    "Breast Cancer Mammogram Classification": "乳腺癌乳腺摄影分类",
    "Cancel": "取消",
    "Chatbot Model Assessment": "聊天机器人模型评估",
    "Choose similar images:": "选择相似图像：",
    "Create relations between regions": "在区域之间创建关系",
    "Delete": "删除",
    "Delete selected region": "删除所选区域",
    "Enable and select which set of predictions to use for prelabeling.": "启用并选择要用于预标注的那组预测结果。",
    "Enterprise": "企业版",
    "Generated Images": "生成的图像",
    "Human Preference collection for RLHF": "用于 RLHF 的人工偏好收集",
    "Incorrect Amount": "金额错误",
    "Incorrect Name": "名称错误",
    "Labeling Instructions": "标注说明",
    "Labeling Interface": "标注界面",
    "Labeling Interface Settings": "标注界面设置",
    "Learn more": "了解更多",
    "LLM Ranker": "LLM 排序器",
    "Model": "模型",
    "No model or predictions available": "没有可用的模型或预测",
    "No predictions uploaded yet": "尚未上传任何预测结果",
    "Organization": "组织",
    "Please provide additional comments": "请提供额外评论",
    "Please read the passage": "请阅读这段内容",
    "Predictions": "预测",
    "Predictions Settings": "预测设置",
    "Prelabeling": "预标注",
    "Rate this article": "给这篇文章评分",
    "Regions": "区域",
    "Save": "保存",
    "Saved!": "已保存！",
    "See a log of user actions for this annotation": "查看此标注的用户操作日志",
    "Select a text span answering the following question:": "选择一个文本片段来回答以下问题：",
    "Select document related to the query:": "选择与查询相关的文档：",
    "Select label and click the image to start": "选择标签并点击图像开始",
    "Select predictable region spans in time series:": "选择时间序列中的可预测区域跨度：",
    "Select text to correct": "选择要纠正的文本",
    "Select which predictions or which model you want to use:": "选择你要使用的预测结果或模型：",
    "Show before labeling": "标注前显示",
    "Supervised Language Model Fine-tuning": "监督式语言模型微调",
    "The instruction field supports HTML markup and it allows use of images, iframes (pdf).": "说明字段支持 HTML 标记，并允许使用图片、iframe（PDF）。",
    "Typo": "错别字",
    "Upload predictions to automatically prelabel your data and speed up annotation. Import predictions from multiple model versions to compare their performance, or connect live models from the Model page to generate predictions on demand.": "上传预测结果以自动预标注你的数据并加快标注。你可以从多个模型版本导入预测结果以比较其表现，或从模型页面连接实时模型按需生成预测。",
    "Use predictions to prelabel tasks": "使用预测结果对任务进行预标注",
    "View annotation activity": "查看标注活动",
    "Visual Ranker": "视觉排序器",
    "What are the key benefits of using Reinforcement Learning from Human Feedback (RLHF) for dataset collection in the context of Large Language Model (LLM) generation?": "在大语言模型（LLM）生成场景中，使用基于人类反馈的强化学习（RLHF）进行数据集收集的主要优势是什么？",
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
    "Browse Templates": "浏览模板",
    "Cancel": "取消",
    "Close": "关闭",
    "Cloud Storage": "云存储",
    "Cloud Storage Settings": "云存储设置",
    "Color": "颜色",
    "Configure the labeling interface with tags.": "使用标签配置标注界面。",
    "Configure the labeling interface with tags. See all tags.": "使用标签配置标注界面。查看所有标签。",
    "Configure your AWS S3 connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 AWS S3 连接",
    "Configure your Azure Blob Storage connection using Service Principal authentication for enhanced security (proxy only)": "使用 Service Principal 身份验证配置你的 Azure Blob 存储连接以增强安全性（仅代理）",
    "Configure your Azure Blob Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Azure Blob 存储连接",
    "Configure your Databricks Unity Catalog Volumes connection with all required settings (proxy only)": "使用所有必需设置配置你的 Databricks Unity Catalog Volumes 连接（仅代理）",
    "Configure your Google Cloud Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Google Cloud Storage 连接",
    "Configure your Google Cloud Storage connection with Workload Identity Federation authentication (proxy only)": "使用 Workload Identity Federation 身份验证配置你的 Google Cloud Storage 连接（仅代理）",
    "Configure your local file storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的本地文件存储连接",
    "Configure your Redis storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置你的 Redis 存储连接",
    "Connect a machine learning model to generate live predictions for your project. Compare predictions, accelerate labeling with automatic prelabeling, and direct your team to the most impactful tasks through active learning.": "连接机器学习模型，为你的项目生成实时预测。比较预测结果，使用自动预标注加速标注，并通过主动学习让团队优先处理最有价值的任务。",
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
    "Random sampling": "随机采样",
    "Redis Storage": "Redis 存储",
    "Remember Selected Tool": "记住所选工具",
    "Reset Cache": "重置缓存",
    "Reset Cache may help in cases like if you are unable to modify the labeling configuration due to validation errors concerning existing labels, but you are confident that the labels don't exist. You can use this action to reset the cache and try again.": "如果由于现有标签的校验错误而无法修改标注配置，但你确认这些标签并不存在，重置缓存可能会有帮助。你可以使用此操作重置缓存并重试。",
    "Save": "保存",
    "Save Changes": "保存更改",
    "Save general settings": "保存常规设置",
    "Save machine learning form": "保存机器学习表单",
    "Save machine learning settings": "保存机器学习设置",
    "Save storage settings": "保存存储设置",
    "Saved!": "已保存！",
    "See all": "查看全部",
    "See all tags.": "查看所有标签。",
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
    "Setup integrations that subscribe to certain events using Webhooks. When an event is triggered, Label Studio sends an HTTP POST request to the configured webhook URL.": "设置使用 Webhook 订阅特定事件的集成。当事件被触发时，Label Studio 会向已配置的 Webhook URL 发送 HTTP POST 请求。",
    "Webhooks": "网络钩子",
    "Webhooks Settings": "网络钩子设置"
  },
  "organization": {
    "Add Members": "添加成员",
    "API Token Settings": "API 令牌设置",
    "API Tokens Settings": "API 令牌设置",
    "Copied!": "已复制！",
    "Copy link": "复制链接",
    "Create a Model": "创建模型",
    "Email": "电子邮箱",
    "Invite members": "邀请成员",
    "Last Activity": "最后活动时间",
    "Learn more": "了解更多",
    "Organization": "组织",
    "People": "成员",
    "Reset Link": "重置链接"
  },
  "templates": {
    "Activity Recognition": "活动识别",
    "ASR Hypotheses Selection": "ASR 假设选择",
    "Automatic Speech Recognition": "自动语音识别",
    "Automatic Speech Recognition using Segments": "使用片段的自动语音识别",
    "Breast Cancer Mammogram Classification": "乳腺癌乳腺摄影分类",
    "Chat": "聊天",
    "Chatbot Model Assessment": "聊天机器人模型评估",
    "Community Contributions": "社区贡献",
    "Computer Vision": "计算机视觉",
    "Content Moderation": "内容审核",
    "Content-based Image Retrieval": "基于内容的图像检索",
    "Conversational AI": "对话式 AI",
    "Conversational Analysis": "对话分析",
    "Coreference Resolution & Entity Linking": "共指消解与实体链接",
    "Document Retrieval": "文档检索",
    "Freeform Metadata": "自由格式元数据",
    "Generative AI": "生成式 AI",
    "Go Back": "返回",
    "Go to Home": "前往首页",
    "Here’s a few things you can try:": "你可以尝试以下操作：",
    "HTML Entity Recognition": "HTML 实体识别",
    "Human Preference collection for RLHF": "用于 RLHF 的人工偏好收集",
    "Image Captioning": "图像描述",
    "Image Classification": "图像分类",
    "Intent Classification": "意图分类",
    "Intent Classification and Slot Filling": "意图分类与槽位填充",
    "Inventory Tracking": "库存跟踪",
    "Keypoint Labeling": "关键点标注",
    "Label Studio": "Label Studio",
    "Light": "浅色",
    "LLM Ranker": "LLM 排序器",
    "LLM Response Grading": "LLM 回复评分",
    "Machine Translation": "机器翻译",
    "Medical Image Classification with Bounding Boxes": "带边界框的医学图像分类",
    "Multi-page document annotation": "多页文档标注",
    "Named Entity Recognition": "命名实体识别",
    "Natural Language Processing": "自然语言处理",
    "Object Detection with Bounding Boxes": "边界框目标检测",
    "OCR Invoices Pre-NER BIO Format": "OCR 发票预实体识别 BIO 格式",
    "OCR Labeling for PDFs": "PDF OCR 标注",
    "Optical Character Recognition": "光学字符识别",
    "Pairwise classification": "成对分类",
    "Pairwise regression": "成对回归",
    "PDF Classification": "PDF 分类",
    "Question Answering": "问题回答",
    "Ranking & Scoring": "排序与打分",
    "Relation Extraction": "关系抽取",
    "Response Generation": "回复生成",
    "Response Selection": "响应选择",
    "Search Page Ranking": "搜索结果页排序",
    "Semantic Segmentation with Masks": "掩码语义分割",
    "Semantic Segmentation with Polygons": "多边形语义分割",
    "Signal Quality": "信号质量",
    "Signal Quality Detection": "信号质量检测",
    "Sound Event Detection": "声音事件检测",
    "Speaker Segmentation": "说话人分段",
    "Speech Transcription": "语音转写",
    "Structured Data Parsing": "结构化数据解析",
    "Supervised Language Model Fine-tuning": "监督式语言模型微调",
    "Tabular Data": "表格数据",
    "Taxonomy": "分类体系",
    "Text Classification": "文本分类",
    "Text Summarization": "文本摘要",
    "Text-to-Image Generation": "文生图生成",
    "Time Series Analysis": "时间序列分析",
    "Time Series Forecasting": "时间序列预测",
    "Uh oh, this page doesn’t exist.": "哎呀，这个页面不存在。",
    "Video Classification": "视频分类",
    "Video Frame Classification": "视频帧分类",
    "Video Object Tracking": "视频目标跟踪",
    "Video Timeline Segmentation": "视频时间轴分割",
    "Videos": "视频",
    "Visual Genome": "视觉基因组",
    "Visual Question Answering": "视觉问答",
    "Visual Ranker": "视觉排序器"
  },
  "generic": {
    "Apply your AWS spend to Label Studio Enterprise": "将你的 AWS 承诺消费用于 Label Studio 企业版",
    "Assign roles to your team using Label Studio Enterprise and control access to sensitive data at the project and workspace levels.": "使用 Label Studio 企业版为团队分配角色，并在项目和工作区级别控制对敏感数据的访问。",
    "Audio Segmentation": "音频分割",
    "Auto Detect": "自动检测",
    "By Time": "按时间",
    "Cancel delete": "取消删除",
    "Close": "关闭",
    "Combine automation plus human supervision to evaluate and ensure LLM quality in the Enterprise platform.": "在企业版平台中结合自动化与人工监督，评估并确保 LLM 质量。",
    "Copied": "已复制",
    "Copied!": "已复制！",
    "Create relations between regions": "在区域之间创建关系",
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
    "Hop backward": "快速向后跳转",
    "Hop forward": "快速向前跳转",
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
    "Link regions to define relationships between them": "链接区域以定义它们之间的关系",
    "Lock Region": "锁定区域",
    "Log Out": "退出登录",
    "Magic Wand": "魔棒工具",
    "Model": "模型",
    "Organization": "组织",
    "Pan Image": "平移图像",
    "Playback Settings": "播放设置",
    "Press Shift + Enter to Add": "按 Shift + Enter 添加",
    "Projects": "项目",
    "Redo": "重做",
    "Rotate Left": "向左旋转",
    "Rotate Right": "向右旋转",
    "Save": "保存",
    "Save time with Auto-Labeling": "使用自动标注节省时间",
    "Saved!": "已保存！",
    "Select a region to view its properties, metadata and available actions": "选择一个区域以查看其属性、元数据和可用操作",
    "Select an option": "选择一个选项",
    "Sequential sampling": "顺序采样",
    "Settings": "设置",
    "Share knowledge with the community": "与社区分享经验",
    "Show all authors": "显示所有作者",
    "Slack Community": "Slack 社区",
    "Spectrogram Settings": "频谱图设置",
    "Start labeling and track your results": "开始标注并跟踪你的结果",
    "Step forward": "前进一帧",
    "Submit annotation": "提交标注",
    "Try Label Studio Starter Cloud, optimized for small teams and projects.": "试试为小团队和项目优化的 Label Studio Starter Cloud。",
    "Undo": "撤销",
    "Use automation to instantly label large-scale datasets without sacrificing quality in the Enterprise platform.": "使用自动化可即时标注大规模数据集，同时在企业版平台中不牺牲质量。",
    "using this panel": "使用此面板",
    "View region details": "查看区域详情",
    "Want to simplify and secure logging in?": "想让登录更简单、更安全吗？",
    "You can connect ML models using the backend SDK to save time with pre-labeling or active learning.": "你可以通过后端 SDK 连接 ML 模型，利用预标注或主动学习来节省时间。",
    "You can control access to specific projects and workspaces for internal team members and external annotators using Label Studio Enterprise.": "使用 Label Studio 企业版，你可以为内部团队成员和外部标注员控制特定项目和工作区的访问权限。",
    "You can increase the quality of your labeled data with reviewer workflows and task agreement scores using Label Studio Enterprise.": "你可以使用 Label Studio 企业版的审核流程和任务一致性评分来提高标注数据质量。",
    "You can save time managing infrastructure and upgrades, plus access more features for automation, quality, and team management, by using the Enterprise cloud service.": "使用企业云服务，你可以节省基础设施与升级维护时间，并获得更多自动化、质量管理和团队管理功能。",
    "Zoom In": "放大",
    "Zoom Out": "缩小",
    "Zoom to fit": "缩放至适合"
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
    updated = updated.replace(/^Home \| Label Studio$/g, "首页 | Label Studio");
    updated = updated.replace(/^Projects \| Label Studio$/g, "项目 | Label Studio");
    updated = updated.replace(/^Create new project$/g, "创建新项目");
    updated = updated.replace(/^Cancel project creation$/g, "取消项目创建");
    updated = updated.replace(/^Description$/g, "描述");
    updated = updated.replace(/^Optional description of your project$/g, "项目可选描述");
    updated = updated.replace(/See all tags/g, "查看所有标签");
    updated = updated.replace(/See all/g, "查看全部");
    updated = updated.replace(/Add Webhook/g, "添加网络钩子");
    updated = updated.replace(/Add your first Webhook/g, "添加你的第一个网络钩子");
    updated = updated.replace(
      /You can control access to specific projects and workspaces for internal team members and external annotators using Label Studio 企业版\./g,
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
    var elementWalker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT);
    while (elementWalker.nextNode()) {
      processAttributes(elementWalker.currentNode);
    }
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

  function scheduleApplyOverlay() {
    [0, 120, 400, 1000].forEach(function (delay) {
      window.setTimeout(applyOverlay, delay);
    });
  }

  function hookHistory(methodName) {
    var original = history[methodName];
    history[methodName] = function () {
      var result = original.apply(this, arguments);
      scheduleApplyOverlay();
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
    scheduleApplyOverlay();
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scheduleApplyOverlay, { once: true });
  } else {
    scheduleApplyOverlay();
  }

  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ATTRIBUTE_NAMES
  });
})();
