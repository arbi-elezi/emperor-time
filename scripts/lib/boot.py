#!/usr/bin/env python3
"""Silent session boot (Python core).

Writes .emperor/host.env, survey.md, and optionally eval.log. User never
types this. Closes bash↔ps1 twin drift: boot.sh sourced host.sh + identify.sh
+ eval.sh; boot.ps1 sourced host.ps1 + identify.ps1 + eval.ps1 — report
encoding and WSL interop probes already drifted in the host twins.

One core owns the boot sequence via host.py + identify.py + eval.py.

Thin twins: scripts/boot.sh / scripts/boot.ps1
CLI: boot.py [--root DIR] [--skip-identify] [--skip-eval]
Env: EMPEROR_BOOT_VERBOSE=1 prints host.env after write.
     EMPEROR_BOOT_SKIP_EVAL=1 / EMPEROR_BOOT_SKIP_IDENTIFY=1 same as flags.
Exits 0 after host/survey write. When structural eval runs on an Emperor Time tree (SKILL.md present) and the log ends EVALS FAILED, exits 1 (honesty: do not mask red eval).
Explicit emperor boot and emperor host must propagate that EVALS FAILED exit 1 to the caller.
The --skip-eval flag always exits 0.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Allow `python3 scripts/lib/boot.py` without package install.
_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from host import detect  # noqa: E402


def _repo_scripts() -> Path:
    return Path(__file__).resolve().parent.parent


def boot(
    root: Path,
    *,
    skip_identify: bool = False,
    skip_eval: bool = False,
) -> tuple[Path, bool]:
    """Run silent boot under root. Returns (host.env path, eval_failed)."""
    emperor = root / ".emperor"
    emperor.mkdir(parents=True, exist_ok=True)

    info = detect()
    host_env = emperor / "host.env"
    host_env.write_text(info.report_line() + "\n", encoding="utf-8")

    scripts = _repo_scripts()
    identify_py = scripts / "lib" / "identify.py"
    eval_py = scripts / "lib" / "eval.py"

    if not skip_identify and identify_py.is_file():
        survey = emperor / "survey.md"
        try:
            p = subprocess.run(
                ["python3", str(identify_py), str(root)],
                capture_output=True,
                text=True,
                check=False,
                cwd=str(root),
            )
            survey.write_text(p.stdout or "", encoding="utf-8")
        except OSError:
            pass

    if not skip_eval and eval_py.is_file() and (root / "SKILL.md").is_file():
        try:
            p = subprocess.run(
                ["python3", str(eval_py)],
                capture_output=True,
                text=True,
                check=False,
                cwd=str(root),
            )
            (emperor / "eval.log").write_text(
                (p.stdout or "") + (p.stderr or ""),
                encoding="utf-8",
            )
        except OSError:
            pass

    eval_failed = False
    # Honesty only when this boot actually ran structural eval (not --skip-eval).
    # Do not inherit a stale EVALS FAILED from a prior run when skip_eval is set.
    if not skip_eval:
        eval_log = emperor / "eval.log"
        if eval_log.is_file():
            try:
                body = eval_log.read_text(encoding="utf-8", errors="replace")
            except OSError:
                body = ""
            if "EVALS FAILED" in body:
                eval_failed = True
                if os.environ.get("EMPEROR_BOOT_VERBOSE", "") == "1":
                    sys.stderr.write(
                        "[Emperor Time] boot: structural eval FAILED"
                        " - see .emperor/eval.log\n"
                    )

    if os.environ.get("EMPEROR_BOOT_VERBOSE", "") == "1":
        sys.stdout.write(host_env.read_text(encoding="utf-8"))

    return host_env, eval_failed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Silent Emperor Time boot (host.env + survey + optional eval.log)."
    )
    ap.add_argument(
        "--root",
        default=".",
        help="workspace root to write .emperor into (default: .)",
    )
    ap.add_argument(
        "--skip-identify",
        action="store_true",
        help="do not write survey.md",
    )
    ap.add_argument(
        "--skip-eval",
        action="store_true",
        help="do not write eval.log (avoids nested eval during tests)",
    )
    args = ap.parse_args(argv)

    skip_identify = args.skip_identify or os.environ.get(
        "EMPEROR_BOOT_SKIP_IDENTIFY", ""
    ) == "1"
    skip_eval = args.skip_eval or os.environ.get("EMPEROR_BOOT_SKIP_EVAL", "") == "1"

    eval_failed = False
    try:
        _host_env, eval_failed = boot(
            Path(args.root).resolve(),
            skip_identify=skip_identify,
            skip_eval=skip_eval,
        )
    except OSError:
        # Still write what we can; do not crash the session wrapper.
        pass
    # Honesty: red structural eval on an ET tree must not look like a clean boot.
    return 1 if eval_failed else 0


if __name__ == "__main__":
    sys.exit(main())
