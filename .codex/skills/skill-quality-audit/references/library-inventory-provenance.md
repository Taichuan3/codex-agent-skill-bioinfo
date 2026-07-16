# Skill/Agent Library Inventory and Provenance

Use this reference when the task is library-wide: inventorying all local skills/agents, deciding what is canonical, or publishing a curated Git branch.

## Core principle

Do not equate every discovered `SKILL.md` with an independent user-owned skill. A machine-wide scan commonly includes runtime mirrors, canonical sources, project copies, bundled/Hub/upstream material, temporary clones, historical backups, and private self-models. Bulk-copying them creates license, provenance, trigger, and stale-version problems.

## Two-pass inventory

### Pass 1: broad discovery

Discover, without reading unrelated project data:

- `SKILL.md`;
- `AGENTS.md`, `CLAUDE.md`, `HERMES.md`, `.hermes.md`;
- agent metadata under `agents/`;
- Git roots, origins, branches, and dirty state.

Exclude dependency/build trees, `.git/objects`, large data/results, and OS caches. Count broad hits only as raw discovery evidence.

### Pass 2: provenance-aware catalog

Classify each active asset as one of:

1. `canonical-source` — installable source maintained in a real repo;
2. `runtime-mirror` — installed Hermes/Codex copy; compare before promotion;
3. `project-specific` — belongs to one private project;
4. `bundled-or-upstream` — preserve source/license; reference rather than vendor;
5. `cache-or-archive` — exclude from active catalog;
6. `personal-local-only` — self-model, chat distillation, relationship/life profile, or raw private context; never upload automatically.

A machine-readable manifest should use home-relative paths and include at least:

- kind and logical name;
- relative path;
- SHA-256 and byte size;
- provenance class;
- upload policy;
- Git root/origin/branch when applicable;
- concise reason for the policy.

Do not include file contents, credentials, session transcripts, memories, raw research data, or manuscript content in the inventory.

## Canonical and drift decisions

For a logical skill present in source, Hermes runtime, Codex runtime, and project mirrors:

1. compare names, frontmatter, linked files, and hashes;
2. treat runtime as an important source of user-tested improvements, not an automatic winner;
3. treat old project copies as mirrors unless they contain project-specific mechanisms worth extracting;
4. perform semantic three-way comparison for drift;
5. backport stable mechanisms to the canonical source branch;
6. never replace a newer runtime body with an older GitHub body merely because GitHub is remote.

Prefer class-level umbrella skills plus `references/` over many snapshot skills.

## Repository mapping

Map assets by ownership rather than convenience:

- general reusable domain skills → their canonical skill repo;
- project-specific agent/skill → private project repo or a private curated catalog;
- bundled/Hub/third-party skills → upstream reference only;
- personal self-mirror → local-only unless the user explicitly authorizes fields, redaction, visibility, and destination.

If a project worktree is heavily dirty, do not mix cataloging with project changes. Save a reviewed private snapshot in the catalog and defer project-repo integration.

## Branch and privacy gates

- Push only to the user-authorized review/working branch; never update `main` without explicit permission.
- Prefer a private catalog when inventory contains private project names or machine topology.
- Normalize absolute home paths to `~` in portable copies and manifests.
- Check remote URLs for embedded credentials before writing them to a manifest.
- Scan staged content for secrets, personal-local-only paths, large files, CRLF/trailing-whitespace issues, and unexpected project artifacts.
- Verify remote visibility, default branch, pushed commit, and clean worktree after push.

## Common pitfalls

- Raw hit counts are not canonical skill counts.
- Do not re-publish third-party skill bodies without license/provenance review.
- Do not let a catalog recursively treat its curated snapshots as new canonicals; classify the catalog explicitly.
- CSV writers may emit CRLF by default; set a deterministic line terminator before `git diff --check`.
- A private GitHub repo is still not appropriate for raw chats, self-model source material, credentials, controlled data, or unpublished sensitive research.

## Delivery report

Report:

- broad discovery counts and curated counts separately;
- canonical source map;
- what was copied versus reference-only versus excluded;
- sensitive assets kept local-only;
- drift requiring later semantic merge;
- repository/branch/visibility and commit state;
- verification scope and remaining risks.
