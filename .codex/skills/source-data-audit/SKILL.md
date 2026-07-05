---
name: source-data-audit
description: 用于构建或审查生物信息学论文 source-data inventory、numbers-to-lock、figure/table-to-source traceability、Data/Code Availability、FAIR-like metadata、repository/accession plan 和关键文字证据来源。
---

# Source Data Audit

## 使用场景

当用户要求整理 source data、锁定论文数字、检查图表数据来源、准备 Data/Code Availability、审查 FAIR 元数据或规划 repository/accession 时使用本 skill。

## 审查目标

- 每个 figure / table 的数据来源清楚。
- 每个关键数字和关键文字结论能追踪到脚本、输入、输出或文献。
- raw、filtered、projected、manual-reviewed 数据状态明确。
- 文件命名和列名稳定，后续论文阶段不用猜测含义。
- Data/Code Availability 不承诺尚未准备好的数据。
- 对错误修正或轻微修改后的派生图表/表格，可以覆盖旧文件；不需要在工作路径保留旧的错误版本。
- 覆盖后 inventory 必须指向当前有效文件，必要时在 notes 中说明这是 correction，而不是保留多份混淆版本。

## 推荐字段

source-data inventory 可包含：

- `figure_or_table`
- `panel`
- `claim`
- `source_file`
- `data_state`
- `script`
- `environment`
- `key_numbers`
- `caveat`
- `status`
- `latest`
- `updated_at`

## 输出格式

根据任务输出：

- source-data inventory 草案或审查意见
- numbers-to-lock 清单
- Data/Code Availability notes
- 缺失文件、缺失 metadata 或不可复现环节
- 下一步补齐优先级
- 当前有效文件和可覆盖/应归档文件建议

## 按需读取

- 需要设计 manifest、source data 字段、FAIR-like 检查或 dataset README 时，读取 `references/fair-manifest.md`。
- 需要规划 repository、accession、DOI、受限数据或投稿前数据准备时，读取 `references/repository-readiness.md`。
