---
name: literature-search-workflow
description: 用于生物信息学与计算生物学问题的可复现文献集合检索、检索式与纳排标准设计、筛选记录、证据表、共识/争议/知识缺口和决策性 evidence map；适用于项目启动、方法比较、背景补证和寻找公共数据，不用于精读指定单篇论文、数据库实体 lookup 或仅核验现有 citation。
---

# Literature Search Workflow

## 核心问题

如何把开放式研究问题转成可复查的 paper set、证据地图和下一步决策？

## 能力边界

- 本 Skill 拥有 literature discovery、query design、screening、paper-set synthesis 和检索层面的 gap map。
- 用户指定一篇或固定少量论文并要求精读时，改用 `paper-reader`。
- 只查 gene/variant/protein/compound 等数据库记录时，改用 `scientific-database-grounding`。
- 只核验现有 DOI/PMID/参考文献及其 claim support 时，改用 `citation-verifier`。
- 从现有项目结果或稿件决定最小补分析时，改用 `evidence-gap-finder`；逐句审查 overclaim 时改用 `claim-evidence-audit`。
- 检索可提出候选数据集或实验，不执行下载、重分析、湿实验或最终 go/no-go 科研决策。

## 检索与证据边界

- 先定义 1–3 个可回答问题，再选择关键词、来源和时间范围。
- 记录数据库、完整检索式、检索日期、过滤器、命中数、去重规则和纳排理由；结果过大时先抽样检查命中质量。
- 优先使用领域数据库、期刊/预印本平台和可核验 metadata source；不编造 DOI、PMID、作者、年份或结论。
- metadata 或摘要只能支撑题录与有限摘要信息；需要方法、结果或 claim support 时核对全文、图表或补充材料。
- 空结果表示“在记录的范围内未检出”，不等于证据不存在。
- 区分 primary research、review、preprint、dataset record 和 database annotation；区分 evidence、interpretation、limitation 和 speculation。

## 工作流程

1. 写出 decision question、PICO/PECO 或 entity–context–method 框架，并标记未知项。
2. 构建 concept blocks、同义词、物种/组织/assay/方法变体和排除词；先运行窄查询检查相关性，再扩展。
3. 选择最小来源集合，记录可重放 query 和检索日期；必要时采用 citation chaining。
4. 建立去重和 screening 记录，保存 title/abstract 与 full-text 两阶段纳排理由。
5. 对纳入文献提取 study design、dataset、method、comparison、supported claim、limitation、resource 和 relevance。
6. 综合 consensus、controversy、method/data gap、可复用资源和证据不足处；不要按论文逐篇堆摘要。
7. 给出 `follow`、`reproduce`、`avoid`、`cite_only`、`data_source` 或 `method_reference` 等建议，并把研究方向决策交给用户。
8. 报告检索覆盖、访问限制、未核验全文、时间截点和下一轮最有价值的检索。

## 特殊检索路由

- 需要标准 evidence table 时读取 `references/evidence-table-template.md`。
- 需要为项目决策建立 dataset/method/gap map 与 go/no-go memo 时读取 `references/evidence-map-matrix.md`。
- 需要连接 repeat-rich locus 假说、不同证据层和公共数据 accession 时读取 `references/repeat-locus-literature-search.md`。
- 需要检索蛋白互作、突变依据或 docking feasibility 时读取 `references/protein-interaction-literature-search.md`。

## 交付契约

至少交付 search questions、sources、exact search strings、date、inclusion/exclusion、screening counts、evidence table、synthesis、coverage limitations 和 next papers/actions。若任务仅为策略设计而未实际检索，明确标记 `planned`，不得把示例命中写成检索结果。
