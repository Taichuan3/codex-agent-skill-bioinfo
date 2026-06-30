---
name: scientific-database-grounding
description: 用于生物信息学研究中需要查询或核验科学数据库时，围绕基因、变异、调控元件、表达、蛋白结构、化合物、药物靶点和文献记录建立可追踪的 database grounding。适用于 AlphaGenome/ClinVar/dbSNP/gnomAD/GTEx/ENCODE/Ensembl/UniProt/AlphaFold DB/ChEMBL/PubMed 等数据库查询、交叉核验和 provenance 记录；不用于普通文献阅读或无数据库需求的写作润色。
---

# Scientific Database Grounding

## 核心问题

如何把基因、变异、区间、蛋白、化合物或文献判断落到可追踪数据库记录上？

## 使用场景

当任务需要把研究判断落到外部科学数据库记录时使用本 skill，例如：

- 查询 gene、variant、rsID、genomic interval、regulatory element 或 expression evidence。
- 核验 ClinVar、dbSNP、gnomAD、GTEx、ENCODE、Ensembl、UCSC、AlphaGenome 等数据库中的坐标、版本、等位基因或组织/细胞类型信息。
- 查询蛋白、domain、structure、UniProt、AlphaFold DB、InterPro、PDB 或 ligand/drug target 关联。
- 查询 ChEMBL、DrugBank-like public information、Open Targets、PubMed、EuropePMC、bioRxiv、OpenAlex 等，建立 target/compound/literature evidence map。
- 需要把数据库结果写入 report、Methods、source data、caveat 或审稿回复。

不要用于：

- 用户只要求阅读一篇论文：用 `paper-reader`。
- 开放式系统文献检索：用 `literature-search-workflow`，本 skill 只补 database grounding。
- 写脚本或跑分析：主 skill 是 `bioinfo-analysis-code`，本 skill 只提供数据库来源和核验要求。

## 核心原则

- 数据库记录必须带来源、版本或访问日期。
- 不把数据库注释当成实验验证；区分 curated、predicted、inferred、literature-derived 和 model-predicted evidence。
- 坐标必须记录 genome build；variant 必须记录 reference/alternate allele、strand 和 transcript context。
- 蛋白和结构记录必须区分 canonical isoform、model structure、experimental structure 和 predicted confidence。
- 药物/靶点信息必须区分 binding evidence、clinical association、repurposing hypothesis、ADMET prediction 和 approved indication。
- API 或网页结果失败时不要编造；改用替代数据库、离线文件或说明 blocker。

## 执行流程

1. 定义实体：gene/variant/interval/protein/compound/literature question 是什么，记录用户给定 ID 和不确定项。
2. 选择最小数据库集合：只查能回答当前问题的 2–4 个核心来源。
3. 记录查询参数：ID、genome build、transcript、species、API endpoint、date、filters。
4. 交叉核验冲突：如果数据库之间坐标、名称、版本或解释不一致，列出冲突，不静默选择一个。
5. 输出 evidence map：把 database record、claim、support level、caveat 和后续验证需求对应起来。
6. 若结果进入报告或论文，生成可追踪表格或 source-data 片段。

## 推荐数据库分层

按需读取 `references/database-source-map.md`，根据任务选择来源；涉及 NCBI 查询时使用其中的 Entrez ESearch/ELink/ESummary/EFetch 记录规则。

## 输出格式

- Question / entity
- Databases queried
- Query parameters and date
- Key records
- Cross-database agreement/conflict
- Evidence level: Strong / Moderate / Exploratory / Speculative
- Caveats
- Suggested next analysis or validation

## 与其他 skill 的关系

- 与 `literature-search-workflow`：文献检索负责研究背景和 paper set；本 skill 负责数据库记录和 ID grounding。
- 与 `bioinfo-analysis-code`：代码 skill 负责执行和表格处理；本 skill 负责查询来源、字段含义和 provenance。
- 与 `claim-evidence-audit`：claim 审查负责判断文字是否越界；本 skill 提供数据库证据表。
- 与 `protein-structure-docking` / `drug-discovery-admet-screening`：结构、docking、target validation 或 ADMET 任务需要数据库 grounding 时，先用本 skill 锁定 protein/compound/target/literature 输入定义。
