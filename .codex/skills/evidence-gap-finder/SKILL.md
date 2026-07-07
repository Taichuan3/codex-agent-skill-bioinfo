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

## 用户批注草稿 / revision backlog 场景

当用户在草稿括号中标记“没有证据证明”“没有确切图像”“需要补图”“后续重构”“结尾可合并”等，并要求先汇总待办而不是立即修改时：

1. 不要直接按批注逐句改正文。
2. 先提取括号批注和口头反馈，合并成 revision backlog。
3. 按 `全局问题 / 各 Results 小节 / 图像补充 / Methods-Supplement 分层 / 术语一致性 / 推荐执行顺序` 组织。
4. 每个待办要绑定 claim、当前缺口、最小补分析或降级写法、可能输出物和优先级。
5. 明确哪些是 blocking gap，哪些是文字减法或 nice-to-have。

## 输出格式

| Claim | Current evidence | Gap | Risk | Minimal fix | Cost | Priority |
|---|---|---|---|---|---|---|

需要优先级规则时读取 `references/gap-priority-rubric.md`。
