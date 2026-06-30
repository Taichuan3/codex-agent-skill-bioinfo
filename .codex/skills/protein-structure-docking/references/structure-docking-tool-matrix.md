# Structure / Docking Tool Matrix

| Task | Candidate tools | Use when | Main caveat |
|---|---|---|---|
| Protein-ligand pilot docking | AutoDock Vina, GNINA, CB-Dock, DiffDock-like tools | ligand and receptor are defined; need quick exploratory pose | score is not proof of affinity; protonation/pocket definition matters |
| Protein-protein docking | HDOCK, ClusPro, HADDOCK when restraints exist | testing interface hypotheses or WT vs mutant trend | docking rank can be unstable; require controls and interface inspection |
| Structure/complex prediction | AlphaFold DB, ColabFold, Boltz, Chai, AF3-like services | structure unavailable or complex prediction needed | model confidence does not equal binding validation |
| Pose validation | visual inspection, PoseBusters-like checks, clash/contact analysis | deciding whether a pose is physically plausible | validation filters reduce false positives but do not prove biology |

## QC checklist

- Same receptor preparation across compared conditions.
- Same ligand/partner preparation and protonation/chain policy.
- Explicit residue numbering and chain mapping.
- Negative/positive controls when available.
- Visual inspection of clashes, pocket placement, interface contacts.
- Store raw output, parsed summary table, and representative figures.
