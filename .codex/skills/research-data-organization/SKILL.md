---
name: research-data-organization
description: 用于组织生物信息学项目的数据、表格、结果、图和常用文件路径，解决结果分散、最新文件不清、重要表格难找、投稿数据难汇总的问题。适用于建立目录结构、整理 latest/priority 文件、设计 manifest、迁移常用结果到一级目录或索引表。
---

# Research Data Organization

## 使用场景

当用户抱怨结果文件太散、找不到最新表格、一个结果生成多个文件夹、投稿时不知道哪个表该上传，或要求整理项目数据目录时使用本 skill。

## 核心原则

- 数据要可追踪，也要容易读取。
- 原始数据保持只读；已确认结论的关键表格和高频文件要有清晰入口。
- 重要文件可以通过 `latest`、`priority`、`manifest` 或一级目录索引暴露出来。
- 错误旧文件不需要永久保留在工作路径；可覆盖修正后的图表和派生表，但要保证最终 manifest 指向当前有效版本。
- 不用深层目录隐藏关键论文表格。

## 推荐结构

```text
results/
  priority_tables/
  priority_figures/
  source_data/
  latest_manifest.tsv
  archive/
```

## Manifest 推荐字段

- `id`
- `file_path`
- `file_type`
- `status`
- `latest`
- `related_claim`
- `related_figure`
- `source_input`
- `script`
- `updated_at`
- `notes`

## 工作流程

1. 扫描或读取用户指定目录，不默认全盘读取。
2. 识别高频文件、已确认结论文件、投稿相关文件和过期文件。
3. 建议一个浅层入口：priority tables、priority figures、source data、manifest。
4. 对需要覆盖的修正图表或派生表，确认它们是错误修正还是新版本分支。
5. 输出整理计划或 manifest 草案。

## 输出格式

- `Recommended layout`
- `Priority files`
- `Manifest fields`
- `Overwrite / archive decisions`
- `Next actions`

## 按需读取

需要设计目录、latest/priority 入口、manifest 字段或投稿前数据整理策略时，读取 `references/layout-and-manifest.md`。
