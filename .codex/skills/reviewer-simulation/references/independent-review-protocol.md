# Independent review protocol

## Trigger and ownership

When the user's requested deliverable is an assessment, audit or review, use
three independent read-only reviewers by default. This includes manuscript,
research-plan, code/Skill and artifact reviews. Do not trigger merely because
source text contains “review”, or for routine questions, grammar edits,
formatting checks or the author's ordinary final self-check. An explicit
quick/single-review request or reviewer count overrides the default.

The domain Skill still owns the question and standards. Manuscript simulation
uses reviewer-simulation; an existing decision uses research-decision-review;
Skill quality uses skill-quality-audit. This protocol grants no permission to
repair, run analyses, install, publish or contact anyone.

## Setup

1. Freeze one input packet: exact artifact version/hash where available, source
   locations, user question, scope, criteria and missing inputs. Do not include
   the author's proposed verdict, suspected defects or other reviewer output.
2. Preassign complementary lenses for the selected count (default three): evidence and
   validity; methods and reproducibility; utility, clarity and alternatives.
   Lenses are not fabricated expert identities. Each may flag any grounded issue.
3. Launch fresh isolated subagents/contexts with only that packet, the protocol,
   and their lens; do not fork the author's discussion history. Reviewers are
   read-only, do not delegate or contact each other, and must not read existing
   review logs. Default to three reviewer workstreams; the author only coordinates.
4. If fresh isolation or slots are unavailable, use separate isolated invocations
   sequentially or report the limitation and offer a single bounded review.
   Never describe three voices in one context as three independent reviewers.

## Individual reports and freeze

Each report states coverage and inaccessible material. Every finding has an ID,
artifact pointer, evidence, impact/severity, uncertainty and a minimal resolution
test. Missing evidence is not proof of a defect. A reviewer may find no problems;
there is no concern quota. Do not invent scientific outcomes or editorial decisions.

Freeze reports before comparison (separate immutable outputs or hashed report
files). Preserve legitimate duplicate findings, disagreements and minority
warnings. Do not send intermediate findings or synthesized concerns to reviewers.

## Synthesis and later changes

The lead groups findings only after all reports are frozen. Count consensus only
where at least two independently identify the same underlying issue; majority
agreement is not evidence of correctness. Resolve by sources and methods, not
vote alone, and leave unresolvable scientific choices to the user.

Run arithmetic, denominator, table/prose and provenance consistency checks as a
separate post-review pass when relevant. Label these as lead/audit findings,
never retroactively as reviewer consensus. Corrections create a new artifact
version and an explicitly labelled re-review; do not silently alter frozen reports.

Deliver scope, the selected reviewers' report pointers or bounded summaries, merged findings with
support counts, dissent, post-review findings, unassessed areas and next decision.
Use existing project output/index conventions; do not replace GUIDE, manifest
or source-data ownership. Reviewing does not itself authorize project edits.

## Provenance

Mechanism-level adaptation, independently written, from nature-reviewer at
Yuan1z0825/nature-skills commit 233ed09957d32d8cf45dd96c495663c5c5d8e447
(Apache-2.0). Local changes broaden domain routing, make user overrides explicit,
and retain local authority and artifact-management rules. No upstream code,
full prompt, auto-update hook or mandatory punctuation style is copied.
