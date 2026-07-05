---
name: submission-readiness-audit
description: 用于生物信息学论文投稿前或大版本收尾前的综合预检，检查主文、图表、方法、source data、代码、数据可用性、引用、补充材料和审稿风险是否达到可投稿状态。不用于普通任务交付前轻量自检。
---

# Submission Readiness Audit

## 使用场景

当用户准备投稿、预投稿、发给合作者做最终审阅、或完成大版本论文收尾时使用本 skill。普通交付前 QA 使用 `task-self-check`。

## 核心原则

- 投稿前检查必须跨主文、图表、方法、source data、代码和引用。
- 先找阻断问题，再找美化问题。
- 所有 main claim 必须能映射到 figure/table/source data/citation。
- 不把“文字看起来顺”当作可投稿。

## 审计维度

1. 论文结构：题目、摘要、引言、结果、讨论、方法是否各司其职。
2. 证据链：claim-evidence-figure-caveat 是否闭合。
3. 图表：panel 顺序、图注、统计、n、source data、可读性。
4. 数字一致性：摘要、结果、图注、方法、表格是否冲突。
5. 方法与复现：数据来源、软件版本、参数、环境、代码路径。
6. 数据可用性：repository、accession、source data、supplementary tables。
7. 引用：关键背景、方法、比较对象和 claim 是否有合适引用。
8. 审稿风险：过度解释、机制不足、统计不足、外部验证不足。

## 输出格式

| Area | Status | Blocking issue | Evidence | Required action | Priority |
|---|---|---|---|---|---|

最后给出：

- `Go / Conditional go / Not ready`
- `Top 5 blocking fixes`
- `Nice-to-have fixes`
- `Suggested next skill`

需要完整 checklist 时读取 `references/submission-checklist.md`。
