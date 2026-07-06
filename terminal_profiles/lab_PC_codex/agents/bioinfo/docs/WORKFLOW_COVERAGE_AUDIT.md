# Rigorous Workflow Coverage Audit

审计日期：2026-05-19

审计对象：`journal_codex_AGENT` v1.3 当前 `AGENTS.md`、26 个通用 skills，以及归档文档 `rigorous_research_workflow_computational_biology.md`。

## 总体结论

当前 agent/skill 已覆盖大部分模块，但原流程文档是一条“从问题到论文”的完整研究生命周期，而现有实现更像多个独立 skill。主要缺口不是新增单点功能，而是需要一个包级指导文件把这些 skill 串起来，并把若干科研习惯下沉到对应 reference。

本轮处理：

- 新增 `docs/RIGOROUS_COMPUTATIONAL_RESEARCH_WORKFLOW_GUIDE.md`，作为通用研究流程指导文件。
- 补强 `project-guide-maintainer`，让 `PROJECT_GUIDE.md` 能承接完整研究主线，而不是只承接 planner 输出。
- 补强 `research-project-planner` 的选题卡和五句话框架。
- 补强 `bioinfo-analysis-code` 的 exploration/confirmation/validation、负结果、ML 泄漏和 pipeline 分级。
- 补强 `task-self-check`、`submission-readiness-audit` 的阶段自检和 reviewer attack list。

## 覆盖矩阵

| 原文模块 | 当前覆盖 | 缺口判断 | 本轮处理 |
|---|---|---|---|
| 0 总体流程 | 根 `AGENTS.md` 有身份和路由；各 skill 分散覆盖 | 缺少包级生命周期指南 | 新增 `RIGOROUS_COMPUTATIONAL_RESEARCH_WORKFLOW_GUIDE.md` |
| 1 问题重要和概念推进 | `research-project-planner`, `research-decision-review` | 选题时对 importance/conceptual advance 的检查可更明确 | 补强 planner 模板 |
| 2 选题阶段 | `research-project-planner` | 缺少一页选题卡 | 补入 project brief template |
| 3 立项阶段 | `research-question-brief`, `research-project-planner`, `project-guide-maintainer` | `PROJECT_GUIDE.md` 应保留五句话和研究阶段状态 | 补强 project guide 模板 |
| 4 Figure skeleton | `figure-caption`, `publication-plotting`, `claim-evidence-audit` | 基本覆盖；需要强调每图服务 central claim | 写入包级 guide |
| 5 可复现项目 | `project-environment-bootstrap`, `research-data-organization`, `bioinfo-analysis-code`, `source-data-audit` | 已覆盖；编号 workflow 已补，但需和阶段状态连接 | 补强 reproducibility reference |
| 6 Pipeline | `bioinfo-analysis-code` | 已有编号和 pipeline tiers；需强调 notebook 不能作为最终系统 | 已在 workflow reference 覆盖，轻微补强 |
| 7 Exploration/confirmation/validation | `validation-strategy-planner`, `evidence-gap-finder`, `bioinfo-analysis-code` | 缺少 ML 泄漏和负结果记录的显式门控 | 补强 reproducibility/self-check |
| 8 写作阶段 | 三个写作 skill, `claim-evidence-audit` | 已覆盖；五句话框架应进入 project guide/planner | 补强 planner 和 guide |
| 9 投稿前审计 | `submission-readiness-audit`, `reviewer-simulation`, `source-data-audit` | reviewer attack list 应显式模板化 | 补强 submission checklist |
| 10 完整流程 | 多 skill 分散覆盖 | 缺少统一串联 | 新增包级 guide |
| 11 习惯改变 | 根 `AGENTS.md` 和多个 skill 间接覆盖 | 不适合塞进根 AGENT | 写入包级 guide 和相关 reference |
| 12 最小可执行版本 | `research-project-planner`, `project-guide-maintainer`, `task-self-check` | 应作为混乱项目的 fallback | 写入包级 guide |

## 外部参考吸收点

| 来源 | 可吸收点 | 对应落点 |
|---|---|---|
| PLOS Ten Simple Rules for Reproducible Computational Research | 每个结果要记录生成方式；避免手工不可追踪处理；记录软件、参数和输入 | `bioinfo-analysis-code`, `source-data-audit` |
| ENCORE framework | project compendium 应整合 concepts、data、code、results、documentation | `project-guide-maintainer`, `research-data-organization` |
| FAIR computational workflows | workflow 本身需要可发现、可访问、可互操作、可复用的元数据和文档 | `bioinfo-analysis-code`, `source-data-audit` |
| Nextflow / nf-core | 单命令执行、容器、执行 provenance、标准化参数和文档 | `bioinfo-analysis-code`, `environment-and-tool-adoption` |
| Research compendium / compbio template | 论文、代码、数据、环境、结果共同组成可复现研究包 | 包级 guide, `research-data-organization` |
| GitHub / bioinformatics forum 讨论 | GitHub 不适合放大数据；仓库应放代码、说明、轻量结果和下载/复现脚本 | `project-environment-bootstrap`, `research-data-organization` |

## 后续可选改进

| 优先级 | 建议 | 说明 |
|---|---|---|
| P1 | 给 `project-guide-maintainer` 增加压缩脚本或模板生成脚本 | 可快速生成 `PROJECT_GUIDE.md` 初稿 |
| P1 | 给 `source-data-audit` 增加 inventory 模板 CSV | 更容易标准化 source data 追踪 |
| P2 | 给 `bioinfo-analysis-code` 增加 `run_all.sh`/Snakemake/Nextflow 示例 references | 等真实项目需要时再加，避免现在变长 |
| P2 | 新增专项 workflow pack | RNA-seq、single-cell、ATAC-seq、variant/GWAS 等按需添加 |
| P2 | 增加 `PROJECT_GUIDE.md` 摘要更新 diff 模板 | 方便长期项目少读上下文 |

