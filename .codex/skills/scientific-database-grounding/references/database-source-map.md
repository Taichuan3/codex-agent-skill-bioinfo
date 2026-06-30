# Database Source Map

Use this reference only when a task needs concrete database grounding.

## Genetics / variant / regulatory

| Need | Primary sources | Record carefully |
|---|---|---|
| Variant identity | dbSNP, ClinVar, Ensembl VEP, gnomAD | rsID, genome build, REF/ALT, transcript, clinical significance, allele frequency |
| Regulatory interval | ENCODE cCREs, UCSC, Ensembl Regulatory Build, JASPAR | genome build, assay type, cell/tissue source, score, motif version |
| Expression context | GTEx, Human Protein Atlas, Tabula/cell atlas sources | tissue/cell type, unit, version, sample context |
| Model prediction | AlphaGenome or other sequence models | model/version, input sequence/build, output type, tissue/track context, prediction window |

## Protein / structure

| Need | Primary sources | Record carefully |
|---|---|---|
| Protein sequence | UniProt, NCBI, Ensembl | accession, isoform, length, organism, canonical status |
| Domain/function | InterPro, Pfam, GO, UniProt annotations | domain boundaries, evidence code, reviewed/unreviewed status |
| Structure | PDB, AlphaFold DB, ESM/other predicted structures | experimental vs predicted, chain, residue numbering, confidence, missing regions |

## Compound / drug target

| Need | Primary sources | Record carefully |
|---|---|---|
| Bioactivity | ChEMBL, PubChem BioAssay, BindingDB if available | assay type, target organism, IC50/Kd/Ki, units, confidence score |
| Target rationale | Open Targets, literature databases, pathway databases | evidence type, disease context, genetic support, directionality |
| ADMET / safety | public ADMET tools or literature | prediction vs measured, applicability domain, uncertainty |

## Literature metadata

Use PubMed/EuropePMC/OpenAlex/Crossref to verify metadata. Use paper-reading or literature-search skills for interpretation.
