---
name: project-environment-bootstrap
description: 用于新生信项目启动、切换机器或工作目录、运行分析前环境不明、缺少 PROJECT_ENVIRONMENT.md、conda/Jupyter/VS Code/GitHub 同步配置检查和本地环境记录初始化。不用于日常编码、绘图、分析、写作、翻译或已确认环境下的小任务。
---

# Project Environment Bootstrap

## 使用场景

只在项目环境需要初始化或重新确认时使用本 skill：

- 新项目第一次开始。
- 当前项目根目录缺少 `PROJECT_ENVIRONMENT.md`。
- 切换机器、服务器、WSL、VS Code remote 或工作目录。
- 准备运行分析但 conda/Jupyter/GitHub 环境未知。
- GitHub 同步、conda 环境、Jupyter kernel 或 VS Code 工作目录出现问题。
- 用户明确要求“检查环境”“初始化项目环境”“配置 GitHub 同步”“生成 PROJECT_ENVIRONMENT.md”。

## 不触发场景

为了节省上下文，本 skill 不应在日常任务中触发：

- 普通代码编写、调试、轻量统计或脚本修改。
- 普通绘图、图表修改、caption、source data 检查。
- 中文润色、英文翻译、英文润色、论文段落重构。
- 文献阅读、引用核验、审稿模拟或审稿回复。
- 已有有效 `PROJECT_ENVIRONMENT.md`，且主机、工作目录、conda 环境、Git remote 未变化。
- 用户只要求运行一个明确命令，且当前环境已足够明确。

## 核心原则

- `PROJECT_ENVIRONMENT.md` 是本地私有环境记录，默认不提交 GitHub。
- 创建或更新 `PROJECT_ENVIRONMENT.md` 时，必须检查 `.gitignore` 是否保护它。
- 轻量结果表、图表、代码和普通文档可以按项目策略同步；本 skill 不默认禁止上传数据或结果。
- 不污染环境：优先使用项目专属 conda 环境；MacBook 通用生信环境可为 `bioinfo`，其他机器不假设同名环境。
- 公共仓库更严格；私有项目仓库仍不建议提交 token、密钥、本机环境文件、服务器地址或个人绝对路径。
- 临时/借用/公共设备进入谨慎模式。

## 首次初始化必须询问

如果缺少 `PROJECT_ENVIRONMENT.md`，先问用户以下信息，不要直接完整生成：

1. 当前设备是否是常用工作设备，还是临时/借用/公共设备？
2. 当前项目 GitHub 仓库是 public、private，还是暂不上传？
3. 当前推荐 conda 环境是当前激活环境、MacBook 通用 `bioinfo`、项目专属环境，还是未确定？
4. 是否允许在本地环境文件中记录 hostname、用户名、绝对路径和服务器地址？
5. GitHub 同步策略：只同步代码/文档，还是也同步轻量结果表和图表？

## 工作流程

1. 判断是否真的需要启动本 skill；若是日常任务且环境已明确，直接退出并继续原任务。
2. 检查当前工作目录、OS、shell、hostname、VS Code/Jupyter/WSL/服务器迹象。
3. 检查 conda、当前环境、Python/R/Jupyter 版本；不要自动切换环境，除非用户确认。
4. 检查 Git repo、remote、branch、upstream 和 GitHub 连接状态。
5. 检查 `.gitignore` 是否包含 `PROJECT_ENVIRONMENT.md` 和明显敏感配置。
6. 如缺少 `PROJECT_ENVIRONMENT.md`，先询问首次初始化问题，再按模板生成。
7. 如已有环境文件，只在机器、目录、环境或 remote 变化时建议更新。

## 输出格式

- `是否需要环境初始化`
- `当前环境摘要`
- `GitHub 同步状态`
- `隐私与 .gitignore 检查`
- `需要用户确认的问题`：仅首次初始化或信息不足时输出。
- `已创建/建议更新的文件`

## 按需读取

- 需要生成 `PROJECT_ENVIRONMENT.md` 时，读取 `references/project-environment-template.md`。
- 需要检查 GitHub 上传隐私和 `.gitignore` 时，读取 `references/privacy-and-gitignore.md`。
- 需要检查 GitHub remote、branch、push 或 ignored/tracked 状态时，读取 `references/github-sync-checklist.md`。
- 当前设备为临时/借用/公共设备时，读取 `references/temporary-machine-safety.md`。
- 需要记录 conda、Jupyter、VS Code 或 WSL/服务器差异时，读取 `references/conda-jupyter-vscode.md`。
