---
name: research-decision-review
description: 审查已有生物信息学研究方案中的高影响取舍，比较继续/转向/停止、采用/改造/重写工具、claim 强度或论文路线等选项，并给出条件化建议、替代方案、敏感假设和最小去风险步骤；用于用户明确寻求“是否合理/值得/过度解释”的 decision support，不用于从零规划项目、为单个 claim 设计验证矩阵、普通执行或交付前 QA。
---

# Research Decision Review

## 核心问题

如何让一个已有高影响选择的推荐、代价和会改变结论的条件可见？

## 边界

- 本 Skill 审查已有选项，不从零生成完整 project charter；项目启动或重大重规划用 `research-project-planner`。
- 针对具体 claim 生成计算、外部数据、统计和实验验证矩阵时用 `validation-strategy-planner`；本 Skill 只指出哪类证据会改变决策。
- 交付前查错用 `task-self-check`，系统 claim 审计用 `claim-evidence-audit`，具体执行交给相应执行 Skill。
- 普通执行任务不默认触发“建设性反对”；只有任务核心是取舍，或继续执行存在明确高影响风险时才使用。
- 输出是 decision support。用户拥有研究方向、方法、解释、最终 claim 与 go/no-go 决定。

## 工作流程

1. 写清决策、候选选项、目标、硬约束、时间点和决策所有者；缺少会改变建议的信息时，只问必要问题。
2. 核验用户提供的证据与必要背景，区分 verified evidence、method judgment、value/cost judgment 和 speculation。
3. 至少比较当前方案与一个可信替代方案，评估 scientific value、evidence fit、feasibility、reproducibility、tool maturity、ownership cost 和 reviewer risk。
4. 识别关键假设、阈值和不可逆成本；说明它们变化时 recommendation 是否翻转。
5. 给出条件化 recommendation、反对理由、反方最强论点和最低成本的去风险步骤。
6. 明列用户仍需决定的事项；不得用技术默认替用户选择或把计划写成已验证结论。

## 特殊取舍

- 工具选择比较 source、license、维护状态、接口适配、可复现性和长期维护成本；成熟不等于适用。
- 重写只在外部实现不适配、不安全、不可复现、license 不允许、核心逻辑需要完全可控，或重写总成本更低时成立。
- continue/pivot/stop 必须关联可观察证据、剩余信息价值和机会成本，不用沉没成本支撑继续。
- claim 强度取舍必须区分 observation、association、functional support、mechanism 和 causality。

## 输出契约

- Decision and owner
- Conditional recommendation and confidence
- Evidence used and unknowns
- Option comparison with main trade-offs
- Key assumptions, flip conditions and reviewer risks
- Minimal de-risking step
- User decision required

需要 continue/pivot/stop、use/adapt/rewrite 或 reviewer-attack 的结构化判据时读取 `references/decision-rubric.md`；简单二选一不必加载。
