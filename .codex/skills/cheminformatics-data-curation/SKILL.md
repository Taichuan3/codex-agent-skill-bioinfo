---
name: cheminformatics-data-curation
description: 整理 SMILES/SDF、compound registry 和 assay records：结构标准化、salt/stereo/tautomer/protomer 政策、单位与测量协调、lineage、QC/attrition 和 split-ready handoff。不负责候选排序、模型比较、单一数据库查询、docking 或临床建议。
---

# Cheminformatics Data Curation

## 核心问题

如何把来源异质的分子结构和 assay 记录转成可复查、可重跑、可用于建模的数据集，同时保留原始事实、转换理由、失败和不可比较项？

## 能力与路由边界

- 本 Skill 负责结构与测量记录的 dataset-level curation、lineage、QC、exclusion 和 split-ready handoff；用户确认 endpoint、化学实体政策、聚合政策及可接受的信息损失。
- 只核验单个 CID、InChIKey、ChEMBL ID 或化合物身份时，改用 `scientific-database-grounding`。
- campaign 设计、ADMET panel、候选排序和 stop/pivot 由 `drug-discovery-admet-screening` 负责；本 Skill 只提供带 provenance 的 curated dataset。
- scaffold split、baseline、公平模型比较和 leakage 审计由 `ml-benchmarking` 负责；本 Skill 输出 structure groups、measurement groups 和可复用 split keys。
- RDKit/CLI 的安装与版本选择交给 `environment-and-tool-adoption`；冻结规则后的代码实现组合 `bioinfo-analysis-code`。
- receptor/ligand preparation、pose 或 docking 解释交给 `protein-structure-docking`。

## 输入契约

在转换前锁定：

1. 决策用途：identity table、assay harmonization、QSAR dataset、screening library 或 audit。
2. 来源：数据库/文件、release 或访问日期、license/access、原始 ID 和 immutable input/hash。
3. 化学字段：SMILES/SDF/InChI、stereochemistry、charge、salt/mixture、isotope 和原始名称。
4. 测量字段：target/construct/species、assay type/format、endpoint、relation/operator、value、units、pH/temperature/time 等已知条件。
5. 政策：fragment parent、neutralization、tautomer/protomer、stereo-unknown、duplicate/replicate、censoring、unit conversion 和 exclusion。
6. 输出：curated table、raw-to-standardized map、exclusion/failure table、QC summary、data card 和 modeling handoff。

## 工作流程

1. 锁定模式：`structure curation`、`assay harmonization`、`dataset audit` 或 `modeling handoff`。
2. 保留原始文件与原始字段只读；先统计记录数、结构解析率、空值、重复 ID、结构冲突和 endpoint/unit 分布。
3. 在执行前写明结构政策；逐步记录 parse、fragment/salt、charge、aromaticity、stereo、tautomer/protomer 和 canonicalization 的 action、status、reason 与 software/version。
4. 为每条原始记录保留稳定 lineage；标准化结构不得覆盖 raw structure，也不得只以 canonical SMILES 充当全部 provenance。
5. 核验 assay context；不同 target/construct/species、endpoint、relation 或实验条件不在无依据时合并。
6. 单位转换保留原值、原单位、转换公式/常数和目标单位；`<`、`>`、`=` 等 censored relation 不静默变成精确值。
7. 识别 exact duplicate、structure duplicate、stereoisomer、tautomer/protomer、replicate 和 conflicting measurement；聚合前声明统计规则并保留 measurement-level 表。
8. 生成 structure family/scaffold、measurement group 和 source/batch keys，并标 assessed/unknown/not_applicable；空scaffold和未评估tautomer/protomer关系不得冒充有效分组。显式给出 split_ready 与未满足条件；assay_context_group 不包含化学身份，不能单独用于跨分子聚合。不宣称某 split 已验证模型泛化。
9. 报告每步 input/output/changed/failed/excluded counts、原因分布、抽样人工检查和不可逆信息损失。
10. 输出版本化 curated artifacts、数据卡和 handoff；明确 `not assessed`、`unknown`、`failed`、`excluded` 与 `not applicable`。

## 解释硬边界

- 标准化是分析政策，不是发现唯一“真实”化学实体；pH、assay 与作用机制可能需要不同 protomer/tautomer。
- 去盐、中和、选 parent 或忽略 stereochemistry 都可能改变身份和标签；不得无记录覆盖。
- ChEMBL/BindingDB/PubChem 的值不因 endpoint 名称相似就自动可比。
- PAINS、rule-of-five、structural alert、RDKit sanitization 或模型可解析性不等于可合成、有效、安全或可开发。
- 随机行级去重不等于 scaffold、series、target 或 temporal leakage 已解决。
- 只把通过已声明 QC 的数据交给下游；失败记录和 attrition 也是交付物。

## 模式化输出

- `structure curation`：policy、raw-to-standardized map、transformation events、failures、structure QC 和版本。
- `assay harmonization`：target/assay/endpoint/relation/unit context、转换、不可比较组、replicate/conflict 和 coverage。
- `dataset audit`：schema、lineage、duplicate/conflict、attrition、抽样复核和最小修复。
- `modeling handoff`：curated table、entity/group keys、label policy、exclusions、split risks、environment 和 caveat。

## 按需读取

设计 structure/measurement schema、标准化政策、QC/attrition 或 modeling handoff 时，读取 `references/chemical-curation-contract.md`。

最终回复先给可用数据范围与主要损失，再给精确输入输出、政策、软件版本、QC/attrition、不可比较项、下游 handoff 和需要用户确认的化学/assay 决策。
