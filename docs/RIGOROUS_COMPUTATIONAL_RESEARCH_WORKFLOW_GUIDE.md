# Rigorous Computational Biology Workflow Guide

本文件是 `journal_codex_AGENT` 的包级研究流程指导文件。它不替代任何 skill，也不应该在日常任务中默认全文读取；它的作用是定义通用生信研究的“骨架”：从问题形成、证据设计、可复现执行、验证、写作到投稿审计。

## 设计依据

本指南综合了本地归档文档 `rigorous_research_workflow_computational_biology.md`，以及计算研究可复现性和 workflow 相关公开资料：

- PLOS Computational Biology: Ten Simple Rules for Reproducible Computational Research
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285
- Nature Communications: ENCORE framework for reproducible computational research
  https://www.nature.com/articles/s41467-024-52446-8
- Scientific Data: Applying the FAIR Principles to computational workflows
  https://www.nature.com/articles/s41597-025-04451-9
- Nature Biotechnology: Nextflow enables reproducible computational workflows
  https://www.nature.com/articles/nbt.3820
- nf-core pipeline specifications
  https://nf-co.re/docs/specifications/pipelines/overview
- rOpenSci research compendium pattern
  https://github.com/ropensci/rrrpkg
- Computational biology project template
  https://github.com/bsmith89/compbio-template

## 核心判断

计算生物学研究不能从“我会跑什么分析”开始。更稳的顺序是：

```text
定义重要问题
-> 明确知识缺口
-> 提出可检验假设
-> 设计证据链和 figure skeleton
-> 建立可复现计算系统
-> exploration
-> confirmation
-> validation
-> 收敛科学故事
-> 投稿前审计
-> 审稿迭代
```

对应到本智能体，`research-project-planner` 只负责前期规划；完整流程应由多个 skill 串联完成。

## 最小项目指导文件

每个长期项目建议维护一个轻量 `PROJECT_GUIDE.md`，由 `project-guide-maintainer` 负责创建、压缩和更新。它不是操作日志，也不是完整论文，而是后续任务理解项目的最小上下文入口。

建议保留：

- `One-line summary`
- `Central question`
- `Known / Unknown / Question / Finding / Advance`
- `Working hypothesis / model`
- `Figure skeleton`
- `Evidence package`
- `Exploration / Confirmation / Validation status`
- `Current progress`
- `Open questions`
- `Next decisions`
- `Reviewer attack list`
- `Pointers`：优先脚本、表格、图、source data、operation log

`PROJECT_PLAN.md` 只记录操作、命令、运行结果和复盘；除非需要查历史执行细节，不应作为默认读取对象。

## 阶段和 Skill 映射

| 研究阶段 | 目标 | 默认 skill |
|---|---|---|
| 方向扫描 | 找领域争议、未解问题、关键文献和方法路线 | `literature-search-workflow`, `paper-reader` |
| 原始想法压缩 | 把口头想法变成短 brief | `research-question-brief` |
| 项目立项 | 写 central question、gap、hypothesis、expected claim、figure skeleton | `research-project-planner` |
| 项目指导维护 | 把 brief/planner 输出压缩成轻量长期上下文 | `project-guide-maintainer` |
| 证据设计 | figure-to-claim、所需对照、source data 和 caveat | `figure-caption`, `claim-evidence-audit` |
| 环境启动 | 只在新项目、切换机器/目录或环境未知时检查 | `project-environment-bootstrap` |
| 数据和产物组织 | 管理 latest/priority 表格、图和 manifest | `research-data-organization` |
| 分析执行 | 编号脚本、pipeline、输入输出、环境和日志 | `bioinfo-analysis-code` |
| 探索结果补强 | 找 evidence gap 和最小补分析集合 | `evidence-gap-finder` |
| 验证策略 | 设计 confirmation、validation、外部数据和降级写法 | `validation-strategy-planner` |
| 图表生成 | manuscript-ready/PPT-readable 输出和 source data | `publication-plotting` |
| 写作和润色 | 中文润色、英文翻译、英文润色 | `chinese-scientific-polishing`, `scientific-english-translation`, `scientific-english-polishing` |
| 投稿前审计 | 复现、source data、引用、图表、方法、审稿风险 | `submission-readiness-audit`, `source-data-audit`, `manuscript-consistency-audit` |
| 审稿迭代 | 拆解真实审稿意见并形成行动和回复 | `reviewer-response-builder` |

## 选题卡

新方向正式开题前，建议先写一页选题卡：

| 维度 | 要回答的问题 |
|---|---|
| 重要性 | 这个问题解决后，领域里的什么判断会改变？ |
| 新颖性 | 它是新机制、新方法、新资源，还是新解释框架？ |
| 可行性 | 3-6 个月内能否得到 decisive result？ |
| 证据路径 | 需要哪些数据、模型、统计、对照和验证？ |
| 风险 | 最大不确定性来自数据、方法、解释还是验证？ |
| 个人优势 | 为什么当前项目/用户适合做这个问题？ |
| 产出形态 | 更像 discovery、method、resource，还是 integrative analysis？ |

## 五句话框架

写论文、维护 `PROJECT_GUIDE.md` 或收敛故事前，先检查五句话：

1. `Known`：领域已知什么？
2. `Unknown`：最关键的未知是什么？
3. `Question`：本文问什么问题？
4. `Finding`：当前数据支持了什么发现？
5. `Advance`：这个发现如何改变理解、方法或后续实验设计？

这五句话写不清楚时，不应直接进入大段 manuscript 写作。

## Figure Skeleton 原则

每张主图都必须回答一个问题，并推进同一个 central claim。

| 图 | 常见作用 |
|---|---|
| Fig. 1 | 数据集、QC、总体 landscape 或关键现象 |
| Fig. 2 | 核心发现：差异、轨迹、网络、signature、空间定位等 |
| Fig. 3 | 机制推断：pathway、TF、ligand-receptor、causal model 等 |
| Fig. 4 | 独立验证：外部队列、跨物种、公开数据或实验数据 |
| Fig. 5 | 功能或预测价值：biomarker、risk model、drug response、perturbation |
| Fig. 6 | 模型总结：graphical model 或 mechanism model |

不要为了“做得多”堆图。不能服务 central claim 的结果应降级为补图、备选路线或暂不进入论文。

## 可复现项目最低标准

最低目标：三个月后的自己能够只看 README 和 run script 重新生成主要图表。

推荐结构：

```text
00_project_brief/
01_literature/
02_data/
  raw/
  processed/
  metadata/
03_code/
  00_setup/
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
04_workflows/
05_results/
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
  tables/
  figures/
  source_data/
  logs/
06_manuscript/
```

轻量项目可以简化目录，但仍应保留：

- 原始数据只读
- 编号脚本
- 输入、输出、命令、参数、环境记录
- 主要图表 source data
- 当前有效结果 manifest
- README 或 `PROJECT_GUIDE.md` 指向主要入口

## Pipeline 分级

| 等级 | 标准 |
|---|---|
| Minimum | 编号脚本、明确输入输出、记录命令和版本控制代码 |
| Stable | conda/mamba/renv、README 命令、logs、`run_all.sh`、关键输出 manifest |
| Advanced | Snakemake/Nextflow/nf-core 风格、容器、执行 trace、语义化版本、可行时 CI |

Notebook 可以用于探索和记录，但正式结果不应只存在 notebook 中。

## Exploration / Confirmation / Validation

| 阶段 | 目的 | 允许 | 不允许 |
|---|---|---|---|
| Exploration | 找模式和假设 | 多尝试、多画图、多比较 | 把探索结果写成最终证明 |
| Confirmation | 检验核心假设 | 固定参数、固定统计、做对照 | 看到结果不好就无限调参 |
| Validation | 证明结果稳健 | 外部队列、orthogonal method、实验验证、负对照 | 在同一数据集里循环证明自己 |

常见高风险点：

- 公开数据挖掘容易得到漂亮但不稳的故事。
- 机器学习必须避免 train/test/validation 泄漏，尤其是归一化、批次校正和特征选择。
- p value 不能替代生物学解释。
- 负结果也要记录，防止重复绕路。

## 投稿前 Reviewer Attack List

投稿或大版本收尾前，必须主动攻击自己的论文：

| 类型 | 问题 |
|---|---|
| Central claim | 核心主张是否一句话能说清？ |
| Figure logic | 每张主图是否服务 central claim？ |
| Alternative explanations | 是否排除批次效应、样本偏倚、混杂变量和方法 artifact？ |
| Validation | 是否有独立数据、实验或 orthogonal method 支持？ |
| Reproducibility | 主要图是否能从代码重新生成？ |
| Data/code availability | 数据、代码、环境、参数、版本是否清楚？ |
| Methods | 统计方法、阈值、软件版本、随机种子和排除规则是否写明？ |
| Journal fit | 是 field-specific advance，还是 broad conceptual advance？ |

## 最小可执行版本

如果项目还很混乱，只做这六件事：

1. 写一句 central question。
2. 写五句话：Known、Unknown、Question、Finding、Advance。
3. 画理想状态下 4-6 张主图。
4. 建立或整理 repo，使代码、数据、结果、文档分开。
5. 给每个关键结果写清楚数据来源、脚本、参数和输出图。
6. 写 reviewer attack list，列出最可能被质疑的 10 点。

