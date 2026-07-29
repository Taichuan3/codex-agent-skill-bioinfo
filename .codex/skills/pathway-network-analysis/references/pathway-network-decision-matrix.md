# Pathway / Network Decision Matrix

| Need | Method | Key checks | Caveat |
|---|---|---|---|
| over-representation | ORA / Fisher-style enrichment | background universe, ID mapping, FDR | sensitive to gene list threshold |
| ranked shifts | GSEA / fgsea / camera/roast | rank metric, duplicates, gene-set size | direction depends on ranking design |
| pathway database | Reactome, GO, KEGG, WikiPathways, MSigDB | version/date, species, redundancy | databases encode prior knowledge bias |
| network analysis | STRING, BioGRID, NetworkX, igraph | edge source, confidence, degree bias | centrality is not functional proof |
| leading-edge interpretation | fgsea/GSEA leading edge, core enrichment genes | gene IDs, effect direction, overlap with input table | pathway names alone are weak evidence |
| regulon/network activity | SCENIC/AUCell, VIPER, PROGENy-like scores | model database, target gene set, activity matrix | inferred activity is not direct perturbation evidence |
| visualization | dot plot, enrichment map, network graph | denominator, FDR, term grouping, label selection | dense networks can imply unsupported specificity |
