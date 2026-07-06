---
name: validation-strategy-planner
description: 用于为探索性生物信息学结果、候选机制、模型结论、富集结果或审稿风险设计验证策略，区分计算验证、外部数据验证、统计敏感性分析、实验验证和降级写法。
---

# Validation Strategy Planner

## 使用场景

当用户有 exploratory 发现、候选机制、模型结果、富集结果或 reviewer risk，需要判断如何验证、是否值得验证、或无法验证时如何安全表述时使用本 skill。

## 核心原则

- 验证策略要服务具体 claim。
- 不把“再跑一个分析”自动等同于验证。
- 优先设计低成本、高信息量、能排除替代解释的检查。
- 明确哪些验证能升级 claim，哪些只能支持探索性观察。

## 验证类型

- 计算复核：参数敏感性、负对照、shuffle/null、交叉方法、重复运行。
- 外部数据：独立 cohort、公开数据库、orthogonal assay、文献对照。
- 统计验证：背景集、multiple testing、effect size、confidence interval、power。
- 实验验证：qPCR、reporter、CRISPR、perturbation、wet-lab assay。
- 表述降级：当验证不可行时，改写为 observation、candidate、hypothesis。

## 输出格式

| Claim | Current level | Validation option | What it tests | Cost | Expected upgrade | Caveat |
|---|---|---|---|---|---|---|

最后给出 recommended path：`minimal`、`balanced`、`submission-strength` 三档。

需要验证矩阵时读取 `references/validation-matrix.md`。
