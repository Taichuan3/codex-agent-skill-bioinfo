# Clinical Bioinformatics Evidence Boundary

| Evidence | Source examples | Can support | Cannot support |
|---|---|---|---|
| trial record | ClinicalTrials.gov, EUCTR | trial existence/design/status | efficacy conclusion without results |
| clinical assertion | ClinVar, guideline summaries | curated association context | personal diagnosis |
| PGx annotation | CPIC/FDA labels/public PGx databases | research-level drug-gene context | dosing advice for a person |
| survival/biomarker | cohort analysis, literature | exploratory/prognostic association | clinical decision without validation |
| trial results | ClinicalTrials.gov results, publication | endpoint-specific interventional evidence | generalized efficacy outside studied population |
| safety/regulatory signal | OpenFDA, label sections, adverse-event summaries | known safety context or reporting signal | incidence or causality without proper denominator |
| cohort table | TCGA/UKB/registry/clinical cohort | descriptive or model-based association | individual prognosis without validated clinical model |
