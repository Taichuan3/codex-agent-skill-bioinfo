---
name: protein-docking-drug-discovery
description: 用于蛋白结构、protein-ligand docking、protein-protein docking、binder/protein design、virtual screening、ADMET 和药物靶点探索的候选工作流规划、输入定义锁定、工具选择、结果解释和 caveat 控制。适用于用户提出蛋白对接、突变体比较、PIP3/小分子结合、binder 设计、靶点验证或药物筛选想法；不直接替代服务器/GPU 上的重型计算。
---

# Protein Docking and Drug Discovery

## 使用场景

当用户讨论或执行以下任务时使用：

- protein-ligand docking、小分子/脂质/代谢物结合位点分析。
- protein-protein docking、肽段/结构域互作、突变体结合差异。
- binder design、protein design、AlphaFold/Boltz/Chai/BindCraft/RFdiffusion 类工作流规划。
- virtual screening、ADMET、target validation、drug repurposing 或 chemoinformatics 初筛。
- 需要把本地 Mac QC、服务器/GPU 计算、报告图表和证据边界串起来。

不要用于：

- 纯序列数据库查询：先用 `scientific-database-grounding`。
- 普通数据整理或绘图：用 `bioinfo-analysis-code` 或 `publication-plotting`。
- 没有结构/药物/设计问题的普通生信分析。

## 输入定义 QA

任何 docking 或 design 解释前必须先锁定输入：

1. Protein sequence：来源、accession、isoform、长度、物种、是否用户自定义序列。
2. Structure：PDB/AlphaFold/预测模型来源，chain、residue numbering、缺失区、confidence。
3. Motif/domain：1-based residue coordinates，WT 与 mutant 的精确差异。
4. Ligand/compound：SMILES/InChI/SDF、protonation、tautomer、stereochemistry、charge、是否脂质或金属/辅因子。
5. Docking target：binding site 是已知 pocket、全局 blind docking、蛋白-蛋白界面还是膜/脂质相关位点。
6. Compute location：本地 QC、服务器/GPU、外部 web server 或容器；记录版本和参数。

如果以上定义不清，不解释 docking 分数为生物学结论。

## 工具选择原则

- 快速可行性：HDOCK、ClusPro、CB-Dock、AutoDock Vina、GNINA 等可作为 pilot，但必须标记为 exploratory。
- 结构预测/复合物：AlphaFold DB、ColabFold、Boltz、Chai、AlphaFold3-like services 或服务器工具要区分模型 confidence 和 binding evidence。
- Binder/protein design：BindCraft、RFdiffusion、ProteinMPNN 等需要 GPU/服务器，先做设计目标和约束定义，不在 Mac 上强跑。
- ADMET/chemoinformatics：RDKit、ChEMBL、ADMET tools、QSAR 预测必须记录 applicability domain 和 uncertainty。
- 重型计算优先服务器/GPU；Mac 负责输入 QA、轻量转换、结果 QC、表格、图和报告。

## 结果解释边界

- Docking score 不是 binding affinity 的直接证明。
- 单一 pose 不是稳定构象；需要重复、对照、物理合理性和可视化检查。
- 突变体差异需要同一工具、同一参数、同一输入定义下比较。
- ADMET 是筛选提示，不是临床安全结论。
- Protein design 结果需要过滤：pLDDT/PAE/interface confidence、clash、motif preservation、sequence liability、negative controls。

## 输出格式

- Task type
- Locked inputs
- Tool/workflow choice and rationale
- Commands or server submission plan
- Expected outputs
- QC checks
- Interpretation level: Strong / Moderate / Exploratory / Speculative
- Caveats and next validation

## 按需读取

需要选择 docking/design/ADMET 工具时读取 `references/docking-tool-decision-matrix.md`。
