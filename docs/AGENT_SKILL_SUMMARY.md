# 通用生信 AGENT 与 Skill 使用说明

更新日期：2026-05-19

本文件用于人工审阅当前 `journal_codex_AGENT` 打包版中的通用生信研究 AGENT 与本地 skills。它不是新的规则源，不替代 `AGENTS.md` 或 `.codex/skills/*/SKILL.md`；它的作用是帮助用户理解当前体系已经完成到什么程度、每个模块负责什么、未来使用时应该如何触发。

v1.3 打包状态：

- 包内包含 1 个根 `AGENTS.md` 和 26 个通用 skill。
- 每个 skill 均包含 `SKILL.md` 和 Codex UI 元数据 `agents/openai.yaml`。
- 合规审计见 `docs/SKILL_AUDIT.md`。
- v1.2 已新增文献/引用、投稿一致性、真实审稿回复、证据缺口和验证策略 skills；后续候选能力见 `docs/REFERENCE_CANDIDATES.md`。
- v1.3 已新增 `project-environment-bootstrap`，用于新项目启动、切换机器/目录、环境未知或缺少 `PROJECT_ENVIRONMENT.md` 时检查本地环境；日常编码、绘图、分析、写作和翻译不触发。

## 1. 当前设计目标

当前体系的目标是构建一个“通用生信科研智能体”，用于支持不同生物信息学项目。它应覆盖研究前期规划、项目指导文件维护、数据分析、代码复现、图表制作、论文写作、审稿模拟、source data、工具采用和交付前自检。

核心设计原则：

- 根 `AGENTS.md` 保持短，只放跨项目通用规则。
- 具体任务细节下沉到 skill。
- 项目背景、核心问题、研究主线、路线和当前进度放到轻量 `PROJECT_GUIDE.md` 或同等项目指导文件。
- 具体项目的专属术语、固定路径、特殊 caveat 和长期解释边界可放到 `project_profiles/<project>/AGENTS.md`。
- 长 checklist、模板、rubric 和例子放到 skill 的 `references/` 中，按需读取。
- 默认中文沟通，但代码、文件名、列名、数据库名、方法名、图中坐标轴和通用术语可保留英文。
- 科研结论必须有证据来源，不允许模型凭常识自动补全未验证结论。

这个结构参考了 Anthropic skill 的思路：skill 是一个自包含目录，`SKILL.md` 负责说明“这个 skill 是什么、什么时候触发、核心流程是什么”，复杂细节放在同目录下的 `references/`、脚本或资源中。

## 2. 根 AGENT 的定位

根文件：

```text
journal_codex_AGENT/AGENTS.md
```

根 AGENT 当前只负责以下几件事：

- 定义 agent 身份：长期协作的生物信息学研究 agent。
- 定义默认沟通语言：中文为主，技术术语可保留英文。
- 定义上下文读取原则：只读取最小必要上下文。
- 定义 skill 路由：根据任务类型选择对应 skill。
- 定义证据等级：Strong、Moderate、Exploratory、Speculative。
- 定义硬约束：原始数据只读、不静默改变参数或环境、外部工具要记录来源等。
- 定义建设性反对：当方案有逻辑、证据、复现、图表或审稿风险时，必须指出并给替代方案。
- 定义输出标准：说明改了什么、文件在哪里、证据等级/caveat 是什么、是否建议写入长期记录。

根 AGENT 不再承载：

- 详细绘图 QA checklist。
- 详细代码复现 checklist。
- 详细 source data 字段和投稿前审计流程。
- 论文各章节润色规则。
- 具体项目背景和专属 caveat。
- `paper-writing` / `lab-analysis` 两个子 AGENT。

## 3. 上下文读取规则

当前最重要的上下文规则是：先理解用户需求，再选择 skill；读取足够理解任务的轻量背景，但避免被长项目记录占满。

默认读取顺序：

1. 当前任务对应的 `.codex/skills/*/SKILL.md`
2. `PROJECT_GUIDE.md` 或同等轻量项目指导文件中的摘要、背景、核心问题、结果/图表骨架和当前进度
3. 必要的 `project_profiles/<project>/AGENTS.md`
4. 用户明确指定的草稿、表格、脚本、图或模块文档

`PROJECT_GUIDE.md` 是理解研究背景和当前主线的优先入口。它应由 `research-question-brief`、`research-project-planner` 和 `project-guide-maintainer` 共同维护，内容尽量短，但要能说明研究背景、主要想法、路线、当前进度和论文主体骨架。

`PROJECT_PLAN.md` 或同等项目计划默认是操作记录/复盘对象，不是每次任务的默认读取对象。只有以下情况才建议读取：

- 任务无法继续，需要查历史操作或具体输出。
- 用户要求复盘。
- 上下文回忆不足，会影响判断。
- 需要把本次结果写入长期记录。

这个设计是为了解决之前反复读取长项目计划导致上下文浪费的问题。

## 4. 证据等级

所有写作、图表解释、审稿模拟、claim 审查都应使用以下等级：

| 等级 | 含义 | 可写作强度 |
|---|---|---|
| Strong | 有当前项目直接输出，且有 table、figure、script、source data 或已发表论文支撑 | 可以作为 Results 的主要结论 |
| Moderate | 多个分析模块一致，或 prior publication 与当前分析共同支持 | 可以写为较稳健观察，但需保留范围 |
| Exploratory | 早期分析、有限参数检查、局部复核、manual review 未完成或统计背景仍需确认 | 只能写为候选、提示、观察或探索性结果 |
| Speculative | 尚无直接验证的功能、机制或因果假说 | 不应写成 Results 强结论，可放 Discussion 并明确假说性质 |

关键规则：

- 不能把 exploratory 结果写成 definitive conclusion。
- 不能把 association 写成 causation。
- 不能把候选机制写成已证明机制。
- 不能发明样本数、统计结果、文献或机制。
- 用户要求更强表述时，应指出证据缺口，并给出安全降级写法。

## 5. 通用 Skill 总览

当前通用 skill 位于：

```text
/Users/yajiehu/bioinfo/.codex/skills/
```

通用 skill 可以分为 9 个模块：

1. 研究启动与问题整理
2. 项目指导文件维护
3. 证据与审稿风险
4. 写作与语言
5. 图表与图注
6. 数据组织与 source data
7. 代码与复现
8. 环境与外部工具
9. 自检与 skill 审计

下面逐一说明。

## 6. 研究启动与问题整理

### 6.1 `research-project-planner`

路径：

```text
.codex/skills/research-project-planner/SKILL.md
```

用途：

用于项目开始前的背景调查、研究问题澄清、知识缺口定位、可检验假设、证据包、figure skeleton 和技术路线设计。

适合触发的情况：

- “我想做一个课题，但目标不清楚。”
- “帮我规划研究路线。”
- “先做背景调查和技术路线。”
- “这个想法能不能做成论文？”

核心输出：

- `Central question`
- `Known / background`
- `Knowledge gap`
- `Hypothesis`
- `Expected claim`
- `Evidence package`
- `Figure skeleton`
- `Technical route`
- `Risks and alternatives`
- `Stop / pivot criteria`
- `Immediate next actions`

设计意图：

这个 skill 不是直接做分析，也不是直接写论文，而是在项目开始前帮助用户把模糊方向变成可执行研究路线。它强调“从科学问题开始，不从我会什么分析开始”。

参考文件：

```text
.codex/skills/research-project-planner/references/project-brief-template.md
```

### 6.2 `research-question-brief`

路径：

```text
.codex/skills/research-question-brief/SKILL.md
```

用途：

把用户口头或零散描述的原始研究想法整理成短 brief。

适合触发的情况：

- 用户还在讨论阶段，没有形成完整项目。
- 用户希望保留一个短方向文档。
- 多轮交流后，需要把想法压缩成不超过 1 页的方向记录。

推荐结构：

- `One-line idea`
- `Current working question`
- `Why it matters`
- `Possible hypothesis`
- `Evidence needed`
- `Current constraints`
- `Open questions`
- `Next decision`

与 `research-project-planner` 的区别：

- `research-question-brief` 维护“用户原始想法的短文档”。
- `research-project-planner` 设计“完整项目路线和证据链”。

设计意图：

减少长记录对上下文的占用。它只保存主要论点、目标、边界、证据需求和下一步，不保存长背景、完整文献笔记或大量路径。

参考文件：

```text
.codex/skills/research-question-brief/references/research-question-brief-template.md
```

### 6.3 `project-guide-maintainer`

路径：

```text
.codex/skills/project-guide-maintainer/SKILL.md
```

用途：

创建、更新或压缩轻量 `PROJECT_GUIDE.md` 项目指导文件。它把 `research-question-brief` 的原始想法和 `research-project-planner` 的项目路线整合成后续任务可以快速读取的研究背景、核心问题、主线、路线、当前进度和论文骨架。

适合触发的情况：

- “维护项目指导文件。”
- “把当前进展压缩成以后可读的背景。”
- “更新研究主线。”
- “把研究问题、路线和当前进度整理成一个总文件。”
- 项目已经有多轮讨论和分析结果，需要一个短文件串联起来。

`PROJECT_GUIDE.md` 与 `PROJECT_PLAN.md` 的区别：

- `PROJECT_GUIDE.md` 是研究背景和主线入口，用来帮助 agent 快速理解项目。
- `PROJECT_PLAN.md` 是操作记录、运行结果和复盘日志，不应每次默认读取。

推荐结构：

- `One-line summary`
- `Background`
- `Central question`
- `Working hypothesis / model`
- `Current story chain`
- `Result / figure skeleton`
- `Current progress`
- `Key evidence and caveats`
- `Open questions`
- `Next decisions`
- `Pointers`

设计意图：

这个 skill 是从旧专案总控中的“项目模型、story chain、preferred figures、evidence notes”泛化而来。它解决的问题是：不能什么背景都不读，但也不能每次都读取很长的项目计划。因此需要一个足够短、足够信息密集的项目指导文件，作为后续写论文、做图、分析整合和审稿模拟的共同入口。

参考文件：

```text
.codex/skills/project-guide-maintainer/references/project-guide-template.md
```

## 7. 证据与审稿风险

### 7.1 `claim-evidence-audit`

路径：

```text
.codex/skills/claim-evidence-audit/SKILL.md
```

用途：

在论文写作、结果段、摘要、讨论、图注、figure interpretation、审稿回复或投稿前检查中，审查 claim 是否有足够证据，是否 overclaim，是否映射到 figure/table/source data/caveat。

适合触发的情况：

- “这个说法是否成立？”
- “这段是否过度解释？”
- “这个图能支持这个结论吗？”
- “审稿人会不会质疑这里？”
- 论文结果、摘要、讨论、图注或 response letter 需要检查证据边界。

不适合触发的情况：

- 普通代码执行。
- 普通文件整理。
- 普通绘图实现。
- 环境安装。
- 只是在处理数据但没有判断科学 claim。

输出格式通常是：

| Claim | Evidence | Level | Risk | Recommended wording |
|---|---|---|---|---|

设计意图：

这是科研诚信防线，但不应该对所有任务泛化触发。它要求把论文或图表中的每个 claim 拆成可验证单元，再检查证据来源、等级、风险和推荐降级写法。

### 7.2 `reviewer-simulation`

路径：

```text
.codex/skills/reviewer-simulation/SKILL.md
```

用途：

模拟生物信息学论文审稿人，识别证据链、统计、复现、图表、方法、机制解释和期刊叙事风险。

适合触发的情况：

- “模拟审稿人。”
- “找硬伤。”
- “预测 major concerns。”
- “准备 rebuttal。”
- “判断哪些补分析优先。”

输出通常按严重程度排序：

- Critical：可能阻止论文成立。
- Major：需要补分析、重写或补充证据。
- Minor：表达、图注、方法细节或易读性问题。

设计意图：

帮助在投稿前主动发现风险，并区分“可以文字澄清”的问题和“必须新增分析”的问题。

### 7.3 `research-decision-review`

路径：

```text
.codex/skills/research-decision-review/SKILL.md
```

用途：

在已经理解用户需求和必要背景后，用于关键研究决策取舍，包括是否继续、是否转向、是否采用外部工具、是否重写已有方法、某个解释是否过度。

适合触发的情况：

- “这样做合理吗？”
- “要不要采用这个工具？”
- “是否值得继续？”
- “我是不是过度解释了？”
- “要不要自己重写代码？”
- 当前方案明显存在证据、复现、成本、审稿或叙事风险。

不适合触发的情况：

- 用户只是要求执行一个明确任务。
- 还没有读懂用户目标和材料。
- 风险很小，只需要普通执行或轻量提醒。

决策维度：

- Scientific value
- Evidence strength
- Feasibility
- Reproducibility
- Tool maturity
- Cost of ownership
- Reviewer risk

设计意图：

增强“建设性反对”，但不是默认反驳用户。它应在读懂需求后、发现确实存在高影响取舍或明显风险时触发。普通执行型任务不应机械进入 decision review。

参考文件：

```text
.codex/skills/research-decision-review/references/decision-rubric.md
```

## 8. 写作与语言

### 8.1 `chinese-scientific-polishing`

路径：

```text
.codex/skills/chinese-scientific-polishing/SKILL.md
```

用途：

中文科研文本润色、结构优化和可读性提升。只做中文层面的润色，不做英文翻译。

适合触发的情况：

- “中文润色。”
- “让这段更通顺。”
- “结果段更好读。”
- “优化结构。”
- “中文论文段落打磨。”

核心规则：

- 保护证据边界。
- 先判断文本属于摘要、引言、结果、讨论、方法、图注还是回复信。
- 不把正文润色成数据堆砌。
- 数据用于支撑关键句，不应淹没叙事。
- 润色后给出 `Tips`，指出还能删减、补证据或调整结构的地方。

章节功能：

- 摘要：短、清楚，只放核心问题、方法、主要发现和意义。
- 引言：背景、缺口、问题和研究目的，不提前堆结果。
- 结果：回答“观察到了什么”，每段围绕一个 claim，数据适量。
- 讨论：解释意义、边界、替代解释和未来方向。
- 方法：透明、可复现，避免文学化。
- 图注：说明数据、样本、统计、过滤和 caveat。

参考文件：

```text
.codex/skills/chinese-scientific-polishing/references/section-responsibilities.md
.codex/skills/chinese-scientific-polishing/references/polishing-checklist.md
```

### 8.2 `scientific-english-translation`

路径：

```text
.codex/skills/scientific-english-translation/SKILL.md
```

用途：

将中文科研文本翻译为英文，或将中文草稿转成 Nature/CNS-leaning 但证据边界安全的英文表达。

适合触发的情况：

- “翻译成英文。”
- “中文转英文。”
- “Nature 风格英文。”
- “英文论文表达。”

核心规则：

- 先保护科学 claim，再追求英文风格。
- 不把相关性写成因果。
- 不把候选机制写成已证明机制。
- 不发明数据、文献、样本数、统计结果或机制。
- 可给忠实英文版和更精炼版本。

输出通常包括：

- `English version`
- `Optional concise version`
- `Risk notes`
- `Terms preserved`

参考文件：

```text
.codex/skills/scientific-english-translation/references/translation-stance.md
```

### 8.3 `scientific-english-polishing`

路径：

```text
.codex/skills/scientific-english-polishing/SKILL.md
```

用途：

已有英文科研文本的润色、压缩、段落重构、Nature/CNS-leaning academic style 和学术语气检查。

适合触发的情况：

- 用户已经给了英文文本。
- 需要英文润色、压缩或更高水平期刊风格。
- 需要打磨 abstract、title、figure legend 或 response letter。

核心规则：

- 先确认 claim 的证据等级，再改英文。
- 不为了语言更强而把 association 写成 causation。
- 不把 exploratory、candidate、putative、suggestive 写成 demonstrated、established、required。
- 能压缩就压缩，但不能删除关键 caveat、样本范围、数据类型和统计限定。

参考文件：

```text
.codex/skills/scientific-english-polishing/references/style-guardrails.md
```

## 9. 图表与图注

### 9.1 `figure-caption`

路径：

```text
.codex/skills/figure-caption/SKILL.md
```

用途：

用于 figure title、panel title、legend、caption、figure-to-claim 审查和图注中的 source data/caveat 表达。

适合触发的情况：

- “写图题。”
- “写 caption。”
- “重排 panel。”
- “检查图注是否支持论文 claim。”

写图注前需要明确：

- Figure 的主 claim。
- 每个 panel 的角色。
- 输入数据、样本范围和过滤状态。
- 统计方法、n、重复或背景集合。
- source data 路径或需要生成的 source data。
- caveat 和 reviewer risk。

设计意图：

图注不是单纯描述图片，而是把 figure 放进证据链中，帮助读者理解数据来源、比较对象、统计和限制。

### 9.2 `publication-plotting`

路径：

```text
.codex/skills/publication-plotting/SKILL.md
```

用途：

用于 manuscript-ready figures、PPT 可读图、论文主图和补图的绘制、修改、审查和导出。

适合触发的情况：

- “画论文图。”
- “修改图。”
- “检查图是否有遮挡。”
- “导出 PNG 和 SVG。”
- “整理 figure source data。”

核心规则：

- 绘图前先定义 figure contract。
- 图表服务证据链，不做装饰性复杂化。
- 每个 panel 都要能追踪到 source data。
- 默认导出 PNG + SVG；投稿或最终图再加 PDF/TIFF。
- SVG/PDF 文字尽量保持可编辑。
- 字号统一且可读：论文多 panel 图通常 6.5-8 pt，PPT 展示图通常 12-18 pt。
- 优先低饱和、可区分、色盲友好的 CNS/Nature 风格配色。
- 图例不得遮挡数据。

QA 重点：

- 图中文字、点、线、图例、panel label 是否互相遮挡。
- PNG 与 SVG 是否视觉一致。
- source data 是否能重建主要 panel。
- caption 是否说明数据来源和过滤状态。
- PPT 场景下缩放后是否仍可读。

参考文件：

```text
.codex/skills/publication-plotting/references/figure-contract.md
.codex/skills/publication-plotting/references/visual-qa.md
```

## 10. 数据组织与 Source Data

### 10.1 `research-data-organization`

路径：

```text
.codex/skills/research-data-organization/SKILL.md
```

用途：

组织项目数据、表格、结果、图和常用文件路径，解决结果分散、最新文件不清、重要表格难找、投稿数据难汇总的问题。

适合触发的情况：

- “结果文件太散。”
- “找不到最新表格。”
- “一个结果生成多个文件夹。”
- “投稿时不知道哪个表要上传。”
- “帮我整理项目数据目录。”

推荐结构：

```text
results/
  priority_tables/
  priority_figures/
  source_data/
  latest_manifest.tsv
  archive/
```

核心规则：

- 数据要可追踪，也要容易读取。
- 原始数据保持只读。
- 已确认结论的关键表格和高频文件要有清晰入口。
- 重要文件可以通过 `latest`、`priority`、`manifest` 或一级目录索引暴露出来。
- 错误旧文件不需要永久保留在工作路径；可覆盖修正后的图表和派生表，但 manifest 必须指向当前有效版本。
- 不用深层目录隐藏关键论文表格。

参考文件：

```text
.codex/skills/research-data-organization/references/layout-and-manifest.md
```

### 10.2 `source-data-audit`

路径：

```text
.codex/skills/source-data-audit/SKILL.md
```

用途：

构建或审查 source-data inventory、numbers-to-lock、figure/table-to-source traceability、Data/Code Availability、FAIR-like metadata 和 repository/accession plan。

适合触发的情况：

- “整理 source data。”
- “锁定论文数字。”
- “检查图表数据来源。”
- “准备 Data/Code Availability。”
- “审查 FAIR 元数据。”
- “投稿前 source data 检查。”

推荐字段：

- `figure_or_table`
- `panel`
- `claim`
- `source_file`
- `data_state`
- `script`
- `environment`
- `key_numbers`
- `caveat`
- `status`
- `latest`
- `updated_at`

核心规则：

- 每个 figure/table 的数据来源必须清楚。
- 每个关键数字和关键文字结论都应追踪到脚本、输入、输出或文献。
- raw、filtered、projected、manual-reviewed 数据状态必须明确。
- Data/Code Availability 不承诺尚未准备好的数据。
- 错误修正或轻微修改后的派生图表/表格可以覆盖旧文件，但 inventory 必须指向当前有效文件。

参考文件：

```text
.codex/skills/source-data-audit/references/fair-manifest.md
.codex/skills/source-data-audit/references/repository-readiness.md
```

## 11. 代码与复现

### 11.1 `bioinfo-analysis-code`

路径：

```text
.codex/skills/bioinfo-analysis-code/SKILL.md
```

用途：

用于生物信息学分析脚本、表格整理、轻量统计、Jupyter/CLI 工作流、运行命令、环境记录、可重复性说明、代码整理和发表前代码优化。

适合触发的情况：

- “写脚本。”
- “整理 TSV/CSV。”
- “合并 metadata。”
- “做轻量统计。”
- “生成 summary table。”
- “调试分析流程。”
- “记录运行命令。”
- “发表前整理代码。”

核心规则：

- 原始数据不修改。
- 输出写入新的结果目录或用户指定路径。
- 脚本必须声明输入、输出、关键参数和运行环境。
- 不静默改变过滤阈值、样本集合、参考版本或工具版本。
- 探索阶段可以写轻量脚本，但仍要记录关键命令和输入输出。
- 收尾或投稿阶段要整理为可读、可复现、可提交代码，补充必要注释、参数说明和 README 片段。
- 注释解释非显然逻辑、输入输出和关键参数，不写无意义逐行注释。

复现等级：

- `exploratory`：探索阶段，可轻量但要记录关键命令。
- `stable`：结果稳定，有明确输入输出和脚本。
- `submission-ready`：投稿或公开代码阶段，需要 README、环境、参数、source data 和可再生成流程。

参考文件：

```text
.codex/skills/bioinfo-analysis-code/references/reproducibility-levels.md
```

## 12. 环境与外部工具

### 12.1 `environment-and-tool-adoption`

路径：

```text
.codex/skills/environment-and-tool-adoption/SKILL.md
```

用途：

用于安装缺失的 Python/R/命令行包，评估并采用 GitHub 工具、论文代码、官方 protocol 或成熟软件，避免重复造轮子。

适合触发的情况：

- 本地缺少 pandas、R 包、绘图包或生信软件。
- 需要采用 GitHub 工具或论文代码。
- 需要判断是否自己重写一个方法。
- 需要根据 protocol 安装依赖或复现别人流程。

核心规则：

- 优先使用成熟工具和已有论文代码，不重复造轮子。
- 安装前先检查当前环境、包管理器、项目约束和已有替代方案。
- 不直接运行不可信脚本；先审查来源、license、依赖和输入输出。
- 记录工具版本、安装命令、来源链接、license、适配改动和运行环境。
- 对探索阶段和发表整理阶段使用不同严格度。

安装流程：

1. 检查当前环境和已有包。
2. 判断安装方式：`mamba/conda`、`pip`、`R install.packages`、`BiocManager`、`brew`、源码或容器。
3. 优先选择可复现方式，例如环境文件、版本号或 lock file。
4. 安装后运行最小验证命令。
5. 记录安装命令和版本。

参考文件：

```text
.codex/skills/environment-and-tool-adoption/references/tool-adoption-rubric.md
```

## 13. 自检与 Skill 审计

### 13.1 `task-self-check`

路径：

```text
.codex/skills/task-self-check/SKILL.md
```

用途：

任何生物信息学研究任务交付前的轻量自检。

适合触发的情况：

- “检查一下。”
- “自检。”
- “交付前 QA。”
- “看看有没有问题。”
- 任务完成前需要统一质量门控。

快速检查项：

- Claim：关键结论是否有证据来源，证据等级是否合适。
- Writing：段落是否服务章节功能，是否过度堆数据，是否越界。
- Code：输入、输出、命令、环境、参数是否清楚。
- Figure：是否有遮挡，字号是否可读，PNG/SVG 是否一致，source data 是否可追踪。
- Data：关键表格和最新文件是否容易找到，manifest 是否指向当前有效版本。
- Tool：外部工具或包是否记录版本、来源、license 和适配改动。

设计意图：

这是交付前轻量质量门控，不应重新读取大量上下文。复杂投稿级审计再交给更专门的 skill。

参考文件：

```text
.codex/skills/task-self-check/references/self-check-rubric.md
```

### 13.2 `skill-quality-audit`

路径：

```text
.codex/skills/skill-quality-audit/SKILL.md
```

用途：

审查本地 Codex/Agent skill 的质量、触发描述、结构完整性、上下文占用、references 拆分、安全风险、科研诚信边界和可维护性。

适合触发的情况：

- “检查这个 skill。”
- “优化 skill。”
- “这个 skill 是否太长/会误触发？”
- “按 Anthropic/AIPOCH 思路审计 skill。”

Hard gates：

- `SKILL.md` 是否存在。
- frontmatter 是否有 `name` 和 `description`。
- `description` 是否清楚说明何时触发。
- 是否要求默认读取大量无关文件。
- 是否包含危险命令或直接执行不可信用户字符串的脚本。
- 是否可能诱导模型编造数据、文献、机制或过强 claim。

参考文件：

```text
.codex/skills/skill-quality-audit/references/skill-audit-rubric.md
```

## 14. 从旧专案抽取出的通用能力

旧专案中最值得泛化的部分不是具体研究事实，而是“项目模型”这一层能力：用少量文字保存背景、核心问题、story chain、证据等级、preferred figures 和当前进度。这个能力已经转化为通用 `project-guide-maintainer`，并以 `PROJECT_GUIDE.md` 作为轻量项目指导文件。

已泛化到通用体系的旧专案经验：

- 项目需要一个短主线文件，而不是每次读取很长的操作日志。
- 研究内容应该以 story chain / result skeleton / figure skeleton 串联。
- 每个主要结果应带 evidence level 和 caveat。
- 图表和论文结构应该围绕主线组织，而不是按分析脚本堆叠。
- 写作审查需要检查冗余表达、过强动词、术语一致性和 figure/number integrity。

不在本说明中展开旧专案专属 profile 或专属 skill。它们可以保留在本地用于旧项目，但不是通用体系的一部分。

## 15. 当前完成度

已完成：

- 根 `AGENTS.md` 已按 Anthropic skill 思路二次瘦身。
- 不再维护 `paper-writing` / `lab-analysis` 两个子 AGENT。
- 默认中文规则已经写入根 AGENT。
- 最小上下文读取规则已经写入根 AGENT。
- `PROJECT_GUIDE.md` 已定位为项目背景、主线、路线和当前进度的轻量入口。
- `PROJECT_PLAN.md` 已定位为记录/复盘对象，不默认读取。
- 证据等级已经写入根 AGENT 和 `claim-evidence-audit`。
- 建设性反对已经写入根 AGENT，并由 `research-decision-review` 扩展。
- 研究前期规划已经下沉为 `research-project-planner`。
- 用户原始想法短文档已经下沉为 `research-question-brief`。
- 项目指导文件维护已经下沉为 `project-guide-maintainer`。
- 中文润色、英文翻译、英文润色已经拆成 3 个 skills。
- 图表绘制和 QA 已下沉到 `publication-plotting`。
- 图注和 figure-to-claim 已下沉到 `figure-caption`。
- source data 和复现审计已下沉到 `source-data-audit`。
- 数据目录、latest、priority、manifest 逻辑已下沉到 `research-data-organization`。
- 代码和复现整理已下沉到 `bioinfo-analysis-code`。
- 包安装、外部工具采用、避免重复造轮子已下沉到 `environment-and-tool-adoption`。
- 交付前自检已下沉到 `task-self-check`。
- skill 质量审计已下沉到 `skill-quality-audit`。

## 16. 使用建议

### 16.1 开始一个新研究方向

推荐流程：

1. 用 `research-question-brief` 先把用户原始想法压缩成短方向文档。
2. 用 `research-project-planner` 设计 central question、gap、hypothesis、evidence package 和 technical route。
3. 用 `project-guide-maintainer` 建立或更新 `PROJECT_GUIDE.md`，作为后续任务的轻量背景入口。
4. 如果已有相关论文或工具，再用 `environment-and-tool-adoption` 判断是否采用成熟工具或论文代码。
5. 后续进入具体分析时再触发 `bioinfo-analysis-code`。

### 16.2 写论文或润色文本

推荐流程：

1. 中文文本先用 `chinese-scientific-polishing`。
2. 中文到英文用 `scientific-english-translation`。
3. 已有英文文本再用 `scientific-english-polishing`。
4. 如果是在结果、摘要、讨论、图注或 response 中担心 overclaim，用 `claim-evidence-audit`。
5. 投稿前用 `reviewer-simulation`。

### 16.3 做图和图注

推荐流程：

1. 用 `publication-plotting` 先定义 figure contract。
2. 绘制或修改图，并输出 PNG + SVG。
3. 用 `figure-caption` 写 figure title、panel title 和 caption。
4. 用 `source-data-audit` 检查 figure/table/source data 是否可追踪。
5. 交付前用 `task-self-check` 做轻量 QA。

### 16.4 整理数据和代码

推荐流程：

1. 用 `research-data-organization` 建立 priority tables、priority figures、latest manifest。
2. 用 `bioinfo-analysis-code` 整理脚本、输入、输出、命令、环境和复现等级。
3. 用 `source-data-audit` 准备 source-data inventory 和 numbers-to-lock。
4. 投稿或发布前，把代码提升到 `submission-ready` 级别。

### 16.5 遇到缺失包或现成工具

推荐流程：

1. 用 `environment-and-tool-adoption` 检查当前环境和已有替代方案。
2. 判断安装方式和版本记录方式。
3. 审查 GitHub 工具或论文代码的维护状态、license、文档和输入输出。
4. 决定直接使用、局部借鉴、重写最小实现或放弃。
5. 记录版本、来源、license、安装命令和适配改动。

## 17. 后续可人工确认的问题

建议用户重点检查以下问题：

- 根 `AGENTS.md` 是否已经足够短，是否还需要继续压缩。
- `research-project-planner` 的 project brief 是否符合实际科研启动习惯。
- `research-question-brief` 是否足够短，是否适合长期维护用户原始想法。
- `project-guide-maintainer` 生成的 `PROJECT_GUIDE.md` 是否能用最少内容保留足够背景、路线和当前进度。
- `claim-evidence-audit` 的触发边界是否已经足够具体，是否避免普通任务误触发。
- `research-decision-review` 是否只在真正存在高影响取舍或明显风险时触发。
- `chinese-scientific-polishing` 是否充分解决“正文不要堆太多数据”的问题。
- `publication-plotting` 的字号、配色、导出格式、遮挡检查是否符合实际图表偏好。
- `research-data-organization` 的 `priority_tables/priority_figures/latest_manifest` 是否符合实际文件管理习惯。
- `source-data-audit` 的字段是否足够满足投稿和回溯需求。
- `environment-and-tool-adoption` 是否需要加入更明确的安装权限边界或环境隔离规则。
- 是否需要把 high-impact figure reference 改造成真正通用的图表风格参考 skill。
- 是否需要为常见生信分析类型继续增加专项 skill，例如 RNA-seq、single-cell、ATAC-seq、variant calling、GWAS、phylogenomics、genome assembly QC 等。

## 18. 一句话总结

当前体系已经转为“通用生信研究 AGENT + 多个按需触发的科研 skills”。根 AGENT 负责短规则和路由，`PROJECT_GUIDE.md` 负责轻量项目背景和主线，skill 负责具体任务，project profile 负责项目特殊边界。这个结构能够减少上下文占用，也方便未来按模块继续扩展。
