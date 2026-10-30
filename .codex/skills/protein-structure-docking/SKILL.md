---
name: protein-structure-docking
description: 用于蛋白结构来源与模型 QA、受体/配体或互作伙伴输入锁定、protein-ligand/protein-protein docking 工作流选择、pose/界面 QC、突变体匹配比较及结构结果解释；适用于 PDB/AlphaFold/ColabFold/Boltz/Chai、HDOCK/ClusPro/HADDOCK、Vina/GNINA/DiffDock 类任务。不用于 ADMET/QSAR、campaign-level 虚拟筛选排序、靶点/药物优先级或临床用药判断。
---

# Protein Structure Docking

## 核心问题

如何在输入、结构来源、比较条件和对照可追踪的前提下生成或审查结构/docking 假设，同时不把模型分数升级为结合、功能、因果或临床结论？

## 能力与路由边界

- 本 Skill 负责结构模型、受体/配体/partner 制备、pocket/界面定义、单个或小批 docking、pose/界面 QC 和 matched comparison。
- campaign-level compound prioritization、ADMET/QSAR、target validation、repurposing 或多证据 GO/NO-GO 交给 `drug-discovery-admet-screening`；docking 只提供独立证据层。
- 普通 accession/sequence/compound ID 核验交给 `scientific-database-grounding`。
- 图形重绘交给 `publication-plotting`；实验结合、功能或临床结论需要独立数据和相应专项流程。
- 查看现有结果时直接读取已有 pose、界面图或分数并解释，不擅自重跑；只讨论可行性时不计算。明确要求试跑时执行授权的小规模尝试，不只给计划。

## 输入契约

快速探索先确认用户指定的输入文件可读、对象和目标 chain 无歧义、任务是蛋白–蛋白还是蛋白–小分子，以及现有工具能否处理该输入。需要 box、配体化学状态或关键辅因子的工具，仍须满足其必要前提；不为省事任意补选。查看已有结果不要求补齐所有数据库信息；未知项标明，不作依赖它的解释。

正式分析、matched comparison 或用户明确要求全面 QA 时，按用途锁定下列相关字段；不适用项标记 N/A：

1. Protein：accession、species、isoform、sequence、domain/motif、WT/mutant 差异和 numbering map。
2. Structure：PDB/mmCIF 或预测模型来源、chain/model、apo/holo、缺失残基、confidence、cofactor/metal/membrane context。
3. Ligand/partner：结构或序列标识、stereochemistry、protomer/tautomer、charge、salts 和共价/金属约束。
4. Target definition：known pocket、blind/cryptic site、PPI interface、restraint-defined、membrane/lipid、metal 或 covalent site。
5. Comparison policy：统一 receptor/ligand preparation、box/restraints、软件版本、参数、seed、replicate 和 scoring policy。
6. Compute/provenance：本地、服务器/GPU、容器或外部服务，以及版本、参数、输入 hash 和输出路径。

对象或必要 chain 映射不清时，问最关键的一项并暂停受影响计算；不影响当前观察的元数据缺口不阻塞探索，不解释依赖缺失映射的分数或残基差异。

## 工作流程

1. 按意图区分查看、试跑、针对性检查和正式分析；默认取能回答当前问题的最小深度，不向用户逐次询问模式选择。
2. 读取适用的项目规则和用户指定输入；原始结构、序列与 ligand 文件保持只读。
3. 分类任务：known-pocket self-dock、apo/cross-dock、blind/cryptic search、PPI/binder、metal/covalent 或 matched WT-mutant。
4. 已有适配工具时直接使用；只有需要选型或升级时读 `references/structure-docking-tool-matrix.md`。快速探索不强制先做完整工具比较和对照设计；正式比较须满足匹配协议。
5. 大批量或昂贵计算先跑小样本 pilot，检查日志、完成数、失败数、pose 合理性、运行时间和磁盘占用后再扩展。
6. 同步保存输入、派生输入、实际制备步骤、命令/版本、参数与 seed（含默认值或无法取得的项）、输出路径、基本 QC 和失败原因；探索也不事后补记。完整对照、重复计算、敏感性分析和批次 summary 按正式分析需求补做，不增加探索前置报告。
7. 按 `references/protein-docking-evidence-contract.md` 的深度要求检查；快速探索看 pose 是否可读、是否明显错位/严重穿插，只描述已观察到的接触或问题，未检查项不写成通过。
8. 只把通过基本 QC 的 pose、界面或分数作为候选假设；将虚拟筛选或 ADMET 需求明确 handoff，不自行合并成药物总分。
9. 先交图、现有结果或运行状态，用普通中文回答当前问题；例如“模型中这两个区域有接触，但还不能据此确认真实结合”。具体结论须来自实际产物，不机械套用示例。正式分析的完整证据和下一验证另行展开。

## 执行后端

- 需要查找或补全结构/序列时读取 `../capability_registry.json` 的 `CAP-STRUCT-001`，使用已安装 PDB/AlphaFold/UniProt 等后端；用户指定的本地输入足够时不强制重新查库。外部模型工具仅在任务适配且有相应授权时采用，大批量前先做 bounded pilot。
- registry 不授权安装、配额或上传结构。尤其不能把 protein-ligand DiffDock/NIM 当作 protein-protein docking 后端；不匹配时停止并回到方法选择。

## 解释硬边界

- Docking score 不是 `Kd`、`Ki`、`IC50`、结合证明、选择性或 efficacy。
- pLDDT、PAE、pTM、ipTM、ipSAE、DiffDock/Boltz/AF-like confidence 是模型或几何指标，不是互作或功能验证。
- 单个 pose、单次 seed、单一工具或 WT-mutant score delta 只能产生结构假设；不得推出功能改变或因果机制。
- 同源结构、结构相似或预测 pocket 不等于相同功能、真实结合位点或生理互作。
- 多工具一致和物理 QC 可以提高假设可信度，但不能代替结合、生化、细胞、动物或临床验证。
- 在正式分析记录中使用 Strong / Moderate / Exploratory / Speculative 标记解释等级；探索回复用“模型预测”等普通中文表达，不要求用户理解内部等级。
- 不从 docking/structure 输出推断患者获益、剂量、安全性或治疗建议。

## 模式化输出

以下完整字段用于正式分析或对应专项交付，快速探索不逐项铺陈；可追溯记录仍保留在项目约定位置。

- `structure/model QA`：结构来源、coverage/numbering/confidence、缺失上下文、适用与不适用用途。
- `docking plan`：locked inputs、task class、tool/rationale、controls、pilot、expected outputs、stop conditions。
- `bounded pilot/run`：实际命令或服务参数、输入/输出、成功/失败计数、资源使用和是否可扩展。
- `result interpretation`：pose/interface QC、rank/score 定义、replicate/control、证据等级、不可支持的 claims。
- `matched comparison`：严格匹配项、差异信号、敏感性、反例和独立验证需求。

## 按需读取

- 需要选择 structure/docking 方法、对照或升级路径时，读取 `references/structure-docking-tool-matrix.md`。
- 需要锁定输入字段、设计 batch summary、执行 pose/interface QC 或解释 score/confidence 时，读取 `references/protein-docking-evidence-contract.md`。

最终回复先给实际观察或结果文件，再用一句话说明最关键限制；没有运行或没有可用结果就直接说明。完整方法、参数与 QC 留在运行记录，不默认附长篇验证路线。
