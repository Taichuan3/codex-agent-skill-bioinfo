# Protein interaction / docking feasibility literature search notes

Use this reference when a user asks whether two proteins, a mutation, or a docking hypothesis has literature support.

## Recommended search decomposition

1. Direct interaction evidence
   - Query both gene/protein aliases and species variants.
   - Examples: `ACTN4 PHLDB2`, `alpha-actinin-4 LL5beta`, `Actn4 Phldb2`.
   - Check PubMed/PMC plus interaction databases such as IntAct/BioGRID/STRING.
   - Treat high-throughput co-IP/proximity datasets as weak network evidence unless the exact pair is directly reported and validated.
2. Mechanistic/domain evidence
   - Search domains, motifs, ligands, and pathway terms.
   - Examples: `alpha-actinin phosphoinositide PIP2 binding site`, `LL5beta PtdIns(3,4,5)P3 PH domain`.
3. Mutation rationale
   - Search exact residues/motifs first; if absent, look for homologous-family residues and biochemical logic.
   - Distinguish direct mutation evidence from indirect charge/motif rationale.
4. Feasibility synthesis
   - Separate: direct binding evidence, shared pathway/localization evidence, domain compatibility, and computational-only hypotheses.

## Evidence grading reminders

- Direct low-throughput binding/co-IP/pulldown with the exact pair: Moderate to Strong depending on validation.
- Interaction database entry from high-throughput datasets only: Weak unless supported by the original paper and orthogonal validation.
- Shared localization/pathway or common scaffold: Exploratory, not direct interaction.
- Motif/domain annotation plus homologous mutagenesis: Moderate for rationale, weak for exact residue claim.
- Docking output without experimental validation: Exploratory.

## Useful reporting pattern

- State explicitly when direct interaction literature was not found.
- Provide a table with: question, citation/source, supported claim, evidence level, and caveat.
- For docking feasibility, recommend the narrowest model supported by literature first (e.g. ligand/headgroup or domain fragment before full-length protein-protein docking).
- Avoid upgrading a computational or indirect-network result into a claim of direct physical interaction.

## Session-derived example: ACTN4 / PHLDB2 / PIP3

- PubMed search found no clear title/abstract evidence for direct ACTN4–PHLDB2 binding.
- IntAct/high-throughput network evidence can show ACTN4 and PHLDB2 in cytoskeletal/scaffold contexts, but this is weak and not a direct interaction claim.
- ACTN4 has a phosphoinositide-binding region overlapping mouse ACTN4 residues ~176–194; alpha-actinin-family PIP2-binding evidence supports a Lys/Arg-rich motif rationale.
- K→A and K→E mutations can be justified as loss-of-positive-charge and charge-reversal tests, respectively, but should not be described as previously proven residue-specific ACTN4 PIP3 mutations unless a direct paper is found.
- PHLDB2/LL5β has stronger literature as a PIP3-sensitive PH-domain scaffold, linking PIP3-rich membrane regions to filamin/actin and microtubule-associated platforms.
- Feasibility conclusion: ACTN4–PIP3/headgroup docking is better supported than full-length ACTN4–PHLDB2 docking; direct protein-protein docking should be framed as exploratory hypothesis generation.
