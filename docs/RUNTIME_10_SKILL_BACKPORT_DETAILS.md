# Runtime 10 Skill Backport Review Details

> This document reviews all 10 mature Hermes runtime bioinfo skills in the same format. Runtime files are local iterated copies; they are more complete but also more likely to contain duplicated, project-specific, or sedimented rules. The action here is to define how to compress/backport into the GitHub source repo without overwriting runtime.

| # | Runtime skill | Current status | Runtime size | Source size | Mature experience to keep | Sediment / redundancy risk | Backport format |
|---:|---|---|---:|---:|---|---|---|
| 1 | `publication-plotting` | 已完成第一轮 source 压缩回流 | 104 lines/14836 chars/7 refs | 88 lines/2860 chars/3 refs | figure contract、source data、visual QA、reader-facing report integration | 项目特异图经验非常多，主 skill 不宜继续承载所有案例 | 保留 runtime 暂不覆盖；source 用短主文 + report-figure-integration reference |
| 2 | `claim-evidence-audit` | 下一步处理 | 80 lines/5012 chars/2 refs | 49 lines/1270 chars/0 refs | 证据等级、claim 降级、安全改写、figure/table/source-data 对照 | 可能和 source-data-audit/submission-readiness-audit 重复 | 压缩成 claim→evidence→risk→safe wording 输出合同 |
| 3 | `bioinfo-analysis-code` | 后续处理 | 88 lines/3491 chars/7 refs | 84 lines/1723 chars/3 refs | preflight、smoke test、commands/params/manifest、output verification | 可能和新 local-first checklist 重复 | 合并到一个执行闭环 reference，删除重复原则句 |
| 4 | `literature-search-workflow` | 后续处理 | 69 lines/3847 chars/4 refs | 45 lines/970 chars/1 refs | 检索式、数据库选择、纳排标准、证据表/知识缺口 | 容易和 database grounding/citation verifier 重叠 | 强化 systematic search；数据库核验外包给 scientific-database-grounding |
| 5 | `paper-reader` | 后续处理 | 56 lines/2014 chars/2 refs | 47 lines/984 chars/1 refs | 单篇论文 figure grounding、方法提取、局限、可借鉴分析 | 容易变成系统检索 | 保持 single-paper reading 输出合同 |
| 6 | `scientific-english-polishing` | 后续处理 | 55 lines/1982 chars/2 refs | 58 lines/1892 chars/2 refs | 英文已有文本润色、压缩、section tone、claim 不升级 | 和 translation 共享很多规则，易重复 | 建立 shared writing boundary reference，保留独立入口 |
| 7 | `scientific-english-translation` | 后续处理 | 58 lines/2039 chars/2 refs | 60 lines/1775 chars/2 refs | 中文→英文转换、证据边界、安全表达、章节语气 | 和 polishing 重复但输入不同 | 共享 reference，不合并入口 |
| 8 | `chinese-scientific-polishing` | 后续处理 | 67 lines/3345 chars/1 refs | 61 lines/1741 chars/3 refs | 中文读者可读性、段落重构、证据边界、科研叙事 | 和英文写作 skill 重复证据边界 | 保留中文表达/报告风格核心 |
| 9 | `research-question-brief` | 后续轻量处理 | 51 lines/1100 chars/1 refs | 55 lines/1163 chars/1 refs | one-line idea、working question、why matters、next decision | 已经较短；不宜过度扩展 | 只对齐核心问题/输出合同 |
| 10 | `research-project-planner` | 后续轻量处理 | 65 lines/1693 chars/1 refs | 69 lines/1773 chars/1 refs | central question、evidence package、figure skeleton、路线图 | 容易和 brief 重叠 | 保持 planner 是路线设计，不是 brief |

## Per-skill review blocks

### 1. `publication-plotting`

- Current status: 已完成第一轮 source 压缩回流
- Runtime size: 104 lines / 14836 chars / refs: ['references/alphagenome-cage-matched-profile-figures.md', 'references/figure-contract.md', 'references/motif-hit-interval-landscape.md', 'references/reader-facing-report-figure-optimization.md', 'references/repeat-unit-structure-figure-cropping.md', 'references/result-report-figure-workflow.md', 'references/visual-qa.md']
- Source size: 88 lines / 2860 chars / refs: ['references/figure-contract.md', 'references/report-figure-integration.md', 'references/visual-qa.md']
- Mature experience to keep: figure contract、source data、visual QA、reader-facing report integration
- Sediment / redundancy risk: 项目特异图经验非常多，主 skill 不宜继续承载所有案例
- Backport format: 保留 runtime 暂不覆盖；source 用短主文 + report-figure-integration reference
- Source core problem: 如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？
- Runtime headings snapshot: Publication Plotting, 使用场景, 不适合触发, Figure Contract, 绘图规则, Report figure placement and captioning lessons, QA Checklist, 输出格式, 按需读取
- Source headings snapshot: Publication Plotting, 核心问题, 使用场景, 不适合触发, 最小 Figure Contract, 绘图规则, Report / manuscript figure integration, QA Checklist, 输出格式, 按需读取

### 2. `claim-evidence-audit`

- Current status: 下一步处理
- Runtime size: 80 lines / 5012 chars / refs: ['references/alphagenome_cage_track_mismatch.md', 'references/repeat_region_external_validation_claims.md']
- Source size: 49 lines / 1270 chars / refs: none
- Mature experience to keep: 证据等级、claim 降级、安全改写、figure/table/source-data 对照
- Sediment / redundancy risk: 可能和 source-data-audit/submission-readiness-audit 重复
- Backport format: 压缩成 claim→evidence→risk→safe wording 输出合同
- Source core problem: 如何判断一个科学 claim 是否被当前 figure/table/source data/citation 支撑，并给出安全降级写法？
- Runtime headings snapshot: Claim Evidence Audit, 使用场景, 不适合触发, 证据等级, 审查流程, 输出语言和用户文本处理, 输出格式, 用户报告/草稿语言偏好, 用户报告/结果段改写偏好与常见坑, 特殊场景：repeat-rich 区域的 public-data 外部验证
- Source headings snapshot: Claim Evidence Audit, 核心问题, 使用场景, 不适合触发, 证据等级, 审查流程, 输出格式

### 3. `bioinfo-analysis-code`

- Current status: 后续处理
- Runtime size: 88 lines / 3491 chars / refs: ['references/alphagenome-cage-1bp-validation.md', 'references/protein_structure_docking_workflow.md', 'references/protein_structure_prediction_docking_workflow.md', 'references/repeat_cage_cluster_sequence_workflow.md', 'references/report_reproducibility_package.md', 'references/reproducibility-levels.md', 'references/workflow-numbering.md']
- Source size: 84 lines / 1723 chars / refs: ['references/local-first-execution-checklist.md', 'references/reproducibility-levels.md', 'references/workflow-numbering.md']
- Mature experience to keep: preflight、smoke test、commands/params/manifest、output verification
- Sediment / redundancy risk: 可能和新 local-first checklist 重复
- Backport format: 合并到一个执行闭环 reference，删除重复原则句
- Source core problem: 如何把生信分析从一次性脚本变成输入、输出、参数、环境和 caveat 都可追踪的可复现执行？
- Runtime headings snapshot: Bioinfo Analysis Code, 使用场景, 执行原则, 推荐输出结构, 输出格式, 按需读取
- Source headings snapshot: Bioinfo Analysis Code, 核心问题, 使用场景, 执行原则, 推荐输出结构, 输出格式, 按需读取

### 4. `literature-search-workflow`

- Current status: 后续处理
- Runtime size: 69 lines / 3847 chars / refs: ['references/evidence-table-template.md', 'references/hypothesis-driven-repeat-alt-synthesis.md', 'references/protein-interaction-literature-search.md', 'references/repeat-alt-dataset-search.md']
- Source size: 45 lines / 970 chars / refs: ['references/evidence-table-template.md']
- Mature experience to keep: 检索式、数据库选择、纳排标准、证据表/知识缺口
- Sediment / redundancy risk: 容易和 database grounding/citation verifier 重叠
- Backport format: 强化 systematic search；数据库核验外包给 scientific-database-grounding
- Source core problem: 如何把开放式文献问题转成可复现检索式、筛选标准、证据表和知识缺口？
- Runtime headings snapshot: Literature Search Workflow, 使用场景, 核心原则, 工作流程, 输出格式, Hypothesis-driven synthesis for repeat elements / ALT / telomere projects, Molecular interaction / docking feasibility searches
- Source headings snapshot: Literature Search Workflow, 核心问题, 使用场景, 核心原则, 工作流程, 输出格式

### 5. `paper-reader`

- Current status: 后续处理
- Runtime size: 56 lines / 2014 chars / refs: ['references/alt-centromeric-footprints-d20s16.md', 'references/figure-grounding-template.md']
- Source size: 47 lines / 984 chars / refs: ['references/figure-grounding-template.md']
- Mature experience to keep: 单篇论文 figure grounding、方法提取、局限、可借鉴分析
- Sediment / redundancy risk: 容易变成系统检索
- Backport format: 保持 single-paper reading 输出合同
- Source core problem: 如何从一篇指定论文中提取可验证证据、figure grounding、方法启发和局限，而不是泛泛总结？
- Runtime headings snapshot: Paper Reader, 使用场景, 核心原则, 工作流程, 输出格式, Follow-up Q&A and project-link discipline
- Source headings snapshot: Paper Reader, 核心问题, 使用场景, 核心原则, 工作流程, 输出格式

### 6. `scientific-english-polishing`

- Current status: 后续处理
- Runtime size: 55 lines / 1982 chars / refs: ['references/high-impact-journal-writing.md', 'references/style-guardrails.md']
- Source size: 58 lines / 1892 chars / refs: ['references/high-impact-journal-writing.md', 'references/style-guardrails.md']
- Mature experience to keep: 英文已有文本润色、压缩、section tone、claim 不升级
- Sediment / redundancy risk: 和 translation 共享很多规则，易重复
- Backport format: 建立 shared writing boundary reference，保留独立入口
- Source core problem: 如何在不升级 claim 的前提下，把已有英文科研文本变得更清楚、更精炼、更符合学术表达？
- Runtime headings snapshot: Scientific English Polishing, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 按需读取
- Source headings snapshot: Scientific English Polishing, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 按需读取

### 7. `scientific-english-translation`

- Current status: 后续处理
- Runtime size: 58 lines / 2039 chars / refs: ['references/high-impact-journal-translation.md', 'references/translation-stance.md']
- Source size: 60 lines / 1775 chars / refs: ['references/high-impact-journal-translation.md', 'references/translation-stance.md']
- Mature experience to keep: 中文→英文转换、证据边界、安全表达、章节语气
- Sediment / redundancy risk: 和 polishing 重复但输入不同
- Backport format: 共享 reference，不合并入口
- Source core problem: 如何把中文科研草稿翻译成证据边界安全、可投稿语气的英文表达？
- Runtime headings snapshot: Scientific English Translation, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 风格参考, 按需读取
- Source headings snapshot: Scientific English Translation, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 输出格式, 风格参考, 按需读取

### 8. `chinese-scientific-polishing`

- Current status: 后续处理
- Runtime size: 67 lines / 3345 chars / refs: ['references/external-report-polishing-and-bundling.md']
- Source size: 61 lines / 1741 chars / refs: ['references/high-impact-journal-writing.md', 'references/polishing-checklist.md', 'references/section-responsibilities.md']
- Mature experience to keep: 中文读者可读性、段落重构、证据边界、科研叙事
- Sediment / redundancy risk: 和英文写作 skill 重复证据边界
- Backport format: 保留中文表达/报告风格核心
- Source core problem: 如何在不改变证据强度的前提下，让中文科研文本更清楚、更顺、更像给真实读者看的研究叙事？
- Runtime headings snapshot: Chinese Scientific Polishing, 使用场景, 核心原则, 用户偏好与常见坑, 工作流程, Methods 改写规则, 输出格式
- Source headings snapshot: Chinese Scientific Polishing, 核心问题, 使用场景, 核心原则, 各部分功能, 工作流程, 输出格式, 按需读取

### 9. `research-question-brief`

- Current status: 后续轻量处理
- Runtime size: 51 lines / 1100 chars / refs: ['references/research-question-brief-template.md']
- Source size: 55 lines / 1163 chars / refs: ['references/research-question-brief-template.md']
- Mature experience to keep: one-line idea、working question、why matters、next decision
- Sediment / redundancy risk: 已经较短；不宜过度扩展
- Backport format: 只对齐核心问题/输出合同
- Source core problem: 如何把零散想法压缩成一个短 research question brief，保留为什么重要和下一步决策？
- Runtime headings snapshot: Research Question Brief, 使用场景, 不适合触发, 核心原则, 推荐结构, 工作流程, 输出规则
- Source headings snapshot: Research Question Brief, 核心问题, 使用场景, 不适合触发, 核心原则, 推荐结构, 工作流程, 输出规则

### 10. `research-project-planner`

- Current status: 后续轻量处理
- Runtime size: 65 lines / 1693 chars / refs: ['references/project-brief-template.md']
- Source size: 69 lines / 1773 chars / refs: ['references/project-brief-template.md']
- Mature experience to keep: central question、evidence package、figure skeleton、路线图
- Sediment / redundancy risk: 容易和 brief 重叠
- Backport format: 保持 planner 是路线设计，不是 brief
- Source core problem: 如何把模糊研究方向变成 central question、evidence package、figure skeleton 和可执行路线？
- Runtime headings snapshot: Research Project Planner, 使用场景, 不适合触发, 核心原则, 工作流程, 必要输出, 可选参考
- Source headings snapshot: Research Project Planner, 核心问题, 使用场景, 不适合触发, 核心原则, 工作流程, 必要输出, 可选参考

## Execution rule

Process every runtime-overlap skill with this format before declaring the old-skill optimization pass complete. Do not stop after one skill; if editing is too large for one commit, keep the audit complete and split implementation commits by skill.
