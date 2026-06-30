#!/usr/bin/env bash
# Draft-only sync helper for multi-terminal agent/skill collaboration.
# Default behavior is safe: generate a report and DO NOT push/merge.

set -euo pipefail

MODE="report"  # report | branch
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_SKILLS_DIR="${HERMES_RUNTIME_SKILLS_DIR:-$HOME/.hermes/skills/bioinfo}"
DATE="$(date +%F)"
REPORT_DIR="$REPO_DIR/docs/sync-reports"
REPORT="$REPORT_DIR/$DATE-agent-skill-sync.md"

usage() {
  cat <<'USAGE'
Usage: scripts/agent_skill_sync_draft.sh [--report|--branch]

--report  Generate a sync report only. No git branch, no commit, no push. Default.
--branch  Generate report and create a local sync branch, but still do not commit/push.

Environment:
  HERMES_RUNTIME_SKILLS_DIR  Defaults to ~/.hermes/skills/bioinfo
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --report) MODE="report" ;;
    --branch) MODE="branch" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
  shift
done

cd "$REPO_DIR"
mkdir -p "$REPORT_DIR"

current_branch="$(git branch --show-current 2>/dev/null || true)"
remote_url="$(git remote get-url origin 2>/dev/null || echo 'NO_ORIGIN')"
head_sha="$(git rev-parse --short HEAD 2>/dev/null || echo 'NO_GIT')"

{
  echo "# Agent / Skill Sync Report — $DATE"
  echo
  echo "## Repository"
  echo
  echo "- Repo dir: \`$REPO_DIR\`"
  echo "- Origin: \`$remote_url\`"
  echo "- Branch: \`$current_branch\`"
  echo "- HEAD: \`$head_sha\`"
  echo "- Runtime skills: \`$RUNTIME_SKILLS_DIR\`"
  echo
  echo "## Git status"
  echo
  echo '```text'
  git status --short || true
  echo '```'
  echo
  echo "## Branches"
  echo
  echo '```text'
  git branch --all --sort=-committerdate | sed -n '1,40p' || true
  echo '```'
  echo
  echo "## Skill inventory"
  echo
  repo_count="$(find .codex/skills -name SKILL.md 2>/dev/null | wc -l | tr -d ' ')"
  runtime_count="$(find "$RUNTIME_SKILLS_DIR" -name SKILL.md 2>/dev/null | wc -l | tr -d ' ')"
  echo "- Repo .codex skills: $repo_count"
  echo "- Runtime Hermes bioinfo skills: $runtime_count"
  echo
  echo "### Repo skills"
  echo
  echo '```text'
  find .codex/skills -mindepth 2 -maxdepth 2 -name SKILL.md 2>/dev/null | sed 's#^\.codex/skills/##; s#/SKILL.md$##' | sort || true
  echo '```'
  echo
  echo "### Runtime skills"
  echo
  echo '```text'
  if [[ -d "$RUNTIME_SKILLS_DIR" ]]; then
    find "$RUNTIME_SKILLS_DIR" -mindepth 2 -maxdepth 2 -name SKILL.md 2>/dev/null | sed "s#^$RUNTIME_SKILLS_DIR/##; s#/SKILL.md##" | sort || true
  else
    echo "Runtime dir not found"
  fi
  echo '```'
  echo
  echo "## Runtime vs repo rough diff"
  echo
  echo "> This is a name-level diff only. It does not imply files should be copied automatically."
  echo
  tmp_repo="$(mktemp)"; tmp_runtime="$(mktemp)"
  find .codex/skills -mindepth 2 -maxdepth 2 -name SKILL.md 2>/dev/null | sed 's#^\.codex/skills/##; s#/SKILL.md$##' | sort > "$tmp_repo" || true
  if [[ -d "$RUNTIME_SKILLS_DIR" ]]; then
    find "$RUNTIME_SKILLS_DIR" -mindepth 2 -maxdepth 2 -name SKILL.md 2>/dev/null | sed "s#^$RUNTIME_SKILLS_DIR/##; s#/SKILL.md##" | sort > "$tmp_runtime" || true
  else
    : > "$tmp_runtime"
  fi
  echo "### In runtime but not repo"
  echo
  echo '```text'
  comm -13 "$tmp_repo" "$tmp_runtime" || true
  echo '```'
  echo
  echo "### In repo but not runtime"
  echo
  echo '```text'
  comm -23 "$tmp_repo" "$tmp_runtime" || true
  echo '```'
  rm -f "$tmp_repo" "$tmp_runtime"
  echo
  echo "## Safety checks"
  echo
  echo '```text'
  git diff --check 2>&1 || true
  echo '```'
  echo
  echo "## Next action recommendation"
  echo
  echo "- Review this report manually."
  echo "- If changes are valid, create a focused branch and PR."
  echo "- Do not auto-merge until trigger overlap, source metadata, and file scope are reviewed."
} > "$REPORT"

if [[ "$MODE" == "branch" ]]; then
  branch="hermes/sync/local-runtime-skills-$DATE"
  if git show-ref --verify --quiet "refs/heads/$branch"; then
    git checkout "$branch"
  else
    git checkout -b "$branch"
  fi
  echo "Created/switched to branch: $branch"
fi

echo "Wrote report: $REPORT"
echo "Mode: $MODE"
echo "No commit, push, merge, or runtime overwrite was performed."
