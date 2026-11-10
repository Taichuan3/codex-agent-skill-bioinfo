#!/usr/bin/env python3
"""Offline engineering fixtures, NOT image-generation or scientific validation."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from PIL import Image
from pptx import Presentation

SCRIPTS = Path(__file__).resolve().parent


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="codex-ppt-portable-") as temporary:
        root = Path(temporary)
        env = {k: v for k, v in os.environ.items() if k not in {
            "OPENAI_API_KEY", "OPENAI_BASE_URL", "CODEX_PPT_IMAGE_MODEL"
        }}
        env.update(CODEX_PPT_HOME=str(root / "empty-runtime"), PYTHONDONTWRITEBYTECODE="1")

        def run(script: str, *args: str, ok: bool = True) -> str:
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPTS / script), *map(str, args)],
                env=env, text=True, capture_output=True, check=False,
            )
            assert (result.returncode == 0) == ok, result.stdout + result.stderr
            return result.stdout + result.stderr

        for script in SCRIPTS.glob("*.py"):
            if script.name not in {"slide_run_state.py", Path(__file__).name}:
                run(script.name, "--help")
        rejected = run("image_gen.py", "generate", "--prompt", "fixture", "--dry-run", ok=False)
        assert "no default model" in rejected
        run("image_gen.py", "generate", "--model", "gpt-image-1", "--size", "1536x1024",
            "--prompt", "fixture only", "--dry-run")

        deck = root / "fixture-deck"
        deck.mkdir()
        spec = deck / "deck_spec.json"
        spec.write_text(json.dumps({
            "deck_name": "fixture-deck",
            "sample_generation_method": {"backend_used": "built-in image tool", "tool_name": "image_gen"},
            "slides": [{"number": 1, "title": "Engineering fixture only"}],
        }), encoding="utf-8")
        run("prepare_slide_prompts.py", "--spec", spec, "--out-dir", deck,
            "--selected-backend", "built-in image tool")
        before = (deck / "slide_jobs.json").read_bytes()
        status = json.loads(run("slide_job_status.py", deck, "--json"))
        assert status["counts"] == {"pending": 1}
        assert (deck / "slide_jobs.json").read_bytes() == before
        run("record_slide_dispatch.py", deck, "--slide", "1", "--agent-id", "fixture-agent")

        # A synthetic solid-color image exercises file/assembly plumbing only.
        # It is not a real image-backend output or a production slide.
        image = root / "synthetic-test-input.png"
        Image.new("RGB", (160, 90), "white").save(image)
        common = (deck, "--slide", "1", "--agent-id", "fixture-agent",
                  "--selected-source", image, "--qa-note", "synthetic engineering fixture only")
        mismatch = run("record_slide_result.py", *common, "--backend-used", "scripts/image_gen.py", ok=False)
        assert "Backend mismatch" in mismatch
        run("record_slide_result.py", *common, "--backend-used", "built-in image tool")
        status = json.loads(run("slide_job_status.py", deck, "--json"))
        assert status["counts"] == {"recorded": 1}
        (deck / "speech.md").write_text("## Slide 1: Fixture\n\nOffline engineering test.\n", encoding="utf-8")
        run("assemble_ppt.py", root, "fixture-deck.pptx")
        presentation = Presentation(deck / "fixture-deck.pptx")
        assert len(presentation.slides) == 1
        assert "Offline engineering test" in presentation.slides[0].notes_slide.notes_text_frame.text
        assert not (root / "empty-runtime").exists()
    print("PASS: offline CLI, explicit-model stop, job state, backend mismatch and PPTX/notes fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
