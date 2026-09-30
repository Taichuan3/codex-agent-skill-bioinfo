---
name: scientific-database-grounding
description: 查询、解析和交叉核验生物医学实体数据库记录，保留ID/版本/坐标/参数/证据/日期。开放论文集→literature-search-workflow；指定论文→paper-reader；引用核验→citation-verifier；查询脚本/ETL→bioinfo-analysis-code；文字claim审查→claim-evidence-audit。
---
# Scientific Database Grounding
## 核心问题
如何用可重放来源解析实体并保留跨库冲突？
## 边界
拥有 entity resolution、lookup、record reconciliation/provenance；领域结构/docking/ADMET判断交领域Skill。记录/预测仅证明来源在该版本/日期的记载，不证明机制、因果、疗效或安全。
## 流程与交付
1. 固定 retrieval question、实体类型、原始ID/namespace、species、assembly/transcript/isoform、disease ontology、compound ID、未知项及目标字段；最小1–4个来源并说明primary/cross-check理由，官方API/下载表优先。
2. 先count/summary/小样本核命中和规模，再取最少字段；保留endpoint、query/body、filters、fields、pagination/limit、release/访问日期、原始ID和记录数。只检查凭据是否存在，不读/输出token/cookie/header/.env。
3. 核别名、build/allele/strand/transcript/isoform/species/assay/unit/evidence code；不静默合并。列agreement/conflict/unresolved mapping/release lag，不用方便来源覆盖冲突。空结果不等于实体不存在；保留失败/限流与替代来源。
4. 交 question/databases、exact identifiers/query、version/date、counts/fields/records、record–claim–evidence type–caveat映射、冲突/未解映射、handoff字段；写报告/source data附可重放query/command和字段定义。未执行标 planned query，不造记录。
## 执行后端
实际查询读 `../capability_registry.json` 的 `CAP-DB-001`，优先已安装source-specific curated Skill；仅跨实体能减少重复才比BioMCP。registry只选路不授权安装/凭据/配额/上传，检查条款、网络、凭据状态和项目权限。不可用保持planned/review，不用低质量摘要顶替；执行附backend/version、exact query、records/failures/replay pointer。

## 按需读取

- 需要选择 genetics、regulatory、expression、protein、structure、compound 或 literature metadata 来源时，读取 `references/database-source-map.md`。
- 需要设计 API query、ID 解析、字段裁剪、分页、限流、凭据安全或冲突核验时，读取 `references/database-query-contract.md`。

## 交付契约

至少交付 retrieval question、databases、exact identifiers/query parameters、version/date、record counts、selected fields/records、agreement/conflict、evidence type、caveats 和未解决映射。未实际查询时标记 `planned query`，不得提供伪造记录。
