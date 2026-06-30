---
name: reviewer-response-builder
description: 用于处理真实审稿意见、返修信、editor decision 或合作者批注，将评论拆解为 response table、行动计划、补分析优先级、正文修改点和礼貌但有边界的回复草稿。不用于模拟潜在审稿人风险；模拟风险使用 reviewer-simulation。
---

# Reviewer Response Builder

## 核心问题

如何把真实审稿意见拆成行动计划、补分析优先级、正文修改点和礼貌但有边界的回复？

## 使用场景

当用户提供真实审稿意见、editor letter、返修要求或合作者逐条批注，并希望生成回复策略、response letter 或改稿计划时使用本 skill。

## 核心原则

- 先分类评论，再写回复。
- 每条回复都要对应行动、证据或边界说明。
- 不承诺无法完成的实验或分析。
- 对合理批评正面回应；对不成立要求礼貌解释。
- 与 `reviewer-simulation` 区分：本 skill 处理真实 comments。

## 工作流程

1. 拆分 comments：editor、reviewer、major、minor、technical、writing。
2. 标记评论类型：clarification、new analysis、new experiment、text revision、figure revision、overclaim、data availability。
3. 判断行动：accept、partially accept、clarify、push back、defer。
4. 生成补分析优先级和 manuscript 修改点。
5. 起草 response：感谢、行动、结果、文稿位置、边界。

## 输出格式

| Comment | Type | Decision | Action | Manuscript change | Response draft | Risk |
|---|---|---|---|---|---|---|

需要回复语气模板时读取 `references/response-language.md`。
