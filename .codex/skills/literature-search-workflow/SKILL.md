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

## 工作流程

1. 把用户问题转成 1-3 个检索问题。
2. 设计关键词组：biological entity、data type、method、phenotype、organism、mechanism。
3. 选择数据库：PubMed、Google Scholar、Semantic Scholar、CrossRef、bioRxiv、arXiv、领域数据库。
4. 记录检索式、日期、筛选标准和排除理由。
5. 输出 evidence table：每篇文献支持什么、证据等级、是否可引用。
6. 总结 knowledge gap 和下一步阅读优先级。

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
