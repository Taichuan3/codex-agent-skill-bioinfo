---
name: reviewer-response-builder
description: 用于处理已提供的真实 editor decision、reviewer comments 或合作者逐条批注，将其无遗漏地拆成 comment-response-action-manuscript change 记录并起草有证据边界的回复；不模拟潜在审稿意见、不声称未完成改动已完成，也不替代 claim/source-data/consistency 专项核验。
---

# Reviewer Response Builder

## 核心问题

如何把真实审稿意见逐条变成可追踪、可执行、与实际改稿和证据一致的 response package？

## 能力边界

- 只处理用户提供的真实 decision letter、reviewer comments 或明确的合作者批注。
- 尚无真实 comments、需要预判攻击时，改用 `reviewer-simulation`。
- 对回复涉及的具体 claim、source data 或跨稿件冲突，分别调用 `claim-evidence-audit`、`source-data-audit`、`manuscript-consistency-audit` 核验后再写完成式表述。
- 整套 revised package 是否可重投，交给 `submission-readiness-audit`。
- 不代替作者决定新增实验、拒绝请求、承诺时间或最终 response language。

## 回复合同

- 先保留原始 comment ID、reviewer/editor 层级和原文范围，再拆成原子要求；不得合并后漏答。
- 区分 reviewer observation、request、rationale 与隐含验收标准。
- 为每条评论选择 `accept`、`partially accept`、`clarify`、`evidence-bound pushback` 或 `author decision needed`。
- 每条完成式回复必须绑定实际 action、结果、manuscript location 和可核验证据。
- 未完成分析、未知 line number/figure panel、缺 citation 或待作者确认的策略使用 `AUTHOR_INPUT_NEEDED` 或 future-tense placeholder。
- 不编造 reviewer intent、editor instruction、实验、分析、统计、位置或提交状态；不承诺超出证据和授权范围的工作。
- pushback 要回应核心科学问题并承认现有边界，不能用礼貌措辞掩盖证据缺口。

## 工作流程

1. 锁定 decision letter、review version、comment hierarchy 和 revision deadline（如已提供）。
2. 先抽取 editor instructions，再按原 ID 拆分 reviewer comments；建立 completeness count。
3. 分类为 clarification、text/figure revision、new analysis、new experiment、overclaim、statistics、reproducibility 或 data availability。
4. 对每条评论记录 decision、action、owner/dependency、证据需求、manuscript change、风险和完成状态。
5. 需要专项科学核验时先生成 handoff，不把计划写成已完成结果。
6. 起草 point-by-point response：感谢/承认问题、实际行动与结果、修改位置、仍有边界。
7. QA 原 comment 数与 response 数、交叉引用、完成时态、位置、证据、礼貌 pushback 和 unresolved placeholders。
8. 汇报可直接使用的回复、待作者决定项、待执行分析与 revised-package 复核入口。

## 输出合同

| Comment ID | Atomic request | Decision | Action/status | Evidence | Manuscript change | Response draft | Risk |
|---|---|---|---|---|---|---|---|

同时给出 comment coverage、`AUTHOR_INPUT_NEEDED` 清单、analysis dependencies 和 response-letter QA。

## 按需读取

需要 accept、partial accept 或 evidence-bound pushback 的英文句式时，读取 [response-language.md](references/response-language.md)；只借用结构，不把模板中的动作写成已完成事实。

最终回复先给 comment coverage 与阻断项，再给 response table/草稿、实际已完成与计划中动作、验证边界和作者决策点。
