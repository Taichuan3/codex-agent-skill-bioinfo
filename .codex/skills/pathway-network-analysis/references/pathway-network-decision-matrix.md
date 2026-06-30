# Pathway / Network Decision Matrix

| Need | Method | Key checks | Caveat |
|---|---|---|---|
| over-representation | ORA / Fisher-style enrichment | background universe, ID mapping, FDR | sensitive to gene list threshold |
| ranked shifts | GSEA / fgsea / camera/roast | rank metric, duplicates, gene-set size | direction depends on ranking design |
| pathway database | Reactome, GO, KEGG, WikiPathways, MSigDB | version/date, species, redundancy | databases encode prior knowledge bias |
| network analysis | STRING, BioGRID, NetworkX, igraph | edge source, confidence, degree bias | centrality is not functional proof |
