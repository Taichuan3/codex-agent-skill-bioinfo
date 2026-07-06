# Reader-facing report figure optimization notes

Use when converting internal/project figures into a reader-facing academic or seminar report.

## Reader-facing defaults

- The report body should show the result, not the internal audit trail. Keep provenance, scripts, source-data paths, and claim-boundary notes in internal notes or supplementary records, not beside every figure.
- Prefer figure captions and section headings over long in-plot titles/subtitles. Remove redundant `ax.set_title(...)` / `fig.suptitle(...)` when the report text already states the message.
- Prioritize legibility at report insertion size: enlarge tick labels, axis labels, legends, and direct labels before adding more detail.

## Pie-chart replacement pattern

For complex source composition, replace pie/donut charts with ordered horizontal bar charts:

1. Preserve the old output filename if the report already links to it, so existing Markdown paths do not break.
2. Sort categories by count or effect size.
3. Aggregate long tails into `other` when needed.
4. Use a restrained, low-saturation palette; gray for `other` / transformed / secondary categories.
5. Put counts and percentages at the bar ends.
6. Convert snake_case labels into reader-facing labels with spaces or slashes.
8. Verify no y-axis labels are clipped after export.

## Report-link synchronization pattern

When optimizing figures already embedded in a reader-facing Markdown report, decide explicitly whether the report should keep linking to the original analysis outputs or to a clean report-facing copy.

Use a clean report-facing copy when any of these apply:

- The original filename contains internal numbering or obsolete chart-type words (`figure_09O`, `figure_09S`, `*_pie.png`) that the user does not want in report source.
- Markdown/PDF preview may cache same-name images and hide the fact that a figure was redrawn.
- The report is being prepared as a standalone deliverable where images should live under a concise directory such as `figures/project_report/`.

Recommended steps:

1. Regenerate the canonical analysis PNG/SVG from the source script.
2. Copy only report-used PNG/SVG pairs into `figures/project_report/` with clean sequential names (`result2_05_histone_mark_class_signal_dotplot.png`, etc.).
3. Update `PROJECT_REPORT.md` image links to the clean copies.
4. Parse the Markdown and verify every linked PNG exists, every paired SVG exists, and all links are under the intended report directory.
5. Search the Markdown links for stale internal tokens (`figure_09`, `09O`, `09S`, `pie`) before telling the user the report is synchronized.

## Script/rerun pitfalls

- Some source-attribution scripts regenerate many figures at once. After rerun, keep the intended figure diffs and restore unrelated auto-refreshed outputs before committing.
- If the default Python lacks plotting libraries, use the project-specific conda environment rather than recording the failure as a durable limitation.
- Always verify both PNG and SVG exports exist after regeneration.

## Full-report integration pass

When the user asks to make “all figures” consistent across a reader-facing report, handle it as an inventory + rerun + QA workflow rather than isolated edits:

1. Parse the report Markdown for every `![alt](path)` image and verify both PNG and SVG siblings exist.
2. Map each inserted figure back to its generating script where possible. Patch scripts first so the style change is reproducible.
3. Apply one report-wide rule set: no internal figure numbers in plot titles, no oversized `suptitle`, no audit/provenance wording inside reader-facing figures, unified font sizes, stable color families, and stable output filenames.
4. Rerun the relevant scripts in the project environment; for scripts that regenerate many outputs, restore unrelated auto-refreshed files before summarizing or committing.
5. For legacy/report figures with no discoverable generating script, a minimal post-processing pass is acceptable: edit SVG viewBox or crop PNG/SVG in parallel to remove a redundant title, but explicitly record this as direct post-processing in the project notes.
6. Scan the report text and report-linked SVGs for forbidden stale strings after redesign (`Figure 09`, `Result 2 Figure`, old chart-type words such as `pie chart`, `raw-response provenance`, internal claim-boundary wording).
7. Do at least a small visual QA sample from each figure family; if QA reveals clipping or overlong labels, patch and rerun immediately rather than leaving it as a note.

## Integrated report-wide figure pass

When the user asks to optimize a whole report rather than one figure:

1. Parse the report Markdown and enumerate every `![alt](path)` image actually inserted in the reader-facing document.
2. Map each inserted image to the generating script; do not treat every output produced by a batch script as part of the report.
3. Apply global style rules consistently: remove internal in-plot numbering/titles (`Figure 09O`, `09S`, `Result 2 Figure 1`), enlarge labels, reserve caption/section heading for narrative, and keep filenames stable unless explicitly renaming paths.
4. Rerun generating scripts in the project plotting environment; if a batch script refreshes unrelated figures, restore non-report outputs before committing.
5. Verify all inserted PNGs exist and have paired SVGs; scan report-used SVGs for stale title tokens such as `Figure 09`, `Result 2 Figure`, `Figure 9.`.
6. Visual-QA the specific high-risk figures the user mentioned, not only file existence.

## Dotplot / heatmap legend layout

- Dot-size / outline legends often overlap rotated x-axis labels or footnotes when placed below a dense dotplot. Prefer a right-side legend column with `bbox_to_anchor` outside the axes and a smaller `right=` subplot area for the data panel.
- Keep colorbar and dot-size legend in separate right-side lanes; leave enough horizontal gap so colorbar tick labels and legend text do not collide.
- If the right-side area becomes too crowded, move explanatory text to caption/report prose and keep the in-figure legend minimal (`Dot size / outline`, support levels, mixed-direction marker).
- After moving legends, inspect the rendered PNG, not only the script: check overlap among data panel, x-axis labels, axis title, footnote, colorbar, and dot-size legend.

## Visual QA checklist for this pass

- No oversized in-plot title or subtitle.
- No internal figure numbering/title strings are visible inside report-facing figures.
- Labels are readable in the report, not only at full-resolution zoom.
- No left/right clipping of long labels or value annotations.
- Dotplot legends, colorbars, x-axis labels, and footnotes do not overlap. For dotplots with both a colorbar and dot-size/outline legend, do not rely on vertical colorbar labels beside the legend; use a compact colorbar title above the colorbar (e.g. `weighted\ndirectionality`) and place the dot-size legend in a separate right-side area. Re-open the final report-facing PNG after copying/synchronization and inspect this explicitly before final response.
- Palette is consistent with the figure role: primary evidence can be stronger; secondary/caveat figures should be visually quieter.
- Report text and alt text match the new chart type after a redesign, e.g. do not leave “pie chart” text after replacing with a bar chart.

