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
    RIGOROUS_COMPUTATIONAL_RESEARCH_WORKFLOW_GUIDE.md
    SKILL_AUDIT.md
    WORKFLOW_COVERAGE_AUDIT.md
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
- `docs/RIGOROUS_COMPUTATIONAL_RESEARCH_WORKFLOW_GUIDE.md` 是包级科研流程指导文件，不应在日常任务中默认全文读取。
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

## v1.4 合规状态

- 28 个通用 skill 均通过官方 `quick_validate.py`。
- 28 个通用 skill 均已补充 `agents/openai.yaml`。
- 根 `AGENTS.md` 保持短入口，不包含候选扩展功能。
- 已新增包级科研流程指导文件和 workflow 覆盖审计，不作为日常任务默认读取内容。
- 详细审计见 `docs/SKILL_AUDIT.md`。

## Hermes 迁移状态

本仓库仍是通用生信 agent/skill 的源头。Hermes 侧采用隔离迁移策略：先审计和试用，再把成熟、高频、低风险的 skill 复制到 `~/.hermes/skills/bioinfo/` 作为运行副本；项目事实、路径和临时进度仍保留在项目 `AGENTS.md`、`PROJECT_GUIDE.md` 或 `PROJECT_PLAN.md`。

当前迁移审计见：`docs/HERMES_MIGRATION_AUDIT.md`。

v1.2 新增文献/引用、投稿一致性、真实审稿回复、证据缺口和验证策略相关 skills。生信专项包仍按真实项目需求后续增补。
v1.3 新增项目环境启动检查 skill：`project-environment-bootstrap`，用于新项目、切换机器/目录或环境未知时初始化本地私有 `PROJECT_ENVIRONMENT.md`。
v1.4 补充从问题到论文的计算生物学流程指导文件，并将选题卡、五句话框架、阶段自检、reviewer attack list 和可复现 workflow 要点下沉到相关 references。


v1.5-candidate 新增 `scientific-database-grounding` 与 `protein-docking-drug-discovery` 候选 skill，用于承接全量外部 skill/agent 审计后的数据库 grounding 与蛋白/药筛方向缺口；尚未默认迁移到 Hermes runtime。
