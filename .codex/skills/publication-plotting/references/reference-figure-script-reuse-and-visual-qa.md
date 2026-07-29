# Reference figure script reuse and visual QA

Session lesson from model-output report figure revision.

## Trigger

Use this when the user says a new or revised figure should “参考” an existing figure, e.g. “参考 `result3_06_matched_cage_external_vs_alphagenome.png` 的画法”.

## Durable workflow

1. Treat “reference this figure” as two requirements, not only a visual-style request:
   - absorb the visual style/layout; and
   - search locally for the script that generated the reference figure.
2. Prefer modifying or extending the existing generating script, source-data table, and output path pattern.
3. Only write a new standalone script when the original script cannot be found, is unrelated to the requested data resolution, or would be riskier to modify.
4. If a new helper is unavoidable, document why and keep the output filenames/source-data contract compatible with the existing figure family.
5. Preserve stable report-facing image paths where possible to avoid Markdown/PDF link churn.

## Visual QA pitfall

For dense profile plots with rugs/ticks/CTSS markers, verify that marker lanes do not cover x-axis labels or baseline traces. If markers overlap the axis, move them into a dedicated rug lane by extending the y-axis lower bound and using short `vlines` rather than plotting markers directly on top of the tick-label area.

## Verification checklist

- Original plotting script searched and either reused or explicitly ruled out.
- PNG and SVG regenerated.
- Source data regenerated or confirmed unchanged.
- Visual QA checks label overlap, legend overlap, axis range comparability, and marker/rug lane placement.
- Ad-hoc verification confirms figure files and source tables exist and expected dimensions/rows are present.
