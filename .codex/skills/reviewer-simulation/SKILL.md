---
name: reviewer-simulation
description: 用于模拟生物信息学论文审稿人，识别证据链、统计、复现、图表、方法、机制解释和期刊叙事风险，并生成 response strategy 或补分析优先级。
---

# Reviewer Simulation

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

## 输出格式

优先输出按严重度排序的审稿意见：

| Severity | Reviewer concern | Why it matters | Recommended response |
|---|---|---|---|

Severity 使用：

- **Critical**：可能阻止论文成立。
- **Major**：需要补分析、重写或补充证据。
- **Minor**：表达、图注、方法细节或易读性问题。

给出 response strategy 时，区分“可以文字澄清”和“需要新增分析”。
