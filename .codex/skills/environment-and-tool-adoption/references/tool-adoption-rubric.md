# Tool Adoption Rubric

## Source review

Check before adopting external code:

- Source: official project, package registry, paper, protocol, or upstream repository.
- Maintenance: releases, issue response, compatibility statements, documentation, and archived/deprecated status. Popularity is supporting context, not proof of quality.
- License: compatible with intended use.
- Installation: package manager, container, source build, system dependencies.
- Inputs/outputs: match local data or need wrappers.
- Method fit: supported organism/assay/platform, scale, assumptions, expected baseline, and known limitations.
- Reproducibility: version, digest, seeds, environment, model weights, reference databases, and test data.
- Security: install scripts, binary provenance, network behavior, credential needs, and unsafe deserialization.
- Citation: paper, DOI, software citation or URL.

## Decision

| Choice | Use when |
|---|---|
| Use directly | Mature, documented, licensed and matches task. |
| Wrap locally | Good tool but needs input/output conversion. |
| Borrow ideas | Useful method but code is hard to run or maintain. |
| Rewrite | Code is unsafe, unlicensed, obsolete, incompatible, or the needed logic is small. |

Do not rewrite a validated domain method merely to avoid installation. Do not adopt external code merely because it is popular or published.

## Installation preference

Choose the smallest method that preserves isolation and reproducibility:

1. existing compatible environment;
2. project environment or lock file;
3. trusted package manager with pinned version;
4. verified container or binary;
5. reviewed source build.

System-wide or administrator-level changes require an explicit reason and action-specific approval.

## Validation levels

- Availability: import, `--version`, `--help`, or executable lookup.
- Smoke test: synthetic or bundled test input produces expected schema and exit behavior.
- Integration: local wrapper, paths, reference assets, and downstream consumer work together.
- Scientific validation: benchmark or domain control supports method fitness.

Report the highest level actually completed. Do not call availability or smoke testing scientific validation.

## Install record

```text
Tool/package:
Version:
Source:
License:
Install command:
Verification command:
Local adaptation:
Citation:
Validation level:
Rollback/uninstall:
Known limitations:
```
