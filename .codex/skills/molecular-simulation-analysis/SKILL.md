---
name: molecular-simulation-analysis
description: 设计、执行或审查 MD/分子模拟轨迹分析：topology/trajectory、单位与时间、PBC、selection/alignment、RMSD/RMSF/contact、采样、replicate/uncertainty 和 source data。支持 OpenMM/GROMACS/AMBER 与 MDAnalysis/MDTraj；不负责生产模拟、参数化、自由能执行或从短轨迹证明稳定结合。
---

# Molecular Simulation Analysis

## 核心问题

如何把 topology 与 trajectory 转成问题驱动、可复现并尊重时间相关性和采样边界的分析，而不是堆积 RMSD 等图形后过度解释？

## 能力与路由边界

- 本 Skill 负责 trajectory preflight、分析设计、已授权的 bounded analysis、统计/QC 和解释边界；用户确认科学问题、selection、reference、analysis window 和最终 claim。
- system building、protonation、force-field/ligand parameterization、production run protocol 或 FEP/ABFE/RBFE 执行不在本 Skill 范围；需要专项方法审查后再决定工具。
- docking、pose、pocket 和结构输入 QA 由 `protein-structure-docking` 负责；本 Skill 可接收锁定的结构/模拟 provenance。
- 已冻结分析契约后的脚本、notebook、批处理和 workflow 实现组合 `bioinfo-analysis-code`。
- 工具安装、环境兼容和后端选择交给 `environment-and-tool-adoption`；图形设计与投稿导出交给 `publication-plotting`。
- read-only 请求只审查输入、方法、图表和结论，不改轨迹、不重跑模拟。

## 输入契约

分析前锁定：

1. 决策问题和 observable：稳定性描述、局部柔性、相互作用占有率、构象分群、条件比较或采样诊断。
2. topology/trajectory：格式、路径/hash、atom order、frame count、time step、单位、periodic box 和 trajectory stride。
3. 系统 provenance：engine/version、force field、water/ions、temperature/pressure、constraints、integrator、equilibration/production、restart 和 replica/seed。
4. selection/reference：chain/segment/residue/atom mapping、fit selection、analysis selection、reference frame/ensemble 和 ligand naming。
5. preprocessing：PBC unwrap/make-whole、center、alignment、frame exclusion 和 transformation order。
6. comparison/statistics：replica policy、analysis window、block size/autocorrelation、uncertainty、multiple comparisons 和 stop criteria。

## 工作流程

1. 锁定模式：`analysis plan`、`trajectory preflight`、`bounded analysis` 或 `result audit`。
2. 保持原始 topology/trajectory 只读；核验 atom count/order、frame/time、units、box、missing/corrupt frames、restart discontinuity 和 replica mapping。声明 equilibrium/biased-or-nonequilibrium/unknown；reader时间不等于已验证物理时间。科学provenance不足时STOP科学解释，可在明确授权下做有界解析/数值工程测试，但工程PASS不得解除科学STOP。
3. 将 PBC 处理、centering、fitting 与 observable 计算拆开记录；保存 transformation order，不覆盖原始轨迹。
4. 先根据科学问题指定 fit selection、analysis selection、reference 和 analysis window；不得在看图后无记录地挑选最有利窗口。
5. 选择最小 observable 集：RMSD、RMSF、distance/contact、H-bond、radius of gyration、SASA、dihedral、PCA/cluster 等只在能回答问题时使用。
6. 对时间序列检查 equilibration/transient、drift、autocorrelation 和 block sensitivity；trajectory frames 不作为独立生物学重复。
7. 比较条件时优先独立 replicas；报告 within-run variation、between-replica consistency、effective information 和失败/未完成 replica。
8. 对 cutoff、selection、reference、fit group、window 或 clustering 参数做必要敏感性分析；记录结论是否稳定。
9. 保存 tidy source data，包含 `system_id, replica, frame, time, selection, metric, value, units, method_version, qc_status` 及参数/provenance 指针。
10. 交付实际分析范围、QC、图表/source data、统计限制和下一验证；若采样不足，降级表述或停止比较。

## 解释硬边界

- RMSD plateau 不单独证明系统平衡、配体稳定结合、正确 pose 或生理状态。
- 低 RMSF、高 contact occupancy 或单条持续氢键不单独证明功能、亲和力或机制。
- 短轨迹、单 replica、被挑选的时间窗口或高相关 frames 不能提供可靠独立样本量。
- 轨迹内误差不能替代独立重复；帧数增加不等于采样空间充分。
- 不同 force field、protonation、box、restraint、temperature、trajectory stride 或 preprocessing 的结果不可默认直接比较。
- PCA/cluster 展示的是所给轨迹与特征定义下的构象结构，不证明真实自由能面或完整状态集合。
- MM/GBSA、FEP 或其他自由能输出需要独立方法契约；不以普通轨迹图替代其收敛与误差分析。

## 模式化输出

- `analysis plan`：question、inputs、selections/reference、preprocessing、observables、statistics、controls、artifacts 和 stop criteria。
- `trajectory preflight`：topology/frame/time/unit/PBC/replica 状态、阻塞项和可分析范围。
- `bounded analysis`：实际命令/代码、版本、QC、source data、plots、sensitivity、失败和证据等级。
- `result audit`：图表到输入/selection/window 的追踪、时间相关性、replica、unsupported claims 和最小修复。

## 按需读取

设计 trajectory schema、preprocessing、observable、sampling/statistics、source data 或 claim language 时，读取 `references/trajectory-analysis-contract.md`。

最终回复先给哪些问题能或不能由当前轨迹回答，再给精确输入、selection/reference、preprocessing、分析窗口、工具版本、QC、统计/采样边界、artifacts 和下一项验证。
