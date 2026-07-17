---
name: research-data-organization
description: 用于组织生物信息学项目的数据、表格、结果、图和常用文件路径，解决结果分散、最新文件不清、重要表格难找、投稿数据难汇总的问题。适用于建立目录结构、整理 latest/priority 文件、设计 manifest、迁移常用结果到一级目录或索引表。
---

# Research Data Organization

## 核心问题

如何让项目数据、结果、图表和 latest 文件入口清楚，避免未来找不到或用错版本？

## 使用场景

当用户抱怨结果文件太散、找不到最新表格、一个结果生成多个文件夹、投稿时不知道哪个表该上传，或要求整理项目数据目录时使用本 skill。

## 核心原则

- 数据要可追踪，也要容易读取。
- 先 metadata-first 盘点，再决定是否迁移；目录美观不能优先于 consumer compatibility 和 provenance。
- 任务明确指定为 read-only audit 时，只在回复中给出盘点和建议，不创建 catalog、manifest、README/index 或其他文件。
- 用户未明确授权 physical move、rename、delete 或 archive 时，可以按用户请求创建或更新非破坏性的 catalog、manifest、README/index 和 migration plan，但不得改变现有路径或删除/覆盖现有 artifact。
- `keep`、`toss`、`current`、`deprecated` 等分类是建议；删除、覆盖和物理移动由用户决定。
- 新项目或大版本重构时，默认参考 Cookiecutter Data Science / CCDS 思路：`data/raw` immutable、`data/interim` 中间数据、`data/processed` 分析就绪数据、`data/external` 第三方数据、`references` 数据字典/说明、`reports/figures` 输出图表、`src/` 可复用代码、`notebooks/` 探索记录、`Makefile`/workflow 作为入口。
- 原始数据保持只读；已确认结论的关键表格和高频文件要有清晰入口。
- 重要文件可以通过 `latest`、`priority`、`manifest`、Directory Card (`README.md`) 或一级目录索引暴露出来。
- 对稳定、会复用、会进论文或容易混淆的 artifact 目录，选择性维护短 `README.md` Directory Card；不要给每个 run、临时图或中间缓存写 README。
- 多步骤分析结果应使用阶段编号组织，例如 `01_preprocessing`、`02_qc`、`03_analysis`、`04_visualization`。编号应与脚本或 workflow step 对应。
- 关键结果文件名可包含阶段编号，便于判断产物来源和处理顺序，例如 `03_differential_expression.tsv`、`04_main_figure.svg`。
- 错误旧文件不需要永久保留在工作路径；可覆盖修正后的图表和派生表，但要保证最终 manifest 指向当前有效版本。
- 不用深层目录隐藏关键论文表格。

## 推荐结构

```text
results/
  01_preprocessing/
  02_qc/
  03_analysis/
  04_visualization/
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

1. 明确任务模式：read-only audit、documentation/index cleanup、migration plan 或用户已授权的 physical move。
2. 扫描或读取用户指定目录，不默认全盘读取；只读审计不创建 catalog、README 或其他文件，直接在回复中给出可复核结果。
3. 先建立 metadata-first catalog 设计，识别高频文件、已确认结论文件、投稿相关文件、过期文件、producer 和 consumer。
4. 从实际 loader、workflow、report links 或生成脚本核验消费关系；不能从 README、文件名或“文件存在”推断当前分析已使用。
5. 将数据标为 current snapshot、as-of/time-valid candidate、verified historical/as-of-valid、release-lag proxy、unversioned snapshot 或 not assessed；历史日期列不等于当时可见。
6. 建议浅层入口：priority tables、priority figures、source data、manifest 和选择性的 Directory Cards。
7. 若涉及路径变化，先输出 migration map 和 compatibility/verification plan；取得用户明确授权后才执行 physical move。
8. 对需要覆盖的修正图表或派生表，确认它们是错误修正还是新版本分支，并让 manifest 指向当前有效版本。

## 成熟项目 CCDS 重排规则

当用户要求按 Cookiecutter Data Science / CCDS 重排一个已有大型项目时，不要只做旁支清理、PDF/隐私修正或 verification 汇报后就停止。主任务应是让数据和 analyses 结构可理解、可导航、可逐步迁移。

推荐顺序：

1. 先明确用户要的是 `README/index cleanup`、`migration plan` 还是已明确授权的 `physical move`；未授权时停在 audit/plan。
2. 先做 no-move audit：确定 final report / manuscript 是主线，给 analyses 分成 primary report support、technical/provenance、supplementary/exploratory、raw/local-only、archive/provenance。
3. 移动文件前写 migration map，至少包含 `source_path`、`target_path`、`move_type`、`reason`、`report_link_impact`、`script_path_impact`、`compatibility_action`、`status`。
4. 成熟生信项目中，优先移动低风险顶层目录：legacy `figures/` -> `reports/figures/`、root `scripts/` -> `src/scripts/`、`sync_reports/`/`logs/` -> `metadata/`、release package -> `release/`。
5. raw/reference 数据可以移入 `data/raw/`，但如果旧脚本/文档依赖旧路径，应保留本地 compatibility symlink，并在 `.gitignore` 中忽略 symlink/large data。
6. 对编号 `analyses/` 和已交付 report bundle，默认先保留稳定路径；只有在第二阶段 migration map 和 link/script verification 准备好后再移动。
7. 移动后添加 targeted Directory Cards，而不是给所有 run 目录写 README。
8. 汇报时以主任务为中心：说明结构怎么变了、哪些路径保持稳定、验证了什么、还剩什么，不要让临时验证脚本路径成为主要内容。

详细清单见 `references/ccds-rearrangement-checklist.md`。

## 汇报要求

- 汇报要先说“围绕主任务完成了什么”，再列改动文件、验证结果和下一步；不要把临时验证脚本路径或工具日志放在主体。
- 如果系统要求 ad-hoc verification，只在“验证结果”中简洁说明通过了哪些业务检查，不要让验证回复替代主任务进展汇报。
- 当用户明确批评“你忘了主要任务 / 只做了补充”，立即回到主任务并交付实际目录整理 artifacts，而不是继续解释。

## 输出格式

- `Recommended layout`
- `Stage numbering`
- `Priority files`
- `Manifest fields`
- `Overwrite / archive decisions`
- `Next actions`

For this user's project-organization work, write project-facing organization docs in Chinese by default (`README.md`, Directory Cards, `PROJECT_GUIDE.md`, `PROJECT_PLAN.md`, audit/comparison notes) unless the user explicitly asks for English or the artifact is formal English manuscript/code/API text. After broad reorganizations, summarize the result in chat without requiring the user to open files: current layout, what moved/was kept, source-data/report status, risks, and next decision. If Hermes/Codex collaboration is expected, use Codex for a broad read-only scan or second-pass audit and compare its findings with Hermes's findings explicitly.

## 按需读取

需要设计目录、latest/priority 入口、manifest 字段或投稿前数据整理策略时，读取 `references/layout-and-manifest.md`。
需要把多步骤分析产物按处理顺序编号，或设计 stage-to-output 映射时，读取 `references/numbered-output-layout.md`。
新项目启动、大版本重构、或用户提到 Cookiecutter Data Science / CCDS / 找不到文件 / 数据管理混乱时，读取 `references/cookiecutter-data-science-layout.md`。
成熟项目需要盘点 artifact、核验实际 consumer、区分 as-of/time-valid 状态或设计 registry/migration map 时，读取 `references/metadata-first-project-audit.md`。
