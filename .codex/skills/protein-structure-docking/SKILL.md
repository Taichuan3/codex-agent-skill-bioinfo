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
- read-only 请求只给审计、解释或运行计划，不提交服务器任务、不改输入或生成结果。

## 输入契约

在选择工具或解释结果前锁定：

1. Protein：accession、species、isoform、sequence、domain/motif、WT/mutant 差异和 numbering map。
2. Structure：PDB/mmCIF 或预测模型来源、chain/model、apo/holo、缺失残基、confidence、cofactor/metal/membrane context。
3. Ligand/partner：结构或序列标识、stereochemistry、protomer/tautomer、charge、salts 和共价/金属约束。
4. Target definition：known pocket、blind/cryptic site、PPI interface、restraint-defined、membrane/lipid、metal 或 covalent site。
5. Comparison policy：统一 receptor/ligand preparation、box/restraints、软件版本、参数、seed、replicate 和 scoring policy。
6. Compute/provenance：本地、服务器/GPU、容器或外部服务，以及版本、参数、输入 hash 和输出路径。

输入或 residue/chain 映射不清时，先报告阻塞项，不解释分数差异。

## 工作流程

1. 锁定模式：`structure/model QA`、`docking plan`、`bounded pilot/run`、`result interpretation` 或 `matched comparison`。
2. 读取适用的项目规则和用户指定输入；原始结构、序列与 ligand 文件保持只读。
3. 分类任务：known-pocket self-dock、apo/cross-dock、blind/cryptic search、PPI/binder、metal/covalent 或 matched WT-mutant。
4. 按 `references/structure-docking-tool-matrix.md` 选择方法、对照和升级路径；说明为什么适配本任务及主要失败模式。
5. 大批量或昂贵计算先跑小样本 pilot，检查日志、完成数、失败数、pose 合理性、运行时间和磁盘占用后再扩展。
6. 保存原始输出；另生成可追踪 summary，记录 preparation、software/model version、parameters、seed/replicate、QC 和失败原因。
7. 按 `references/protein-docking-evidence-contract.md` 分离 input fact、model output、physical/QC assessment、biological evidence 和 interpretation。
8. 只把通过基本 QC 的 pose、界面或分数作为候选假设；将虚拟筛选或 ADMET 需求明确 handoff，不自行合并成药物总分。
9. 交付精确输入/输出、方法与参数、QC/对照、证据等级、caveat 和下一项正交验证。

## 执行后端

- 读取 `../../capability_registry.json` 的 `CAP-STRUCT-001`，先用已安装 PDB/AlphaFold/UniProt 等后端锁定输入；外部模型工具只在 task class 匹配并完成 bounded pilot 后采用。
- registry 不授权安装、配额或上传结构。尤其不能把 protein-ligand DiffDock/NIM 当作 protein-protein docking 后端；不匹配时停止并回到方法选择。

## 解释硬边界

- Docking score 不是 `Kd`、`Ki`、`IC50`、结合证明、选择性或 efficacy。
- pLDDT、PAE、pTM、ipTM、ipSAE、DiffDock/Boltz/AF-like confidence 是模型或几何指标，不是互作或功能验证。
- 单个 pose、单次 seed、单一工具或 WT-mutant score delta 只能产生结构假设；不得推出功能改变或因果机制。
- 同源结构、结构相似或预测 pocket 不等于相同功能、真实结合位点或生理互作。
- 多工具一致和物理 QC 可以提高假设可信度，但不能代替结合、生化、细胞、动物或临床验证。
- 使用 Strong / Moderate / Exploratory / Speculative 标记解释等级；没有正交实验支持的 computational docking 通常保持 Exploratory。
- 不从 docking/structure 输出推断患者获益、剂量、安全性或治疗建议。

## 模式化输出

- `structure/model QA`：结构来源、coverage/numbering/confidence、缺失上下文、适用与不适用用途。
- `docking plan`：locked inputs、task class、tool/rationale、controls、pilot、expected outputs、stop conditions。
- `bounded pilot/run`：实际命令或服务参数、输入/输出、成功/失败计数、资源使用和是否可扩展。
- `result interpretation`：pose/interface QC、rank/score 定义、replicate/control、证据等级、不可支持的 claims。
- `matched comparison`：严格匹配项、差异信号、敏感性、反例和独立验证需求。

## 按需读取

- 需要选择 structure/docking 方法、对照或升级路径时，读取 `references/structure-docking-tool-matrix.md`。
- 需要锁定输入字段、设计 batch summary、执行 pose/interface QC 或解释 score/confidence 时，读取 `references/protein-docking-evidence-contract.md`。

最终回复先给结构/docking 结论边界，再给精确文件、方法/参数、QC、失败项、未运行范围和下一验证。
