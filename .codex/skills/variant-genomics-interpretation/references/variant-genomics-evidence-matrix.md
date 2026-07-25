# Variant / Genomics Evidence Matrix

| Evidence type | Required identity/context | Useful source class | Can support | Cannot establish alone |
|---|---|---|---|---|
| Variant record | build, chr:pos, REF/ALT, normalization, transcript | VCF header, reference FASTA, transcript annotation | stable entity mapping | biological effect |
| Callset QC | sample, depth, genotype quality, filters, identity | callset metrics and pipeline reports | fitness for bounded downstream use | truth of every genotype |
| Population frequency | allele, ancestry, AC/AN, filters, release | population reference or cohort | frequency in represented data | pathogenicity or penetrance |
| Predicted consequence | transcript, consequence ontology, model/version | annotation and prediction tools | hypothesis about affected feature | functional or clinical effect |
| Clinical assertion | condition, allele, review status, date, conflicts | curated clinical archive or guideline | assertion context | diagnosis for an individual |
| GWAS association | trait, effect allele, ancestry, model, sample size | summary statistics or catalog | population-level association | causal variant, gene or mechanism |
| Fine-mapping | locus, variant coverage, LD reference, priors | credible-set model output | model-dependent candidate set | a uniquely causal variant |
| QTL / colocalization | tissue/cell context, alleles, LD, model | molecular QTL and coloc output | regulatory association or shared signal | causal mediation |
| Rare-variant test | mask, annotation, frequency rule, ancestry, burden model | gene/region test output | aggregate association | pathogenicity of each allele |
| PRS / MR | training GWAS, ancestry, LD, instruments, assumptions | model output and sensitivity analyses | bounded prediction or causal-inference evidence | personal action or assumption-free causality |

Keep sources as separate rows when they answer different questions. Record release/query date and unresolved conflict instead of collapsing them into one opaque score.
