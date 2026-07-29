# Drug Screening / ADMET Decision Matrix

| Need | Candidate sources/tools | Output | Caveat |
|---|---|---|---|
| Target validation | Open Targets-like evidence, GWAS/eQTL/pQTL colocalization, literature | target evidence table | association and causality must be separated |
| Bioactivity lookup | ChEMBL, PubChem BioAssay, BindingDB if available | activity table with units and assay context | assays vary by construct, species, and confidence |
| Virtual screening | RDKit filters, Vina/GNINA/SMINA, DiffDock-like tools | ranked compounds and pose/QC summaries | false positives high; docking rank alone is weak |
| ADMET/QSAR | ADMETlab-like tools, ADMET-AI-like models, RDKit descriptors, chemprop/DeepChem when available | predicted property table | prediction only; require applicability domain |
| Repurposing | drug-target databases, pathway/omics reversal, literature | candidate mechanism table | hypothesis generation, not efficacy proof |
| Target scoring | Open Targets, ChEMBL, PDB/AFDB, clinical/safety sources | dimension-level GO/NO-GO rationale | decision support, not experimental validation |
| Molecule generation | MolMIM/GenMol/SAFE-like generation, RDKit filters | valid/unique/novel candidate set | generated molecules need synthesis and risk checks |

## Candidate table minimum columns

candidate_id, target, evidence_type, source, metric, value, version_or_date, uncertainty, caveat, next_validation


## Screening preparation

- Standardize compounds before ranking: salts, stereochemistry, tautomer/protomer, charge, duplicates and assay-compatible units.
- Separate evidence layers: target genetics, expression/context, bioactivity, docking/pose, ADMET/QSAR, literature and clinical/PGx annotations.
- For ADMET/QSAR, record endpoint, model/source, applicability domain, uncertainty/calibration and structural alerts.
- Record whether each metric is measured, curated, predicted, text-mined or model-derived.
- For GO/NO-GO style summaries, state stop/pivot criteria and the missing validation needed to upgrade evidence.
