---
name: project-environment-bootstrap
description: 用于新生信项目、新机器/服务器/remote workspace，或当前 cwd、conda/interpreter、Jupyter kernel、Git branch/upstream 与本地环境记录不明或互相冲突时，做只读核验并安全初始化/刷新 PROJECT_ENVIRONMENT.md；不负责选择安装新工具、日常分析或 Git 发布。
---

# Project Environment Bootstrap

## 核心问题

如何在不改变分析定义或安装依赖的前提下，确认一个项目在哪里、用什么环境运行，并留下安全的本地环境入口？

## 能力边界

- 本 Skill 负责环境现状核验、本地环境记录和最小 Git/Jupyter/IDE readiness；不选择或安装缺失软件。
- 依赖选择、安装、升级、外部代码采用或 license 判断交给 `environment-and-tool-adoption`。
- 分析、绘图、建模和论文工作由对应领域 Skill 处理；已确认环境下的小任务不需要重复 bootstrap。
- Git readiness 检查不包含登录授权、commit、push、建仓库或修改 remote；这些动作需要用户针对性授权。
- `PROJECT_ENVIRONMENT.md` 是 local-only 状态，不是可移植 environment lock、方法记录或项目历史。

## 权限与安全

- `read-only preflight` 只报告观察结果，不创建或修改文件。
- 创建或刷新环境记录前，确认目标项目根、设备信任级别和允许记录的机器字段；信息不足时保留 `unknown`，不得猜测。
- 创建或更新 `PROJECT_ENVIRONMENT.md` 时，同步检查 `.gitignore`；若文件已 tracked/staged，停止并报告。
- 不记录 token、密钥、cookie、凭证内容或患者可识别信息。临时、借用或公共设备使用最小记录模式。
- 不自动切换环境、安装包、修改 global config、启动长期服务或测试写权限之外的远端资源。
- 不静默改变环境名、版本、kernel、remote、branch、参考数据库或执行位置。

## 工作流程

1. 锁定模式：`read-only preflight`、`initialize local record`、`refresh after move` 或 `temporary-machine check`。
2. 读取项目根 `AGENTS.md` 和现有 `PROJECT_ENVIRONMENT.md`；只检查与环境有关的最小文件，不扫描数据或结果。
3. 核验 cwd/project root、OS/shell、local/remote 类型、Git root/branch/upstream、conda 环境和 Python/R/Jupyter/kernel 可见性。
4. 对声明与实际观察做差异表；把 unavailable、not tested 和 permission blocked 分开。
5. 需要写记录时，先确认设备信任、repo 可见性、同步策略和机器字段粒度，再使用本地模板。
6. 检查 local record 的 ignored/tracked/staged 状态；只在明确范围内更新 `.gitignore`。
7. 运行最小无副作用验证，例如解析版本、kernel 列表或 Git read-only 状态；连接测试按用户授权和网络条件执行。
8. 若发现缺失依赖或工具不合适，报告 handoff 给 `environment-and-tool-adoption`，不在 bootstrap 内安装。
9. 交付实际环境摘要、写入路径、未改变项、验证边界和下一项用户决定。

## 模式化输出

- `read-only preflight`：报告范围、observed environment、声明差异、未测试项和是否需要初始化；不得写文件。
- `initialize local record`：报告新建的 local record、`.gitignore` 保护、用户确认字段和最小验证。
- `refresh after move`：报告旧值、新观察、保留/更新字段和仍需确认的 remote/kernel 差异。
- `temporary-machine check`：报告最小记录策略、临时凭证风险、清理提醒和未执行的持久配置。

## 按需读取

- 创建或刷新本地记录时，读取 `references/project-environment-template.md`。
- 检查 local-only 文件、敏感字段或 `.gitignore` 时，读取 `references/privacy-and-gitignore.md`。
- 核验 Git root、remote、branch、upstream、ignored/tracked 状态或连接边界时，读取 `references/github-sync-checklist.md`。
- 临时、借用或公共设备上工作时，读取 `references/temporary-machine-safety.md`。
- 区分 conda、Jupyter kernel、VS Code Remote、WSL 或服务器环境时，读取 `references/conda-jupyter-vscode.md`。

最终回复先给 environment readiness 结论，再给精确文件、验证边界、未执行动作和下一决策。
