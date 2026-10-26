# Global Agent and Skill maintenance

Reviewed: 2026-09-30. Maintenance runs weekly on Sunday at 22:00 Asia/Tokyo and returns a concise report. Scheduling is maintained separately; this document does not install a scheduler.

## Scope and source selection

Only global Agent guidance and global Skills are maintenance targets. Project instructions, project Skills, project state, research inputs, native memories, credentials and security settings remain outside this maintenance scope. Preserve project-specific environments and scientific decisions.

Prefer current official documentation and maintained upstream repositories. Popularity is a discovery signal, not a correctness or license guarantee. Forum discussions require confirmation from primary evidence. Extract mechanisms into an existing owner Skill or reference; do not bulk-import a library or execute external scripts.

## Update and validation procedure

1. Establish the canonical source, current branch/commit, installed snapshot and applicable tool versions. Compare hashes and semantic changes; stop if concurrent changes cannot be attributed safely.
2. Keep a private backup and before/after digests before each write. Preserve user rules and file permissions, make minimal changes, and record source date, applicability and license status. Backups and machine-specific inventory are not public repository content.
3. Check direct references, document structure, triggering boundaries and appropriate package checks. Scientific efficacy and behavior validation are separate from static success.
4. Keep installed snapshots immutable. A validated source change is not proof of runtime activation. Do not switch runtime during an active task when that could change its behavior.
5. Publish only the exact approved diff to the authorized repository/branch. Compare the target branch first; do not merge unrelated historical branch work. Use a normal fast-forward push, follow branch protection, and never force-push. Report the remote commit and CI status.

Permission for this maintenance does not authorize software installation, unfamiliar code execution, credential handling or security configuration changes. Remote publication and main updates require corresponding user authorization; when given, it applies to validated global maintenance content only.

## Computational biology review priorities

- Preserve raw inputs, sample identity, reference/database versions, coordinate conventions, parameters, seeds, tool/interpreter versions, logs and evidence limitations.
- Record environment locks with platform/architecture. Use small representative and boundary fixtures before large tasks; process success alone does not validate scientific results.
- For relevant VCF/BAM/FASTA work, retain headers, contig identity, sample and phase-set provenance. Avoid adding assay-specific requirements to unrelated projects.
- Long tasks need resource limits, stop criteria, recovery metadata and cache/output retention. Nextflow resume requires both task cache and task work outputs; do not claim resumability from published outputs alone.

## Selected sources and status

- [Official AGENTS guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md): scope and override behavior; preserve local scope conventions.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): descriptions and selective reference loading.
- [OpenAI Plugins](https://github.com/openai/plugins): current official example discovery; check each item before adoption. [openai/skills](https://github.com/openai/skills) is deprecated; do not retain its old installation guidance as current.
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills): renamed from Claude Scientific Skills. Repository-level MIT does not establish every individual Skill license; inspect item metadata and tool version compatibility before reuse.
- [Snakemake deployment](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html): reproducible environments and configuration; check the installed version before using evolving features.
- [Nextflow cache and resume](https://docs.seqera.io/nextflow/cache-and-resume): task recovery prerequisites.
- [Claude instruction documentation](https://code.claude.com/docs/en/memory): version-specific capabilities; prompt-audit requires 2.1.283 or later according to the reviewed page.

These sources were opened during review on 2026-09-30. This is mechanism-level documentation review, not a security audit of their full repositories, an installation recommendation, or proof of recent commit activity.

## Rollback

Record the parent commit for each published change. Revert the specific maintenance commit on top of the current branch rather than resetting shared history. Restore local guidance from its private backup only if the target digest still matches the maintenance result; otherwise remove the attributable changed sections while preserving concurrent edits. Source rollback and runtime rollback are distinct actions.
