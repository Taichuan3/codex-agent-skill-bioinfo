# All Source Skills Review Matrix

> Branch: `Hermes-review`. This is the complete batch review requested by the user: all 29 source skills are checked in the same format, with runtime overlap noted where applicable. This is an audit/review pass, not runtime promotion.

## Format

Each row records: current layer, core problem, observed issue, handling action, and boundary to preserve. “runtime-overlap” means a mature runtime copy exists and should be mined carefully; it does not mean direct overwrite.

| # | Skill | Layer | Source size | Runtime copy | Core problem | Main issue / sediment risk | Handling action | Boundary to preserve |
|---:|---|---|---:|---|---|---|---|---|
| 1 | `bioinfo-analysis-code` | runtime-overlap | 84 lines/1723 chars/3 refs | yes: 88 lines/3491 chars | 如何把生信分析从一次性脚本变成输入、输出、参数、环境和 caveat 都可追踪的可复现执行？ | 容易和 project-environment-bootstrap、task-self-check 重复；应保持“执行与表格/脚本”核心 | 把 runtime 的 preflight/smoke/output verification 与 source 的 local-first checklist 合并去重 | 保留执行闭环：输入锁定→小样本/烟测→全量→输出校验→manifest/commands/params |
| 2 | `chinese-scientific-polishing` | runtime-overlap | 61 lines/1741 chars/3 refs | yes: 67 lines/3345 chars | 如何在不改变证据强度的前提下，让中文科研文本更清楚、更顺、更像给真实读者看的研究叙事？ | 容易和英文 polishing/translation 重复；证据边界可共享但入口不能合并 | 回流 runtime 中中文段落重构、读者可读性、结果/讨论差异；压缩重复的证据边界提醒 | 保留中文写作体验：清楚、顺、读者能读懂，不改变 claim |
| 3 | `citation-verifier` | source-only | 37 lines/829 chars/1 refs | no | 如何确认每条 citation 真实存在、元数据正确，并且确实支持它旁边的 claim？ | 不要变成开放式文献检索或 Zotero 管理器 | 补齐与 literature-search-workflow/paper-reader 的边界；吸收外部 citation-management 的 DOI/PMID/BibTeX metadata 检查 | 保留核验 citation 是否真实且支持旁边 claim 的核心 |
| 4 | `claim-evidence-audit` | runtime-overlap | 49 lines/1270 chars/0 refs | yes: 80 lines/5012 chars | 如何判断一个科学 claim 是否被当前 figure/table/source data/citation 支撑，并给出安全降级写法？ | runtime 更完整但容易过宽；source 目前过短 | 从 runtime 回流成熟的证据等级、claim 降级、figure/table/source-data 对照；删除和 source-data-audit/submission-audit 重复的全局检查 | 保留 claim→evidence→safe wording 的审查核心 |
| 5 | `drug-discovery-admet-screening` | new-candidate | 55 lines/1838 chars/1 refs | no | 如何把靶点、化合物、筛选目标、ADMET 风险和证据来源组织成可追踪的早期药物发现筛选计划，而不把预测或数据库关联升级为药效/安全结论？ | 不要混入具体 docking pose，也不要做个人医疗/用药建议 | 保持 candidate；补真实使用后再扩展，不进入 runtime；继续强化 target/compound/ADMET evidence table | 保留 early drug discovery screening strategy 核心 |
| 6 | `environment-and-tool-adoption` | source-only | 53 lines/1088 chars/1 refs | no | 如何在需要外部工具或依赖时，选择成熟方案、记录来源版本 license，并避免不可复现或不可信安装？ | 不要每次缺包都触发长审计；只在复杂外部工具/论文代码时触发 | 连接 bioinfo-analysis-code 的执行前依赖评估；吸收 license/source/version/adaptation record | 保留成熟工具采用与重复造轮子规避核心 |
| 7 | `evidence-gap-finder` | source-only | 37 lines/765 chars/1 refs | no | 如何从现有结果和草稿中找出最小但关键的缺失证据，而不是盲目增加分析？ | 不要变成泛泛 reviewer simulation | 增强最小补分析/最小验证集合；与 validation-strategy-planner 分工：前者找缺口，后者设计验证 | 保留“缺什么证据才能支撑 claim”的核心 |
| 8 | `figure-caption` | source-only | 46 lines/949 chars/0 refs | no | 如何让每个 figure title、panel title 和 caption 准确说明图中数据，同时不把解释性结论塞进图注？ | 不要承担绘图执行；不要把结论塞进 caption | 继续强化 caption vs Results prose、panel title、denominator/source-data boundary；与 publication-plotting 共享但不合并 | 保留 figure title/panel/caption 文本核心 |
| 9 | `literature-search-workflow` | runtime-overlap | 45 lines/970 chars/1 refs | yes: 69 lines/3847 chars | 如何把开放式文献问题转成可复现检索式、筛选标准、证据表和知识缺口？ | 容易和 paper-reader/citation-verifier/scientific-database-grounding 混淆 | 回流 runtime 的检索式、数据库选择、纳排标准、证据表；接入 database grounding 但不变成数据库查询 skill | 保留系统文献检索和知识缺口整理核心 |
| 10 | `manuscript-consistency-audit` | source-only | 36 lines/763 chars/1 refs | no | 如何发现稿件内部数字、术语、样本集合、图表编号和 claim 的冲突？ | 不要扩成投稿全检查 | 强化数字/术语/样本集合/figure 编号一致性；与 claim-evidence/source-data/submission 分层 | 保留稿件内部一致性核心 |
| 11 | `paper-reader` | runtime-overlap | 47 lines/984 chars/1 refs | yes: 56 lines/2014 chars | 如何从一篇指定论文中提取可验证证据、figure grounding、方法启发和局限，而不是泛泛总结？ | 不要变成 literature search 或 citation verifier | 回流 runtime 的 figure grounding、方法提取、局限与可借鉴模块；保持单篇论文边界 | 保留指定论文深读核心 |
| 12 | `project-environment-bootstrap` | source-only | 79 lines/2304 chars/5 refs | no | 如何在新项目或新机器上快速确认工作目录、环境、Git/Jupyter/conda 状态并留下本地环境记录？ | 不要成为日常分析前的强制流程 | 压缩环境初始化规则；保持只在新项目/切机器/环境未知触发 | 保留项目环境入口记录核心 |
| 13 | `project-guide-maintainer` | source-only | 98 lines/2415 chars/1 refs | no | 如何把项目背景、核心问题、当前结果和下一步压缩成未来 agent 能快速读取的轻量 PROJECT_GUIDE？ | 不要和 PROJECT_PLAN 操作日志混淆 | 压缩 PROJECT_GUIDE 更新时机；吸收 context compression，但不写流水账 | 保留轻量项目入口文档核心 |
| 14 | `protein-structure-docking` | new-candidate | 72 lines/2435 chars/1 refs | no | 如何在输入定义清楚、结构来源可追踪、工具选择合理的前提下，规划或解释蛋白结构与 docking 结果，而不把 docking score 误写成结合或功能证明？ | 不要混入 ADMET/virtual screening/target validation | 保持 candidate；真实项目后再扩展；继续锁定输入定义、准备/QC、pose interpretation boundary | 保留 protein structure/docking interpretation 核心 |
| 15 | `publication-plotting` | runtime-overlap | 88 lines/2860 chars/3 refs | yes: 104 lines/14836 chars | 如何把分析结果转成 manuscript-ready figure、source data 和可追踪的 panel contract？ | runtime 沉积很多项目特异图经验；不能整篇复制 | 已完成第一轮压缩回流：主 skill 保持短，复杂报告图经验进入 reference | 保留 figure contract/source data/visual QA/document link integration 核心 |
| 16 | `research-data-organization` | source-only | 77 lines/1624 chars/2 refs | no | 如何让项目数据、结果、图表和 latest 文件入口清楚，避免未来找不到或用错版本？ | 不要变成清理所有目录的泛用文件管家 | 强化 latest/priority/manifest 规则；和 source-data-audit 分工：组织项目文件 vs 投稿 source-data traceability | 保留研究文件入口与结果定位核心 |
| 17 | `research-decision-review` | source-only | 48 lines/1120 chars/1 refs | no | 如何在高影响研究决策前识别风险、成本、证据边界和 stop/pivot 条件？ | 不要对普通执行任务过度反对 | 强化建设性反对、stop/pivot criteria、成本/证据/审稿风险矩阵 | 保留高影响决策审查核心 |
| 18 | `research-project-planner` | runtime-overlap | 69 lines/1773 chars/1 refs | yes: 65 lines/1693 chars | 如何把模糊研究方向变成 central question、evidence package、figure skeleton 和可执行路线？ | 容易和 research-question-brief 重叠；planner 应从 brief 走向路线 | 回流 runtime 中研究路线/figure skeleton/证据包经验；避免过长模板 | 保留从模糊方向到可执行项目路线核心 |
| 19 | `research-question-brief` | runtime-overlap | 55 lines/1163 chars/1 refs | yes: 51 lines/1100 chars | 如何把零散想法压缩成一个短 research question brief，保留为什么重要和下一步决策？ | 不要写成 project planner | 轻量对齐 runtime/source；保持短，不引入完整规划 | 保留把想法压缩成 research question brief 核心 |
| 20 | `reviewer-response-builder` | source-only | 38 lines/967 chars/1 refs | no | 如何把真实审稿意见拆成行动计划、补分析优先级、正文修改点和礼貌但有边界的回复？ | 不要模拟潜在意见；只处理真实 comments | 吸收 reviewer comment table、action/response/risk 输出；与 reviewer-simulation 分工 | 保留真实审稿回复构建核心 |
| 21 | `reviewer-simulation` | source-only | 42 lines/702 chars/0 refs | no | 如何提前模拟审稿人会攻击的证据、统计、复现、图表和叙事风险？ | 不要变成 response letter builder | 吸收 external reviewer attack list；输出按严重度排序并区分文字澄清 vs 新分析 | 保留提前发现审稿风险核心 |
| 22 | `scientific-database-grounding` | new-candidate | 67 lines/2667 chars/1 refs | no | 如何把基因、变异、区间、蛋白、化合物或文献判断落到可追踪数据库记录上？ | 不要变成 literature search 或 drug discovery 业务逻辑 | 保持独立 candidate；继续补 database source map/provenance/Entrez/冲突处理 | 保留实体→数据库记录→evidence map 核心 |
| 23 | `scientific-english-polishing` | runtime-overlap | 58 lines/1892 chars/2 refs | yes: 55 lines/1982 chars | 如何在不升级 claim 的前提下，把已有英文科研文本变得更清楚、更精炼、更符合学术表达？ | 不要把中文翻译任务拉进来 | 回流 runtime 中 section-specific polish、压缩、学术语气；与 translation 共享边界但不合并 | 保留已有英文文本润色核心 |
| 24 | `scientific-english-translation` | runtime-overlap | 60 lines/1775 chars/2 refs | yes: 58 lines/2039 chars | 如何把中文科研草稿翻译成证据边界安全、可投稿语气的英文表达？ | 不要变成英文润色入口 | 回流 runtime 的中文→英文证据边界、安全表达、章节语气；和 polishing 保持独立触发 | 保留中文科研草稿转英文核心 |
| 25 | `skill-quality-audit` | source-only | 54 lines/1221 chars/2 refs | no | 如何判断一个 skill 是否触发精准、上下文高效、任务闭环、可维护，并给出修改方案？ | 不要承载领域内容 | 继续作为 meta-skill；吸收 one-core-question、external absorption rubric、progressive disclosure 检查 | 保留审查 skill 质量和触发精准性的核心 |
| 26 | `source-data-audit` | source-only | 58 lines/1321 chars/2 refs | no | 如何把 manuscript figure/table/number/claim 追踪到 source data、Data/Code Availability 和 FAIR-like metadata？ | 不要变成绘图 skill 或全投稿检查 | 强化 figure/table/number/source-data traceability 与 FAIR-like metadata；与 publication-plotting 连接 | 保留 source-data inventory 核心 |
| 27 | `submission-readiness-audit` | source-only | 47 lines/1065 chars/1 refs | no | 如何判断一篇生信稿件在主文、图表、方法、source data、代码和引用层面是否接近可投稿？ | 不要用于普通任务交付前轻量自检 | 强化投稿前综合门槛；整合但不吞并 consistency/source-data/citation checks | 保留投稿前 readiness gate 核心 |
| 28 | `task-self-check` | source-only | 48 lines/938 chars/1 refs | no | 如何在交付前做轻量质量门控，确认没有证据、复现、图表、路径或文字越界问题？ | 不要代替专项审查 skill | 吸收 verification-before-completion；保持轻量交付前自检 | 保留任务完成前最低门槛核心 |
| 29 | `validation-strategy-planner` | source-only | 39 lines/934 chars/1 refs | no | 如何为探索性结果或候选机制设计最小、分层、可执行的验证策略？ | 不要代替 evidence-gap-finder 找缺口 | 强化计算/外部数据/统计敏感性/实验验证分层和降级写法 | 保留为探索性结果设计验证策略核心 |

## Batch conclusions

- The work should proceed as batch old-skill optimization, not one-off new-skill creation.
- Runtime copies are richer but may contain repeated and project-specific rules; they should be mined, compressed and backported into source, not copied wholesale.
- Source-only candidate skills should be reviewed in the same format, but not promoted to runtime during this pass.
- Every skill should keep one core question. Shared caveats should move to references or neighboring skill boundaries instead of being repeated everywhere.
