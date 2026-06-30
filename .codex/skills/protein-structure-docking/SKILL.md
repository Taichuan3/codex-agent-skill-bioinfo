---
name: protein-structure-docking
description: 用于蛋白结构与 docking 任务的输入定义锁定、结构来源选择、protein-ligand 或 protein-protein docking 工具选择、运行计划、结果 QC 和证据边界控制。适用于突变体比较、肽段/结构域互作、小分子/脂质结合位点、HDOCK/ClusPro/Vina/GNINA/Boltz/Chai/AlphaFold 类结构预测或对接解释；不负责 ADMET、虚拟筛选或药物靶点优先级评分。
---

# Protein Structure Docking

## 核心问题

如何在输入定义清楚、结构来源可追踪、工具选择合理的前提下，规划或解释蛋白结构与 docking 结果，而不把 docking score 误写成结合或功能证明？

## 使用场景

当用户讨论或执行以下任务时使用：

- protein-ligand docking、小分子/脂质/代谢物结合位点分析。
- protein-protein docking、肽段/结构域互作、突变体结合差异。
- AlphaFold DB、ColabFold、Boltz、Chai、AlphaFold3-like services、HDOCK、ClusPro、AutoDock Vina、GNINA 等结构/对接工具选择。
- 需要把本地 Mac 输入 QA、服务器/GPU 计算、结果 QC、图表和证据边界串起来。

不要用于：

- 药物筛选、ADMET、target validation 或 repurposing：用 `drug-discovery-admet-screening`。
- 纯序列/数据库查询：先用 `scientific-database-grounding`。
- 普通数据整理或绘图：用 `bioinfo-analysis-code` 或 `publication-plotting`。

## 输入定义 QA

任何 docking 解释前必须锁定：

1. Protein sequence：来源、accession、isoform、长度、物种、是否用户自定义序列。
2. Structure：PDB/AlphaFold/预测模型来源，chain、residue numbering、缺失区、confidence。
3. Motif/domain：1-based residue coordinates，WT 与 mutant 的精确差异。
4. Ligand/partner：SMILES/InChI/SDF 或 partner chain/sequence；记录 protonation、tautomer、stereochemistry、charge、cofactor/metal/lipid context。
5. Docking target：已知 pocket、blind docking、蛋白-蛋白界面、膜/脂质相关位点或 restraint-defined site。
6. Compute location：本地 QC、服务器/GPU、外部 web server 或容器；记录版本和参数。

如果输入定义不清，不解释 docking 分数为生物学结论。

## 工具选择原则

- 快速可行性：HDOCK、ClusPro、CB-Dock、AutoDock Vina、GNINA 可作为 exploratory pilot。
- 结构预测/复合物：AlphaFold DB、ColabFold、Boltz、Chai、AF3-like services 要区分 model confidence 与 binding evidence。
- 突变体比较：必须同一 receptor preparation、ligand/partner preparation、参数和 scoring policy。
- 重型计算优先服务器/GPU；Mac 负责输入 QA、轻量转换、结果 QC、表格、图和报告。

## 结果解释边界

- Docking score 不是 binding affinity 的直接证明。
- 单一 pose 不是稳定构象；需要重复、对照、物理合理性和可视化检查。
- 突变体差异是 exploratory signal，除非有独立实验或多工具/多参数一致支持。
- 结构预测 confidence 不等于互作验证。

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

需要选择 docking/structure 工具时读取 `references/structure-docking-tool-matrix.md`。
