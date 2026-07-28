---
name: claim-evidence-audit
description: 用于审查稿件、报告、图注或回复中的具体科学 claim 是否被数据、图表、统计、文献与 caveat 支持，包括把预测结构写成实验结构、把相关性写成因果等证据升级，并给出等级和安全改写；不负责 docking/模型方法解释、source-data inventory、跨稿件一致性、整套投稿 readiness、模拟审稿或真实审稿编排。
---

# Claim Evidence Audit

## 核心问题

如何判断一个具体科学 claim 被什么证据支持到什么强度，以及怎样在不升级证据的前提下表达？

## 能力边界

- 审查 claim 与 evidence 的语义匹配、因果/机制/泛化越界和安全降级写法。
- 图表缺少 source file、script、metadata 或 deposition route 时，交给 `source-data-audit` 建立可追溯记录。
- 摘要、Results、Methods、图注和表格彼此冲突时，交给 `manuscript-consistency-audit`。
- 判断整套稿件是否可进入投稿流程时，交给 `submission-readiness-audit`。
- 预判潜在审稿攻击时，交给 `reviewer-simulation`；处理真实 editor/reviewer comments 时，交给 `reviewer-response-builder`。
- 只做绘图、文献检索、引用身份核验、代码或文件整理时，分别使用对应专项 Skill。

## 证据合同

- 把 claim 拆成最小可验证单元；分别标注对象、方向、范围、比较、因果强度和适用情境。
- 只使用已提供或可核验的 project output、figure/table、统计、source data、方法与 citation；材料不足时明确缺口。
- 区分 `Strong`、`Moderate`、`Exploratory`、`Speculative`，并分开写 evidence、interpretation、limitation 与 speculation。
- 不把数据库注释、模型分数、enrichment、docking、ADMET/QSAR、短 MD、registered trial 或相关性升级为功能、机制、疗效、安全性或因果证明。
- 不把“存在 provenance 缺口”自动等同于“观察为假”；分别报告 traceability risk 与 scientific support。
- 不替用户作最终 claim 决策，也不编造补实验、样本、统计、引用或 manuscript location。

## 工作流程

1. 锁定审查范围、版本和权威证据入口；没有材料时先列缺失项。
2. 抽取 claim，拆分观察、解释、机制、因果和泛化部分。
3. 映射 figure/table/panel、统计、source data、script 或 citation，并记录不确定项。
4. 检查样本/队列、assay、species、tissue、cell type、区域、阈值、比较对象和验证独立性。
5. 评定证据等级与主要 reviewer risk；区分“需要补 traceability”和“需要补分析/验证”。
6. 为每条 claim 给出 `keep`、`downgrade`、`move_to_discussion`、`needs_source_data`、`needs_analysis` 或 `remove`。
7. 给出保持同一语言与证据强度的最小安全改写；正式英文只在用户要求时提供。
8. 汇报已审证据、未审材料、判定边界和需要用户确认的最终措辞。

## 输出合同

| Claim ID | Claim unit | Evidence | Level | Traceability | Risk | Action | Safe wording |
|---|---|---|---|---|---|---|---|

## 按需读取

- 审查 manuscript/report 的 claim-to-figure 映射、action taxonomy 或 reviewer attack points 时，读取 [claim-to-figure-audit.md](references/claim-to-figure-audit.md)。
- 审查 clinical/translational、variant、drug repurposing、target validation 或 ADMET/QSAR claim 时，读取 [translational-evidence-boundary.md](references/translational-evidence-boundary.md)。
- 审查 repeat-rich 或 mappability-sensitive 区域的 public-data/model concordance 时，读取 [repeat-rich-external-validation.md](references/repeat-rich-external-validation.md)。

最终回复先给高风险 claim 与安全措辞，再给证据映射、未覆盖材料、限制和需要用户决定的 claim。
