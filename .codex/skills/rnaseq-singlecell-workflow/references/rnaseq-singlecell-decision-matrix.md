# RNA-seq / Single-cell Decision Matrix

| Need | Common tools/workflows | Main checks | Caveat |
|---|---|---|---|
| bulk RNA-seq preprocessing | nf-core/rnaseq, STAR/Salmon/RSEM, featureCounts | reference/annotation, strandedness, mapping rate, sample sheet | preprocessing choices affect downstream DE |
| bulk DE | DESeq2, edgeR, limma-voom | design matrix, batch, dispersion, contrasts, FDR | DE is association, not mechanism |
| scRNA-seq clustering/markers | Scanpy, Seurat, scVI/scANVI | QC thresholds, doublets, batch, marker specificity | clusters are model-dependent |
| pseudo-bulk | edgeR/DESeq2 on sample-level aggregates | biological replicate count, cluster identity, library size | cell-level p-values can inflate evidence |
| splicing/isoform | rMATS, LeafCutter, MAJIQ, SUPPA2, long-read tools | junction support, coverage, event definition | 3' scRNA-seq is weak for most splicing claims |
| count-matrix QC | DESeq2 VST/rlog, edgeR filterByExpr, PCA/correlation | raw counts, sample roster, depth, detected genes, outliers | transformed matrices are for QC, not DE testing |
| automated QC report | MultiQC plus upstream logs | expected sample count, module scope, upstream tool versions | MultiQC aggregates existing metrics; it does not measure or gate by itself |
| GRN/regulon | pySCENIC/SCENIC+, arboreto, AUCell | motif database/species, random seed, motif pruning, AUC matrix | co-expression modules are not regulons until motif-pruned |
