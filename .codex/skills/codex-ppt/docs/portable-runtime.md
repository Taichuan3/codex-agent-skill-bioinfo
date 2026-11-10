# Portable runtime overlay

This package preserves the upstream slide workflow but not its automatic setup
assumption. This file takes precedence over OS-specific command examples in
the other docs. Installing the Skill copies instructions and scripts only.
Do not bootstrap dependencies, configure secrets or make API calls during
Skill synchronization. Reuse a working environment first; request missing
installation/configuration authority when needed.

## Python and paths

Use Python 3.11+ for the portable package. `{skill_root}` means the installed
directory containing this Skill's `SKILL.md`, not a fixed source checkout.
The default runtime directory is `.codex-ppt-skill` in the user's home;
`CODEX_PPT_HOME` overrides it. It stores mutable dependencies and personal
styles outside the immutable Skill snapshot.

After installation authority, macOS/Linux:

```bash
python3 "{skill_root}/scripts/codex_ppt_runtime.py" bootstrap
"{runtime_home}/.venv/bin/python" "{skill_root}/scripts/slide_job_status.py" "{deck_dir}"
```

After installation authority, Windows PowerShell:

```powershell
py -3.11 "{skill_root}/scripts/codex_ppt_runtime.py" bootstrap
& "{runtime_home}/.venv/Scripts/python.exe" "{skill_root}/scripts/slide_job_status.py" "{deck_dir}"
```

Replace placeholders with actual paths, quote paths containing spaces, and
use PowerShell's `&` call operator. Do not paste Bash line-continuation `\`
or `${NAME:-default}` syntax into PowerShell. Run one-line commands or use
PowerShell's backtick continuation. `~/.venv/bin/python` examples elsewhere
must be translated to the runtime's `.venv/Scripts/python.exe` on Windows.

Dependencies are listed in `requirements.txt`; it is a compatible-range
manifest, not a lockfile. Record the actual versions for each project. Python
venvs themselves do not sync between OSs. The built-in image tool needs no
local API credential; assembly still requires python-pptx and Pillow.

## Explicit fallback selection

Confirm the provider endpoint, supported model and upload scope before real
CLI use. Model names in inherited examples are historical examples, not a
promise of current availability. The portable CLI has no default model: pass
the confirmed `--model` or configure `CODEX_PPT_IMAGE_MODEL` explicitly. Model
selection does not itself authorize an API request. Preserve known working
local configuration rather than overwriting it during sync.

Credential setup is a separate user-authorized action through the available
secure provider flow. Never copy keys into Git, chat, logs or command-line
history; do not run the inherited `--api-key` examples with a literal secret.
For ordinary tasks let the selected CLI read its configuration; do not print
or inspect credential files manually. A POSIX 0600 chmod is not a guarantee
of Windows ACL isolation. User-custom style files also remain local unless
explicitly reviewed and approved for publication.

## Scientific assets

Reference-image generation can alter source figures despite a preservation
prompt. Verify scientific labels, axes, numerical values and visual traces
against the original. If exact fidelity is required or cannot be verified,
stop that slide and offer `pptx-generator` for lossless original-image
embedding. Do not present a generated chart as unchanged experimental data.

## Return to a project

Keep final artifacts in the project's stable presentation module and link
them from its existing navigation. Date/run identifiers label intermediate
history, not the only entry point. The parent agent owns shared index updates;
workers return deltas. A read-only status request does not write project state.
