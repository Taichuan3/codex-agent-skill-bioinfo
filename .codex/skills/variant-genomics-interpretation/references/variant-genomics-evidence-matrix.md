# Variant / Genomics Evidence Matrix

| Evidence type | Useful sources/tools | Required fields | Main caveat |
|---|---|---|---|
| variant identity | dbSNP, Ensembl VEP, ClinVar | build, REF/ALT, transcript, consequence | coordinate/build mismatches are common |
| population frequency | gnomAD, 1000G, cohort VCF | ancestry, AF, AC/AN, filters | population mismatch changes interpretation |
| association | GWAS Catalog, Open Targets, PheWAS | trait, effect, p, ancestry, sample size | association is not causality |
| colocalization/QTL | coloc, SuSiE, eQTL/sQTL/pQTL sources | locus, LD, credible set, posterior | shared signal depends on fine-mapping assumptions |
| clinical assertion | ClinVar, guidelines, literature | review status, condition, assertion date | not personal medical advice |
| callset/sample QC | bcftools, GATK/Picard, VerifyBamID/Somalier-like summaries | depth, missingness, contamination, sex/identity, filters | bad callset QC invalidates downstream interpretation |
| regulatory conservation/TFBS | UCSC phyloP/phastCons, JASPAR, UniBind, ENCODE cCRE | build, interval, collection, TF/cell context | conserved or bound does not prove disease mechanism |
| PRS/MR | PRSice/LDpred/PLINK, TwoSampleMR, MR-Egger | GWAS source, LD reference, ancestry, instrument strength | population transfer and pleiotropy can dominate |
