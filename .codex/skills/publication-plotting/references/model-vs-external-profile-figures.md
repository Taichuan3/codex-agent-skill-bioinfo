# Model versus external profile figures

Use this reference when a figure compares a model prediction with an official processed target and/or a project-derived observed signal.

## Comparison objects

Keep the signal objects explicit:

- `A — model prediction`;
- `B — official processed target` identified by model or dataset metadata;
- `C — project observed signal` produced by the current processing workflow.

Plot only objects that exist, and label each comparison (`A vs B`, `B vs C`, `A vs C`). Do not call concordance “accuracy” without a predefined metric and reference truth.

## Figure design

- Pair magnitude views such as aligned heatmaps with continuous profiles when both overview and localization matter.
- Use comparable coordinate systems, strand conventions, transformations and fixed axes across rows intended for direct comparison.
- Show multiple scientifically justified resolutions when a narrow signal may be hidden by binning or smoothing.
- Put exact positions or events in a separate rug/event lane so they do not cover baselines or x-axis labels.
- Distinguish exact-source, related-context and proxy rows visually and in the caption.
- Show the full declared interval universe unless the user explicitly chooses a focal subset; mark selection criteria in the contract.

## Source data

Emit both summary- and trace-level tables when applicable:

- interval/region summary: comparison, interval, value, normalization and provenance;
- trace data: coordinate/bin, each raw or transformed signal, event-present flag and display transform.

Record reference assembly, resolution, smoothing, strand combination, normalization and any missing raw-data limitation.

## QA and claim boundary

- Re-open exports and inspect legends, rug lanes, colorbars, axes and region labels for overlap.
- Confirm fixed axes are appropriate and stated; otherwise label free scales clearly.
- A profile match is proxy concordance. A mismatch can reflect model, processing, reference, mapping or resolution differences and is not automatically model failure.
- An absence claim requires an exact signal object, threshold and resolution; unavailable raw data preclude robustness claims for untested processing choices.
