# journal_codex_AGENT v1.4 Skill 合规审计

审计日期：2026-05-19

## 结论

- 26 个通用 skill 均通过官方 `quick_validate.py`。
- 26 个 skill 均已补充 `agents/openai.yaml`，用于 Codex UI 元数据展示。
- 每个 skill 均包含 `SKILL.md`、frontmatter `name` 和 `description`。
- skill 文件夹名与 frontmatter `name` 完全一致。
- 未发现阻断发布的 P0 合规问题。
- v1.4 未新增科研功能 skill；本轮新增包级 workflow 指导文档，并把若干流程要求下沉到现有 skill references。

## 校验方式

使用临时 Python 环境运行官方校验脚本：

```bash
python -m venv /tmp/journal_codex_agent_validate
/tmp/journal_codex_agent_validate/bin/python -m pip install --upgrade pip pyyaml

for d in journal_codex_AGENT/.codex/skills/*; do
  /tmp/journal_codex_agent_validate/bin/python \
    ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done
```

`agents/openai.yaml` 使用官方生成脚本补齐：

```bash
~/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py
```

## 26 个 Skill 审计表

| Skill | Trigger precision | Context efficiency | Progressive disclosure | Research integrity | Maintainability | Hard gate | 后续改进 |
|---|---|---|---|---|---|---|---|
| `bioinfo-analysis-code` | Good：限定脚本、表格、统计、环境和代码整理 | Good：正文短，复杂规范放入 references | Good：已有 references | Good：强调输入、输出、环境、caveat、阶段编号、ML 泄漏检查和负结果记录 | Good | Pass | 后续可补 Snakemake/Nextflow 示例 reference |
| `chinese-scientific-polishing` | Good：明确只做中文润色，不做翻译 | Good | Good：已有 references | Good：保护证据边界和章节功能 | Good | Pass | 可补更多摘要/引言/结果段示例 |
| `citation-verifier` | Good：限定引用、DOI、PMID、BibTeX 和 claim-to-citation | Good | Good：已有 references | Excellent：防止引用幻觉和 citation mismatch | Good | Pass | 可补自动 BibTeX 清洗脚本 |
| `claim-evidence-audit` | Good：已限定论文写作、结果、图注、回复和投稿前检查 | Good | Fair：暂无 references | Excellent：核心就是 claim-evidence-caveat | Good | Pass | P2：增加 claim 降级模板和审稿风险例表 |
| `evidence-gap-finder` | Good：限定已有结果/草稿中的缺失证据和最小补分析 | Good | Good：已有 references | Excellent：避免无限扩展和 overclaim | Good | Pass | 可补 gap-to-skill 路由表 |
| `environment-and-tool-adoption` | Good：限定安装缺失包、采用外部工具和避免重复造轮子 | Good | Good：已有 references | Good：要求版本、来源、license 和适配记录 | Good | Pass | P2：补 license 风险分级表 |
| `figure-caption` | Good：限定图题、panel title、legend、caption 和 figure-to-claim | Good | Fair：暂无 references | Good：要求 source data/caveat 表达 | Good | Pass | P2：增加 main/supplementary caption 模板 |
| `literature-search-workflow` | Good：限定系统文献检索和证据表，不读单篇论文 | Good | Good：已有 references | Excellent：要求检索式、筛选标准和证据表 | Good | Pass | 可补 PubMed/CrossRef 查询脚本 |
| `manuscript-consistency-audit` | Good：限定数字、术语、图号、样本集合一致性 | Good | Good：已有 references | Excellent：以 source data/locked table 为权威 | Good | Pass | 可补 number extraction 辅助脚本 |
| `paper-reader` | Good：限定用户指定论文阅读，不做开放式检索 | Good | Good：已有 references | Good：区分作者结论、证据和可借鉴方法 | Good | Pass | 可补 PDF extraction workflow |
| `project-environment-bootstrap` | Good：限定新项目、切换机器/目录、环境未知或缺少环境文件；明确日常任务不触发 | Good：正文短，细节放入 references | Good：已有 references | Good：保护本地环境文件和 GitHub 同步隐私边界 | Good | Pass | 可补不同平台自动检测脚本 |
| `project-guide-maintainer` | Good：限定轻量 `PROJECT_GUIDE.md` 维护 | Good | Good：已有 references | Good：避免长上下文，保留主线、五句话框架、证据包、阶段状态和 reviewer attack | Good | Pass | 可加入 `PROJECT_GUIDE.md` 自动压缩模板 |
| `publication-plotting` | Good：限定 manuscript-ready/PPT 可读图和 QA | Good | Good：已有 references | Good：figure contract、source data、遮挡检查 | Good | Pass | 可补不同图型的字号和导出 preset |
| `research-data-organization` | Good：限定结果分散、latest/priority、manifest、阶段编号和投稿数据整理 | Good | Good：已有 references | Good：关注可追踪、当前有效版本、浅层入口和 workflow step 映射 | Good | Pass | 已补 `numbered-output-layout.md`；后续可补自动 manifest 模板 |
| `research-decision-review` | Good：明确需先理解背景，高影响决策才触发 | Good | Good：已有 references | Excellent：避免盲目反对，要求替代方案 | Good | Pass | 可补“何时不触发”反例 |
| `research-project-planner` | Good：限定项目启动、背景调查、技术路线和可检验假设 | Good | Good：已有 references | Good：强调选题卡、五句话框架、证据包和可复现计划 | Good | Pass | 可接入后续文献检索 skill |
| `research-question-brief` | Good：限定口头想法转短 brief | Excellent：目标就是压缩上下文 | Good：已有 references | Good：保留目标、边界、证据需求 | Good | Pass | 可补 brief 更新 diff 模板 |
| `reviewer-response-builder` | Good：限定真实审稿意见和返修回复，不做风险模拟 | Good | Good：已有 references | Good：每条回复对应行动、证据或边界 | Good | Pass | 可补 response letter 总模板 |
| `reviewer-simulation` | Good：限定论文审稿风险和 response strategy | Good | Fair：暂无 references | Good：强调证据链、统计、复现、机制风险 | Good | Pass | P2：增加审稿人类型和 response priority 模板 |
| `scientific-english-polishing` | Good：明确已有英文润色，不做中文翻译 | Good | Good：已有 references | Good：不能升级 claim | Good | Pass | 可补不同期刊语气强度模板 |
| `scientific-english-translation` | Good：明确中文到英文翻译，不负责中文润色 | Good | Good：已有 references | Good：证据边界安全 | Good | Pass | 可补术语表接口 |
| `skill-quality-audit` | Good：限定本地 skill 质量审计 | Good | Good：已有 references | Good：包含安全和科研诚信边界 | Good | Pass | 可补打分 rubric |
| `source-data-audit` | Good：限定 inventory、availability、FAIR-like metadata | Good | Good：已有 references | Excellent：可追踪性核心 skill | Good | Pass | 可补投稿数据仓库 checklist |
| `submission-readiness-audit` | Good：限定投稿前或大版本收尾综合预检 | Good | Good：已有 references | Excellent：跨主文、图表、方法、数据、代码、引用和 reviewer attack list | Good | Pass | 可补 journal-specific checklist |
| `task-self-check` | Good：限定交付前轻量 QA | Good | Good：已有 references | Good：覆盖 evidence、file、code、figure、text 和 phase-aware 检查 | Good | Pass | 可补“轻量/深度 QA”分流表 |
| `validation-strategy-planner` | Good：限定探索性结果和候选机制的验证路线 | Good | Good：已有 references | Excellent：区分计算、外部数据、统计、实验和降级写法 | Good | Pass | 可补不同 omics 的验证案例 |

## `agents/openai.yaml` 检查

每个 skill 已包含：

```text
agents/openai.yaml
```

`interface` 字段下均包括：

- `display_name`
- `short_description`
- `default_prompt`

其中 `default_prompt` 均包含对应 `$skill-name`，便于 Codex UI 中直接调用。

## 本轮未修改的内容

- v1.2 已新增 `paper-reader`、`literature-search-workflow`、`citation-verifier`、`submission-readiness-audit`、`manuscript-consistency-audit`、`reviewer-response-builder`、`evidence-gap-finder`、`validation-strategy-planner`。
- 未引入旧专案 profile、旧专案 skill 或任何专案事实。
- 未把外部高星仓库内容直接复制进包内。
- 根 `AGENTS.md` 仍保持短路由；新增功能只作为 skill 路由，不展开长流程。

## v1.4 新增审计结论

- `docs/RIGOROUS_COMPUTATIONAL_RESEARCH_WORKFLOW_GUIDE.md` 已作为包级指导文件，承接原 `rigorous_research_workflow_computational_biology.md` 中的完整研究生命周期。
- `docs/WORKFLOW_COVERAGE_AUDIT.md` 已记录原文 0-12 个模块与当前 skill 的覆盖关系。
- `research-data-organization` 已完成阶段编号、priority/latest 入口、manifest 字段和覆盖/归档规则的本地化适配。
- 根 `AGENTS.md` 未扩写，符合“根入口短、细节下沉 skill/reference”的原则。

## 后续优先改进建议

1. 根据真实项目需求补 RNA-seq、single-cell、ATAC-seq、GSEA、variant/GWAS 等专项包。
2. 为 `citation-verifier`、`manuscript-consistency-audit` 补轻量 extraction/format 脚本。
3. 为 `publication-plotting` 补不同图型的字号、导出和配色 preset。
4. 为 `reviewer-simulation` 和 `reviewer-response-builder` 补 response priority 与 response letter 模板。
