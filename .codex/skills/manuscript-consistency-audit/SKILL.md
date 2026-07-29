---
name: manuscript-consistency-audit
description: 用于检查生物信息学稿件各位置之间的内部一致性，定位摘要、Results、Methods、图注、表格、补充材料中的数字、术语、样本集合、过滤标准、统计定义、figure/table 编号和 claim 表述冲突；不评定 claim 证据强度、不构建 source-data inventory、不做整套投稿 gate 或文字润色。
---

# Manuscript Consistency Audit

## 核心问题

如何基于明确权威来源发现并修复稿件不同位置之间的事实和定义冲突，而不猜测正确值？

## 能力边界

- 比较同一数字、术语、样本 universe、过滤/统计定义、figure/table 引用和 claim 在多个稿件位置的表达。
- 单个 claim 是否被数据支持，交给 `claim-evidence-audit`。
- figure/table 的 source file、script、metadata 或 deposition 缺失，交给 `source-data-audit`。
- 整套投稿包是否 ready，交给 `submission-readiness-audit`；语言风格和翻译交给相应 polishing/translation Skill。
- 预判 reviewer concerns 时，交给 `reviewer-simulation`；收到真实 comments 并需逐条改稿时，交给 `reviewer-response-builder`。

## 一致性合同

- 先声明稿件版本、比较范围和 authority hierarchy。
- 优先使用 verified source data、locked table、figure map、analysis config 或用户指定版本；没有 authority 时标记 `AUTHOR_INPUT_NEEDED`。
- 区分 `consistent`、`conflict`、`missing authority`、`scope-dependent` 与 `not assessed`。
- 将 reader-facing hygiene 作为独立状态检查：Results、Discussion 和 caption 不应暴露本机绝对路径、仓库目录、脚本或原始表格文件名、内部 flag/run ID/pipeline label、原始命令或未解决的作者/编辑批注；批注从读者正文移出时，尚未解决的科学问题必须原意保留为 author action。
- Methods 保留复现必需的软件、版本、参数、阈值和公开 accession；机器特异路径与内部运行标签留在 manifest、source-data inventory 或项目记录中。科学上必要的标识符不得删除，但首次面向读者出现时应定义。
- 不把“所有位置一致”误写成“科学上正确”；一致性不替代证据审查。
- 不自动改数字、样本或统计定义，不把一种分析口径静默覆盖另一种。
- 只提出解决冲突所需的最小修改，不重写无关段落或提升 claim 强度。

## 工作流程

1. 锁定 manuscript、supplement、figure/legend/table 的版本与审计范围。
2. 建立 authority hierarchy；缺少 number lock 时先生成候选表，不自行定值。
3. 抽取数字、denominator、n、术语、样本集合、过滤阈值、统计检验、软件/参考版本、图表编号和关键 claim；同时扫描 reader-facing 区域中的内部实现痕迹与未解决批注。
4. 按概念聚合所有 locations，与 authority 对照并记录差异类型。
5. 对 claim-strength 差异只标出位置和方向；需要科学判定时转交 `claim-evidence-audit`。
6. 给出 exact location、权威值、最小修复和需要作者决定的冲突；内部 provenance 与未解决批注应分别迁移到可追踪记录和 author-action list，而不是直接丢失。
7. 修改获授权时只改确认项；复查 cross-reference 和 number lock，不宣称未检查位置已一致。

## 输出合同

| Item | Location | Current text | Authority | Status | Fix |
|---|---|---|---|---|---|

报告 coverage、authority gaps、blocking conflicts、reader-facing hygiene conflicts、author actions、已修位置与未审材料。

## 按需读取

建立或更新 number/term authority 表时，读取 [number-lock-template.md](references/number-lock-template.md)。

最终回复先给阻断性冲突和 authority 缺口，再给修复清单、覆盖范围、验证边界和作者待确认项。
