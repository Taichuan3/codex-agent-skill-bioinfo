# Citation Risk Types

- `verified`: identity and required claim-support evidence were inspected.
- `partially_verified`: metadata or abstract was verified, but required full-text evidence was unavailable.
- `unresolved`: citation identity could not be resolved within the recorded sources and search scope.
- `fabricated`: strong evidence shows the cited record does not exist or identifiers were invented; do not use this label for access failure alone.
- `metadata_error`: title, author, journal, year, DOI, or PMID does not match.
- `claim_mismatch`: paper exists but does not support the sentence.
- `scope_mismatch`: paper supports a narrower system, organism, cell type, dataset, or condition.
- `review_vs_primary`: review cited where primary evidence is needed.
- `method_only`: citation supports a method, not the biological conclusion.

Record the source and evidence location used for every status. Prefer `unresolved` or `partially_verified` when access is insufficient.
