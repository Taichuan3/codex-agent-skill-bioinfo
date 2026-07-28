---
name: research-discovery-orchestration
description: 用于把开放科研问题编排为可审计的人机协同闭环：冻结问题，串联文献/数据库证据、结构化假设、assay或候选优先级、人类决策门、实验/计算分析、多轨迹分歧综合、claim验证与下一轮反馈；适用于用户明确要求 literature-to-hypothesis-to-experiment 或 lab-in-the-loop 全流程。单纯项目规划、文献检索、候选排序、固定分析、claim审计或项目状态维护分别使用现有专项 Skill。
---

# Research Discovery Orchestration

## 核心问题

如何把已有专项能力串成可停止、可复核、有人类决策门的科研发现循环，并证明编排减少了返工，而不是增加一层包装？

## 所有权与路由

- 本 Skill 只拥有跨阶段编排、stage transition、共享 artifact 契约、人类决策门和实验结果到下一轮假设的 handoff；不拥有具体领域方法或最终科研判断。
- 只需澄清问题或从零规划项目时，分别使用 `research-question-brief` 或 `research-project-planner`。
- 文献集合、数据库实体、药物候选、分析实现、验证矩阵和 claim 审查分别交给 `literature-search-workflow`、`scientific-database-grounding`、`drug-discovery-admet-screening`、相应领域 Skill/`bioinfo-analysis-code`、`validation-strategy-planner` 和 `claim-evidence-audit`。
- 已有高影响方案取舍用 `research-decision-review`；项目状态、GUIDE 或目录导航不由本 Skill 维护。
- 只有任务明确跨越至少三个相邻阶段，且需要闭环反馈或跨 Agent 交接时才使用本 Skill；不要因“科研”“多 Agent”关键词单独触发。

## 权限与证据边界

- 用户确认研究问题、方法/assay、候选、实验执行、关键分析定义、最终 claim 和 continue/pivot/stop。
- 未获授权不得调用付费平台、上传私有数据、执行湿实验、改变样本/阈值/过滤/参考版本或自动进入下一轮。
- 文献综合、模型输出、数据库注释、排序和多轨迹一致性只能生成优先级或假设，不能单独证明功能、机制、疗效、安全或因果。
- 不要求或保存隐藏 chain-of-thought；保存简短 rationale、证据指针、替代解释、决策和不确定性。
- 原始数据只读；每次分析声明输入、环境、参数、seed、统计定义、产物和偏离。

## 闭环工作流

1. 锁定模式：`plan-only`、`dry-run`、`evidence-backed cycle` 或 `post-experiment iteration`；声明当前阶段、允许动作和停止点。
2. 冻结 cycle contract：研究问题、决策所有者、约束、成功/失败判据、允许的证据来源、预算和本轮最大范围。
3. 建立 evidence map：先做宽覆盖，再对会改变决策的候选做深核验；保留检索式、日期、纳排、来源和未核验全文。
4. 生成 hypothesis cards：每条包含机制、现有支持、可证伪预测、主要替代解释、可区分的 assay/analysis、可行性和证据等级。
5. 先按预声明维度筛查 identity、证据相关性、可测试性、技术风险、信息增益、成本与可行性，并显式保留缺失/冲突，再决定是否需要两两比较；不得让单一综合分替代维度证据。
6. 在进入实验、昂贵计算或正式候选选择前设置 human gate，输出保留/合并/拒绝及理由；未确认时停止在 decision package。
7. 执行交给专项 Skill/Agent；先冻结分析契约和验收条件。只有合理分析选择可能改变结论时才启用独立多轨迹。
8. 综合轨迹时比较输入、方法选择、过滤、统计、结果和 claim；保留 disagreement 与 failure，不以多数票掩盖系统偏差或相关轨迹。
9. 将结果映射回 hypothesis cards，区分 supported、weakened、refuted、unresolved 和 new hypothesis；用 claim/validation 守门决定允许表述。
10. 由用户选择 `continue`、`pivot`、`stop` 或 `repeat with changed assumption`；新一轮必须引用上一轮 manifest 和明确改变项。

## 交付契约

至少交付 cycle manifest、evidence map、hypothesis cards、候选/assay decision package、human-gate record、分析 handoff、trajectory comparison（若适用）、claim/validation map、feedback ledger 和 next-decision。cycle manifest 只作索引；每类事实指定一个 canonical owner，其他 artifact 只引用或生成派生视图。所有阶段使用稳定 `cycle_id`、`stage_id` 与 artifact 指针，不复制长内容。

## 停止与效率门

- 问题、证据入口、决策所有者、实验权限或分析输入不足时，停止并给最小补充项。
- 候选排序对顺序、seed、judge 或 rubric 不稳定时，不输出唯一赢家；报告层级、并列或需人工复核。
- 多轨迹共享同一错误输入、不可追踪或无法重建时，不把一致性当独立证据。
- 编排增加重复报告、上下文、tool calls 或 handoff，且没有提高完整性、可追溯性或决策速度时，回退到最小专项 Skill 组合。

## 按需读取

- 需要定义 manifest、hypothesis card、decision package、analysis handoff 或 feedback ledger 时，读取 `references/discovery-artifact-contract.md`。
- 需要两两排序、稳定性检查、多轨迹或共识/分歧综合时，读取 `references/ranking-and-consensus-contract.md`。
- 需要比较本 Skill 与原流程的效率、质量和回滚门槛时，读取 `references/pilot-evaluation-rubric.md`。

最终回复先给当前 cycle/stage、完成的 decision package 和人类待决项，再给 artifacts、验证、分歧、证据边界、效率观察和 stop/pivot/continue 条件。
