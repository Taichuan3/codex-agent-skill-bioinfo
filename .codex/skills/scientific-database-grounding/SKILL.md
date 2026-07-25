---
name: scientific-database-grounding
description: 用于查询、解析和交叉核验生物医学科学数据库中的 gene、variant、interval、expression、protein、structure、compound、target、disease、trial 或 publication 记录，保留 ID、版本、坐标、查询参数、证据类型和访问日期；不用于开放式文献综述、指定论文精读、分析代码实现或仅审查文本 claim。
---

# Scientific Database Grounding

## 核心问题

如何把实体身份与研究判断落到可重放、可交叉核验的数据库记录上？

## 能力边界

- 本 Skill 拥有 entity resolution、database lookup、record reconciliation 和 database-evidence provenance。
- 开放式寻找与综合论文集合时，改用 `literature-search-workflow`；精读指定论文时改用 `paper-reader`。
- 只验证参考文献身份或 claim-to-citation 时，改用 `citation-verifier`。
- 写查询脚本、批量 ETL 或下游分析时，以 `bioinfo-analysis-code` 为主，本 Skill 仅规定来源与字段契约。
- 审查文字是否 overclaim 时，改用 `claim-evidence-audit`；结构、docking 或 ADMET 结论仍由各领域 Skill 负责。
- 数据库记录只能证明“该来源在该版本/日期存在此记录或预测”，不能自动证明机制、因果、疗效或安全性。

## 查询边界

- 先解析 species、ID namespace、assembly/transcript/isoform、disease ontology、compound identifier 和用户未确认项。
- 只选择能回答问题的最小 1–4 个来源；官方 API/下载表优先于 aggregator 或网页摘要。
- 记录 endpoint、query/body、filters、fields、pagination、limit、release/访问日期和记录数；先 count/小样本，再扩大。
- 不读取或输出 token、cookie、header 或 `.env` 内容；只报告凭据是否可用。
- 空结果不等于实体不存在；记录查询范围、失败、rate limit 和替代来源。
- 不静默合并不同 build、allele、strand、transcript、isoform、species、assay、unit 或 evidence code。

## 工作流程

1. 定义 retrieval question、实体类型、输入 ID、上下文与目标字段。
2. 选择 primary source 和必要 cross-check，记录为何每个来源能回答问题。
3. 运行 count/summary 或小范围查询，检查命中实体、结果规模和分页。
4. 获取最少字段，保留原始 identifier、版本、query provenance 和 record count。
5. 核验别名、坐标/allele、transcript/isoform、organism、assay/unit、evidence status 和日期。
6. 列出跨来源 agreement、conflict、unresolved mapping 和 release lag；不得用较方便的来源覆盖冲突。
7. 输出 database record–claim–evidence type–caveat 映射；需要下游分析时提供明确 handoff 字段。
8. 若写入报告或 source data，保存可重放 query/command、字段定义和访问日期。

## 按需读取

- 需要选择 genetics、regulatory、expression、protein、structure、compound 或 literature metadata 来源时，读取 `references/database-source-map.md`。
- 需要设计 API query、ID 解析、字段裁剪、分页、限流、凭据安全或冲突核验时，读取 `references/database-query-contract.md`。

## 交付契约

至少交付 retrieval question、databases、exact identifiers/query parameters、version/date、record counts、selected fields/records、agreement/conflict、evidence type、caveats 和未解决映射。未实际查询时标记 `planned query`，不得提供伪造记录。
