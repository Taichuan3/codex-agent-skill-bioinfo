# Bioinfo Codex 多设备同步边界

## 目标

本仓库是可复现的生信 Codex 控制面，不是 `~/.codex` 的完整镜像。MacBook、Home/Lab 电脑和服务器安装同一 Git release，再叠加各自的本机认证、路径和环境。

运行时 Agent 只采用两层：

1. 用户级全局 `$HOME/.codex/AGENTS.md`：稳定方法、证据边界、默认数据布局、Skill 路由和安全规则。
2. 具体项目根 `AGENTS.md`：项目事实、环境、实际输入输出、禁止修改路径和对默认布局的偏离。

`~/bioinfo` 等只用于容纳多个项目的父目录不是 Codex 工作区层，不应放 `AGENTS.md`、`PROJECT_GUIDE.md` 或 `PROJECT_PLAN.md`。

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

1. 通用 bioinfo：本仓库的 38 个 Skills 和 6 个自定义 Agents。
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
6. 其他终端或高风险实验推送短期分支并创建 draft PR；MacBook canonical 在用户明确批准后可直接更新 `main`。

不要让 Home/Lab 分支长期充当完整机器镜像，也不要把某台机器的目录整包覆盖 canonical。

## 安装与机器差异

在 clone 中运行：

```bash
python3 scripts/install_codex_bioinfo.py
python3 scripts/install_codex_bioinfo.py --apply
```

安装/校验脚本要求 Python 3.11+；必要时使用本机 `bioinfo` conda 环境。

安装器管理：

- `$HOME/.codex/packages/codex-agent-skill-bioinfo/<revision-digest>/skills` 的 release snapshot
- `$HOME/.agents/skills`：macOS/Linux 为指向 snapshot 的符号链接，Windows 为带 SHA-256 marker 的托管副本
- `$HOME/.codex/agents/*.toml`
- `$HOME/.codex/AGENTS.md` 中的受管 bioinfo block

`--apply` 在 Git checkout 中只接受干净 source，并记录 commit 与 package digest；安装失败时事务性恢复已触及的 Skill deployment、Windows marker、global guidance、legacy Skills 和 custom Agents。仓库不提交 `.agents/skills` 符号链接，避免 Windows 将其检出为文本文件；运行时 parity 以 clean commit、snapshot digest 和安装 marker 为证据。

`$HOME/.agents/skills` 是用户级全局发现入口，因此 38 个 Skills 在任意项目目录均可用，不依赖项目是否位于 `~/bioinfo`。若历史安装在 `$HOME/.codex/skills` 留下重名用户 Skills，使用：

```bash
python3 scripts/install_codex_bioinfo.py --apply \
  --replace-global-guidance \
  --retire-legacy-codex-skills
```

安装器会把这些旧用户 Skill 移入可恢复备份并保留 `.system`。

Windows PowerShell 使用 Python 3.11+：

```powershell
py -3.11 scripts/validate_package.py
py -3.11 scripts/install_codex_bioinfo.py
py -3.11 scripts/install_codex_bioinfo.py --apply
```

普通的现有 `$HOME/.agents/skills` 目录不会被自动接管；先人工判断来源。只有本安装器生成、marker 有效且目录摘要未变化的托管副本才能自动升级或迁移。

安装器不管理：

- `$HOME/.codex/config.toml` 的模型、网络、MCP、插件和权限
- SSH、GitHub/OpenAI 登录
- conda、Jupyter、服务器调度器
- 项目数据或项目级 Agent

把 `.codex/config.toml.example` 的 `[features]` 与 `[agents]` 片段按机器手工合并到用户配置；不要用公共模板覆盖已有配置。示例以本轮实际安装的 Codex CLI 版本验证，升级 Codex 后应重新运行 config/doctor 检查并与官方 config reference 对照。

## 跨设备交接

一项工作只在一个 branch/worktree 上可写。离开当前设备前：

1. 停在可复现 checkpoint。
2. 运行最小验证。
3. 非 canonical 终端 commit 并 push 唯一 task branch；MacBook canonical 经批准后更新 `main`。
4. 在 commit、PR 或 handoff 中记录目标、commit、测试、未完成项和下一命令。
5. 另一台机器 fetch 后从 `main` 建立干净 checkout/worktree；不接管未提交状态。

服务器作为执行节点：同一 release 提供规则和 Skills，原始数据、环境、凭据和大型结果留在服务器，Git 只同步代码、manifest、轻量 source data 和审查记录。
