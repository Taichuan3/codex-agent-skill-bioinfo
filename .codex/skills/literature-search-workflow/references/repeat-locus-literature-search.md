# Repeat or locus hypothesis literature search

Use this reference to connect an unpublished locus/repeat hypothesis with literature and public datasets without collapsing distinct evidence layers.

## Evidence-layer map

| Layer | Typical evidence | What it can test | Common boundary |
|---|---|---|---|
| Expression | RNA-seq, targeted RNA assays, perturbation expression | abundance and context specificity | negative abundance does not test DNA/contact mechanisms |
| Sequence or structure | complete assemblies, long reads, comparative genomics | architecture, copy state, conservation and variation | structure alone does not establish function |
| Motif or occupancy | motif scans, ChIP-seq, CUT&RUN/CUT&Tag, footprints | sequence compatibility or occupancy | motif hits do not prove binding; occupancy does not prove regulation |
| 3D contact | Hi-C, Micro-C, targeted contact assays | spatial association | contact does not prove activation or causality |
| DNA rearrangement | WGS, long reads, split/clipped reads, assemblies | breakpoint or insertion evidence | enrichment alone is not a validated breakpoint |

## Search sequence

1. Write a one-paragraph hypothesis that names the locus, relevant structure, biological context and candidate molecular interface.
2. Turn each evidence layer into a separate search question and query; do not use one negative layer to reject a different mechanism.
3. Start dataset discovery from Data Availability, repository study records and supplementary methods.
4. Resolve study-level accessions to sample/run records and verify assay, organism, context, perturbation, replicate, control, library layout, read length and public availability.
5. Record reference assembly, mapping strategy, multi-mapping policy and whether the assay can distinguish locus-specific from family-level signal.
6. Grade every supported claim and record what the paper or dataset cannot prove.

## Dataset evidence table

| Dataset | Assay | Sample/context | Target or perturbation | Input/control | Reference and mapping caveat | What it can test | What it cannot prove | Priority |
|---|---|---|---|---|---|---|---|---|

## Interpretation guardrails

- Negative RNA evidence constrains an RNA-abundance mechanism only when assay power, context and locus quantification are adequate.
- Repeat-rich signals require explicit unique versus multi-mapping sensitivity and reference dependence.
- Motif enrichment, chromatin occupancy, contact and rearrangement are distinct observations; do not combine them into a causal chain without direct validation.
- Keep unpublished details minimal in reusable public-facing artifacts and never copy private paths or raw project tables into a generic reference.
