#!/usr/bin/env python3
"""Structural evals for Emperor Time (Python core). Does not spawn a model.

Thin twins: scripts/eval.sh / scripts/eval.ps1 — same exit 0/1 and
EVAL PASS / EVAL FAIL / EVALS PASSED / EVALS FAILED messaging.

Closes bash↔ps1 twin drift: eval.ps1 was a presence stub (~35 lines) while
eval.sh held the full lock suite. One core owns every assertion.
"""
from __future__ import annotations

import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


class Harness:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.fail = 0

    def section(self, title: str) -> None:
        print(f"== {title} ==")

    def fail_msg(self, msg: str) -> None:
        print(f"EVAL FAIL: {msg}")
        self.fail = 1

    def pass_msg(self, msg: str) -> None:
        print(f"EVAL PASS: {msg}")

    def need(self, rel: str) -> bool:
        if not (self.root / rel).exists():
            self.fail_msg(f"missing {rel}")
            return False
        return True

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def contains(self, needle: str, rel: str) -> bool:
        try:
            return needle in self.read(rel)
        except OSError:
            return False

    def require_contains(self, needle: str, rel: str, fail: str) -> None:
        if not self.contains(needle, rel):
            self.fail_msg(fail)

    def bash_n(self, rel: str, fail: str) -> None:
        p = self.root / rel
        r = subprocess.run(
            ["bash", "-n", str(p)],
            capture_output=True,
            text=True,
            check=False,
        )
        if r.returncode != 0:
            self.fail_msg(fail)

    def py_compile(self, rel: str, fail: str) -> None:
        try:
            py_compile.compile(str(self.root / rel), doraise=True)
        except py_compile.PyCompileError:
            self.fail_msg(fail)

    def run(
        self,
        args: list[str],
        *,
        env: dict[str, str] | None = None,
        cwd: str | Path | None = None,
    ) -> tuple[int, str]:
        full_env = os.environ.copy()
        if env:
            full_env.update(env)
        try:
            p = subprocess.run(
                args,
                capture_output=True,
                text=True,
                check=False,
                env=full_env,
                cwd=str(cwd) if cwd else None,
            )
        except FileNotFoundError:
            return 127, ""
        out = (p.stdout or "") + (p.stderr or "")
        return p.returncode, out

    def run_py(self, rel: str, *args: str) -> tuple[int, str]:
        return self.run(["python3", str(self.root / rel), *args])

    def run_sh(self, rel: str, *args: str, env: dict[str, str] | None = None) -> tuple[int, str]:
        return self.run(["bash", str(self.root / rel), *args], env=env)

    def grep_out(self, text: str, pattern: str, *, flags: int = 0) -> bool:
        return re.search(pattern, text, flags) is not None


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_evals(root: Path) -> int:
    h = Harness(root)

    # ---- presence ----
    h.section("presence")
    for f in [
        "SKILL.md",
        "chains/dowsing-chain/SKILL.md",
        "chains/chain-jail/SKILL.md",
        "chains/judgment-chain/SKILL.md",
        "chains/steal-chain/SKILL.md",
        "chains/steal-chain/ci-mode.md",
        "chains/steal-chain/swarm-emulate.md",
        "chains/holy-chain/SKILL.md",
        "templates/work-order.md",
        "scripts/gate.sh",
        "scripts/gate.ps1",
        "scripts/lib/gate.py",
        "scripts/lib/identify.py",
        "scripts/lib/finish.py",
        "scripts/lib/eval.py",
        "scripts/lib/done.py",
        "scripts/lib/queue.py",
        "scripts/lib/forge.py",
        "scripts/done.sh",
        "scripts/done.ps1",
        "scripts/queue.sh",
        "scripts/queue.ps1",
        "scripts/eval.sh",
        "scripts/eval.ps1",
        "scripts/emperor",
        "scripts/emperor.ps1",
        "scripts/emperor.cmd",
        "scripts/emperor.zsh",
        "skills/emperor-scope/SKILL.md",
        "evals/evals.json",
        "evals/triggers.json",
    ]:
        h.need(f)

    # ---- vows + five chains ----
    h.section("vows + five chains still named in master skill")
    if not h.contains("Vow of Evidence", "SKILL.md"):
        h.fail_msg("vows missing")
    for c in (
        "Dowsing Chain",
        "Chain Jail",
        "Judgment Chain",
        "Steal Chain",
        "Holy Chain",
    ):
        if not h.contains(c, "SKILL.md"):
            h.fail_msg(f"{c} unnamed in SKILL.md")

    # ---- twins ----
    h.section("twins")
    for pair in (
        "done",
        "gate",
        "eval",
        "review-pack",
        "dowse",
        "install",
        "worktree",
        "queue",
        "forge",
        "finish",
        "activate",
        "identify",
        "boot",
        "route",
        "excavate",
        "heal",
        "grill",
        "tdd",
        "iso",
        "review",
        "author",
        "evidence",
        "receive",
        "execute",
    ):
        h.need(f"scripts/{pair}.sh")
        h.need(f"scripts/{pair}.ps1")

    # ---- silent-boot PS ----
    h.section("silent-boot PS twin uses host.ps1")
    h.require_contains("lib/host.ps1", "scripts/boot.ps1", "boot.ps1 does not source lib/host.ps1")
    h.require_contains(
        "Write-EmperorHostReport",
        "scripts/lib/host.ps1",
        "host.ps1 missing Write-EmperorHostReport",
    )
    h.require_contains("host.env", "scripts/emperor.ps1", "emperor.ps1 missing silent-boot host.env check")
    h.require_contains(
        "scripts/emperor boot",
        "adapters/cursor/README.md",
        "cursor adapter missing emperor boot path",
    )

    # ---- silent-boot zsh ----
    h.section("silent-boot zsh twin matches bash")
    h.require_contains("host.env", "scripts/emperor.zsh", "emperor.zsh missing silent-boot host.env check")
    h.require_contains("boot.sh", "scripts/emperor.zsh", "emperor.zsh missing boot.sh silent-boot path")
    h.require_contains(
        'TOOL" == host || "$TOOL" == boot',
        "scripts/emperor.zsh",
        "emperor.zsh missing host|boot special-case (bash parity)",
    )
    h.require_contains(
        'TOOL" == identify',
        "scripts/emperor.zsh",
        "emperor.zsh missing identify silent/path special-case",
    )
    h.require_contains(
        'TOOL" == excavate',
        "scripts/emperor.zsh",
        "emperor.zsh missing excavate first-class alias",
    )
    h.require_contains(
        "emperor.zsh",
        "adapters/cursor/README.md",
        "cursor adapter missing emperor.zsh silent-boot mention",
    )

    # ---- steal ----
    h.section("steal router lists ci + swarm")
    h.require_contains("ci-mode.md", "chains/steal-chain/SKILL.md", "steal router missing ci-mode.md")
    h.require_contains(
        "swarm-emulate.md",
        "chains/steal-chain/SKILL.md",
        "steal router missing swarm-emulate.md",
    )

    # ---- hooks ----
    h.section("hooks treat cmd as a peer")
    h.require_contains("emperor.cmd", "hooks/hooks.json", "hooks do not mention emperor.cmd")
    if h.contains("No cmd.exe shim", "hooks/hooks.json"):
        h.fail_msg("hooks still say No cmd.exe shim")

    # ---- gate syntax ----
    h.section("gate script syntax")
    h.bash_n("scripts/gate.sh", "gate.sh syntax")
    h.bash_n("scripts/emperor", "emperor syntax")

    # ---- eval.py self-lock ----
    h.section("eval.py Python core")
    h.need("scripts/lib/eval.py")
    h.py_compile("scripts/lib/eval.py", "eval.py compile")
    h.require_contains("lib/eval.py", "scripts/eval.sh", "eval.sh thin twin missing eval.py")
    h.require_contains("lib/eval.py", "scripts/eval.ps1", "eval.ps1 thin twin missing eval.py")
    # thin twins must stay thin (no full reimplementation)
    eval_sh = h.read("scripts/eval.sh")
    if len(eval_sh.splitlines()) > 20:
        h.fail_msg("eval.sh should be thin twin (<=20 lines)")
    eval_ps1 = h.read("scripts/eval.ps1")
    if len(eval_ps1.splitlines()) > 30:
        h.fail_msg("eval.ps1 should be thin twin (<=30 lines)")
    h.pass_msg("eval.py thin twins")

    # ---- gate.py ----
    h.section("gate.py Python core")
    h.need("scripts/lib/gate.py")
    h.py_compile("scripts/lib/gate.py", "gate.py compile")
    h.require_contains("lib/gate.py", "scripts/gate.sh", "gate.sh thin twin missing gate.py")
    h.require_contains("lib/gate.py", "scripts/gate.ps1", "gate.ps1 thin twin missing gate.py")
    h.require_contains("CONJECTURE", "scripts/lib/gate.py", "gate.py missing CONJECTURE warn")
    h.require_contains("work_order.py", "scripts/lib/gate.py", "gate.py missing work_order.py")
    h.require_contains(
        "scripts/lib/gate.py",
        "references/mechanical-gates.md",
        "mechanical-gates.md missing gate.py",
    )
    tmpg = Path(tempfile.mkdtemp())
    try:
        (tmpg / ".gates").mkdir()
        (tmpg / "ledger.md").write_text("## G0\nOrigin: test\nTask: prior\n", encoding="utf-8")
        rc, _ = h.run_sh("scripts/gate.sh", "g1", str(tmpg))
        if rc == 0:
            h.fail_msg("gate g1 should refuse without prior g0 stamp")
        else:
            h.pass_msg("gate.py refuses unordered g1")
    finally:
        shutil.rmtree(tmpg, ignore_errors=True)

    # ---- identify.py ----
    h.section("identify.py Python core")
    h.need("scripts/lib/identify.py")
    h.py_compile("scripts/lib/identify.py", "identify.py compile")
    h.require_contains("lib/identify.py", "scripts/identify.sh", "identify.sh thin twin missing identify.py")
    h.require_contains("lib/identify.py", "scripts/identify.ps1", "identify.ps1 thin twin missing identify.py")
    h.require_contains("shebang", "scripts/lib/identify.py", "identify.py missing shebang survey")
    h.require_contains("*.f90", "scripts/lib/identify.py", "identify.py missing *.f90 fossil")
    h.require_contains(
        "scripts/lib/identify.py",
        "references/archaeology.md",
        "archaeology.md missing identify.py",
    )
    _, id_out = h.run_sh("scripts/identify.sh", str(root / "evals/fixtures/lost-pas"))
    if not h.grep_out(id_out, r"[0-9]+ \*\.pas"):
        h.fail_msg("identify.py twin missed *.pas")
    if "-- shebangs --" not in id_out:
        h.fail_msg("identify.py twin missing shebangs section")
    else:
        h.pass_msg("identify.py thin twins + shebangs")

    # ---- unquoted VERIFIED g4 ----
    h.section("fixture: unquoted VERIFIED must fail g4")
    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / ".gates").mkdir()
        stamp = _utc_stamp()
        for g in ("g0", "g1", "g2", "g3"):
            (tmp / ".gates" / g).write_text(stamp + "\n", encoding="utf-8")
        (tmp / "ledger.md").write_text(
            "# Task Ledger\n## G0\n## G1 Acceptance criteria\n## G2\n## G3\n## G4\n- Verdict:\n",
            encoding="utf-8",
        )
        (tmp / "claims.md").write_text(
            "| # | Claim | Status | Prediction | Experiment | Evidence | Date |\n"
            "| 1 | tests pass | VERIFIED | pass | pytest | tests pass | 2026-01-01 |\n",
            encoding="utf-8",
        )
        (tmp / "critique.md").write_text("self-critique filed\n", encoding="utf-8")
        rc, _ = h.run_sh("scripts/gate.sh", "g4", str(tmp))
        if rc == 0:
            h.fail_msg("unquoted VERIFIED was allowed")
        else:
            h.pass_msg("unquoted VERIFIED rejected")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ---- triggers ----
    h.section("trigger file present")
    h.require_contains("emperor time", "evals/triggers.json", "triggers")

    # ---- route mvp ----
    h.section("route mvp")
    if (root / "scripts/route.sh").is_file():
        h.bash_n("scripts/route.sh", "route.sh syntax")
        for utter, needle, fail in (
            ("lost pascal tree", "emperor-excavate", "route lost pascal → excavate"),
            ("hello.f90", "emperor-excavate", "route hello.f90 → excavate"),
            ("gfortran build", "emperor-excavate", "route gfortran → excavate (not build)"),
            ("queue next", "emperor-queue", "route queue next → queue"),
            ("blocked task", "emperor-queue", "route blocked task → queue"),
            ("red build", "emperor-heal", "route red build → heal"),
        ):
            _, out = h.run_sh("scripts/route.sh", utter)
            if needle not in out:
                h.fail_msg(fail)
        rc, _ = h.run_sh("scripts/route.sh", "what is 2+2")
        if rc == 0:
            h.fail_msg("route should miss trivia")
        else:
            h.pass_msg("route misses trivia")

    # ---- queue (Python core) + empty UX ----
    h.section("queue (Python core) + empty UX")
    h.need("scripts/lib/queue.py")
    h.need("scripts/queue.sh")
    h.need("scripts/queue.ps1")
    h.bash_n("scripts/queue.sh", "queue.sh syntax")
    h.py_compile("scripts/lib/queue.py", "queue.py compile")
    h.require_contains("lib/queue.py", "scripts/queue.sh", "queue.sh thin twin missing queue.py")
    h.require_contains("lib/queue.py", "scripts/queue.ps1", "queue.ps1 thin twin missing queue.py")
    queue_sh_lines = len((root / "scripts/queue.sh").read_text(encoding="utf-8").splitlines())
    queue_ps_lines = len((root / "scripts/queue.ps1").read_text(encoding="utf-8").splitlines())
    if queue_sh_lines > 20:
        h.fail_msg("queue.sh should be thin twin (<=20 lines)")
    if queue_ps_lines > 30:
        h.fail_msg("queue.ps1 should be thin twin (<=30 lines)")
    h.require_contains(
        "scripts/lib/queue.py",
        "references/software-factory.md",
        "software-factory.md missing queue.py",
    )
    h.require_contains(
        "queue.py",
        "skills/emperor-queue/SKILL.md",
        "emperor-queue skill missing queue.py",
    )
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as qf:
        qpath = qf.name
        qf.write(
            "# Emperor queue (eval fixture)\n"
            "# WIP=1 kept in comments only — no checkbox placeholder.\n"
        )
    try:
        rc, out = h.run_sh(
            "scripts/queue.sh",
            "next",
            env={
                "EMPEROR_QUEUE_SOURCE": "local",
                "EMPEROR_QUEUE_FILE": qpath,
            },
        )
        if rc == 0:
            h.fail_msg("empty comment-only queue should exit non-zero")
        elif "NEXT none" not in out:
            h.fail_msg("empty queue missing NEXT none")

        Path(qpath).write_text(
            "# Emperor queue\n"
            "- [ ] (empty — replace this line with real work or connect gh)\n"
            "- [ ] ship the widget\n",
            encoding="utf-8",
        )
        _, out = h.run_sh(
            "scripts/queue.sh",
            "next",
            env={
                "EMPEROR_QUEUE_SOURCE": "local",
                "EMPEROR_QUEUE_FILE": qpath,
            },
        )
        if "ship the widget" not in out:
            h.fail_msg("queue next should promote real task past placeholder")
        if "(empty" in out:
            h.fail_msg("queue next promoted placeholder")
        qbody = Path(qpath).read_text(encoding="utf-8")
        if not re.search(r"^- \[~\] ship the widget", qbody, re.M):
            h.fail_msg("placeholder queue file not promoted correctly")
        if not re.search(r"^- \[ \] \(empty", qbody, re.M):
            h.fail_msg("placeholder line should remain untouched")
        # WIP=1 refuse second active
        rc2, out2 = h.run_sh(
            "scripts/queue.sh",
            "next",
            env={
                "EMPEROR_QUEUE_SOURCE": "local",
                "EMPEROR_QUEUE_FILE": qpath,
            },
        )
        if rc2 != 0 or "WIP=1" not in out2 or "active" not in out2:
            h.fail_msg("queue next should WIP-refuse while active exists")
        else:
            h.pass_msg("queue WIP=1 refuse")
        # done substring
        rc3, out3 = h.run_sh(
            "scripts/queue.sh",
            "done",
            "widget",
            env={
                "EMPEROR_QUEUE_SOURCE": "local",
                "EMPEROR_QUEUE_FILE": qpath,
            },
        )
        if rc3 != 0 or "CHECKED:" not in out3:
            h.fail_msg("queue done should CHECKED")
        qbody2 = Path(qpath).read_text(encoding="utf-8")
        if not re.search(r"^- \[x\] ship the widget", qbody2, re.M):
            h.fail_msg("queue done should mark [x]")
        else:
            h.pass_msg("queue done marks [x]")
    finally:
        Path(qpath).unlink(missing_ok=True)
    h.pass_msg("queue.py thin twins + empty UX + WIP + done")

    # ---- archaeology fixtures ----
    fixtures = [
        ("lost-pas identify finds *.pas", "lost-pas", "HELLO.PAS", r"[0-9]+ \*\.pas", []),
        ("lost-asm identify finds *.asm", "lost-asm", "FOO.ASM", r"[0-9]+ \*\.asm", []),
        (
            "lost-cbl identify finds *.cbl",
            "lost-cbl",
            "HELLO.CBL",
            r"[0-9]+ \*\.cbl",
            ["references/archaeology-cobol-manual.md"],
        ),
        (
            "lost-f90 identify finds *.f90",
            "lost-f90",
            "HELLO.F90",
            r"[0-9]+ \*\.f90",
            ["references/archaeology-fortran-manual.md"],
        ),
    ]
    # The loop above was messy — clear fail state not affected; rewrite cleanly below by
    # only running the clean fixtures list (sections already printed wrongly once).
    # Actually we printed wrong section headers. Fix: only use the clean list.
    # Reset approach: the incomplete loop above already ran section() with bad titles.
    # For correctness of checks, run the real fixtures now with proper titles.

    for title, folder, main_file, pat, extra_needs in fixtures:
        h.section(f"fixture: {title}")
        h.need(f"evals/fixtures/{folder}/{main_file}")
        h.need(f"evals/fixtures/{folder}/README.md")
        h.need(f"evals/fixtures/{folder}/PROBE.md")
        for e in extra_needs:
            h.need(e)
        _, id_out = h.run_sh("scripts/identify.sh", str(root / f"evals/fixtures/{folder}"))
        if not h.grep_out(id_out, pat):
            ext = pat.split(r"\*")[-1].replace("\\", "")
            h.fail_msg(f"identify missed *{ext} on {folder}")

    # ---- plan header ----
    h.section("plan header (Superpowers leaf)")
    h.need("scripts/lib/work_order.py")
    h.need("templates/work-order.md")
    h.need("evals/fixtures/plans-header/work-order-missing-header.md")
    h.need("evals/fixtures/plans-header/work-order-complete.md")
    h.require_contains("Review Focus", "templates/work-order.md", "template missing Review Focus")
    h.require_contains(
        "Global Constraints",
        "templates/work-order.md",
        "template missing Global Constraints",
    )
    h.need("scripts/lib/gate.py")
    h.py_compile("scripts/lib/gate.py", "gate.py compile")
    h.require_contains("lib/gate.py", "scripts/gate.sh", "gate.sh does not call gate.py")
    h.require_contains("lib/gate.py", "scripts/gate.ps1", "gate.ps1 does not call gate.py")
    h.require_contains("work_order.py", "scripts/lib/gate.py", "gate.py does not call work_order.py")
    rc, miss_out = h.run_py(
        "scripts/lib/work_order.py",
        str(root / "evals/fixtures/plans-header/work-order-missing-header.md"),
    )
    if rc == 0:
        h.fail_msg("incomplete work-order should fail plan-header check")
    elif not re.search(
        r"Review Focus|Goal|Architecture|plan header|work_order FAIL",
        miss_out,
        re.I,
    ):
        h.fail_msg("missing-header failure message unclear")
    else:
        h.pass_msg("incomplete plan header rejected")
    rc, ok_out = h.run_py(
        "scripts/lib/work_order.py",
        str(root / "evals/fixtures/plans-header/work-order-complete.md"),
    )
    if rc != 0:
        print(ok_out)
        h.fail_msg("complete work-order should pass plan-header check")
    else:
        h.pass_msg("complete plan header accepted")

    # ---- finish menu ----
    h.section("finish menu (forge aspect)")
    h.need("skills/emperor-forge/finish-menu.md")
    h.need("scripts/finish.sh")
    h.need("scripts/finish.ps1")
    h.need("scripts/lib/finish.py")
    h.bash_n("scripts/finish.sh", "finish.sh syntax")
    h.py_compile("scripts/lib/finish.py", "finish.py compile")
    h.require_contains("lib/finish.py", "scripts/finish.sh", "finish.sh thin twin missing finish.py")
    h.require_contains("lib/finish.py", "scripts/finish.ps1", "finish.ps1 thin twin missing finish.py")
    h.require_contains("origin/HEAD", "scripts/lib/finish.py", "finish.py missing origin/HEAD base_guess")
    h.require_contains(
        "scripts/lib/finish.py",
        "skills/emperor-forge/finish-menu.md",
        "finish-menu.md missing finish.py",
    )
    h.require_contains(
        "Merge back to",
        "skills/emperor-forge/finish-menu.md",
        "finish-menu missing merge option",
    )
    h.require_contains(
        "typed word",
        "skills/emperor-forge/finish-menu.md",
        "finish-menu missing discard confirm",
    )
    h.require_contains(
        "finish-menu.md",
        "skills/emperor-forge/SKILL.md",
        "forge skill missing finish-menu",
    )
    h.require_contains("finish|", "scripts/emperor", "emperor bash missing finish")
    _, fin_out = h.run_sh("scripts/finish.sh")
    if not re.search(r"^ENV kind=", fin_out, re.M):
        h.fail_msg("finish.sh missing ENV kind")
    if not re.search(r"^MENU ", fin_out, re.M):
        h.fail_msg("finish.sh missing MENU")
    if "base_guess=" not in fin_out:
        h.fail_msg("finish missing base_guess")
    h.pass_msg("finish.py thin twins + ENV/MENU")
    _, out = h.run_sh("scripts/route.sh", "finish the branch")
    if "emperor-forge" not in out:
        h.fail_msg("route finish the branch → forge")

    # ---- activate ----
    h.section("activate MUST-route (SessionStart leaf)")
    h.need("skills/emperor-resume/must-route.md")
    h.need("scripts/lib/activate.py")
    h.need("scripts/activate.sh")
    h.need("scripts/activate.ps1")
    h.bash_n("scripts/activate.sh", "activate.sh syntax")
    h.py_compile("scripts/lib/activate.py", "activate.py compile")
    h.require_contains("activate.py", "scripts/activate.sh", "activate.sh does not call activate.py")
    h.require_contains("activate.py", "scripts/activate.ps1", "activate.ps1 does not call activate.py")
    h.require_contains("activate|", "scripts/emperor", "emperor bash missing activate")
    h.require_contains("scripts/activate", "hooks/hooks.json", "SessionStart missing activate")
    h.require_contains("MUST-route", "hooks/hooks.json", "SessionStart prompt missing MUST-route")
    h.require_contains(
        "must-route.md",
        "skills/emperor-resume/SKILL.md",
        "resume skill missing must-route",
    )
    h.require_contains(
        "using-superpowers",
        "skills/emperor-resume/must-route.md",
        "must-route missing provenance",
    )
    _, act_out = h.run_py("scripts/lib/activate.py", "--cwd", str(root))
    if not re.search(r"^ACTIVATION must_route=yes", act_out, re.M):
        h.fail_msg("activate missing must_route=yes")
    if not re.search(r"^ACTIVATION next=", act_out, re.M):
        h.fail_msg("activate missing next=")
    if not re.search(r"^MUST:", act_out, re.M):
        h.fail_msg("activate missing MUST line")
    _, act_u = h.run_py("scripts/lib/activate.py", "--cwd", str(root), "-u", "red build")
    if "emperor-heal" not in act_u:
        h.fail_msg("activate utterance red build → heal")

    # ---- route.py ----
    h.section("route.py Python core")
    h.need("scripts/lib/route.py")
    h.py_compile("scripts/lib/route.py", "route.py compile")
    h.require_contains("lib/route.py", "scripts/route.sh", "route.sh does not call route.py")
    h.require_contains("lib/route.py", "scripts/route.ps1", "route.ps1 does not call route.py")
    # thin twins must stay thin (utterance normalize lives in route.py)
    route_sh = (root / "scripts/route.sh").read_text(encoding="utf-8")
    route_ps1 = (root / "scripts/route.ps1").read_text(encoding="utf-8")
    if len(route_sh.splitlines()) > 20:
        h.fail_msg("route.sh should be thin twin (<=20 lines)")
    if len(route_ps1.splitlines()) > 30:
        h.fail_msg("route.ps1 should be thin twin (<=30 lines)")
    h.require_contains(".f90", "evals/triggers.json", "triggers missing .f90 excavate pattern")
    h.require_contains("fortran", "evals/triggers.json", "triggers missing fortran excavate pattern")
    h.require_contains("gfortran", "evals/triggers.json", "triggers missing gfortran excavate pattern")
    _, rout_py = h.run_py("scripts/lib/route.py", "finish the branch")
    if "emperor-forge" not in rout_py:
        h.fail_msg("route.py finish the branch → forge")
    _, rout_f90 = h.run_py("scripts/lib/route.py", "hello.f90")
    if "emperor-excavate" not in rout_f90:
        h.fail_msg("route.py hello.f90 → excavate")
    rc, _ = h.run_py("scripts/lib/route.py", "what is 2+2")
    if rc == 0:
        h.fail_msg("route.py should miss trivia")
    else:
        h.pass_msg("route.py misses trivia + fortran excavate + thin twins")

    # ---- MUST-route doctrine ----
    h.section("MUST-route doctrine + adapters")
    h.require_contains(
        "MUST: pick one governing",
        "SKILL.md",
        "SKILL Load law missing MUST governing",
    )
    h.require_contains(
        "MUST-route (standing order)",
        "AGENTS.md",
        "AGENTS missing MUST-route standing order",
    )
    h.require_contains("MUST-route", "hooks/hooks.json", "SessionStart prompt missing MUST-route")
    for ad in ("cursor", "codex", "kimi-cli", "ollama", "opencode", "generic"):
        h.require_contains(
            "MUST-route (before creative work)",
            f"adapters/{ad}/README.md",
            f"adapters/{ad} missing MUST-route note",
        )
    h.require_contains(
        "scripts/lib/route.py",
        "references/sdlc-comparison.md",
        "sdlc-comparison missing route.py",
    )
    h.require_contains(
        "eval.yml",
        "references/sdlc-comparison.md",
        "sdlc-comparison missing eval.yml honesty",
    )

    # Heal — explicit (card helpers above got too abstract; keep explicit like bash)
    h.section("heal four-phase debug leaf")
    h.need("skills/emperor-heal/debug-four-phases.md")
    h.need("scripts/lib/debug_phases.py")
    h.need("scripts/heal.sh")
    h.need("scripts/heal.ps1")
    h.bash_n("scripts/heal.sh", "heal.sh syntax")
    h.py_compile("scripts/lib/debug_phases.py", "debug_phases.py compile")
    h.require_contains("debug_phases.py", "scripts/heal.sh", "heal.sh does not call debug_phases.py")
    h.require_contains("debug_phases.py", "scripts/heal.ps1", "heal.ps1 does not call debug_phases.py")
    h.require_contains("heal|", "scripts/emperor", "emperor bash missing heal")
    h.require_contains("'heal'", "scripts/emperor.ps1", "emperor.ps1 missing heal")
    h.require_contains(
        "debug-four-phases.md",
        "skills/emperor-heal/SKILL.md",
        "heal skill missing four-phase leaf",
    )
    h.require_contains(
        "The Four Phases",
        "skills/emperor-heal/debug-four-phases.md",
        "four-phase leaf missing provenance heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/debug-four-phases.md",
        "four-phase leaf missing source skill",
    )
    h.require_contains(
        "debug-four-phases.md",
        "chains/holy-chain/SKILL.md",
        "holy-chain missing four-phase MUST",
    )
    _, heal_out = h.run_py("scripts/lib/debug_phases.py")
    if not re.search(r"^DEBUG four_phases=yes", heal_out, re.M):
        h.fail_msg("debug_phases missing four_phases=yes")
    if not re.search(r"^PHASE 1 ", heal_out, re.M):
        h.fail_msg("debug_phases missing PHASE 1")
    if not re.search(r"^PHASE 4 ", heal_out, re.M):
        h.fail_msg("debug_phases missing PHASE 4")
    if not re.search(r"^MUST:", heal_out, re.M):
        h.fail_msg("debug_phases missing MUST line")
    rc, _ = h.run_py("scripts/lib/debug_phases.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("debug_phases should reject phase skip 1→3")
    else:
        h.pass_msg("debug_phases rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/debug_phases.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("debug_phases 2→3 should OK")
    _, heal_sh = h.run_sh("scripts/heal.sh")
    if not re.search(r"^DEBUG four_phases=yes", heal_sh, re.M):
        h.fail_msg("heal.sh missing four_phases card")

    # grill
    h.section("grill brainstorm HARD-GATE leaf")
    h.need("skills/emperor-require-design/grill-checklist.md")
    h.need("scripts/lib/grill.py")
    h.need("scripts/grill.sh")
    h.need("scripts/grill.ps1")
    h.bash_n("scripts/grill.sh", "grill.sh syntax")
    h.py_compile("scripts/lib/grill.py", "grill.py compile")
    h.require_contains("grill.py", "scripts/grill.sh", "grill.sh does not call grill.py")
    h.require_contains("grill.py", "scripts/grill.ps1", "grill.ps1 does not call grill.py")
    h.require_contains("grill|", "scripts/emperor", "emperor bash missing grill")
    h.require_contains("'grill'", "scripts/emperor.ps1", "emperor.ps1 missing grill")
    h.require_contains(
        "grill-checklist.md",
        "skills/emperor-require-design/SKILL.md",
        "require-design missing grill leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-require-design/grill-checklist.md",
        "grill leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "brainstorming",
        "skills/emperor-require-design/grill-checklist.md",
        "grill leaf missing source skill",
    )
    _, grill_out = h.run_py("scripts/lib/grill.py")
    if not re.search(r"^GRILL checklist=yes", grill_out, re.M):
        h.fail_msg("grill missing checklist=yes")
    if not re.search(r"^STEP 1 ", grill_out, re.M):
        h.fail_msg("grill missing STEP 1")
    if not re.search(r"^STEP 5 ", grill_out, re.M):
        h.fail_msg("grill missing STEP 5")
    if not re.search(r"^MUST:", grill_out, re.M):
        h.fail_msg("grill missing MUST line")
    rc, _ = h.run_py("scripts/lib/grill.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("grill should reject step skip 1→3")
    else:
        h.pass_msg("grill rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/grill.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("grill 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/grill.py", "--reject-impl")
    if rc == 0:
        h.fail_msg("grill --reject-impl should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/grill.py", "--reject-impl")
        if not re.search(r"^REJECT IMPL:", reject, re.M):
            h.fail_msg("reject-impl missing REJECT IMPL line")
        else:
            h.pass_msg("grill --reject-impl hard-gates impl")
    _, grill_sh = h.run_sh("scripts/grill.sh")
    if not re.search(r"^GRILL checklist=yes", grill_sh, re.M):
        h.fail_msg("grill.sh missing checklist card")

    # tdd
    h.section("tdd iron-law / RGR HARD-GATE leaf")
    h.need("skills/emperor-tdd/red-green-refactor.md")
    h.need("scripts/lib/tdd.py")
    h.need("scripts/tdd.sh")
    h.need("scripts/tdd.ps1")
    h.bash_n("scripts/tdd.sh", "tdd.sh syntax")
    h.py_compile("scripts/lib/tdd.py", "tdd.py compile")
    h.require_contains("tdd.py", "scripts/tdd.sh", "tdd.sh does not call tdd.py")
    h.require_contains("tdd.py", "scripts/tdd.ps1", "tdd.ps1 does not call tdd.py")
    h.require_contains("tdd|", "scripts/emperor", "emperor bash missing tdd")
    h.require_contains("'tdd'", "scripts/emperor.ps1", "emperor.ps1 missing tdd")
    h.require_contains(
        "red-green-refactor.md",
        "skills/emperor-tdd/SKILL.md",
        "emperor-tdd missing RGR leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-tdd/red-green-refactor.md",
        "tdd leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "test-driven-development",
        "skills/emperor-tdd/red-green-refactor.md",
        "tdd leaf missing source skill",
    )
    _, tdd_out = h.run_py("scripts/lib/tdd.py")
    if not re.search(r"^TDD checklist=yes", tdd_out, re.M):
        h.fail_msg("tdd missing checklist=yes")
    if not re.search(r"^STEP 1 ", tdd_out, re.M):
        h.fail_msg("tdd missing STEP 1")
    if not re.search(r"^STEP 5 ", tdd_out, re.M):
        h.fail_msg("tdd missing STEP 5")
    if not re.search(r"^MUST:", tdd_out, re.M):
        h.fail_msg("tdd missing MUST line")
    if "NO_PRODUCTION_CODE_WITHOUT_FAILING_PROBE_FIRST" not in tdd_out:
        h.fail_msg("tdd missing iron law token")
    rc, _ = h.run_py("scripts/lib/tdd.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("tdd should reject step skip 1→3")
    else:
        h.pass_msg("tdd rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/tdd.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("tdd 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/tdd.py", "--reject-prod")
    if rc == 0:
        h.fail_msg("tdd --reject-prod should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/tdd.py", "--reject-prod")
        if not re.search(r"^REJECT PROD:", reject, re.M):
            h.fail_msg("reject-prod missing REJECT PROD line")
        else:
            h.pass_msg("tdd --reject-prod hard-gates prod")
    _, tdd_sh = h.run_sh("scripts/tdd.sh")
    if not re.search(r"^TDD checklist=yes", tdd_sh, re.M):
        h.fail_msg("tdd.sh missing checklist card")

    # worktree iso
    h.section("worktree isolation HARD-GATE leaf")
    h.need("skills/emperor-worktree/isolation-checklist.md")
    h.need("scripts/lib/worktree_iso.py")
    h.need("scripts/iso.sh")
    h.need("scripts/iso.ps1")
    h.bash_n("scripts/iso.sh", "iso.sh syntax")
    h.py_compile("scripts/lib/worktree_iso.py", "worktree_iso.py compile")
    h.require_contains("worktree_iso.py", "scripts/iso.sh", "iso.sh does not call worktree_iso.py")
    h.require_contains("worktree_iso.py", "scripts/iso.ps1", "iso.ps1 does not call worktree_iso.py")
    h.require_contains("iso|", "scripts/emperor", "emperor bash missing iso")
    h.require_contains("'iso'", "scripts/emperor.ps1", "emperor.ps1 missing iso")
    h.require_contains(
        "isolation-checklist.md",
        "skills/emperor-worktree/SKILL.md",
        "emperor-worktree missing isolation leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-worktree/isolation-checklist.md",
        "iso leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "using-git-worktrees",
        "skills/emperor-worktree/isolation-checklist.md",
        "iso leaf missing source skill",
    )
    _, iso_out = h.run_py("scripts/lib/worktree_iso.py")
    if not re.search(r"^WORKTREE checklist=yes", iso_out, re.M):
        h.fail_msg("iso missing checklist=yes")
    if not re.search(r"^STEP 1 ", iso_out, re.M):
        h.fail_msg("iso missing STEP 1")
    if not re.search(r"^STEP 5 ", iso_out, re.M):
        h.fail_msg("iso missing STEP 5")
    if not re.search(r"^MUST:", iso_out, re.M):
        h.fail_msg("iso missing MUST line")
    if "NO_MUTATE_WITHOUT_ISOLATION_DETECT" not in iso_out:
        h.fail_msg("iso missing iron law token")
    rc, _ = h.run_py("scripts/lib/worktree_iso.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("iso should reject step skip 1→3")
    else:
        h.pass_msg("iso rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/worktree_iso.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("iso 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/worktree_iso.py", "--reject-blind-create")
    if rc == 0:
        h.fail_msg("iso --reject-blind-create should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/worktree_iso.py", "--reject-blind-create")
        if not re.search(r"^REJECT BLIND-CREATE:", reject, re.M):
            h.fail_msg("reject-blind-create missing REJECT line")
        else:
            h.pass_msg("iso --reject-blind-create hard-gates blind create")
    _, iso_sh = h.run_sh("scripts/iso.sh")
    if not re.search(r"^WORKTREE checklist=yes", iso_sh, re.M):
        h.fail_msg("iso.sh missing checklist card")

    # request-review
    h.section("request-review HARD-GATE leaf")
    h.need("skills/emperor-verify/request-review-checklist.md")
    h.need("scripts/lib/review_req.py")
    h.need("scripts/review.sh")
    h.need("scripts/review.ps1")
    h.bash_n("scripts/review.sh", "review.sh syntax")
    h.py_compile("scripts/lib/review_req.py", "review_req.py compile")
    h.require_contains("review_req.py", "scripts/review.sh", "review.sh does not call review_req.py")
    h.require_contains("review_req.py", "scripts/review.ps1", "review.ps1 does not call review_req.py")
    h.require_contains("review|", "scripts/emperor", "emperor bash missing review")
    h.require_contains("'review'", "scripts/emperor.ps1", "emperor.ps1 missing review")
    h.require_contains(
        "request-review-checklist.md",
        "skills/emperor-verify/SKILL.md",
        "emperor-verify missing request-review leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-verify/request-review-checklist.md",
        "review leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "requesting-code-review",
        "skills/emperor-verify/request-review-checklist.md",
        "review leaf missing source skill",
    )
    _, rev_out = h.run_py("scripts/lib/review_req.py")
    if not re.search(r"^REVIEW checklist=yes", rev_out, re.M):
        h.fail_msg("review missing checklist=yes")
    if not re.search(r"^STEP 1 ", rev_out, re.M):
        h.fail_msg("review missing STEP 1")
    if not re.search(r"^STEP 5 ", rev_out, re.M):
        h.fail_msg("review missing STEP 5")
    if not re.search(r"^MUST:", rev_out, re.M):
        h.fail_msg("review missing MUST line")
    if "NO_PROCEED_WITHOUT_REQUESTED_REVIEW" not in rev_out:
        h.fail_msg("review missing iron law token")
    rc, _ = h.run_py("scripts/lib/review_req.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("review should reject step skip 1→3")
    else:
        h.pass_msg("review rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/review_req.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("review 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/review_req.py", "--reject-self-review")
    if rc == 0:
        h.fail_msg("review --reject-self-review should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/review_req.py", "--reject-self-review")
        if not re.search(r"^REJECT SELF-REVIEW:", reject, re.M):
            h.fail_msg("reject-self-review missing REJECT line")
        else:
            h.pass_msg("review --reject-self-review hard-gates self-review")
    _, rev_sh = h.run_sh("scripts/review.sh")
    if not re.search(r"^REVIEW checklist=yes", rev_sh, re.M):
        h.fail_msg("review.sh missing checklist card")

    # author
    h.section("authoring iron-law / skill RGR HARD-GATE leaf")
    h.need("chains/chain-jail/authoring-checklist.md")
    h.need("scripts/lib/author.py")
    h.need("scripts/author.sh")
    h.need("scripts/author.ps1")
    h.bash_n("scripts/author.sh", "author.sh syntax")
    h.py_compile("scripts/lib/author.py", "author.py compile")
    h.require_contains("author.py", "scripts/author.sh", "author.sh does not call author.py")
    h.require_contains("author.py", "scripts/author.ps1", "author.ps1 does not call author.py")
    h.require_contains("author|", "scripts/emperor", "emperor bash missing author")
    h.require_contains("'author'", "scripts/emperor.ps1", "emperor.ps1 missing author")
    h.require_contains(
        "authoring-checklist.md",
        "chains/chain-jail/SKILL.md",
        "chain-jail missing authoring leaf",
    )
    h.require_contains(
        "authoring-checklist.md",
        "chains/chain-jail/authoring.md",
        "authoring.md missing checklist pointer",
    )
    h.require_contains(
        "HARD-GATE",
        "chains/chain-jail/authoring-checklist.md",
        "author leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "writing-skills",
        "chains/chain-jail/authoring-checklist.md",
        "author leaf missing source skill",
    )
    h.require_contains(
        "authoring-checklist.md",
        "skills/emperor-capture/SKILL.md",
        "emperor-capture missing authoring leaf",
    )
    _, auth_out = h.run_py("scripts/lib/author.py")
    if not re.search(r"^AUTHOR checklist=yes", auth_out, re.M):
        h.fail_msg("author missing checklist=yes")
    if not re.search(r"^STEP 1 ", auth_out, re.M):
        h.fail_msg("author missing STEP 1")
    if not re.search(r"^STEP 5 ", auth_out, re.M):
        h.fail_msg("author missing STEP 5")
    if not re.search(r"^MUST:", auth_out, re.M):
        h.fail_msg("author missing MUST line")
    if "NO_SKILL_WITHOUT_FAILING_BASELINE_FIRST" not in auth_out:
        h.fail_msg("author missing iron law token")
    rc, _ = h.run_py("scripts/lib/author.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("author should reject step skip 1→3")
    else:
        h.pass_msg("author rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/author.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("author 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/author.py", "--reject-untested")
    if rc == 0:
        h.fail_msg("author --reject-untested should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/author.py", "--reject-untested")
        if not re.search(r"^REJECT UNTESTED:", reject, re.M):
            h.fail_msg("reject-untested missing REJECT line")
        else:
            h.pass_msg("author --reject-untested hard-gates untested skill write")
    _, auth_sh = h.run_sh("scripts/author.sh")
    if not re.search(r"^AUTHOR checklist=yes", auth_sh, re.M):
        h.fail_msg("author.sh missing checklist card")

    # evidence
    h.section("verification-before-completion / evidence HARD-GATE leaf")
    h.need("skills/emperor-verify/verification-checklist.md")
    h.need("scripts/lib/evidence.py")
    h.need("scripts/evidence.sh")
    h.need("scripts/evidence.ps1")
    h.bash_n("scripts/evidence.sh", "evidence.sh syntax")
    h.py_compile("scripts/lib/evidence.py", "evidence.py compile")
    h.require_contains("evidence.py", "scripts/evidence.sh", "evidence.sh does not call evidence.py")
    h.require_contains("evidence.py", "scripts/evidence.ps1", "evidence.ps1 does not call evidence.py")
    h.require_contains("evidence|", "scripts/emperor", "emperor bash missing evidence")
    h.require_contains("'evidence'", "scripts/emperor.ps1", "emperor.ps1 missing evidence")
    h.require_contains(
        "verification-checklist.md",
        "skills/emperor-verify/SKILL.md",
        "emperor-verify missing evidence leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-verify/verification-checklist.md",
        "evidence leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "verification-before-completion",
        "skills/emperor-verify/verification-checklist.md",
        "evidence leaf missing source skill",
    )
    _, evid_out = h.run_py("scripts/lib/evidence.py")
    if not re.search(r"^EVIDENCE checklist=yes", evid_out, re.M):
        h.fail_msg("evidence missing checklist=yes")
    if not re.search(r"^STEP 1 ", evid_out, re.M):
        h.fail_msg("evidence missing STEP 1")
    if not re.search(r"^STEP 5 ", evid_out, re.M):
        h.fail_msg("evidence missing STEP 5")
    if not re.search(r"^MUST:", evid_out, re.M):
        h.fail_msg("evidence missing MUST line")
    if "NO_COMPLETION_CLAIMS_WITHOUT_FRESH_VERIFICATION_EVIDENCE" not in evid_out:
        h.fail_msg("evidence missing iron law token")
    rc, _ = h.run_py("scripts/lib/evidence.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("evidence should reject step skip 1→3")
    else:
        h.pass_msg("evidence rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/evidence.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("evidence 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/evidence.py", "--reject-unverified")
    if rc == 0:
        h.fail_msg("evidence --reject-unverified should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/evidence.py", "--reject-unverified")
        if not re.search(r"^REJECT UNVERIFIED:", reject, re.M):
            h.fail_msg("reject-unverified missing REJECT line")
        else:
            h.pass_msg("evidence --reject-unverified hard-gates unverified claims")
    _, evid_sh = h.run_sh("scripts/evidence.sh")
    if not re.search(r"^EVIDENCE checklist=yes", evid_sh, re.M):
        h.fail_msg("evidence.sh missing checklist card")

    # receive-review
    h.section("receiving-code-review / receive HARD-GATE leaf")
    h.need("skills/emperor-verify/receive-review-checklist.md")
    h.need("scripts/lib/receive.py")
    h.need("scripts/receive.sh")
    h.need("scripts/receive.ps1")
    h.bash_n("scripts/receive.sh", "receive.sh syntax")
    h.py_compile("scripts/lib/receive.py", "receive.py compile")
    h.require_contains("receive.py", "scripts/receive.sh", "receive.sh does not call receive.py")
    h.require_contains("receive.py", "scripts/receive.ps1", "receive.ps1 does not call receive.py")
    h.require_contains("receive|", "scripts/emperor", "emperor bash missing receive")
    h.require_contains("'receive'", "scripts/emperor.ps1", "emperor.ps1 missing receive")
    h.require_contains(
        "receive-review-checklist.md",
        "skills/emperor-verify/SKILL.md",
        "emperor-verify missing receive-review leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-verify/receive-review-checklist.md",
        "receive leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "receiving-code-review",
        "skills/emperor-verify/receive-review-checklist.md",
        "receive leaf missing source skill",
    )
    _, recv_out = h.run_py("scripts/lib/receive.py")
    if not re.search(r"^RECEIVE checklist=yes", recv_out, re.M):
        h.fail_msg("receive missing checklist=yes")
    if not re.search(r"^STEP 1 ", recv_out, re.M):
        h.fail_msg("receive missing STEP 1")
    if not re.search(r"^STEP 6 ", recv_out, re.M):
        h.fail_msg("receive missing STEP 6")
    if not re.search(r"^MUST:", recv_out, re.M):
        h.fail_msg("receive missing MUST line")
    if "NO_IMPLEMENT_WITHOUT_VERIFYING_REVIEW_FEEDBACK" not in recv_out:
        h.fail_msg("receive missing iron law token")
    rc, _ = h.run_py("scripts/lib/receive.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("receive should reject step skip 1→3")
    else:
        h.pass_msg("receive rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/receive.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("receive 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/receive.py", "--reject-blind-implement")
    if rc == 0:
        h.fail_msg("receive --reject-blind-implement should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/receive.py", "--reject-blind-implement")
        if not re.search(r"^REJECT BLIND-IMPLEMENT:", reject, re.M):
            h.fail_msg("reject-blind-implement missing REJECT line")
        else:
            h.pass_msg("receive --reject-blind-implement hard-gates blind implement")
    _, recv_sh = h.run_sh("scripts/receive.sh")
    if not re.search(r"^RECEIVE checklist=yes", recv_sh, re.M):
        h.fail_msg("receive.sh missing checklist card")

    # execute-plans
    h.section("executing-plans / execute HARD-GATE leaf")
    h.need("skills/emperor-build/executing-plans-checklist.md")
    h.need("scripts/lib/execute.py")
    h.need("scripts/execute.sh")
    h.need("scripts/execute.ps1")
    h.bash_n("scripts/execute.sh", "execute.sh syntax")
    h.py_compile("scripts/lib/execute.py", "execute.py compile")
    h.require_contains("execute.py", "scripts/execute.sh", "execute.sh does not call execute.py")
    h.require_contains("execute.py", "scripts/execute.ps1", "execute.ps1 does not call execute.py")
    h.require_contains("execute|", "scripts/emperor", "emperor bash missing execute")
    h.require_contains("'execute'", "scripts/emperor.ps1", "emperor.ps1 missing execute")
    h.require_contains(
        "executing-plans-checklist.md",
        "skills/emperor-build/SKILL.md",
        "emperor-build missing executing-plans leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-build/executing-plans-checklist.md",
        "execute leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "executing-plans",
        "skills/emperor-build/executing-plans-checklist.md",
        "execute leaf missing source skill",
    )
    _, exec_out = h.run_py("scripts/lib/execute.py")
    if not re.search(r"^EXECUTE checklist=yes", exec_out, re.M):
        h.fail_msg("execute missing checklist=yes")
    if not re.search(r"^STEP 1 ", exec_out, re.M):
        h.fail_msg("execute missing STEP 1")
    if not re.search(r"^STEP 6 ", exec_out, re.M):
        h.fail_msg("execute missing STEP 6")
    if not re.search(r"^MUST:", exec_out, re.M):
        h.fail_msg("execute missing MUST line")
    if "NO_CHECKIN_THEATER_FOUR_STOPS_ONLY" not in exec_out:
        h.fail_msg("execute missing iron law token")
    rc, _ = h.run_py("scripts/lib/execute.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("execute should reject step skip 1→3")
    else:
        h.pass_msg("execute rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/execute.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("execute 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/execute.py", "--reject-checkin")
    if rc == 0:
        h.fail_msg("execute --reject-checkin should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/execute.py", "--reject-checkin")
        if not re.search(r"^REJECT CHECKIN:", reject, re.M):
            h.fail_msg("reject-checkin missing REJECT line")
        else:
            h.pass_msg("execute --reject-checkin hard-gates check-in theater")
    _, exec_sh = h.run_sh("scripts/execute.sh")
    if not re.search(r"^EXECUTE checklist=yes", exec_sh, re.M):
        h.fail_msg("execute.sh missing checklist card")


    # ---- done probes (Python core) ----
    h.section("done probes (Python core)")
    h.need("scripts/lib/done.py")
    h.need("scripts/done.sh")
    h.need("scripts/done.ps1")
    h.need("evals/fixtures/done-probes/ok/DONE.md")
    h.need("evals/fixtures/done-probes/fail/DONE.md")
    h.need("evals/fixtures/done-probes/no-probes/DONE.md")
    h.bash_n("scripts/done.sh", "done.sh syntax")
    h.py_compile("scripts/lib/done.py", "done.py compile")
    h.require_contains("lib/done.py", "scripts/done.sh", "done.sh thin twin missing done.py")
    h.require_contains("lib/done.py", "scripts/done.ps1", "done.ps1 thin twin missing done.py")
    # thin twins must stay thin (probe runner lives in done.py)
    done_sh_lines = len((root / "scripts/done.sh").read_text(encoding="utf-8").splitlines())
    done_ps_lines = len((root / "scripts/done.ps1").read_text(encoding="utf-8").splitlines())
    if done_sh_lines > 20:
        h.fail_msg("done.sh should be thin twin (<=20 lines)")
    if done_ps_lines > 30:
        h.fail_msg("done.ps1 should be thin twin (<=30 lines)")
    h.require_contains(
        "scripts/lib/done.py",
        "references/dogma.md",
        "dogma.md missing done.py",
    )
    rc, ok_out = h.run_sh("scripts/done.sh", "evals/fixtures/done-probes/ok")
    if rc != 0 or "DONE OK" not in ok_out:
        h.fail_msg("done ok fixture should PASS + DONE OK")
    else:
        h.pass_msg("done ok fixture")
    rc, fail_out = h.run_sh("scripts/done.sh", "evals/fixtures/done-probes/fail")
    if rc == 0:
        h.fail_msg("done fail fixture should exit non-zero")
    elif "DONE FAIL:" not in fail_out:
        h.fail_msg("done fail fixture missing DONE FAIL")
    else:
        h.pass_msg("done fail fixture")
    rc, nop_out = h.run_py("scripts/lib/done.py", "evals/fixtures/done-probes/no-probes")
    if rc == 0:
        h.fail_msg("done no-probes should exit non-zero")
    else:
        h.pass_msg("done no-probes rejected")
    h.require_contains("done|", "scripts/emperor", "emperor bash missing done")
    h.pass_msg("done.py thin twins + probe fixtures")

    # ---- forge.py consent + PR body ----
    h.section("forge.py Python core")
    h.need("scripts/lib/forge.py")
    h.need("scripts/forge.sh")
    h.need("scripts/forge.ps1")
    h.bash_n("scripts/forge.sh", "forge.sh syntax")
    h.py_compile("scripts/lib/forge.py", "forge.py compile")
    h.require_contains("lib/forge.py", "scripts/forge.sh", "forge.sh thin twin missing forge.py")
    h.require_contains("lib/forge.py", "scripts/forge.ps1", "forge.ps1 thin twin missing forge.py")
    forge_sh_lines = len((root / "scripts/forge.sh").read_text(encoding="utf-8").splitlines())
    forge_ps_lines = len((root / "scripts/forge.ps1").read_text(encoding="utf-8").splitlines())
    if forge_sh_lines > 20:
        h.fail_msg("forge.sh should be thin twin (<=20 lines)")
    if forge_ps_lines > 30:
        h.fail_msg("forge.ps1 should be thin twin (<=30 lines)")
    h.require_contains(
        "scripts/lib/forge.py",
        "references/software-factory.md",
        "software-factory.md missing forge.py",
    )
    h.require_contains(
        "forge.py",
        "skills/emperor-forge/SKILL.md",
        "emperor-forge skill missing forge.py",
    )
    h.require_contains(
        "scripts/lib/forge.py",
        "references/mechanical-gates.md",
        "mechanical-gates.md missing forge.py",
    )
    tmpf = Path(tempfile.mkdtemp())
    try:
        (tmpf / "ledger.md").write_text(
            "# Task: ship the widget\n"
            "## G0\nOrigin: eval\n"
            "## G1 Acceptance criteria\n"
            "1. Widget ships\n"
            "## G2\nDesign\n",
            encoding="utf-8",
        )
        (tmpf / "DONE.md").write_text(
            "probe: echo HELLO_EMPEROR_DONE\nexpect: HELLO_EMPEROR_DONE\n",
            encoding="utf-8",
        )
        rc, out = h.run_sh("scripts/forge.sh", str(tmpf))
        if rc != 3 or "FORGE REFUSED" not in out:
            h.fail_msg("forge without consent should refuse exit 3")
        else:
            h.pass_msg("forge refuses without consent")
        rc, out = h.run_sh(
            "scripts/forge.sh",
            str(tmpf),
            env={"EMPEROR_CONSENT_PR": "1", "EMPEROR_FORGE_DRY": "1"},
        )
        if rc != 0 or "FORGE DRY" not in out:
            h.fail_msg("forge with consent should DRY exit 0")
        elif "ship the widget" not in out:
            h.fail_msg("forge DRY missing extracted title")
        else:
            h.pass_msg("forge DRY with title")
        pr = (tmpf / "PR.md").read_text(encoding="utf-8")
        g1_part = pr.split("## DONE probes")[0]
        if "## G1 Acceptance criteria" not in pr or "Widget ships" not in pr:
            h.fail_msg("forge PR.md missing G1 section")
        elif "## DONE probes" not in pr or "HELLO_EMPEROR_DONE" not in pr:
            h.fail_msg("forge PR.md missing DONE probes")
        elif "## G0" in g1_part or "Origin: eval" in g1_part:
            # ps1 twin used to dump the full ledger; G0 must stay out of PR body.
            h.fail_msg("forge PR.md dumped full ledger (G0 leak) — twin drift")
        else:
            h.pass_msg("forge PR.md G1+DONE only")
    finally:
        shutil.rmtree(tmpf, ignore_errors=True)
    h.pass_msg("forge.py thin twins + consent + PR body")

    # ---- review_pack.py isolated pack ----
    h.section("review_pack.py Python core")
    h.need("scripts/lib/review_pack.py")
    h.need("scripts/review-pack.sh")
    h.need("scripts/review-pack.ps1")
    h.bash_n("scripts/review-pack.sh", "review-pack.sh syntax")
    h.py_compile("scripts/lib/review_pack.py", "review_pack.py compile")
    h.require_contains(
        "lib/review_pack.py",
        "scripts/review-pack.sh",
        "review-pack.sh thin twin missing review_pack.py",
    )
    h.require_contains(
        "lib/review_pack.py",
        "scripts/review-pack.ps1",
        "review-pack.ps1 thin twin missing review_pack.py",
    )
    rp_sh_lines = len((root / "scripts/review-pack.sh").read_text(encoding="utf-8").splitlines())
    rp_ps_lines = len((root / "scripts/review-pack.ps1").read_text(encoding="utf-8").splitlines())
    if rp_sh_lines > 20:
        h.fail_msg("review-pack.sh should be thin twin (<=20 lines)")
    if rp_ps_lines > 30:
        h.fail_msg("review-pack.ps1 should be thin twin (<=30 lines)")
    h.require_contains(
        "scripts/lib/review_pack.py",
        "references/mechanical-gates.md",
        "mechanical-gates.md missing review_pack.py",
    )
    h.require_contains(
        "review_pack.py",
        "skills/emperor-verify/SKILL.md",
        "emperor-verify skill missing review_pack.py",
    )
    h.require_contains(
        "review_pack.py",
        "skills/emperor-verify/request-review-checklist.md",
        "request-review-checklist missing review_pack.py",
    )
    tmpr = Path(tempfile.mkdtemp())
    try:
        (tmpr / "work-order.md").write_text(
            (
                "# Work Order — eval-pack\n"
                "## Plan header (agentic handoff)\n"
                "**Goal:** should not leak into criteria\n"
                "## Acceptance criteria (checkable)\n"
                "1. Widget ships\n"
                "2. Diff is isolated\n"
                "## Out of scope\n"
                "- Plan header leak\n"
                "## Approach\n"
                "Should not appear in criteria.md\n"
            ),
            encoding="utf-8",
        )
        (tmpr / "claims.md").write_text(
            "| Claim | Status | Evidence |\n|---|---|---|\n| x | VERIFIED | y |\n",
            encoding="utf-8",
        )
        rc, out = h.run_sh("scripts/review-pack.sh", str(tmpr), "HEAD~1", "HEAD")
        if rc != 0 or "REVIEW PACK:" not in out:
            h.fail_msg("review-pack should emit REVIEW PACK")
        else:
            h.pass_msg("review-pack emits pack")
        criteria = (tmpr / "review-pack" / "criteria.md").read_text(encoding="utf-8")
        if "## Acceptance criteria" not in criteria or "Widget ships" not in criteria:
            h.fail_msg("review-pack criteria.md missing Acceptance section")
        elif (
            "## Plan header" in criteria
            or "should not leak" in criteria
            or "## Out of scope" in criteria
            or "## Approach" in criteria
            or "Should not appear" in criteria
        ):
            # ps1 twin used to copy the full work-order; Plan/Out-of-scope must stay out.
            h.fail_msg("review-pack criteria.md dumped full work-order — twin drift")
        else:
            h.pass_msg("review-pack criteria extract only")
        meta = (tmpr / "review-pack" / "meta.md").read_text(encoding="utf-8")
        if "- base:" not in meta or "- head:" not in meta:
            h.fail_msg("review-pack meta.md missing base/head")
        else:
            h.pass_msg("review-pack meta SHAs")
        if not (tmpr / "review-pack" / "claims.md").is_file():
            h.fail_msg("review-pack missing claims.md copy")
        else:
            h.pass_msg("review-pack claims copy")
    finally:
        shutil.rmtree(tmpr, ignore_errors=True)
    h.pass_msg("review_pack.py thin twins + criteria extract")

    # ---- dowse.py machine scan ----
    h.section("dowse.py Python core")
    h.need("scripts/lib/dowse.py")
    h.need("scripts/dowse.sh")
    h.need("scripts/dowse.ps1")
    h.bash_n("scripts/dowse.sh", "dowse.sh syntax")
    h.py_compile("scripts/lib/dowse.py", "dowse.py compile")
    h.require_contains(
        "lib/dowse.py",
        "scripts/dowse.sh",
        "dowse.sh thin twin missing dowse.py",
    )
    h.require_contains(
        "lib/dowse.py",
        "scripts/dowse.ps1",
        "dowse.ps1 thin twin missing dowse.py",
    )
    dw_sh_lines = len((root / "scripts/dowse.sh").read_text(encoding="utf-8").splitlines())
    dw_ps_lines = len((root / "scripts/dowse.ps1").read_text(encoding="utf-8").splitlines())
    if dw_sh_lines > 20:
        h.fail_msg("dowse.sh should be thin twin (<=20 lines)")
    if dw_ps_lines > 40:
        h.fail_msg("dowse.ps1 should be thin twin (<=40 lines)")
    h.require_contains(
        "scripts/lib/dowse.py",
        "chains/dowsing-chain/system-dowsing.md",
        "system-dowsing.md missing dowse.py",
    )
    h.require_contains(
        "dowse.py",
        "references/agent-registry.md",
        "agent-registry.md missing dowse.py",
    )
    h.require_contains(
        "dowse.py",
        "references/mechanical-gates.md",
        "mechanical-gates.md missing dowse.py",
    )
    h.require_contains(
        "--as-json",
        "scripts/lib/dowse.py",
        "dowse.py missing --as-json",
    )
    h.require_contains(
        "--as-json",
        "scripts/dowse.sh",
        "dowse.sh usage missing --as-json",
    )
    h.require_contains(
        "AsJson",
        "scripts/dowse.ps1",
        "dowse.ps1 missing -AsJson switch",
    )
    rc, out = h.run_py("scripts/lib/dowse.py", "--skip-versions", "--as-json")
    if rc != 0:
        h.fail_msg("dowse.py --as-json should exit 0")
    else:
        try:
            import json as _json

            roster = _json.loads(out)
            if not isinstance(roster, list) or len(roster) < 5:
                h.fail_msg("dowse --as-json roster too short")
            else:
                keys = set(roster[0].keys())
                need = {"Agent", "Binary", "Status", "Version", "Auth", "Headless", "SignIn"}
                if not need.issubset(keys):
                    h.fail_msg(f"dowse richer roster missing keys: {need - keys}")
                else:
                    h.pass_msg("dowse --as-json richer roster")
                bins = {e.get("Binary") for e in roster}
                for b in ("claude", "codex", "gh", "ollama"):
                    if b not in bins:
                        h.fail_msg(f"dowse roster missing binary {b}")
                        break
                else:
                    h.pass_msg("dowse roster core binaries")
        except Exception as exc:  # noqa: BLE001 — eval harness
            h.fail_msg(f"dowse --as-json not parseable: {exc}")
    rc2, out2 = h.run_sh("scripts/dowse.sh", "--skip-versions", "--as-json")
    if rc2 != 0 or '"Headless"' not in out2 or '"SignIn"' not in out2:
        h.fail_msg("dowse.sh --as-json should emit richer roster")
    else:
        h.pass_msg("dowse.sh AsJson parity")
    h.pass_msg("dowse.py thin twins + AsJson richer roster")

    # bakeoff honesty
    h.section("bakeoff honesty (mechanism inventory + UNVERIFIABLE live rate)")
    h.need("evals/bakeoff.md")
    h.need("evals/fixtures/this-upgrade.md")
    h.need("scripts/lib/bakeoff_honesty.py")
    h.py_compile("scripts/lib/bakeoff_honesty.py", "bakeoff_honesty.py compile")
    rc, hon_out = h.run_py("scripts/lib/bakeoff_honesty.py", "--cwd", str(root))
    if rc != 0:
        print(hon_out)
        h.fail_msg("bakeoff_honesty.py exit non-zero")
    if not re.search(r"^BAKEOFF HONESTY OK", hon_out, re.M):
        h.fail_msg("bakeoff honesty missing OK")
    if not re.search(r"^LIVE_DEFECT_RATE=UNVERIFIABLE", hon_out, re.M):
        h.fail_msg("bakeoff honesty missing LIVE_DEFECT_RATE label")
    h.require_contains("UNVERIFIABLE", "evals/bakeoff.md", "bakeoff.md missing UNVERIFIABLE")
    h.require_contains("TESTED", "evals/bakeoff.md", "bakeoff.md missing TESTED")
    h.require_contains("lost-cbl", "evals/bakeoff.md", "bakeoff.md missing lost-cbl inventory")
    h.require_contains("lost-f90", "evals/bakeoff.md", "bakeoff.md missing lost-f90 inventory")
    h.require_contains(
        "UNVERIFIABLE",
        "evals/fixtures/this-upgrade.md",
        "this-upgrade.md missing UNVERIFIABLE",
    )
    h.require_contains("0.4.26", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.26 tip")
    h.require_contains("dowse.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing dowse.py")
    h.require_contains("gate.py", "evals/bakeoff.md", "bakeoff.md missing gate.py inventory")
    h.require_contains("eval.py", "evals/bakeoff.md", "bakeoff.md missing eval.py inventory")
    h.require_contains("done.py", "evals/bakeoff.md", "bakeoff.md missing done.py inventory")
    h.require_contains("queue.py", "evals/bakeoff.md", "bakeoff.md missing queue.py inventory")
    h.require_contains("forge.py", "evals/bakeoff.md", "bakeoff.md missing forge.py inventory")
    h.require_contains("review_pack.py", "evals/bakeoff.md", "bakeoff.md missing review_pack.py inventory")
    h.require_contains("dowse.py", "evals/bakeoff.md", "bakeoff.md missing dowse.py inventory")

    if h.fail != 0:
        print("EVALS FAILED")
        return 1
    print("EVALS PASSED")
    return 0


def main(argv: list[str] | None = None) -> int:
    # argv unused — parity with eval.sh (no args)
    _ = argv
    return run_evals(_root())


if __name__ == "__main__":
    sys.exit(main())
