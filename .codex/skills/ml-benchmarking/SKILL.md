---
name: ml-benchmarking
description: 用于设计或审查生物信息学与 AI for biomedicine 的机器学习 benchmark，包括 task contract、可信 baseline、公平模型比较、应用匹配的 split、leakage/negative-control 检查、ablation、外部或 OOD 验证、复现契约和 model-card claim 边界；不用于已冻结方案的普通代码实现、非 ML 项目验证或仅凭指标撰写科学/临床结论。
---

# ML Benchmarking

## 核心问题

如何建立可复现、可公平比较、能暴露 leakage，且证据强度与 claim 相匹配的生物医学机器学习 benchmark？

## 能力与决策边界

- 本 Skill 负责 benchmark 的任务定义、比较设计、审查和实现契约，不把高指标自动解释为生物学机制、临床效用或药物发现成功。
- 用户决定 intended use、target、可接受 split、primary metric、模型取舍和最终 claim；Agent 提供备选、风险、敏感性分析和可验证实现边界。
- 已冻结 benchmark contract 后的 Dataset、runner、table、plot、test 或 workflow 实现，组合或转交 `bioinfo-analysis-code`。
- 不涉及 ML 比较的项目级计算、外部数据、统计或实验验证规划，改用 `validation-strategy-planner`。
- 论文段落、图注或审稿回复中的 claim-to-evidence 审查，改用 `claim-evidence-audit`。
- 不因用户要求“最先进模型”而跳过简单 baseline、数据审计或真实应用匹配的 split。

## 工作流程

1. 冻结 task contract：prediction unit、input、target/label source、prediction horizon、intended use、decision context 和 forbidden claims。
2. 建立数据与 provenance 表：source/version/license、纳排规则、样本关系、重复、pretraining overlap、batch/site/time、homology 或 scaffold 风险。
3. 选择模拟实际泛化对象的 split；按需使用 patient/family/group、gene/protein-family/homology、scaffold、site/batch、temporal 或 external-cohort split。
4. 在看 test 结果前固定 primary metric、secondary metrics、calibration/uncertainty、subgroup/error analysis 和成功判据。
5. 建立递进 baseline：trivial/null、简单规则或 classical model、可信公开基线；说明每个 baseline 排除了什么替代解释。
6. 固定公平比较：相同 eligible data、split/fold、preprocessing scope、tuning budget 和评估代码；用 paired comparison、confidence interval 或重复种子描述不确定性。
7. 审计 leakage：所有 fit/selection/tuning 仅用允许的数据；检查 duplicate/relatedness、homology/scaffold、label proxy、batch/site/time、pretraining contamination 和 test reuse。
8. 加入 negative controls、ablation 和 robustness：label/feature shuffle、null/decoy、modality/component removal、data-size curve、seed/parameter sensitivity 和 OOD challenge。
9. 将 external validation 与 model selection 隔离；外部 cohort、orthogonal assay 或 prospective test 不可反向参与调参。
10. 记录可复现契约：immutable input/version、split IDs、seed、environment、hardware-sensitive settings、命令、日志、metrics/source data 和 model artifact hash。
11. 形成 model card：intended use、unsupported use、训练/评估数据、结果与不确定性、failure modes、subgroup limits、external validity 和 unsupported claims。
12. 交付 benchmark 设计或审计；若进入实现，把冻结的 schema、split、禁止项、测试和 done definition 交给 `bioinfo-analysis-code`。

## 比较与 claim 守门

- “最好”只在预先声明、可比且有不确定性评估的候选集合内成立；跨论文数字不能默认直接比较。
- 单次 holdout、随机 split、内部交叉验证或单一 metric 不能单独证明稳健泛化。
- AUROC/AUPRC、RMSE、correlation、ranking 或生成质量指标不等同于校准、临床净获益、因果机制、结合亲和力、有效性或安全性。
- 测试集被反复查看、用于选模型或改 pipeline 后，不再是未触碰的最终验证集；必须记录污染并降级结论或补充新验证。
- External/OOD 结果缺失时，明确写 `not assessed` 或 `planned`，不得用内部指标替代。
- 所有 performance claim 绑定 dataset/version、unit、split、metric definition、uncertainty 和 validation context。

## 模式化输出

- `benchmark design`：task contract、数据风险、split、baseline、metrics、controls、comparison、validation、reproducibility 和 claim boundary。
- `benchmark audit`：按严重性列出 invalidating leakage、不可比项、复现缺口、可保留结果和最小修复。
- `comparison plan`：候选模型、统一预算与 folds、paired statistics、ablation、stop rule 和报告表结构。
- `implementation handoff`：冻结输入/输出 schema、split IDs、禁止读取 test 的步骤、验收测试、命令和 done definition。
- `claim guard`：指标可支持的最小结论、不能支持的结论、需要补充的验证和安全降级写法。

## 按需读取

设计 task/split 文件、leakage checklist、comparison table、复现记录或 model card 时，读取 `references/ml-benchmark-contract.md`；不要在不需要这些模板时加载它。

最终回复先给 benchmark 结论或设计，再给关键假设、精确 artifacts、验证边界、实现路由、剩余风险和需要用户决定的事项。不得自称完成最终科学或临床批准。
