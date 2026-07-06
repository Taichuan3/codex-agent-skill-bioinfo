# FAIR Manifest and Source Data

## Practical FAIR checks

| Principle | Check |
|---|---|
| Findable | Stable filename, manifest row, related figure/table, persistent identifier when deposited |
| Accessible | Clear path, repository/accession or availability route |
| Interoperable | Open format where possible, clear columns, units and identifiers |
| Reusable | Provenance, script, environment, filtering and licence/access notes |

## Manifest fields

- `id`
- `file_path`
- `file_type`
- `status`
- `latest`
- `related_claim`
- `related_figure`
- `source_input`
- `script`
- `environment`
- `updated_at`
- `notes`

## Dataset README minimum

- Summary
- Files
- Variables and units
- Methods and provenance
- Software and environment
- Access and licence
- Citation or preferred acknowledgement

## Blocking issues

- Figure source data absent for a central claim.
- Data availability statement promises unavailable files.
- Raw and processed data are mixed without provenance.
- Important tables are buried in ambiguous nested output folders.
- Latest result cannot be identified.
