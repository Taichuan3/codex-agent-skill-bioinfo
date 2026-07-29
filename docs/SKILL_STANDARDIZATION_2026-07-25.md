# 37-Skill standardization record — 2026-07-25

> Historical snapshot: this record freezes the 2026-07-25 37-Skill baseline.
> Current counts, entrypoints, post-baseline lineage, and validation commands
> are defined by `local_config.yaml`, `README.md`, and
> `docs/EXTERNAL_FILE_LINEAGE_POST_BASELINE.tsv`.

## Scope and provenance

- Repository: `Taichuan3/codex-agent-skill-bioinfo`
- Working branch: `agent/bioinfo-multidevice-package`
- Pre-batch base commit: `15a0c0b7a51018c239fec8214cae01140d04fed8`
- Baseline Skills: `research-data-organization`, `project-state-maintenance`, `project-guide-maintainer`, `project-directory-card-maintenance`
- Change class: public-safe, cross-project bioinformatics capability source

This pass standardized the existing 37 portable Skills. It did not import a new third-party corpus or add project-specific Skills. Existing domain knowledge was retained or reorganized through mechanism-level keep/merge decisions. Historical external-corpus provenance was reconstructed from earlier audit commits in `docs/EXTERNAL_SOURCE_PROVENANCE.md`; `NOTICE.md` preserves the remaining stable-review boundary.

The reconstructed gate also includes 62 file-level current/tombstone lineage
rows, conservative third-party notices, and 18 exact-ref expression comparisons
covering seven current Skill bodies. Every comparison recorded zero shared
normalized 40-character shingles and zero identical normalized lines of at
least 35 characters; this is evidence of independent rewriting, not a legal
determination.

## Standard contract

Every Skill now provides:

1. `SKILL.md` frontmatter containing only `name` and `description`.
2. One primary deliverable, explicit neighbor routing, authority and evidence boundaries, a bounded workflow, and a delivery contract.
3. One-level `references/`, `scripts/`, or `assets/` loaded only when directly routed from `SKILL.md`.
4. `agents/openai.yaml` containing only quoted `display_name`, 25–64 character `short_description`, and a `default_prompt` naming `$skill-name`.
5. Exactly 20 trigger cases: 10 positive, 10 negative, 10 train, 10 validation, with five positive and five negative cases in each split.
6. At least five outcome cases with required and prohibited behaviors.

The eval JSON files are static routing and outcome specifications. Package validation checks their structure, balance, owner consistency and duplicate-query conflicts; it does not run a model or prove behavioral compliance.

## Capability groups

| Group | Primary separation |
|---|---|
| Research design | question brief vs project plan vs decision review vs claim validation vs delivery QA |
| Literature and evidence | literature search vs paper reading vs database grounding vs citation verification vs evidence gaps |
| Claims and publication | claim support vs source data vs manuscript consistency vs submission gate vs simulated/real review |
| Scientific writing | Chinese polishing vs translation vs existing-English polishing vs figure caption |
| Analysis and figures | reproducible code vs publication plotting vs pathway/network analysis |
| Genomics | RNA/scRNA execution vs variant/statistical genetics vs clinical/translational evidence |
| Structure and drug discovery | structure/docking evidence vs campaign/QSAR/ADMET prioritization |
| Machine learning | fair biomedical benchmark, leakage, generalization and model-card boundaries |
| Environment and governance | project bootstrap vs tool adoption vs Skill QA vs controlled capability evolution |

## Context impact

For the 33 Skills processed after the four-Skill pilot:

- `SKILL.md` lines changed from 1,989 to 1,656.
- `SKILL.md` characters changed from 68,168 to 73,829 because concise English fragments were replaced with more explicit Chinese ownership, safety and routing contracts.
- Always-visible trigger descriptions changed from 4,679 to 6,251 characters to reduce close-neighbor ambiguity.

Progressive disclosure is measured primarily by shorter loaded bodies and direct reference routing, not by deleting domain evidence boundaries.

## Validation evidence

- 37/37 Skill Creator structural checks passed.
- Package validation passed for 37 Skills, 6 custom Agents, static eval schemas, discovery link, manifest counts and privacy patterns.
- Trigger corpus: 740 cases. Outcome corpus: 193 cases.
- Blind frontmatter-only forward routing: 37/37 representative requests routed to the intended primary Skill. Raw requests and observed routes are recorded in `ROUTING_FORWARD_TEST_2026-07-25.tsv`.
- Independent claim/evidence review passed after fixing replication/generalization wording, perturbation/mechanism limits, clinical safety routing, reviewer-response anti-fabrication, and user decision ownership.
- Installer fixtures passed clean apply, idempotence, dirty-source refusal, preflight failure safety, transaction rollback, source revision/digest reporting, and privacy leak rejection.
- Release-safety fixtures reject native memory/log/session paths, SQLite/DB artifacts, nested project-environment records, and symlinked guidance/custom-Agent destinations without changing their topology.
- Historical source validation matches the 62-row lineage to all paths touched
  by the four absorption commits, checks source/ref/path key parity and full
  SHAs, preserves BioNeMo's mixed license and the K-Dense exception, and
  validates all 18 expression-review rows.
- Historical note: runtime discovery originally used a repository Skill symlink. The cross-platform installer now owns the user-global discovery entry; parity is checked against the clean reviewed commit, release digest, and Windows managed-copy marker when applicable.

## Public-package exclusions

The package excludes:

- native memory, sessions, cache, SQLite and generated runtime state;
- credentials, SSH/OAuth material and embedded remote tokens;
- personal or machine-specific paths and environment records;
- raw research data, patient-identifiable data and large result artifacts;
- unpublished project facts, parameters, claims and server topology;
- finance, investment and other non-bioinformatics workflows;
- unreviewed third-party Skill bodies or license-unclear material.

The repository is source-visible but does not currently grant an open-source reuse license. `LICENSE` defines the package-wide permission boundary and `NOTICE.md` records third-party provenance handling.

## Publication and rollback

The authorized action is commit and push of this feature branch. This record does not authorize merge or update of `main`. The branch is a review candidate, not a stable or license-cleared release; the reconstructed provenance and K-Dense snapshot exception in `NOTICE.md` require explicit stable review first.

The published Git commit is the immutable source pointer. Rollback uses a normal Git revert on the feature branch or checks out the prior reviewed commit; remote history must not be rewritten. Re-run package validation, representative routing tests, installer fixtures and runtime discovery/parity after rollback.

### Routing replay protocol

1. Start a fresh Codex task or subagent with access to this repository.
2. Permit reading only each `SKILL.md` frontmatter `name` and `description`; prohibit reading eval JSON, Skill bodies and this result file.
3. Present the TSV queries by group and require exactly one primary Skill, with an optional secondary only when strictly necessary.
4. Record the observed primary route and runtime/build identifier if exposed.
5. Compare observed to expected and retain mismatches. This is a manual model forward test, not an automated or deterministic harness.
