---
name: submission-readiness-audit
description: 用于生物信息学论文投稿前、预投稿或合作者最终审阅前的整套 package readiness gate，综合检查主文、图表、方法、统计、source data、代码、Data/Code Availability、引用和补充材料并给出阻断项；不替代单项深审、模拟审稿、真实审稿回复、期刊格式排版或普通任务 QA。
---

# Submission Readiness Audit

## 核心问题

如何基于完整、可核验的稿件包识别投稿阻断项，并给出有条件的 readiness 建议而不代替作者作最终 go/no-go 决策？

## 能力边界

- 对已组装的 manuscript package 做跨组件 gate，并汇总专门审计结果。
- 深审 claim 强度、source-data traceability 或跨稿件一致性时，分别交给 `claim-evidence-audit`、`source-data-audit`、`manuscript-consistency-audit`。
- 生成假想 reviewer concerns 时，交给 `reviewer-simulation`；处理真实 comments 时，交给 `reviewer-response-builder`。
- 普通代码/文档交付前 QA 使用 `task-self-check`；journal-specific 格式、cover letter 或语言润色不属于本 Skill。
- 给出 `Ready`、`Conditionally ready` 或 `Not ready` 建议，但不声称最终科学批准或替用户投稿。

## Gate 合同

- 先锁定目标版本、计划稿件类型、目标期刊要求是否已提供，以及实际可审材料。
- 缺少主文、图表、supplement、source data、code/README 或 availability statement 时，限定结论，不以 partial package 给出无条件 `Ready`。
- 把 issue 分为 `Blocking`、`Required before submission`、`Recommended`、`Not assessed`。
- 验证证据链、内部一致性、方法/统计可复现性和 access route；不从文件存在推断内容正确。
- 不编造 repository status、accession、代码运行结果、伦理批准、author contribution 或期刊要求。
- 把最终 claim、期刊定位、额外实验与提交决定留给用户。

## 工作流程

1. 建立 package inventory：manuscript、figures/legends、tables、supplement、source data、code/environment、availability、citations 与必要声明。
2. 记录 coverage 和版本冲突；读取现有专项审计，不重复执行无必要的深审。
3. 检查 central question、main claims、figure logic、统计/样本、Methods、复现入口、availability、citation 与补充材料。
4. 将阻断问题绑定到具体证据、文件和完成标准；无法判断时写 `Not assessed`。
5. 区分可通过文字/metadata 修复的问题与需要新分析、验证、作者/期刊决定的问题。
6. 给出 readiness 建议、Top blocking fixes、依赖顺序、owner 和复核条件。
7. 修复后只复核受影响 gate；没有复核证据时不升级状态。

## 输出合同

| Area | Status | Blocking issue | Evidence | Required action | Priority |
|---|---|---|---|---|---|

最后给出 `Ready / Conditionally ready / Not ready`、Top blocking fixes、未审材料、复核条件和 suggested specialist handoff。

## 按需读取

执行全维度 gate、组织 reviewer attack list 或核对 blocking/important 项时，读取 [submission-checklist.md](references/submission-checklist.md)。

最终回复先给 readiness 建议和阻断项，再给 package coverage、证据、专项 handoff、验证边界及用户决策点。
