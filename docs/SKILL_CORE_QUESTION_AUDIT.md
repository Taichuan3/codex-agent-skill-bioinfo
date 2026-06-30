# 29 Skill Core-Question Audit

> Each candidate skill should answer one core question. This audit records the current core question and whether the skill is kept, strengthened, split, or reserved for future merge review.

| Skill | Core question | Decision |
|---|---|---|
| `bioinfo-analysis-code` | 如何把生信分析从一次性脚本变成输入、输出、参数、环境和 caveat 都可追踪的可复现执行？ | strengthened / target for future strengthening |
| `chinese-scientific-polishing` | 如何在不改变证据强度的前提下，让中文科研文本更清楚、更顺、更像给真实读者看的研究叙事？ | keep |
| `citation-verifier` | 如何确认每条 citation 真实存在、元数据正确，并且确实支持它旁边的 claim？ | keep |
| `claim-evidence-audit` | 如何判断一个科学 claim 是否被当前 figure/table/source data/citation 支撑，并给出安全降级写法？ | strengthened / target for future strengthening |
| `drug-discovery-admet-screening` | 如何把靶点、化合物、筛选目标、ADMET 风险和证据来源组织成可追踪的早期药物发现筛选计划，而不把预测或数据库关联升级为药效/安全结论？ | split from broad protein/docking/drug candidate |
| `environment-and-tool-adoption` | 如何在需要外部工具或依赖时，选择成熟方案、记录来源版本 license，并避免不可复现或不可信安装？ | strengthened / target for future strengthening |
| `evidence-gap-finder` | 如何从现有结果和草稿中找出最小但关键的缺失证据，而不是盲目增加分析？ | keep |
| `figure-caption` | 如何让每个 figure title、panel title 和 caption 准确说明图中数据，同时不把解释性结论塞进图注？ | strengthened / target for future strengthening |
| `literature-search-workflow` | 如何把开放式文献问题转成可复现检索式、筛选标准、证据表和知识缺口？ | keep |
| `manuscript-consistency-audit` | 如何发现稿件内部数字、术语、样本集合、图表编号和 claim 的冲突？ | keep |
| `paper-reader` | 如何从一篇指定论文中提取可验证证据、figure grounding、方法启发和局限，而不是泛泛总结？ | keep |
| `project-environment-bootstrap` | 如何在新项目或新机器上快速确认工作目录、环境、Git/Jupyter/conda 状态并留下本地环境记录？ | keep |
| `project-guide-maintainer` | 如何把项目背景、核心问题、当前结果和下一步压缩成未来 agent 能快速读取的轻量 PROJECT_GUIDE？ | keep |
| `protein-structure-docking` | 如何在输入定义清楚、结构来源可追踪、工具选择合理的前提下，规划或解释蛋白结构与 docking 结果，而不把 docking score 误写成结合或功能证明？ | split from broad protein/docking/drug candidate |
| `publication-plotting` | 如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？ | strengthened / target for future strengthening |
| `research-data-organization` | 如何让项目数据、结果、图表和 latest 文件入口清楚，避免未来找不到或用错版本？ | keep |
| `research-decision-review` | 如何在高影响研究决策前识别风险、成本、证据边界和 stop/pivot 条件？ | keep |
| `research-project-planner` | 如何把模糊研究方向变成 central question、evidence package、figure skeleton 和可执行路线？ | keep |
| `research-question-brief` | 如何把零散想法压缩成一个短 research question brief，保留为什么重要和下一步决策？ | keep |
| `reviewer-response-builder` | 如何把真实审稿意见拆成行动计划、补分析优先级、正文修改点和礼貌但有边界的回复？ | keep |
| `reviewer-simulation` | 如何提前模拟审稿人会攻击的证据、统计、复现、图表和叙事风险？ | keep |
| `scientific-database-grounding` | 如何把基因、变异、区间、蛋白、化合物或文献判断落到可追踪数据库记录上？ | strengthened / target for future strengthening |
| `scientific-english-polishing` | 如何在不升级 claim 的前提下，把已有英文科研文本变得更清楚、更精炼、更符合学术表达？ | keep |
| `scientific-english-translation` | 如何把中文科研草稿翻译成证据边界安全、可投稿语气的英文表达？ | keep |
| `skill-quality-audit` | 如何判断一个 skill 是否触发精准、上下文高效、任务闭环、可维护，并给出修改方案？ | strengthened / target for future strengthening |
| `source-data-audit` | 如何把 manuscript figure/table/number/claim 追踪到 source data、Data/Code Availability 和 FAIR-like metadata？ | keep |
| `submission-readiness-audit` | 如何判断一篇生信稿件在主文、图表、方法、source data、代码和引用层面是否接近可投稿？ | keep |
| `task-self-check` | 如何在交付前做轻量质量门控，确认没有证据、复现、图表、路径或文字越界问题？ | strengthened / target for future strengthening |
| `validation-strategy-planner` | 如何为探索性结果或候选机制设计最小、分层、可执行的验证策略？ | keep |

## Merge / split decisions

- Split: `protein-docking-drug-discovery` was too broad, so it is replaced by `protein-structure-docking` and `drug-discovery-admet-screening`.
- No immediate merge among writing/reviewer/source-data skills: they overlap but answer different core questions along the manuscript lifecycle.
- Keep `research-question-brief` and `research-project-planner` separate: brief compresses an idea; planner designs the full route.
- Keep `project-environment-bootstrap` and `environment-and-tool-adoption` separate: one checks project environment; the other evaluates/adopts external tools.
- Keep runtime promotion separate from source repo edits: these changes remain candidate-source only until used and accepted.
