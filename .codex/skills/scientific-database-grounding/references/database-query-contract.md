# Database Query Contract

用于设计可重放的科学数据库查询，并统一实体解析、分页、字段选择、冲突核验和凭据边界。

## 查询前

- 明确实体类型：gene、variant、interval、protein、structure、compound、drug、disease、trial、publication。
- 明确 species 和 ID namespace：gene symbol、NCBI Gene ID、Ensembl ID、UniProt accession、rsID、HGVS、ChEMBL ID、PubChem CID、EFO/MONDO disease ID。
- 明确版本上下文：genome build、transcript set、database release 或访问日期。
- 执行 API-key safety：对需要 API key 的数据库只做 presence check；不要输出 `.env` 或 token 内容。

## 查询中

- 优先使用官方 API、下载表或可记录的 endpoint；网页复制只作为最后手段。
- 采用 count-first / summary-first：先 count/summary 后 search/evidence；大结果集必须处理 pagination、limit、cursor 或 offset。
- 字段先行：ClinicalTrials、UniProt、ChEMBL、Open Targets、STRING、UCSC 等结果可能很大，先选择 fields/columns 或把响应写入文件，再用 `jq`/表格解析读取必要字段。
- 检索先小后大：先用 count、limit 5、status 或 dry-run 检查 query 是否命中预期实体，再扩大范围。
- 对 NCBI/Ensembl/UniProt/ClinicalTrials 等有 rate limit 的 API，串行或限流请求。
- 对 POST-only 或 GraphQL 查询，保留 query body、variables 和 response fields。
- 对需要凭据或注册的服务，只记录凭据是否存在、服务模式和访问日期；不要把 token、cookie、Authorization header 或 `.env` 内容放入输出。
- 记录失败请求、重试、空结果和替代来源，不把空结果解释为不存在。

## 交叉核验

- Variant：至少核对 genome build、chr/pos/ref/alt、rsID/HGVS、clinical significance、review status 和 transcript consequence。
- Gene/protein：核对 symbol alias、species、canonical isoform、domain、subcellular/location 或 expression context。
- Compound/drug：核对 name synonym、structure identifier、bioactivity assay type、target species、approved indication 和 safety/regulatory source。
- Disease/clinical：核对 ontology ID、population/context、trial phase/status、endpoint 和 whether evidence is observational, curated, predicted, or interventional。

## 输出

输出应包含：

- retrieval question
- databases queried
- exact query parameters and date
- response fields / columns retained
- number of records considered
- selected records and identifiers
- agreement/conflict across sources
- evidence type and caveat

数据库记录不是机制证明。ClinVar/Open Targets/PrimeKG/ChEMBL/ClinicalTrials/OpenFDA 等结果只能支撑“已有记录/关联/候选证据”，不能直接写成当前项目验证、临床疗效或个人医疗建议。
