---
name: reviewer-simulation
description: 用于模拟生物信息学论文审稿人，识别证据链、统计、复现、图表、方法、机制解释和期刊叙事风险，并生成 response strategy 或补分析优先级。
---

# Reviewer Simulation

## 核心问题

如何提前模拟审稿人会攻击的证据、统计、复现、图表和叙事风险？

## 使用场景

当用户要求“模拟审稿人”“找硬伤”“预测 major concerns”“准备 rebuttal”“判断哪些补分析优先”时使用本 skill。

## 审稿视角

至少从以下角度检查：

- 研究问题是否清楚，结果顺序是否支持主线。
- claim 是否由当前证据支撑。
- 样本、过滤、统计背景和多重比较是否清楚。
- 图表是否承载了关键结论。
- 方法和代码是否足以复现。
- 机制、功能或因果解释是否过度。
- 数据可用性、source data 和 accession 是否完整。
- 对 computational/omics 稿件，检查样本 universe、参考版本、坐标系统、ID mapping loss、随机种子、workflow pinning、database date 和 source-data traceability 是否足以复现。
- 若用户要求 Nature/CNS 风格预审，可从三类 reviewer emphasis 模拟：novelty/broad interest、technical rigor/reproducibility、clarity/reader fit；三者共享同一事实基础，不编造 reviewer 身份。
- partial manuscript 或只有摘要/图注时，必须写明 assessment boundary 和 missing materials，不能给出确定性 editorial decision。

## 输出格式

优先输出按严重度排序的审稿意见：

| Severity | Reviewer concern | Why it matters | Recommended response |
|---|---|---|---|

Severity 使用：

- **Critical**：可能阻止论文成立。
- **Major**：需要补分析、重写或补充证据。
- **Minor**：表达、图注、方法细节或易读性问题。

给出 response strategy 时，区分“可以文字澄清”和“需要新增分析”。

若审查 RNA-seq/single-cell、variant/genomics、pathway/network、clinical/translational 或 protein/docking 结果，优先把风险归入：输入定义不清、统计/过滤不透明、数据库证据越界、图表承载不足、复现入口缺失、claim 过强。
