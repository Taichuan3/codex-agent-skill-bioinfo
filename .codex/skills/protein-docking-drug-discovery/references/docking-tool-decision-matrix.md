# Docking / Design Tool Decision Matrix

## Minimal decision table

| Task | Candidate tools | Use when | Main caveat |
|---|---|---|---|
| Protein-ligand pilot docking | AutoDock Vina, GNINA, CB-Dock, DiffDock-like tools | ligand and receptor are defined; need quick exploratory pose | score is not proof of affinity; protonation/pocket definition matters |
| Protein-protein docking | HDOCK, ClusPro, HADDOCK when restraints exist | testing interface hypotheses or WT vs mutant trend | docking rank can be unstable; require controls and interface inspection |
| Structure/complex prediction | AlphaFold DB, ColabFold, Boltz, Chai, AF3-like services | structure unavailable or complex prediction needed | model confidence does not equal binding validation |
| Binder/protein design | RFdiffusion, ProteinMPNN, BindCraft, LigandMPNN | designing binders or constrained variants | GPU/large compute; needs stringent filtering and experimental validation |
| Virtual screening | Vina/GNINA/SMINA, RDKit filters, ChEMBL/PubChem inputs | many compounds against one target | false positives high; use consensus/QC and applicability domain |
| ADMET/QSAR | RDKit descriptors, ADMETlab-like tools, ADMET-AI-like predictors | early druggability/toxicity filtering | prediction only; record uncertainty and domain |

## QC checklist

- Same receptor preparation across compared conditions.
- Same ligand preparation and protonation policy.
- Explicit residue numbering and chain mapping.
- Negative/positive controls when available.
- Visual inspection of clashes, pocket placement, interface contacts.
- Store raw output, parsed summary table, and representative figures.
