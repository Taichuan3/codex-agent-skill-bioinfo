# Protein structure prediction and docking workflow notes

Use this reference when a bioinformatics task depends on predicted protein structures before docking or interface analysis.

## User-facing workflow preferences

- Treat structure generation as the foundation for docking. Do not rush into docking with low-quality or wrong-length structures when the user asks for AlphaFold-quality inputs.
- Show key tables and images directly in chat when reporting results; do not only provide file paths.
- Clearly distinguish exploratory/pilot results from interpretable or publication-ready results.
- If the user corrects mutation definitions, immediately regenerate FASTA/PDB/restraint inputs and invalidate older outputs based on the wrong definition.

## AlphaFold2 vs ColabFold wording

- Be precise: ColabFold is commonly used as a runner/wrapper around AlphaFold2/AF2-ptm models with MMseqs2 MSA generation. Do not imply it is a totally separate structure prediction algorithm when the model is `alphafold2_ptm`.
- Phrase methods as: “AlphaFold2/AF2-ptm via ColabFold runner” when using `colabfold_batch --model-type alphafold2_ptm`.
- If the user explicitly asks for AlphaFold2, explain this relationship before proceeding and make sure outputs are labeled with the model type, not just “ColabFold.”

## Quality-first sequence → structure → docking checklist

1. Verify sequence length, header, and mutation definitions before any modeling.
2. Generate or reuse MSA intentionally; record whether cached `.a3m` or FASTA was used.
3. Prefer higher-quality prediction settings when docking depends on the model:
   - multiple models (`--num-models 3` or `5` depending on time budget),
   - multiple recycles (`--num-recycle 3+`),
   - sufficiently deep MSA (`--max-seq`, `--max-extra-seq`),
   - templates only when the required tools are actually installed,
   - optional Amber/OpenMM relax only after deciding the top model is worth the extra CPU time.
4. For long proteins on CPU-only machines, explicitly state the trade-off: full production settings may take overnight to multiple days. Pick an overnight-feasible quality upgrade rather than a token quick run.
5. After prediction, report at minimum: pLDDT, pTM, PAE image/summary, residue coverage, and local pLDDT for the biologically relevant motif/domain.
6. Only proceed to docking if structure quality is acceptable for the region being interpreted. If pTM is low or most residues have pLDDT <50, recommend domain-level or restrained docking instead of full-length blind docking.
7. For docking, report score tables, interface residues, motif/domain contact status, and steric-clash metrics. Large numbers of atom pairs <2 Å indicate invalid poses even if docking scores look favorable.

## Pitfalls from ACTN4–PHLDB2 session

- Full-length HDOCK sequence-input jobs may return modeled fragments rather than explicit full-length structures; always check returned residue coverage before interpreting docking.
- Full-length blind docking of large low-confidence proteins can produce strongly scored but physically impossible poses with severe steric overlap. Add clash metrics before presenting any pose as plausible.
- Template-enabled ColabFold requires HHsuite/hhsearch. If `hhsearch` is unavailable, do not keep retrying the same command; either install HHsuite in a suitable environment or run no-template AF2 and clearly record the caveat.
- For mutation workflows, name files with the exact changed residues and keep obsolete wrong-definition outputs out of interpretation.
