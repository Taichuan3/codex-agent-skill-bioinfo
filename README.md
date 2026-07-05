# codex-agent-skill-bioinfo

通用生物信息学研究 Codex agent 与 skills 包。

本分支 `home_PC_codex` 是从家用 Windows PC 的本地 Codex 环境整理出的快照，用于交给 MacBook 上的 Hermes 做最终审查、汇总、合并和优化。它只包含可复用的 agent / skill 文件，不包含项目原始数据、分析结果、环境目录或临时缓存。

## 内容

- `AGENTS.md`: 通用生信研究 agent 入口、硬约束、证据规则和 skill 路由。
- `.codex/skills/`: 当前本机生效的 26 个 bioinformatics research skills。
- `.agents/skills`: 指向 `../.codex/skills` 的 repo-scope discovery 入口，兼容 standalone Codex/Hermes 读取。
- `local_config.yaml`: 本包的入口、skill 列表、验证规则和维护约束。
- `HERMES_REVIEW_NOTES.md`: 给 Hermes 的审查说明。

## 使用方式

在新项目中复用时：

1. 将 `AGENTS.md` 放到项目根目录。
2. 将 `.codex/skills/` 合并到项目的 `.codex/skills/`。
3. 如果需要 repo-scope skill discovery，保留 `.agents/skills` 指向 `.codex/skills`。
4. 根据任务语义按需读取对应 `SKILL.md`，不要一次性把所有 skill 塞进上下文。

## 维护原则

- `AGENTS.md` 保持短，只保留跨项目复用的身份、硬约束、证据规则和 skill 路由。
- 任务细节放入 `.codex/skills/<skill>/SKILL.md`。
- 项目背景和当前进度应放在具体项目的 `PROJECT_GUIDE.md` 或 profile 中，不进入本仓库。
- 不提交 raw data、`.env`、token、账号信息、本机绝对路径、临时缓存或项目运行结果。
- 新 skill 只在真实能力缺口明确时新增；能合并进现有 skill 的经验优先合并。

## 当前快照

- Snapshot source: Home PC local Codex bioinfo runtime
- Branch: `home_PC_codex`
- Skill count: 26
- Intended reviewer: Hermes on MacBook
