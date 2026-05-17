---
name: bioinfo-analysis-code
description: 用于生物信息学分析脚本、表格整理、轻量统计、Jupyter/CLI 工作流、运行命令、环境记录、可重复性说明、代码整理和发表前代码可读性优化。
---

# Bioinfo Analysis Code

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

## 推荐输出结构

```text
scripts/
results/
  tables/
  figures/
  source_data/
jobs/
summary.md
```

## 输出格式

完成任务时说明：

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
