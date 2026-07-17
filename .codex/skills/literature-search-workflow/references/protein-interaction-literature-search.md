# Protein interaction / docking feasibility literature search notes

Use this reference when a user asks whether two proteins, a mutation, or a docking hypothesis has literature support.

## Recommended search decomposition

1. Direct interaction evidence
   - Query both gene/protein aliases and species variants.
   - Combine canonical symbols, protein names, family aliases and species-specific forms for both partners.
   - Check PubMed/PMC plus interaction databases such as IntAct/BioGRID/STRING.
   - Treat high-throughput co-IP/proximity datasets as weak network evidence unless the exact pair is directly reported and validated.
2. Mechanistic/domain evidence
   - Search domains, motifs, ligands, and pathway terms.
   - Query each partner with the candidate domain, motif, ligand and pathway terms rather than relying on the pair name alone.
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
