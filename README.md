# label-studio-zh-docker

这是一个基于 `heartexlabs/label-studio:1.23.0` 的 Label Studio 中文 overlay 镜像仓库。

仓库做的事情很简单：

- 不修改官方前端源码
- 通过 `Dockerfile` 注入中文 overlay 资源
- 通过 `patches/apply_overlay.py` 给模板加上 JS / CSS 挂载点
- 通过 CNB 自动构建并推送镜像到国内仓库 `cnb.cool/vvllm/label-studio-zh-docker:{分支名}`，同时保留海外仓库 `lianshufeng/label-studio-zh:{分支名}` 作为兼容镜像

## 镜像用途

镜像启动后，Label Studio 仍然保持原有功能，只是在运行时额外挂载中文 overlay，用于改善中文界面文案覆盖率。

当前仓库默认固定使用：

- 基础镜像：`heartexlabs/label-studio:1.23.0`
- 海外发布镜像：`lianshufeng/label-studio-zh:{分支名}`
- 国内发布镜像：`cnb.cool/vvllm/label-studio-zh-docker:{分支名}`

这里的 `{分支名}` 由 CNB 构建时自动生成，通常对应当前分支名。

## 本地运行

如果你只是想本地启动验证：

```bash
docker compose up --build
```

启动后访问：

- `http://localhost:8090`

本地 compose 会同时启动：

- PostgreSQL
- Label Studio

数据默认持久化到：

- `./data/postgres`
- `./data/label-studio`

## 镜像构建

仓库根目录的 `Dockerfile` 会在构建时完成两件事：

1. 把 `overrides/static/zh-overlay/ls-zh.js` 和 `overrides/static/zh-overlay/ls-zh.css` 复制进镜像
2. 执行 `patches/apply_overlay.py`，把模板中的中文 overlay 资源注入进去

CNB 使用 `.cnb.yml` 直接构建并推送镜像，镜像标签规则为：

- `lianshufeng/label-studio-zh:${BRANCH_NAME}`
- `cnb.cool/vvllm/label-studio-zh-docker:${BRANCH_NAME}`

其中分支名会自动转换为小写，并把 `/`、空格替换成 `-`，避免生成非法 tag。

## 目录说明

- `Dockerfile`：镜像构建入口
- `docker-compose.yml`：本地联调环境
- `patches/apply_overlay.py`：模板注入脚本
- `overrides/static/zh-overlay/ls-zh.js`：运行时中文替换逻辑
- `overrides/static/zh-overlay/ls-zh.css`：少量样式补充
- `scripts/`：字符串提取、词典生成、翻译同步、JS 构建、运行时校验脚本
- `translations/catalog.json`：翻译记忆库
- `.cnb.yml`：CNB 自动构建配置

## 运行时覆盖范围

当前 overlay 的目标是覆盖真实 UI 中常见的中文界面文案，包括但不限于：

- 登录与注册
- 首页与项目列表
- 创建项目弹窗
- 导入导出
- 数据管理
- 标注页面
- 设置页面
- 存储
- Webhooks
- 账户菜单与个人设置
- 顶部导航和侧边导航

不会去改动真实业务数据、标注内容、代码片段或第三方库内部实现。

## 中文化流程

如果你要重新生成 `ls-zh.js`，推荐按仓库里的脚本链路执行：

```bash
python scripts/extract_label_studio_strings.py .tmp/label-studio-1.23.0 --output .tmp/label-studio-1.23.0-strings.json
python scripts/generate_overlay_dictionary.py .tmp/label-studio-1.23.0-strings.json --output-json .tmp/label-studio-1.23.0-dictionary.json
python scripts/sync_translation_catalog.py .tmp/label-studio-1.23.0-dictionary.json --catalog translations/catalog.json --output-json .tmp/label-studio-1.23.0-translations.json --missing-report .tmp/label-studio-1.23.0-missing-translations.json --high-priority-report .tmp/label-studio-1.23.0-high-priority-missing.json
python scripts/build_overlay_js.py .tmp/label-studio-1.23.0-translations.json --output-js overrides/static/zh-overlay/ls-zh.js --untranslated-report .tmp/label-studio-1.23.0-untranslated-overlay.json
python scripts/verify_runtime_overlay.py --translations-json .tmp/label-studio-1.23.0-translations.json --high-priority-report .tmp/label-studio-1.23.0-high-priority-missing.json --untranslated-report .tmp/label-studio-1.23.0-untranslated-overlay.json --output .tmp/label-studio-1.23.0-runtime-audit.json
```

这条链路的核心是：

- 先从官方源码提取英文 UI 字符串
- 再生成候选词典
- 再同步到翻译目录
- 再生成最终运行时 `ls-zh.js`
- 最后做运行时覆盖校验

## 构建说明

CNB 构建成功后，会产出并推送：

- `lianshufeng/label-studio-zh:{分支名}`
- `cnb.cool/vvllm/label-studio-zh-docker:{分支名}`

如果你后续想在别的环境里做发布，可以继续沿用这个 tag 规则。

## 已知状态

当前仓库重点是：

- 可直接 Docker 构建
- 可通过 CNB 自动推送镜像
- 中文 overlay 资源已经接入模板

如果你发现页面里还有英文残留，通常不是构建链路问题，而是 `ls-zh.js` 里还需要补充对应文案。
