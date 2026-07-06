# Data Layout and Manifest Reference

## 目标

让项目结果既可追踪，也容易被再次找到。不要为了记录完整性，把已确认结论的关键表格、主图、source data 和投稿材料埋在多层临时目录里。

## 推荐目录

```text
results/
  latest_manifest.tsv
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
  priority_tables/
  priority_figures/
  source_data/
  archive/
```

## 使用规则

- `priority_tables/` 放已确认结论、高频使用、投稿或复盘常用的表格。
- `priority_figures/` 放当前有效的展示图、论文图或 PPT 图。
- `source_data/` 放可重建 figure/table 的整理数据，不放无法解释来源的孤立文件。
- 编号目录放按 workflow 顺序产生的阶段产物，编号应能对应脚本或 workflow step。
- `latest_manifest.tsv` 是入口索引，记录当前有效文件，不要求每次读取长项目计划。
- `archive/` 只放确实需要保留的旧版本、分支方案或历史比较；错误修正后的派生文件可以覆盖旧文件。

## Manifest 字段

```text
id
stage_id
stage_name
file_path
file_type
status
latest
related_claim
related_figure
source_input
script
command
environment
updated_at
notes
```

## 覆盖与归档

- 原始数据保持只读。
- 派生表格、整理表、图和中间结果如果只是错误修正或轻微调整，可以覆盖旧文件。
- 如果两版代表不同分析路线、不同参数或不同科学解释，应保留为分支并在 `notes` 中说明。
- 覆盖后必须更新 manifest，让它指向当前有效版本。
