# journal_codex_AGENT

这是当前通用生信科研 AGENT 与 skills 的打包版本，用于人工审阅、迁移或在新项目中复用。

## 内容

```text
journal_codex_AGENT/
  AGENTS.md
  local_config.yaml
  .codex/
    skills/
      bioinfo-analysis-code/
      chinese-scientific-polishing/
      citation-verifier/
      claim-evidence-audit/
      evidence-gap-finder/
      environment-and-tool-adoption/
      figure-caption/
      literature-search-workflow/
      manuscript-consistency-audit/
      paper-reader/
      project-environment-bootstrap/
      project-guide-maintainer/
      publication-plotting/
      research-data-organization/
      research-decision-review/
      research-project-planner/
      research-question-brief/
      reviewer-response-builder/
      reviewer-simulation/
      scientific-english-polishing/
      scientific-english-translation/
      skill-quality-audit/
      source-data-audit/
      submission-readiness-audit/
      task-self-check/
      validation-strategy-planner/
  docs/
    AGENT_SKILL_SUMMARY.md
    AGENT_SKELETON_TODO.md
    SKILL_AUDIT.md
    REFERENCE_CANDIDATES.md
```

每个 skill 目录均包含：

- `SKILL.md`
- `agents/openai.yaml`
- 可选的 `references/`

## 边界

- 本包只包含通用版 AGENT 和通用 skills。
- 不包含旧专案专属 skills。
- 不包含项目数据、分析结果、论文草稿或操作日志。
- `PROJECT_GUIDE.md` 不在包内创建；它应由具体项目根据 `project-guide-maintainer` skill 生成。
- `docs/REFERENCE_CANDIDATES.md` 只记录后续可选扩展，不代表已经安装或启用这些候选 skill。
- `local_config.yaml` 是本地打包配置清单，只用于人工审阅、迁移和校验，不替代 `AGENTS.md` 或 skill 触发逻辑。

## 使用方式

在新项目中复用时，可以把：

- `AGENTS.md` 放到项目根目录。
- `.codex/skills/` 合并到项目的 `.codex/skills/`。
- `docs/` 作为人工说明和审阅材料保留。

具体项目开始后，建议先用：

1. `research-question-brief` 整理用户原始想法。
2. `research-project-planner` 设计研究路线。
3. `project-guide-maintainer` 创建轻量 `PROJECT_GUIDE.md`。

## v1.3 合规状态

- 26 个通用 skill 均通过官方 `quick_validate.py`。
- 26 个通用 skill 均已补充 `agents/openai.yaml`。
- 根 `AGENTS.md` 保持短入口，不包含候选扩展功能。
- 详细审计见 `docs/SKILL_AUDIT.md`。

v1.2 新增文献/引用、投稿一致性、真实审稿回复、证据缺口和验证策略相关 skills。生信专项包仍按真实项目需求后续增补。
v1.3 新增项目环境启动检查 skill：`project-environment-bootstrap`，用于新项目、切换机器/目录或环境未知时初始化本地私有 `PROJECT_ENVIRONMENT.md`。
