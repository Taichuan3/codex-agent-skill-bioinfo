# Omics Execution Contract

用于吸收外部 RNA-seq、single-cell、variant/genomics、pathway/network 和 workflow-manager skills 中可复用的执行机制。不要把本文件变成具体工具手册；具体命令仍以项目脚本、官方文档和本地环境为准。

## 先锁定输入

- 数据类型：FASTQ/BAM/count matrix/H5AD/VCF/BED/gene list/network edge table。
- 样本 universe：样本 ID、condition、batch、paired design、replicate、cell/sample 层级，明确 excluded samples。
- 参考版本：genome build、annotation release、transcriptome、protein database、pathway database 和访问日期。
- 坐标系统：BED 为 0-based half-open；VCF 和常见 genomic region string 为 1-based；跨工具转换必须记录。
- 随机性：UMAP/t-SNE/Leiden/network layout、downsampling、bootstrap、permutation 等必须固定 seed。

## 分析前预检

- 先运行最小样本或测试 profile，确认环境、索引、容器、权限、路径和输出结构。
- 对大型 workflow pin pipeline revision、tool/container version、参数文件和执行 profile；不要用 `latest` 生成投稿结果。
- 对 NGS 文件先检查 header/index、read/count dimensions、sample names、chromosome naming 和 metadata join key。
- 对 single-cell 先保留 raw counts layer；不要重复 normalize 已经 normalized 的矩阵。
- 对 variant/interval 先检查 genome build、contig naming、index 文件和 coordinate convention。

## 任务类型要点

- Bulk RNA-seq：区分 FASTQ-to-count、count QC、DE model、contrast table 和 shrinkage/visualization；记录 low-count filtering 和 design formula。
- Single-cell：QC 阈值需有 rationale；ambient RNA、doublet、batch correction、cell-type annotation 和 pseudobulk DE 都是独立 decision points，不静默串联。
- Variant/genomics：记录 caller/filter、sample set、INFO/FORMAT 字段含义、allele frequency source、transcript consequence 和 multi-allelic handling。
- Pathway/network：记录 gene universe、ID mapping loss、database version、directionality/weight、multiple testing 和 whether the result is enrichment, topology, or hypothesis generation。

## 输出契约

每个稳定步骤至少写清：

- command 或 notebook/script path
- input files and checksums or dimensions
- key parameters and thresholds
- output files
- log file
- environment/tool versions
- known caveats

## 不升级结论

- QC、clustering、enrichment、network centrality、docking-like score 或 database association 通常只提供 Exploratory 到 Moderate 证据。
- 如果没有独立样本、orthogonal validation 或 direct experimental support，不把 pathway/network/single-cell annotation 写成机制或因果结论。
