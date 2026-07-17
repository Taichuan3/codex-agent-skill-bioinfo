# Visual QA

## Readability

- Paper multi-panel figures: usually 6.5-8 pt final text.
- PPT or presentation figures: usually 12-18 pt final text.
- Axis labels, tick labels, legends and panel labels must remain readable after export.
- Avoid negative spacing and crowded labels.

## Layout

- Check that labels, legends, data points, error bars and panel letters do not overlap.
- Use direct labels when legends force eye travel or cover data.
- Remove dead margins and repeated legends.
- Align comparable axes across panels.

## Crop, replacement and relinking

- Prefer regeneration from source data and script. If direct cropping is necessary, preserve complete semantic units: labels, scale/ticks, data marks and required annotations.
- Record the source file, crop bounds or transform, and whether the canonical or report-facing output was replaced.
- Inspect crop boundaries for fragments from adjacent panels and for removed scale/context.
- After replacement or relinking, verify document links, captions, alt text, numbering and source-data pointers in the same pass.
- A crop changes presentation, not evidence strength; it must not imply that omitted observations were absent from the source universe.

## Color

- Prefer one neutral family, one signal family and one accent family.
- Avoid rainbow colormaps.
- Do not rely on red/green as the only encoding.
- Check grayscale interpretability for key contrasts.
- Use consistent colors for the same condition across panels.

## Export

- Default deliverables: PNG + SVG.
- Final submission may add PDF/TIFF according to journal requirements.
- SVG/PDF text should remain editable when possible.
- Reopen exports and compare PNG/SVG visual consistency.
- Inspect the final document-facing copy after any copy, crop or cache-busting rename; checking only the canonical source image is insufficient.

## Statistics and source data

For quantitative panels, record:

- `n` definition
- biological/technical replicate definition
- center and spread
- statistical test and correction
- source-data file

For image panels, record:

- raw file or source
- processed file
- crop/contrast/pseudocolor notes
- scale calibration
- quantification link
