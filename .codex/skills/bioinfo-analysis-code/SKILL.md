---
name: bioinfo-analysis-code
description: 用于生物信息学分析脚本、表格整理、轻量统计、Jupyter/CLI 工作流、运行命令、环境记录、可重复性说明、代码整理和发表前代码可读性优化。
---

# Bioinfo Analysis Code

## 核心问题

如何把生信分析从一次性脚本变成输入、输出、参数、环境和 caveat 都可追踪的可复现执行？

## 使用场景

当用户要求写脚本、整理 TSV/CSV、合并 metadata、做轻量统计、生成 summary table、调试分析流程或记录运行命令时使用本 skill。

## 执行原则

- 原始数据不修改。
- 输出写入新的结果目录或用户指定路径。
- 脚本必须声明输入、输出、关键参数和运行环境。
- 不静默改变过滤阈值、样本集合、参考版本或工具版本。
- 大型计算任务先确认项目 profile 中的服务器、集群或容器规则。
- 结果进入论文前必须留下可复现脚本、source data 和 caveat。
- 探索阶段可以写轻量脚本，但仍要记录关键命令和输入输出。
- 收尾或投稿阶段要整理为可读、可复现、可提交的代码，补充必要注释、参数说明和 README 片段。
- 注释应解释非显然逻辑、输入输出和关键参数，不写无意义逐行注释。
- 多步骤分析必须使用阶段编号组织脚本和产物，例如 `00_`, `01_`, `02_`。编号应反映处理顺序，而不是随意命名。
- 脚本、notebook、结果目录和关键输出文件应共享同一阶段编号，便于从结果反查生成步骤。
- notebook 可用于探索和记录，但稳定流程应整理成编号脚本或 workflow；不要把正式分析变成一堆无法按顺序重跑的 notebook。
- 当分析超过少数几个步骤，或需要反复重跑时，应考虑 `run_all.sh`、Snakemake、Nextflow 或类似 pipeline 入口。

## 推荐输出结构

```text
03_code/
  00_setup/
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
04_workflows/
  run_all.sh
  environment.yml
05_results/
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
  tables/
  figures/
  source_data/
  logs/
```

轻量项目也可以保持简单，但仍建议脚本按顺序编号：

```text
01_download_data.R
02_qc_filtering.R
03_normalization.R
04_differential_analysis.R
05_make_figures.R
```

## 输出格式

完成任务时说明：

- Step ID / workflow order
- Script
- Inputs
- Outputs
- Command
- Environment
- Key results
- Caveats / next checks
- Reproducibility level: `exploratory`、`stable` 或 `submission-ready`

## 按需读取

需要判断代码整理深度、探索阶段和投稿阶段的注释/README/环境要求时，读取 `references/reproducibility-levels.md`。
需要设计编号脚本、阶段产物、pipeline 入口或可复现项目结构时，读取 `references/workflow-numbering.md`。
需要执行外部工具、批量分析或多步骤 workflow，并希望避免“能跑但不可复现”时，读取 `references/local-first-execution-checklist.md`。
