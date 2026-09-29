#!/usr/bin/env python3
"""Mechanical gates G0–G5 for Emperor Time (Python core).

Judgment Chain is the law; this module is the lock on the door.
A model writing "G4 PASS" in markdown is not a gate. An exit code is.

Thin twins: scripts/gate.sh / scripts/gate.ps1 — same CLI:
  gate.py g0|g1|g2|g3|g4|g5 <task-dir>

Preserves gate.sh semantics (including G4 CONJECTURE warn) so bash/ps1
cannot drift. G2 delegates plan-header check to work_order.py.
G4 delegates claim-audit sweep to claim_audit.py.
G4 delegates self-critique eight-count to critique.py
(critique file presence ≠ eight-count completeness).
G4 also delegates Steal quarantine admission to quarantine.py
(SKIP (vacuous) when no worker runs / no steal markers).
G4 also delegates Steal consent-protocol to consent.py
(SKIP (vacuous) when no worker runs / no steal markers).
G4 also delegates Steal sign-in / dispatch / swarm to steal_flow.py
(SKIP (vacuous) when no matching steal-flow activity).
G4 also delegates Jail pin-and-consent to pin_consent.py
(SKIP (vacuous) when no captured-skill / pin markers).
G0 also delegates ask→spec to ask_spec.py --require-spec
(always-on: thrash without a written ask→spec FAILS; never vacuous).
G4 also delegates proportionality / anti-loop to proportionality.py
(records a gate cycle, then checks caps; SKIP (vacuous) when no
effort_class / cycle ledger).
G4 also delegates hetero-critique isolation to review_pack.py
(SKIP (vacuous) when no review-pack / no hetero markers).
G0 also delegates thoughttrail + super-context to context.py
(SKIP (vacuous) when no context / thoughttrail markers).
G5 delegates verdict + Breach Register honesty to verdict.py
(PASS substring + header-only theater is not enough).
G5 also delegates forge PR-consent to forge.py
(SKIP (vacuous) when no forge / public-PR markers).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

GATES = ("g0", "g1", "g2", "g3", "g4", "g5")
PRIOR = {
    "g1": "g0",
    "g2": "g1",
    "g3": "g2",
    "g4": "g3",
    "g5": "g4",
}


class GateFail(Exception):
    """Hard gate failure — message already shaped for stderr."""

    def __init__(self, gate: str, msg: str) -> None:
        self.gate = gate
        self.msg = msg
        super().__init__(msg)


def _fail(gate: str, msg: str) -> None:
    raise GateFail(gate, msg)


def _ok(gate: str, msg: str) -> None:
    print(f"GATE {gate} PASS: {msg}")


def _has(pattern: str, path: Path) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def _mark(stamp: Path, gate: str) -> None:
    stamp.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (stamp / gate).write_text(now + "\n", encoding="utf-8")


def _require_prior(stamp: Path, gate: str) -> None:
    prior = PRIOR.get(gate)
    if prior is None:
        return
    if not (stamp / prior).is_file():
        _fail(gate, f"prior gate {prior} never passed mechanically")


def _need_ledger(gate: str, ledger: Path) -> None:
    if not ledger.is_file():
        _fail(gate, f"missing {ledger}")


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run_work_order(gate: str, order: Path) -> None:
    py = _root() / "scripts" / "lib" / "work_order.py"
    proc = subprocess.run(
        [sys.executable, str(py), str(order)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "plan header (work_order.py)")


def _run_claim_audit(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "claim_audit.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-audit", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "claim audit (claim_audit.py)")


def _run_critique(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "critique.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-critique", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "critique eight-count (critique.py)")


def _run_quarantine(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "quarantine.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-quarantine", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "steal quarantine (quarantine.py)")


def _run_consent(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "consent.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-consent", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "steal consent (consent.py)")


def _run_steal_flow(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "steal_flow.py"
    for flag in ("--check-signin", "--check-dispatch", "--check-swarm"):
        proc = subprocess.run(
            [sys.executable, str(py), flag, str(task)],
            check=False,
        )
        if proc.returncode != 0:
            _fail(gate, f"steal flow ({flag})")


def _run_pin_consent(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "pin_consent.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-pin-consent", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "jail pin-and-consent (pin_consent.py)")


def _run_ask_spec(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "ask_spec.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--require-spec", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "ask→spec (ask_spec.py --require-spec)")


def _run_proportionality(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "proportionality.py"
    proc = subprocess.run(
        [
            sys.executable,
            str(py),
            "--bump-gate",
            "--check-proportionality",
            str(task),
        ],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "proportionality / anti-loop (proportionality.py)")


def _run_review_isolation(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "review_pack.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-isolation", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "hetero-critique isolation (review_pack.py)")


def _run_context(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "context.py"
    for flag in ("--check-context", "--check-trail"):
        proc = subprocess.run(
            [sys.executable, str(py), flag, str(task)],
            check=False,
        )
        if proc.returncode != 0:
            _fail(gate, f"thoughttrail/super-context ({flag})")


def _run_forge_consent(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "forge.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-pr-consent", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "forge PR consent (forge.py)")


def _run_verdict(gate: str, task: Path) -> None:
    py = _root() / "scripts" / "lib" / "verdict.py"
    proc = subprocess.run(
        [sys.executable, str(py), "--check-verdict", str(task)],
        check=False,
    )
    if proc.returncode != 0:
        _fail(gate, "verdict + breach register (verdict.py)")


def run_gate(gate: str, task: Path) -> None:
    if not task.is_dir():
        _fail(gate, f"missing task dir {task}")

    ledger = task / "ledger.md"
    order = task / "work-order.md"
    claims = task / "claims.md"
    stamp = task / ".gates"
    stamp.mkdir(parents=True, exist_ok=True)

    if gate == "g0":
        _need_ledger(gate, ledger)
        if not _has(r"G0", ledger):
            _fail(gate, "ledger has no G0 section")
        if not _has(r"quoted|Origin|Task:", ledger):
            _fail(gate, "ledger missing origin/task line")
        # Thoughttrail + super-context: graph/trail when activity claimed.
        # SKIP (vacuous) when no context / thoughttrail markers.
        _run_context(gate, task)
        # Ask→spec: always-on scoped brief before setup thrash.
        # Missing written ask-spec FAILS (never vacuous SKIP).
        _run_ask_spec(gate, task)
        _mark(stamp, gate)
        _ok(gate, str(ledger))
        return

    if gate == "g1":
        _require_prior(stamp, gate)
        _need_ledger(gate, ledger)
        if not _has(r"Acceptance criteria", ledger):
            _fail(gate, "no acceptance criteria")
        if not _has(r"Out of scope", ledger):
            _fail(gate, "no out-of-scope")
        _mark(stamp, gate)
        _ok(gate, "requirements present")
        return

    if gate == "g2":
        _require_prior(stamp, gate)
        _need_ledger(gate, ledger)
        trivial = _has(r"Size:.*trivial", ledger) or (
            order.is_file() and _has(r"Size:.*trivial", order)
        )
        if trivial:
            if not _has(r"G2", ledger):
                _fail(gate, "trivial task still needs a G2 line")
            _mark(stamp, gate)
            _ok(gate, "trivial G2")
            return
        if not order.is_file():
            _fail(gate, "non-trivial task missing work-order.md")
        if not _has(r"Expected:", order):
            _fail(gate, "work-order has no Expected: lines")
        if not _has(r"Acceptance criteria", order):
            _fail(gate, "work-order missing acceptance criteria")
        _run_work_order(gate, order)
        _mark(stamp, gate)
        _ok(gate, str(order))
        return

    if gate == "g3":
        _require_prior(stamp, gate)
        _need_ledger(gate, ledger)
        if not _has(r"G3", ledger):
            _fail(gate, "no G3 section")
        try:
            inside = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                check=False,
                capture_output=True,
                text=True,
            )
            if inside.returncode == 0:
                diff = subprocess.run(
                    ["git", "diff", "--stat"],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                (task / "diffstat.txt").write_text(
                    diff.stdout or "", encoding="utf-8"
                )
        except OSError:
            pass
        _mark(stamp, gate)
        _ok(gate, "build section present")
        return

    if gate == "g4":
        _require_prior(stamp, gate)
        _need_ledger(gate, ledger)
        # Mechanical eight-count: all axes + Checked evidence.
        # Critique file presence ≠ eight-count completeness (critique.py).
        _run_critique(gate, task)
        # Mechanical claim-audit: CLAIM AUDIT line + terminal rows.
        # Not critique-file-present theater — exit code from claim_audit.py.
        _run_claim_audit(gate, task)
        # Steal consent: CONSENT record before enlistment.
        # SKIP (vacuous) when no worker runs / steal markers.
        _run_consent(gate, task)
        # Steal quarantine: runs layout + CONJECTURE start + ADMITTED|REJECTED.
        # SKIP (vacuous) when no worker runs / steal markers.
        _run_quarantine(gate, task)
        # Steal sign-in / dispatch / swarm HARD-GATE (steal_flow.py).
        # SKIP (vacuous) when no matching activity.
        _run_steal_flow(gate, task)
        # Jail pin-and-consent HARD-GATE (pin_consent.py).
        # SKIP (vacuous) when no captured-skill / pin markers.
        _run_pin_consent(gate, task)
        # Proportionality / anti-loop HARD-GATE (proportionality.py).
        # Records a gate cycle then checks effort_class caps.
        # SKIP (vacuous) when no effort_class / cycle ledger.
        _run_proportionality(gate, task)
        # Hetero-critique isolation: review-pack has no author diary / CoT.
        # SKIP (vacuous) when no review-pack / no hetero markers.
        _run_review_isolation(gate, task)
        if claims.is_file():
            text = claims.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                if not re.search(r"\|.*\|\s*CONJECTURE\s*\|", line, re.I):
                    continue
                if re.search(r"UNVERIFIABLE|carried|labeled", line, re.I):
                    continue
                print(
                    f"GATE G4 WARN: unterminated CONJECTURE rows in {claims}",
                    file=sys.stderr,
                )
                break
            for line in text.splitlines():
                if not re.search(r"\|.*\|\s*VERIFIED\s*\|", line, re.I):
                    continue
                if '"' not in line and "`" not in line:
                    _fail(gate, "VERIFIED row without quoted evidence")
        if not _has(r"Verdict", ledger):
            _fail(gate, "ledger missing Verdict line")
        _mark(stamp, gate)
        _ok(gate, "verify artifacts present")
        return

    if gate == "g5":
        _require_prior(stamp, gate)
        _need_ledger(gate, ledger)
        # Mechanical verdict + Breach Register: deliverable ruling + citations;
        # empty/theater Stake rows fail (verdict.py). Header-only PASS theater ≠ G5.
        _run_verdict(gate, task)
        # Forge PR consent: EMPEROR_CONSENT_PR or ledger quote when forge/PR claimed.
        # SKIP (vacuous) when no forge / public-PR markers (merge-locally OK).
        _run_forge_consent(gate, task)
        _mark(stamp, gate)
        _ok(gate, "deliverable artifacts present")
        return

    raise SystemExit(2)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="gate.py",
        description="Emperor Time mechanical gates G0–G5 (Python core)",
    )
    ap.add_argument("gate", choices=GATES, help="gate id")
    ap.add_argument(
        "task_dir",
        type=Path,
        help="task directory with ledger.md / work-order.md / …",
    )
    # Match bash usage exit 2 when args missing — argparse exits 2 by default.
    try:
        args = ap.parse_args(argv)
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 2
        return code if code != 0 else 2

    try:
        run_gate(args.gate, args.task_dir)
    except GateFail as e:
        print(f"GATE {e.gate} FAIL: {e.msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
