# label-studio-zh-docker

基于 `heartexlabs/label-studio:1.23.0` 的 Label Studio 中文界面 overlay 方案。

## 使用

```bash
docker compose up --build
```

启动后访问 `http://localhost:8090`。

## 版本

本次已自动确认并升级到 GitHub 官方最新正式版 `1.23.0`。

- GitHub Release：`https://github.com/HumanSignal/label-studio/releases/tag/1.23.0`
- Docker semver 标签：`https://hub.docker.com/layers/heartexlabs/label-studio/1.23.0/images/sha256-aa461572e8f9d86a1bf9520c1db620204e86160fd2f80dd7e9d40ac84a8828ea`

未使用 `latest`，因为它会随上游变动，不利于复现和稳定维护；本仓库固定到明确的正式版本标签。

## 说明

- `patches/apply_overlay.py` 会在 `base.html` 和 `simple.html` 注入中文 overlay 的 CSS、JS 与运行配置。
- `scripts/` 目录提供完整的提取、去噪、词典同步和 `ls-zh.js` 构建链，可在无宿主机 Python 时通过容器内 Python 重跑。
- `translations/catalog.json` 保存已确认翻译的正式词条，`overrides/static/zh-overlay/ls-zh.js` 由源码扫描结果和该目录合并生成。
- 结构化扫描结果输出在 `.tmp/label-studio-1.23.0-strings.json`，候选词典输出在 `.tmp/label-studio-1.23.0-dictionary.json`。
- 全量未翻译报告输出在 `.tmp/label-studio-1.23.0-missing-translations.json`，高优先级未翻译报告输出在 `.tmp/label-studio-1.23.0-high-priority-missing.json`。

## 验证

- 已验证：镜像构建成功；容器内 `base.html`、`simple.html` 已注入 `/static/zh-overlay/ls-zh.css` 与 `/static/zh-overlay/ls-zh.js`；`/user/login/`、`/` 首页、账户下拉菜单、`/user/account/personal-info`、`/user/account/hotkeys`、项目数据页和导出弹层均已实际命中 overlay。
- 当前仍有未翻译项：截至本次生成，`ls-zh.js` 已纳入 447 条已翻译词条，但高优先级未翻译报告仍有 1295 条，集中在标注页、数据管理和设置页。
- 待补充：真实标注任务页、项目设置中的存储/Webhooks/组织成员细项仍未在本次会话里逐页抽样验证，且部分页面仍有中英文混合文案。
