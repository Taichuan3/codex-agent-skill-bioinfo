# External-facing bioinformatics report polishing and bundling notes

Use when a Chinese scientific report is intended for an external reader rather than the author. Report bundling is a separate material action: do it only when the user requests a bundle, and combine with `research-data-organization` when artifact selection or manifest work is needed.

## Text cleanup

- Remove author-directed editing commands and collaboration traces such as `给自己看`, `作者内部`, `TODO`, strike-through revision marks, or user-agent discussion. Do not remove a sentence merely because it contains “不能证明” or “安全边界”: a limitation such as “未见显著差异不能证明等价” is scientific content and must remain. Preserve unresolved scientific issues from deleted annotations in author actions and retain any conclusion-changing qualification in the prose.
- Reduce gratuitous repetition, but preserve meaningful author voice such as `我们提出/发现/检验`; impersonal phrasing is optional, not a blanket replacement.
- Keep evidence boundaries through neutral wording, but do not repeat defensive caveats in every section.
- Report/paper structure should improve readability; do not make prose dense or scripture-like just to sound formal.

## Source-data and reproducibility materials

- Do not place long local path indexes in the report body. Instead, create a report bundle such as `reports/<report_name>/` containing:
  - final report markdown/copy for sharing;
  - compressed reproducibility package;
  - optional unpacked package for local inspection;
  - source-data index;
  - README and MANIFEST/checksums.
- For a small report-level reproducibility package, include curated inputs, summary/source tables, selected scripts, environment files and checksums; exclude raw sequencing files, full references and caches unless explicitly requested and appropriate.
- Prefer English filenames and README/MANIFEST in the package, even if the report body is Chinese.

## Citations and conversion compatibility

- For Markdown that will later be translated and exported to DOCX/PDF, numbered Nature-style references with HTML superscripts (`<sup>1</sup>`, `<sup>1,2</sup>`) are robust and simple.
- Avoid Zotero field codes in plain Markdown unless the downstream DOCX workflow explicitly requires them.
- When using reference-manager metadata, keep the source database read-only; never modify a live citation database from a report-polishing session.
