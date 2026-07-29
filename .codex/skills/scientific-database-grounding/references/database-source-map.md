# Database Source Map

Use this reference only when a task needs concrete database grounding.

## Genetics / variant / regulatory

| Need | Primary sources | Record carefully |
|---|---|---|
| Variant identity | dbSNP, ClinVar, Ensembl VEP, gnomAD | rsID, genome build, REF/ALT, transcript, clinical significance, allele frequency |
| Regulatory interval | ENCODE cCREs, UCSC, Ensembl Regulatory Build, JASPAR | genome build, assay type, cell/tissue source, score, motif version |
| Expression context | GTEx, Human Protein Atlas, Tabula/cell atlas sources | tissue/cell type, unit, version, sample context |
| Model prediction | Sequence/regulatory prediction models | model/version, input sequence/build, output type, tissue/track context, prediction window |

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


## Entity-level provenance fields

| Entity | Primary record | Secondary cross-check | Must record |
|---|---|---|---|
| Gene | HGNC/Ensembl/NCBI Gene | UniProt, GTEx, Open Targets | symbol, stable ID, species, alias resolution, database version/date |
| Variant | dbSNP/ClinVar/gnomAD/Ensembl VEP | literature, locus-specific databases when relevant | rsID, build, REF/ALT, transcript, consequence, frequency, clinical significance |
| Regulatory interval | ENCODE/UCSC/Ensembl Regulatory Build | GTEx/eQTL, JASPAR, model outputs | build, coordinates, assay type, tissue/cell source, score, track version |
| Protein | UniProt/PDB/AlphaFold DB | InterPro/Pfam/GO | accession, isoform, chain, residue numbering, evidence code, structure confidence |
| Compound | ChEMBL/PubChem BioAssay/BindingDB | literature, Open Targets, ADMET tools | compound ID, SMILES/InChI, assay type, target organism, units, confidence, prediction vs measured |
| Literature | PubMed/EuropePMC/OpenAlex/Crossref | journal site, DOI resolver | PMID/DOI, title, authors, year, query string, retrieval date |

## NCBI Entrez notes

- ESearch returns UIDs, not the biological record itself; inspect QueryTranslation when building a reproducible query.
- Record database, query string, retmax/retstart, date, and whether WebEnv/history server was used.
- Use ELink only with an explicit linkname when mapping between databases; do not assume the default link is the one needed.
- Use ESummary for metadata tables and EFetch for full records/sequences; record rettype/retmode.
- If UID mapping, transcript context, or build differs across sources, list the conflict instead of silently merging.
