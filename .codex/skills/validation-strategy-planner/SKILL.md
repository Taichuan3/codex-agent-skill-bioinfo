---
name: validation-strategy-planner
description: 为一个已明确的探索性生物信息学发现、候选机制、模型结论、富集结果或 reviewer challenge 设计 claim-linked 验证策略，比较计算复核、统计敏感性、独立数据、正交实验与降级表述，并给出 minimal/balanced/submission-strength 路线和停止条件；不用于从零规划项目、执行验证、审查整体研究取舍或交付前 QA。
---

# Validation Strategy Planner

## 核心问题

哪项验证真正检验当前 claim、排除关键替代解释，并能以合理成本改变证据等级？

## 边界

- 本 Skill 需要一个明确 claim、当前证据和预期升级目标；缺少 claim 时先澄清，不生成泛化“多做验证”清单。
- 从零设计整个项目路线用 `research-project-planner`；判断项目或方法是否值得继续用 `research-decision-review`。
- 执行计算或统计验证使用相应分析 Skill；完成后的交付门控用 `task-self-check`，claim 全面审计用 `claim-evidence-audit`。
- 验证不可行时给出证据安全的降级表述，不把额外关联分析冒充机制或因果验证。

## 工作流程

1. 将目标拆成 claim、当前证据等级、关键假设、主要替代解释和期望升级；标明数据与资源约束。
2. 为每项候选验证写出它检验什么、不能证明什么、成功/失败判据和对 claim 的影响。
3. 覆盖适用层级：计算复核、统计敏感性、独立数据、正交测量、扰动实验和必要的表述降级；不机械要求全部层级。
4. 优先低成本、高信息量、能排除强替代解释的验证，并避免数据泄漏、非独立重复、同源数据库循环支持和参数挑选。
5. 组合 `minimal`、`balanced`、`submission-strength` 三档路线，标明顺序、依赖、成本等级和 stop/escalate 条件。
6. 明确验证成功、混合或失败时允许的最高 claim 强度，以及仍不能排除的限制。

## 输出契约

- Claim、current level、target level、key alternative
- Validation matrix：option、what it tests、cannot prove、success criterion、cost、dependency、expected upgrade、caveat
- Minimal / balanced / submission-strength paths
- Stop/escalate criteria
- Claim language under success / mixed / failure outcomes
- User decisions and execution handoff

需要验证类型的适用边界、常见伪验证和可填写矩阵时读取 `references/validation-matrix.md`；只需单项敏感性建议时不必加载。
