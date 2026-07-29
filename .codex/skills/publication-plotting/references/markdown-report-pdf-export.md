# Markdown report PDF export workflow

Use when the user asks to save/export a Markdown research report as PDF, especially when the report contains many local figure links.

## Preferred workflow

1. Keep the source Markdown unchanged unless the user asks for content edits.
2. Create a small export stylesheet next to the report, e.g. `pdf_export.css`, with:
   - `@page { size: A4; margin: ... }`
   - readable body font/line-height
   - `img { max-width: 100%; height: auto; page-break-inside: avoid; }`
   - table/caption/small-text styling
3. Use `md-to-pdf` when available because it handles local relative image links well via Chromium/Puppeteer:

```bash
npx --yes md-to-pdf REPORT.md \
  --stylesheet pdf_export.css \
  --pdf-options '{"format":"A4","printBackground":true,"margin":{"top":"18mm","right":"16mm","bottom":"18mm","left":"16mm"}}'
```

4. Output path should normally share the Markdown basename: `REPORT.pdf`.

## Verification pattern

Use a focused temporary `hermes-verify-*.py` script when the export CSS or PDF output is a changed artifact. Check:

- CSS exists and contains key tokens (`@page`, `size: A4`, `font-family`, `img`, `max-width: 100%`).
- PDF exists, is non-empty, starts with `%PDF-`, and is large enough for a figure-rich report.
- macOS metadata recognizes it as PDF and page count is reasonable:

```bash
mdls -raw -name kMDItemContentType REPORT.pdf
mdls -raw -name kMDItemNumberOfPages REPORT.pdf
```

- Count Markdown images and embedded PDF image objects:

```python
md_images = sum(1 for line in md.read_text().splitlines() if line.startswith('!['))
image_objects = pdf_bytes.count(b'/Subtype /Image')
```

- Generate a QuickLook preview for a visual smoke test on macOS:

```bash
qlmanage -t -s 1000 -o /tmp/report_pdf_preview REPORT.pdf
```

If the user provided contact details in front matter, remind them to decide whether phone/email should remain visible before public sharing.
