---
name: source-data-audit
description: 用于构建或审查生物信息学论文 figure/table/panel 到 source file、producer、统计定义与 deposition/access route 的可追溯 inventory，并检查 numbers-to-lock、Data/Code Availability、FAIR-like metadata 和 repository readiness；不判定 claim 强度、稿件跨位置一致性、整套投稿 readiness 或 reviewer response。
---

# Source Data Audit

## 核心问题

如何让每个投稿图表和锁定数字都能追踪到当前有效 source data、生成过程、统计定义与真实可用的访问路径？

## 能力边界

- 建立或审查 figure/table/panel source-data inventory、numbers-to-lock 来源、repository/accession 和 Data/Code Availability。
- 只判断 claim 是否被证据支持时，交给 `claim-evidence-audit`；本 Skill 只报告 traceability 是否闭合。
- 只检查摘要、正文、图注、方法和表格中的数字/术语是否冲突时，交给 `manuscript-consistency-audit`。
- 需要整套投稿包综合 gate 时，交给 `submission-readiness-audit`。
- 预判审稿攻击或编排真实审稿回复时，分别交给 `reviewer-simulation` 或 `reviewer-response-builder`；本 Skill 只提供可追溯性证据。
- 项目级数据布局、latest/priority 入口或物理迁移交给 `research-data-organization`；单目录导航交给 `project-directory-card-maintenance`。

## 审计合同

- 锁定稿件版本、figure/table 清单和 inventory 范围；不默认扫描整个项目或大型 raw-data 目录。
- 为每个 panel/表记录 current source file、data state、producer/script、input、environment、统计定义、关键数字、caveat 和状态。
- 区分 raw、filtered、normalized、projected、manual-reviewed 与 plotted source data；不得静默合并层级。
- 从 producer、consumer、manifest、hash 或可重复命令核验 current 状态；不得仅凭文件名、日期或 README 断言。
- 为每个 dataset 指定 public repository、controlled access、within paper/supplement、reused public data、third-party restricted、justified request 或 not applicable。
- 只有存在伦理、法律、商业、第三方限制时才把 `available upon request` 作为主路径；否则应优先 repository/accession/DOI 或随文 source data。
- 不承诺尚未存在、未上传、未测试访问或受限条件未确认的数据/代码。
- 保持原始数据只读；对已确认的派生错误修正，只在用户授权后更新 current 指针并记录 correction。

## 工作流程

1. 读取稿件/figure map、现有 manifest 和用户指定入口；大型目录先读 Directory Card。
2. 枚举 figure/table/panel 与 numbers-to-lock，建立一行一对象的审计表。
3. 核验 source file、producer、input、统计/转换、环境与 consumer；标记 `verified`、`missing`、`ambiguous` 或 `not assessed`。
4. 检查列名、单位、identifier、样本/过滤状态、license、version、access date 与 reuse restriction。
5. 核对 repository/accession/DOI、private-review link 和 Data/Code Availability 的真实性。
6. 将缺失项按 central-claim impact 与修复依赖排序；把科学支持判定转交 `claim-evidence-audit`。
7. 如获授权更新 inventory，报告精确路径与校验；不移动 raw data 或静默替换分析定义。

## 输出合同

| Figure/Table | Panel | Source file | Data state | Producer | Statistics | Access route | Status | Required action |
|---|---|---|---|---|---|---|---|---|

同时给出 numbers-to-lock、Data/Code Availability truth check、blocking gaps、未扫描范围和下一责任人。

## 按需读取

- 设计 manifest 字段、FAIR-like 检查或 dataset README 时，读取 [fair-manifest.md](references/fair-manifest.md)。
- 规划 repository、accession、DOI、受限数据、复用公共数据或 reviewer access 时，读取 [repository-readiness.md](references/repository-readiness.md)。

最终回复先给阻断性 traceability 缺口，再给 inventory/availability 状态、精确文件、验证边界和下一步。
