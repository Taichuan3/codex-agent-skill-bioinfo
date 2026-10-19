---
name: reviewer-simulation
description: 用于尚无真实审稿意见时对生物信息学稿件/摘要做 prospective reviewer red-team，默认三位独立只读审查者，生成证据关联的假想 concerns、可反驳性测试和补分析优先级；用户人数/快速模式优先。不处理真实 comments，不扮演具名专家或断言真实 editorial decision；非稿件审查仍归领域 Skill。
---

# Reviewer Simulation

## 核心问题

如何在不虚构审稿人或编辑决定的前提下，提前找出稿件最可能受到的高价值科学与方法攻击？

## 能力边界

- 在真实 peer review 之前生成 hypothetical concerns、严重度、依据、可回答方式和补分析优先级。
- 已提供真实 editor letter、reviewer comments 或 collaborator annotations 时，改用 `reviewer-response-builder`。
- 判断整套 package 是否 ready 时，改用 `submission-readiness-audit`。
- 只审查具体 claim、source-data traceability 或稿件内部冲突时，分别改用 `claim-evidence-audit`、`source-data-audit` 或 `manuscript-consistency-audit`。
- 不模拟具名审稿人，不声称预测实际决定，不把缺失材料当成已验证缺陷。

## 模拟合同

- 锁定稿件版本、目标期刊/读者（如已提供）、材料范围和 assessment boundary。
- 从 novelty/reader value、claim-evidence、study design/statistics、method/reproducibility、figure logic、alternative explanations 与 data/code availability 选择适用视角。
- 每条 concern 必须引用稿件位置、figure/table 或明确缺失材料；避免泛化的“需要更多验证”。
- 区分 `Critical`、`Major`、`Minor`，并区分文字澄清、重分析、外部验证、新实验与不可在本轮解决的定位问题。
- 对 computational/omics 稿件检查 sample universe、reference/coordinate、ID mapping loss、filtering、multiple testing、random seed、workflow/database version 和 source-data traceability。
- partial manuscript 只给条件性审查，不给确定性 editorial verdict。
- 不编造 reviewer identity、journal policy、实验结果、统计缺陷或 rebuttal 已完成状态。

## 工作流程

1. 明确审查交付物；默认按 `references/independent-review-protocol.md` 启动三位独立只读审查者，用户指定人数/快速模式优先。材料包仅包含原始材料、版本、位置、范围与标准，不预置主 Agent 的疑点或结论；各 reviewer 独立建立主张与证据地图。
2. 先列能推翻中心结论或破坏可复现性的攻击，再列叙事和可读性问题。
3. 为每条 concern 写明 evidence/location、why it matters、最小充分 response 和残余风险。
4. 检查替代解释、confounder、data leakage、baseline/sensitivity、independent validation 与 claim generalization。
5. 对每项 response 标记 `clarify`、`reanalyze`、`new validation`、`new experiment`、`downgrade` 或 `scope decision`。
6. 按 central-claim impact、可行动性和成本排序；把具体深审转交相应 Skill。
7. 冻结各 reviewer 意见后再综合，保留分歧；单列后置一致性检查，不反写独立报告。汇报材料边界与最可能改变优先级的未知因素，不将模拟意见写成真实审稿事实。

## 输出合同

| Severity | Hypothetical concern | Evidence/location | Why it matters | Response class | Priority |
|---|---|---|---|---|---|

最后给出 top attack chain、最小 rebuttal-enabling work、不能从现有材料判断的事项和专项 handoff。

最终回复明确说明这是 prospective simulation，不是实际 reviewer 意见或最终 editorial decision。

## 按需读取

- 明确要求评估/审查或需协调多个独立视角时，读取 `references/independent-review-protocol.md`。该协议只负责协作方式；非稿件任务仍由对应领域 Skill 主持，不改称模拟同行评审。
