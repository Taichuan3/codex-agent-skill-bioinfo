# Hermes 迁移与迭代审计

审计日期：2026-06-18
审计对象：`journal_codex_AGENT` / `codex-agent-skill-bioinfo`
目标：在不污染 Hermes 默认能力的前提下，将成熟、通用、高频的生信科研 skill 逐步迁移为 Hermes 原生 skill，并保留 GitHub 仓库作为源头。

## 1. 外部标准吸收

参考来源：

- OpenAI Codex Agent Skills 文档
- Agent Skills open format
- Hermes Agent skill authoring 约定

关键原则：

1. `SKILL.md` 必须有短而精确的 `name` 和 `description`。
2. description 是隐式触发的核心，应说明“什么时候用”和“什么时候不用”。
3. 复杂 checklist、模板、rubric 应放在 `references/`，主 `SKILL.md` 保持短入口。
4. 使用 progressive disclosure：默认只暴露名称和描述，任务匹配后再读全文。
5. 项目事实、路径、临时进度不进入全局 Hermes skill，应留在 `AGENTS.md`、`PROJECT_GUIDE.md` 或 `PROJECT_PLAN.md`。

## 2. 隔离策略

推荐分层：

```text
GitHub repo
  原始 source of truth，保存 Codex/Hermes 兼容 skill

/Users/yajiehu/bioinfo/AGENTS.md
  项目级规则，Codex 和 Hermes 都可读取

~/.hermes/skills/bioinfo/
  只放经过验证的稳定 Hermes 原生 skill

Hermes 自生成/优化 skill
  必须单独命名，不覆盖原始 skill，除非用户确认
```

## 3. 迁移分级

### P1：优先迁移为 Hermes 原生 skill

| Skill | 理由 | 迁移建议 |
|---|---|---|
| `bioinfo-analysis-code` | 高频，适合脚本、表格、轻量统计、复现说明 | 首批迁移 |
| `paper-reader` | 单篇论文阅读，高频且边界清楚 | 首批迁移 |
| `literature-search-workflow` | 系统文献检索和 evidence table | 首批迁移 |
| `claim-evidence-audit` | 防 overclaim，科研诚信核心 | 第二批迁移，补 reference 模板 |
| `research-project-planner` | 课题设计和 figure skeleton | 第二批迁移 |
| `research-question-brief` | 压缩想法，减少上下文 | 第二批迁移 |
| `project-guide-maintainer` | 长期项目主线维护 | 第二批迁移，先拆分主文件 |
| `publication-plotting` | 图表、source data、视觉 QA | 第二批迁移 |
| `scientific-english-translation` | 中文到英文科研翻译 | 第二批迁移 |
| `scientific-english-polishing` | 英文润色但不升级 claim | 第二批迁移 |

### P2：按需迁移

| Skill | 适用阶段 | 建议 |
|---|---|---|
| `citation-verifier` | 写作/投稿前 | 加强“不用于开放式文献检索”的边界 |
| `evidence-gap-finder` | 已有结果但证据链不足 | 加强和 validation/planner 的分工 |
| `validation-strategy-planner` | 探索性结果验证 | 保留按需触发 |
| `reviewer-response-builder` | 真实审稿意见 | 按需迁移 |
| `reviewer-simulation` | 投稿前风险模拟 | 补 reviewer type / response priority reference |
| `submission-readiness-audit` | 投稿前总检 | 按需迁移 |
| `manuscript-consistency-audit` | 数字/术语/图号一致性 | 按需迁移 |
| `source-data-audit` | source data / Data Availability | 按需迁移 |
| `research-data-organization` | 结果和 manifest 整理 | 按需迁移 |
| `project-environment-bootstrap` | 新项目/新机器/环境未知 | 按需迁移 |

### P3：先观察或合并

| Skill | 原因 | 建议 |
|---|---|---|
| `figure-caption` | 与 publication-plotting 重叠 | 先作为子模块或 reference |
| `task-self-check` | 和 Hermes 执行纪律重叠 | 保留为 QA reference |
| `skill-quality-audit` | 主要用于维护 skill 包本身 | 不进入默认工作流 |
| `environment-and-tool-adoption` | 与分析执行和项目环境有交叉 | 按复杂外部工具场景触发 |
| `research-decision-review` | 价值高但容易过度反对 | 保留按需触发 |
| `chinese-scientific-polishing` | 中文润色非主线高频 | 观察使用频率 |

## 4. 当前低风险优化建议

已接受的根 agent 优化方向：

- `PROJECT_PLAN.md` 作为写入型操作日志，不默认读取。
- 实质任务完成后追加简短记录。
- 纯问答、临时讨论、只读检查或用户明确不需要记录时跳过。

后续 skill 优化方向：

1. 给 P2/P3 skill 增加 `When NOT to Use` 或“不适合触发”小节。
2. 给 `claim-evidence-audit`、`reviewer-simulation`、`figure-caption` 增加 references 模板。
3. 将 `project-guide-maintainer` 的长流程进一步拆到 references。
4. 保留 GitHub 仓库为源头，Hermes 只迁移验证过的运行副本。

## 5. 首批迁移试点

首批建议只迁移三个低风险高频 skill：

```text
bioinfo-analysis-code
paper-reader
literature-search-workflow
```

迁移目标：

```text
~/.hermes/skills/bioinfo/<skill>/
```

验证：

- 目录存在
- `SKILL.md` frontmatter 合法
- references 保留
- 不修改 `~/.hermes/SOUL.md`
- 不改 Hermes 全局 config

## 6. 迭代规则

- 高频且表现稳定：保留并优化为 Hermes 原生 skill。
- 高频但误触发：收窄 description。
- 低频且项目专属：留在项目 `.codex/skills/`。
- 与其他 skill 重叠：合并或降级为 reference。
- 任务中出现真实坑点：补充 pitfall。
- 涉及科研 claim 的修改：必须保留证据等级和 caveat。
