# label-studio-zh-docker

这是一个基于 `heartexlabs/label-studio:1.23.0` 构建的 Label Studio 中文界面 overlay 仓库。仓库当前固定在 `1.23.0`，通过 Docker 构建时注入自定义 CSS、JS 和模板补丁，不直接修改官方前端源码。

## 快速启动

```bash
docker compose up --build
```

启动后访问 `http://localhost:8090`。

首次启动会同时拉起 PostgreSQL 和 Label Studio；持久化数据默认写入 `./data/postgres` 与 `./data/label-studio`。

## 当前实现

- `Dockerfile` 以 `heartexlabs/label-studio:1.23.0` 为基础镜像，并在构建阶段复制 `ls-zh.js`、`ls-zh.css` 与 `patches/apply_overlay.py`。
- `patches/apply_overlay.py` 会对 `base.html` 和 `simple.html` 做锚点补丁，注入 `/static/zh-overlay/ls-zh.css`、`/static/zh-overlay/ls-zh.js` 和 `window.LS_ZH_OVERLAY` 配置。
- `docker-compose.yml` 使用 `pgautoupgrade/pgautoupgrade:17-alpine` 作为数据库，应用容器镜像名固定为 `label-studio-zh-docker:1.23.0`，默认端口映射为 `8090:8000`。
- 当前维护方式是直接在当前分支执行扫描、词典同步和构建；是否按版本号切分支由使用者自行决定。

## 目录说明

- `overrides/static/zh-overlay/ls-zh.js`：运行时中文词典与 DOM 替换逻辑。
- `overrides/static/zh-overlay/ls-zh.css`：少量补充样式。
- `patches/apply_overlay.py`：模板注入补丁脚本。
- `scripts/`：源码提取、候选词典生成、翻译目录同步、运行时 JS 构建、覆盖率审计脚本。
- `translations/catalog.json`：已确认的翻译记忆库。
- `.tmp/`：源码缓存、结构化扫描结果和报告输出目录，不作为正式发布产物。

## 重新生成 overlay

在已经准备好 `.tmp/label-studio-1.23.0/` 上游源码目录后，可按下面顺序重跑生成链：

```bash
python scripts/extract_label_studio_strings.py .tmp/label-studio-1.23.0 --output .tmp/label-studio-1.23.0-strings.json
python scripts/generate_overlay_dictionary.py .tmp/label-studio-1.23.0-strings.json --output-json .tmp/label-studio-1.23.0-dictionary.json
python scripts/sync_translation_catalog.py .tmp/label-studio-1.23.0-dictionary.json --catalog translations/catalog.json --output-json .tmp/label-studio-1.23.0-translations.json --missing-report .tmp/label-studio-1.23.0-missing-translations.json --high-priority-report .tmp/label-studio-1.23.0-high-priority-missing.json
python scripts/build_overlay_js.py .tmp/label-studio-1.23.0-translations.json --output-js overrides/static/zh-overlay/ls-zh.js --untranslated-report .tmp/label-studio-1.23.0-untranslated-overlay.json
python scripts/verify_runtime_overlay.py --translations-json .tmp/label-studio-1.23.0-translations.json --high-priority-report .tmp/label-studio-1.23.0-high-priority-missing.json --untranslated-report .tmp/label-studio-1.23.0-untranslated-overlay.json --output .tmp/label-studio-1.23.0-coverage-report.json
```

如果宿主机没有 Python，应改为在容器内执行同一套脚本，而不是跳过扫描和词典生成。

## 当前产物与状态

- 当前仓库已包含 `.tmp/label-studio-1.23.0-strings.json`、`.tmp/label-studio-1.23.0-dictionary.json`、`.tmp/label-studio-1.23.0-translations.json`、`.tmp/label-studio-1.23.0-missing-translations.json`、`.tmp/label-studio-1.23.0-high-priority-missing.json` 和 `.tmp/label-studio-1.23.0-coverage-report.json`。
- `translations/catalog.json` 当前包含 12 个模块、435 条已沉淀词条：`auth`、`home`、`projects`、`import_export`、`data_manager`、`labeling`、`settings`、`storage`、`webhooks`、`organization`、`templates`、`generic`。
- 当前候选词典包含 3144 条候选字符串；高优先级未翻译报告中仍有 1233 条待补。
- 覆盖率审计结果显示 6 个焦点区域中仍有 3 个存在必补缺口：`data_manager`、`project_settings`、`account_settings`；`login`、`home`、`data_manager`、`project_settings`、`account_settings`、`hotkeys` 仍有残留英文，当前状态不能视为“全部页面已完成中文化”。

## 版本来源

- GitHub Release：`https://github.com/HumanSignal/label-studio/releases/tag/1.23.0`
- Docker 标签：`heartexlabs/label-studio:1.23.0`

这里固定使用明确的正式版本标签，而不是 `latest`，目的是保证构建结果可复现，避免上游镜像漂移导致词典、模板锚点和运行行为不一致。
