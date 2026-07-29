# codex-agent-skill-bioinfo

通用生物信息学研究 Codex agent 与 skills 包。

本分支 `home_PC_codex` 是从家用 Windows PC 的本地 Codex 环境整理出的候选快照，用于交给 MacBook 上的 Hermes/Codex 与 `main` 逐项比较、审查和吸收。它不是可直接安装的完整发布镜像；安装与同步以 `main` 的 README、validator 和 installer 为准。

## 内容

- `AGENTS.md`: 本分支原有的通用生信研究 agent 入口；未复制当前科研项目的项目级 `AGENTS.md`。
- `.codex/skills/`: 2026-07-29 从 Home PC 项目运行时整理的 36 个 bioinformatics research skills。
- `.agents/skills`: 指向 `../.codex/skills` 的 repo-scope discovery 入口，兼容 standalone Codex/Hermes 读取。
- `local_config.yaml`: 本包的入口、skill 列表、验证规则和维护约束。
- `HERMES_REVIEW_NOTES.md`: 给 Hermes 的审查说明。

## 审查方式

本分支只作为候选输入：

1. 与 `main` 同名 skill 逐项比较，不整目录覆盖 canonical。
2. 仅吸收稳定、跨项目复用且已去除机器/项目沉积的机制。
3. 对候选内容执行结构、触发、隐私、provenance 和行为审查。
4. 实际安装始终从 `main` 运行仓库自带 installer。

## 维护原则

- `AGENTS.md` 保持短，只保留跨项目复用的身份、硬约束、证据规则和 skill 路由。
- 任务细节放入 `.codex/skills/<skill>/SKILL.md`。
- 项目背景和当前进度应放在具体项目的 `PROJECT_GUIDE.md` 或 profile 中，不进入本仓库。
- 不提交 raw data、`.env`、token、账号信息、本机绝对路径、临时缓存或项目运行结果。
- 新 skill 只在真实能力缺口明确时新增；能合并进现有 skill 的经验优先合并。

## 当前快照

- Snapshot source: Home PC local Codex bioinfo runtime
- Branch: `home_PC_codex`
- Snapshot date: 2026-07-29
- Local package version: `1.8-integrated`
- Skill count: 36
- Intended reviewer: Hermes on MacBook
