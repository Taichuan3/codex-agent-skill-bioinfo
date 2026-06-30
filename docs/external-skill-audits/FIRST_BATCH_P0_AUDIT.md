# First Batch External Skill Repo Audit

> 分支：`Hermes-review`。本报告为第一批外部高质量 skill / agent 仓库的只读审计。仓库已浅克隆到 `~/.hermes/tmp/external-skill-sources/` 用于学习结构；未复制到 `~/.hermes/skills/`，未合并到 main。

## 审计批次

本批次选择 P0 中与用户背景和 Hermes/bioinfo 体系最相关的 4 个仓库：

1. `Yuan1z0825/nature-skills`
2. `google-deepmind/science-skills`
3. `K-Dense-AI/scientific-agent-skills`
4. `ClawBio/ClawBio`

## 本地只读下载位置

```text
/Users/yajiehu/.hermes/tmp/external-skill-sources/Yuan1z0825_nature-skills
/Users/yajiehu/.hermes/tmp/external-skill-sources/google-deepmind_science-skills
/Users/yajiehu/.hermes/tmp/external-skill-sources/K-Dense-AI_scientific-agent-skills
/Users/yajiehu/.hermes/tmp/external-skill-sources/ClawBio_ClawBio
```

这些目录只是临时学习/审计缓存，不是 source of truth。

## 1. Yuan1z0825/nature-skills

- URL: https://github.com/Yuan1z0825/nature-skills
- Local commit: `af29cdd`
- License: `Apache-2.0`
- Stars snapshot: `24433`
- `SKILL.md`: `14`
- 核心定位：面向科研写作、Nature 风格表达、文献、引用、绘图、审稿、返修、proposal、paper-to-PPT/patent 的中文科研 skill 包。

### 观察到的 skill 模块

```text
nature-academic-search
nature-citation
nature-data
nature-downloader
nature-figure
nature-literature-pipeline
nature-paper-to-patent
nature-paper2ppt
nature-polishing
nature-proposal-writer
nature-reader
nature-response
nature-reviewer
nature-writing
```

### 高价值可吸收内容

- `SKILL.md` 作为 router，长规则拆到 `static/`、`references/`、共享目录的架构思想。
- 科研写作、审稿回复、figure、citation、data availability 的完整任务链。
- 对中文科研用户友好的输出合同和操作型工作流。
- 对重复科研劳动进行 skill 化的设计哲学。

### 与现有 bioinfo skills 的关系

- 与 `paper-reader`、`literature-search-workflow`、`scientific-english-polishing`、`publication-plotting`、`claim-evidence-audit` 高度重叠。
- 不建议整包迁移；建议吸收架构与 workflow 表达，而不是替换现有 bioinfo skills。
- 可新增或增强：`figure-caption`、`reviewer-response-builder`、`source-data-audit`、`submission-readiness-audit`。

### 风险

- 可能过度 Nature/CNS 化，导致普通生信任务表达过强。
- 中文科研写作习惯明显，若迁移到通用 skill 需保留用户偏好但避免过度泛化。
- 部分模块偏 heavy workflow，如 paper-to-patent、PPT，不应优先进入核心 runtime。

### 建议

- **吸收等级：Core architecture + selective workflow**。
- 优先学习 router / shared / references 分层和科研输出合同。
- 不直接复制完整 skill；以用户现有 bioinfo skill 为主，逐步补充高价值 references。

## 2. google-deepmind/science-skills

- URL: https://github.com/google-deepmind/science-skills
- Local commit: `33557e0`
- License: `Apache-2.0`
- Stars snapshot: `2128`
- `SKILL.md`: `37`
- 核心定位：科学数据库与工具 grounding skills，覆盖 genomics、structural biology、cheminformatics、literature search。

### 观察到的高相关模块

```text
alphagenome_single_variant_analysis
alphafold_database_fetch_and_analyze
chembl_database
clinvar_database
dbsnp_database
encode_ccres_database
ensembl_database
gnomad_database
gtex_database
human_protein_atlas_database
interpro_database
jaspar_database
ncbi_sequence_fetch
uniprot_database
literature_search_arxiv / biorxiv / europepmc / openalex
```

### 高价值可吸收内容

- 对数据库调用的 deterministic / provenance-rich 设计。
- 与用户 genetics / D20S16 主方向高度相关的 variant、gene、regulatory、protein database grounding。
- 与未来 AI drug discovery 扩展相关的 ChEMBL、AlphaFold DB、UniProt、InterPro。
- 可以作为 Hermes bioinfo skills 的“数据库访问参考层”，而不是写作层。

### 与现有 bioinfo skills 的关系

- 可增强 `literature-search-workflow`、`bioinfo-analysis-code`、未来 `variant-annotation-workflow`、`genetic-database-mining`。
- 当前用户 skill 更偏研究流程和写作；Science Skills 更偏数据源 grounding，互补性强。

### 风险

- 部分 skills 依赖 API key、`uv`、网络访问或特定工具安装。
- 直接迁移会增加工具依赖和失败面。
- 数据库版本、API 限流、terms of use 需要记录。

### 建议

- **吸收等级：High priority on-demand database grounding**。
- 优先建立一个本地 umbrella skill：`genetic-database-grounding` 或 `scientific-database-grounding`，内部 references 指向 AlphaGenome/ClinVar/dbSNP/gnomAD/GTEx/ChEMBL/UniProt 等。
- 不立即把 37 个 skill 全部放入 Hermes runtime；应按任务触发分组。

## 3. K-Dense-AI/scientific-agent-skills

- URL: https://github.com/K-Dense-AI/scientific-agent-skills
- Local commit: `0807ddb`
- License: `MIT`
- Stars snapshot: `29630`
- `SKILL.md`: `149`
- 核心定位：跨学科科学 agent skills 大库，覆盖 bioinformatics、genomics、drug discovery、chemistry、materials、databases、multi-omics 等。

### 观察到的高相关模块示例

```text
anndata
biopython
bioservices
bulk-rnaseq
cellxgene-census
citation-management
clinical-decision-support
clinical-reports
cobrapy
```

README 声称覆盖：

- Bioinformatics & Genomics
- Multi-omics & Systems Biology
- Drug-target binding / molecular workflows
- Scientific database lookup
- Scientific writing and reporting

### 高价值可吸收内容

- 用作“科学 skill 地图”和缺口发现工具。
- 可从中采样：single-cell、RNA-seq、multi-omics、drug-target、database lookup、citation-management。
- 对我们设计“AI for biology 未来扩展层”很有帮助。

### 与现有 bioinfo skills 的关系

- 大量内容与现有 `bioinfo-analysis-code`、`literature-search-workflow`、`publication-plotting`、未来 drug discovery skills 重叠。
- 更适合作为候选池，不适合直接 runtime 全量安装。

### 风险

- 规模大，质量可能不均。
- 可能混合了真实手写 skill、工具包装、自动生成或过宽 trigger。
- 149 个 skill 若直接导入会严重增加误触发和上下文管理负担。

### 建议

- **吸收等级：Reference pool + selective extraction**。
- 第二轮需要按主题抽样审计：`single-cell/RNA-seq`、`drug discovery`、`database lookup`、`citation-management`。
- 不建议直接复制到默认 Hermes runtime。

## 4. ClawBio/ClawBio

- URL: https://github.com/ClawBio/ClawBio
- Local commit: `fbb0910`
- License: `MIT`
- Stars snapshot: `1012`
- `SKILL.md`: `92`
- 核心定位：bioinformatics-native AI agent skill library，local-first、reproducible、带测试与 benchmark。

### 观察到的高相关模块示例

```text
affinity-proteomics
analyze-fasta
archaic-introgression
article-data-fetcher
bio-orchestrator
bioconductor-bridge
busco-assessor
clinical-variant-reporter
clinical-trial-finder
claw-ancestry-pca
claw-metagenomics
claw-methylation-cycle
```

README 强调：

- 90+ skills
- 部分 production-ready
- Galaxy tools integration
- benchmark validation
- local-first
- reproducible
- no guessing

### 高价值可吸收内容

- 与用户 bioinfo 方向最接近，尤其 local-first、reproducible、benchmark validation 的理念。
- 可学习如何把生信任务 skill 化，同时保持可执行和可验证。
- `clinical-variant-reporter`、`analyze-fasta`、`bio-orchestrator`、`bioconductor-bridge` 等值得二轮审计。

### 与现有 bioinfo skills 的关系

- 现有用户 skills 更偏科研项目管理、写作、证据、图表和轻量分析。
- ClawBio 更偏具体 bioinformatics execution skill，互补性强。
- 可用于补齐：variant annotation、FASTA/sequence、RNA-seq/scRNA-seq、clinical variant、Galaxy/bioconductor workflows。

### 风险

- 依赖 Python package `clawbio`、Galaxy tools、demo data 或具体 CLI。
- 直接迁移可能导致本地环境依赖复杂。
- 需要区分“可执行工具 skill”和“纯流程指导 skill”。

### 建议

- **吸收等级：High priority, execution-workflow reference**。
- 优先吸收 local-first / reproducibility / benchmark thinking。
- 不直接复制执行型 skill；先抽取为 Hermes references 或创建 wrapper skill，必要时再安装工具。

## 第一批总体结论

### 最值得立即吸收的不是具体文件，而是四类能力

1. **科研 skill 架构**：来自 `nature-skills`
   - router / manifest / static / references / shared
   - 输出合同和中文科研 workflow

2. **科学数据库 grounding**：来自 `science-skills`
   - AlphaGenome、ClinVar、dbSNP、gnomAD、GTEx、ChEMBL、UniProt、AFDB
   - provenance-rich 查询思路

3. **科学任务地图**：来自 `scientific-agent-skills`
   - bioinformatics / drug discovery / multi-omics / database lookup 的广覆盖候选池

4. **可复现生信执行**：来自 `ClawBio`
   - local-first、benchmark、demo、tests、no guessing

### 建议进入下一步的具体行动

1. 创建/增强 `genetic-database-grounding` 类 skill，吸收 `science-skills` 的数据库分层思路。
2. 为现有 `bioinfo-analysis-code` 增加 local-first / reproducibility / benchmark checklist，参考 ClawBio。
3. 为现有写作/图表/审稿 skills 增加 `nature-skills` 的 router 与输出合同模式，但避免过度 Nature 化。
4. 从 `scientific-agent-skills` 中按主题抽样审计，不全量迁移。

### 当前不建议做的事

- 不把 149/553/605 这类大规模 skill 库全量复制到 Hermes runtime。
- 不让外部 skill 覆盖用户已有 bioinfo 核心逻辑。
- 不启用自动 merge 或自动 runtime overwrite。
- 不把需要复杂依赖的 execution skill 直接变成默认触发 skill。

## 下一批建议审计

1. `NVIDIA-BioNeMo/bionemo-agent-toolkit`
2. `adaptyvbio/protein-design-skills`
3. `learningmatter-mit/AtomisticSkills`
4. `obra/superpowers`
5. `addyosmani/agent-skills`
