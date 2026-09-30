# Chemical curation contract

## Structure policy

```yaml
input:
  source: ""
  release_or_access_date: ""
  immutable_manifest_or_hash: ""
  structure_fields: []
  raw_identifier_fields: []
policy:
  parser_and_version: ""
  sanitization: ""
  fragment_parent: ""
  salts_and_mixtures: ""
  charge_and_neutralization: ""
  aromaticity: ""
  isotope: ""
  stereochemistry: retain | require | flag_unknown | remove_with_justification
  tautomer: retain | canonicalize_for_defined_use | enumerate_for_defined_use
  protomer_and_ph: ""
  canonical_identifier: ""
  failure_policy: retain_with_status | exclude_with_reason
```

每项 transformation 至少记录：

`raw_record_id, raw_structure, step, action, before, after, status, reason, software, version`

禁止覆盖 raw structure。用于 join 的标准化 ID 需要同时保留原始来源 ID 和 collision 检查。

## Measurement policy

```yaml
endpoint:
  target_id_and_construct: ""
  species: ""
  assay_type_and_format: ""
  endpoint_name: ""
  relation_policy: ""
  original_units: []
  target_unit: ""
  conversion: ""
  conditions_retained: []
replicates:
  grouping_keys: []
  aggregation: none | median | mean | model_based
  conflict_rule: ""
  censored_values: retain_relation | interval_model | exclude_with_reason
label:
  continuous_or_class: ""
  threshold_and_source: ""
  ambiguous_policy: ""
```

不要把 `IC50`、`EC50`、`Ki`、`Kd`、percent inhibition 或不同 biological systems 合并成一个标签。若必须转换或聚合，保留 measurement-level 表、理由和敏感性。

## Required artifacts

| Artifact | Minimum content |
|---|---|
| input manifest | file/source, version/date, hash, row count, license/access |
| structure map | raw ID/structure, standardized ID/structure, actions, status |
| measurement table | target/assay/endpoint/relation/value/units/context |
| exclusion table | raw ID, stage, reason, recoverability |
| QC summary | counts and rates by stage, conflicts, sample inspection |
| data card | intended use, policies, coverage, limitations, environment |
| modeling handoff | entity/group keys, label policy, split risks, immutable version |

## Attrition table

`stage, input_n, unchanged_n, changed_n, failed_n, excluded_n, output_n, reason, software_version`

Counts must reconcile. Report molecule records, unique raw entities, unique standardized structures and measurements separately.

## Modeling handoff checks

- Exact structure, stereochemical, tautomer/protomer and scaffold relationships are represented by explicit group keys.
- Replicates and repeated measurements cannot cross a downstream split unintentionally.
- Preprocessing learned from labels is not performed before split.
- Dataset source, assay, time and batch are available for leakage/error analysis.
- Excluded and failed records remain auditable.
- The handoff states what was not assessed, including synthesis, assay validity, applicability domain and external generalization.

## Split-readiness gate

- Report `split_ready: true | false` with unresolved criteria. Canonical identifiers alone do not establish readiness.
- Each structure/scaffold/stereo/tautomer/protomer/source/replicate group declares `assessed`, `unknown`, or `not_applicable` with evidence. Empty acyclic scaffolds are not valid shared keys; define an explicit alternative or block handoff.
- Missing required groups keep `split_ready: false`; downstream split/generalization validation belongs to ml-benchmarking.
- `assay_context_group` contains assay conditions, not chemical identity. Aggregation must also include chemical entity and endpoint/relation policy; never average different compounds just because context matches.
