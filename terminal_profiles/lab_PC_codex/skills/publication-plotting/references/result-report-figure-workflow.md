# Result-report figure workflow notes

Use this when revising a manuscript-style project report that mixes raw model outputs and custom attribution layers.

## Recommended narrative/figure order

1. Start with the model-native output layer if it is how the user or reader first sees the signal.
   - For sequence/regulatory prediction models, define `output type` as the model-native returned signal/data category (e.g. CAGE-like signal, PRO-cap-like signal, ATAC, DNase, RNA-seq, TF binding, histone marks).
   - Show the raw or output-type profile figure before derived dotplots when it is the clearest visual scan of whether signal exists and where it lies.
2. Then move to custom atlas/source-attribution layers.
   - Example layers: histone/TF/target, organ-module, disease/proxy, cohort/source attribution.
   - Make framework figures and section prose use the same layers as the downstream result narrative.
3. If a main-text figure is replaced by a more suitable figure, move the old screened/optimized figure to supplement if it remains useful. Do not silently drop it.

## Caption vs prose boundary

- Caption explains how to read the figure: panels, axes, rows/columns, colors, point size, n/denominators, normalization, and data universe.
- Results prose interprets the figure: what signal is observed, what it suggests, which regions are prioritized, and what the evidence boundary is.
- Avoid putting internal audit phrasing such as “cannot write as…” in reader-facing captions. If a caveat is necessary in a caption, make it a concise data-scope statement.

## QA checks

- The first figure in a result subsection matches the first narrative claim.
- Figure links are unique and resolve.
- A promoted figure is removed from supplementary duplicate display.
- Replaced but still-useful figures remain visible in supplement with renumbered captions.
- Section-specific inline comments/bracket notes are removed after integration.
