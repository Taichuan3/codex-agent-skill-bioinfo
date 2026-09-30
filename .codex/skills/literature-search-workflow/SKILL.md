---
name: literature-search-workflow
description: 检索并综合生物信息学论文集合：检索式、纳排、筛选、证据表与知识缺口。指定论文精读→paper-reader；实体查询→scientific-database-grounding；仅核验引用→citation-verifier。
---
# Literature Search Workflow
## 核心问题
如何将开放问题转成可重查的 paper set、证据地图与下一步决策？
## 边界
拥有 query、screening、dedup、paper-set synthesis；现有结果的补分析→evidence-gap-finder，逐句 overclaim→claim-evidence-audit。只提出候选资源/实验，不下载、重分析、实验或替用户决定 go/no-go。
## 流程与交付
1. 限定 1–3 个问题、entity/context/method（可用 PICO/PECO）、未知项、时间范围；构建概念块/同义词/排除词，先窄查询检查命中，再扩展，必要时 citation chaining。
2. 选择最小权威来源集；保留来源、完整 query、日期、过滤器、命中/筛选数、去重规则和 title/abstract/full-text 两阶段纳排理由。结果过大先抽样。
3. evidence table 保留 study design、data、method/comparison、supported claim、evidence location、limitation、resource/relevance。不得编造题录；摘要/metadata 不支撑未核验全文细节。区分 primary/review/preprint/dataset/annotation 及 evidence/interpretation/limitation/speculation。
4. 综合共识、争议、method/data gap，给 follow/reproduce/avoid/cite_only/data_source/method_reference 建议，由用户决策。报告覆盖、访问限制、未核全文、时间截点与 next papers/actions；未运行检索标 planned，空结果仅表示本范围未检出。
## 执行后端
实际检索读取 `../capability_registry.json` 的 `CAP-LIT-001`；优先已安装 source-specific PubMed/PMC/bioRxiv，本 Skill 保留科学与综合所有权。仅有稳定全文集且需重复问答才试 PaperQA2，小集已知答案验证引用定位、无依据陈述、缺文、隐私与成本。registry 不授权安装、API key 或上传论文；后端不可用交可重放 search plan。

## 特殊检索路由

- 需要标准 evidence table 时读取 `references/evidence-table-template.md`。
- 需要为项目决策建立 dataset/method/gap map 与 go/no-go memo 时读取 `references/evidence-map-matrix.md`。
- 需要连接 repeat-rich locus 假说、不同证据层和公共数据 accession 时读取 `references/repeat-locus-literature-search.md`。
- 需要检索蛋白互作、突变依据或 docking feasibility 时读取 `references/protein-interaction-literature-search.md`。

## 交付契约

至少交付 search questions、sources、exact search strings、date、inclusion/exclusion、screening counts、evidence table、synthesis、coverage limitations 和 next papers/actions。若任务仅为策略设计而未实际检索，明确标记 `planned`，不得把示例命中写成检索结果。
