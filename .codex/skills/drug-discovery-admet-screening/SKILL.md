---
name: drug-discovery-admet-screening
description: 用于早期药物发现的 target-evidence 分层、compound/repurposing 候选筛选、bioactivity grounding、virtual-screening campaign 设计、QSAR/ADMET endpoint 评估、候选优先级与 stop/pivot 规则；适用于 ChEMBL/Open Targets/BindingDB/PubChem、descriptor/ML 模型、结构警示和多证据候选表。不用于具体 docking pose/界面解释、单个结构模型 QA、个人用药或临床治疗建议。
---

# Drug Discovery and ADMET Screening

## 核心问题

如何把 target、compound、assay、QSAR/ADMET 和 screening evidence 组织成可审计的早期发现决策，同时不把数据库关联或预测分数升级为因果、疗效、安全或临床结论？

## 能力与路由边界

- 本 Skill 提供 campaign-level target/compound 分层、bioactivity/repurposing evidence、QSAR/ADMET 模型适用性、筛选候选表和条件化 stop/pivot 建议；用户确认排序规则、下一实验和最终 go/no-go。
- 具体 protein structure、pocket/box、pose、interface、docking preparation 或 score 解释交给 `protein-structure-docking`；本 Skill 只接收带 provenance/QC 的 docking evidence summary。
- 纯 accession、chemical identity、database ID 或单一记录核验交给 `scientific-database-grounding`。
- benchmark 的 split、leakage、baseline 和模型比较需要时组合 `ml-benchmarking`；个人用药和临床治疗决策不在本 Skill 范围。
- read-only 请求只报告 evidence map、候选 schema 或计划，不调用付费服务、不提交筛选任务、不改化合物集合。

## 工作流程

1. 锁定模式：`target evidence map`、`bioactivity/repurposing review`、`screen design`、`QSAR/ADMET assessment` 或 `candidate prioritization`。
2. 定义 decision question：target、disease/biological context、compound space、endpoint、assay relevance、可接受风险和下游实验。
3. Ground identities and provenance：核验 target/compound、数据库版本/访问日期、assay/organism/construct、measurement type、units 和 relation/operator。
4. 标准化 compound space：处理 salts、mixtures、duplicates、stereochemistry、tautomer/protomer、charge、structure validity 和 assay-compatible units；保留 raw-to-standardized mapping。
5. 按 `references/drug-screening-decision-matrix.md` 选择证据层和方法；不得用单一综合分替代各维度证据。
6. 对 QSAR/ADMET 记录 endpoint definition、dataset provenance、split、baseline、applicability domain、calibration/uncertainty、missingness 和 structural alerts；外部验证缺失时明确限制。
7. 分开记录 target association、causal support、expression/context、measured bioactivity、docking/pose、QSAR/ADMET、chemical feasibility、literature 和 clinical/regulatory context。
8. 建立候选表并做 dimension-level ranking；报告 conflicting evidence、coverage、sensitivity 和排名规则，不把缺失值默认为 pass。
9. 定义 stop/pivot 和 next-validation criteria；交付精确输入/输出、版本、过滤规则、候选变化、证据等级和未解决风险。

## 解释硬边界

- Open Targets、GWAS/eQTL/pQTL、pathway、knowledge graph 或文献关联不是靶点因果验证；说明证据设计、共定位/扰动支持和替代解释。
- ChEMBL、BindingDB、PubChem 等活性值依赖 assay、construct、species、endpoint、operator 和 units；不同测定不可无依据合并。
- QSAR/ADMET 预测、Lipinski/Veber/QED、PAINS 或 structural alerts 是筛选线索，不是药效、安全性、毒性缺失或临床可用性证明。
- Docking rank/pose 只是独立 exploratory layer；不得用 docking score 代替 affinity，也不得用 ADMET pass 代替 efficacy。
- Repurposing、omics reversal、文本挖掘或 clinical-trial presence 只能支持候选背景，不能证明机制、疗效或适应证。
- 使用 Strong / Moderate / Exploratory / Speculative 标记证据等级；未经外部或实验验证的 computational screen 通常保持 Exploratory。
- 不从预测或数据库结果提供患者级用药、剂量、停药或风险建议。

## 模式化输出

- `target evidence map`：evidence dimensions、source/version、support/conflict、causal boundary、missing validation。
- `bioactivity/repurposing review`：identity/assay normalization、measured evidence、context mismatch、candidate status。
- `screen design`：decision question、compound space、filters/models、controls/baselines、pilot、artifacts、stop criteria。
- `QSAR/ADMET assessment`：endpoint/model/data/split、applicability/calibration、prediction coverage、alerts、unsupported claims。
- `candidate prioritization`：dimension-level table、ranking rule、sensitivity/conflicts、evidence level、next validation。

## 按需读取

- 需要选择 target validation、bioactivity、virtual screening、QSAR/ADMET、repurposing 或 molecule-generation 路径时，读取 `references/drug-screening-decision-matrix.md`。
- 具体 docking pose、结构制备或界面 QC 不读取本 reference，直接转交 `protein-structure-docking`。

最终回复先给候选分层、条件化建议及证据边界，再给精确文件、数据/模型版本、过滤和排序规则、验证范围、失败项，以及需要用户决定的下一实验或 go/no-go。
