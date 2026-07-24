# Bioinfo Codex 多设备同步边界

## 目标

本仓库是可复现的生信 Codex 控制面，不是 `~/.codex` 的完整镜像。MacBook、Home/Lab 电脑和服务器安装同一 Git release，再叠加各自的本机认证、路径和环境。

## 四类内容

| 层 | 归属 | 是否进入本公共仓库 |
|---|---|---|
| Portable bioinfo core | 通用 `AGENTS.md`、Skills、自定义 Agents、安装器、validator | 是 |
| Project-private | 项目 `AGENTS.md`、项目 Skill、`PROJECT_GUIDE.md`、未发表事实 | 否；随对应私有项目仓库 |
| Machine-local | 登录、SSH、服务器、绝对路径、conda/Jupyter 记录、插件授权 | 否 |
| Generated runtime | 原生 Memory、session、cache、logs、临时 worktree | 否 |

金融投资、旅行和个人账本属于另一个工作域，不进入 bioinfo package。

## 项目子分类

计算生物学项目可以共享通用内核，但项目事实不能交叉污染：

1. 通用 bioinfo：本仓库的 37 个 Skills 和 6 个自定义 Agents。
2. 基因组模型/调控预测项目：项目 API Skill 与主管 Agent 随私有项目仓库。
3. 蛋白结构与 docking 项目：通用方法进入 `protein-structure-docking`；具体蛋白、突变、结构与结果留在项目仓库。
4. 重复序列/基因组结构等未发表课题：通用 repeat/genomics、绘图和证据审查机制可回流；未发表假说、路径、数据和 claim 永不进入公共内核。

## Memory 晋升

不要同步原生 Memory 数据库。每条可复用经验先确定归属：

- 稳定跨项目行为规则 → 根 `AGENTS.md`
- 项目当前事实、证据和 next actions → 私有项目 `PROJECT_GUIDE.md`
- 项目硬约束、目录和环境逻辑 → 私有项目 `AGENTS.md`
- 重复出现的多步骤流程 → Skill/reference/script
- 质量门槛 → checklist/eval/validator
- 一次性讨论、工具日志和临时状态 → 不晋升

只有去除身份、绝对路径、服务器、凭据、未发表结果和项目特异沉积后，内容才能进入公共仓库。

## 候选整合

1. 每台终端在短生命周期 `agent/<topic>` 分支提交候选差异。
2. `bioinfo_source_mapper` 先确定来源、使用证据和重叠项。
3. 实现 Agent 逐项 keep/merge/split/project-only/local-only/reject。
4. `bioinfo_reproducibility_reviewer` 与 `bioinfo_release_reviewer` 独立复核。
5. 运行 `python3 scripts/validate_package.py`。
6. 推送分支并创建 draft PR；未经用户明确批准不合并 `main`。

不要让 Home/Lab 分支长期充当完整机器镜像，也不要把某台机器的目录整包覆盖 canonical。

## 安装与机器差异

在 clone 中运行：

```bash
python3 scripts/install_codex_bioinfo.py
python3 scripts/install_codex_bioinfo.py --apply
```

安装/校验脚本要求 Python 3.11+；必要时使用本机 `bioinfo` conda 环境。

安装器管理：

- `$HOME/.agents/skills` → 当前 clone 的 `.codex/skills`
- `$HOME/.codex/agents/*.toml`
- `$HOME/.codex/AGENTS.md` 中的受管 bioinfo block

安装器不管理：

- `$HOME/.codex/config.toml` 的模型、网络、MCP、插件和权限
- SSH、GitHub/OpenAI 登录
- conda、Jupyter、服务器调度器
- 项目数据或项目级 Agent

把 `.codex/config.toml.example` 的 `[agents]` 片段按机器手工合并到用户配置；不要用公共模板覆盖已有配置。

## 跨设备交接

一项工作只在一个 branch/worktree 上可写。离开当前设备前：

1. 停在可复现 checkpoint。
2. 运行最小验证。
3. commit 并 push 唯一 task branch。
4. 在 PR 或 handoff 中记录目标、commit、测试、未完成项和下一命令。
5. 另一台机器 fetch 后创建干净 worktree；不接管未提交状态。

服务器作为执行节点：同一 release 提供规则和 Skills，原始数据、环境、凭据和大型结果留在服务器，Git 只同步代码、manifest、轻量 source data 和审查记录。
