# Metadata-first project audit

用于成熟研究项目“先知道有什么、谁在使用、时间语义是什么，再决定怎么迁移”的可复用审计。

## Audit mode and authority

- `read-only audit`：只读取和报告，不创建 catalog、README、manifest 或脚本，不改变文件。
- `artifact generation`：用户要求持久化审计结果时，才创建 catalog/registry/migration map。
- `physical migration`：必须有明确 migration map、compatibility plan 和用户授权；分类建议不等于移动或删除授权。

## Artifact catalog contract

建议字段：

- `asset_id`, `path`, `layer`, `role`, `format`, `size_bytes`, `mtime`;
- `row_count`, `column_count`, `date_start`, `date_end`, `primary_key_candidate`, `duplicate_key_rows`;
- `source_fields`, `as_of_fields`, `quality_fields`, `time_valid_class`;
- `producer`, `consumer`, `schema_status`, `target_layer`, `migration_action`, `checksum`.

Catalog 是 profile，不是 schema certification。若由脚本生成，manifest 必须排除自身，并校验记录路径集合、size 和 mtime。

## Consumer verification

从实际 loader、workflow、configuration、report link 和 writer code 列出读取/写入资产，与 catalog 做差集：

- available but unused;
- consumed but undocumented;
- documented but missing;
- consumed current proxy;
- duplicate or conflicting source.

“项目里存在一张表”不能写成“当前模型或主分析消费了该表”。README 和文件名只能导航，不能替代 consumer code 证据。

## As-of and time-valid classification

可按项目语义使用：

- `verified_historical_as_of_valid`;
- `as_of_candidate_requires_source_audit`;
- `release_lag_proxy_not_exact_calendar`;
- `current_snapshot_not_historical`;
- `historical_grid_without_field_history`;
- `source_snapshot_not_versioned`;
- `test_fixture_only`;
- `not_assessed`.

文件含历史日期列不等于所有字段在当时可见。必须核验发布日期、修订、回填、数据库版本和字段可用时点。

## Registries and conflicts

- Model registry 可记录 model ID/version、role、status、data contract、主要指标、validation status、evidence path 和 claim boundary。
- Experiment registry 可记录 run ID、config/dataset/code version、split、benchmark、status、artifact paths 和 contamination state。
- 重复 registry 以稳定 ID 对齐，保留 source paths、copy count 和冲突状态；不要因建立 canonical view 就删除旧副本。

## Migration map

至少记录 `source_path`、`target_path`、`risk`、`reason`、`path_consumers`、`compatibility_action`、`move_phase`、`verification` 和 `status`。

推荐顺序：no-move audit → targeted Directory Cards → canonical registries → data/schema contracts → migration map → 单 pipeline 用户授权迁移与回归 → 最后再评估旧路径清理。
