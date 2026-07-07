# External-facing bioinformatics report polishing and bundling notes

Use when a Chinese scientific report is intended for an external reader (TA, collaborator, reviewer) rather than the author.

## Text cleanup

- Remove internal editing notes and collaboration traces: `给自己看`, `作者内部`, `安全边界`, `不能证明/不能写成`, `TODO`, strike-through deletions, or parenthetical user-agent discussion.
- Prefer `本研究`, `本报告`, `本节`, or passive phrasing over repeated first-person `我们`.
- Keep evidence boundaries through neutral wording, but do not repeat defensive caveats in every section.
- Report/paper structure should improve readability; do not make prose dense or scripture-like just to sound formal.

## Source-data and reproducibility materials

- Do not place long local path indexes in the report body. Instead, create a report bundle such as `reports/<report_name>/` containing:
  - final report markdown/copy for sharing;
  - compressed reproducibility package;
  - optional unpacked package for local inspection;
  - source-data index;
  - README and MANIFEST/checksums.
- For a small report-level reproducibility package, include curated inputs, summary/source tables, selected scripts, environment files and checksums; exclude raw FASTQ/BAM/full reference/API-cache unless explicitly requested.
- Prefer English filenames and README/MANIFEST in the package, even if the report body is Chinese.

## Citations and conversion compatibility

- For Markdown that will later be translated and exported to DOCX/PDF, numbered Nature-style references with HTML superscripts (`<sup>1</sup>`, `<sup>1,2</sup>`) are robust and simple.
- Avoid Zotero field codes in plain Markdown unless the downstream DOCX workflow explicitly requires them.
- When using Zotero metadata, query a temporary copy of `zotero.sqlite` read-only if the live database is locked; never modify Zotero directly from a report-polishing session.
