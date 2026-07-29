# Omics Figure QA

用于把外部 single-cell、RNA-seq、variant/genomics、pathway/network、scientific visualization skills 中的高价值图形规则压缩到本地 publication plotting。

## 通用

- 每张图必须说明 data universe：genes、samples、cells、variants、regions、pathways、network nodes/edges。
- 标注 denominator：过滤前后数量、用于统计的 n、显示的 top N 和未显示部分。
- 记录 normalization、batch correction、model formula、database release、genome build 和 random seed。
- Source data / source data table 应能重建 panel，不只保存最终 PNG/SVG；line/text figures 避免 JPEG，优先 SVG/PDF 或高分辨率 PNG。

## Single-cell

- UMAP/t-SNE 是可视化，不是谱系或距离的强证据；caption 不写成连续发育或因果过程，除非有专门 trajectory/validation。
- QC、ambient RNA、doublet、batch correction 和 annotation 是独立 caveat；图注或方法中需要能追踪。
- 差异表达优先用 sample-level pseudobulk 支撑 condition claim；cell-level test 只能作为探索或补充。

## RNA-seq

- Volcano/MA/heatmap 需说明 contrast、design formula、filtering、FDR threshold、effect-size threshold 和 shrinkage 方法。
- PCA/cluster 图需说明输入矩阵、normalization 和是否使用 top variable genes。

## Variant / Genomics

- Locus、interval、coverage 和 variant 图必须写 genome build、coordinate convention、reference/alternate allele 和 transcript context。
- 多数据库注释图需区分 submitted/curated/predicted/clinical evidence，避免把 annotation 画成实验验证。

## Pathway / Network

- Enrichment 图必须说明 gene universe、ID mapping loss、database version 和 multiple-testing correction。
- Network 图必须说明 edge source、directionality/weight、layout seed 和 node filtering；centrality/community 结果通常是 hypothesis-generating。
