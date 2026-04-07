(function () {
  "use strict";

  var config = window.LS_ZH_OVERLAY || {};

  if (config.enabled === false) {
    return;
  }

  var MODULE_MAPS = {
  auth: {
    "Access Token": "访问令牌",
    "Log in": "登录",
    "Learn more": "了解更多",
    "My Account": "我的账户",
    "Personal Access Token": "个人访问令牌",
    "Account & Settings": "账户和设置",
    "Data Manager": "数据管理",
    "Email Preferences": "邮件偏好",
    "Membership Info": "成员信息",
    "Sign up": "注册",
    "Docs": "文档",
    "Export": "导出",
    "Import": "导入",
    "Select an option": "选择一个选项",
    "Customize your keyboard shortcuts to speed up your workflow. Click on any hotkey below to assign a new key combination that works best for you.": "自定义键盘快捷键以提升工作效率。点击下方任意快捷键即可分配更适合您的新组合键。",
    "Create Account": "创建账户",
    "Label Studio Logo": "标签工作室标志",
    "Did you know?": "你可知道？",
    "Create a copy of the selected region": "创建所选区域的副本",
    "First Name": "名字",
    "Label Studio now has a Starter Cloud offering optimized for small teams and projects.": "Label Studio 现在拥有针对小型团队和项目进行优化的 Starter Cloud 产品。",
    "Last Name": "姓氏",
    "Save": "保存",
    "Select all text in current phrase and create annotation": "选择当前短语中的所有文本并创建注释",
    "Shortcuts for common annotation tasks like submit, skip, undo and redo": "提交、跳过、撤消和重做等常见注释任务的快捷方式",
    "Shortcuts for navigating and managing tasks in Project's Data Manager": "在项目数据管理器中导航和管理任务的快捷方式",
    "Copy your new access token from below and keep it secure.": "请从下方复制新的访问令牌并妥善保管。",
    "Create a relation between selected regions": "创建选定区域之间的关系",
    "Delete currently selected region": "删除当前选定的区域",
    "Delete Selected Region": "删除选定区域",
    "Delete selected segment": "删除选定的段",
    "A full-fledged open source solution for data labeling": "一个功能完整的数据标注开源方案",
    "Create Region Relation": "创建区域关系",
    "Delete All Regions": "删除所有区域",
    "Delete Segment": "删除片段",
    "Failed to save imported hotkeys": "无法保存导入的热键",
    "How did you hear about Label Studio?": "您是如何得知 Label Studio 的？",
    "Shortcuts for manipulating time series data regions": "操作时间序列数据区域的快捷方式",
    "You can only have one active token": "您只能拥有一个活跃令牌",
    "Edit metadata for selected region": "编辑所选区域的元数据",
    "Import Hotkeys": "导入快捷键",
    "Reset Hotkeys to Defaults?": "要将快捷键恢复为默认设置吗？",
    "Submit Annotation": "提交标注",
    "Submit the current annotation": "提交当前注释",
    "Unknown error": "未知错误",
    "All hotkeys and settings have been reset to defaults and saved": "所有热键和设置已重置为默认值并保存",
    "Click to edit hotkey": "点击编辑热键",
    "Create New Token": "创建新令牌",
    "Edit Region Metadata": "编辑区域元数据",
    "Great news!": "好消息！",
    "No hotkeys found in the imported data": "导入数据中未找到热键",
    "See all templates": "查看所有模板",
    "Shortcuts for controlling tools panel when labeling images": "标注图像时控制工具面板的快捷方式",
    "Annotations completed by you": "由您完成的注释",
    "Cancel": "取消",
    "Could not load custom hotkeys from server, using cached settings": "无法使用缓存设置从服务器加载自定义热键",
    "Email Address": "邮箱地址",
    "Error loading hotkeys from API:": "从 API 加载热键时出错：",
    "Projects contributed by you": "您贡献的项目",
    "Use this token to authenticate with our API:": "使用此令牌通过我们的 API 进行身份验证：",
    "Annotations Submitted": "已提交的标注",
    "Brought to you by": "由以下团队提供",
    "Keep me logged in this browser": "在此浏览器中保持登录",
    "Organization ID": "组织 ID",
    "We'll send you sms with code if you change your number": "如果您更改号码，我们会向您发送包含代码的短信",
    "Your active organization": "您的活跃组织",
    "Your role": "你的角色",
    "Allow Duplicate": "允许重复",
    "Already have an account?": "已有账户？",
    "Choose": "选择",
    "Created": "已创建",
    "Documentation": "文档",
    "Don't have an account?": "还没有账户？",
    "Hotkeys JSON": "快捷键 JSON",
    "Request error:": "请求错误：",
    "Apply": "应用",
    "Click to set shortcut": "点击设置快捷键",
    "3-Point Rectangle": "三点矩形",
    "Personal Info": "个人信息",
    "Reset to Defaults": "恢复默认",
    "Select the key point annotation tool": "选择关键点标注工具",
    "Select the move tool to reposition annotations": "选择移动工具来重新定位注释",
    "Select the polygon annotation tool": "选择多边形注释工具",
    "Select the rectangle annotation tool": "选择矩形注释工具",
    "Focus Closed Task": "焦点封闭任务",
    "Focus Next Task": "聚焦下一个任务",
    "Focus on the closed task column": "关注已关闭的任务栏",
    "Focus on the open task column": "关注未完成的任务栏",
    "Focus Open Task": "焦点开放任务",
    "Focus Previous Task": "聚焦上一个任务",
    "Move focus to the next task": "将焦点转移到下一个任务",
    "Move focus to the previous task": "将焦点移至上一个任务",
    "Select All and Annotate": "全选并注释",
    "Select the brush tool": "选择画笔工具",
    "Select the ellipse tool": "选择椭圆工具",
    "Select the eraser tool": "选择橡皮擦工具",
    "Select the magic wand tool for smart region selection": "选择魔棒工具进行智能区域选择",
    "Shortcuts for navigating between images in multi-image tasks": "在多图任务中切换图片的快捷方式",
    "Skip Task": "跳过任务",
    "Skip the current task": "跳过当前任务",
    "Decrease Tool Size": "减小工具大小",
    "Increase Tool Size": "增大工具大小",
    "Shortcuts for creating, selecting and manipulating annotation regions": "用于创建、选择和操作注释区域的快捷方式",
    "Step Back": "后退一步",
    "Step Forward": "前进一步",
    "Annotation Actions": "标注操作",
    "Click to record keyboard shortcut": "点击录制键盘快捷键",
    "Show or hide the selected region": "显示或隐藏所选区域",
    "Unselect Region": "取消选择区域",
    "Audio Controls": "音频控制",
    "Auto Detect": "自动检测",
    "Brush Tool": "画笔工具",
    "Cycle Regions": "循环切换区域",
    "Duplicate Region": "复制区域",
    "Ellipse Tool": "椭圆工具",
    "Eraser Tool": "橡皮擦工具",
    "Exit Region Mode": "退出区域模式",
    "Extend Left": "向左扩展",
    "Extend Left (Large)": "大幅向左扩展",
    "Extend Right": "向右扩展",
    "Extend Right (Large)": "大幅向右扩展",
    "First Frame": "第一帧",
    "Focus First Region": "聚焦第一个区域",
    "Hop Backward": "快速后退",
    "Hop Forward": "快速前进",
    "Image Gallery Navigation": "图库导航",
    "Key Point Tool": "关键点工具",
    "Last Frame": "最后一帧",
    "Lock Region": "锁定区域",
    "Magic Wand": "魔棒工具",
    "Move Tool": "移动工具",
    "Next Image": "下一张图片",
    "Next Keyframe": "下一个关键帧",
    "Next Phrase": "下一个短语",
    "Next Region in Phrase": "短语中的下一区域",
    "Pan Image": "平移图像",
    "Paragraph Navigation": "段落导航",
    "Polygon Tool": "多边形工具",
    "Previous Image": "上一张图片",
    "Previous Keyframe": "上一个关键帧",
    "Previous Phrase": "上一个短语",
    "Previous Region in Phrase": "短语中的上一区域",
    "Rectangle Tool": "矩形工具",
    "Redo": "重做",
    "Redo previously undone action": "重做刚刚撤销的操作",
    "Region Management": "区域管理",
    "Remove all regions": "删除所有区域",
    "Rewind 1 Second": "回退 1 秒",
    "Rotate Left": "向左旋转",
    "Rotate Right": "向右旋转",
    "Seek Backward": "向后跳转",
    "Seek Forward": "向前跳转",
    "Shortcuts for controlling audio playback and navigation": "控制音频播放与导航的快捷方式",
    "Shortcuts for controlling video playback and navigation": "控制视频播放与导航的快捷方式",
    "Show or hide all regions": "显示或隐藏所有区域",
    "Shrink Left": "向左收缩",
    "Shrink Left (Large)": "大幅向左收缩",
    "Shrink Right": "向右收缩",
    "Shrink Right (Large)": "大幅向右收缩",
    "Time Series Controls": "时间序列控制",
    "Toggle All Region Visibility": "切换所有区域可见性",
    "Toggle Bulk Sidebar": "切换批量操作侧边栏",
    "Toggle Region Visibility": "切换区域可见性",
    "Undo": "撤销",
    "Undo last action": "撤销上一步操作",
    "Video Controls": "视频控制",
    "View next image": "视图下一张图片",
    "View previous image": "视图上一张图片",
    "Zoom In": "放大",
    "Zoom Out": "缩小",
    "Zoom to 100%": "缩放至 100%",
    "Zoom to Fit": "缩放至适应",
    "Administrator": "管理员",
    "Annotator": "标注员",
    "Authentication required": "需要身份验证",
    "Enable": "启用",
    "Please enter JSON data to import": "请输入要导入的 JSON 数据",
    "Beta": "测试版",
    "Copy": "复制",
    "Email": "邮箱",
    "Log Out": "退出登录",
    "Password": "密码"
  },
  home: {
    "Create Project": "创建项目",
    "Import": "导入",
    "Connect your cloud storage or upload files from your computer": "连接您的云存储或从计算机上传文件",
    "Import data to get your project started": "导入数据以启动您的项目",
    "Create new project": "创建新项目",
    "Google Cloud Storage": "谷歌云存储",
    "Import your data": "导入数据",
    "No tasks available for review or labeling": "没有可供审查或标记的任务",
    "Start labeling tasks": "开始标记任务",
    "Azure Blob Storage": "Azure Blob 存储",
    "Choose a dataset from your computer to get started": "从您的计算机中选择一个数据集以开始",
    "Redis Storage": "Redis 存储",
    "Tasks imported to this project will appear here": "导入到该项目的任务将显示在此处",
    "Error occurred while loading data": "加载数据时发生错误",
    "Invite Members": "邀请成员",
    "Tasks you've labeled will appear here": "您标记的任务将显示在此处",
    "Connect Cloud Storage": "连接云存储",
    "Create your first project": "创建您的第一个项目",
    "Failed to load data": "加载数据失败",
    "Import Data": "导入数据",
    "Label All Tasks": "标记所有任务",
    "No data available": "无可用数据",
    "Label Studio Version: Community": "Label Studio 版本：社区版",
    "See docs on importing data": "查看导入数据文档",
    "Let's get you started.": "让我们开始吧。",
    "Recent Projects": "最近项目",
    "View All": "查看全部",
    "Welcome 👋": "欢迎 👋",
    "Home": "首页",
    "API Documentation": "API 文档",
    "Slack Community": "Slack 社区",
    "No tasks available": "没有可用的任务",
    "Unable to connect to the server. Please check your internet connection.": "无法连接到服务器。请检查您的互联网连接。",
    "No tasks found": "没有找到任务",
    "Tasks assigned to you will appear here": "分配给您的任务将显示在此处",
    "Tasks will appear here when they become available": "任务可用时将显示在此处",
    "Documentation": "文档",
    "Learn, explore and get help": "学习、探索并获取帮助",
    "Release Notes": "发布说明",
    "Resources": "资源",
    "Import your data and set up the labeling interface to start annotating": "导入数据并设置标签界面以开始注释"
  },
  projects: {
    "Projects": "项目",
    "Optional description of your project": "项目描述（可选）",
    "Save and Leave": "保存并离开",
    "Settings": "设置",
    "Create Project": "创建项目",
    "Project Name": "项目名称",
    "Cloud Storage": "云存储",
    "Data Import": "数据导入",
    "Learn more": "了解更多",
    "Workspace": "工作区",
    "Labeling Setup": "标注设置",
    "Create new project": "创建新项目",
    "Import data": "导入数据",
    "Label": "标注",
    "Create custom template": "创建自定义模板",
    "Cloud Storage documentation (opens in a new tab)": "云存储文档（在新选项卡中打开）",
    "Add URL": "添加 URL",
    "Cancel project creation": "取消项目创建",
    "delete label": "删除标签",
    "Project options": "项目选项",
    "Video format support depends on your browser. Click to learn more.": "视频格式支持取决于您的浏览器。点击了解更多。",
    "You have unsaved changes.": "您有未保存的更改。",
    "Add filter for long list of labels": "添加长标签列表过滤器",
    "Add label names": "添加标签名称",
    "Save": "保存",
    "Save changes": "保存更改",
    "Save configuration": "保存配置",
    "Add labels": "添加标签",
    "Cancel": "取消",
    "Display labels:": "显示标签：",
    "Labels": "标签",
    "Multi-image labeling documentation (opens in a new tab)": "多图像标签文档（在新选项卡中打开）",
    "Select label and click on image to start": "选择标签并单击图像开始",
    "Would you like to save them before leaving?": "你想在离开之前拯救他们吗？",
    "No sample task data available.": "没有可用的示例任务数据。",
    "Template parsing error:": "模板解析错误：",
    "Can't prepare sample data.": "无法准备样本数据。",
    "Create": "创建",
    "Custom template": "自定义模板",
    "New project": "新建项目",
    "Imported file is too big": "导入的文件太大",
    "Images": "图片",
    "Select an option": "选择一个选项",
    "Organization": "组织",
    "Browse templates": "浏览模板",
    "Select text by words": "按单词选择文本",
    "Audio": "音频",
    "Named entity recognition": "命名实体识别",
    "Computer Vision": "计算机视觉",
    "-\", label:": "-“， 标签：",
    "Cancel import": "取消导入",
    "Finish import": "完成导入",
    "Community": "社区版"
  },
  import_export: {
    "Export data": "导出数据",
    "Export": "导出",
    "You can export dataset in one of the following formats:": "您可以使用以下格式之一导出数据集：",
    "Copy command": "复制命令",
    "Files are being prepared. It might take long time.": "文件正在准备中，可能需要较长时间。",
    "Read more about supported export formats in the Documentation.": "在文档中阅读有关支持的导出格式的更多信息。",
    "Enterprise": "企业版"
  },
  data_manager: {
    "Settings": "设置",
    "Save": "保存",
    "Data": "数据",
    "You have unsaved changes": "您有未保存的更改",
    "Labeling": "标注",
    "Back to projects": "返回项目列表",
    "Total tasks in the project": "项目总任务",
    "Grid settings": "网格设置",
    "Refresh data": "刷新数据",
    "Error occurred when loading data": "加载数据时发生错误",
    "Label Studio Frontend doesn't exist on the page": "页面上不存在 Label Studio 前端",
    "Labeling Instructions": "标注说明",
    "Task Data": "任务数据",
    "Annotation overlap has been reached for this task. Your draft is preserved but cannot be submitted.": "此任务已达到注释重叠。您的草稿已保留，但无法提交。",
    "Before you can annotate the data, set up labeling configuration": "在注释数据之前，请先设置标签配置",
    "Delete selected": "删除所选内容",
    "Next Task": "下一步任务",
    "Project ID:": "项目编号：",
    "importFilters: failed to create filter for": "importFilters：未能创建过滤器",
    "label all": "标记全部",
    "re in label stream and there": "re 在标签流中并且在那里",
    "Annotation is not saved": "注释未保存",
    "Annotation saved successfully": "注释保存成​​功",
    "CancelledError": "取消错误",
    "Error fetching actions:": "获取操作时出错：",
    "Number of submitted annotations. Table shows only submitted results, not current drafts.": "提交的注释数量。表格仅显示提交的结果，而不显示当前的草稿。",
    "Overall agreement over all submitted annotations": "对所有提交的注释达成总体一致",
    "t reload the task on error to avoid losing the user": "错误时不要重新加载任务以避免失去用户",
    "Back": "返回",
    "Draft saved successfully": "草稿保存成功",
    "Instructions": "说明",
    "Filters": "筛选",
    "View Task Source": "查看任务源",
    "Copy filters": "复制过滤器",
    "Focus previous task": "聚焦上一个任务",
    "Copy task ID": "复制任务 ID",
    "Default": "默认",
    "Filtered tasks": "过滤任务",
    "All Fields": "所有字段",
    "Can't find task": "找不到任务",
    "Tasks Actions": "任务操作",
    "You're almost there!": "你快到了！",
    "Comfortable density": "舒适密度",
    "Compact density": "紧凑密度",
    "Open New Tab": "打开新标签页",
    "Failed to copy filters:": "复制过滤器失败：",
    "Filter": "筛选",
    "Image": "图片",
    "List": "列表",
    "Tab name": "标签页名称",
    "Tab options": "标签页选项",
    "Failed to copy to clipboard": "无法复制到剪贴板",
    "Grid view": "网格视图",
    "List view": "列表视图",
    "Order by": "排序方式",
    "Switch to list view": "切换到列表视图",
    "Task cannot be skipped: allow_skip is false and user lacks manager role": "任务无法跳过：allow_skip 为 false 并且用户缺少管理员角色",
    "Task ID:": "任务编号：",
    "Columns": "列",
    "Copy": "复制",
    "Copy (2)": "副本（2）",
    "Copy JSON": "复制 JSON",
    "No content to copy": "没有可复制的内容",
    "Select value": "选择值",
    "Task cannot be skipped": "任务无法跳过",
    "Task ID must be provided": "必须提供任务 ID",
    "Task ID not found": "未找到任务 ID",
    "Task is not skipped": "任务不被跳过",
    "Task skipped successfully": "任务已成功跳过",
    "This task cannot be skipped": "该任务无法跳过",
    "Unknown": "未知",
    "Your action is being processed in the background.": "您的操作正在后台处理。",
    "Annotator": "标注员",
    "Cannot read clipboard. Please allow clipboard access and try again.": "无法读取剪贴板。请允许剪贴板访问并重试。",
    "SelectOptions": "选择选项",
    "task selected": "已选择任务",
    "Sort descending": "降序排序",
    "Toggle open": "切换打开",
    "View": "视图",
    "all selected": "全部所选",
    "You must upgrade your plan to import data": "您必须升级您的计划才能导入数据",
    "Agreement": "一致性",
    "Cancel": "取消",
    "Data Manager": "数据管理"
  },
  labeling: {
    "Learn more": "了解更多",
    "Delete": "删除",
    "Select label and click the image to start": "选择标签并单击图像开始",
    "Add any notes or edge cases...": "添加任何注释或边缘情况...",
    "Save": "保存",
    "Add a comment (optional)": "添加评论（可选）",
    "Labeling Instructions": "标注说明",
    "Labeling Config": "标注配置",
    "created,": "已创建,",
    "Labeling Interface": "标注界面",
    "Organization": "组织",
    "Create Annotation": "创建标注",
    "Delete selected annotation": "删除选定的注释",
    "Save annotation settings": "保存注释设置",
    "Create new annotation": "创建新注释",
    "Delete selected region": "删除选定区域",
    "Create Relation": "创建关系",
    "Delete annotation?": "删除注释？",
    "Delete Relation": "删除关系",
    "Delete Annotation": "删除标注",
    "Select labels": "选择标签",
    "Use predictions to prelabel tasks": "使用预测来预先标记任务",
    "x\", label:": "x”，标签：",
    "Annotation Settings": "标注设置",
    "Delete Predictions": "删除预测",
    "Delete Region": "删除区域",
    "Type your answer here...": "在此输入您的答案...",
    "y\", label:": "y”，标签：",
    "Enter description here...": "在此输入描述...",
    "Label 1": "标签1",
    "Please confirm you want to delete this annotation": "请确认您要删除此注释",
    "Region": "区域",
    "Regions": "区域",
    "Chatbot Model Assessment": "聊天机器人模型评估",
    "Create relations between regions": "创建区域之间的关系",
    "Human Preference collection for RLHF": "RLHF 的人类偏好集合",
    "Labeling Interface Settings": "标签界面设置",
    "LLM Ranker": "法学硕士排名",
    "Select a text span answering the following question:": "选择回答以下问题的文本范围：",
    "Select document related to the query:": "选择与查询相关的文档：",
    "Select predictable region spans in time series:": "选择时间序列中的可预测区域跨度：",
    "Choose similar images:": "选择相似的图像：",
    "Created": "已创建",
    "Dont you hate that?": "你不讨厌这样吗？",
    "Predictions Settings": "预测设置",
    "Review deleted": "评论已删除",
    "Select text to correct": "选择要更正的文本",
    "There was an error saving your draft": "保存草稿时出错",
    "What's your opinion on pineapple pizza?": "您对菠萝披萨有何看法？",
    "CancelledError": "取消错误",
    "Choose response": "选择回复",
    "Choose text sentiment": "选择文字情感",
    "Error checking pixel transparency:": "检查像素透明度时出错：",
    "You must provide the response to the prompt": "您必须提供对提示的响应",
    "Cancel": "取消",
    "Draft saved successfully": "草稿保存成功",
    "Predictions List": "预测列表",
    "Breast Cancer Mammogram Classification": "乳腺癌乳房X光检查分类",
    "image1,image2": "图片1,图片2",
    "Annotation": "标注",
    "Predictions": "预测",
    "Start frame": "起始帧",
    "Copy Annotation ID": "复制注释 ID",
    "Copy Annotation Link": "复制注释链接",
    "Copy Region Link": "复制区域链接",
    "Hide all": "隐藏全部",
    "Show all": "显示全部",
    "Annotation ID": "标注 ID",
    "Annotations List Toggle": "标注列表切换",
    "Region options": "区域选项",
    "View all annotations": "查看全部标注",
    "Hide": "隐藏",
    "Show": "显示",
    "Toggle Visibility": "切换可见性",
    "Please select model or predictions": "请选择模型或预测",
    "Select a region": "选择地区",
    "This action cannot be undone. Are you sure?": "此操作无法撤消。你确定吗？",
    "Enterprise": "企业版",
    "Segment start must be greater than 0": "段开始必须大于 0",
    "Unknown": "未知",
    "Model": "模型"
  },
  settings: {
    "Settings": "设置",
    "Cloud Storage": "云存储",
    "Delete Project": "删除项目",
    "Learn more": "了解更多",
    "Project Name": "项目名称",
    "Data Manager": "数据管理",
    "Workspace": "工作区",
    "Hotkeys": "快捷键",
    "Add Source Storage": "添加源存储",
    "Add Target Storage": "添加目标存储",
    "Google Cloud Storage": "谷歌云存储",
    "Keep label selected after creating a region": "创建区域后保持标签处于选中状态",
    "Allows continuous region creation using the selected label": "允许使用所选标​​签创建连续区域",
    "Azure Blob Storage": "Azure Blob 存储",
    "Configure your Google Cloud Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置您的 Google Cloud Storage 连接",
    "Configure your local file storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置本地文件存储连接",
    "Configure your Redis storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置 Redis 存储连接",
    "Redis Storage": "Redis 存储",
    "Save machine learning settings": "保存机器学习设置",
    "Use cloud or database storage as the source for your labeling tasks or the target of your completed annotations.": "使用云存储或数据库存储作为标注任务的数据源，或作为已完成标注的目标存储。",
    "Configure your AWS S3 connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置您的 AWS S3 连接",
    "Configure your Azure Blob Storage connection with all required Label Studio settings": "使用所有必需的 Label Studio 设置配置 Azure Blob 存储连接",
    "Display region label names": "显示区域标签名称",
    "Save general settings": "保存常规设置",
    "Add your first cloud storage": "添加您的第一个云存储",
    "Available on Label Studio Enterprise": "可在 Label Studio Enterprise 上使用",
    "Learn more about cloud storage (opens in new window)": "了解有关云存储的更多信息（在新窗口中打开）",
    "Learn more about cloud storage troubleshooting": "了解有关云存储故障排除的更多信息",
    "Save": "保存",
    "Configure your Databricks Unity Catalog Volumes connection with all required settings (proxy only)": "使用所有必需的设置配置 Databricks Unity Catalog Volumes 连接（仅限代理）",
    "Labeling Interface Settings": "标签界面设置",
    "Save machine learning form": "保存机器学习表格",
    "Source Cloud Storage": "源云存储",
    "Storage options": "存储选项",
    "Storage Sync Error Log": "存储同步错误日志",
    "Target Cloud Storage": "目标云存储",
    "Configure your Google Cloud Storage connection with Workload Identity Federation authentication (proxy only)": "使用 Workload Identity Federation 身份验证配置您的 Google Cloud Storage 连接（仅限代理）",
    "Delete ML Backend": "删除 ML 后端",
    "Deleting storage": "删除存储",
    "Enables quick selection of labels using hotkeys": "允许使用热键快速选择标签",
    "Google Project ID": "谷歌项目 ID",
    "Save storage settings": "保存存储设置",
    "Your redis password": "你的redis密码",
    "Your storage account key": "您的存储帐户密钥",
    "Add machine learning model": "添加机器学习模型",
    "Automatically selects newly created regions": "自动选择新创建的区域",
    "Configure your Azure Blob Storage connection using Service Principal authentication for enhanced security (proxy only)": "使用服务主体身份验证配置 Azure Blob 存储连接以增强安全性（仅限代理）",
    "Edit": "编辑",
    "Enable labeling hotkeys": "启用标注快捷键",
    "Labeling hotkeys": "标注快捷键",
    "Remember Selected Tool": "记住选择的工具",
    "Session token (optional)": "会话令牌（可选）",
    "Time-to-Live (optional, Personal Access Token only)": "生存时间（可选，仅限个人访问令牌）",
    "Account Name": "账户名称",
    "Add storage": "添加存储",
    "Annotation settings": "标注设置",
    "Cloud Storage Settings": "云存储设置",
    "Show region labels": "显示区域标签",
    "Account Key": "账户密钥",
    "Completed with errors: sync job completed but some tasks had validation errors": "已完成但有错误：同步作业已完成，但某些任务存在验证错误",
    "Deleting a project removes all tasks, annotations, and project data from the database.": "删除项目将从数据库中删除所有任务、注释和项目数据。",
    "General Settings": "常规设置",
    "Project deleted successfully": "项目删除成功",
    "Save Changes": "保存更改",
    "Connect Model": "连接模型",
    "Model Settings": "模型设置",
    "Cancel": "取消",
    "If the Data Manager is not loading, dropping all Data Manager tabs can help.": "如果数据管理器未加载，删除所有数据管理器选项卡会有所帮助。",
    "Actions": "操作",
    "Perform these actions at your own risk. Actions you take on this page can't be reverted. Make sure your data is backed up.": "执行以下操作需自行承担风险。此页面上的操作无法撤销。请确保您的数据已备份。",
    "add new": "添加新建",
    "Reset Cache may help in cases like if you are unable to modify the labeling configuration due to validation errors concerning existing labels, but you are confident that the labels don't exist. You can use this action to reset the cache and try again.": "如果您因为现有标签的校验错误而无法修改标注配置，但又确认这些标签实际上并不存在，重置缓存可能会有帮助。您可以使用此操作重置缓存后再试一次。",
    "Danger Zone": "危险操作",
    "Drop All Tabs": "关闭所有标签页",
    "Reset Cache": "重置缓存",
    "Select an option": "选择一个选项",
    "General": "常规",
    "Bucket prefix": "Bucket 前缀",
    "Let's connect your first model": "让我们连接您的第一个模型",
    "Persists the selected tool across tasks": "跨任务保留所选工具",
    "Model": "模型",
    "Select authentication method": "选择身份验证方法",
    "Select region after creating it": "创建后选择区域",
    "Select regions after creating": "创建后选择区域",
    "Start model training on annotation submission": "在注释提交上开始模型训练",
    "Tasks are chosen with uniform random": "任务是均匀随机选择的",
    "Tasks are ordered by Task ID": "任务按任务 ID 排序",
    "Identify and reference specific lines of text in your document": "识别并引用文档中的特定文本行",
    "Machine learning model options": "机器学习模型选项",
    "Start Model Training": "开始模型训练",
    "Name": "名称",
    "Region Name": "区域名称",
    "This action cannot be undone. Are you sure?": "此操作无法撤消。你确定吗？",
    "Connect": "连接",
    "Copy": "复制",
    "Community": "社区版"
  },
  storage: {
    "Select an option": "选择一个选项",
    "Save": "保存",
    "Google Cloud Storage": "谷歌云存储",
    "Azure Blob Storage": "Azure Blob 存储",
    "Previous": "上一步",
    "Configure Connection": "配置连接",
    "API context not available": "API 上下文不可用",
    "Audio": "音频",
    "Images": "图片",
    "Tasks": "任务",
    "Videos": "视频",
    "Bucket Prefix": "Bucket 前缀",
    "Bytes": "字节",
    "Connection Verified": "连接已验证",
    "Next": "下一步",
    "Add storage": "添加存储"
  },
  webhooks: {
    "Webhooks": "Webhook 回调",
    "Learn more": "了解更多",
    "Delete Webhook": "删除 Webhook",
    "Cancel": "取消",
    "Delete": "删除",
    "Add Webhook": "添加 Webhook",
    "Add your first webhook": "添加您的第一个 Webhook",
    "Add Header": "添加请求头",
    "Save Changes": "保存更改",
    "Webhooks Settings": "Webhook 回调设置",
    "Edit": "编辑",
    "Is Active": "已启用",
    "Edit Webhook": "编辑 Webhook",
    "New Webhook": "新建 Webhook",
    "Headers": "请求头",
    "Payload": "负载",
    "Payload URL": "负载 URL"
  },
  organization: {
    "Learn more": "了解更多",
    "API Tokens Settings": "API 令牌设置",
    "Create a Model": "创建 a 模型",
    "Created Projects": "已创建项目",
    "Create Model": "创建模型",
    "Add Members": "添加成员",
    "Invite new member": "邀请新建成员",
    "API Token Settings": "API 令牌设置",
    "Show API token settings": "显示 API 令牌设置",
    "Invite members": "邀请成员",
    "Create new model": "创建新模型",
    "API Token settings saved": "已保存 API 令牌设置",
    "Organization": "组织",
    "Close user details": "关闭用户详情"
  },
  templates: {
    "Structured Data Parsing": "结构化数据解析",
    "ASR Hypotheses Selection": "ASR 假设选择",
    "Named Entity Recognition": "命名实体识别",
    "OCR Labeling for PDFs": "PDF 的 OCR 标签",
    "Automatic Speech Recognition": "自动语音识别",
    "Automatic Speech Recognition using Segments": "使用分段的自动语音识别",
    "Breast Cancer Mammogram Classification": "乳腺癌乳房X光检查分类",
    "Change Point Detection": "变化点检测",
    "Chatbot Model Assessment": "聊天机器人模型评估",
    "Conversational Analysis": "会话分析",
    "Coreference Resolution & Entity Linking": "共指解析和实体链接",
    "Evaluate Production Conversations for RLHF": "评估 RLHF 的生产对话",
    "HTML Entity Recognition": "HTML实体识别",
    "HTML NER Tagging": "HTML NER 标记",
    "Human Preference collection for RLHF": "RLHF 的人类偏好集合",
    "Intent Classification": "意图分类",
    "Intent Classification and Slot Filling": "意图分类和槽位填充",
    "LLM Ranker": "法学硕士排名",
    "LLM Response Grading": "LLM 反应分级",
    "Medical Image Classification with Bounding Boxes": "使用边界框进行医学图像分类",
    "NER Tagging for Invoices (BIO Format)": "发票的 NER 标记（BIO 格式）",
    "Object Detection with Bounding Boxes": "使用边界框进行物体检测",
    "Optical Character Recognition": "光学字符识别",
    "Outliers & Anomaly Detection": "异常值和异常检测",
    "Pairwise classification": "成对分类",
    "Pairwise regression": "成对回归",
    "PDF Classification": "PDF分类",
    "Search Page Ranking": "搜索页面排名",
    "Semantic Segmentation with Masks": "使用掩码进行语义分割",
    "Semantic Segmentation with Polygons": "多边形语义分割",
    "Signal Quality Detection": "信号质量检测",
    "Sound Event Detection": "声音事件检测",
    "Speaker Segmentation": "说话人分割",
    "Speech Transcription": "语音转写",
    "Taxonomy": "分类学",
    "Time Series Forecasting": "时间序列预测",
    "Video Frame Classification": "视频帧分类",
    "Video Object Tracking": "视频对象跟踪",
    "Video Timeline Segmentation": "视频时间线分割",
    "Visual Question Answering": "视觉问答",
    "Light": "浅色",
    "Here’s a few things you can try:": "您可以尝试以下一些操作：",
    "Chat": "聊天",
    "Community Contributions": "社区贡献",
    "Computer Vision": "计算机视觉",
    "Generative AI": "生成式人工智能",
    "Natural Language Processing": "自然语言处理",
    "Ranking & Scoring": "排名与评分",
    "Time Series Analysis": "时间序列分析",
    "Conversational AI": "对话式人工智能",
    "Videos": "视频",
    "Go to Home": "回到首页",
    "Auto": "汽车",
    "Dark": "黑暗的",
    "Heidi's down": "海蒂倒下了",
    "Uh oh, something went wrong.": "呃哦，出了点问题。",
    "Uh oh, this is not permitted.": "呃哦，这是不允许的。",
    "Uh oh, this page doesn’t exist.": "呃哦，这个页面不存在。",
    "Logs": "日志",
    "Audio/Speech Processing": "音频/语音处理",
    "Custom template": "自定义模板"
  },
  generic: {
    "Save": "保存",
    "Cancel skip": "取消跳过",
    "Add \"": "添加 \"",
    "Learn more": "了解更多",
    "Settings": "设置",
    "Projects": "项目",
    "Log Out": "退出登录",
    "Delete": "删除",
    "Add new label": "添加新建标注",
    "Copy labeling config": "复制标注配置",
    "Delete annotation": "删除标注",
    "Submit current annotation": "提交当前标注",
    "Audio settings": "音频设置",
    "Try Label Studio Starter Cloud, optimized for small teams and projects.": "试试 Label Studio Starter Cloud，它针对小型团队和项目做了优化。",
    "Add a comment": "添加评论",
    "Cancel delete": "取消删除",
    "Create a new annotation": "创建 a 新建标注",
    "Delete Region": "删除区域",
    "Label Studio Logo": "标签工作室标志",
    "Enterprise": "企业版",
    "Submit annotation": "提交标注",
    "Annotations": "标注",
    "Go to Previous Task": "前往上一步任务",
    "Annotation overlap has been reached for this task. Your draft is preserved but cannot be submitted.": "此任务已达到注释重叠。您的草稿已保留，但无法提交。",
    "Create relations between regions": "创建区域之间的关系",
    "Unknown error": "未知错误",
    "CancelledError": "取消错误",
    "Cancel edit": "取消编辑",
    "Continue": "继续",
    "data()": "数据()",
    "Hide Instructions": "隐藏说明",
    "Labeling Instructions": "标注说明",
    "Upload Image": "上传图片",
    "Zoom 100%": "缩放 100%",
    "Instructions": "说明",
    "Docs": "文档",
    "Organization": "组织",
    "Home": "首页",
    "Select an option": "选择一个选项",
    "Slack Community": "Slack 社区",
    "Did you know?": "你可知道？",
    "Redo": "重做",
    "Previous task": "上一步任务",
    "Copy Annotation": "复制标注",
    "Edit": "编辑",
    "Undo": "撤销",
    "Zoom In": "放大",
    "Zoom Out": "缩小",
    "Zoom to fit": "缩放至适应",
    "Skip current task": "跳过当前任务",
    "Edit Region": "编辑区域",
    "Hide all regions": "隐藏全部区域",
    "Pan Image": "平移图像",
    "Show all regions": "显示全部区域",
    "This task cannot be skipped": "该任务无法跳过",
    "Density": "密度",
    "Open Annotation Tab": "打开标注标签页",
    "Search...": "搜索...",
    "select all": "选择全部",
    "Tab": "标签页",
    "View": "视图",
    "Failed to copy to clipboard": "无法复制到剪贴板",
    "Hop backward": "快速后退",
    "Hop forward": "快速前进",
    "Magic Wand": "魔棒工具",
    "Rotate Left": "向左旋转",
    "Rotate Right": "向右旋转",
    "Search JSON": "搜索 JSON",
    "Show instructions": "显示说明",
    "Step forward": "前进一步",
    "Task cannot be skipped: allow_skip is false and user lacks manager role": "任务无法跳过：allow_skip 为 false 并且用户缺少管理员角色",
    "Copy JSON": "复制 JSON",
    "Next task": "下一步任务",
    "Auto Detect": "自动检测",
    "Choose text sentiment": "选择文字情感",
    "Search": "搜索",
    "First name": "名字",
    "Last name": "姓氏",
    "Bytes": "字节",
    "Heidi's down": "海蒂倒下了",
    "Image 1": "图片 1",
    "Image 2": "图片 2",
    "Lock Region": "锁定区域",
    "Model": "模型",
    "color 0.2s": "颜色 0.2s",
    "model 0": "模型 0",
    "Cloud Storage": "云存储",
    "Create Project": "创建项目",
    "Danger Zone": "危险操作",
    "Data Manager": "数据管理",
    "Delete Project": "删除项目",
    "Drop All Tabs": "关闭所有标签页",
    "Export": "导出",
    "Import": "导入",
    "Labeling Interface": "标注界面",
    "Members": "成员",
    "Membership Info": "成员信息",
    "Optional description of your project": "项目描述（可选）",
    "Personal Info": "个人信息",
    "Perform these actions at your own risk.": "执行以下操作需自行承担风险。",
    "Actions you take on this page can't be reverted.": "此页面上的操作无法撤销。",
    "Make sure your data is backed up.": "请确保您的数据已备份。",
    "Perform these actions at your own risk. Actions you take on this page can't be reverted. Make sure your data is backed up.": "执行以下操作需自行承担风险。此页面上的操作无法撤销。请确保您的数据已备份。",
    "Project Name": "项目名称",
    "Predictions": "预测",
    "Annotation": "标注",
    "Reset Cache": "重置缓存",
    "Reset Cache may help in cases like if you are unable to modify the labeling configuration due to validation errors concerning existing labels, but you are confident that the labels don't exist.": "如果您因为现有标签的校验错误而无法修改标注配置，但又确认这些标签实际上并不存在，重置缓存可能会有帮助。",
    "You can use this action to reset the cache and try again.": "您可以使用此操作重置缓存后再试一次。",
    "Reset Cache may help in cases like if you are unable to modify the labeling configuration due to validation errors concerning existing labels, but you are confident that the labels don't exist. You can use this action to reset the cache and try again.": "如果您因为现有标签的校验错误而无法修改标注配置，但又确认这些标签实际上并不存在，重置缓存可能会有帮助。您可以使用此操作重置缓存后再试一次。",
    "Reset to Defaults": "恢复默认",
    "Save and Leave": "保存并离开",
    "Submit": "提交",
    "Workspace": "工作区"
  }
};

  var SKIP_TAGS = {
    SCRIPT: true,
    STYLE: true,
    CODE: true,
    PRE: true,
    TEXTAREA: true
  };

  var ATTRIBUTES = [
    "placeholder",
    "title",
    "aria-label",
    "aria-placeholder",
    "alt",
    "data-tooltip",
    "data-title",
    "value"
  ];

  var EXACT_MAP = Object.create(null);
  var NORMALIZED_MAP = Object.create(null);
  var PHRASE_RULES = [];

  Object.keys(MODULE_MAPS).forEach(function (moduleName) {
    var moduleMap = MODULE_MAPS[moduleName] || {};
    Object.keys(moduleMap).forEach(function (source) {
      var target = moduleMap[source];
      if (!(source in EXACT_MAP)) {
        EXACT_MAP[source] = target;
      }

      var normalizedSource = normalizeSpaces(source);
      if (!(normalizedSource in NORMALIZED_MAP)) {
        NORMALIZED_MAP[normalizedSource] = target;
      }

      if (source.length >= 8 && source.length <= 120 && source.indexOf(" ") !== -1) {
        PHRASE_RULES.push([source, target]);
      }
    });
  });

  PHRASE_RULES.sort(function (a, b) {
    return b[0].length - a[0].length;
  });

  function normalizeSpaces(text) {
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

    return !!element.closest([
      '[data-region="true"]',
      '[data-testid="task-content"]',
      '[class*="task-text"]',
      '[class*="task-preview"]',
      '[class*="annotation-text"]',
      '[class*="htx-text"]',
      '[class*="lsf-richtext"]'
    ].join(", "));
  }

  function translateValue(value) {
    if (!value) {
      return value;
    }

    var exact = EXACT_MAP[value];
    if (exact) {
      return exact;
    }

    var normalized = normalizeSpaces(value);
    if (!normalized) {
      return value;
    }

    var normalizedExact = NORMALIZED_MAP[normalized];
    if (normalizedExact) {
      return value.replace(normalized, normalizedExact);
    }

    var nextValue = value;
    PHRASE_RULES.forEach(function (pair) {
      var source = pair[0];
      var target = pair[1];
      if (nextValue.indexOf(source) !== -1) {
        nextValue = nextValue.split(source).join(target);
      }
    });

    return nextValue;
  }

  function processTextNode(node) {
    if (!node || !node.parentElement || shouldSkipElement(node.parentElement)) {
      return;
    }

    var nextValue = translateValue(node.nodeValue);
    if (nextValue !== node.nodeValue) {
      node.nodeValue = nextValue;
    }
  }

  function processAttributes(element) {
    if (!(element instanceof Element) || shouldSkipElement(element)) {
      return;
    }

    ATTRIBUTES.forEach(function (attr) {
      if (!element.hasAttribute(attr)) {
        return;
      }

      var currentValue = element.getAttribute(attr);
      var nextValue = translateValue(currentValue);
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

    root.querySelectorAll("*").forEach(processAttributes);
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

  function applyOverlay() {
    walk(document.body);
  }

  function hookHistory(methodName) {
    var original = history[methodName];
    if (typeof original !== "function") {
      return;
    }

    history[methodName] = function () {
      var result = original.apply(this, arguments);
      window.setTimeout(applyOverlay, 0);
      return result;
    };
  }

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
    attributeFilter: ATTRIBUTES
  });
})();
