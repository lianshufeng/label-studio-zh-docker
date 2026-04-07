"# label-studio-zh-docke"

基于 `heartexlabs/label-studio:1.23.0` 的中文覆盖 Docker 方案。

## 使用

```bash
docker compose up --build
```

启动后访问：

- `http://localhost:8090`

## 版本

当前基线已升级到官方最新正式版 `1.23.0`（2026-04-07 核对），对应 Docker 基础镜像标签为 `1.23.0`。

未使用 `latest`，因为它会随上游漂移，不利于复现和稳定维护；本仓库按官方 GitHub Releases 的最新正式版固定版本。
