# Result-oriented human handoff

## Design

Retain CCDS separation of immutable inputs, intermediate/processed data, code and reports. Add a human view grouped by stable research module: Result/Figure numbering is display metadata, not the immutable module identity. Tool names and dates belong to execution, not the sole paper-writing entrypoint.

Use existing result/figure/source-data roots. Declare one navigation registry and generate a shallow Markdown index and, when useful, local HTML gallery. Do not create another source-data store or manually duplicate current lists. Dataset/run registries retain scientific authority; navigation references them instead of selecting a new baseline.

## Before a paper has Results

Do not force Result numbers or a desired conclusion onto exploratory work. Start with a few need-driven modules such as data intake/QC, a sequence comparison, structure analysis or a bounded hypothesis test. Give each a stable ID, question, inputs, method, outputs, status and next decision; `result_mapping` may be empty. Shared preprocessing is a dependency, not a duplicated Result module. Software is a backend attribute unless a tool benchmark is the research question.

Use explicit states such as planned, exploring, blocked, candidate, accepted or stopped; a negative result is not discarded. Retain alternatives and failure evidence with their constraints. Once the author accepts a paper outline, map modules/assets to Results many-to-many in the human view, without renaming historical run paths. Result 2 becoming Result 3 changes display mapping, not scientific provenance. Create only modules needed now, not a template full of empty folders. A root work index is sufficient before a Results index becomes meaningful.

## Registry fields

Minimum fields: `asset_id`, `module_id`, `scope`, `label`, `path`, `status`, `source_data`, `producer`, `command`, `environment`, `sha256`.

- Paths are project-root-relative. Optional fields hold consumer/evidence, scientific_run, presentation_run, acceptance and gaps.
- Scope separates scientific analysis, paper presentation and submission. Current is unique within `(scope, module_id, label)`; newest filenames do not choose it.
- Labels come from actual manuscript/report consumers or accepted mappings, not filenames.
- Unverified provenance is `pending`. Same-directory/run membership is only a hint, not producer proof.
- Shared source tables have one authority. Editing/submission copies are separate roles, not presumed identical.
- Historical manifests remain as-of snapshots; report stale snapshots rather than rewriting mismatch away.
- Standard status values include current, candidate, planned, exploring, blocked, failed, accepted, stopped, historical, superseded, as_of_record, provenance_pending, unverified_remote, reference, referenced, package_record and archived. Document project-specific values with an `x-` prefix; scope/module/label must be nonempty. Empty early-project registries are permitted but are not completed artifact handoffs.

## Human views

From root README expose Result index/gallery: figure preview, exact table, source, producer/command and coverage state. Use relative links, escape HTML metadata and preserve spaces in paths. No remote images/scripts/fonts or automatic fetches; remote manuscript figures are explicit external links marked unverified. Show missing fields instead of hiding them.

## New output contract

Before running name module, output root, candidate/current role and consumer. Keep runs/logs separate from fixed human entry. After authorized acceptance/update publish to declared current location or verified stable view, regenerate and validate navigation. An index does not excuse arbitrary future output roots. Relocation still needs migration map, consumer repair, rollback and authorization.

## Verification and provenance

Check existence, applicable hashes, unique current roles, consumer links and no external-resource loading. A reviewer unfamiliar with history must find a selected figure, source and producer from root navigation. Navigation validation is not scientific reproduction.

Mechanism-level synthesis checked 2026-09-28; no upstream templates copied:
- https://cookiecutter-data-science.drivendata.org/opinions/
- https://doi.org/10.1371/journal.pcbi.1005510
- https://github.com/buschman-lab/ProjectTemplate
- https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html
