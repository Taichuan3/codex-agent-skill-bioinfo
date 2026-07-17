---
name: literature-search-workflow
description: 用于生物信息学或计算生物学项目的系统文献检索、关键词设计、数据库选择、纳入排除标准、证据表和知识缺口整理。适用于项目启动、补证据、查找方法依据或为论文背景寻找文献；不用于阅读单篇指定论文。
---

# Literature Search Workflow

## 核心问题

如何把开放式文献问题转成可复现检索式、筛选标准、证据表和知识缺口？

## 使用场景

当用户需要查找一组文献、建立背景证据、比较方法或补充引用时使用本 skill。若用户只给出一篇论文要求阅读，使用 `paper-reader`。

## 核心原则

- 先定义检索问题，不直接堆关键词。
- 优先使用权威数据库和可追踪检索式。
- 明确 inclusion / exclusion criteria。
- 文献只支持它实际证明的 claim。
- 不编造 DOI、PMID、作者、年份或结论。
- 网页访问或全文抽取失败时，先用 Crossref、OpenAlex、DOI resolver 或 Semantic Scholar 等 metadata source 锁定题名、作者、年份、期刊和 DOI；不能从不完整摘要补写结论。

## 工作流程

1. 把用户问题转成 1-3 个检索问题。
2. 设计关键词组：biological entity、data type、method、phenotype、organism、mechanism。
3. 选择数据库：PubMed、Google Scholar、Semantic Scholar、CrossRef、bioRxiv、arXiv、领域数据库。
4. 记录检索式、日期、筛选标准和排除理由。
5. 输出 evidence matrix：每篇文献的 claim、evidence、dataset、method、limitation、reusable resources、relevance 和 action。
6. 总结 consensus、controversy、method gap、data gap、可复用资源和我的可能贡献，而不只是列摘要。
7. 给出 go/no-go 或下一阶段决策价值：继续、复现、避免、仅引用、需要补数据/结构/assay。

## 输出格式

- `Search questions`
- `Search strings`
- `Databases`
- `Inclusion / exclusion criteria`
- `Evidence table`
- `Citation candidates`
- `Knowledge gaps`
- `Next papers to read`

需要 evidence table 模板时读取 `references/evidence-table-template.md`。
需要将开放式背景检索整理为项目决策用的 evidence map、dataset/method/gap map、go/no-go memo 时，读取 `references/evidence-map-matrix.md`。

## Hypothesis-driven locus or repeat synthesis

当用户要把未发表的 locus/repeat 假说与公共证据连接，或寻找相应公共数据时：

1. 先分 expression、sequence/structure、motif/binding、3D contact 和 DNA rearrangement 等证据层，再分别设计检索式。
2. Negative expression evidence 只能约束 transcript-abundance 假说，不能自动否定 DNA、chromatin、contact 或 rearrangement 假说。
3. 先从论文 Data Availability 和 study-level record 找 accession，再核对 run-level assay、sample、control、reference 和 read metadata。
4. 对重复或低可比对区间，预先记录 reference、read length、MAPQ、multi-mapping、selection protocol 和 assay-specific limitation。
5. 按 Strong / Moderate / Exploratory / Speculative 标记各层证据，并写清每篇论文或数据集没有证明什么。

详细检索与报告模板见 `references/repeat-locus-literature-search.md`。

## Molecular interaction / docking feasibility searches

当用户询问两个蛋白是否互作、某个突变是否有依据、或 docking 方案是否可行时：

1. 先把问题拆成 direct interaction、mechanistic/domain evidence、mutation rationale、computational feasibility 四层；不要只堆 gene names。
2. 同时检索别名和物种形式，例如 gene symbol、protein name、family name、domain name、ligand name、Greek/ASCII variants。
3. PubMed/PMC 文献之外，检查 IntAct/BioGRID/STRING 等互作数据库；高通量 coIP/proximity 只能作为 weak network evidence，不能自动等同直接互作。
4. 若没有找到 direct interaction paper，要明确说“未找到直接证据”，再区分 shared pathway/localization、motif/domain compatibility 与 docking hypothesis。
5. 突变依据要区分 exact-residue evidence 与 homologous-family/charge-rationale evidence；K/R-rich lipid-binding motif 的 K→A/K→E 设计可以作为电荷贡献测试，但不能写成已证明的位点，除非有直接文献。
6. 可行性建议优先支持最窄、证据最强的模型：ligand/headgroup 或 domain/fragment docking 通常优先于全长多结构域蛋白 docking。

蛋白互作/突变/docking 可行性检索的详细参考见 `references/protein-interaction-literature-search.md`。
