# Protein structure prediction and docking workflow notes

Use this reference when a bioinformatics task involves protein structure prediction, mutation models, protein-protein docking, or protein-ligand docking.

## Workflow safeguards

- Treat structure quality as a prerequisite for docking. Do not rush to docking before confirming sequence identity, mutation definitions, model coverage, pLDDT/pTM/PAE, and obvious steric problems.
- When the user corrects mutation definitions, immediately regenerate all dependent FASTA/PDB/restraint files and mark old outputs obsolete. Verify differences against WT explicitly by residue number.
- When requested, present key comparison tables and figures together with their file paths.
- Be precise with terminology: ColabFold can be a runner/wrapper for AlphaFold2/AF2-ptm models, not a completely unrelated modeling algorithm. Say “AlphaFold2/AF2-ptm via ColabFold runner” when that is what was used.

## Recommended sequence-to-docking pipeline

1. **Sequence and mutation QC**
   - Confirm FASTA length, headers, exact motif positions, residue numbering, and mutant-vs-WT diffs.
   - For multiple mutants, make a small table: WT residue, mutant residue, and whether any residue remains unchanged.

2. **Structure prediction before docking**
   - Generate structures for WT and each mutant with the same settings where possible.
   - Report: coverage, mean/median pLDDT, pTM, PAE if available, and local pLDDT for the biologically relevant motif/domain.
   - For long/flexible proteins, identify high-confidence domains/regions rather than assuming the full-length global conformation is reliable.

3. **Compute placement**
   - Use a laptop only for QC, setup, smoke tests, small ligand docking, and result parsing/plotting.
   - Use GPU/server resources for full AlphaFold2/ColabFold runs on large proteins, AlphaFold-Multimer/complex prediction, ensemble prediction, and full protein-protein docking campaigns.

4. **Docking strategy**
   - Avoid treating one full-length blind docking result as a conclusion, especially when the protein model has low pTM or large low-pLDDT regions.
   - Prefer domain/region docking or restrained docking when there is a biological hypothesis about an interface.
   - Run replicate/ensemble docking across multiple AF2 models when resources allow.
   - For small-molecule/phospholipid docking, set the box around the biologically relevant motif/domain to reduce search space and focus interpretation.

5. **Result QC before interpretation**
   - Check whether top poses have severe clashes/overlap (e.g., many atom pairs <2 Å, near-zero motif distances). If so, label the run as failed/low-confidence even if scores look favorable.
   - Do not interpret docking scores as binding affinity/Kd. Use them only for within-run ranking and exploratory triage.
   - Report caveats prominently: structure confidence, model coverage, docking sampling, restraints, and whether the modeled region matches the user-provided sequence.

## Suggested server settings

For large single-protein AF2/ColabFold jobs when server/GPU is available:

```text
model-type: alphafold2_ptm
num-models: 5
num-recycle: 3–6
templates: on if HHsuite/hhsearch is available
Amber relax: top ranked model(s) only
```

For CPU-only laptops, reduce scope first rather than forcing production settings: run smoke tests, one quick model, or domain-only prediction, and explain that production structure generation should move to a server.
