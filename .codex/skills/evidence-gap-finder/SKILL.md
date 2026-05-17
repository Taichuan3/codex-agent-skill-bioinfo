---
name: evidence-gap-finder
description: 用于从已有结果、论文草稿、figure plan、claim-evidence map 或审稿风险中找出缺失证据、过弱 claim、未闭合 caveat 和最小补分析集合。适用于准备加强论文证据链或决定下一步补什么分析。
---

# Evidence Gap Finder

## 使用场景

当用户已经有结果或草稿，但不确定哪些证据缺失、哪些 claim 过强、下一步最值得补什么分析时使用本 skill。

## 核心原则

- 目标是找最小补强路径，不是无限扩展项目。
- 区分 blocking gap、important gap、nice-to-have gap。
- 每个 gap 必须对应 claim、figure、source data 或 reviewer risk。
- exploratory 结果优先用降级写法或验证策略处理。

## 工作流程

1. 抽取目标 claim 和已有 evidence。
2. 判断每个 claim 的证据等级。
3. 标记缺口类型：数据缺失、对照缺失、统计缺失、复现缺失、外部验证缺失、解释过度。
4. 为每个缺口给出最小补分析或降级写法。
5. 按影响和成本排序。

## 输出格式

| Claim | Current evidence | Gap | Risk | Minimal fix | Cost | Priority |
|---|---|---|---|---|---|---|

需要优先级规则时读取 `references/gap-priority-rubric.md`。
