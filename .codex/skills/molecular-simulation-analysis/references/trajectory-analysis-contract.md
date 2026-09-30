# Trajectory analysis contract

## Input and preprocessing

```yaml
question: ""
systems:
  - system_id: ""
    topology: ""
    trajectories: []
    replicas: []
    engine_and_version: ""
    force_field: ""
    ensemble: ""
    temperature: ""
    pressure: ""
    timestep: ""
    saved_stride: ""
    units: ""
preflight:
  atom_order_and_count: ""
  frame_count_and_time: ""
  periodic_box: ""
  discontinuities_or_corruption: ""
  residue_and_ligand_mapping: ""
preprocessing:
  make_whole_or_unwrap: ""
  center: ""
  fit_selection: ""
  reference: ""
  analysis_selection: ""
  frame_window: ""
  transformation_order: []
```

原始 trajectory 保持只读。转换后的 trajectory 若保存，使用新路径并记录 producer、参数和输入 hash。

## Observable contract

| Observable | Define before use | Common false inference |
|---|---|---|
| RMSD | fit group, analysis group, reference, atom mapping | plateau proves equilibrium or binding |
| RMSF | fit policy, atom/residue reduction, window | low flexibility proves functional importance |
| distance/contact | atom groups, periodicity, cutoff, occupancy denominator | persistent contact proves affinity |
| H-bond | donor/acceptor definition, distance/angle, water policy | occupancy proves mechanism |
| Rg/SASA | selection, radii/algorithm, units | compactness proves native state |
| dihedral | atom definition, periodic statistics | one distribution proves full sampling |
| PCA/cluster | features, alignment, scaling, fit data, cluster rule | clusters equal true metastable states |

每个 observable 都要绑定 decision question、单位、计算库/版本、参数、source-data path 和 sensitivity。

## Sampling and statistics

- 先画时间序列和 cumulative/block summaries，再计算一个总均值。
- 声明 equilibration exclusion；不得只因图更平稳而选择窗口。
- 估计或定性检查 autocorrelation；frames 不能当作独立 replicates。
- 独立 replica 是条件比较的主要重复层。单 replica 结果保持 descriptive/exploratory。
- 报告 block/window/cutoff/reference/selection sensitivity。
- 若 production 长度、replica 数或状态转换不足以支持比较，保留 `sampling insufficient`。

## Source data schema

```text
system_id
condition
replica
frame
time
time_unit
selection
reference
metric
value
value_unit
window
preprocessing_id
method
version
parameter_id
qc_status
source_trajectory
```

## Claim ladder

- `descriptive`：在已分析轨迹和定义下观察到某数值/趋势。
- `comparative exploratory`：匹配设置与 replicas 下存在方向一致的差异，但外部验证和采样仍有限。
- `mechanistic hypothesis`：轨迹支持一个可检验结构假说；仍需正交实验或更强模拟。
- 不从普通短 MD 单独升级为 affinity、功能、因果、安全或临床结论。

## Stop conditions

- topology/trajectory atom mapping 不一致且无法恢复；
- 单位、time step、PBC 或 restart provenance 不明；
- selection/reference 不能映射；
- 条件比较的 system preparation 或 analysis policy 不匹配；
- 严重采样不足使预定 claim 无法评估；
- 需要自由能或生产级模拟但没有独立方法、资源和验证契约。

## Engineering versus scientific gate

- Record `equilibrium`, `biased_or_nonequilibrium`, or `unknown`; biased transition paths such as DIMS are not equilibrium samples.
- Reader frame/time metadata is not validated physical timestep/stride. Use frame indices when physical time is unverified.
- Missing scientific provenance keeps `scientific_status: STOP`. Explicitly authorized bounded parsing/numerical tests may proceed only when their own mapping/unit prerequisites are satisfied; report `engineering_status` separately.
- Engineering PASS never clears scientific STOP or establishes equilibrium/kinetics/thermodynamics. Unknown PBC forbids PBC-dependent observables, not a scoped non-PBC parser test.
