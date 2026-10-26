# Scientific English Translation Stance

## Translation priorities

1. Preserve scientific meaning.
2. Preserve evidence boundary.
3. Preserve user-provided or source-defined terminology.
4. Improve clarity and flow.
5. Add journal-leaning style only when safe.

## Terminology map

Before translating complex manuscript text, identify key terms that must stay stable.

| Chinese source term | Preferred English term | Avoid / only use if distinct | Note |
|---|---|---|---|
|  |  |  |  |

Rules:

- One concept should map to one English term.
- Do not introduce synonym variation for readability if it changes the apparent object.
- If the Chinese source uses multiple words for the same concept, choose one preferred English term and flag the Chinese inconsistency in `Risk notes`.
- If two English terms are both needed, define the distinction first. For example, use `element` for the repeat unit and `copy` for an occurrence only if that distinction is explicit and stable.

## Do not upgrade

- 相关性 -> 因果
- 候选机制 -> 已证明机制
- 探索性结果 -> 稳定结论
- 局部数据集结果 -> 普遍规律

## Output variants

- `Faithful version`: close to the Chinese source.
- `Concise version`: shorter, but not stronger.
- `Nature-leaning version`: more polished and selective, but still bounded.

## Risk notes

Check whether terms overstate the supplied evidence, especially:

- demonstrate
- establish
- reveal the mechanism
- drive
- determine
- universal

Do not flag or weaken a word just because it appears in this list. If a strong
source claim conflicts with the supplied design, identify the conflict and
offer a bounded alternative; do not silently upgrade or downgrade the author's
confirmed scientific conclusion. Complete unaffected translation first.

## Handoff from Chinese

The normal route is Chinese revision, optional Hashimoto-style Chinese
polishing, author confirmation, then an explicit English translation request.
These are separable modules, not mandatory repeated steps. A direct “translate
this” request supplies the translation authorization for that input. A statement
that the Chinese is approved does not itself authorize an English output.
