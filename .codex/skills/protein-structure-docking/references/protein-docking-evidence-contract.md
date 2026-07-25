# Protein Docking Evidence Contract

## 输入与 provenance

| Layer | Minimum record |
|---|---|
| Protein | accession, species, isoform, sequence/hash, domains, mutations |
| Structure | source ID/version, method/model, chain, residue map, apo/holo, missing regions, confidence |
| Ligand/partner | stable ID or sequence, structure file/hash, stereochemistry, protomer/tautomer, charge, salts |
| Site/context | pocket/interface/restraints, cofactors, metals, membrane/lipid or covalent assumptions |
| Run | software/model version, preparation protocol, parameters, seed, replicate, compute environment, output path |

UniProt、PDB chain、预测模型与用户坐标必须显式对齐。无法对齐时把相关 residue-level 解释标记为 `not assessed`。

## 对照与运行 QC

- known binder 可用时优先 self-dock/redock 或 cross-dock；记录 RMSD 定义及 atom mapping。
- 比较 WT/mutant、ligand 或方法时固定 preparation、site/box/restraints、参数、seed/replicate policy 和 ranking definition。
- batch summary 至少包含 `sample_id, receptor_id, ligand_or_partner_id, site, method_version, seed, replicate, status, score_name, score_value, qc_status, output_path, failure_reason`。
- 检查完成率、重复一致性、正/负对照、clash、buried unsatisfied polar groups、不合理 torsion/strain、pocket placement、metal geometry、membrane context 和缺失 pocket/interface residue。
- 原始模型输出与后处理结果分开保存；转换、过滤和 rank 规则必须可重跑。

## 证据层

| Layer | Can support | Cannot support alone |
|---|---|---|
| Model confidence | model/geometry triage | binding, function, causality |
| Docking score/rank | within-protocol prioritization | affinity, potency, selectivity |
| Pose/interface QC | physical plausibility | stable physiological interaction |
| Matched score delta | perturbation hypothesis | mutation function or mechanism |
| Orthogonal experiments | assay-specific evidence | broader clinical efficacy or safety without relevant studies |

多工具或多参数一致只能在输入、比较协议和失败模式可比时作为 sensitivity evidence。不得把不同工具的 raw score 当作同一量纲直接平均。

## 交付最小字段

- locked inputs and unresolved mappings
- structure and ligand/partner provenance
- task class, method, parameters, controls and replicates
- run counts and failures
- pose/interface QC and score definition
- evidence level and unsupported claims
- exact artifact paths and next orthogonal validation
