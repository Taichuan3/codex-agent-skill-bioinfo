# Protein Docking Evidence Contract

用于吸收外部 PDB、Boltz、DiffDock、protein-QC、UniProt 等 skills 的通用机制。目标是锁定输入、减少错误解释，并把结构/对接结果限制在合适证据等级。

## 输入锁定

- Protein：accession、species、isoform、sequence length、domain boundaries、mutation list。
- Structure：experimental PDB/mmCIF、AlphaFold DB、Boltz/Chai/ColabFold model；记录 chain、model number、missing residues、pLDDT/PAE/interface confidence。
- Ligand/partner：SMILES/InChI/SDF/MOL2、protonation、tautomer、stereochemistry、charge、cofactor/metal/lipid context。
- Binding site：known pocket、blind docking、interface residue、restraint 或 literature-defined region。
- Numbering：UniProt、PDB chain residue number、model residue number和用户给定坐标必须对齐。

## 运行与 QC

- 对 known binder 优先 self-dock/cross-dock 或 positive control；没有对照时结果只能 exploratory。
- 对 batch docking 建立样本表，包含 receptor、ligand、site、method、seed、replicate 和 output path。
- 检查 pose：clash、buried polar group、unreasonable torsion、metal coordination、membrane context、missing pocket residues。
- 对多个工具/参数一致性只提升到 Moderate；仍不能替代实验结合数据。
- 记录软件版本、model/version、GPU/server、参数和随机种子。

## 解释边界

- Pose confidence 不是 binding affinity。
- Docking score 不是 `Kd`、`IC50` 或 efficacy。
- Predicted complex confidence 不是 protein-protein interaction proof。
- WT-mutant score difference 是 hypothesis-generating，除非同一 preparation、同一参数、重复和对照都支持。
- Virtual screening rank 必须结合化学可行性、已知活性、PAINS/reactivity、ADMET 和 orthogonal validation。

## 输出

- locked inputs
- structure provenance
- method and parameters
- QC pass/fail
- ranked poses or candidates
- evidence level
- caveats and next validation
