# Runtime Skill Backport Audit

> Branch: `Hermes-review`. Purpose: audit the 10 mature Hermes runtime bioinfo skills before changing source or runtime files. Runtime skills are richer because they were iterated locally, but they may also contain duplicated or sedimented rules. This document decides what should be compressed and backported into the GitHub source repo, and what should remain runtime-only or be discarded.

## Scope

- Runtime source: `~/.hermes/skills/bioinfo/`
- GitHub source repo: `.codex/skills/`
- Rule: do not overwrite runtime from source. First extract mature patterns, compress them, then update source on `Hermes-review`. Runtime promotion remains a separate later step.

## Summary table

| Skill | Runtime size | Source size | Runtime complexity | Immediate handling | Main risk |
|---|---:|---:|---|---|---|
| `publication-plotting` | 104 lines / 14836 chars / 7 refs | 67 lines / 1612 chars / 2 refs | high | 压缩回流 figure contract/source data/visual QA；runtime 太长，不可整篇覆盖 source | 最高复杂度：实战规则多但沉积重，需拆成 always-visible 核心 + references |
| `claim-evidence-audit` | 80 lines / 5012 chars / 2 refs | 49 lines / 1270 chars / 0 refs | medium | 回流证据等级、claim 降级、figure/table/source-data 对照；压缩重复 caveat | source 过短，runtime 规则成熟但可能和 source-data/submission audit 重叠 |
| `bioinfo-analysis-code` | 88 lines / 3491 chars / 7 refs | 84 lines / 1723 chars / 3 refs | high | 回流 preflight/smoke/output verification；与新 local-first checklist 合并去重 | runtime 与新增 checklist 可能重复，需统一到一个执行闭环 |
| `literature-search-workflow` | 69 lines / 3847 chars / 4 refs | 45 lines / 970 chars / 1 refs | medium | 回流检索式、纳排标准、证据表；保持与 database-grounding/citation-verifier 分工 | 避免变成 paper-reader 或数据库 API wrapper |
| `paper-reader` | 56 lines / 2014 chars / 2 refs | 47 lines / 984 chars / 1 refs | medium | 回流 figure grounding、方法提取、limitations；保持单篇阅读边界 | 避免膨胀成系统综述 |
| `scientific-english-polishing` | 55 lines / 1982 chars / 2 refs | 58 lines / 1892 chars / 2 refs | medium | 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口 | 三种写作 skill 容易重复证据边界规则 |
| `scientific-english-translation` | 58 lines / 2039 chars / 2 refs | 60 lines / 1775 chars / 2 refs | medium | 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口 | 三种写作 skill 容易重复证据边界规则 |
| `chinese-scientific-polishing` | 67 lines / 3345 chars / 1 refs | 61 lines / 1741 chars / 3 refs | medium | 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口 | 三种写作 skill 容易重复证据边界规则 |
| `research-question-brief` | 51 lines / 1100 chars / 1 refs | 55 lines / 1163 chars / 1 refs | low | 回流简洁问题定义和输出合同；保留 source 的核心问题结构 | runtime/source 差异小，轻量对齐即可 |
| `research-project-planner` | 65 lines / 1693 chars / 1 refs | 69 lines / 1773 chars / 1 refs | low | 回流简洁问题定义和输出合同；保留 source 的核心问题结构 | runtime/source 差异小，轻量对齐即可 |

## Per-skill audit

### `publication-plotting`

- Runtime: 104 lines, 14836 chars, refs=['alphagenome-cage-matched-profile-figures.md', 'figure-contract.md', 'motif-hit-interval-landscape.md', 'reader-facing-report-figure-optimization.md', 'repeat-unit-structure-figure-cropping.md', 'result-report-figure-workflow.md', 'visual-qa.md']
- Source: 67 lines, 1612 chars, refs=['figure-contract.md', 'visual-qa.md']
- Runtime headings: Publication Plotting, 使用场景, 不适合触发, Figure Contract, 绘图规则, Report figure placement and captioning lessons, QA Checklist, 输出格式, 按需读取
- Source headings: Publication Plotting, 核心问题, 使用场景, 不适合触发, Figure Contract, 绘图规则, QA Checklist, 输出格式, 按需读取
- Runtime sections not represented in source: Report figure placement and captioning lessons
- Source sections absent in runtime: 核心问题
- Handling: 压缩回流 figure contract/source data/visual QA；runtime 太长，不可整篇覆盖 source
- Caveat: 最高复杂度：实战规则多但沉积重，需拆成 always-visible 核心 + references

### `claim-evidence-audit`

- Runtime: 80 lines, 5012 chars, refs=['alphagenome_cage_track_mismatch.md', 'repeat_region_external_validation_claims.md']
- Source: 49 lines, 1270 chars, refs=none
- Runtime headings: Claim Evidence Audit, 使用场景, 不适合触发, 证据等级, 审查流程, 输出语言和用户文本处理, 输出格式, 用户报告/草稿语言偏好, 用户报告/结果段改写偏好与常见坑, 特殊场景：repeat-rich 区域的 public-data 外部验证
- Source headings: Claim Evidence Audit, 核心问题, 使用场景, 不适合触发, 证据等级, 审查流程, 输出格式
- Runtime sections not represented in source: 输出语言和用户文本处理, 用户报告/草稿语言偏好, 用户报告/结果段改写偏好与常见坑, 特殊场景：repeat-rich 区域的 public-data 外部验证
- Source sections absent in runtime: 核心问题
- Handling: 回流证据等级、claim 降级、figure/table/source-data 对照；压缩重复 caveat
- Caveat: source 过短，runtime 规则成熟但可能和 source-data/submission audit 重叠

### `bioinfo-analysis-code`

- Runtime: 88 lines, 3491 chars, refs=['alphagenome-cage-1bp-validation.md', 'protein_structure_docking_workflow.md', 'protein_structure_prediction_docking_workflow.md', 'repeat_cage_cluster_sequence_workflow.md', 'report_reproducibility_package.md', 'reproducibility-levels.md', 'workflow-numbering.md']
- Source: 84 lines, 1723 chars, refs=['local-first-execution-checklist.md', 'reproducibility-levels.md', 'workflow-numbering.md']
- Runtime headings: Bioinfo Analysis Code, 使用场景, 执行原则, 推荐输出结构, 输出格式, 按需读取
- Source headings: Bioinfo Analysis Code, 核心问题, 使用场景, 执行原则, 推荐输出结构, 输出格式, 按需读取
- Source sections absent in runtime: 核心问题
- Handling: 回流 preflight/smoke/output verification；与新 local-first checklist 合并去重
- Caveat: runtime 与新增 checklist 可能重复，需统一到一个执行闭环

### `literature-search-workflow`

- Runtime: 69 lines, 3847 chars, refs=['evidence-table-template.md', 'hypothesis-driven-repeat-alt-synthesis.md', 'protein-interaction-literature-search.md', 'repeat-alt-dataset-search.md']
- Source: 45 lines, 970 chars, refs=['evidence-table-template.md']
- Runtime headings: Literature Search Workflow, 使用场景, 核心原则, 工作流程, 输出格式, Hypothesis-driven synthesis for repeat elements / ALT / telomere projects, Molecular interaction / docking feasibility searches
- Source headings: Literature Search Workflow, 核心问题, 使用场景, 核心原则, 工作流程, 输出格式
- Runtime sections not represented in source: Hypothesis-driven synthesis for repeat elements / ALT / telomere projects, Molecular interaction / docking feasibility searches
- Source sections absent in runtime: 核心问题
- Handling: 回流检索式、纳排标准、证据表；保持与 database-grounding/citation-verifier 分工
- Caveat: 避免变成 paper-reader 或数据库 API wrapper

### `paper-reader`

- Runtime: 56 lines, 2014 chars, refs=['alt-centromeric-footprints-d20s16.md', 'figure-grounding-template.md']
- Source: 47 lines, 984 chars, refs=['figure-grounding-template.md']
- Runtime headings: Paper Reader, 使用场景, 核心原则, 工作流程, 输出格式, Follow-up Q&A and project-link discipline
- Source headings: Paper Reader, 核心问题, 使用场景, 核心原则, 工作流程, 输出格式
- Runtime sections not represented in source: Follow-up Q&A and project-link discipline
- Source sections absent in runtime: 核心问题
- Handling: 回流 figure grounding、方法提取、limitations；保持单篇阅读边界
- Caveat: 避免膨胀成系统综述

### `scientific-english-polishing`

- Runtime: 55 lines, 1982 chars, refs=['high-impact-journal-writing.md', 'style-guardrails.md']
- Source: 58 lines, 1892 chars, refs=['high-impact-journal-writing.md', 'style-guardrails.md']
- Runtime headings: Scientific English Polishing, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 按需读取
- Source headings: Scientific English Polishing, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 按需读取
- Source sections absent in runtime: 核心问题
- Handling: 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口
- Caveat: 三种写作 skill 容易重复证据边界规则

### `scientific-english-translation`

- Runtime: 58 lines, 2039 chars, refs=['high-impact-journal-translation.md', 'translation-stance.md']
- Source: 60 lines, 1775 chars, refs=['high-impact-journal-translation.md', 'translation-stance.md']
- Runtime headings: Scientific English Translation, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 风格参考, 按需读取
- Source headings: Scientific English Translation, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 风格参考, 按需读取
- Source sections absent in runtime: 核心问题
- Handling: 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口
- Caveat: 三种写作 skill 容易重复证据边界规则

### `chinese-scientific-polishing`

- Runtime: 67 lines, 3345 chars, refs=['external-report-polishing-and-bundling.md']
- Source: 61 lines, 1741 chars, refs=['high-impact-journal-writing.md', 'polishing-checklist.md', 'section-responsibilities.md']
- Runtime headings: Chinese Scientific Polishing, 使用场景, 核心原则, 用户偏好与常见坑, 工作流程, Methods 改写规则, 输出格式
- Source headings: Chinese Scientific Polishing, 核心问题, 使用场景, 核心原则, 各部分功能, 工作流程, 输出格式, 按需读取
- Runtime sections not represented in source: 用户偏好与常见坑, Methods 改写规则
- Source sections absent in runtime: 核心问题, 各部分功能, 按需读取
- Handling: 回流 section-specific 语气、claim 不升级、response/manuscript 表达边界；可共享 reference 不合并入口
- Caveat: 三种写作 skill 容易重复证据边界规则

### `research-question-brief`

- Runtime: 51 lines, 1100 chars, refs=['research-question-brief-template.md']
- Source: 55 lines, 1163 chars, refs=['research-question-brief-template.md']
- Runtime headings: Research Question Brief, 使用场景, 不适合触发, 核心原则, 推荐结构, 工作流程, 输出规则
- Source headings: Research Question Brief, 核心问题, 使用场景, 不适合触发, 核心原则, 推荐结构, 工作流程, 输出规则
- Source sections absent in runtime: 核心问题
- Handling: 回流简洁问题定义和输出合同；保留 source 的核心问题结构
- Caveat: runtime/source 差异小，轻量对齐即可

### `research-project-planner`

- Runtime: 65 lines, 1693 chars, refs=['project-brief-template.md']
- Source: 69 lines, 1773 chars, refs=['project-brief-template.md']
- Runtime headings: Research Project Planner, 使用场景, 不适合触发, 核心原则, 工作流程, 必要输出, 可选参考
- Source headings: Research Project Planner, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 必要输出, 可选参考
- Source sections absent in runtime: 核心问题
- Handling: 回流简洁问题定义和输出合同；保留 source 的核心问题结构
- Caveat: runtime/source 差异小，轻量对齐即可

## Execution order for old-skill optimization

This is an execution order, not a value ranking:

1. `publication-plotting`
2. `claim-evidence-audit`
3. `bioinfo-analysis-code`
4. `literature-search-workflow`
5. `paper-reader`
6. `scientific-english-polishing`
7. `scientific-english-translation`
8. `chinese-scientific-polishing`
9. `research-question-brief`
10. `research-project-planner`

## Backport policy

- Prefer source repo edits first; runtime edits only after source version is reviewed and accepted.
- Backport mature runtime rules as compressed mechanisms, not full prose dumps.
- Preserve the new source convention that every skill states one `## 核心问题`.
- Split always-visible core rules from bulky examples/references.
- If runtime contains useful but duplicated rules, keep one canonical wording in source and reference it from related skills rather than repeating it.
- Do not promote new candidate skills into runtime during this old-skill pass.

## First target recommended by execution order

Start with `publication-plotting` because it is the most complex mature runtime skill and likely contains the most practical figure/source-data rules. The goal is not to shorten it blindly, but to extract a clean source version with:

- one core question;
- a small always-visible workflow;
- figure contract / source-data / visual QA as references;
- explicit boundary with `figure-caption`, `claim-evidence-audit`, and `source-data-audit`.

## Complete batch-review follow-up

The first version of this audit started with `publication-plotting`. The complete same-format batch review is now split into:

- `docs/ALL_29_SKILL_REVIEW_MATRIX.md` — all 29 source skills, including source-only candidates and runtime-overlap skills.
- `docs/RUNTIME_10_SKILL_BACKPORT_DETAILS.md` — all 10 mature Hermes runtime skills with the same backport/sediment review format.

Use those two documents as the checklist before editing further old skills.
