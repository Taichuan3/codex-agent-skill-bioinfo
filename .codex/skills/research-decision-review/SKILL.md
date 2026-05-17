---
name: research-decision-review
description: 用于在已经理解用户需求和必要背景后，对生物信息学研究中的高影响决策进行建设性反对和取舍评估，包括分析方案、论文结构、外部工具采用、证据解释、是否继续/转向/停止、是否重写已有方法。适用于用户问“这样做合理吗”“要不要采用这个工具/方法”“是否值得继续”“我是不是过度解释了”“要不要自己重写代码”，或当前方案明显存在证据、复现、成本或审稿风险的场景；不用于普通执行型任务的默认反驳。
---

# Research Decision Review

## 使用场景

当任务的核心不是执行，而是判断方向、取舍、风险和替代方案时使用本 skill。必须先理解用户目标、已有材料和当前约束，再决定是否触发；不要在尚未读懂需求时因为“可能需要反对”而机械触发。

普通执行型任务默认不使用本 skill。只有当继续执行可能造成明显科学风险、复现风险、资源浪费、错误叙事或不必要重复造轮子时，才转入 decision review。

## 决策维度

- `Scientific value`：问题是否重要，能否改变理解或实践。
- `Evidence strength`：当前证据能否支撑 claim。
- `Feasibility`：时间、数据、技能、计算和验证是否可行。
- `Reproducibility`：方法、代码、数据和环境是否可追踪。
- `Tool maturity`：是否已有成熟工具、论文代码或官方 protocol。
- `Cost of ownership`：自己维护代码或流程的长期成本。
- `Reviewer risk`：审稿人最可能攻击哪里。

## 默认立场

- 能用成熟工具时，不优先重复造轮子。
- 成熟工具也必须审查来源、license、维护状态、输入输出和适配边界。
- 自己重写只在以下情况合理：外部工具不适配、不可复现、license 不合适、核心方法需要完全可控，或重写成本低于适配成本。
- 反对用户时必须给出替代方案。

## 输出格式

```text
Decision review
- Recommendation:
- Why:
- Main risks:
- Evidence needed:
- Alternative options:
- Minimal next step:
```

需要更细的取舍表时读取 `references/decision-rubric.md`。
