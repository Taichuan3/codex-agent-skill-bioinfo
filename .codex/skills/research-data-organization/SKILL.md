---
name: research-data-organization
description: 用于生信项目 CCDS（Cookiecutter Data Science）整理、当前/priority artifact 盘点与 manifest 维护、迁移规划；排除普通绘图、单目录 README、单纯 source-data 追溯，未授权不移动/删除。
---

# Research Data Organization

## 核心问题

如何让项目数据、结果、图表和 latest 文件入口清楚，避免未来找不到或用错版本？

## 目标

- 让当前有效的数据、结果、图表和投稿材料具有浅层、可验证的入口。
- 让每个重要 artifact 能追踪到输入、producer、consumer、统计定义和当前状态。
- 在不破坏既有工作流的前提下，给出可逐步执行和回滚的结构改进方案。

## 权限与边界

- 先锁定模式：`read-only audit`、`documentation/index cleanup`、`migration plan` 或用户已授权的 `physical move`。
- 原始数据只读；不得静默改变样本、阈值、参考版本、统计定义或执行环境。
- `read-only audit` 只在回复中报告，不创建 catalog、manifest、README、索引或临时审计文件。
- 未获明确授权时，不移动、重命名、删除、覆盖或归档现有 artifact；`keep`、`archive`、`deprecated` 等只是候选状态。
- 已确认的错误派生结果可在获得授权后原位修正；不同分析定义或版本应分支保存，并让 manifest 明确指向当前有效版本。
- 项目 `AGENTS.md` 声明的真实路径优先于默认 CCDS 布局；不要为了目录美观强制迁移成熟项目。
- 大型服务器数据优先保留原位，用 manifest、索引和可重复命令提供入口，避免无收益复制。

## 工作流程

1. 读取适用的项目 `AGENTS.md`、`PROJECT_GUIDE.md` 和用户指定入口；扫描大型目录前先读对应 Directory Card。
2. 限定盘点范围，先检查目录树、文件数量、大小、格式和少量样本；不要默认遍历整台机器或全部服务器数据。
3. 识别主报告、当前图表、关键表格、source data、producer、consumer 和已知版本入口。
4. 从 loader、workflow、report link 或生成脚本核验消费关系；不能仅凭 README、文件名或“文件存在”断言当前分析已使用。
5. 区分 current snapshot、as-of/time-valid candidate、verified historical/as-of-valid、release-lag proxy、unversioned snapshot 和 not assessed；历史日期列不等于当时可见。
6. 设计最小改进：优先补充 manifest、latest/priority 入口、source-data 映射和少量 Directory Cards，再考虑物理重排。
7. 涉及路径变化时，先生成 migration map、consumer 兼容方案、验证项和回滚路径；除非用户已明确授权，否则停在 plan。
8. 获得授权并完成移动后，核验目标路径、脚本和报告链接、兼容入口、Git 状态及 manifest；不要用工具日志代替业务验证。
9. 先汇报围绕主任务完成的结构改进，再列精确路径、验证边界、剩余风险和下一项需要用户决定的动作。

## 路由与组合

- 只维护一个重要目录的短 README 时，改用 `project-directory-card-maintenance`。
- 只处理 PROJECT_GUIDE/PROJECT_PLAN 状态时，改用 `project-state-maintenance`。
- 只审计论文 figure/table 的 source-data 完整性时，组合或改用 `source-data-audit`。
- 只进行图形设计、绘制或 visual QA 时，改用 `publication-plotting`。

## 模式化输出

- `read-only audit`：给出范围、当前结构、可验证发现、建议入口、风险和未决问题；不得创建文件。
- `documentation/index cleanup`：列出创建或更新的 manifest、README/index、latest/priority 入口及精确路径，并说明未改变哪些路径。
- `migration plan`：提供 `source_path`、`target_path`、`move_type`、`reason`、link/script impact、compatibility action、status、verification 和 rollback。
- `physical move`：报告实际移动、保留和兼容路径，更新后的索引，以及链接、脚本、Git 和可重复性验证结果。
- `unsafe destructive request`：不执行直接删除或无检查清理；先解析精确目标、只读盘点依赖与可恢复性，提出保留/归档/迁移方案，并等待针对该动作的明确授权。

项目侧组织文档默认使用中文，正式英文稿件、代码和 API 字段除外。广泛整理后，必须在回复中直接概括当前布局、移动或保留内容、source-data/report 状态、风险和下一决策，不能要求用户自行打开文件才能理解结果。

## 按需读取

- 新项目、CCDS 采用、整体结构设计或“找不到文件”时，读取 `references/cookiecutter-data-science-layout.md`。
- 设计 manifest、latest/priority 入口或投稿前材料索引时，读取 `references/layout-and-manifest.md`。
- 多步骤产物需要阶段编号和 stage-to-output 映射时，读取 `references/numbered-output-layout.md`。
- 成熟项目需要核验 consumer、time-valid 状态、registry 或 migration map 时，读取 `references/metadata-first-project-audit.md`。
- 成熟项目已进入物理重排评估或执行时，再读取 `references/ccds-rearrangement-checklist.md`。
