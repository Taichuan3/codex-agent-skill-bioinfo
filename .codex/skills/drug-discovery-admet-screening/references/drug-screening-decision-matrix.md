# Drug Screening / ADMET Decision Matrix

| Need | Candidate sources/tools | Output | Caveat |
|---|---|---|---|
| Target validation | Open Targets-like evidence, GWAS/eQTL/pQTL colocalization, literature | target evidence table | association and causality must be separated |
| Bioactivity lookup | ChEMBL, PubChem BioAssay, BindingDB if available | activity table with units and assay context | assays vary by construct, species, and confidence |
| Virtual screening | RDKit filters, Vina/GNINA/SMINA, DiffDock-like tools | ranked compounds and pose/QC summaries | false positives high; docking rank alone is weak |
| ADMET/QSAR | ADMETlab-like tools, ADMET-AI-like models, RDKit descriptors, chemprop/DeepChem when available | predicted property table | prediction only; require applicability domain |
| Repurposing | drug-target databases, pathway/omics reversal, literature | candidate mechanism table | hypothesis generation, not efficacy proof |

## Candidate table minimum columns

candidate_id, target, evidence_type, source, metric, value, version_or_date, uncertainty, caveat, next_validation
