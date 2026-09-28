#!/usr/bin/env python3
"""Close an SDD task: probe + non-empty BASE..HEAD → progress ledger.

Appends a progress line only when:
  1. BASE was recorded by task-start
  2. BASE is an ancestor of HEAD
  3. BASE..HEAD is non-empty
  4. The probe passes (DONE.md-style or --probe/--expect)

Refuses (exit ≠0) on failed probe or empty/invalid range — no ledger write.

Deepens execute/subagent from print-cards into mutating mechanics.
Layout: `.emperor/sdd/<slug>/`. Never vendors whole Superpowers prompts.

Thin twins: scripts/task-done.sh / scripts/task-done.ps1
CLI: task_done.py <plan-file> <N> [--probe CMD] [--expect SUBSTR]
     task_done.py <plan-file> <N> --done-file PATH
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from sdd_workspace import resolve as resolve_workspace


def _run(cmd: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def _git_rev(ref: str, cwd: Path | None = None) -> str | None:
    p = _run(["git", "rev-parse", "--verify", "--quiet", ref], cwd=cwd)
    if p.returncode == 0 and p.stdout.strip():
        return p.stdout.strip()
    return None


def _is_ancestor(base: str, head: str, cwd: Path | None = None) -> bool:
    p = _run(["git", "merge-base", "--is-ancestor", base, head], cwd=cwd)
    return p.returncode == 0


def _range_count(base: str, head: str, cwd: Path | None = None) -> int:
    p = _run(["git", "rev-list", "--count", f"{base}..{head}"], cwd=cwd)
    if p.returncode != 0:
        return 0
    try:
        return int(p.stdout.strip() or "0")
    except ValueError:
        return 0


def _run_probe(cmd: str) -> tuple[bool, str]:
    """Run probe via bash -lc (parity with done.py). Returns (ok, output)."""
    try:
        p = subprocess.run(
            ["bash", "-lc", cmd],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        p = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=False
        )
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode == 0, out


def _eval_done_file(path: Path) -> tuple[bool, str]:
    """DONE.md-style probe:/expect: pairs. Empty expect → pass on any output."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if not any(line.startswith("probe:") for line in text.splitlines()):
        return False, f"no probes in {path}"
    fail = 0
    msgs: list[str] = []
    cmd: str | None = None
    expect = ""

    def flush() -> None:
        nonlocal fail, cmd, expect
        if not cmd:
            return
        ok_rc, out = _run_probe(cmd)
        # Match done.py: empty expect always passes (substring); nonzero rc
        # still OK if expect matches — but for task-done we also require
        # expect match. Empty expect → pass regardless of rc (parity).
        if expect == "" or expect in out:
            msgs.append(f"DONE PASS: {cmd}")
        else:
            msgs.append(f"DONE FAIL: {cmd}")
            fail = 1
        cmd = None
        expect = ""

    for raw in text.splitlines():
        if raw.startswith("probe:"):
            flush()
            cmd = raw[len("probe:") :].lstrip()
            expect = ""
        elif raw.startswith("expect:"):
            expect = raw[len("expect:") :].lstrip()
    flush()
    return fail == 0, "\n".join(msgs)


def finish_task(
    plan: Path,
    n: int,
    *,
    probe: str | None = None,
    expect: str = "",
    done_file: Path | None = None,
) -> str:
    """Validate range + probe; append progress. Returns ledger line.
    Raises RuntimeError on refusal (no ledger write).
    """
    if not plan.is_file():
        raise FileNotFoundError(f"no such plan file: {plan}")
    if n < 1:
        raise ValueError(f"task number must be >= 1, got {n}")

    ws = resolve_workspace(plan)
    base_path = ws / f"task-{n}-base"
    if not base_path.is_file():
        raise RuntimeError(
            f"no BASE for task {n} (run task-start first): missing {base_path}"
        )
    base = base_path.read_text(encoding="utf-8").strip()
    if not base:
        raise RuntimeError(f"empty BASE file: {base_path}")

    plan_repo = plan.resolve().parent
    if _git_rev(base, cwd=plan_repo) is None:
        raise RuntimeError(f"bad BASE: {base}")
    head = _git_rev("HEAD", cwd=plan_repo)
    if head is None:
        raise RuntimeError("not a git repo (cannot resolve HEAD)")

    if not _is_ancestor(base, head, cwd=plan_repo):
        raise RuntimeError(
            f"HEAD is not a descendant of BASE: {base}..{head}"
        )
    count = _range_count(base, head, cwd=plan_repo)
    if count <= 0:
        raise RuntimeError(f"empty commit range: {base}..{head}")

    # Probe
    probe_ok = False
    probe_msg = ""
    if done_file is not None:
        if not done_file.is_file():
            raise RuntimeError(f"missing done file: {done_file}")
        probe_ok, probe_msg = _eval_done_file(done_file)
    elif probe is not None:
        _rc_ok, out = _run_probe(probe)
        if expect == "" or expect in out:
            # Also require command success when --expect is set? Keep parity
            # with done.py: substring wins; if expect empty, require rc==0
            # for an explicit --probe (stricter than empty-expect DONE.md).
            if expect == "":
                probe_ok = _rc_ok
            else:
                probe_ok = True
            probe_msg = f"probe {'PASS' if probe_ok else 'FAIL'}: {probe}"
        else:
            probe_ok = False
            probe_msg = f"probe FAIL: {probe} (expect {expect!r})"
    else:
        # Default: look for task-N-done.md in workspace
        default_done = ws / f"task-{n}-done.md"
        if default_done.is_file():
            probe_ok, probe_msg = _eval_done_file(default_done)
        else:
            raise RuntimeError(
                f"no probe: pass --probe CMD or write {default_done}"
            )

    if not probe_ok:
        raise RuntimeError(f"probe failed — refusing ledger\n{probe_msg}")

    line = (
        f"Task {n}: complete base={base[:12]} head={head[:12]} "
        f"commits={count} probe=PASS\n"
    )
    progress = ws / "progress.md"
    if not progress.is_file():
        plan_id = (ws / "plan-path").read_text(encoding="utf-8").strip()
        progress.write_text(
            f"# SDD progress\n- plan: {plan_id}\n\n",
            encoding="utf-8",
        )
    with progress.open("a", encoding="utf-8") as fh:
        fh.write(line)
    return line.rstrip()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "SDD task-done: probe + non-empty BASE..HEAD → append progress"
        )
    )
    ap.add_argument("plan_file", type=Path, help="path to work-order / plan")
    ap.add_argument("task_number", type=int, help="Task N (1-based)")
    ap.add_argument(
        "--probe",
        default=None,
        help="shell probe command (bash -lc); requires exit 0 if no --expect",
    )
    ap.add_argument(
        "--expect",
        default="",
        help="substring that must appear in probe output",
    )
    ap.add_argument(
        "--done-file",
        type=Path,
        default=None,
        help="DONE.md-style probe:/expect: file",
    )
    args = ap.parse_args(argv)
    try:
        line = finish_task(
            args.plan_file,
            args.task_number,
            probe=args.probe,
            expect=args.expect,
            done_file=args.done_file,
        )
    except (FileNotFoundError, ValueError, RuntimeError, OSError) as exc:
        print(f"task_done FAIL: {exc}", file=sys.stderr)
        return 3 if "empty commit range" in str(exc) or "probe failed" in str(exc) or "not a descendant" in str(exc) else 2
    print(line)
    print(f"progress: {(resolve_workspace(args.plan_file) / 'progress.md').resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
