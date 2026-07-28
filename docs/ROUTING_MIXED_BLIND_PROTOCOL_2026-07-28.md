# Mixed blind routing protocol — 2026-07-28

## Records and order

1. `ROUTING_MIXED_BLIND_BASELINE_2026-07-28.tsv` preserves the two raw
   pre-fix rounds against owner-canonical `main`
   (`32b5e2e41a48964d8cdad08b1293d6a54f644606`). The evaluators received the
   38 queries, current Skill descriptions and visible plugin/system Skills, but
   not the expected labels or the other run. The Codex Desktop model build was
   not exposed. Run A scored 21/38, run B 20/38, agreement was 34/38, and 14
   same-answer mismatches were present.
2. Case adjudication happened before post-fix scoring. B06 was changed from
   `bioinfo-analysis-code` to `none` because it is explicitly a non-bioinfo
   generic script. B20 was changed from `claim-evidence-audit` to
   `protein-structure-docking` because interpreting the meaning and limits of a
   docking score belongs first to the domain owner. B35 was rewritten to state
   manuscript submission scope; the original wording was ambiguous with
   `task-self-check`.
3. `ROUTING_MIXED_BLIND_TEST_2026-07-28.tsv` preserves two new independent
   full reruns in fresh no-history subagent contexts against the isolated
   candidate worktree. Run A scored 36/38, run B 38/38, and agreement was
   36/38. A separate fresh targeted rerun after the last claim/docking
   description adjustment selected `protein-structure-docking` for B20 and
   `claim-evidence-audit` for B30.

## Remaining boundary

B28 remains a model-level routing ambiguity: one evaluator returned `none`,
while another selected `reviewer-simulation` to apply that Skill's explicit
no-impersonation/no-editorial-decision refusal. Both preserve the safety
boundary, but only `none` matches the current primary-route label. Keep this as
an observed variance rather than rewriting it as a full pass.

These routing records test owner selection, not scientific correctness,
runtime tool integration, or outcome quality.
