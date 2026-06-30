# Report Figure Integration

Use this reference when figures are already embedded in a reader-facing report, manuscript draft, slide deck, or supplement. It compresses mature runtime lessons while keeping project-specific examples out of the always-loaded `SKILL.md`.

## Reader-facing defaults

- The report body should show the result, not the internal audit trail. Keep provenance, scripts, source-data paths and claim-boundary notes in Methods, supplement, source-data index or author notes unless the user explicitly wants them in the main text.
- Prefer section headings and captions over long in-plot titles/subtitles. Remove redundant `suptitle` / internal plot titles when the surrounding text already states the message.
- Prioritize legibility at insertion size: enlarge tick labels, axis labels, legends and direct labels before adding more detail.
- Use reader-facing labels rather than internal IDs when possible; preserve exact paths and IDs in provenance/source-data records.

## Inventory-first workflow

1. Parse the report/slide source for actually inserted images.
2. Verify each inserted PNG exists and, when expected, has a paired SVG.
3. Map each inserted image to the generating script or direct-edit source.
4. Modify the script first when a reproducible generator exists.
5. If batch scripts regenerate unrelated figures, keep the intended report diffs and restore unrelated auto-refreshed outputs.
6. Re-open or visually inspect high-risk outputs before reporting completion.

## Path and link synchronization

When optimizing figures already linked from Markdown or PPT, decide whether to keep the original path or create a clean report-facing copy.

Keep the original path when:

- the user asked to modify a specific existing figure;
- filename stability matters more than clean naming;
- the edit is a direct replacement and the report link should not move.

Create a clean report-facing copy when:

- the original filename contains internal numbering or obsolete chart-type words;
- preview/PDF caching may hide same-name redraws;
- the report is becoming a standalone deliverable with a curated `figures/project_report/` directory.

After moving or copying, update the document links in the same pass and search for stale tokens such as old figure numbers, `pie chart`, internal panel IDs, or previous alt text.

## Main versus supplement movement

- If a figure is promoted from supplement to main text, remove duplicate supplementary display.
- If a main figure is replaced by a better one but the old screened figure remains useful, move it to supplement instead of silently dropping it.
- Renumber local figure labels and supplementary captions after moving figures.
- Captions should remain explanatory: panels, axes, encodings, data universe, n/denominators and normalization. Results prose carries interpretation and evidence boundaries.

## Common redesign patterns

### Complex source composition

Prefer ordered bar charts, dot plots or heatmaps over pie/donut charts when categories are many or when the figure must support a narrative layer. Sort categories, aggregate long tails, show counts/percentages when useful, and align categories with the Results logic rather than convenient metadata columns.

### Dense dotplot / heatmap legends

Place colorbars and dot-size/outline legends in separate lanes. Avoid putting legends below dense rotated x-axis labels. Inspect the rendered PNG, not only the script, for overlap among axis labels, footnotes, colorbar and legend.

### Raw output versus attribution layers

When readers need both raw model output and attribution layers, show the raw/model-native output first if it is the clearest first-pass evidence, then show custom atlas/source-attribution layers. Do not let an attribution summary substitute for the raw signal overview when the raw signal is the claim's starting point.

## Verification checklist

- Every linked image exists.
- Expected paired SVG/PDF exports exist.
- No duplicate display after figure movement.
- No stale internal figure names or old chart-type descriptions remain in Markdown/PPT/captions.
- Insertion-size readability is checked for labels, legends, colorbars and panel labels.
- Source-data or provenance index exists when the figure is used as evidence.
