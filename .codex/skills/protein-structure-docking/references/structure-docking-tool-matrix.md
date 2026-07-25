# Structure / Docking Tool Matrix

| Task | Candidate tools | Use when | Main caveat |
|---|---|---|---|
| Known-pocket protein-ligand pilot | AutoDock Vina, GNINA, SMINA-like tools | receptor, ligand and box are defined; controls are possible | score is protocol-specific, not affinity |
| Blind or pose-generation hypothesis | CB-Dock, DiffDock-like tools | site or pose is uncertain and broad hypothesis generation is acceptable | confidence does not identify a true site or binding |
| Protein-protein docking | HDOCK, ClusPro, HADDOCK when restraints exist | testing interface hypotheses or WT vs mutant trend | docking rank can be unstable; require controls and interface inspection |
| Structure/complex prediction | AlphaFold DB, ColabFold, Boltz, Chai, AF3-like services | structure unavailable or complex prediction needed | model confidence does not equal binding validation |
| Pose validation | visual inspection, PoseBusters-like checks, clash/contact analysis | deciding whether a pose is physically plausible | validation filters reduce false positives but do not prove biology |
| Affinity refinement | FEP/RBFE/ABFE implementations with validated setup | binding mode and congeneric series are credible and compute/protocol expertise exists | expensive, assumption-sensitive and still assay-dependent |

## QC checklist

- Same receptor preparation across compared conditions.
- Same ligand/partner preparation and protonation/chain policy.
- Explicit residue numbering and chain mapping.
- Negative/positive controls when available.
- Visual inspection of clashes, pocket placement, interface contacts.
- Store raw output, parsed summary table, failure records and representative figures.


## Preparation chain

- Protein preparation: confirm sequence/accession/isoform, chain, residue numbering, missing regions, cofactors/metals, protonation assumptions and whether the structure is apo/holo/predicted.
- Ligand preparation: standardize SMILES/InChI/SDF, stereochemistry, protomer/tautomer/charge, salts, conformer ensemble and force-field assumptions.
- Pocket / box definition: distinguish known pocket, blind docking, cryptic pocket, protein-protein interface, membrane/lipid site, metal/covalent site and restraint-defined target.
- Controls: redock known ligand when possible; include negative/positive controls or WT/mutant matched setup for comparisons.
- Pose validation: check clashes, pocket placement, contact plausibility, strain/geometry where possible, repeated seeds or alternative tools for fragile conclusions.

## Default path and escalation

- Use Vina/GNINA/SMINA-like workflows for exploratory screening when receptor and ligand are well-defined.
- Treat DiffDock/Boltz/Chai/AF3-like outputs as pose or complex hypotheses; use independent QC/rescoring before interpretation.
- Use FEP/RBFE/ABFE only as later refinement after the binding mode and candidate set are credible.
- API-backed tools require an authorized account, versioned endpoint record and bounded pilot before campaign use.
