---
name: claim-evidence-audit
description: 用于审查论文文本、结果解释、图注、审稿回复或投稿前材料中的生物信息学 claim 是否被 figure/table/source data/citation/caveat 充分支持，并给出证据等级、风险和安全降级写法。不用于普通代码执行、绘图实现、文件整理或环境安装。
---

# Claim Evidence Audit

## 核心问题

如何判断一个科学 claim 是否被当前 figure/table/source data/citation 支撑，并给出安全降级写法？

## 使用场景

当任务涉及论文文本、结果解释、图注、figure-to-claim、审稿回复、投稿前检查，或用户明确要求检查“这个说法是否成立”“是否 overclaim”“结果段是否安全”“图能否支持结论”“审稿人会不会质疑证据”时使用本 skill。

不要因为任务中出现了数据、图或结果就自动触发本 skill。普通脚本执行、文件整理、绘图实现和环境安装应优先使用对应执行 skill；只有需要判断科学 claim 与证据是否匹配时才使用本 skill。

## 不适合触发

- 只需要写脚本、跑命令、整理表格或修复代码时，不使用本 skill。
- 只需要画图或调整图形样式时，优先使用 `publication-plotting`。
- 只需要查找新文献时，优先使用 `literature-search-workflow`。
- 只需要验证引用格式或 DOI/PMID 时，优先使用 `citation-verifier`。


## 证据等级

- **Strong**：有当前项目直接输出，且有 table、figure、script、source data 或已发表论文支撑。
- **Moderate**：多个分析模块结果一致，或 prior publication 与当前分析共同支持。
- **Exploratory**：基于早期分析、有限参数检查、局部复核、manual review 未完成或统计背景仍需确认。
- **Speculative**：尚无直接验证的功能、机制或因果假说。

## 审查流程

1. 抽取每个 claim，拆成最小可验证单元。
2. 为每个 claim 找到对应 evidence、figure/table、source data、script 或 citation。
3. 若处于论文/报告/投稿阶段，建立或检查 claim-to-figure 映射：`claim_id`、figure panel、source data、script、statistical test、limitation、reviewer risk。
4. 判断证据等级和主要 caveat。
5. 标记过强动词、因果词、机制词、泛化范围和样本范围问题。
6. 给出推荐写法：保留、降级、移动到 Discussion、补分析后再写或删除。

临床、转化、数据库和药筛相关 claim 需要额外检查证据类型：数据库关联、预测分数、trial status、approved indication、case evidence、population context 和当前项目直接结果不能混写。

## 输出语言和用户文本处理

- 默认用中文输出审查、草稿和推荐写法；只有用户明确要求英文时才改用英文。
- 如果用户提供英文 claim、英文结论句或英文 figure text，不要自动把最终段落写成英文；应把英文视为“待审查/待转述的原始 claim”，并用中文科研表述重写。
- 路径、列名、数据库名、assay/track/output type、基因/mark/target 名称可以保留英文，但叙事、解释、caveat 和结论应保持中文。

## 输出格式

优先输出表格：

| Claim | Evidence | Level | Risk | Recommended wording |
|---|---|---|---|---|

如果材料不足，先列出缺失证据，不要凭记忆补全。

## 按需读取

需要审查 ClinVar/Open Targets/ClinicalTrials/OpenFDA/ChEMBL/ADMET/QSAR/repurposing 等临床或转化 claim 时，读取 `references/translational-evidence-boundary.md`。
需要审查 manuscript/report 的 claim-to-figure、source data、script/statistical-test traceability、reviewer attack points 或 `CLAIM_TABLE.md` 时，读取 `references/claim-to-figure-audit.md`。

## 用户报告/草稿语言偏好

当用户要求中文报告、中文草稿或中文结果段时，即使用户提供的核心结论是英文，也要把正文叙事写成中文科研表述；英文只保留必要术语、assay/track 名、列名、文件路径、figure/source-data 名称和可复用的英文备选句。不要因为输入 claim 是英文就把整段结果写成英文。若需要嵌入英文句子，应明确标为“英文备选写法/英文 caption 草稿”，并在中文主叙事之后提供。

## 用户报告/结果段改写偏好与常见坑

- 当用户用英文给出核心结论、claim 或 figure interpretation，但明确说“我要中文/依旧是中文”时，正文叙事必须用中文科研表述；英文只保留必要术语、数据库名、track/output type、列名、路径和引文式短语。不要因为输入 claim 是英文就把整个结果段写成英文。
- 对生物信息学项目报告/草稿改写，优先写成“结果叙事 + 证据路径 + claim boundary”，避免流水账式 stage log。若插入图像，必须同时记录 figure path、generating script、source data / plotted source data，以及图像能支持的最小安全结论。
- 用户更正图像目录或指定图片来源后，要主动替换前一版插图和 provenance，而不是追加造成混淆；重新核对所有新图路径存在，并确认旧的错误目录不再出现在相关小节。
- 对 model-vs-external-data concordance，不要轻易写成“准确率”。除非已有定义好的 accuracy metric，否则写成 spatial/profile concordance、proxy support 或 matched-track consistency，并明确哪些 sample/assay 最强、哪些只是 weak/mixed support。
- If a Results paragraph introduces an auxiliary caveat analysis (e.g. synthetic-read mappability, assay-bias sensitivity, proxy-context coverage) but the main text lacks a figure, source-data citation, and clear connection to the primary claim, recommend either adding explicit support or moving/removing it from the main Results narrative. Do not let unsupported or weakly supported caveats become a closing “safe conclusion” that distracts from the actual supported result.

## 特殊场景：mappability-sensitive 区域的 public-data 外部验证

当审查公共数据对模型预测或候选位点的外部验证，尤其是 repeat-rich / mappability-sensitive 区域时，读取 `references/repeat-rich-external-validation.md`。必须区分模型预测、官方 processed target 与项目重处理信号，检查数据来源、metadata 冲突、assembly、strict/relaxed mapping、MAPQ、matched input/control、mappability sensitivity 和 source-data provenance。

Mappability / synthetic-read sensitivity 通常是解释边界或技术 caveat，不应自动升级为 Results 主结论。任何“无信号”结论必须绑定被检查的 signal object、threshold 和 resolution。只有当正文有对应图表、图注、source data 路径和明确叙事需要时，才把它作为 main result 展示；否则优先放在 Methods、supplement 或内部 caveat notes。
