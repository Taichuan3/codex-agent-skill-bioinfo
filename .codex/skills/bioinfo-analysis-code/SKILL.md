---
name: bioinfo-analysis-code
description: 用于实现、调试或重构可复现的生物信息学分析代码，包括脚本、notebook、CLI/workflow、表格处理、轻量统计、运行记录和复现包；不用于以视觉设计为主的绘图、caption/source-data 审计或 pathway/network 方法解释。
---

# Bioinfo Analysis Code

## 核心问题

如何把生信分析从一次性脚本变成输入、输出、参数、环境和 caveat 都可追踪的可复现执行？

## 边界与组合

- 负责代码实现、运行、调试、表格和轻量统计；科学问题、统计定义、样本/过滤选择和最终解释由用户确认。
- 以图形设计、panel 编排、导出和 visual QA 为主时，改用 `publication-plotting`；本 Skill 只提供绘图所需的数据处理或可复现代码。
- 只写 figure legend/caption 时用 `figure-caption`；只核验 panel 的 source data、脚本和统计追溯时用 `source-data-audit`。
- pathway enrichment 或 network 的 universe、方法、QC 和生物学解释用 `pathway-network-analysis`；需要把已确认方案实现成脚本或 workflow 时再组合本 Skill。
- 蛋白结构或 docking 的方法选择与证据边界优先用 `protein-structure-docking`；本 Skill 可实现其输入检查、批处理、结果解析和复现包装。
- 工具选型、安装或新环境采用 `environment-and-tool-adoption`，项目级目录迁移和 manifest 用 `research-data-organization`。

## 工作流程

1. 读取适用的 `AGENTS.md`、必要的 `PROJECT_GUIDE.md` 和局部 Directory Card；锁定用户授权的文件与输出范围。
2. 声明输入、输出、schema、样本/feature universe、过滤与统计定义、参考/数据库版本、随机种子和环境；原始数据保持只读。
3. 先检查少量行、文件数、维度和 join key；大型或昂贵任务先跑可代表的小样本，并检查日志、输出计数和磁盘占用。
4. 把参数放入 CLI/config，而不是隐藏在对话或 notebook state；多步骤流程让脚本、结果和日志共享稳定 stage ID。
5. 运行与风险相称的验证：schema、行列数、唯一键、样本覆盖、缺失值、预期输出和关键不变量。不得用“命令成功”替代结果验证。
6. 将稳定 notebook 整理为脚本或明确固定其 kernel、环境、输入和导出；反复重跑的流程提供 `run_all.sh`、Snakemake、Nextflow 或同等入口。
7. 交付脚本、命令、输入、输出、环境、关键参数、验证、caveat 和复现级别；不得从局部指标升级功能、机制或临床 claim。

## 复现级别

- `exploratory`：允许快速试验，但记录输入、命令、输出和不稳定参数。
- `stable`：显式参数、固定输出、环境版本、验证和 caveat，可被后续图表或报告复用。
- `submission-ready`：主结果可从文档化入口重建，脚本、日志、source data、环境和版本可追踪。

## 按需资源

- 执行前后检查、smoke test 和稳定输出 bundle：读取 [local-first-execution-checklist.md](references/local-first-execution-checklist.md)。
- Omics 输入、坐标、版本、随机性和任务级执行契约：读取 [omics-execution-contract.md](references/omics-execution-contract.md)。
- 探索、稳定、投稿级代码要求与 leakage 检查：读取 [reproducibility-levels.md](references/reproducibility-levels.md)。
- 多步骤编号、notebook 收敛和 pipeline 层级：读取 [workflow-numbering.md](references/workflow-numbering.md)。
- 面向外部读者的复现包、manifest 和排除项：读取 [report_reproducibility_package.md](references/report_reproducibility_package.md)。
- 实现通用结构预测到 docking 的 QC 与结果解析时：读取 [protein_structure_docking_workflow.md](references/protein_structure_docking_workflow.md)。
- 预测结构作为 docking 输入、需要更细的模型质量门控时：读取 [protein_structure_prediction_docking_workflow.md](references/protein_structure_prediction_docking_workflow.md)。

最终回复先给已实现结果，再列精确文件、命令、输入输出、验证边界、caveat 和未解决风险。
