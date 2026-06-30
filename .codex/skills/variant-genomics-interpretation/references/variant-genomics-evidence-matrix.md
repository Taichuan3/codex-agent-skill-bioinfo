# Variant / Genomics Evidence Matrix

| Evidence type | Useful sources/tools | Required fields | Main caveat |
|---|---|---|---|
| variant identity | dbSNP, Ensembl VEP, ClinVar | build, REF/ALT, transcript, consequence | coordinate/build mismatches are common |
| population frequency | gnomAD, 1000G, cohort VCF | ancestry, AF, AC/AN, filters | population mismatch changes interpretation |
| association | GWAS Catalog, Open Targets, PheWAS | trait, effect, p, ancestry, sample size | association is not causality |
| colocalization/QTL | coloc, SuSiE, eQTL/sQTL/pQTL sources | locus, LD, credible set, posterior | shared signal depends on fine-mapping assumptions |
| clinical assertion | ClinVar, guidelines, literature | review status, condition, assertion date | not personal medical advice |
