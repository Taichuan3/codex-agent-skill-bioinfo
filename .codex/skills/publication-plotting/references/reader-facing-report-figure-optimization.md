# Reader-facing report figure integration

Use this reference when figures are embedded in a manuscript draft, report, slide deck or supplement and must be made consistent, readable and traceable.

## Inventory first

1. Parse the document source and enumerate only the images actually inserted.
2. Map each image to its generating script, source data and canonical output where possible.
3. Verify linked files and expected paired exports exist.
4. Apply one document-wide rule set for typography, color, titles, caption style and insertion-size readability.
5. Re-open high-risk rendered outputs after regeneration or direct editing.

Batch scripts may regenerate unrelated figures. Keep the intended document-used changes and avoid carrying unrelated output drift into the task.

## Reader-facing defaults

- Show results in the document body; keep detailed provenance and internal claim notes in Methods, supplement, source-data index or author notes.
- Let section headings and captions carry the narrative. Remove redundant in-plot titles and internal identifiers.
- Captions explain panels, axes, encodings, data universe, n/denominators, normalization and key parameters. Results prose carries interpretation and caveats.
- Prefer ordered bars, dot plots, heatmaps or small multiples for complex composition. Keep labels aligned with the user-confirmed Results logic rather than convenient metadata fields.

## Link and placement synchronization

- Keep a stable path for a direct replacement when document continuity matters.
- Use a clean report-facing copy when the canonical analysis filename is unsuitable, caching obscures a redraw, or the deliverable needs a curated image directory.
- After any crop, replacement, copy, rename or move, update image links, caption, alt text, local numbering and surrounding citations in the same pass.
- When promoting a figure to main text, remove duplicate supplementary display. When a replaced figure remains useful, retain it in supplement only with updated numbering.
- Verify no stale chart-type wording, internal identifiers, duplicate displays or missing image links remain.

## Reproducibility boundary

Patch the generating script first when a compatible generator exists. Direct SVG or raster post-processing is acceptable only when regeneration is unavailable or disproportionate; record crop bounds, transforms and source file so the edit can be traced.

## Verification

- Every linked image exists and expected sibling export is present.
- Captions and alt text match the final chart and data universe.
- Main/supplement placement is unique and follows the user-confirmed figure logic.
- Labels, legends, colorbars and annotations remain readable at insertion size.
- Source-data/provenance pointers remain connected after relinking.
