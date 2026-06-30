---
name: manuscript-consistency-audit
description: 用于检查科研稿件内部一致性，包括摘要、正文、结果标题、图注、方法、补充表、source data 和引用中的数字、术语、样本集合、过滤标准、figure/table 编号和 claim 表述是否冲突。
---

# Manuscript Consistency Audit

## 核心问题

如何发现稿件内部数字、术语、样本集合、图表编号和 claim 的冲突？

## 使用场景

当用户担心论文前后不一致、数字冲突、图号错、术语混乱、摘要和结果强度不一致、或投稿前需要 number lock 时使用本 skill。

## 核心原则

- 一致性检查不是润色；先找冲突和风险。
- 不自动改数字，除非有明确 source data 或用户指定权威版本。
- 同一概念只保留一个主术语，变体需要说明。
- 数字和样本集合以 source data / locked table 为准。

## 工作流程

1. 确定权威来源：source data、locked table、figure map、用户指定版本。
2. 抽取 manuscript 中的数字、术语、样本数、图表编号和关键 claim。
3. 对照权威来源标记一致、冲突、缺来源和需人工确认。
4. 给出最小修改建议，不重写无关段落。

## 输出格式

| Item | Location | Current text | Authority | Status | Fix |
|---|---|---|---|---|---|

需要 number lock 模板时读取 `references/number-lock-template.md`。
