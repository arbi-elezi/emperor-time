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
        "subagent",
        "parallel",
    ):
        h.need(f"scripts/{pair}.sh")
        h.need(f"scripts/{pair}.ps1")

    # ---- silent-boot PS ----
    h.section("silent-boot PS twin + host report helpers")
    h.require_contains(
        "lib/boot.py",
        "scripts/boot.ps1",
        "boot.ps1 thin twin missing boot.py",
    )
    h.require_contains(
        "Write-EmperorHostReport",
        "scripts/lib/host.ps1",
        "host.ps1 missing Write-EmperorHostReport",
    )
    h.require_contains(
        "host.py",
        "scripts/lib/host.ps1",
        "host.ps1 Write-EmperorHostReport missing host.py delegate",
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
    h.require_contains("*.vhd", "scripts/lib/identify.py", "identify.py missing *.vhd fossil")
    h.require_contains("*.adb", "scripts/lib/identify.py", "identify.py missing *.adb fossil")
    h.require_contains("*.fs", "scripts/lib/identify.py", "identify.py missing *.fs fossil")
    h.require_contains("*.lisp", "scripts/lib/identify.py", "identify.py missing *.lisp fossil")
    h.require_contains("*.pro", "scripts/lib/identify.py", "identify.py missing *.pro fossil")
    h.require_contains("*.tcl", "scripts/lib/identify.py", "identify.py missing *.tcl fossil")
    h.require_contains("*.erl", "scripts/lib/identify.py", "identify.py missing *.erl fossil")
    h.require_contains("*.rex", "scripts/lib/identify.py", "identify.py missing *.rex fossil")
    h.require_contains("*.mod", "scripts/lib/identify.py", "identify.py missing *.mod fossil")
    h.require_contains("*.a68", "scripts/lib/identify.py", "identify.py missing *.a68 fossil")
    h.require_contains("*.a60", "scripts/lib/identify.py", "identify.py missing *.a60 fossil")
    h.require_contains("*.alw", "scripts/lib/identify.py", "identify.py missing *.alw fossil")
    h.require_contains("*.icn", "scripts/lib/identify.py", "identify.py missing *.icn fossil")
    h.require_contains("*.obn", "scripts/lib/identify.py", "identify.py missing *.obn fossil")
    h.require_contains("*.sno", "scripts/lib/identify.py", "identify.py missing *.sno fossil")
    h.require_contains("*.sim", "scripts/lib/identify.py", "identify.py missing *.sim fossil")
    h.require_contains("*.apl", "scripts/lib/identify.py", "identify.py missing *.apl fossil")
    h.require_contains("*.b", "scripts/lib/identify.py", "identify.py missing *.b fossil")
    h.require_contains("*.bcpl", "scripts/lib/identify.py", "identify.py missing *.bcpl fossil")
    h.require_contains("*.pli", "scripts/lib/identify.py", "identify.py missing *.pli fossil")
    h.require_contains("*.pl1", "scripts/lib/identify.py", "identify.py missing *.pl1 fossil")
    h.require_contains("*.st", "scripts/lib/identify.py", "identify.py missing *.st fossil")
    h.require_contains("*.ps", "scripts/lib/identify.py", "identify.py missing *.ps fossil")
    h.require_contains("*.eps", "scripts/lib/identify.py", "identify.py missing *.eps fossil")
    h.require_contains("*.bas", "scripts/lib/identify.py", "identify.py missing *.bas fossil")
    h.require_contains("*.scm", "scripts/lib/identify.py", "identify.py missing *.scm fossil")
    h.require_contains("*.awk", "scripts/lib/identify.py", "identify.py missing *.awk fossil")
    h.require_contains("*.sed", "scripts/lib/identify.py", "identify.py missing *.sed fossil")
    h.require_contains("*.m4", "scripts/lib/identify.py", "identify.py missing *.m4 fossil")
    h.require_contains("*.ed", "scripts/lib/identify.py", "identify.py missing *.ed fossil")
    h.require_contains("*.mk", "scripts/lib/identify.py", "identify.py missing *.mk fossil")
    h.require_contains("*.dc", "scripts/lib/identify.py", "identify.py missing *.dc fossil")
    h.require_contains("*.l", "scripts/lib/identify.py", "identify.py missing *.l fossil")
    h.require_contains("*.lex", "scripts/lib/identify.py", "identify.py missing *.lex fossil")
    h.require_contains("*.y", "scripts/lib/identify.py", "identify.py missing *.y fossil")
    h.require_contains("*.roff", "scripts/lib/identify.py", "identify.py missing *.roff fossil")
    h.require_contains("*.pl", "scripts/lib/identify.py", "identify.py missing *.pl fossil")
    h.require_contains("*.pm", "scripts/lib/identify.py", "identify.py missing *.pm fossil")
    h.require_contains("*.bc", "scripts/lib/identify.py", "identify.py missing *.bc fossil")
    h.require_contains("*.exp", "scripts/lib/identify.py", "identify.py missing *.exp fossil")
    h.require_contains("*.lua", "scripts/lib/identify.py", "identify.py missing *.lua fossil")
    h.require_contains("*.rb", "scripts/lib/identify.py", "identify.py missing *.rb fossil")
    h.require_contains("*.go", "scripts/lib/identify.py", "identify.py missing *.go fossil")
    h.require_contains("*.rs", "scripts/lib/identify.py", "identify.py missing *.rs fossil")
    h.require_contains("*.c", "scripts/lib/identify.py", "identify.py missing *.c fossil")
    h.require_contains("*.js", "scripts/lib/identify.py", "identify.py missing *.js fossil")
    h.require_contains("*.py", "scripts/lib/identify.py", "identify.py missing *.py fossil")
    h.require_contains("*.ts", "scripts/lib/identify.py", "identify.py missing *.ts fossil")
    h.require_contains("*.sh", "scripts/lib/identify.py", "identify.py missing *.sh fossil")
    h.require_contains("*.php", "scripts/lib/identify.py", "identify.py missing *.php fossil")
    h.require_contains("*.sql", "scripts/lib/identify.py", "identify.py missing *.sql fossil")
    h.require_contains("*.jq", "scripts/lib/identify.py", "identify.py missing *.jq fossil")
    h.require_contains("*.xsl", "scripts/lib/identify.py", "identify.py missing *.xsl fossil")
    h.require_contains("*.xslt", "scripts/lib/identify.py", "identify.py missing *.xslt fossil")
    h.require_contains("*.xml", "scripts/lib/identify.py", "identify.py missing *.xml fossil")
    h.require_contains("*.yaml", "scripts/lib/identify.py", "identify.py missing *.yaml fossil")
    h.require_contains("*.yml", "scripts/lib/identify.py", "identify.py missing *.yml fossil")
    h.require_contains("*.toml", "scripts/lib/identify.py", "identify.py missing *.toml fossil")
    h.require_contains("*.html", "scripts/lib/identify.py", "identify.py missing *.html fossil")
    h.require_contains("*.htm", "scripts/lib/identify.py", "identify.py missing *.htm fossil")
    h.require_contains("*.csv", "scripts/lib/identify.py", "identify.py missing *.csv fossil")
    h.require_contains("*.json", "scripts/lib/identify.py", "identify.py missing *.json fossil")
    h.require_contains("*.ini", "scripts/lib/identify.py", "identify.py missing *.ini fossil")
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
            ("hello.vhd", "emperor-excavate", "route hello.vhd → excavate"),
            ("ghdl -a HELLO.VHD", "emperor-excavate", "route ghdl → excavate"),
            ("hello.adb", "emperor-excavate", "route hello.adb → excavate"),
            ("gnatmake HELLO.ADB", "emperor-excavate", "route gnatmake → excavate"),
            ("hello.fs", "emperor-excavate", "route hello.fs → excavate"),
            ("pforth HELLO.FS", "emperor-excavate", "route pforth → excavate"),
            ("hello.lisp", "emperor-excavate", "route hello.lisp → excavate"),
            ("clisp HELLO.LISP", "emperor-excavate", "route clisp → excavate"),
            ("hello.pro", "emperor-excavate", "route hello.pro → excavate"),
            ("swipl HELLO.PRO", "emperor-excavate", "route swipl → excavate"),
            ("hello.tcl", "emperor-excavate", "route hello.tcl → excavate"),
            ("tclsh HELLO.TCL", "emperor-excavate", "route tclsh → excavate"),
            ("hello.erl", "emperor-excavate", "route hello.erl → excavate"),
            ("escript HELLO.ERL", "emperor-excavate", "route escript → excavate"),
            ("hello.rex", "emperor-excavate", "route hello.rex → excavate"),
            ("regina HELLO.REX", "emperor-excavate", "route regina → excavate"),
            ("hello.mod", "emperor-excavate", "route hello.mod → excavate"),
            ("gm2 HELLO.MOD", "emperor-excavate", "route gm2 → excavate"),
            ("hello.a68", "emperor-excavate", "route hello.a68 → excavate"),
            ("a68g HELLO.A68", "emperor-excavate", "route a68g → excavate"),
            ("hello.a60", "emperor-excavate", "route hello.a60 → excavate"),
            ("marst HELLO.A60", "emperor-excavate", "route marst → excavate"),
            ("hello.alw", "emperor-excavate", "route hello.alw → excavate"),
            ("awe HELLO.ALW", "emperor-excavate", "route awe → excavate"),
            ("hello.icn", "emperor-excavate", "route hello.icn → excavate"),
            ("icont HELLO.ICN", "emperor-excavate", "route icont → excavate"),
            ("hello.obn", "emperor-excavate", "route hello.obn → excavate"),
            ("voc HELLO.OBN", "emperor-excavate", "route voc → excavate"),
            ("hello.sno", "emperor-excavate", "route hello.sno → excavate"),
            ("snobol4 HELLO.SNO", "emperor-excavate", "route snobol4 → excavate"),
            ("hello.sim", "emperor-excavate", "route hello.sim → excavate"),
            ("cim HELLO.SIM", "emperor-excavate", "route cim → excavate"),
            ("hello.apl", "emperor-excavate", "route hello.apl → excavate"),
            ("apl HELLO.APL", "emperor-excavate", "route apl → excavate"),
            ("bcpl HELLO.B", "emperor-excavate", "route bcpl → excavate"),
            ("cintsys hello.b", "emperor-excavate", "route cintsys → excavate"),
            ("hello.pli", "emperor-excavate", "route hello.pli → excavate"),
            ("plic HELLO.PLI", "emperor-excavate", "route plic → excavate"),
            ("gst HELLO.ST", "emperor-excavate", "route gst → excavate"),
            ("smalltalk HELLO.ST", "emperor-excavate", "route smalltalk → excavate"),
            ("ghostscript HELLO.PS", "emperor-excavate", "route ghostscript → excavate"),
            ("postscript HELLO.PS", "emperor-excavate", "route postscript → excavate"),
            ("bwbasic HELLO.BAS", "emperor-excavate", "route bwbasic → excavate"),
            ("bywater HELLO.BAS", "emperor-excavate", "route bywater → excavate"),
            ("csi HELLO.SCM", "emperor-excavate", "route csi → excavate"),
            ("chicken HELLO.SCM", "emperor-excavate", "route chicken → excavate"),
            ("chicken-scheme HELLO.SCM", "emperor-excavate", "route chicken-scheme → excavate"),
            ("hello.scm", "emperor-excavate", "route hello.scm → excavate"),
            ("gawk HELLO.AWK", "emperor-excavate", "route gawk → excavate"),
            ("awk HELLO.AWK", "emperor-excavate", "route awk → excavate"),
            ("nawk HELLO.AWK", "emperor-excavate", "route nawk → excavate"),
            ("hello.awk", "emperor-excavate", "route hello.awk → excavate"),
            ("sed HELLO.SED", "emperor-excavate", "route sed → excavate"),
            ("gsed HELLO.SED", "emperor-excavate", "route gsed → excavate"),
            ("hello.sed", "emperor-excavate", "route hello.sed → excavate"),
            ("m4 HELLO.M4", "emperor-excavate", "route m4 → excavate"),
            ("gm4 HELLO.M4", "emperor-excavate", "route gm4 → excavate"),
            ("hello.m4", "emperor-excavate", "route hello.m4 → excavate"),
            ("ed HELLO.ED", "emperor-excavate", "route ed → excavate"),
            ("gnu-ed HELLO.ED", "emperor-excavate", "route gnu-ed → excavate"),
            ("hello.ed", "emperor-excavate", "route hello.ed → excavate"),
            ("gmake HELLO.MK", "emperor-excavate", "route gmake → excavate"),
            ("gnu-make HELLO.MK", "emperor-excavate", "route gnu-make → excavate"),
            ("hello.mk", "emperor-excavate", "route hello.mk → excavate"),
            ("makefile", "emperor-excavate", "route makefile → excavate"),
            ("dc HELLO.DC", "emperor-excavate", "route dc → excavate"),
            ("gnu-dc HELLO.DC", "emperor-excavate", "route gnu-dc → excavate"),
            ("hello.dc", "emperor-excavate", "route hello.dc → excavate"),
            ("lex HELLO.L", "emperor-excavate", "route lex → excavate"),
            ("flex HELLO.L", "emperor-excavate", "route flex → excavate"),
            ("gnu-flex HELLO.L", "emperor-excavate", "route gnu-flex → excavate"),
            ("hello.lex", "emperor-excavate", "route hello.lex → excavate"),
            ("yacc HELLO.Y", "emperor-excavate", "route yacc → excavate"),
            ("bison HELLO.Y", "emperor-excavate", "route bison → excavate"),
            ("gnu-bison HELLO.Y", "emperor-excavate", "route gnu-bison → excavate"),
            ("hello.y", "emperor-excavate", "route hello.y → excavate"),
            ("roff HELLO.ROFF", "emperor-excavate", "route roff → excavate"),
            ("nroff HELLO.ROFF", "emperor-excavate", "route nroff → excavate"),
            ("groff HELLO.ROFF", "emperor-excavate", "route groff → excavate"),
            ("gnu-groff HELLO.ROFF", "emperor-excavate", "route gnu-groff → excavate"),
            ("hello.roff", "emperor-excavate", "route hello.roff → excavate"),
            ("perl HELLO.PL", "emperor-excavate", "route perl → excavate"),
            ("perl5 HELLO.PL", "emperor-excavate", "route perl5 → excavate"),
            ("hello.pm", "emperor-excavate", "route hello.pm → excavate"),
            ("bc HELLO.BC", "emperor-excavate", "route bc → excavate"),
            ("gnu-bc HELLO.BC", "emperor-excavate", "route gnu-bc → excavate"),
            ("expect HELLO.EXP", "emperor-excavate", "route expect → excavate"),
            ("tcl-expect HELLO.EXP", "emperor-excavate", "route tcl-expect → excavate"),
            ("hello.exp", "emperor-excavate", "route hello.exp → excavate"),
            ("lua HELLO.LUA", "emperor-excavate", "route lua → excavate"),
            ("lua5.4 HELLO.LUA", "emperor-excavate", "route lua5.4 → excavate"),
            ("hello.lua", "emperor-excavate", "route hello.lua → excavate"),
            ("ruby HELLO.RB", "emperor-excavate", "route ruby → excavate"),
            ("ruby3.3 HELLO.RB", "emperor-excavate", "route ruby3.3 → excavate"),
            ("hello.rb", "emperor-excavate", "route hello.rb → excavate"),
            ("golang HELLO.go", "emperor-excavate", "route golang → excavate"),
            ("go1.24 HELLO.go", "emperor-excavate", "route go1.24 → excavate"),
            ("hello.go", "emperor-excavate", "route hello.go → excavate"),
            ("rust HELLO.rs", "emperor-excavate", "route rust → excavate"),
            ("rustc HELLO.rs", "emperor-excavate", "route rustc → excavate"),
            ("rust1.85 HELLO.rs", "emperor-excavate", "route rust1.85 → excavate"),
            ("hello.rs", "emperor-excavate", "route hello.rs → excavate"),
            ("gcc HELLO.c", "emperor-excavate", "route gcc → excavate"),
            ("gcc14 HELLO.c", "emperor-excavate", "route gcc14 → excavate"),
            ("c11 HELLO.c", "emperor-excavate", "route c11 → excavate"),
            ("hello.c", "emperor-excavate", "route hello.c → excavate"),
            ("nodejs HELLO.js", "emperor-excavate", "route nodejs → excavate"),
            ("node20 HELLO.js", "emperor-excavate", "route node20 → excavate"),
            ("javascript HELLO.js", "emperor-excavate", "route javascript → excavate"),
            ("hello.js", "emperor-excavate", "route hello.js → excavate"),
            ("python3 HELLO.py", "emperor-excavate", "route python3 → excavate"),
            ("python3.13 HELLO.py", "emperor-excavate", "route python3.13 → excavate"),
            ("cpython HELLO.py", "emperor-excavate", "route cpython → excavate"),
            ("hello.py", "emperor-excavate", "route hello.py → excavate"),
            ("typescript HELLO.ts", "emperor-excavate", "route typescript → excavate"),
            ("typescript5 HELLO.ts", "emperor-excavate", "route typescript5 → excavate"),
            ("tsc HELLO.ts", "emperor-excavate", "route tsc → excavate"),
            ("ts5 HELLO.ts", "emperor-excavate", "route ts5 → excavate"),
            ("hello.ts", "emperor-excavate", "route hello.ts → excavate"),
            ("bash HELLO.sh", "emperor-excavate", "route bash → excavate"),
            ("bash5 HELLO.sh", "emperor-excavate", "route bash5 → excavate"),
            ("bash5.2 HELLO.sh", "emperor-excavate", "route bash5.2 → excavate"),
            ("gnu-bash HELLO.sh", "emperor-excavate", "route gnu-bash → excavate"),
            ("hello.sh", "emperor-excavate", "route hello.sh → excavate"),
            ("php HELLO.php", "emperor-excavate", "route php → excavate"),
            ("php8 HELLO.php", "emperor-excavate", "route php8 → excavate"),
            ("php8.4 HELLO.php", "emperor-excavate", "route php8.4 → excavate"),
            ("php-cli HELLO.php", "emperor-excavate", "route php-cli → excavate"),
            ("hello.php", "emperor-excavate", "route hello.php → excavate"),
            ("sqlite HELLO.sql", "emperor-excavate", "route sqlite → excavate"),
            ("sqlite3 HELLO.sql", "emperor-excavate", "route sqlite3 → excavate"),
            ("sqlite3.46 HELLO.sql", "emperor-excavate", "route sqlite3.46 → excavate"),
            ("hello.sql", "emperor-excavate", "route hello.sql → excavate"),
            ("jq HELLO.jq", "emperor-excavate", "route jq → excavate"),
            ("jq1.7 HELLO.jq", "emperor-excavate", "route jq1.7 → excavate"),
            ("jqlang HELLO.jq", "emperor-excavate", "route jqlang → excavate"),
            ("hello.jq", "emperor-excavate", "route hello.jq → excavate"),
            ("xsltproc HELLO.xsl", "emperor-excavate", "route xsltproc → excavate"),
            ("libxslt HELLO.xsl", "emperor-excavate", "route libxslt → excavate"),
            ("xslt HELLO.xsl", "emperor-excavate", "route xslt → excavate"),
            ("hello.xsl", "emperor-excavate", "route hello.xsl → excavate"),
            ("hello.xslt", "emperor-excavate", "route hello.xslt → excavate"),
            ("xmllint HELLO.xml", "emperor-excavate", "route xmllint → excavate"),
            ("libxml2 HELLO.xml", "emperor-excavate", "route libxml2 → excavate"),
            ("xml HELLO.xml", "emperor-excavate", "route xml → excavate"),
            ("hello.xml", "emperor-excavate", "route hello.xml → excavate"),
            ("yq HELLO.yaml", "emperor-excavate", "route yq → excavate"),
            ("kislyuk-yq HELLO.yaml", "emperor-excavate", "route kislyuk-yq → excavate"),
            ("yq3.4 HELLO.yaml", "emperor-excavate", "route yq3.4 → excavate"),
            ("yaml HELLO.yaml", "emperor-excavate", "route yaml → excavate"),
            ("hello.yaml", "emperor-excavate", "route hello.yaml → excavate"),
            ("hello.yml", "emperor-excavate", "route hello.yml → excavate"),
            ("tomlq HELLO.toml", "emperor-excavate", "route tomlq → excavate"),
            ("kislyuk-tomlq HELLO.toml", "emperor-excavate", "route kislyuk-tomlq → excavate"),
            ("tomlq3.4 HELLO.toml", "emperor-excavate", "route tomlq3.4 → excavate"),
            ("toml HELLO.toml", "emperor-excavate", "route toml → excavate"),
            ("hello.toml", "emperor-excavate", "route hello.toml → excavate"),
            ("tidy HELLO.html", "emperor-excavate", "route tidy → excavate"),
            ("html-tidy HELLO.html", "emperor-excavate", "route html-tidy → excavate"),
            ("tidy5.8 HELLO.html", "emperor-excavate", "route tidy5.8 → excavate"),
            ("html HELLO.html", "emperor-excavate", "route html → excavate"),
            ("hello.html", "emperor-excavate", "route hello.html → excavate"),
            ("hello.htm", "emperor-excavate", "route hello.htm → excavate"),
            ("csv HELLO.csv", "emperor-excavate", "route csv → excavate"),
            ("pycsv HELLO.csv", "emperor-excavate", "route pycsv → excavate"),
            ("csv1.0 HELLO.csv", "emperor-excavate", "route csv1.0 → excavate"),
            ("hello.csv", "emperor-excavate", "route hello.csv → excavate"),
            ("pyjson HELLO.json", "emperor-excavate", "route pyjson → excavate"),
            ("json2.0 HELLO.json", "emperor-excavate", "route json2.0 → excavate"),
            ("hello.json", "emperor-excavate", "route hello.json → excavate"),
            ("ini HELLO.ini", "emperor-excavate", "route ini → excavate"),
            ("pyini HELLO.ini", "emperor-excavate", "route pyini → excavate"),
            ("configparser HELLO.ini", "emperor-excavate", "route configparser → excavate"),
            ("hello.ini", "emperor-excavate", "route hello.ini → excavate"),
            ("plist HELLO.plist", "emperor-excavate", "route plist → excavate"),
            ("pyplist HELLO.plist", "emperor-excavate", "route pyplist → excavate"),
            ("plistlib HELLO.plist", "emperor-excavate", "route plistlib → excavate"),
            ("hello.plist", "emperor-excavate", "route hello.plist → excavate"),
            ("eml HELLO.eml", "emperor-excavate", "route eml → excavate"),
            ("pyemail HELLO.eml", "emperor-excavate", "route pyemail → excavate"),
            ("email.parser HELLO.eml", "emperor-excavate", "route email.parser → excavate"),
            ("hello.eml", "emperor-excavate", "route hello.eml → excavate"),
            ("zip HELLO.zip", "emperor-excavate", "route zip → excavate"),
            ("pyzip HELLO.zip", "emperor-excavate", "route pyzip → excavate"),
            ("zipfile HELLO.zip", "emperor-excavate", "route zipfile → excavate"),
            ("hello.zip", "emperor-excavate", "route hello.zip → excavate"),
            ("tar HELLO.tar", "emperor-excavate", "route tar → excavate"),
            ("pytar HELLO.tar", "emperor-excavate", "route pytar → excavate"),
            ("tarfile HELLO.tar", "emperor-excavate", "route tarfile → excavate"),
            ("hello.tar", "emperor-excavate", "route hello.tar → excavate"),
            ("gzip HELLO.gz", "emperor-excavate", "route gzip → excavate"),
            ("pygzip HELLO.gz", "emperor-excavate", "route pygzip → excavate"),
            ("gzipfile HELLO.gz", "emperor-excavate", "route gzipfile → excavate"),
            ("hello.gz", "emperor-excavate", "route hello.gz → excavate"),
            ("targz HELLO.tar.gz", "emperor-excavate", "route targz → excavate"),
            ("tarball HELLO.tar.gz", "emperor-excavate", "route tarball → excavate"),
            ("pytargz HELLO.tar.gz", "emperor-excavate", "route pytargz → excavate"),
            ("hello.tar.gz", "emperor-excavate", "route hello.tar.gz → excavate"),
            ("hello.tgz", "emperor-excavate", "route hello.tgz → excavate"),
            ("hello.tar.bz2", "emperor-excavate", "route hello.tar.bz2 → excavate"),
            ("hello.tar.xz", "emperor-excavate", "route hello.tar.xz → excavate"),
            ("whl HELLO.whl", "emperor-excavate", "route whl → excavate"),
            ("pywhl HELLO.whl", "emperor-excavate", "route pywhl → excavate"),
            ("wheel HELLO.whl", "emperor-excavate", "route wheel → excavate"),
            ("hello.whl", "emperor-excavate", "route hello.whl → excavate"),
            ("jar HELLO.jar", "emperor-excavate", "route jar → excavate"),
            ("pyjar HELLO.jar", "emperor-excavate", "route pyjar → excavate"),
            ("java-archive HELLO.jar", "emperor-excavate", "route java-archive → excavate"),
            ("hello.jar", "emperor-excavate", "route hello.jar → excavate"),
            ("war HELLO.war", "emperor-excavate", "route war → excavate"),
            ("pywar HELLO.war", "emperor-excavate", "route pywar → excavate"),
            ("web-archive HELLO.war", "emperor-excavate", "route web-archive → excavate"),
            ("hello.war", "emperor-excavate", "route hello.war → excavate"),
            ("apk HELLO.apk", "emperor-excavate", "route apk → excavate"),
            ("pyapk HELLO.apk", "emperor-excavate", "route pyapk → excavate"),
            ("android-package HELLO.apk", "emperor-excavate", "route android-package → excavate"),
            ("hello.apk", "emperor-excavate", "route hello.apk → excavate"),
            ("docx HELLO.docx", "emperor-excavate", "route docx → excavate"),
            ("pydocx HELLO.docx", "emperor-excavate", "route pydocx → excavate"),
            ("ooxml-word HELLO.docx", "emperor-excavate", "route ooxml-word → excavate"),
            ("hello.docx", "emperor-excavate", "route hello.docx → excavate"),
            ("xlsx HELLO.xlsx", "emperor-excavate", "route xlsx → excavate"),
            ("pyxlsx HELLO.xlsx", "emperor-excavate", "route pyxlsx → excavate"),
            ("ooxml-excel HELLO.xlsx", "emperor-excavate", "route ooxml-excel → excavate"),
            ("hello.xlsx", "emperor-excavate", "route hello.xlsx → excavate"),
            ("tsv HELLO.tsv", "emperor-excavate", "route tsv → excavate"),
            ("pytsv HELLO.tsv", "emperor-excavate", "route pytsv → excavate"),
            ("tab-separated HELLO.tsv", "emperor-excavate", "route tab-separated → excavate"),
            ("hello.tsv", "emperor-excavate", "route hello.tsv → excavate"),
            ("jsonl HELLO.jsonl", "emperor-excavate", "route jsonl → excavate"),
            ("pyjsonl HELLO.jsonl", "emperor-excavate", "route pyjsonl → excavate"),
            ("ndjson HELLO.jsonl", "emperor-excavate", "route ndjson → excavate"),
            ("hello.jsonl", "emperor-excavate", "route hello.jsonl → excavate"),
            ("pptx HELLO.pptx", "emperor-excavate", "route pptx → excavate"),
            ("pypptx HELLO.pptx", "emperor-excavate", "route pypptx → excavate"),
            ("ooxml-pptx HELLO.pptx", "emperor-excavate", "route ooxml-pptx → excavate"),
            ("hello.pptx", "emperor-excavate", "route hello.pptx → excavate"),
            ("pdf HELLO.pdf", "emperor-excavate", "route pdf → excavate"),
            ("pdftotext HELLO.pdf", "emperor-excavate", "route pdftotext → excavate"),
            ("poppler HELLO.pdf", "emperor-excavate", "route poppler → excavate"),
            ("hello.pdf", "emperor-excavate", "route hello.pdf → excavate"),
            ("png HELLO.png", "emperor-excavate", "route png → excavate"),
            ("pillow HELLO.png", "emperor-excavate", "route pillow → excavate"),
            ("pil HELLO.png", "emperor-excavate", "route pil → excavate"),
            ("hello.png", "emperor-excavate", "route hello.png → excavate"),
            ("wav HELLO.wav", "emperor-excavate", "route wav → excavate"),
            ("ffmpeg HELLO.wav", "emperor-excavate", "route ffmpeg → excavate"),
            ("ffprobe HELLO.wav", "emperor-excavate", "route ffprobe → excavate"),
            ("hello.wav", "emperor-excavate", "route hello.wav → excavate"),
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
        (
            "lost-vhd identify finds *.vhd",
            "lost-vhd",
            "HELLO.VHD",
            r"[0-9]+ \*\.vhd",
            ["references/archaeology-vhdl-manual.md"],
        ),
        (
            "lost-ada identify finds *.adb",
            "lost-ada",
            "HELLO.ADB",
            r"[0-9]+ \*\.adb",
            ["references/archaeology-ada-manual.md"],
        ),
        (
            "lost-fs identify finds *.fs",
            "lost-fs",
            "HELLO.FS",
            r"[0-9]+ \*\.fs",
            ["references/archaeology-forth-manual.md"],
        ),
        (
            "lost-lisp identify finds *.lisp",
            "lost-lisp",
            "HELLO.LISP",
            r"[0-9]+ \*\.lisp",
            ["references/archaeology-lisp-manual.md"],
        ),
        (
            "lost-prolog identify finds *.pro",
            "lost-prolog",
            "HELLO.PRO",
            r"[0-9]+ \*\.pro",
            ["references/archaeology-prolog-manual.md"],
        ),
        (
            "lost-tcl identify finds *.tcl",
            "lost-tcl",
            "HELLO.TCL",
            r"[0-9]+ \*\.tcl",
            ["references/archaeology-tcl-manual.md"],
        ),
        (
            "lost-erl identify finds *.erl",
            "lost-erl",
            "HELLO.ERL",
            r"[0-9]+ \*\.erl",
            ["references/archaeology-erlang-manual.md"],
        ),
        (
            "lost-rex identify finds *.rex",
            "lost-rex",
            "HELLO.REX",
            r"[0-9]+ \*\.rex",
            ["references/archaeology-rexx-manual.md"],
        ),
        (
            "lost-mod identify finds *.mod",
            "lost-mod",
            "HELLO.MOD",
            r"[0-9]+ \*\.mod",
            ["references/archaeology-modula2-manual.md"],
        ),
        (
            "lost-a68 identify finds *.a68",
            "lost-a68",
            "HELLO.A68",
            r"[0-9]+ \*\.a68",
            ["references/archaeology-algol68-manual.md"],
        ),
        (
            "lost-a60 identify finds *.a60",
            "lost-a60",
            "HELLO.A60",
            r"[0-9]+ \*\.a60",
            ["references/archaeology-algol60-manual.md"],
        ),
        (
            "lost-alw identify finds *.alw",
            "lost-alw",
            "HELLO.ALW",
            r"[0-9]+ \*\.alw",
            ["references/archaeology-algolw-manual.md"],
        ),
        (
            "lost-icn identify finds *.icn",
            "lost-icn",
            "HELLO.ICN",
            r"[0-9]+ \*\.icn",
            ["references/archaeology-icon-manual.md"],
        ),
        (
            "lost-obn identify finds *.obn",
            "lost-obn",
            "HELLO.OBN",
            r"[0-9]+ \*\.obn",
            ["references/archaeology-oberon-manual.md"],
        ),
        (
            "lost-sno identify finds *.sno",
            "lost-sno",
            "HELLO.SNO",
            r"[0-9]+ \*\.sno",
            ["references/archaeology-snobol-manual.md"],
        ),
        (
            "lost-cim identify finds *.sim",
            "lost-cim",
            "HELLO.SIM",
            r"[0-9]+ \*\.sim",
            ["references/archaeology-simula-manual.md"],
        ),
        (
            "lost-apl identify finds *.apl",
            "lost-apl",
            "HELLO.APL",
            r"[0-9]+ \*\.apl",
            ["references/archaeology-apl-manual.md"],
        ),
        (
            "lost-bcpl identify finds *.b",
            "lost-bcpl",
            "HELLO.B",
            r"[0-9]+ \*\.b",
            ["references/archaeology-bcpl-manual.md"],
        ),
        (
            "lost-pli identify finds *.pli",
            "lost-pli",
            "HELLO.PLI",
            r"[0-9]+ \*\.pli",
            ["references/archaeology-pli-manual.md"],
        ),
        (
            "lost-st identify finds *.st",
            "lost-st",
            "HELLO.ST",
            r"[0-9]+ \*\.st",
            ["references/archaeology-smalltalk-manual.md"],
        ),
        (
            "lost-ps identify finds *.ps",
            "lost-ps",
            "HELLO.PS",
            r"[0-9]+ \*\.ps",
            ["references/archaeology-postscript-manual.md"],
        ),
        (
            "lost-bas identify finds *.bas",
            "lost-bas",
            "HELLO.BAS",
            r"[0-9]+ \*\.bas",
            ["references/archaeology-basic-manual.md"],
        ),
        (
            "lost-scm identify finds *.scm",
            "lost-scm",
            "HELLO.SCM",
            r"[0-9]+ \*\.scm",
            ["references/archaeology-scheme-manual.md"],
        ),
        (
            "lost-awk identify finds *.awk",
            "lost-awk",
            "HELLO.AWK",
            r"[0-9]+ \*\.awk",
            ["references/archaeology-awk-manual.md"],
        ),
        (
            "lost-sed identify finds *.sed",
            "lost-sed",
            "HELLO.SED",
            r"[0-9]+ \*\.sed",
            ["references/archaeology-sed-manual.md"],
        ),
        (
            "lost-m4 identify finds *.m4",
            "lost-m4",
            "HELLO.M4",
            r"[0-9]+ \*\.m4",
            ["references/archaeology-m4-manual.md"],
        ),
        (
            "lost-ed identify finds *.ed",
            "lost-ed",
            "HELLO.ED",
            r"[0-9]+ \*\.ed",
            ["references/archaeology-ed-manual.md"],
        ),
        (
            "lost-make identify finds Makefile",
            "lost-make",
            "Makefile",
            r"[0-9]+ Makefile",
            ["references/archaeology-make-manual.md"],
        ),
        (
            "lost-dc identify finds *.dc",
            "lost-dc",
            "HELLO.DC",
            r"[0-9]+ \*\.dc",
            ["references/archaeology-dc-manual.md"],
        ),
        (
            "lost-lex identify finds *.l",
            "lost-lex",
            "HELLO.L",
            r"[0-9]+ \*\.l",
            ["references/archaeology-lex-manual.md"],
        ),
        (
            "lost-yacc identify finds *.y",
            "lost-yacc",
            "HELLO.Y",
            r"[0-9]+ \*\.y",
            ["references/archaeology-yacc-manual.md"],
        ),
        (
            "lost-roff identify finds *.roff",
            "lost-roff",
            "HELLO.ROFF",
            r"[0-9]+ \*\.roff",
            ["references/archaeology-roff-manual.md"],
        ),
        (
            "lost-pl identify finds *.pl",
            "lost-pl",
            "HELLO.PL",
            r"[0-9]+ \*\.pl",
            ["references/archaeology-perl-manual.md"],
        ),
        (
            "lost-bc identify finds *.bc",
            "lost-bc",
            "HELLO.BC",
            r"[0-9]+ \*\.bc",
            ["references/archaeology-bc-manual.md"],
        ),
        (
            "lost-expect identify finds *.exp",
            "lost-expect",
            "HELLO.EXP",
            r"[0-9]+ \*\.exp",
            ["references/archaeology-expect-manual.md"],
        ),
        (
            "lost-lua identify finds *.lua",
            "lost-lua",
            "HELLO.LUA",
            r"[0-9]+ \*\.lua",
            ["references/archaeology-lua-manual.md"],
        ),
        (
            "lost-ruby identify finds *.rb",
            "lost-ruby",
            "HELLO.RB",
            r"[0-9]+ \*\.rb",
            ["references/archaeology-ruby-manual.md"],
        ),
        (
            "lost-go identify finds *.go",
            "lost-go",
            "HELLO.go",
            r"[0-9]+ \*\.go",
            ["references/archaeology-go-manual.md"],
        ),
        (
            "lost-rust identify finds *.rs",
            "lost-rust",
            "HELLO.rs",
            r"[0-9]+ \*\.rs",
            ["references/archaeology-rust-manual.md"],
        ),
        (
            "lost-c identify finds *.c",
            "lost-c",
            "HELLO.c",
            r"[0-9]+ \*\.c",
            ["references/archaeology-c-manual.md"],
        ),
        (
            "lost-js identify finds *.js",
            "lost-js",
            "HELLO.js",
            r"[0-9]+ \*\.js",
            ["references/archaeology-js-manual.md"],
        ),
        (
            "lost-py identify finds *.py",
            "lost-py",
            "HELLO.py",
            r"[0-9]+ \*\.py",
            ["references/archaeology-python-manual.md"],
        ),
        (
            "lost-ts identify finds *.ts",
            "lost-ts",
            "HELLO.ts",
            r"[0-9]+ \*\.ts",
            ["references/archaeology-typescript-manual.md"],
        ),
        (
            "lost-sh identify finds *.sh",
            "lost-sh",
            "HELLO.sh",
            r"[0-9]+ \*\.sh",
            ["references/archaeology-bash-manual.md"],
        ),
        (
            "lost-php identify finds *.php",
            "lost-php",
            "HELLO.php",
            r"[0-9]+ \*\.php",
            ["references/archaeology-php-manual.md"],
        ),
        (
            "lost-sql identify finds *.sql",
            "lost-sql",
            "HELLO.sql",
            r"[0-9]+ \*\.sql",
            ["references/archaeology-sql-manual.md"],
        ),
        (
            "lost-jq identify finds *.jq",
            "lost-jq",
            "HELLO.jq",
            r"[0-9]+ \*\.jq",
            ["references/archaeology-jq-manual.md"],
        ),
        (
            "lost-xsl identify finds *.xsl",
            "lost-xsl",
            "HELLO.xsl",
            r"[0-9]+ \*\.xsl",
            ["references/archaeology-xslt-manual.md"],
        ),
        (
            "lost-xml identify finds *.xml",
            "lost-xml",
            "HELLO.xml",
            r"[0-9]+ \*\.xml",
            ["references/archaeology-xml-manual.md"],
        ),
        (
            "lost-yaml identify finds *.yaml",
            "lost-yaml",
            "HELLO.yaml",
            r"[0-9]+ \*\.yaml",
            ["references/archaeology-yaml-manual.md"],
        ),
        (
            "lost-toml identify finds *.toml",
            "lost-toml",
            "HELLO.toml",
            r"[0-9]+ \*\.toml",
            ["references/archaeology-toml-manual.md"],
        ),
        (
            "lost-html identify finds *.html",
            "lost-html",
            "HELLO.html",
            r"[0-9]+ \*\.html",
            ["references/archaeology-html-manual.md"],
        ),
        (
            "lost-csv identify finds *.csv",
            "lost-csv",
            "HELLO.csv",
            r"[0-9]+ \*\.csv",
            ["references/archaeology-csv-manual.md"],
        ),
        (
            "lost-json identify finds *.json",
            "lost-json",
            "HELLO.json",
            r"[0-9]+ \*\.json",
            ["references/archaeology-json-manual.md"],
        ),
        (
            "lost-ini identify finds *.ini",
            "lost-ini",
            "HELLO.ini",
            r"[0-9]+ \*\.ini",
            ["references/archaeology-ini-manual.md"],
        ),
        (
            "lost-plist identify finds *.plist",
            "lost-plist",
            "HELLO.plist",
            r"[0-9]+ \*\.plist",
            ["references/archaeology-plist-manual.md"],
        ),
        (
            "lost-eml identify finds *.eml",
            "lost-eml",
            "HELLO.eml",
            r"[0-9]+ \*\.eml",
            ["references/archaeology-eml-manual.md"],
        ),
        (
            "lost-zip identify finds *.zip",
            "lost-zip",
            "HELLO.zip",
            r"[0-9]+ \*\.zip",
            ["references/archaeology-zip-manual.md"],
        ),
        (
            "lost-tar identify finds *.tar",
            "lost-tar",
            "HELLO.tar",
            r"[0-9]+ \*\.tar",
            ["references/archaeology-tar-manual.md"],
        ),
        (
            "lost-gz identify finds *.gz",
            "lost-gz",
            "HELLO.gz",
            r"[0-9]+ \*\.gz",
            ["references/archaeology-gzip-manual.md"],
        ),
        (
            "lost-targz identify finds *.tar.gz",
            "lost-targz",
            "HELLO.tar.gz",
            r"[0-9]+ \*\.tar\.gz",
            ["references/archaeology-targz-manual.md"],
        ),
        (
            "lost-whl identify finds *.whl",
            "lost-whl",
            "HELLO.whl",
            r"[0-9]+ \*\.whl",
            ["references/archaeology-whl-manual.md"],
        ),
        (
            "lost-jar identify finds *.jar",
            "lost-jar",
            "HELLO.jar",
            r"[0-9]+ \*\.jar",
            ["references/archaeology-jar-manual.md"],
        ),
        (
            "lost-war identify finds *.war",
            "lost-war",
            "HELLO.war",
            r"[0-9]+ \*\.war",
            ["references/archaeology-war-manual.md"],
        ),
        (
            "lost-apk identify finds *.apk",
            "lost-apk",
            "HELLO.apk",
            r"[0-9]+ \*\.apk",
            ["references/archaeology-apk-manual.md"],
        ),
        (
            "lost-docx identify finds *.docx",
            "lost-docx",
            "HELLO.docx",
            r"[0-9]+ \*\.docx",
            ["references/archaeology-docx-manual.md"],
        ),
        (
            "lost-xlsx identify finds *.xlsx",
            "lost-xlsx",
            "HELLO.xlsx",
            r"[0-9]+ \*\.xlsx",
            ["references/archaeology-xlsx-manual.md"],
        ),
        (
            "lost-tsv identify finds *.tsv",
            "lost-tsv",
            "HELLO.tsv",
            r"[0-9]+ \*\.tsv",
            ["references/archaeology-tsv-manual.md"],
        ),
        (
            "lost-jsonl identify finds *.jsonl",
            "lost-jsonl",
            "HELLO.jsonl",
            r"[0-9]+ \*\.jsonl",
            ["references/archaeology-jsonl-manual.md"],
        ),
        (
            "lost-pptx identify finds *.pptx",
            "lost-pptx",
            "HELLO.pptx",
            r"[0-9]+ \*\.pptx",
            ["references/archaeology-pptx-manual.md"],
        ),
        (
            "lost-pdf identify finds *.pdf",
            "lost-pdf",
            "HELLO.pdf",
            r"[0-9]+ \*\.pdf",
            ["references/archaeology-pdf-manual.md"],
        ),
        (
            "lost-png identify finds *.png",
            "lost-png",
            "HELLO.png",
            r"[0-9]+ \*\.png",
            ["references/archaeology-png-manual.md"],
        ),
        (
            "lost-wav identify finds *.wav",
            "lost-wav",
            "HELLO.wav",
            r"[0-9]+ \*\.wav",
            ["references/archaeology-wav-manual.md"],
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
    h.require_contains(".vhd", "evals/triggers.json", "triggers missing .vhd excavate pattern")
    h.require_contains("vhdl", "evals/triggers.json", "triggers missing vhdl excavate pattern")
    h.require_contains("ghdl", "evals/triggers.json", "triggers missing ghdl excavate pattern")
    h.require_contains(".adb", "evals/triggers.json", "triggers missing .adb excavate pattern")
    h.require_contains("ada", "evals/triggers.json", "triggers missing ada excavate pattern")
    h.require_contains("gnat", "evals/triggers.json", "triggers missing gnat excavate pattern")
    h.require_contains("gnatmake", "evals/triggers.json", "triggers missing gnatmake excavate pattern")
    h.require_contains(".fs", "evals/triggers.json", "triggers missing .fs excavate pattern")
    h.require_contains("pforth", "evals/triggers.json", "triggers missing pforth excavate pattern")
    h.require_contains("gforth", "evals/triggers.json", "triggers missing gforth excavate pattern")
    h.require_contains(".fth", "evals/triggers.json", "triggers missing .fth excavate pattern")
    h.require_contains(".lisp", "evals/triggers.json", "triggers missing .lisp excavate pattern")
    h.require_contains("clisp", "evals/triggers.json", "triggers missing clisp excavate pattern")
    h.require_contains("sbcl", "evals/triggers.json", "triggers missing sbcl excavate pattern")
    h.require_contains(".pro", "evals/triggers.json", "triggers missing .pro excavate pattern")
    h.require_contains("swipl", "evals/triggers.json", "triggers missing swipl excavate pattern")
    h.require_contains("gprolog", "evals/triggers.json", "triggers missing gprolog excavate pattern")
    h.require_contains(".tcl", "evals/triggers.json", "triggers missing .tcl excavate pattern")
    h.require_contains("tclsh", "evals/triggers.json", "triggers missing tclsh excavate pattern")
    h.require_contains(".erl", "evals/triggers.json", "triggers missing .erl excavate pattern")
    h.require_contains("escript", "evals/triggers.json", "triggers missing escript excavate pattern")
    h.require_contains("erlc", "evals/triggers.json", "triggers missing erlc excavate pattern")
    h.require_contains(".rex", "evals/triggers.json", "triggers missing .rex excavate pattern")
    h.require_contains("regina", "evals/triggers.json", "triggers missing regina excavate pattern")
    h.require_contains("rexx", "evals/triggers.json", "triggers missing rexx excavate pattern")
    h.require_contains(".mod", "evals/triggers.json", "triggers missing .mod excavate pattern")
    h.require_contains("gm2", "evals/triggers.json", "triggers missing gm2 excavate pattern")
    h.require_contains("modula", "evals/triggers.json", "triggers missing modula excavate pattern")
    h.require_contains(".a68", "evals/triggers.json", "triggers missing .a68 excavate pattern")
    h.require_contains("a68g", "evals/triggers.json", "triggers missing a68g excavate pattern")
    h.require_contains("algol", "evals/triggers.json", "triggers missing algol excavate pattern")
    h.require_contains(".a60", "evals/triggers.json", "triggers missing .a60 excavate pattern")
    h.require_contains("marst", "evals/triggers.json", "triggers missing marst excavate pattern")
    h.require_contains("algol60", "evals/triggers.json", "triggers missing algol60 excavate pattern")
    h.require_contains(".alw", "evals/triggers.json", "triggers missing .alw excavate pattern")
    h.require_contains("awe", "evals/triggers.json", "triggers missing awe excavate pattern")
    h.require_contains("algolw", "evals/triggers.json", "triggers missing algolw excavate pattern")
    h.require_contains(".icn", "evals/triggers.json", "triggers missing .icn excavate pattern")
    h.require_contains("icont", "evals/triggers.json", "triggers missing icont excavate pattern")
    h.require_contains("iconx", "evals/triggers.json", "triggers missing iconx excavate pattern")
    h.require_contains(".obn", "evals/triggers.json", "triggers missing .obn excavate pattern")
    h.require_contains("voc", "evals/triggers.json", "triggers missing voc excavate pattern")
    h.require_contains("oberon", "evals/triggers.json", "triggers missing oberon excavate pattern")
    h.require_contains(".sno", "evals/triggers.json", "triggers missing .sno excavate pattern")
    h.require_contains("snobol4", "evals/triggers.json", "triggers missing snobol4 excavate pattern")
    h.require_contains("snobol", "evals/triggers.json", "triggers missing snobol excavate pattern")
    h.require_contains(".sim", "evals/triggers.json", "triggers missing .sim excavate pattern")
    h.require_contains("cim", "evals/triggers.json", "triggers missing cim excavate pattern")
    h.require_contains("simula", "evals/triggers.json", "triggers missing simula excavate pattern")
    h.require_contains(".apl", "evals/triggers.json", "triggers missing .apl excavate pattern")
    h.require_contains("apl", "evals/triggers.json", "triggers missing apl excavate pattern")
    h.require_contains("gnu-apl", "evals/triggers.json", "triggers missing gnu-apl excavate pattern")
    h.require_contains(".bcpl", "evals/triggers.json", "triggers missing .bcpl excavate pattern")
    h.require_contains("bcpl", "evals/triggers.json", "triggers missing bcpl excavate pattern")
    h.require_contains("cintsys", "evals/triggers.json", "triggers missing cintsys excavate pattern")
    h.require_contains("cintcode", "evals/triggers.json", "triggers missing cintcode excavate pattern")
    h.require_contains(".pli", "evals/triggers.json", "triggers missing .pli excavate pattern")
    h.require_contains(".pl1", "evals/triggers.json", "triggers missing .pl1 excavate pattern")
    h.require_contains("plic", "evals/triggers.json", "triggers missing plic excavate pattern")
    h.require_contains("pli", "evals/triggers.json", "triggers missing pli excavate pattern")
    h.require_contains("pl1", "evals/triggers.json", "triggers missing pl1 excavate pattern")
    h.require_contains("iron-spring", "evals/triggers.json", "triggers missing iron-spring excavate pattern")
    h.require_contains("gst", "evals/triggers.json", "triggers missing gst excavate pattern")
    h.require_contains("smalltalk", "evals/triggers.json", "triggers missing smalltalk excavate pattern")
    h.require_contains("gnu-smalltalk", "evals/triggers.json", "triggers missing gnu-smalltalk excavate pattern")
    h.require_contains("ghostscript", "evals/triggers.json", "triggers missing ghostscript excavate pattern")
    h.require_contains("postscript", "evals/triggers.json", "triggers missing postscript excavate pattern")
    h.require_contains("bwbasic", "evals/triggers.json", "triggers missing bwbasic excavate pattern")
    h.require_contains("bywater", "evals/triggers.json", "triggers missing bywater excavate pattern")
    h.require_contains(".bas", "evals/triggers.json", "triggers missing .bas excavate pattern")
    h.require_contains("csi", "evals/triggers.json", "triggers missing csi excavate pattern")
    h.require_contains("chicken", "evals/triggers.json", "triggers missing chicken excavate pattern")
    h.require_contains("chicken-scheme", "evals/triggers.json", "triggers missing chicken-scheme excavate pattern")
    h.require_contains(".scm", "evals/triggers.json", "triggers missing .scm excavate pattern")
    h.require_contains("gawk", "evals/triggers.json", "triggers missing gawk excavate pattern")
    h.require_contains("awk", "evals/triggers.json", "triggers missing awk excavate pattern")
    h.require_contains("nawk", "evals/triggers.json", "triggers missing nawk excavate pattern")
    h.require_contains(".awk", "evals/triggers.json", "triggers missing .awk excavate pattern")
    h.require_contains("sed", "evals/triggers.json", "triggers missing sed excavate pattern")
    h.require_contains("gsed", "evals/triggers.json", "triggers missing gsed excavate pattern")
    h.require_contains(".sed", "evals/triggers.json", "triggers missing .sed excavate pattern")
    h.require_contains("m4", "evals/triggers.json", "triggers missing m4 excavate pattern")
    h.require_contains("gm4", "evals/triggers.json", "triggers missing gm4 excavate pattern")
    h.require_contains(".m4", "evals/triggers.json", "triggers missing .m4 excavate pattern")
    h.require_contains("ed", "evals/triggers.json", "triggers missing ed excavate pattern")
    h.require_contains("gnu-ed", "evals/triggers.json", "triggers missing gnu-ed excavate pattern")
    h.require_contains(".ed", "evals/triggers.json", "triggers missing .ed excavate pattern")
    h.require_contains("gmake", "evals/triggers.json", "triggers missing gmake excavate pattern")
    h.require_contains("gnu-make", "evals/triggers.json", "triggers missing gnu-make excavate pattern")
    h.require_contains(".mk", "evals/triggers.json", "triggers missing .mk excavate pattern")
    h.require_contains(".mak", "evals/triggers.json", "triggers missing .mak excavate pattern")
    h.require_contains("makefile", "evals/triggers.json", "triggers missing makefile excavate pattern")
    h.require_contains("dc", "evals/triggers.json", "triggers missing dc excavate pattern")
    h.require_contains("gnu-dc", "evals/triggers.json", "triggers missing gnu-dc excavate pattern")
    h.require_contains(".dc", "evals/triggers.json", "triggers missing .dc excavate pattern")
    h.require_contains("lex", "evals/triggers.json", "triggers missing lex excavate pattern")
    h.require_contains("flex", "evals/triggers.json", "triggers missing flex excavate pattern")
    h.require_contains("gnu-flex", "evals/triggers.json", "triggers missing gnu-flex excavate pattern")
    h.require_contains(".lex", "evals/triggers.json", "triggers missing .lex excavate pattern")
    h.require_contains("yacc", "evals/triggers.json", "triggers missing yacc excavate pattern")
    h.require_contains("bison", "evals/triggers.json", "triggers missing bison excavate pattern")
    h.require_contains("gnu-bison", "evals/triggers.json", "triggers missing gnu-bison excavate pattern")
    h.require_contains(".y", "evals/triggers.json", "triggers missing .y excavate pattern")
    h.require_contains("roff", "evals/triggers.json", "triggers missing roff excavate pattern")
    h.require_contains("nroff", "evals/triggers.json", "triggers missing nroff excavate pattern")
    h.require_contains("groff", "evals/triggers.json", "triggers missing groff excavate pattern")
    h.require_contains("gnu-groff", "evals/triggers.json", "triggers missing gnu-groff excavate pattern")
    h.require_contains(".roff", "evals/triggers.json", "triggers missing .roff excavate pattern")
    h.require_contains("perl", "evals/triggers.json", "triggers missing perl excavate pattern")
    h.require_contains("perl5", "evals/triggers.json", "triggers missing perl5 excavate pattern")
    h.require_contains(".pm", "evals/triggers.json", "triggers missing .pm excavate pattern")
    h.require_contains("bc", "evals/triggers.json", "triggers missing bc excavate pattern")
    h.require_contains("gnu-bc", "evals/triggers.json", "triggers missing gnu-bc excavate pattern")
    h.require_contains("expect", "evals/triggers.json", "triggers missing expect excavate pattern")
    h.require_contains("tcl-expect", "evals/triggers.json", "triggers missing tcl-expect excavate pattern")
    h.require_contains(".exp", "evals/triggers.json", "triggers missing .exp excavate pattern")
    h.require_contains("lua", "evals/triggers.json", "triggers missing lua excavate pattern")
    h.require_contains("lua5.4", "evals/triggers.json", "triggers missing lua5.4 excavate pattern")
    h.require_contains(".lua", "evals/triggers.json", "triggers missing .lua excavate pattern")
    h.require_contains("ruby", "evals/triggers.json", "triggers missing ruby excavate pattern")
    h.require_contains("ruby3.3", "evals/triggers.json", "triggers missing ruby3.3 excavate pattern")
    h.require_contains(".rb", "evals/triggers.json", "triggers missing .rb excavate pattern")
    h.require_contains("golang", "evals/triggers.json", "triggers missing golang excavate pattern")
    h.require_contains("go1.24", "evals/triggers.json", "triggers missing go1.24 excavate pattern")
    h.require_contains(".go", "evals/triggers.json", "triggers missing .go excavate pattern")
    h.require_contains("rust", "evals/triggers.json", "triggers missing rust excavate pattern")
    h.require_contains("rustc", "evals/triggers.json", "triggers missing rustc excavate pattern")
    h.require_contains("rust1.85", "evals/triggers.json", "triggers missing rust1.85 excavate pattern")
    h.require_contains(".rs", "evals/triggers.json", "triggers missing .rs excavate pattern")
    h.require_contains("gcc", "evals/triggers.json", "triggers missing gcc excavate pattern")
    h.require_contains("gcc14", "evals/triggers.json", "triggers missing gcc14 excavate pattern")
    h.require_contains("c11", "evals/triggers.json", "triggers missing c11 excavate pattern")
    h.require_contains(".c", "evals/triggers.json", "triggers missing .c excavate pattern")
    h.require_contains("nodejs", "evals/triggers.json", "triggers missing nodejs excavate pattern")
    h.require_contains("node20", "evals/triggers.json", "triggers missing node20 excavate pattern")
    h.require_contains("javascript", "evals/triggers.json", "triggers missing javascript excavate pattern")
    h.require_contains("cpython", "evals/triggers.json", "triggers missing cpython excavate pattern")
    h.require_contains("python3.13", "evals/triggers.json", "triggers missing python3.13 excavate pattern")
    h.require_contains("python3", "evals/triggers.json", "triggers missing python3 excavate pattern")
    h.require_contains(".py", "evals/triggers.json", "triggers missing .py excavate pattern")
    h.require_contains("typescript", "evals/triggers.json", "triggers missing typescript excavate pattern")
    h.require_contains("typescript5", "evals/triggers.json", "triggers missing typescript5 excavate pattern")
    h.require_contains("tsc", "evals/triggers.json", "triggers missing tsc excavate pattern")
    h.require_contains("ts5", "evals/triggers.json", "triggers missing ts5 excavate pattern")
    h.require_contains(".ts", "evals/triggers.json", "triggers missing .ts excavate pattern")
    h.require_contains("bash", "evals/triggers.json", "triggers missing bash excavate pattern")
    h.require_contains("bash5", "evals/triggers.json", "triggers missing bash5 excavate pattern")
    h.require_contains("bash5.2", "evals/triggers.json", "triggers missing bash5.2 excavate pattern")
    h.require_contains("gnu-bash", "evals/triggers.json", "triggers missing gnu-bash excavate pattern")
    h.require_contains(".sh", "evals/triggers.json", "triggers missing .sh excavate pattern")
    h.require_contains("php", "evals/triggers.json", "triggers missing php excavate pattern")
    h.require_contains("php8", "evals/triggers.json", "triggers missing php8 excavate pattern")
    h.require_contains("php8.4", "evals/triggers.json", "triggers missing php8.4 excavate pattern")
    h.require_contains("php-cli", "evals/triggers.json", "triggers missing php-cli excavate pattern")
    h.require_contains(".php", "evals/triggers.json", "triggers missing .php excavate pattern")
    h.require_contains("sqlite", "evals/triggers.json", "triggers missing sqlite excavate pattern")
    h.require_contains("sqlite3", "evals/triggers.json", "triggers missing sqlite3 excavate pattern")
    h.require_contains("sqlite3.46", "evals/triggers.json", "triggers missing sqlite3.46 excavate pattern")
    h.require_contains(".sql", "evals/triggers.json", "triggers missing .sql excavate pattern")
    h.require_contains("jq", "evals/triggers.json", "triggers missing jq excavate pattern")
    h.require_contains("jq1.7", "evals/triggers.json", "triggers missing jq1.7 excavate pattern")
    h.require_contains("jqlang", "evals/triggers.json", "triggers missing jqlang excavate pattern")
    h.require_contains(".jq", "evals/triggers.json", "triggers missing .jq excavate pattern")
    h.require_contains("xsltproc", "evals/triggers.json", "triggers missing xsltproc excavate pattern")
    h.require_contains("libxslt", "evals/triggers.json", "triggers missing libxslt excavate pattern")
    h.require_contains("xslt", "evals/triggers.json", "triggers missing xslt excavate pattern")
    h.require_contains(".xsl", "evals/triggers.json", "triggers missing .xsl excavate pattern")
    h.require_contains(".xslt", "evals/triggers.json", "triggers missing .xslt excavate pattern")
    h.require_contains("xmllint", "evals/triggers.json", "triggers missing xmllint excavate pattern")
    h.require_contains("libxml2", "evals/triggers.json", "triggers missing libxml2 excavate pattern")
    h.require_contains("xml", "evals/triggers.json", "triggers missing xml excavate pattern")
    h.require_contains(".xml", "evals/triggers.json", "triggers missing .xml excavate pattern")
    h.require_contains("yq", "evals/triggers.json", "triggers missing yq excavate pattern")
    h.require_contains("kislyuk-yq", "evals/triggers.json", "triggers missing kislyuk-yq excavate pattern")
    h.require_contains("yq3.4", "evals/triggers.json", "triggers missing yq3.4 excavate pattern")
    h.require_contains("yaml", "evals/triggers.json", "triggers missing yaml excavate pattern")
    h.require_contains(".yaml", "evals/triggers.json", "triggers missing .yaml excavate pattern")
    h.require_contains(".yml", "evals/triggers.json", "triggers missing .yml excavate pattern")
    h.require_contains("tomlq", "evals/triggers.json", "triggers missing tomlq excavate pattern")
    h.require_contains("kislyuk-tomlq", "evals/triggers.json", "triggers missing kislyuk-tomlq excavate pattern")
    h.require_contains("tomlq3.4", "evals/triggers.json", "triggers missing tomlq3.4 excavate pattern")
    h.require_contains("toml", "evals/triggers.json", "triggers missing toml excavate pattern")
    h.require_contains(".toml", "evals/triggers.json", "triggers missing .toml excavate pattern")
    h.require_contains("tidy", "evals/triggers.json", "triggers missing tidy excavate pattern")
    h.require_contains("html-tidy", "evals/triggers.json", "triggers missing html-tidy excavate pattern")
    h.require_contains("tidy5.8", "evals/triggers.json", "triggers missing tidy5.8 excavate pattern")
    h.require_contains("html", "evals/triggers.json", "triggers missing html excavate pattern")
    h.require_contains(".html", "evals/triggers.json", "triggers missing .html excavate pattern")
    h.require_contains(".htm", "evals/triggers.json", "triggers missing .htm excavate pattern")
    h.require_contains("csv", "evals/triggers.json", "triggers missing csv excavate pattern")
    h.require_contains("pycsv", "evals/triggers.json", "triggers missing pycsv excavate pattern")
    h.require_contains("csv1.0", "evals/triggers.json", "triggers missing csv1.0 excavate pattern")
    h.require_contains(".csv", "evals/triggers.json", "triggers missing .csv excavate pattern")
    h.require_contains("pyjson", "evals/triggers.json", "triggers missing pyjson excavate pattern")
    h.require_contains("json2.0", "evals/triggers.json", "triggers missing json2.0 excavate pattern")
    h.require_contains(".json", "evals/triggers.json", "triggers missing .json excavate pattern")
    h.require_contains("ini", "evals/triggers.json", "triggers missing ini excavate pattern")
    h.require_contains("pyini", "evals/triggers.json", "triggers missing pyini excavate pattern")
    h.require_contains("configparser", "evals/triggers.json", "triggers missing configparser excavate pattern")
    h.require_contains(".ini", "evals/triggers.json", "triggers missing .ini excavate pattern")
    h.require_contains("plist", "evals/triggers.json", "triggers missing plist excavate pattern")
    h.require_contains("pyplist", "evals/triggers.json", "triggers missing pyplist excavate pattern")
    h.require_contains("plistlib", "evals/triggers.json", "triggers missing plistlib excavate pattern")
    h.require_contains(".plist", "evals/triggers.json", "triggers missing .plist excavate pattern")
    h.require_contains("eml", "evals/triggers.json", "triggers missing eml excavate pattern")
    h.require_contains("pyemail", "evals/triggers.json", "triggers missing pyemail excavate pattern")
    h.require_contains("email.parser", "evals/triggers.json", "triggers missing email.parser excavate pattern")
    h.require_contains(".eml", "evals/triggers.json", "triggers missing .eml excavate pattern")
    h.require_contains("zip", "evals/triggers.json", "triggers missing zip excavate pattern")
    h.require_contains("pyzip", "evals/triggers.json", "triggers missing pyzip excavate pattern")
    h.require_contains("zipfile", "evals/triggers.json", "triggers missing zipfile excavate pattern")
    h.require_contains(".zip", "evals/triggers.json", "triggers missing .zip excavate pattern")
    h.require_contains("tar", "evals/triggers.json", "triggers missing tar excavate pattern")
    h.require_contains("pytar", "evals/triggers.json", "triggers missing pytar excavate pattern")
    h.require_contains("tarfile", "evals/triggers.json", "triggers missing tarfile excavate pattern")
    h.require_contains(".tar", "evals/triggers.json", "triggers missing .tar excavate pattern")
    h.require_contains("gzip", "evals/triggers.json", "triggers missing gzip excavate pattern")
    h.require_contains("pygzip", "evals/triggers.json", "triggers missing pygzip excavate pattern")
    h.require_contains("gzipfile", "evals/triggers.json", "triggers missing gzipfile excavate pattern")
    h.require_contains(".gz", "evals/triggers.json", "triggers missing .gz excavate pattern")
    h.require_contains("targz", "evals/triggers.json", "triggers missing targz excavate pattern")
    h.require_contains("tarball", "evals/triggers.json", "triggers missing tarball excavate pattern")
    h.require_contains("pytargz", "evals/triggers.json", "triggers missing pytargz excavate pattern")
    h.require_contains(".tar.gz", "evals/triggers.json", "triggers missing .tar.gz excavate pattern")
    h.require_contains(".tgz", "evals/triggers.json", "triggers missing .tgz excavate pattern")
    h.require_contains(".tar.bz2", "evals/triggers.json", "triggers missing .tar.bz2 excavate pattern")
    h.require_contains(".tar.xz", "evals/triggers.json", "triggers missing .tar.xz excavate pattern")
    h.require_contains(".js", "evals/triggers.json", "triggers missing .js excavate pattern")
    _, rout_py = h.run_py("scripts/lib/route.py", "finish the branch")
    if "emperor-forge" not in rout_py:
        h.fail_msg("route.py finish the branch → forge")
    _, rout_f90 = h.run_py("scripts/lib/route.py", "hello.f90")
    if "emperor-excavate" not in rout_f90:
        h.fail_msg("route.py hello.f90 → excavate")
    _, rout_vhd = h.run_py("scripts/lib/route.py", "hello.vhd")
    if "emperor-excavate" not in rout_vhd:
        h.fail_msg("route.py hello.vhd → excavate")
    _, rout_ada = h.run_py("scripts/lib/route.py", "hello.adb")
    if "emperor-excavate" not in rout_ada:
        h.fail_msg("route.py hello.adb → excavate")
    _, rout_gnat = h.run_py("scripts/lib/route.py", "gnatmake HELLO.ADB")
    if "emperor-excavate" not in rout_gnat:
        h.fail_msg("route.py gnatmake → excavate")
    _, rout_fs = h.run_py("scripts/lib/route.py", "hello.fs")
    if "emperor-excavate" not in rout_fs:
        h.fail_msg("route.py hello.fs → excavate")
    _, rout_pf = h.run_py("scripts/lib/route.py", "pforth HELLO.FS")
    if "emperor-excavate" not in rout_pf:
        h.fail_msg("route.py pforth → excavate")
    _, rout_lisp = h.run_py("scripts/lib/route.py", "hello.lisp")
    if "emperor-excavate" not in rout_lisp:
        h.fail_msg("route.py hello.lisp → excavate")
    _, rout_clisp = h.run_py("scripts/lib/route.py", "clisp HELLO.LISP")
    if "emperor-excavate" not in rout_clisp:
        h.fail_msg("route.py clisp → excavate")
    _, rout_pro = h.run_py("scripts/lib/route.py", "hello.pro")
    if "emperor-excavate" not in rout_pro:
        h.fail_msg("route.py hello.pro → excavate")
    _, rout_swipl = h.run_py("scripts/lib/route.py", "swipl HELLO.PRO")
    if "emperor-excavate" not in rout_swipl:
        h.fail_msg("route.py swipl → excavate")
    _, rout_tcl = h.run_py("scripts/lib/route.py", "hello.tcl")
    if "emperor-excavate" not in rout_tcl:
        h.fail_msg("route.py hello.tcl → excavate")
    _, rout_tclsh = h.run_py("scripts/lib/route.py", "tclsh HELLO.TCL")
    if "emperor-excavate" not in rout_tclsh:
        h.fail_msg("route.py tclsh → excavate")
    _, rout_erl = h.run_py("scripts/lib/route.py", "hello.erl")
    if "emperor-excavate" not in rout_erl:
        h.fail_msg("route.py hello.erl → excavate")
    _, rout_escript = h.run_py("scripts/lib/route.py", "escript HELLO.ERL")
    if "emperor-excavate" not in rout_escript:
        h.fail_msg("route.py escript → excavate")
    _, rout_rex = h.run_py("scripts/lib/route.py", "hello.rex")
    if "emperor-excavate" not in rout_rex:
        h.fail_msg("route.py hello.rex → excavate")
    _, rout_mod = h.run_py("scripts/lib/route.py", "hello.mod")
    if "emperor-excavate" not in rout_mod:
        h.fail_msg("route.py hello.mod → excavate")
    _, rout_a68 = h.run_py("scripts/lib/route.py", "hello.a68")
    if "emperor-excavate" not in rout_a68:
        h.fail_msg("route.py hello.a68 → excavate")
    _, rout_a68g = h.run_py("scripts/lib/route.py", "a68g HELLO.A68")
    if "emperor-excavate" not in rout_a68g:
        h.fail_msg("route.py a68g → excavate")
    _, rout_a60 = h.run_py("scripts/lib/route.py", "hello.a60")
    if "emperor-excavate" not in rout_a60:
        h.fail_msg("route.py hello.a60 → excavate")
    _, rout_marst = h.run_py("scripts/lib/route.py", "marst HELLO.A60")
    if "emperor-excavate" not in rout_marst:
        h.fail_msg("route.py marst → excavate")
    _, rout_alw = h.run_py("scripts/lib/route.py", "hello.alw")
    if "emperor-excavate" not in rout_alw:
        h.fail_msg("route.py hello.alw → excavate")
    _, rout_awe = h.run_py("scripts/lib/route.py", "awe HELLO.ALW")
    if "emperor-excavate" not in rout_awe:
        h.fail_msg("route.py awe → excavate")
    _, rout_icn = h.run_py("scripts/lib/route.py", "hello.icn")
    if "emperor-excavate" not in rout_icn:
        h.fail_msg("route.py hello.icn → excavate")
    _, rout_icont = h.run_py("scripts/lib/route.py", "icont HELLO.ICN")
    if "emperor-excavate" not in rout_icont:
        h.fail_msg("route.py icont → excavate")
    _, rout_obn = h.run_py("scripts/lib/route.py", "hello.obn")
    if "emperor-excavate" not in rout_obn:
        h.fail_msg("route.py hello.obn → excavate")
    _, rout_voc = h.run_py("scripts/lib/route.py", "voc HELLO.OBN")
    if "emperor-excavate" not in rout_voc:
        h.fail_msg("route.py voc → excavate")
    _, rout_sno = h.run_py("scripts/lib/route.py", "hello.sno")
    if "emperor-excavate" not in rout_sno:
        h.fail_msg("route.py hello.sno → excavate")
    _, rout_snobol4 = h.run_py("scripts/lib/route.py", "snobol4 HELLO.SNO")
    if "emperor-excavate" not in rout_snobol4:
        h.fail_msg("route.py snobol4 → excavate")
    _, rout_sim = h.run_py("scripts/lib/route.py", "hello.sim")
    if "emperor-excavate" not in rout_sim:
        h.fail_msg("route.py hello.sim → excavate")
    _, rout_cim = h.run_py("scripts/lib/route.py", "cim HELLO.SIM")
    if "emperor-excavate" not in rout_cim:
        h.fail_msg("route.py cim → excavate")
    _, rout_apl = h.run_py("scripts/lib/route.py", "hello.apl")
    if "emperor-excavate" not in rout_apl:
        h.fail_msg("route.py hello.apl → excavate")
    _, rout_aplbin = h.run_py("scripts/lib/route.py", "apl HELLO.APL")
    if "emperor-excavate" not in rout_aplbin:
        h.fail_msg("route.py apl → excavate")
    _, rout_bcpl = h.run_py("scripts/lib/route.py", "bcpl HELLO.B")
    if "emperor-excavate" not in rout_bcpl:
        h.fail_msg("route.py bcpl → excavate")
    _, rout_cintsys = h.run_py("scripts/lib/route.py", "cintsys hello.b")
    if "emperor-excavate" not in rout_cintsys:
        h.fail_msg("route.py cintsys → excavate")
    _, rout_pli = h.run_py("scripts/lib/route.py", "hello.pli")
    if "emperor-excavate" not in rout_pli:
        h.fail_msg("route.py hello.pli → excavate")
    _, rout_plic = h.run_py("scripts/lib/route.py", "plic HELLO.PLI")
    if "emperor-excavate" not in rout_plic:
        h.fail_msg("route.py plic → excavate")
    _, rout_gst = h.run_py("scripts/lib/route.py", "gst HELLO.ST")
    if "emperor-excavate" not in rout_gst:
        h.fail_msg("route.py gst → excavate")
    _, rout_st = h.run_py("scripts/lib/route.py", "smalltalk HELLO.ST")
    if "emperor-excavate" not in rout_st:
        h.fail_msg("route.py smalltalk → excavate")
    _, rout_gs = h.run_py("scripts/lib/route.py", "ghostscript HELLO.PS")
    if "emperor-excavate" not in rout_gs:
        h.fail_msg("route.py ghostscript → excavate")
    _, rout_ps = h.run_py("scripts/lib/route.py", "postscript HELLO.PS")
    if "emperor-excavate" not in rout_ps:
        h.fail_msg("route.py postscript → excavate")
    _, rout_bw = h.run_py("scripts/lib/route.py", "bwbasic HELLO.BAS")
    if "emperor-excavate" not in rout_bw:
        h.fail_msg("route.py bwbasic → excavate")
    _, rout_byw = h.run_py("scripts/lib/route.py", "bywater HELLO.BAS")
    if "emperor-excavate" not in rout_byw:
        h.fail_msg("route.py bywater → excavate")
    _, rout_csi = h.run_py("scripts/lib/route.py", "csi HELLO.SCM")
    if "emperor-excavate" not in rout_csi:
        h.fail_msg("route.py csi → excavate")
    _, rout_chick = h.run_py("scripts/lib/route.py", "chicken HELLO.SCM")
    if "emperor-excavate" not in rout_chick:
        h.fail_msg("route.py chicken → excavate")
    _, rout_chscm = h.run_py("scripts/lib/route.py", "chicken-scheme HELLO.SCM")
    if "emperor-excavate" not in rout_chscm:
        h.fail_msg("route.py chicken-scheme → excavate")
    _, rout_scm = h.run_py("scripts/lib/route.py", "hello.scm")
    if "emperor-excavate" not in rout_scm:
        h.fail_msg("route.py hello.scm → excavate")
    _, rout_gawk = h.run_py("scripts/lib/route.py", "gawk HELLO.AWK")
    if "emperor-excavate" not in rout_gawk:
        h.fail_msg("route.py gawk → excavate")
    _, rout_awk = h.run_py("scripts/lib/route.py", "awk HELLO.AWK")
    if "emperor-excavate" not in rout_awk:
        h.fail_msg("route.py awk → excavate")
    _, rout_nawk = h.run_py("scripts/lib/route.py", "nawk HELLO.AWK")
    if "emperor-excavate" not in rout_nawk:
        h.fail_msg("route.py nawk → excavate")
    _, rout_awkf = h.run_py("scripts/lib/route.py", "hello.awk")
    if "emperor-excavate" not in rout_awkf:
        h.fail_msg("route.py hello.awk → excavate")
    _, rout_sed = h.run_py("scripts/lib/route.py", "sed HELLO.SED")
    if "emperor-excavate" not in rout_sed:
        h.fail_msg("route.py sed → excavate")
    _, rout_gsed = h.run_py("scripts/lib/route.py", "gsed HELLO.SED")
    if "emperor-excavate" not in rout_gsed:
        h.fail_msg("route.py gsed → excavate")
    _, rout_sedf = h.run_py("scripts/lib/route.py", "hello.sed")
    if "emperor-excavate" not in rout_sedf:
        h.fail_msg("route.py hello.sed → excavate")
    _, rout_m4 = h.run_py("scripts/lib/route.py", "m4 HELLO.M4")
    if "emperor-excavate" not in rout_m4:
        h.fail_msg("route.py m4 → excavate")
    _, rout_gm4 = h.run_py("scripts/lib/route.py", "gm4 HELLO.M4")
    if "emperor-excavate" not in rout_gm4:
        h.fail_msg("route.py gm4 → excavate")
    _, rout_m4f = h.run_py("scripts/lib/route.py", "hello.m4")
    if "emperor-excavate" not in rout_m4f:
        h.fail_msg("route.py hello.m4 → excavate")
    _, rout_ed = h.run_py("scripts/lib/route.py", "ed HELLO.ED")
    if "emperor-excavate" not in rout_ed:
        h.fail_msg("route.py ed → excavate")
    _, rout_gnued = h.run_py("scripts/lib/route.py", "gnu-ed HELLO.ED")
    if "emperor-excavate" not in rout_gnued:
        h.fail_msg("route.py gnu-ed → excavate")
    _, rout_edf = h.run_py("scripts/lib/route.py", "hello.ed")
    if "emperor-excavate" not in rout_edf:
        h.fail_msg("route.py hello.ed → excavate")
    _, rout_gmake = h.run_py("scripts/lib/route.py", "gmake HELLO.MK")
    if "emperor-excavate" not in rout_gmake:
        h.fail_msg("route.py gmake → excavate")
    _, rout_gnumake = h.run_py("scripts/lib/route.py", "gnu-make HELLO.MK")
    if "emperor-excavate" not in rout_gnumake:
        h.fail_msg("route.py gnu-make → excavate")
    _, rout_mkf = h.run_py("scripts/lib/route.py", "hello.mk")
    if "emperor-excavate" not in rout_mkf:
        h.fail_msg("route.py hello.mk → excavate")
    _, rout_makefile = h.run_py("scripts/lib/route.py", "makefile")
    if "emperor-excavate" not in rout_makefile:
        h.fail_msg("route.py makefile → excavate")
    rc_make, rout_bare_make = h.run_py("scripts/lib/route.py", "make software")
    if "emperor-excavate" in rout_bare_make:
        h.fail_msg("route.py bare make/make software must not → excavate")
    _, rout_dc = h.run_py("scripts/lib/route.py", "dc HELLO.DC")
    if "emperor-excavate" not in rout_dc:
        h.fail_msg("route.py dc → excavate")
    _, rout_gnudc = h.run_py("scripts/lib/route.py", "gnu-dc HELLO.DC")
    if "emperor-excavate" not in rout_gnudc:
        h.fail_msg("route.py gnu-dc → excavate")
    _, rout_dcf = h.run_py("scripts/lib/route.py", "hello.dc")
    if "emperor-excavate" not in rout_dcf:
        h.fail_msg("route.py hello.dc → excavate")
    _, rout_lex = h.run_py("scripts/lib/route.py", "lex HELLO.L")
    if "emperor-excavate" not in rout_lex:
        h.fail_msg("route.py lex → excavate")
    _, rout_flex = h.run_py("scripts/lib/route.py", "flex HELLO.L")
    if "emperor-excavate" not in rout_flex:
        h.fail_msg("route.py flex → excavate")
    _, rout_gnuflex = h.run_py("scripts/lib/route.py", "gnu-flex HELLO.L")
    if "emperor-excavate" not in rout_gnuflex:
        h.fail_msg("route.py gnu-flex → excavate")
    _, rout_lexf = h.run_py("scripts/lib/route.py", "hello.lex")
    if "emperor-excavate" not in rout_lexf:
        h.fail_msg("route.py hello.lex → excavate")
    _, rout_yacc = h.run_py("scripts/lib/route.py", "yacc HELLO.Y")
    if "emperor-excavate" not in rout_yacc:
        h.fail_msg("route.py yacc → excavate")
    _, rout_bison = h.run_py("scripts/lib/route.py", "bison HELLO.Y")
    if "emperor-excavate" not in rout_bison:
        h.fail_msg("route.py bison → excavate")
    _, rout_gnubison = h.run_py("scripts/lib/route.py", "gnu-bison HELLO.Y")
    if "emperor-excavate" not in rout_gnubison:
        h.fail_msg("route.py gnu-bison → excavate")
    _, rout_yaccf = h.run_py("scripts/lib/route.py", "hello.y")
    if "emperor-excavate" not in rout_yaccf:
        h.fail_msg("route.py hello.y → excavate")
    _, rout_roff = h.run_py("scripts/lib/route.py", "roff HELLO.ROFF")
    if "emperor-excavate" not in rout_roff:
        h.fail_msg("route.py roff → excavate")
    _, rout_nroff = h.run_py("scripts/lib/route.py", "nroff HELLO.ROFF")
    if "emperor-excavate" not in rout_nroff:
        h.fail_msg("route.py nroff → excavate")
    _, rout_groff = h.run_py("scripts/lib/route.py", "groff HELLO.ROFF")
    if "emperor-excavate" not in rout_groff:
        h.fail_msg("route.py groff → excavate")
    _, rout_gnugroff = h.run_py("scripts/lib/route.py", "gnu-groff HELLO.ROFF")
    if "emperor-excavate" not in rout_gnugroff:
        h.fail_msg("route.py gnu-groff → excavate")
    _, rout_rofff = h.run_py("scripts/lib/route.py", "hello.roff")
    if "emperor-excavate" not in rout_rofff:
        h.fail_msg("route.py hello.roff → excavate")
    _, rout_perl = h.run_py("scripts/lib/route.py", "perl HELLO.PL")
    if "emperor-excavate" not in rout_perl:
        h.fail_msg("route.py perl → excavate")
    _, rout_perl5 = h.run_py("scripts/lib/route.py", "perl5 HELLO.PL")
    if "emperor-excavate" not in rout_perl5:
        h.fail_msg("route.py perl5 → excavate")
    _, rout_pm = h.run_py("scripts/lib/route.py", "hello.pm")
    if "emperor-excavate" not in rout_pm:
        h.fail_msg("route.py hello.pm → excavate")
    # bare .pl refused (PL/I .pli/.pl1 substring); .pm + perl tags cover Perl
    _, rout_bc = h.run_py("scripts/lib/route.py", "bc HELLO.BC")
    if "emperor-excavate" not in rout_bc:
        h.fail_msg("route.py bc → excavate")
    _, rout_gnubc = h.run_py("scripts/lib/route.py", "gnu-bc HELLO.BC")
    if "emperor-excavate" not in rout_gnubc:
        h.fail_msg("route.py gnu-bc → excavate")
    # bare .bc refused (BCPL .bcpl substring); bc / gnu-bc tags cover GNU bc
    _, rout_expect = h.run_py("scripts/lib/route.py", "expect HELLO.EXP")
    if "emperor-excavate" not in rout_expect:
        h.fail_msg("route.py expect → excavate")
    _, rout_tclexpect = h.run_py("scripts/lib/route.py", "tcl-expect HELLO.EXP")
    if "emperor-excavate" not in rout_tclexpect:
        h.fail_msg("route.py tcl-expect → excavate")
    _, rout_exp = h.run_py("scripts/lib/route.py", "hello.exp")
    if "emperor-excavate" not in rout_exp:
        h.fail_msg("route.py hello.exp → excavate")
    _, rout_lua = h.run_py("scripts/lib/route.py", "lua HELLO.LUA")
    if "emperor-excavate" not in rout_lua:
        h.fail_msg("route.py lua → excavate")
    _, rout_lua54 = h.run_py("scripts/lib/route.py", "lua5.4 HELLO.LUA")
    if "emperor-excavate" not in rout_lua54:
        h.fail_msg("route.py lua5.4 → excavate")
    _, rout_luaext = h.run_py("scripts/lib/route.py", "hello.lua")
    if "emperor-excavate" not in rout_luaext:
        h.fail_msg("route.py hello.lua → excavate")
    _, rout_ruby = h.run_py("scripts/lib/route.py", "ruby HELLO.RB")
    if "emperor-excavate" not in rout_ruby:
        h.fail_msg("route.py ruby → excavate")
    _, rout_ruby33 = h.run_py("scripts/lib/route.py", "ruby3.3 HELLO.RB")
    if "emperor-excavate" not in rout_ruby33:
        h.fail_msg("route.py ruby3.3 → excavate")
    _, rout_rbext = h.run_py("scripts/lib/route.py", "hello.rb")
    if "emperor-excavate" not in rout_rbext:
        h.fail_msg("route.py hello.rb → excavate")
    _, rout_golang = h.run_py("scripts/lib/route.py", "golang HELLO.go")
    if "emperor-excavate" not in rout_golang:
        h.fail_msg("route.py golang → excavate")
    _, rout_go124 = h.run_py("scripts/lib/route.py", "go1.24 HELLO.go")
    if "emperor-excavate" not in rout_go124:
        h.fail_msg("route.py go1.24 → excavate")
    _, rout_goext = h.run_py("scripts/lib/route.py", "hello.go")
    if "emperor-excavate" not in rout_goext:
        h.fail_msg("route.py hello.go → excavate")
    # bare go refused (common English); "let's go" / "go ahead" must not excavate
    _, rout_bare_go = h.run_py("scripts/lib/route.py", "let's go")
    if "emperor-excavate" in rout_bare_go:
        h.fail_msg("route.py bare go / let's go must not → excavate")
    _, rout_go_ahead = h.run_py("scripts/lib/route.py", "go ahead")
    if "emperor-excavate" in rout_go_ahead:
        h.fail_msg("route.py go ahead must not → excavate")
    _, rout_rust = h.run_py("scripts/lib/route.py", "rust HELLO.rs")
    if "emperor-excavate" not in rout_rust:
        h.fail_msg("route.py rust → excavate")
    _, rout_rustc = h.run_py("scripts/lib/route.py", "rustc HELLO.rs")
    if "emperor-excavate" not in rout_rustc:
        h.fail_msg("route.py rustc → excavate")
    _, rout_rust185 = h.run_py("scripts/lib/route.py", "rust1.85 HELLO.rs")
    if "emperor-excavate" not in rout_rust185:
        h.fail_msg("route.py rust1.85 → excavate")
    _, rout_rsext = h.run_py("scripts/lib/route.py", "hello.rs")
    if "emperor-excavate" not in rout_rsext:
        h.fail_msg("route.py hello.rs → excavate")
    _, rout_gcc = h.run_py("scripts/lib/route.py", "gcc HELLO.c")
    if "emperor-excavate" not in rout_gcc:
        h.fail_msg("route.py gcc → excavate")
    _, rout_gcc14 = h.run_py("scripts/lib/route.py", "gcc14 HELLO.c")
    if "emperor-excavate" not in rout_gcc14:
        h.fail_msg("route.py gcc14 → excavate")
    _, rout_c11 = h.run_py("scripts/lib/route.py", "c11 HELLO.c")
    if "emperor-excavate" not in rout_c11:
        h.fail_msg("route.py c11 → excavate")
    _, rout_cext = h.run_py("scripts/lib/route.py", "hello.c")
    if "emperor-excavate" not in rout_cext:
        h.fail_msg("route.py hello.c → excavate")
    # bare c must not excavate (single-letter / English); .c boundary vs .cbl/.cl
    _, rout_bare_c = h.run_py("scripts/lib/route.py", "section c notes")
    if "emperor-excavate" in rout_bare_c:
        h.fail_msg("route.py bare c English must not → excavate")
    import importlib.util
    _route_spec = importlib.util.spec_from_file_location(
        "et_route_matches", root / "scripts" / "lib" / "route.py"
    )
    _route_mod = importlib.util.module_from_spec(_route_spec)
    assert _route_spec.loader is not None
    _route_spec.loader.exec_module(_route_mod)
    _m = _route_mod.matches
    if _m(".c", "hello.cbl"):
        h.fail_msg("route matches(.c, hello.cbl) must be False after extension-boundary")
    if _m(".c", "hello.cl"):
        h.fail_msg("route matches(.c, hello.cl) must be False after extension-boundary")
    if not _m(".c", "hello.c"):
        h.fail_msg("route matches(.c, hello.c) must be True")
    _, rout_nodejs = h.run_py("scripts/lib/route.py", "nodejs HELLO.js")
    if "emperor-excavate" not in rout_nodejs:
        h.fail_msg("route.py nodejs → excavate")
    _, rout_node20 = h.run_py("scripts/lib/route.py", "node20 HELLO.js")
    if "emperor-excavate" not in rout_node20:
        h.fail_msg("route.py node20 → excavate")
    _, rout_javascript = h.run_py("scripts/lib/route.py", "javascript HELLO.js")
    if "emperor-excavate" not in rout_javascript:
        h.fail_msg("route.py javascript → excavate")
    _, rout_jsext = h.run_py("scripts/lib/route.py", "hello.js")
    if "emperor-excavate" not in rout_jsext:
        h.fail_msg("route.py hello.js → excavate")
    # .js boundary vs .json/.jsx (reuse matches helper imported above)
    if _m(".js", "hello.json"):
        h.fail_msg("route matches(.js, hello.json) must be False after extension-boundary")
    if _m(".js", "hello.jsx"):
        h.fail_msg("route matches(.js, hello.jsx) must be False after extension-boundary")
    if not _m(".js", "hello.js"):
        h.fail_msg("route matches(.js, hello.js) must be True")
    # bare node must not excavate (common English / tech "AST node" collision)
    _, rout_bare_node = h.run_py("scripts/lib/route.py", "ast node notes")
    if "emperor-excavate" in rout_bare_node:
        h.fail_msg("route.py bare node English must not → excavate")
    _, rout_python3 = h.run_py("scripts/lib/route.py", "python3 HELLO.py")
    if "emperor-excavate" not in rout_python3:
        h.fail_msg("route.py python3 → excavate")
    _, rout_python313 = h.run_py("scripts/lib/route.py", "python3.13 HELLO.py")
    if "emperor-excavate" not in rout_python313:
        h.fail_msg("route.py python3.13 → excavate")
    _, rout_cpython = h.run_py("scripts/lib/route.py", "cpython HELLO.py")
    if "emperor-excavate" not in rout_cpython:
        h.fail_msg("route.py cpython → excavate")
    _, rout_py_abbr = h.run_py("scripts/lib/route.py", "py HELLO.py")
    if "emperor-excavate" not in rout_py_abbr:
        h.fail_msg("route.py bare py → excavate")
    if _m(".py", "hello.pyc"):
        h.fail_msg("route matches(.py, hello.pyc) must be False after extension-boundary")
    if _m(".py", "hello.pyw"):
        h.fail_msg("route matches(.py, hello.pyw) must be False after extension-boundary")
    if _m(".py", "hello.pyi"):
        h.fail_msg("route matches(.py, hello.pyi) must be False after extension-boundary")
    if not _m(".py", "hello.py"):
        h.fail_msg("route matches(.py, hello.py) must be True")
    # bare python must not excavate (ET meta / house-tooling discourse collision)
    _, rout_bare_python = h.run_py("scripts/lib/route.py", "prefer python for new tooling")
    if "emperor-excavate" in rout_bare_python:
        h.fail_msg("route.py bare python ET-meta must not → excavate")
    _, rout_typescript = h.run_py("scripts/lib/route.py", "typescript HELLO.ts")
    if "emperor-excavate" not in rout_typescript:
        h.fail_msg("route.py typescript → excavate")
    _, rout_typescript5 = h.run_py("scripts/lib/route.py", "typescript5 HELLO.ts")
    if "emperor-excavate" not in rout_typescript5:
        h.fail_msg("route.py typescript5 → excavate")
    _, rout_tsc = h.run_py("scripts/lib/route.py", "tsc HELLO.ts")
    if "emperor-excavate" not in rout_tsc:
        h.fail_msg("route.py tsc → excavate")
    _, rout_ts5 = h.run_py("scripts/lib/route.py", "ts5 HELLO.ts")
    if "emperor-excavate" not in rout_ts5:
        h.fail_msg("route.py ts5 → excavate")
    _, rout_ts_abbr = h.run_py("scripts/lib/route.py", "ts HELLO.ts")
    if "emperor-excavate" not in rout_ts_abbr:
        h.fail_msg("route.py bare ts → excavate")
    if _m(".ts", "hello.tsx"):
        h.fail_msg("route matches(.ts, hello.tsx) must be False after extension-boundary")
    if _m(".ts", "hello.tsbuildinfo"):
        h.fail_msg("route matches(.ts, hello.tsbuildinfo) must be False after extension-boundary")
    if _m(".ts", "hello.mts"):
        h.fail_msg("route matches(.ts, hello.mts) must be False after extension-boundary")
    if _m(".ts", "hello.cts"):
        h.fail_msg("route matches(.ts, hello.cts) must be False after extension-boundary")
    if not _m(".ts", "hello.ts"):
        h.fail_msg("route matches(.ts, hello.ts) must be True")
    _, rout_bash = h.run_py("scripts/lib/route.py", "bash HELLO.sh")
    if "emperor-excavate" not in rout_bash:
        h.fail_msg("route.py bash → excavate")
    _, rout_bash5 = h.run_py("scripts/lib/route.py", "bash5 HELLO.sh")
    if "emperor-excavate" not in rout_bash5:
        h.fail_msg("route.py bash5 → excavate")
    _, rout_bash52 = h.run_py("scripts/lib/route.py", "bash5.2 HELLO.sh")
    if "emperor-excavate" not in rout_bash52:
        h.fail_msg("route.py bash5.2 → excavate")
    _, rout_gnu_bash = h.run_py("scripts/lib/route.py", "gnu-bash HELLO.sh")
    if "emperor-excavate" not in rout_gnu_bash:
        h.fail_msg("route.py gnu-bash → excavate")
    _, rout_hello_sh = h.run_py("scripts/lib/route.py", "hello.sh")
    if "emperor-excavate" not in rout_hello_sh:
        h.fail_msg("route.py hello.sh → excavate")
    # bare sh must not excavate (POSIX / dash ambiguity; verified toolchain is bash)
    # Utterance must not include a .sh filename (that correctly routes via extension).
    _, rout_bare_sh = h.run_py("scripts/lib/route.py", "prefer sh for portability")
    if "emperor-excavate" in rout_bare_sh:
        h.fail_msg("route.py bare sh POSIX/dash must not → excavate")
    if _m(".sh", "hello.sha"):
        h.fail_msg("route matches(.sh, hello.sha) must be False after extension-boundary")
    if _m(".sh", "hello.shar"):
        h.fail_msg("route matches(.sh, hello.shar) must be False after extension-boundary")
    if _m(".sh", "hello.shtml"):
        h.fail_msg("route matches(.sh, hello.shtml) must be False after extension-boundary")
    if not _m(".sh", "hello.sh"):
        h.fail_msg("route matches(.sh, hello.sh) must be True")
    _, rout_php = h.run_py("scripts/lib/route.py", "php HELLO.php")
    if "emperor-excavate" not in rout_php:
        h.fail_msg("route.py php → excavate")
    _, rout_php8 = h.run_py("scripts/lib/route.py", "php8 HELLO.php")
    if "emperor-excavate" not in rout_php8:
        h.fail_msg("route.py php8 → excavate")
    _, rout_php84 = h.run_py("scripts/lib/route.py", "php8.4 HELLO.php")
    if "emperor-excavate" not in rout_php84:
        h.fail_msg("route.py php8.4 → excavate")
    _, rout_php_cli = h.run_py("scripts/lib/route.py", "php-cli HELLO.php")
    if "emperor-excavate" not in rout_php_cli:
        h.fail_msg("route.py php-cli → excavate")
    _, rout_hello_php = h.run_py("scripts/lib/route.py", "hello.php")
    if "emperor-excavate" not in rout_hello_php:
        h.fail_msg("route.py hello.php → excavate")
    if _m(".php", "hello.php3"):
        h.fail_msg("route matches(.php, hello.php3) must be False after extension-boundary")
    if _m(".php", "hello.php4"):
        h.fail_msg("route matches(.php, hello.php4) must be False after extension-boundary")
    if _m(".php", "hello.php5"):
        h.fail_msg("route matches(.php, hello.php5) must be False after extension-boundary")
    if _m(".php", "hello.phps"):
        h.fail_msg("route matches(.php, hello.phps) must be False after extension-boundary")
    if not _m(".php", "hello.php"):
        h.fail_msg("route matches(.php, hello.php) must be True")
    _, rout_sqlite = h.run_py("scripts/lib/route.py", "sqlite HELLO.sql")
    if "emperor-excavate" not in rout_sqlite:
        h.fail_msg("route.py sqlite → excavate")
    _, rout_sqlite3 = h.run_py("scripts/lib/route.py", "sqlite3 HELLO.sql")
    if "emperor-excavate" not in rout_sqlite3:
        h.fail_msg("route.py sqlite3 → excavate")
    _, rout_sqlite346 = h.run_py("scripts/lib/route.py", "sqlite3.46 HELLO.sql")
    if "emperor-excavate" not in rout_sqlite346:
        h.fail_msg("route.py sqlite3.46 → excavate")
    _, rout_hello_sql = h.run_py("scripts/lib/route.py", "hello.sql")
    if "emperor-excavate" not in rout_hello_sql:
        h.fail_msg("route.py hello.sql → excavate")
    if _m(".sql", "hello.sqlite"):
        h.fail_msg("route matches(.sql, hello.sqlite) must be False after extension-boundary")
    if _m(".sql", "hello.sqlite3"):
        h.fail_msg("route matches(.sql, hello.sqlite3) must be False after extension-boundary")
    if _m(".sql", "hello.sqlitedb"):
        h.fail_msg("route matches(.sql, hello.sqlitedb) must be False after extension-boundary")
    if not _m(".sql", "hello.sql"):
        h.fail_msg("route matches(.sql, hello.sql) must be True")
    _, rout_jq = h.run_py("scripts/lib/route.py", "jq HELLO.jq")
    if "emperor-excavate" not in rout_jq:
        h.fail_msg("route.py jq → excavate")
    _, rout_jq17 = h.run_py("scripts/lib/route.py", "jq1.7 HELLO.jq")
    if "emperor-excavate" not in rout_jq17:
        h.fail_msg("route.py jq1.7 → excavate")
    _, rout_jqlang = h.run_py("scripts/lib/route.py", "jqlang HELLO.jq")
    if "emperor-excavate" not in rout_jqlang:
        h.fail_msg("route.py jqlang → excavate")
    _, rout_hello_jq = h.run_py("scripts/lib/route.py", "hello.jq")
    if "emperor-excavate" not in rout_hello_jq:
        h.fail_msg("route.py hello.jq → excavate")
    if _m(".jq", "hello.jquery"):
        h.fail_msg("route matches(.jq, hello.jquery) must be False after extension-boundary")
    if not _m(".jq", "hello.jq"):
        h.fail_msg("route matches(.jq, hello.jq) must be True")
    _, rout_xsltproc = h.run_py("scripts/lib/route.py", "xsltproc HELLO.xsl")
    if "emperor-excavate" not in rout_xsltproc:
        h.fail_msg("route.py xsltproc → excavate")
    _, rout_libxslt = h.run_py("scripts/lib/route.py", "libxslt HELLO.xsl")
    if "emperor-excavate" not in rout_libxslt:
        h.fail_msg("route.py libxslt → excavate")
    _, rout_xslt = h.run_py("scripts/lib/route.py", "xslt HELLO.xsl")
    if "emperor-excavate" not in rout_xslt:
        h.fail_msg("route.py xslt → excavate")
    _, rout_hello_xsl = h.run_py("scripts/lib/route.py", "hello.xsl")
    if "emperor-excavate" not in rout_hello_xsl:
        h.fail_msg("route.py hello.xsl → excavate")
    _, rout_hello_xslt = h.run_py("scripts/lib/route.py", "hello.xslt")
    if "emperor-excavate" not in rout_hello_xslt:
        h.fail_msg("route.py hello.xslt → excavate")
    if _m(".xsl", "hello.xslt"):
        h.fail_msg("route matches(.xsl, hello.xslt) must be False after extension-boundary")
    if not _m(".xsl", "hello.xsl"):
        h.fail_msg("route matches(.xsl, hello.xsl) must be True")
    if not _m(".xslt", "hello.xslt"):
        h.fail_msg("route matches(.xslt, hello.xslt) must be True")
    _, rout_xmllint = h.run_py("scripts/lib/route.py", "xmllint HELLO.xml")
    if "emperor-excavate" not in rout_xmllint:
        h.fail_msg("route.py xmllint → excavate")
    _, rout_libxml2 = h.run_py("scripts/lib/route.py", "libxml2 HELLO.xml")
    if "emperor-excavate" not in rout_libxml2:
        h.fail_msg("route.py libxml2 → excavate")
    _, rout_xml = h.run_py("scripts/lib/route.py", "xml HELLO.xml")
    if "emperor-excavate" not in rout_xml:
        h.fail_msg("route.py xml → excavate")
    _, rout_hello_xml = h.run_py("scripts/lib/route.py", "hello.xml")
    if "emperor-excavate" not in rout_hello_xml:
        h.fail_msg("route.py hello.xml → excavate")
    if not _m(".xml", "hello.xml"):
        h.fail_msg("route matches(.xml, hello.xml) must be True")
    if _m(".xml", "hello.xmlrpc"):
        h.fail_msg("route matches(.xml, hello.xmlrpc) must be False after extension-boundary")
    _, rout_yq = h.run_py("scripts/lib/route.py", "yq HELLO.yaml")
    if "emperor-excavate" not in rout_yq:
        h.fail_msg("route.py yq → excavate")
    _, rout_kislyuk = h.run_py("scripts/lib/route.py", "kislyuk-yq HELLO.yaml")
    if "emperor-excavate" not in rout_kislyuk:
        h.fail_msg("route.py kislyuk-yq → excavate")
    _, rout_yq34 = h.run_py("scripts/lib/route.py", "yq3.4 HELLO.yaml")
    if "emperor-excavate" not in rout_yq34:
        h.fail_msg("route.py yq3.4 → excavate")
    _, rout_yaml = h.run_py("scripts/lib/route.py", "yaml HELLO.yaml")
    if "emperor-excavate" not in rout_yaml:
        h.fail_msg("route.py yaml → excavate")
    _, rout_hello_yaml = h.run_py("scripts/lib/route.py", "hello.yaml")
    if "emperor-excavate" not in rout_hello_yaml:
        h.fail_msg("route.py hello.yaml → excavate")
    _, rout_hello_yml = h.run_py("scripts/lib/route.py", "hello.yml")
    if "emperor-excavate" not in rout_hello_yml:
        h.fail_msg("route.py hello.yml → excavate")
    if not _m(".yaml", "hello.yaml"):
        h.fail_msg("route matches(.yaml, hello.yaml) must be True")
    if _m(".yaml", "hello.yamlfoo"):
        h.fail_msg("route matches(.yaml, hello.yamlfoo) must be False after extension-boundary")
    if not _m(".yml", "hello.yml"):
        h.fail_msg("route matches(.yml, hello.yml) must be True")
    if _m(".yml", "hello.ymlfoo"):
        h.fail_msg("route matches(.yml, hello.ymlfoo) must be False after extension-boundary")
    _, rout_tomlq = h.run_py("scripts/lib/route.py", "tomlq HELLO.toml")
    if "emperor-excavate" not in rout_tomlq:
        h.fail_msg("route.py tomlq → excavate")
    _, rout_kislyuk_tomlq = h.run_py("scripts/lib/route.py", "kislyuk-tomlq HELLO.toml")
    if "emperor-excavate" not in rout_kislyuk_tomlq:
        h.fail_msg("route.py kislyuk-tomlq → excavate")
    _, rout_tomlq34 = h.run_py("scripts/lib/route.py", "tomlq3.4 HELLO.toml")
    if "emperor-excavate" not in rout_tomlq34:
        h.fail_msg("route.py tomlq3.4 → excavate")
    _, rout_toml = h.run_py("scripts/lib/route.py", "toml HELLO.toml")
    if "emperor-excavate" not in rout_toml:
        h.fail_msg("route.py toml → excavate")
    _, rout_hello_toml = h.run_py("scripts/lib/route.py", "hello.toml")
    if "emperor-excavate" not in rout_hello_toml:
        h.fail_msg("route.py hello.toml → excavate")
    if not _m(".toml", "hello.toml"):
        h.fail_msg("route matches(.toml, hello.toml) must be True")
    if _m(".toml", "hello.tomlfoo"):
        h.fail_msg("route matches(.toml, hello.tomlfoo) must be False after extension-boundary")
    _, rout_tidy = h.run_py("scripts/lib/route.py", "tidy HELLO.html")
    if "emperor-excavate" not in rout_tidy:
        h.fail_msg("route.py tidy → excavate")
    _, rout_html_tidy = h.run_py("scripts/lib/route.py", "html-tidy HELLO.html")
    if "emperor-excavate" not in rout_html_tidy:
        h.fail_msg("route.py html-tidy → excavate")
    _, rout_tidy58 = h.run_py("scripts/lib/route.py", "tidy5.8 HELLO.html")
    if "emperor-excavate" not in rout_tidy58:
        h.fail_msg("route.py tidy5.8 → excavate")
    _, rout_html = h.run_py("scripts/lib/route.py", "html HELLO.html")
    if "emperor-excavate" not in rout_html:
        h.fail_msg("route.py html → excavate")
    _, rout_hello_html = h.run_py("scripts/lib/route.py", "hello.html")
    if "emperor-excavate" not in rout_hello_html:
        h.fail_msg("route.py hello.html → excavate")
    _, rout_hello_htm = h.run_py("scripts/lib/route.py", "hello.htm")
    if "emperor-excavate" not in rout_hello_htm:
        h.fail_msg("route.py hello.htm → excavate")
    if not _m(".html", "hello.html"):
        h.fail_msg("route matches(.html, hello.html) must be True")
    if _m(".html", "hello.htmlfoo"):
        h.fail_msg("route matches(.html, hello.htmlfoo) must be False after extension-boundary")
    if not _m(".htm", "hello.htm"):
        h.fail_msg("route matches(.htm, hello.htm) must be True")
    if _m(".htm", "hello.html"):
        h.fail_msg("route matches(.htm, hello.html) must be False after extension-boundary")
    _, rout_csv = h.run_py("scripts/lib/route.py", "csv HELLO.csv")
    if "emperor-excavate" not in rout_csv:
        h.fail_msg("route.py csv → excavate")
    _, rout_pycsv = h.run_py("scripts/lib/route.py", "pycsv HELLO.csv")
    if "emperor-excavate" not in rout_pycsv:
        h.fail_msg("route.py pycsv → excavate")
    _, rout_csv10 = h.run_py("scripts/lib/route.py", "csv1.0 HELLO.csv")
    if "emperor-excavate" not in rout_csv10:
        h.fail_msg("route.py csv1.0 → excavate")
    _, rout_hello_csv = h.run_py("scripts/lib/route.py", "hello.csv")
    if "emperor-excavate" not in rout_hello_csv:
        h.fail_msg("route.py hello.csv → excavate")
    if not _m(".csv", "hello.csv"):
        h.fail_msg("route matches(.csv, hello.csv) must be True")
    if _m(".csv", "hello.csvfoo"):
        h.fail_msg("route matches(.csv, hello.csvfoo) must be False after extension-boundary")
    _, rout_pyjson = h.run_py("scripts/lib/route.py", "pyjson HELLO.json")
    if "emperor-excavate" not in rout_pyjson:
        h.fail_msg("route.py pyjson → excavate")
    _, rout_json20 = h.run_py("scripts/lib/route.py", "json2.0 HELLO.json")
    if "emperor-excavate" not in rout_json20:
        h.fail_msg("route.py json2.0 → excavate")
    _, rout_hello_json = h.run_py("scripts/lib/route.py", "hello.json")
    if "emperor-excavate" not in rout_hello_json:
        h.fail_msg("route.py hello.json → excavate")
    if not _m(".json", "hello.json"):
        h.fail_msg("route matches(.json, hello.json) must be True")
    if _m(".json", "hello.jsonfoo"):
        h.fail_msg("route matches(.json, hello.jsonfoo) must be False after extension-boundary")
    if _m(".json", "hello.jsonl"):
        h.fail_msg("route matches(.json, hello.jsonl) must be False after extension-boundary")
    # bare json refused (substring collision with jsonl/json5/jsonc); not in triggers
    rc_bare_json, rout_bare_json = h.run_py("scripts/lib/route.py", "json")
    if "emperor-excavate" in rout_bare_json:
        h.fail_msg("route.py bare json must not → excavate (jsonl/json5/jsonc collision)")
    # hello.jsonl now owned by JSONL leaf (v0.4.114); .json extension-boundary above
    # still refuses prefix-steal. Positive hello.jsonl → excavate asserted in JSONL block.
    _, rout_ini = h.run_py("scripts/lib/route.py", "ini HELLO.ini")
    if "emperor-excavate" not in rout_ini:
        h.fail_msg("route.py ini → excavate")
    _, rout_pyini = h.run_py("scripts/lib/route.py", "pyini HELLO.ini")
    if "emperor-excavate" not in rout_pyini:
        h.fail_msg("route.py pyini → excavate")
    _, rout_configparser = h.run_py("scripts/lib/route.py", "configparser HELLO.ini")
    if "emperor-excavate" not in rout_configparser:
        h.fail_msg("route.py configparser → excavate")
    _, rout_hello_ini = h.run_py("scripts/lib/route.py", "hello.ini")
    if "emperor-excavate" not in rout_hello_ini:
        h.fail_msg("route.py hello.ini → excavate")
    if not _m(".ini", "hello.ini"):
        h.fail_msg("route matches(.ini, hello.ini) must be True")
    if _m(".ini", "hello.inifoo"):
        h.fail_msg("route matches(.ini, hello.inifoo) must be False after extension-boundary")
    if _m(".ini", "hello.init"):
        h.fail_msg("route matches(.ini, hello.init) must be False after extension-boundary")
    _, rout_plist = h.run_py("scripts/lib/route.py", "plist HELLO.plist")
    if "emperor-excavate" not in rout_plist:
        h.fail_msg("route.py plist → excavate")
    _, rout_pyplist = h.run_py("scripts/lib/route.py", "pyplist HELLO.plist")
    if "emperor-excavate" not in rout_pyplist:
        h.fail_msg("route.py pyplist → excavate")
    _, rout_plistlib = h.run_py("scripts/lib/route.py", "plistlib HELLO.plist")
    if "emperor-excavate" not in rout_plistlib:
        h.fail_msg("route.py plistlib → excavate")
    _, rout_hello_plist = h.run_py("scripts/lib/route.py", "hello.plist")
    if "emperor-excavate" not in rout_hello_plist:
        h.fail_msg("route.py hello.plist → excavate")
    if not _m(".plist", "hello.plist"):
        h.fail_msg("route matches(.plist, hello.plist) must be True")
    if _m(".plist", "hello.plistfoo"):
        h.fail_msg("route matches(.plist, hello.plistfoo) must be False after extension-boundary")
    if _m(".plist", "hello.plistx"):
        h.fail_msg("route matches(.plist, hello.plistx) must be False after extension-boundary")
    _, rout_eml = h.run_py("scripts/lib/route.py", "eml HELLO.eml")
    if "emperor-excavate" not in rout_eml:
        h.fail_msg("route.py eml → excavate")
    _, rout_pyemail = h.run_py("scripts/lib/route.py", "pyemail HELLO.eml")
    if "emperor-excavate" not in rout_pyemail:
        h.fail_msg("route.py pyemail → excavate")
    _, rout_email_parser = h.run_py("scripts/lib/route.py", "email.parser HELLO.eml")
    if "emperor-excavate" not in rout_email_parser:
        h.fail_msg("route.py email.parser → excavate")
    _, rout_hello_eml = h.run_py("scripts/lib/route.py", "hello.eml")
    if "emperor-excavate" not in rout_hello_eml:
        h.fail_msg("route.py hello.eml → excavate")
    if not _m(".eml", "hello.eml"):
        h.fail_msg("route matches(.eml, hello.eml) must be True")
    if _m(".eml", "hello.emlfoo"):
        h.fail_msg("route matches(.eml, hello.emlfoo) must be False after extension-boundary")
    if _m(".eml", "hello.emlx"):
        h.fail_msg("route matches(.eml, hello.emlx) must be False after extension-boundary")
    # bare email must NOT route to excavate via eml leaf (discourse collision)
    # (may still match other routes; only assert .eml extension-boundary + positive tags above)
    _, rout_zip = h.run_py("scripts/lib/route.py", "zip HELLO.zip")
    if "emperor-excavate" not in rout_zip:
        h.fail_msg("route.py zip → excavate")
    _, rout_pyzip = h.run_py("scripts/lib/route.py", "pyzip HELLO.zip")
    if "emperor-excavate" not in rout_pyzip:
        h.fail_msg("route.py pyzip → excavate")
    _, rout_zipfile = h.run_py("scripts/lib/route.py", "zipfile HELLO.zip")
    if "emperor-excavate" not in rout_zipfile:
        h.fail_msg("route.py zipfile → excavate")
    _, rout_hello_zip = h.run_py("scripts/lib/route.py", "hello.zip")
    if "emperor-excavate" not in rout_hello_zip:
        h.fail_msg("route.py hello.zip → excavate")
    if not _m(".zip", "hello.zip"):
        h.fail_msg("route matches(.zip, hello.zip) must be True")
    if _m(".zip", "hello.zipfoo"):
        h.fail_msg("route matches(.zip, hello.zipfoo) must be False after extension-boundary")
    _, rout_tar = h.run_py("scripts/lib/route.py", "tar HELLO.tar")
    if "emperor-excavate" not in rout_tar:
        h.fail_msg("route.py tar → excavate")
    _, rout_pytar = h.run_py("scripts/lib/route.py", "pytar HELLO.tar")
    if "emperor-excavate" not in rout_pytar:
        h.fail_msg("route.py pytar → excavate")
    _, rout_tarfile = h.run_py("scripts/lib/route.py", "tarfile HELLO.tar")
    if "emperor-excavate" not in rout_tarfile:
        h.fail_msg("route.py tarfile → excavate")
    _, rout_hello_tar = h.run_py("scripts/lib/route.py", "hello.tar")
    if "emperor-excavate" not in rout_hello_tar:
        h.fail_msg("route.py hello.tar → excavate")
    if not _m(".tar", "hello.tar"):
        h.fail_msg("route matches(.tar, hello.tar) must be True")
    if _m(".tar", "hello.tarfoo"):
        h.fail_msg("route matches(.tar, hello.tarfoo) must be False after extension-boundary")
    _, rout_gzip = h.run_py("scripts/lib/route.py", "gzip HELLO.gz")
    if "emperor-excavate" not in rout_gzip:
        h.fail_msg("route.py gzip → excavate")
    _, rout_pygzip = h.run_py("scripts/lib/route.py", "pygzip HELLO.gz")
    if "emperor-excavate" not in rout_pygzip:
        h.fail_msg("route.py pygzip → excavate")
    _, rout_gzipfile = h.run_py("scripts/lib/route.py", "gzipfile HELLO.gz")
    if "emperor-excavate" not in rout_gzipfile:
        h.fail_msg("route.py gzipfile → excavate")
    _, rout_hello_gz = h.run_py("scripts/lib/route.py", "hello.gz")
    if "emperor-excavate" not in rout_hello_gz:
        h.fail_msg("route.py hello.gz → excavate")
    if not _m(".gz", "hello.gz"):
        h.fail_msg("route matches(.gz, hello.gz) must be True")
    if _m(".gz", "hello.gzfoo"):
        h.fail_msg("route matches(.gz, hello.gzfoo) must be False after extension-boundary")
    _, rout_targz = h.run_py("scripts/lib/route.py", "targz HELLO.tar.gz")
    if "emperor-excavate" not in rout_targz:
        h.fail_msg("route.py targz → excavate")
    _, rout_tarball = h.run_py("scripts/lib/route.py", "tarball HELLO.tar.gz")
    if "emperor-excavate" not in rout_tarball:
        h.fail_msg("route.py tarball → excavate")
    _, rout_pytargz = h.run_py("scripts/lib/route.py", "pytargz HELLO.tar.gz")
    if "emperor-excavate" not in rout_pytargz:
        h.fail_msg("route.py pytargz → excavate")
    _, rout_hello_targz = h.run_py("scripts/lib/route.py", "hello.tar.gz")
    if "emperor-excavate" not in rout_hello_targz:
        h.fail_msg("route.py hello.tar.gz → excavate")
    _, rout_hello_tgz = h.run_py("scripts/lib/route.py", "hello.tgz")
    if "emperor-excavate" not in rout_hello_tgz:
        h.fail_msg("route.py hello.tgz → excavate")
    _, rout_hello_tbz2 = h.run_py("scripts/lib/route.py", "hello.tar.bz2")
    if "emperor-excavate" not in rout_hello_tbz2:
        h.fail_msg("route.py hello.tar.bz2 → excavate")
    _, rout_hello_txz = h.run_py("scripts/lib/route.py", "hello.tar.xz")
    if "emperor-excavate" not in rout_hello_txz:
        h.fail_msg("route.py hello.tar.xz → excavate")
    if not _m(".tar.gz", "hello.tar.gz"):
        h.fail_msg("route matches(.tar.gz, hello.tar.gz) must be True")
    if _m(".tar.gz", "hello.tar.gzfoo"):
        h.fail_msg("route matches(.tar.gz, hello.tar.gzfoo) must be False after extension-boundary")
    if not _m(".tgz", "hello.tgz"):
        h.fail_msg("route matches(.tgz, hello.tgz) must be True")
    if _m(".tgz", "hello.tgzfoo"):
        h.fail_msg("route matches(.tgz, hello.tgzfoo) must be False after extension-boundary")
    _, rout_whl = h.run_py("scripts/lib/route.py", "whl HELLO.whl")
    if "emperor-excavate" not in rout_whl:
        h.fail_msg("route.py whl → excavate")
    _, rout_pywhl = h.run_py("scripts/lib/route.py", "pywhl HELLO.whl")
    if "emperor-excavate" not in rout_pywhl:
        h.fail_msg("route.py pywhl → excavate")
    _, rout_wheel = h.run_py("scripts/lib/route.py", "wheel HELLO.whl")
    if "emperor-excavate" not in rout_wheel:
        h.fail_msg("route.py wheel → excavate")
    _, rout_hello_whl = h.run_py("scripts/lib/route.py", "hello.whl")
    if "emperor-excavate" not in rout_hello_whl:
        h.fail_msg("route.py hello.whl → excavate")
    if not _m(".whl", "hello.whl"):
        h.fail_msg("route matches(.whl, hello.whl) must be True")
    if _m(".whl", "hello.whlfoo"):
        h.fail_msg("route matches(.whl, hello.whlfoo) must be False after extension-boundary")
    _, rout_jar = h.run_py("scripts/lib/route.py", "jar HELLO.jar")
    if "emperor-excavate" not in rout_jar:
        h.fail_msg("route.py jar → excavate")
    _, rout_pyjar = h.run_py("scripts/lib/route.py", "pyjar HELLO.jar")
    if "emperor-excavate" not in rout_pyjar:
        h.fail_msg("route.py pyjar → excavate")
    _, rout_java_archive = h.run_py("scripts/lib/route.py", "java-archive HELLO.jar")
    if "emperor-excavate" not in rout_java_archive:
        h.fail_msg("route.py java-archive → excavate")
    _, rout_hello_jar = h.run_py("scripts/lib/route.py", "hello.jar")
    if "emperor-excavate" not in rout_hello_jar:
        h.fail_msg("route.py hello.jar → excavate")
    if not _m(".jar", "hello.jar"):
        h.fail_msg("route matches(.jar, hello.jar) must be True")
    if _m(".jar", "hello.jarfoo"):
        h.fail_msg("route matches(.jar, hello.jarfoo) must be False after extension-boundary")
    _, rout_war = h.run_py("scripts/lib/route.py", "war HELLO.war")
    if "emperor-excavate" not in rout_war:
        h.fail_msg("route.py war → excavate")
    _, rout_pywar = h.run_py("scripts/lib/route.py", "pywar HELLO.war")
    if "emperor-excavate" not in rout_pywar:
        h.fail_msg("route.py pywar → excavate")
    _, rout_web_archive = h.run_py("scripts/lib/route.py", "web-archive HELLO.war")
    if "emperor-excavate" not in rout_web_archive:
        h.fail_msg("route.py web-archive → excavate")
    _, rout_hello_war = h.run_py("scripts/lib/route.py", "hello.war")
    if "emperor-excavate" not in rout_hello_war:
        h.fail_msg("route.py hello.war → excavate")
    if not _m(".war", "hello.war"):
        h.fail_msg("route matches(.war, hello.war) must be True")
    if _m(".war", "hello.warfoo"):
        h.fail_msg("route matches(.war, hello.warfoo) must be False after extension-boundary")
    _, rout_apk = h.run_py("scripts/lib/route.py", "apk HELLO.apk")
    if "emperor-excavate" not in rout_apk:
        h.fail_msg("route.py apk → excavate")
    _, rout_pyapk = h.run_py("scripts/lib/route.py", "pyapk HELLO.apk")
    if "emperor-excavate" not in rout_pyapk:
        h.fail_msg("route.py pyapk → excavate")
    _, rout_android_package = h.run_py("scripts/lib/route.py", "android-package HELLO.apk")
    if "emperor-excavate" not in rout_android_package:
        h.fail_msg("route.py android-package → excavate")
    _, rout_hello_apk = h.run_py("scripts/lib/route.py", "hello.apk")
    if "emperor-excavate" not in rout_hello_apk:
        h.fail_msg("route.py hello.apk → excavate")
    if not _m(".apk", "hello.apk"):
        h.fail_msg("route matches(.apk, hello.apk) must be True")
    if _m(".apk", "hello.apkfoo"):
        h.fail_msg("route matches(.apk, hello.apkfoo) must be False after extension-boundary")
    _, rout_docx = h.run_py("scripts/lib/route.py", "docx HELLO.docx")
    if "emperor-excavate" not in rout_docx:
        h.fail_msg("route.py docx → excavate")
    _, rout_pydocx = h.run_py("scripts/lib/route.py", "pydocx HELLO.docx")
    if "emperor-excavate" not in rout_pydocx:
        h.fail_msg("route.py pydocx → excavate")
    _, rout_ooxml_word = h.run_py("scripts/lib/route.py", "ooxml-word HELLO.docx")
    if "emperor-excavate" not in rout_ooxml_word:
        h.fail_msg("route.py ooxml-word → excavate")
    _, rout_hello_docx = h.run_py("scripts/lib/route.py", "hello.docx")
    if "emperor-excavate" not in rout_hello_docx:
        h.fail_msg("route.py hello.docx → excavate")
    if not _m(".docx", "hello.docx"):
        h.fail_msg("route matches(.docx, hello.docx) must be True")
    if _m(".docx", "hello.docxfoo"):
        h.fail_msg("route matches(.docx, hello.docxfoo) must be False after extension-boundary")
    _, rout_xlsx = h.run_py("scripts/lib/route.py", "xlsx HELLO.xlsx")
    if "emperor-excavate" not in rout_xlsx:
        h.fail_msg("route.py xlsx → excavate")
    _, rout_pyxlsx = h.run_py("scripts/lib/route.py", "pyxlsx HELLO.xlsx")
    if "emperor-excavate" not in rout_pyxlsx:
        h.fail_msg("route.py pyxlsx → excavate")
    _, rout_ooxml_excel = h.run_py("scripts/lib/route.py", "ooxml-excel HELLO.xlsx")
    if "emperor-excavate" not in rout_ooxml_excel:
        h.fail_msg("route.py ooxml-excel → excavate")
    _, rout_hello_xlsx = h.run_py("scripts/lib/route.py", "hello.xlsx")
    if "emperor-excavate" not in rout_hello_xlsx:
        h.fail_msg("route.py hello.xlsx → excavate")
    if not _m(".xlsx", "hello.xlsx"):
        h.fail_msg("route matches(.xlsx, hello.xlsx) must be True")
    if _m(".xlsx", "hello.xlsxfoo"):
        h.fail_msg("route matches(.xlsx, hello.xlsxfoo) must be False after extension-boundary")
    _, rout_tsv = h.run_py("scripts/lib/route.py", "tsv HELLO.tsv")
    if "emperor-excavate" not in rout_tsv:
        h.fail_msg("route.py tsv → excavate")
    _, rout_pytsv = h.run_py("scripts/lib/route.py", "pytsv HELLO.tsv")
    if "emperor-excavate" not in rout_pytsv:
        h.fail_msg("route.py pytsv → excavate")
    _, rout_tab_separated = h.run_py("scripts/lib/route.py", "tab-separated HELLO.tsv")
    if "emperor-excavate" not in rout_tab_separated:
        h.fail_msg("route.py tab-separated → excavate")
    _, rout_hello_tsv = h.run_py("scripts/lib/route.py", "hello.tsv")
    if "emperor-excavate" not in rout_hello_tsv:
        h.fail_msg("route.py hello.tsv → excavate")
    if not _m(".tsv", "hello.tsv"):
        h.fail_msg("route matches(.tsv, hello.tsv) must be True")
    if _m(".tsv", "hello.tsvfoo"):
        h.fail_msg("route matches(.tsv, hello.tsvfoo) must be False after extension-boundary")
    _, rout_jsonl = h.run_py("scripts/lib/route.py", "jsonl HELLO.jsonl")
    if "emperor-excavate" not in rout_jsonl:
        h.fail_msg("route.py jsonl → excavate")
    _, rout_pyjsonl = h.run_py("scripts/lib/route.py", "pyjsonl HELLO.jsonl")
    if "emperor-excavate" not in rout_pyjsonl:
        h.fail_msg("route.py pyjsonl → excavate")
    _, rout_ndjson = h.run_py("scripts/lib/route.py", "ndjson HELLO.jsonl")
    if "emperor-excavate" not in rout_ndjson:
        h.fail_msg("route.py ndjson → excavate")
    _, rout_hello_jsonl = h.run_py("scripts/lib/route.py", "hello.jsonl")
    if "emperor-excavate" not in rout_hello_jsonl:
        h.fail_msg("route.py hello.jsonl → excavate")
    if not _m(".jsonl", "hello.jsonl"):
        h.fail_msg("route matches(.jsonl, hello.jsonl) must be True")
    if _m(".jsonl", "hello.jsonlfoo"):
        h.fail_msg("route matches(.jsonl, hello.jsonlfoo) must be False after extension-boundary")
    if _m(".json", "hello.jsonl"):
        h.fail_msg("route matches(.json, hello.jsonl) must be False (json leaf must not steal .jsonl)")
    _, rout_pptx = h.run_py("scripts/lib/route.py", "pptx HELLO.pptx")
    if "emperor-excavate" not in rout_pptx:
        h.fail_msg("route.py pptx → excavate")
    _, rout_pypptx = h.run_py("scripts/lib/route.py", "pypptx HELLO.pptx")
    if "emperor-excavate" not in rout_pypptx:
        h.fail_msg("route.py pypptx → excavate")
    _, rout_ooxml_pptx = h.run_py("scripts/lib/route.py", "ooxml-pptx HELLO.pptx")
    if "emperor-excavate" not in rout_ooxml_pptx:
        h.fail_msg("route.py ooxml-pptx → excavate")
    _, rout_hello_pptx = h.run_py("scripts/lib/route.py", "hello.pptx")
    if "emperor-excavate" not in rout_hello_pptx:
        h.fail_msg("route.py hello.pptx → excavate")
    if not _m(".pptx", "hello.pptx"):
        h.fail_msg("route matches(.pptx, hello.pptx) must be True")
    if _m(".pptx", "hello.pptxfoo"):
        h.fail_msg("route matches(.pptx, hello.pptxfoo) must be False after extension-boundary")
    if _m(".zip", "hello.pptx"):
        h.fail_msg("route matches(.zip, hello.pptx) must be False (zip leaf must not steal .pptx)")
    if _m(".docx", "hello.pptx"):
        h.fail_msg("route matches(.docx, hello.pptx) must be False (docx leaf must not steal .pptx)")
    if _m(".xlsx", "hello.pptx"):
        h.fail_msg("route matches(.xlsx, hello.pptx) must be False (xlsx leaf must not steal .pptx)")
    _, rout_pdf = h.run_py("scripts/lib/route.py", "pdf HELLO.pdf")
    if "emperor-excavate" not in rout_pdf:
        h.fail_msg("route.py pdf → excavate")
    _, rout_pdftotext = h.run_py("scripts/lib/route.py", "pdftotext HELLO.pdf")
    if "emperor-excavate" not in rout_pdftotext:
        h.fail_msg("route.py pdftotext → excavate")
    _, rout_poppler = h.run_py("scripts/lib/route.py", "poppler HELLO.pdf")
    if "emperor-excavate" not in rout_poppler:
        h.fail_msg("route.py poppler → excavate")
    _, rout_hello_pdf = h.run_py("scripts/lib/route.py", "hello.pdf")
    if "emperor-excavate" not in rout_hello_pdf:
        h.fail_msg("route.py hello.pdf → excavate")
    if not _m(".pdf", "hello.pdf"):
        h.fail_msg("route matches(.pdf, hello.pdf) must be True")
    if _m(".pdf", "hello.pdffoo"):
        h.fail_msg("route matches(.pdf, hello.pdffoo) must be False after extension-boundary")
    if _m(".ps", "hello.pdf"):
        h.fail_msg("route matches(.ps, hello.pdf) must be False (ps leaf must not steal .pdf)")
    if _m(".pptx", "hello.pdf"):
        h.fail_msg("route matches(.pptx, hello.pdf) must be False (pptx leaf must not steal .pdf)")
    if _m(".docx", "hello.pdf"):
        h.fail_msg("route matches(.docx, hello.pdf) must be False (docx leaf must not steal .pdf)")
    _, rout_png = h.run_py("scripts/lib/route.py", "png HELLO.png")
    if "emperor-excavate" not in rout_png:
        h.fail_msg("route.py png → excavate")
    _, rout_pillow = h.run_py("scripts/lib/route.py", "pillow HELLO.png")
    if "emperor-excavate" not in rout_pillow:
        h.fail_msg("route.py pillow → excavate")
    _, rout_pil = h.run_py("scripts/lib/route.py", "pil HELLO.png")
    if "emperor-excavate" not in rout_pil:
        h.fail_msg("route.py pil → excavate")
    _, rout_hello_png = h.run_py("scripts/lib/route.py", "hello.png")
    if "emperor-excavate" not in rout_hello_png:
        h.fail_msg("route.py hello.png → excavate")
    if not _m(".png", "hello.png"):
        h.fail_msg("route matches(.png, hello.png) must be True")
    if _m(".png", "hello.pngfoo"):
        h.fail_msg("route matches(.png, hello.pngfoo) must be False after extension-boundary")
    if _m(".pdf", "hello.png"):
        h.fail_msg("route matches(.pdf, hello.png) must be False (pdf leaf must not steal .png)")
    if _m(".ps", "hello.png"):
        h.fail_msg("route matches(.ps, hello.png) must be False (ps leaf must not steal .png)")
    if _m(".pptx", "hello.png"):
        h.fail_msg("route matches(.pptx, hello.png) must be False (pptx leaf must not steal .png)")
    _, rout_wav = h.run_py("scripts/lib/route.py", "wav HELLO.wav")
    if "emperor-excavate" not in rout_wav:
        h.fail_msg("route.py wav → excavate")
    _, rout_ffmpeg = h.run_py("scripts/lib/route.py", "ffmpeg HELLO.wav")
    if "emperor-excavate" not in rout_ffmpeg:
        h.fail_msg("route.py ffmpeg → excavate")
    _, rout_ffprobe = h.run_py("scripts/lib/route.py", "ffprobe HELLO.wav")
    if "emperor-excavate" not in rout_ffprobe:
        h.fail_msg("route.py ffprobe → excavate")
    _, rout_hello_wav = h.run_py("scripts/lib/route.py", "hello.wav")
    if "emperor-excavate" not in rout_hello_wav:
        h.fail_msg("route.py hello.wav → excavate")
    if not _m(".wav", "hello.wav"):
        h.fail_msg("route matches(.wav, hello.wav) must be True")
    if _m(".wav", "hello.wavfoo"):
        h.fail_msg("route matches(.wav, hello.wavfoo) must be False after extension-boundary")
    if _m(".png", "hello.wav"):
        h.fail_msg("route matches(.png, hello.wav) must be False (png leaf must not steal .wav)")
    if _m(".pdf", "hello.wav"):
        h.fail_msg("route matches(.pdf, hello.wav) must be False (pdf leaf must not steal .wav)")
    if _m(".ps", "hello.wav"):
        h.fail_msg("route matches(.ps, hello.wav) must be False (ps leaf must not steal .wav)")
    if _m(".pptx", "hello.wav"):
        h.fail_msg("route matches(.pptx, hello.wav) must be False (pptx leaf must not steal .wav)")
    # bare .l must not be enough alone when colliding; .lisp already routes via .lisp
    _, rout_regina = h.run_py("scripts/lib/route.py", "regina HELLO.REX")
    if "emperor-excavate" not in rout_regina:
        h.fail_msg("route.py regina → excavate")
    rc, _ = h.run_py("scripts/lib/route.py", "what is 2+2")
    if rc == 0:
        h.fail_msg("route.py should miss trivia")
    else:
        h.pass_msg("route.py misses trivia + fortran/vhdl/ada/forth/lisp/prolog/tcl/erlang/rexx/modula/algol/algol60/algolw/icon/oberon/snobol/simula/apl/bcpl/pli/st/ps/bas/scm/awk/sed/m4/ed/make/dc/lex/yacc/roff/perl/bc/expect/lua/ruby/go/rust/c/js/py/ts/bash/php/sql/jq/xslt/xml excavate + thin twins")

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

    # subagent-driven
    h.section("subagent-driven / subagent HARD-GATE leaf")
    h.need("skills/emperor-build/subagent-driven-checklist.md")
    h.need("scripts/lib/subagent.py")
    h.need("scripts/subagent.sh")
    h.need("scripts/subagent.ps1")
    h.bash_n("scripts/subagent.sh", "subagent.sh syntax")
    h.py_compile("scripts/lib/subagent.py", "subagent.py compile")
    h.require_contains("subagent.py", "scripts/subagent.sh", "subagent.sh does not call subagent.py")
    h.require_contains("subagent.py", "scripts/subagent.ps1", "subagent.ps1 does not call subagent.py")
    h.require_contains("subagent|", "scripts/emperor", "emperor bash missing subagent")
    h.require_contains("'subagent'", "scripts/emperor.ps1", "emperor.ps1 missing subagent")
    h.require_contains(
        "subagent-driven-checklist.md",
        "skills/emperor-build/SKILL.md",
        "emperor-build missing subagent-driven leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-build/subagent-driven-checklist.md",
        "subagent leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "subagent-driven-development",
        "skills/emperor-build/subagent-driven-checklist.md",
        "subagent leaf missing source skill",
    )
    _, sub_out = h.run_py("scripts/lib/subagent.py")
    if not re.search(r"^SUBAGENT checklist=yes", sub_out, re.M):
        h.fail_msg("subagent missing checklist=yes")
    if not re.search(r"^STEP 1 ", sub_out, re.M):
        h.fail_msg("subagent missing STEP 1")
    if not re.search(r"^STEP 6 ", sub_out, re.M):
        h.fail_msg("subagent missing STEP 6")
    if not re.search(r"^MUST:", sub_out, re.M):
        h.fail_msg("subagent missing MUST line")
    if "FRESH_SUBAGENT_PER_TASK_REVIEW_AFTER_EACH" not in sub_out:
        h.fail_msg("subagent missing iron law token")
    rc, _ = h.run_py("scripts/lib/subagent.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("subagent should reject step skip 1→3")
    else:
        h.pass_msg("subagent rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/subagent.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("subagent 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/subagent.py", "--reject-skip-review")
    if rc == 0:
        h.fail_msg("subagent --reject-skip-review should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/subagent.py", "--reject-skip-review")
        if not re.search(r"^REJECT SKIP-REVIEW:", reject, re.M):
            h.fail_msg("reject-skip-review missing REJECT line")
        else:
            h.pass_msg("subagent --reject-skip-review hard-gates skip review")
    _, sub_sh = h.run_sh("scripts/subagent.sh")
    if not re.search(r"^SUBAGENT checklist=yes", sub_sh, re.M):
        h.fail_msg("subagent.sh missing checklist card")



    # parallel-dispatch
    h.section("dispatching-parallel-agents / parallel HARD-GATE leaf")
    h.need("skills/emperor-dispatch/parallel-dispatch-checklist.md")
    h.need("scripts/lib/parallel.py")
    h.need("scripts/parallel.sh")
    h.need("scripts/parallel.ps1")
    h.bash_n("scripts/parallel.sh", "parallel.sh syntax")
    h.py_compile("scripts/lib/parallel.py", "parallel.py compile")
    h.require_contains("parallel.py", "scripts/parallel.sh", "parallel.sh does not call parallel.py")
    h.require_contains("parallel.py", "scripts/parallel.ps1", "parallel.ps1 does not call parallel.py")
    h.require_contains("parallel|", "scripts/emperor", "emperor bash missing parallel")
    h.require_contains("'parallel'", "scripts/emperor.ps1", "emperor.ps1 missing parallel")
    h.require_contains(
        "parallel-dispatch-checklist.md",
        "skills/emperor-dispatch/SKILL.md",
        "emperor-dispatch missing parallel-dispatch leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-dispatch/parallel-dispatch-checklist.md",
        "parallel leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "dispatching-parallel-agents",
        "skills/emperor-dispatch/parallel-dispatch-checklist.md",
        "parallel leaf missing source skill",
    )
    _, par_out = h.run_py("scripts/lib/parallel.py")
    if not re.search(r"^PARALLEL checklist=yes", par_out, re.M):
        h.fail_msg("parallel missing checklist=yes")
    if not re.search(r"^STEP 1 ", par_out, re.M):
        h.fail_msg("parallel missing STEP 1")
    if not re.search(r"^STEP 6 ", par_out, re.M):
        h.fail_msg("parallel missing STEP 6")
    if not re.search(r"^MUST:", par_out, re.M):
        h.fail_msg("parallel missing MUST line")
    if "ONE_AGENT_PER_INDEPENDENT_DOMAIN_NO_SHARED_WRITABLE" not in par_out:
        h.fail_msg("parallel missing iron law token")
    rc, _ = h.run_py("scripts/lib/parallel.py", "--advance", "1", "3")
    if rc == 0:
        h.fail_msg("parallel should reject step skip 1→3")
    else:
        h.pass_msg("parallel rejects skip 1→3")
    _, adv_ok = h.run_py("scripts/lib/parallel.py", "--advance", "2", "3")
    if not re.search(r"^ADVANCE OK", adv_ok, re.M):
        h.fail_msg("parallel 2→3 should OK")
    rc, _ = h.run_py("scripts/lib/parallel.py", "--reject-shared-scope")
    if rc == 0:
        h.fail_msg("parallel --reject-shared-scope should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/parallel.py", "--reject-shared-scope")
        if not re.search(r"^REJECT SHARED-SCOPE:", reject, re.M):
            h.fail_msg("reject-shared-scope missing REJECT line")
        else:
            h.pass_msg("parallel --reject-shared-scope hard-gates shared scope")
    _, par_sh = h.run_sh("scripts/parallel.sh")
    if not re.search(r"^PARALLEL checklist=yes", par_sh, re.M):
        h.fail_msg("parallel.sh missing checklist card")


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

    # ---- install.py harness deploy ----
    h.section("install.py Python core")
    h.need("scripts/lib/install.py")
    h.need("scripts/install.sh")
    h.need("scripts/install.ps1")
    h.bash_n("scripts/install.sh", "install.sh syntax")
    h.py_compile("scripts/lib/install.py", "install.py compile")
    h.require_contains(
        "lib/install.py",
        "scripts/install.sh",
        "install.sh thin twin missing install.py",
    )
    h.require_contains(
        "lib/install.py",
        "scripts/install.ps1",
        "install.ps1 thin twin missing install.py",
    )
    h.require_contains("install|", "scripts/emperor", "emperor bash missing install")
    h.require_contains("'install'", "scripts/emperor.ps1", "emperor.ps1 missing install")
    for harness in (
        "claude-code",
        "kimi",
        "codex",
        "opencode",
        "generic-agents",
    ):
        h.require_contains(
            harness,
            "scripts/lib/install.py",
            f"install.py missing harness {harness}",
        )
    rc, dry = h.run_py(
        "scripts/lib/install.py", "claude-code", "user", "--dry-run"
    )
    if rc != 0:
        h.fail_msg("install.py --dry-run should exit 0")
    if "=== EMPEROR TIME :: install ===" not in dry:
        h.fail_msg("install.py dry-run missing banner")
    if "(dry run - nothing copied)" not in dry:
        h.fail_msg("install.py dry-run missing dry marker")
    if "target :" not in dry:
        h.fail_msg("install.py dry-run missing target")
    rc2, dry2 = h.run_sh(
        "scripts/install.sh", "opencode", "user", "--dry-run"
    )
    if rc2 != 0 or "(dry run - nothing copied)" not in dry2:
        h.fail_msg("install.sh --dry-run should match python core")
    else:
        h.pass_msg("install.sh dry-run parity")
    rc3, err = h.run_py("scripts/lib/install.py", "nope-harness", "--dry-run")
    # argparse choices → exit 2 typically via SystemExit from parse_args
    if rc3 == 0:
        h.fail_msg("install.py unknown harness should fail")
    else:
        h.pass_msg("install.py rejects unknown harness")
    rc4, out4 = h.run_py(
        "scripts/lib/install.py",
        "generic-agents",
        "user",
        "--with-chain-skills",
        "--dry-run",
    )
    if rc4 != 0 or "chain  :" not in out4 or "planned" not in out4:
        h.fail_msg("install.py --with-chain-skills dry-run should list planned chains")
    else:
        h.pass_msg("install.py with-chain-skills dry-run lists chains")
    h.require_contains(
        "scripts/emperor dowse",
        "scripts/lib/install.py",
        "install.py missing host-agnostic dowse tip",
    )
    h.pass_msg("install.py thin twins + dry-run + harness map")

    # ---- boot.py / host.py silent-boot ----
    h.section("boot.py + host.py Python core")
    h.need("scripts/lib/host.py")
    h.need("scripts/lib/boot.py")
    h.need("scripts/boot.sh")
    h.need("scripts/boot.ps1")
    h.bash_n("scripts/boot.sh", "boot.sh syntax")
    h.py_compile("scripts/lib/host.py", "host.py compile")
    h.py_compile("scripts/lib/boot.py", "boot.py compile")
    h.require_contains(
        "lib/boot.py",
        "scripts/boot.sh",
        "boot.sh thin twin missing boot.py",
    )
    h.require_contains(
        "lib/boot.py",
        "scripts/boot.ps1",
        "boot.ps1 thin twin missing boot.py",
    )
    boot_sh_lines = len(h.read("scripts/boot.sh").splitlines())
    boot_ps1_lines = len(h.read("scripts/boot.ps1").splitlines())
    if boot_sh_lines > 20:
        h.fail_msg("boot.sh should be thin twin (<=20 lines)")
    if boot_ps1_lines > 30:
        h.fail_msg("boot.ps1 should be thin twin (<=30 lines)")
    h.require_contains(
        "host.py",
        "scripts/lib/host.sh",
        "host.sh emperor_host_report missing host.py delegate",
    )
    rc, report = h.run_py("scripts/lib/host.py", "--report")
    if rc != 0:
        h.fail_msg("host.py --report should exit 0")
    for key in ("os=", "shell=", "wsl=", "win_interop=", "encoding="):
        if key not in report:
            h.fail_msg(f"host.py report missing {key}")
            break
    else:
        h.pass_msg("host.py report keys")
    rcj, jout = h.run_py("scripts/lib/host.py", "--as-json")
    if rcj != 0 or '"os"' not in jout or '"shell"' not in jout:
        h.fail_msg("host.py --as-json should emit os/shell")
    else:
        h.pass_msg("host.py --as-json")
    with tempfile.TemporaryDirectory(prefix="et-boot-") as tmp:
        rc_b, _ = h.run_py(
            "scripts/lib/boot.py",
            "--root",
            tmp,
            "--skip-eval",
        )
        host_env = Path(tmp) / ".emperor" / "host.env"
        survey = Path(tmp) / ".emperor" / "survey.md"
        if rc_b != 0:
            h.fail_msg("boot.py --skip-eval should exit 0")
        elif not host_env.is_file():
            h.fail_msg("boot.py should write .emperor/host.env")
        elif "os=" not in host_env.read_text(encoding="utf-8"):
            h.fail_msg("boot.py host.env missing os=")
        elif not survey.is_file():
            h.fail_msg("boot.py should write .emperor/survey.md")
        else:
            h.pass_msg("boot.py writes host.env + survey.md")
    rc_sh, _ = h.run_sh(
        "scripts/boot.sh",
        "--skip-eval",
        "--root",
        str(root),
        env={"EMPEROR_BOOT_SKIP_EVAL": "1"},
    )
    # boot.sh always exits 0; just ensure it runs
    if rc_sh != 0:
        h.fail_msg("boot.sh --skip-eval should exit 0")
    else:
        h.pass_msg("boot.sh thin twin runs")
    h.pass_msg("boot.py + host.py thin twins + report + smoke")


    # ---- worktree.py create helper ----
    h.section("worktree.py Python core")
    h.need("scripts/lib/worktree.py")
    h.need("scripts/worktree.sh")
    h.need("scripts/worktree.ps1")
    h.bash_n("scripts/worktree.sh", "worktree.sh syntax")
    h.py_compile("scripts/lib/worktree.py", "worktree.py compile")
    h.require_contains(
        "lib/worktree.py",
        "scripts/worktree.sh",
        "worktree.sh thin twin missing worktree.py",
    )
    h.require_contains(
        "lib/worktree.py",
        "scripts/worktree.ps1",
        "worktree.ps1 thin twin missing worktree.py",
    )
    wt_sh_lines = len(h.read("scripts/worktree.sh").splitlines())
    wt_ps1_lines = len(h.read("scripts/worktree.ps1").splitlines())
    if wt_sh_lines > 20:
        h.fail_msg("worktree.sh should be thin twin (<=20 lines)")
    if wt_ps1_lines > 30:
        h.fail_msg("worktree.ps1 should be thin twin (<=30 lines)")
    rc_u, out_u = h.run_py("scripts/lib/worktree.py")
    if rc_u != 2 or "usage:" not in out_u:
        h.fail_msg("worktree.py missing id should exit 2 with usage")
    else:
        h.pass_msg("worktree.py usage refuse")
    with tempfile.TemporaryDirectory(prefix="et-wt-nongit-") as tmp:
        rc_ng, out_ng = h.run_py(
            "scripts/lib/worktree.py", "x", "--cwd", tmp
        )
        if rc_ng != 1 or "WORKTREE FAIL" not in out_ng:
            h.fail_msg("worktree.py non-git cwd should exit 1")
        else:
            h.pass_msg("worktree.py not-a-repo refuse")
    with tempfile.TemporaryDirectory(prefix="et-wt-") as tmp:
        for cmd in (
            ["git", "init", "-q"],
            ["git", "config", "user.email", "et@test"],
            ["git", "config", "user.name", "et"],
        ):
            rc_g, _ = h.run(cmd, cwd=tmp)
            if rc_g != 0:
                h.fail_msg(f"worktree smoke git setup failed: {cmd}")
                break
        else:
            (Path(tmp) / "f").write_text("x\n", encoding="utf-8")
            rc_a, _ = h.run(["git", "add", "f"], cwd=tmp)
            rc_c, _ = h.run(["git", "commit", "-qm", "init"], cwd=tmp)
            if rc_a != 0 or rc_c != 0:
                h.fail_msg("worktree smoke commit failed")
            else:
                rc1, out1 = h.run_py(
                    "scripts/lib/worktree.py", "t1", "--cwd", tmp
                )
                if rc1 != 0 or "WORKTREE: .worktrees/t1" not in out1:
                    h.fail_msg("worktree.py create smoke failed")
                elif not (Path(tmp) / ".worktrees" / "t1").is_dir():
                    h.fail_msg("worktree.py did not create .worktrees/t1")
                else:
                    rc2, out2 = h.run_py(
                        "scripts/lib/worktree.py", "t1", "--cwd", tmp
                    )
                    if rc2 != 0 or "WORKTREE EXISTS:" not in out2:
                        h.fail_msg("worktree.py EXISTS short-circuit failed")
                    else:
                        h.pass_msg("worktree.py create + EXISTS smoke")
    h.pass_msg("worktree.py thin twins + create helper")

    # ---- excavate thin alias → identify.py ----
    h.section("excavate thin alias → identify.py")
    h.need("scripts/excavate.sh")
    h.need("scripts/excavate.ps1")
    h.bash_n("scripts/excavate.sh", "excavate.sh syntax")
    h.require_contains(
        "lib/identify.py",
        "scripts/excavate.sh",
        "excavate.sh thin alias missing identify.py",
    )
    h.require_contains(
        "lib/identify.py",
        "scripts/excavate.ps1",
        "excavate.ps1 thin alias missing identify.py",
    )
    ex_sh = h.read("scripts/excavate.sh")
    ex_ps1 = h.read("scripts/excavate.ps1")
    # Refuse live hops (exec/call), not doc comments naming the old path.
    if re.search(r"(exec\s+bash\s+.*identify\.sh|\$ROOT/identify\.sh)", ex_sh):
        h.fail_msg("excavate.sh must not hop through identify.sh")
    if re.search(r"(identify\.ps1['\"]|Join-Path.*identify\.ps1)", ex_ps1):
        h.fail_msg("excavate.ps1 must not hop through identify.ps1")
    ex_sh_lines = len(ex_sh.splitlines())
    ex_ps1_lines = len(ex_ps1.splitlines())
    if ex_sh_lines > 20:
        h.fail_msg("excavate.sh should be thin alias (<=20 lines)")
    if ex_ps1_lines > 40:
        h.fail_msg("excavate.ps1 should be thin alias (<=40 lines)")
    fixture = str(root / "evals/fixtures/lost-pas")
    rc_i, out_i = h.run_py("scripts/lib/identify.py", fixture)
    rc_e, out_e = h.run_sh("scripts/excavate.sh", fixture)
    if rc_i != 0 or rc_e != 0:
        h.fail_msg("excavate/identify smoke non-zero exit")
    elif "== identify" not in out_e:
        h.fail_msg("excavate.sh missing identify survey header")
    elif out_i.splitlines()[:1] != out_e.splitlines()[:1]:
        h.fail_msg("excavate.sh header drifted from identify.py")
    elif out_i != out_e:
        h.fail_msg("excavate.sh survey drifted from identify.py")
    else:
        h.pass_msg("excavate≡identify survey parity")
    h.pass_msg("excavate thin alias → identify.py")

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
    h.require_contains("lost-vhd", "evals/bakeoff.md", "bakeoff.md missing lost-vhd inventory")
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
    h.require_contains("install.py", "evals/bakeoff.md", "bakeoff.md missing install.py inventory")
    h.require_contains("install.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing install.py")
    h.require_contains("0.4.31", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.31 tip")
    h.require_contains("boot.py", "evals/bakeoff.md", "bakeoff.md missing boot.py inventory")
    h.require_contains("host.py", "evals/bakeoff.md", "bakeoff.md missing host.py inventory")
    h.require_contains("boot.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing boot.py")
    h.require_contains("0.4.32", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.32 tip")
    h.require_contains("worktree.py", "evals/bakeoff.md", "bakeoff.md missing worktree.py inventory")
    h.require_contains("worktree.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing worktree.py")
    h.require_contains("0.4.33", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.33 tip")
    h.require_contains("excavate thin", "evals/bakeoff.md", "bakeoff.md missing excavate thin alias inventory")
    h.require_contains("excavate", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing excavate")
    h.require_contains("0.4.34", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.34 tip")
    h.require_contains("lost-vhd", "evals/bakeoff.md", "bakeoff.md missing lost-vhd inventory")
    h.require_contains("archaeology-vhdl-manual.md", "SKILL.md", "SKILL.md missing vhdl Jail pin")
    h.require_contains("0.4.35", "CHANGELOG.md", "CHANGELOG missing 0.4.35")
    h.require_contains("session_discovery.py", "evals/bakeoff.md", "bakeoff.md missing session_discovery.py inventory")
    h.require_contains("session_discovery.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing session_discovery.py")
    h.require_contains("0.4.36", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.36 tip")
    h.require_contains("0.4.36", "CHANGELOG.md", "CHANGELOG missing 0.4.36")
    h.require_contains("diagnose.py", "evals/bakeoff.md", "bakeoff.md missing diagnose.py inventory")
    h.require_contains("diagnose.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing diagnose.py")
    h.require_contains("0.4.37", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.37 tip")
    h.require_contains("0.4.37", "CHANGELOG.md", "CHANGELOG missing 0.4.37")
    h.require_contains("lost-ada", "evals/bakeoff.md", "bakeoff.md missing lost-ada inventory")
    h.require_contains("archaeology-ada-manual.md", "SKILL.md", "SKILL.md missing ada Jail pin")
    h.require_contains("lost-fs", "evals/bakeoff.md", "bakeoff.md missing lost-fs inventory")
    h.require_contains("archaeology-forth-manual.md", "SKILL.md", "SKILL.md missing forth Jail pin")
    h.require_contains("lost-lisp", "evals/bakeoff.md", "bakeoff.md missing lost-lisp inventory")
    h.require_contains("archaeology-lisp-manual.md", "SKILL.md", "SKILL.md missing lisp Jail pin")
    h.require_contains("lost-prolog", "evals/bakeoff.md", "bakeoff.md missing lost-prolog inventory")
    h.require_contains("archaeology-prolog-manual.md", "SKILL.md", "SKILL.md missing prolog Jail pin")
    h.require_contains("lost-tcl", "evals/bakeoff.md", "bakeoff.md missing lost-tcl inventory")
    h.require_contains("archaeology-tcl-manual.md", "SKILL.md", "SKILL.md missing tcl Jail pin")
    h.require_contains("lost-erl", "evals/bakeoff.md", "bakeoff.md missing lost-erl inventory")
    h.require_contains("archaeology-erlang-manual.md", "SKILL.md", "SKILL.md missing erlang Jail pin")
    h.require_contains("lost-rex", "evals/bakeoff.md", "bakeoff.md missing lost-rex inventory")
    h.require_contains("archaeology-rexx-manual.md", "SKILL.md", "SKILL.md missing rexx Jail pin")
    h.require_contains("lost-mod", "evals/bakeoff.md", "bakeoff.md missing lost-mod inventory")
    h.require_contains("archaeology-modula2-manual.md", "SKILL.md", "SKILL.md missing modula2 Jail pin")
    h.require_contains("lost-a68", "evals/bakeoff.md", "bakeoff.md missing lost-a68 inventory")
    h.require_contains("archaeology-algol68-manual.md", "SKILL.md", "SKILL.md missing algol68 Jail pin")
    h.require_contains("lost-a60", "evals/bakeoff.md", "bakeoff.md missing lost-a60 inventory")
    h.require_contains("archaeology-algol60-manual.md", "SKILL.md", "SKILL.md missing algol60 Jail pin")
    h.require_contains("lost-alw", "evals/bakeoff.md", "bakeoff.md missing lost-alw inventory")
    h.require_contains("archaeology-algolw-manual.md", "SKILL.md", "SKILL.md missing algolw Jail pin")
    h.require_contains("lost-icn", "evals/bakeoff.md", "bakeoff.md missing lost-icn inventory")
    h.require_contains("archaeology-icon-manual.md", "SKILL.md", "SKILL.md missing icon Jail pin")
    h.require_contains("lost-obn", "evals/bakeoff.md", "bakeoff.md missing lost-obn inventory")
    h.require_contains("archaeology-oberon-manual.md", "SKILL.md", "SKILL.md missing oberon Jail pin")
    h.require_contains("lost-sno", "evals/bakeoff.md", "bakeoff.md missing lost-sno inventory")
    h.require_contains("archaeology-snobol-manual.md", "SKILL.md", "SKILL.md missing snobol Jail pin")
    h.require_contains("lost-cim", "evals/bakeoff.md", "bakeoff.md missing lost-cim inventory")
    h.require_contains("archaeology-simula-manual.md", "SKILL.md", "SKILL.md missing simula Jail pin")
    h.require_contains("lost-apl", "evals/bakeoff.md", "bakeoff.md missing lost-apl inventory")
    h.require_contains("archaeology-apl-manual.md", "SKILL.md", "SKILL.md missing apl Jail pin")
    h.require_contains("lost-bcpl", "evals/bakeoff.md", "bakeoff.md missing lost-bcpl inventory")
    h.require_contains("archaeology-bcpl-manual.md", "SKILL.md", "SKILL.md missing bcpl Jail pin")
    h.require_contains("lost-pli", "evals/bakeoff.md", "bakeoff.md missing lost-pli inventory")
    h.require_contains("archaeology-pli-manual.md", "SKILL.md", "SKILL.md missing pli Jail pin")
    h.require_contains("lost-st", "evals/bakeoff.md", "bakeoff.md missing lost-st inventory")
    h.require_contains("archaeology-smalltalk-manual.md", "SKILL.md", "SKILL.md missing smalltalk Jail pin")
    h.require_contains("lost-ps", "evals/bakeoff.md", "bakeoff.md missing lost-ps inventory")
    h.require_contains("archaeology-postscript-manual.md", "SKILL.md", "SKILL.md missing postscript Jail pin")
    h.require_contains("lost-bas", "evals/bakeoff.md", "bakeoff.md missing lost-bas inventory")
    h.require_contains("archaeology-basic-manual.md", "SKILL.md", "SKILL.md missing basic Jail pin")
    h.require_contains("lost-scm", "evals/bakeoff.md", "bakeoff.md missing lost-scm inventory")
    h.require_contains("archaeology-scheme-manual.md", "SKILL.md", "SKILL.md missing scheme Jail pin")
    h.require_contains("lost-awk", "evals/bakeoff.md", "bakeoff.md missing lost-awk inventory")
    h.require_contains("archaeology-awk-manual.md", "SKILL.md", "SKILL.md missing awk Jail pin")
    h.require_contains("lost-sed", "evals/bakeoff.md", "bakeoff.md missing lost-sed inventory")
    h.require_contains("archaeology-sed-manual.md", "SKILL.md", "SKILL.md missing sed Jail pin")
    h.require_contains("lost-m4", "evals/bakeoff.md", "bakeoff.md missing lost-m4 inventory")
    h.require_contains("archaeology-m4-manual.md", "SKILL.md", "SKILL.md missing m4 Jail pin")
    h.require_contains("lost-ed", "evals/bakeoff.md", "bakeoff.md missing lost-ed inventory")
    h.require_contains("archaeology-ed-manual.md", "SKILL.md", "SKILL.md missing ed Jail pin")
    h.require_contains("lost-make", "evals/bakeoff.md", "bakeoff.md missing lost-make inventory")
    h.require_contains("archaeology-make-manual.md", "SKILL.md", "SKILL.md missing make Jail pin")
    h.require_contains("lost-dc", "evals/bakeoff.md", "bakeoff.md missing lost-dc inventory")
    h.require_contains("archaeology-dc-manual.md", "SKILL.md", "SKILL.md missing dc Jail pin")
    h.require_contains("lost-lex", "evals/bakeoff.md", "bakeoff.md missing lost-lex inventory")
    h.require_contains("archaeology-lex-manual.md", "SKILL.md", "SKILL.md missing lex Jail pin")
    h.require_contains("lost-yacc", "evals/bakeoff.md", "bakeoff.md missing lost-yacc inventory")
    h.require_contains("archaeology-yacc-manual.md", "SKILL.md", "SKILL.md missing yacc Jail pin")
    h.require_contains("lost-roff", "evals/bakeoff.md", "bakeoff.md missing lost-roff inventory")
    h.require_contains("archaeology-roff-manual.md", "SKILL.md", "SKILL.md missing roff Jail pin")
    h.require_contains("lost-pl", "evals/bakeoff.md", "bakeoff.md missing lost-pl inventory")
    h.require_contains("archaeology-perl-manual.md", "SKILL.md", "SKILL.md missing perl Jail pin")
    h.require_contains("lost-bc", "evals/bakeoff.md", "bakeoff.md missing lost-bc inventory")
    h.require_contains("archaeology-bc-manual.md", "SKILL.md", "SKILL.md missing bc Jail pin")
    h.require_contains("lost-expect", "evals/bakeoff.md", "bakeoff.md missing lost-expect inventory")
    h.require_contains("archaeology-expect-manual.md", "SKILL.md", "SKILL.md missing expect Jail pin")
    h.require_contains("lost-lua", "evals/bakeoff.md", "bakeoff.md missing lost-lua inventory")
    h.require_contains("archaeology-lua-manual.md", "SKILL.md", "SKILL.md missing lua Jail pin")
    h.require_contains("lost-ruby", "evals/bakeoff.md", "bakeoff.md missing lost-ruby inventory")
    h.require_contains("lost-go", "evals/bakeoff.md", "bakeoff.md missing lost-go inventory")
    h.require_contains("lost-rust", "evals/bakeoff.md", "bakeoff.md missing lost-rust inventory")
    h.require_contains("lost-c", "evals/bakeoff.md", "bakeoff.md missing lost-c inventory")
    h.require_contains("lost-js", "evals/bakeoff.md", "bakeoff.md missing lost-js inventory")
    h.require_contains("archaeology-ruby-manual.md", "SKILL.md", "SKILL.md missing ruby Jail pin")
    h.require_contains("archaeology-go-manual.md", "SKILL.md", "SKILL.md missing go Jail pin")
    h.require_contains("archaeology-rust-manual.md", "SKILL.md", "SKILL.md missing rust Jail pin")
    h.require_contains("archaeology-c-manual.md", "SKILL.md", "SKILL.md missing c Jail pin")
    h.require_contains("archaeology-js-manual.md", "SKILL.md", "SKILL.md missing js Jail pin")
    h.require_contains("0.4.38", "CHANGELOG.md", "CHANGELOG missing 0.4.38")
    h.require_contains("root_cause.py", "evals/bakeoff.md", "bakeoff.md missing root_cause.py inventory")
    h.require_contains("root_cause.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing root_cause.py")
    h.require_contains("0.4.39", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.39 tip")
    h.require_contains("lost-ada", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-ada")
    h.require_contains("lost-fs", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-fs")
    h.require_contains("lost-lisp", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-lisp")
    h.require_contains("lost-prolog", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-prolog")
    h.require_contains("lost-tcl", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-tcl")
    h.require_contains("lost-erl", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-erl")
    h.require_contains("lost-rex", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-rex")
    h.require_contains("lost-mod", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-mod")
    h.require_contains("lost-a68", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-a68")
    h.require_contains("lost-a60", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-a60")
    h.require_contains("lost-alw", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-alw")
    h.require_contains("lost-icn", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-icn")
    h.require_contains("lost-obn", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-obn")
    h.require_contains("lost-sno", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-sno")
    h.require_contains("lost-cim", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-cim")
    h.require_contains("lost-apl", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-apl")
    h.require_contains("lost-bcpl", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-bcpl")
    h.require_contains("lost-pli", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-pli")
    h.require_contains("lost-st", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-st")
    h.require_contains("lost-ps", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-ps")
    h.require_contains("lost-bas", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-bas")
    h.require_contains("lost-scm", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-scm")
    h.require_contains("lost-awk", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-awk")
    h.require_contains("lost-sed", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-sed")
    h.require_contains("lost-m4", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-m4")
    h.require_contains("lost-ed", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-ed")
    h.require_contains("lost-make", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-make")
    h.require_contains("lost-dc", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-dc")
    h.require_contains("lost-lex", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-lex")
    h.require_contains("lost-yacc", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-yacc")
    h.require_contains("lost-roff", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-roff")
    h.require_contains("lost-pl", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-pl")
    h.require_contains("lost-bc", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-bc")
    h.require_contains("lost-expect", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-expect")
    h.require_contains("lost-lua", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-lua")
    h.require_contains("lost-ruby", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-ruby")
    h.require_contains("lost-go", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-go")
    h.require_contains("lost-rust", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-rust")
    h.require_contains("lost-c", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-c")
    h.require_contains("lost-js", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing lost-js")
    h.require_contains("0.4.39", "CHANGELOG.md", "CHANGELOG missing 0.4.39")
    h.require_contains("defense.py", "evals/bakeoff.md", "bakeoff.md missing defense.py inventory")
    h.require_contains("defense.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing defense.py")
    h.require_contains("0.4.40", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.40 tip")
    h.require_contains("0.4.40", "CHANGELOG.md", "CHANGELOG missing 0.4.40")
    h.require_contains("condition_wait.py", "evals/bakeoff.md", "bakeoff.md missing condition_wait.py inventory")
    h.require_contains("condition_wait.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing condition_wait.py")
    h.require_contains("0.4.41", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.41 tip")
    h.require_contains("0.4.41", "CHANGELOG.md", "CHANGELOG missing 0.4.41")
    h.require_contains("polluter.py", "evals/bakeoff.md", "bakeoff.md missing polluter.py inventory")
    h.require_contains("polluter.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing polluter.py")
    h.require_contains("0.4.42", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.42 tip")
    h.require_contains("0.4.42", "CHANGELOG.md", "CHANGELOG missing 0.4.42")
    h.require_contains("pressure.py", "evals/bakeoff.md", "bakeoff.md missing pressure.py inventory")
    h.require_contains("pressure.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing pressure.py")
    h.require_contains("good_tests.py", "evals/bakeoff.md", "bakeoff.md missing good_tests.py inventory")
    h.require_contains("good_tests.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing good_tests.py")
    h.require_contains("skill_test.py", "evals/bakeoff.md", "bakeoff.md missing skill_test.py inventory")
    h.require_contains("skill_test.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing skill_test.py")
    h.require_contains("persuasion.py", "evals/bakeoff.md", "bakeoff.md missing persuasion.py inventory")
    h.require_contains("persuasion.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing persuasion.py")
    h.require_contains("sdo.py", "evals/bakeoff.md", "bakeoff.md missing sdo.py inventory")
    h.require_contains("sdo.py", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing sdo.py")
    h.require_contains("0.4.48", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.48 tip")
    h.require_contains("0.4.48", "CHANGELOG.md", "CHANGELOG missing 0.4.48")
    h.require_contains("0.4.49", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.49 tip")
    h.require_contains("0.4.49", "CHANGELOG.md", "CHANGELOG missing 0.4.49")
    h.require_contains("0.4.50", "CHANGELOG.md", "CHANGELOG missing 0.4.50")
    h.require_contains("0.4.51", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.51 tip")
    h.require_contains("0.4.51", "CHANGELOG.md", "CHANGELOG missing 0.4.51")
    h.require_contains("0.4.52", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.52 tip")
    h.require_contains("0.4.52", "CHANGELOG.md", "CHANGELOG missing 0.4.52")
    h.require_contains("0.4.53", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.53 tip")
    h.require_contains("0.4.53", "CHANGELOG.md", "CHANGELOG missing 0.4.53")
    h.require_contains("0.4.54", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.54 tip")
    h.require_contains("0.4.54", "CHANGELOG.md", "CHANGELOG missing 0.4.54")
    h.require_contains("0.4.55", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.55 tip")
    h.require_contains("0.4.55", "CHANGELOG.md", "CHANGELOG missing 0.4.55")
    h.require_contains("0.4.56", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.56 tip")
    h.require_contains("0.4.56", "CHANGELOG.md", "CHANGELOG missing 0.4.56")
    h.require_contains("0.4.57", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.57 tip")
    h.require_contains("0.4.57", "CHANGELOG.md", "CHANGELOG missing 0.4.57")
    h.require_contains("0.4.58", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.58 tip")
    h.require_contains("0.4.58", "CHANGELOG.md", "CHANGELOG missing 0.4.58")
    h.require_contains("0.4.59", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.59 tip")
    h.require_contains("0.4.59", "CHANGELOG.md", "CHANGELOG missing 0.4.59")
    h.require_contains("0.4.60", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.60 tip")
    h.require_contains("0.4.60", "CHANGELOG.md", "CHANGELOG missing 0.4.60")
    h.require_contains("0.4.61", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.61 tip")
    h.require_contains("0.4.61", "CHANGELOG.md", "CHANGELOG missing 0.4.61")
    h.require_contains("0.4.62", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.62 tip")
    h.require_contains("0.4.62", "CHANGELOG.md", "CHANGELOG missing 0.4.62")
    h.require_contains("0.4.63", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.63 tip")
    h.require_contains("0.4.63", "CHANGELOG.md", "CHANGELOG missing 0.4.63")
    h.require_contains("0.4.64", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.64 tip")
    h.require_contains("0.4.64", "CHANGELOG.md", "CHANGELOG missing 0.4.64")
    h.require_contains("0.4.65", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.65 tip")
    h.require_contains("0.4.65", "CHANGELOG.md", "CHANGELOG missing 0.4.65")
    h.require_contains("0.4.66", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.66 tip")
    h.require_contains("0.4.66", "CHANGELOG.md", "CHANGELOG missing 0.4.66")
    h.require_contains("0.4.67", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.67 tip")
    h.require_contains("0.4.67", "CHANGELOG.md", "CHANGELOG missing 0.4.67")
    h.require_contains("0.4.68", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.68 tip")
    h.require_contains("0.4.68", "CHANGELOG.md", "CHANGELOG missing 0.4.68")
    h.require_contains("0.4.69", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.69 tip")
    h.require_contains("0.4.69", "CHANGELOG.md", "CHANGELOG missing 0.4.69")
    h.require_contains("0.4.70", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.70 tip")
    h.require_contains("0.4.70", "CHANGELOG.md", "CHANGELOG missing 0.4.70")
    h.require_contains("0.4.71", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.71 tip")
    h.require_contains("0.4.71", "CHANGELOG.md", "CHANGELOG missing 0.4.71")
    h.require_contains("0.4.72", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.72 tip")
    h.require_contains("0.4.72", "CHANGELOG.md", "CHANGELOG missing 0.4.72")
    h.require_contains("0.4.73", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.73 tip")
    h.require_contains("0.4.73", "CHANGELOG.md", "CHANGELOG missing 0.4.73")
    h.require_contains("0.4.74", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.74 tip")
    h.require_contains("0.4.74", "CHANGELOG.md", "CHANGELOG missing 0.4.74")
    h.require_contains("0.4.75", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.75 tip")
    h.require_contains("0.4.75", "CHANGELOG.md", "CHANGELOG missing 0.4.75")
    h.require_contains("0.4.76", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.76 tip")
    h.require_contains("0.4.76", "CHANGELOG.md", "CHANGELOG missing 0.4.76")
    h.require_contains("0.4.77", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.77 tip")
    h.require_contains("0.4.77", "CHANGELOG.md", "CHANGELOG missing 0.4.77")
    h.require_contains("0.4.78", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.78 tip")
    h.require_contains("0.4.78", "CHANGELOG.md", "CHANGELOG missing 0.4.78")
    h.require_contains("0.4.79", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.79 tip")
    h.require_contains("0.4.79", "CHANGELOG.md", "CHANGELOG missing 0.4.79")
    h.require_contains("0.4.80", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.80 tip")
    h.require_contains("0.4.80", "CHANGELOG.md", "CHANGELOG missing 0.4.80")
    h.require_contains("0.4.81", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.81 tip")
    h.require_contains("0.4.81", "CHANGELOG.md", "CHANGELOG missing 0.4.81")
    h.require_contains("0.4.82", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.82 tip")
    h.require_contains("0.4.82", "CHANGELOG.md", "CHANGELOG missing 0.4.82")
    h.require_contains("0.4.83", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.83 tip")
    h.require_contains("0.4.83", "CHANGELOG.md", "CHANGELOG missing 0.4.83")
    h.require_contains("0.4.84", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.84 tip")
    h.require_contains("0.4.84", "CHANGELOG.md", "CHANGELOG missing 0.4.84")
    h.require_contains("0.4.85", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.85 tip")
    h.require_contains("0.4.85", "CHANGELOG.md", "CHANGELOG missing 0.4.85")
    h.require_contains("0.4.86", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.86 tip")
    h.require_contains("0.4.86", "CHANGELOG.md", "CHANGELOG missing 0.4.86")
    h.require_contains("0.4.87", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.87 tip")
    h.require_contains("0.4.87", "CHANGELOG.md", "CHANGELOG missing 0.4.87")
    h.require_contains("0.4.88", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.88 tip")
    h.require_contains("0.4.88", "CHANGELOG.md", "CHANGELOG missing 0.4.88")
    h.require_contains("0.4.89", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.89 tip")
    h.require_contains("0.4.89", "CHANGELOG.md", "CHANGELOG missing 0.4.89")
    h.require_contains("0.4.92", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.92 tip")
    h.require_contains("0.4.92", "CHANGELOG.md", "CHANGELOG missing 0.4.92")
    h.require_contains("0.4.93", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.93 tip")
    h.require_contains("0.4.93", "CHANGELOG.md", "CHANGELOG missing 0.4.93")
    h.require_contains("0.4.95", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.95 tip")
    h.require_contains("0.4.95", "CHANGELOG.md", "CHANGELOG missing 0.4.95")
    h.require_contains("0.4.96", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.96 tip")
    h.require_contains("0.4.96", "CHANGELOG.md", "CHANGELOG missing 0.4.96")
    h.require_contains("0.4.97", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.97 tip")
    h.require_contains("0.4.97", "CHANGELOG.md", "CHANGELOG missing 0.4.97")
    h.require_contains("0.4.98", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.98 tip")
    h.require_contains("0.4.98", "CHANGELOG.md", "CHANGELOG missing 0.4.98")
    h.require_contains("0.4.99", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.99 tip")
    h.require_contains("0.4.99", "CHANGELOG.md", "CHANGELOG missing 0.4.99")
    h.require_contains("0.4.100", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.100 tip")
    h.require_contains("0.4.100", "CHANGELOG.md", "CHANGELOG missing 0.4.100")
    h.require_contains("0.4.101", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.101 tip")
    h.require_contains("0.4.101", "CHANGELOG.md", "CHANGELOG missing 0.4.101")
    h.require_contains("0.4.102", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.102 tip")
    h.require_contains("0.4.102", "CHANGELOG.md", "CHANGELOG missing 0.4.102")
    h.require_contains("0.4.105", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.105 tip")
    h.require_contains("0.4.105", "CHANGELOG.md", "CHANGELOG missing 0.4.105")
    h.require_contains("0.4.106", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.106 tip")
    h.require_contains("0.4.106", "CHANGELOG.md", "CHANGELOG missing 0.4.106")
    h.require_contains("0.4.107", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.107 tip")
    h.require_contains("0.4.107", "CHANGELOG.md", "CHANGELOG missing 0.4.107")
    h.require_contains("0.4.108", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.108 tip")
    h.require_contains("0.4.108", "CHANGELOG.md", "CHANGELOG missing 0.4.108")
    h.require_contains("0.4.109", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.109 tip")
    h.require_contains("0.4.109", "CHANGELOG.md", "CHANGELOG missing 0.4.109")
    h.require_contains("0.4.110", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.110 tip")
    h.require_contains("0.4.110", "CHANGELOG.md", "CHANGELOG missing 0.4.110")
    h.require_contains("0.4.111", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.111 tip")
    h.require_contains("0.4.111", "CHANGELOG.md", "CHANGELOG missing 0.4.111")
    h.require_contains("0.4.112", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.112 tip")
    h.require_contains("0.4.112", "CHANGELOG.md", "CHANGELOG missing 0.4.112")
    h.require_contains("0.4.113", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.113 tip")
    h.require_contains("0.4.113", "CHANGELOG.md", "CHANGELOG missing 0.4.113")
    h.require_contains("0.4.114", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.114 tip")
    h.require_contains("0.4.114", "CHANGELOG.md", "CHANGELOG missing 0.4.114")
    h.require_contains("0.4.115", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.115 tip")
    h.require_contains("0.4.115", "CHANGELOG.md", "CHANGELOG missing 0.4.115")
    h.require_contains("0.4.117", "CHANGELOG.md", "CHANGELOG missing 0.4.117")
    h.require_contains("0.4.118", "evals/fixtures/this-upgrade.md", "this-upgrade.md missing 0.4.118 tip")
    h.require_contains("0.4.118", ".claude-plugin/plugin.json", "plugin.json not at 0.4.118")
    h.require_contains("0.4.118", "CHANGELOG.md", "CHANGELOG missing 0.4.118")

    # session-discovery
    h.section("session-discovery locate HARD-GATE leaf")
    h.need("skills/emperor-heal/session-discovery.md")
    h.need("references/session-discovery.md")
    h.need("scripts/lib/session_discovery.py")
    h.need("scripts/session-discovery.sh")
    h.need("scripts/session-discovery.ps1")
    h.bash_n("scripts/session-discovery.sh", "session-discovery.sh syntax")
    h.py_compile("scripts/lib/session_discovery.py", "session_discovery.py compile")
    h.require_contains(
        "session_discovery.py",
        "scripts/session-discovery.sh",
        "session-discovery.sh does not call session_discovery.py",
    )
    h.require_contains(
        "session_discovery.py",
        "scripts/session-discovery.ps1",
        "session-discovery.ps1 does not call session_discovery.py",
    )
    h.require_contains(
        "session-discovery",
        "scripts/emperor",
        "emperor bash missing session-discovery",
    )
    h.require_contains(
        "'session-discovery'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing session-discovery",
    )
    h.require_contains(
        "session-discovery",
        "scripts/emperor.cmd",
        "emperor.cmd missing session-discovery",
    )
    h.require_contains(
        "session-discovery",
        "scripts/emperor.zsh",
        "emperor.zsh missing session-discovery",
    )
    h.require_contains(
        "session-discovery.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing session-discovery leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/session-discovery.md",
        "session-discovery leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "diagnosing-superpowers",
        "skills/emperor-heal/session-discovery.md",
        "session-discovery leaf missing source skill",
    )
    h.require_contains(
        "obra/superpowers",
        "references/session-discovery.md",
        "session-discovery reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/session-discovery.md",
        "session-discovery reference missing access date",
    )
    h.require_contains(
        "session discovery",
        "evals/triggers.json",
        "triggers missing session discovery phrase",
    )
    h.require_contains(
        "find session transcript",
        "evals/triggers.json",
        "triggers missing find session transcript phrase",
    )
    _, sess_out = h.run_py("scripts/lib/session_discovery.py")
    if not re.search(r"^SESSION checklist=yes", sess_out, re.M):
        h.fail_msg("session_discovery missing checklist=yes")
    if not re.search(r"^PATH kind=", sess_out, re.M):
        h.fail_msg("session_discovery missing PATH line")
    if not re.search(r"^STATUS summary=", sess_out, re.M):
        h.fail_msg("session_discovery missing STATUS line")
    if not re.search(r"^MUST:", sess_out, re.M):
        h.fail_msg("session_discovery missing MUST line")
    if "NO_SESSION_CLAIM_WITHOUT_VERIFIED_PATH" not in sess_out:
        h.fail_msg("session_discovery missing iron law token")
    # explicit missing path must be ABSENT (honesty)
    _, miss = h.run_py(
        "scripts/lib/session_discovery.py",
        "--path",
        "/tmp/et-session-discovery-absent-path-does-not-exist",
    )
    if "status=ABSENT" not in miss:
        h.fail_msg("session_discovery --path missing should mark ABSENT")
    else:
        h.pass_msg("session_discovery marks missing --path ABSENT")
    # explicit existing path VERIFIED
    _, hit = h.run_py(
        "scripts/lib/session_discovery.py",
        "--path",
        str(root / "scripts/lib/session_discovery.py"),
    )
    if "status=VERIFIED" not in hit:
        h.fail_msg("session_discovery --path existing should VERIFIED")
    else:
        h.pass_msg("session_discovery marks existing --path VERIFIED")
    rc, _ = h.run_py("scripts/lib/session_discovery.py", "--reject-guess")
    if rc == 0:
        h.fail_msg("session_discovery --reject-guess should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/session_discovery.py", "--reject-guess")
        if not re.search(r"^REJECT GUESS:", reject, re.M):
            h.fail_msg("reject-guess missing REJECT line")
        else:
            h.pass_msg("session_discovery --reject-guess hard-gates guess")
    _, sess_sh = h.run_sh("scripts/session-discovery.sh")
    if not re.search(r"^SESSION checklist=yes", sess_sh, re.M):
        h.fail_msg("session-discovery.sh missing checklist card")
    _, rout_sess = h.run_py("scripts/lib/route.py", "session discovery")
    if "emperor-heal" not in rout_sess:
        h.fail_msg("route.py session discovery → heal")
    else:
        h.pass_msg("route.py session discovery → emperor-heal")

    # diagnose (intake + citation HARD-GATE)
    h.section("diagnosing HARD-GATE leaf")
    h.need("skills/emperor-heal/diagnosing.md")
    h.need("references/diagnosing.md")
    h.need("scripts/lib/diagnose.py")
    h.need("scripts/diagnose.sh")
    h.need("scripts/diagnose.ps1")
    h.bash_n("scripts/diagnose.sh", "diagnose.sh syntax")
    h.py_compile("scripts/lib/diagnose.py", "diagnose.py compile")
    h.require_contains(
        "diagnose.py",
        "scripts/diagnose.sh",
        "diagnose.sh does not call diagnose.py",
    )
    h.require_contains(
        "diagnose.py",
        "scripts/diagnose.ps1",
        "diagnose.ps1 does not call diagnose.py",
    )
    h.require_contains(
        "diagnose",
        "scripts/emperor",
        "emperor bash missing diagnose",
    )
    h.require_contains(
        "'diagnose'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing diagnose",
    )
    h.require_contains(
        "diagnose",
        "scripts/emperor.cmd",
        "emperor.cmd missing diagnose",
    )
    h.require_contains(
        "diagnose",
        "scripts/emperor.zsh",
        "emperor.zsh missing diagnose",
    )
    h.require_contains(
        "diagnosing.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing diagnosing leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/diagnosing.md",
        "diagnosing leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "diagnosing-superpowers",
        "skills/emperor-heal/diagnosing.md",
        "diagnosing leaf missing source skill",
    )
    h.require_contains(
        "obra/superpowers",
        "references/diagnosing.md",
        "diagnosing reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/diagnosing.md",
        "diagnosing reference missing access date",
    )
    h.require_contains(
        "Intake before analysis",
        "references/diagnosing.md",
        "diagnosing reference missing intake iron",
    )
    h.require_contains(
        "diagnose the session",
        "evals/triggers.json",
        "triggers missing diagnose the session phrase",
    )
    h.require_contains(
        "intake before analysis",
        "evals/triggers.json",
        "triggers missing intake before analysis phrase",
    )
    _, diag_out = h.run_py("scripts/lib/diagnose.py")
    if not re.search(r"^DIAGNOSE checklist=yes", diag_out, re.M):
        h.fail_msg("diagnose missing checklist=yes")
    if not re.search(r"^INTAKE field=", diag_out, re.M):
        h.fail_msg("diagnose missing INTAKE line")
    if not re.search(r"^CITE rule=", diag_out, re.M):
        h.fail_msg("diagnose missing CITE line")
    if not re.search(r"^MUST:", diag_out, re.M):
        h.fail_msg("diagnose missing MUST line")
    if "NO_FINDING_WITHOUT_PATH_LINE_CITATION" not in diag_out:
        h.fail_msg("diagnose missing citation iron law token")
    if "INTAKE_BEFORE_ANALYSIS" not in diag_out:
        h.fail_msg("diagnose missing intake iron law token")
    rc, _ = h.run_py("scripts/lib/diagnose.py", "--reject-uncited")
    if rc == 0:
        h.fail_msg("diagnose --reject-uncited should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/diagnose.py", "--reject-uncited")
        if not re.search(r"^REJECT UNCITED:", reject, re.M):
            h.fail_msg("reject-uncited missing REJECT line")
        else:
            h.pass_msg("diagnose --reject-uncited hard-gates")
    rc, _ = h.run_py("scripts/lib/diagnose.py", "--reject-skip-intake")
    if rc == 0:
        h.fail_msg("diagnose --reject-skip-intake should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/diagnose.py", "--reject-skip-intake")
        if not re.search(r"^REJECT SKIP INTAKE:", reject, re.M):
            h.fail_msg("reject-skip-intake missing REJECT line")
        else:
            h.pass_msg("diagnose --reject-skip-intake hard-gates")
    rc, cite_ok = h.run_py(
        "scripts/lib/diagnose.py",
        "--check-citation",
        "scripts/lib/diagnose.py:12",
    )
    if rc != 0 or "CITE OK:" not in cite_ok:
        h.fail_msg("diagnose --check-citation should accept path:line")
    else:
        h.pass_msg("diagnose --check-citation accepts path:line")
    rc, cite_bad = h.run_py(
        "scripts/lib/diagnose.py",
        "--check-citation",
        "obviously broken with no cite",
    )
    if rc == 0 or "CITE FAIL:" not in cite_bad:
        h.fail_msg("diagnose --check-citation should reject uncited text")
    else:
        h.pass_msg("diagnose --check-citation rejects uncited text")
    _, diag_sh = h.run_sh("scripts/diagnose.sh")
    if not re.search(r"^DIAGNOSE checklist=yes", diag_sh, re.M):
        h.fail_msg("diagnose.sh missing checklist card")
    _, rout_diag = h.run_py("scripts/lib/route.py", "diagnose the session")
    if "emperor-heal" not in rout_diag:
        h.fail_msg("route.py diagnose the session → heal")
    else:
        h.pass_msg("route.py diagnose the session → emperor-heal")

    # root-cause tracing HARD-GATE
    h.section("root-cause tracing HARD-GATE leaf")
    h.need("skills/emperor-heal/root-cause-tracing.md")
    h.need("references/root-cause-tracing.md")
    h.need("scripts/lib/root_cause.py")
    h.need("scripts/trace.sh")
    h.need("scripts/trace.ps1")
    h.bash_n("scripts/trace.sh", "trace.sh syntax")
    h.py_compile("scripts/lib/root_cause.py", "root_cause.py compile")
    h.require_contains(
        "root_cause.py",
        "scripts/trace.sh",
        "trace.sh does not call root_cause.py",
    )
    h.require_contains(
        "root_cause.py",
        "scripts/trace.ps1",
        "trace.ps1 does not call root_cause.py",
    )
    h.require_contains(
        "trace",
        "scripts/emperor",
        "emperor bash missing trace",
    )
    h.require_contains(
        "'trace'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing trace",
    )
    h.require_contains(
        "trace",
        "scripts/emperor.cmd",
        "emperor.cmd missing trace",
    )
    h.require_contains(
        "trace",
        "scripts/emperor.zsh",
        "emperor.zsh missing trace",
    )
    h.require_contains(
        "root-cause-tracing.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing root-cause-tracing leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/root-cause-tracing.md",
        "root-cause-tracing leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/root-cause-tracing.md",
        "root-cause-tracing leaf missing source skill",
    )
    h.require_contains(
        "root-cause-tracing.md",
        "skills/emperor-heal/root-cause-tracing.md",
        "root-cause-tracing leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/root-cause-tracing.md",
        "root-cause-tracing reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/root-cause-tracing.md",
        "root-cause-tracing reference missing access date",
    )
    h.require_contains(
        "NO SYMPTOM FIX WITHOUT SOURCE TRACE",
        "skills/emperor-heal/root-cause-tracing.md",
        "root-cause-tracing leaf missing iron law text",
    )
    h.require_contains(
        "trace root cause",
        "evals/triggers.json",
        "triggers missing trace root cause phrase",
    )
    h.require_contains(
        "root cause tracing",
        "evals/triggers.json",
        "triggers missing root cause tracing phrase",
    )
    h.require_contains(
        "root-cause-tracing.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing root-cause-tracing leaf",
    )
    _, trace_out = h.run_py("scripts/lib/root_cause.py")
    if not re.search(r"^TRACE checklist=yes", trace_out, re.M):
        h.fail_msg("root_cause missing checklist=yes")
    if not re.search(r"^STEP \d+ id=", trace_out, re.M):
        h.fail_msg("root_cause missing STEP line")
    if not re.search(r"^MUST:", trace_out, re.M):
        h.fail_msg("root_cause missing MUST line")
    if "NO_SYMPTOM_FIX_WITHOUT_SOURCE_TRACE" not in trace_out:
        h.fail_msg("root_cause missing iron law token")
    rc, _ = h.run_py("scripts/lib/root_cause.py", "--reject-symptom-fix")
    if rc == 0:
        h.fail_msg("root_cause --reject-symptom-fix should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/root_cause.py", "--reject-symptom-fix")
        if not re.search(r"^REJECT SYMPTOM FIX:", reject, re.M):
            h.fail_msg("reject-symptom-fix missing REJECT line")
        else:
            h.pass_msg("root_cause --reject-symptom-fix hard-gates")
    rc, _ = h.run_py("scripts/lib/root_cause.py", "--reject-untraced")
    if rc == 0:
        h.fail_msg("root_cause --reject-untraced should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/root_cause.py", "--reject-untraced")
        if not re.search(r"^REJECT UNTRACED:", reject, re.M):
            h.fail_msg("reject-untraced missing REJECT line")
        else:
            h.pass_msg("root_cause --reject-untraced hard-gates")
    rc, chain_ok = h.run_py(
        "scripts/lib/root_cause.py",
        "--check-chain",
        "symptom → called by mid → called by source",
    )
    if rc != 0 or "CHAIN OK:" not in chain_ok:
        h.fail_msg("root_cause --check-chain should accept multi-hop chain")
    else:
        h.pass_msg("root_cause --check-chain accepts multi-hop")
    rc, chain_bad = h.run_py(
        "scripts/lib/root_cause.py",
        "--check-chain",
        "only a single arrow → here",
    )
    if rc == 0 or "CHAIN FAIL:" not in chain_bad:
        h.fail_msg("root_cause --check-chain should reject thin chain")
    else:
        h.pass_msg("root_cause --check-chain rejects thin chain")
    _, trace_sh = h.run_sh("scripts/trace.sh")
    if not re.search(r"^TRACE checklist=yes", trace_sh, re.M):
        h.fail_msg("trace.sh missing checklist card")
    _, rout_trace = h.run_py("scripts/lib/route.py", "trace root cause")
    if "emperor-heal" not in rout_trace:
        h.fail_msg("route.py trace root cause → heal")
    else:
        h.pass_msg("route.py trace root cause → emperor-heal")


    # defense-in-depth HARD-GATE
    h.section("defense-in-depth HARD-GATE leaf")
    h.need("skills/emperor-heal/defense-in-depth.md")
    h.need("references/defense-in-depth.md")
    h.need("scripts/lib/defense.py")
    h.need("scripts/defense.sh")
    h.need("scripts/defense.ps1")
    h.bash_n("scripts/defense.sh", "defense.sh syntax")
    h.py_compile("scripts/lib/defense.py", "defense.py compile")
    h.require_contains(
        "defense.py",
        "scripts/defense.sh",
        "defense.sh does not call defense.py",
    )
    h.require_contains(
        "defense.py",
        "scripts/defense.ps1",
        "defense.ps1 does not call defense.py",
    )
    h.require_contains(
        "defense",
        "scripts/emperor",
        "emperor bash missing defense",
    )
    h.require_contains(
        "'defense'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing defense",
    )
    h.require_contains(
        "defense",
        "scripts/emperor.cmd",
        "emperor.cmd missing defense",
    )
    h.require_contains(
        "defense",
        "scripts/emperor.zsh",
        "emperor.zsh missing defense",
    )
    h.require_contains(
        "defense-in-depth.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing defense-in-depth leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/defense-in-depth.md",
        "defense-in-depth leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/defense-in-depth.md",
        "defense-in-depth leaf missing source skill",
    )
    h.require_contains(
        "defense-in-depth.md",
        "skills/emperor-heal/defense-in-depth.md",
        "defense-in-depth leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/defense-in-depth.md",
        "defense-in-depth reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/defense-in-depth.md",
        "defense-in-depth reference missing access date",
    )
    h.require_contains(
        "NO SINGLE LAYER VALIDATION",
        "skills/emperor-heal/defense-in-depth.md",
        "defense-in-depth leaf missing iron law text",
    )
    h.require_contains(
        "defense in depth",
        "evals/triggers.json",
        "triggers missing defense in depth phrase",
    )
    h.require_contains(
        "validate at every layer",
        "evals/triggers.json",
        "triggers missing validate at every layer phrase",
    )
    h.require_contains(
        "defense-in-depth.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing defense-in-depth leaf",
    )
    _, defense_out = h.run_py("scripts/lib/defense.py")
    if not re.search(r"^DEFENSE checklist=yes", defense_out, re.M):
        h.fail_msg("defense missing checklist=yes")
    if not re.search(r"^LAYER \d+ id=", defense_out, re.M):
        h.fail_msg("defense missing LAYER line")
    if not re.search(r"^MUST:", defense_out, re.M):
        h.fail_msg("defense missing MUST line")
    if "NO_SINGLE_LAYER_VALIDATION" not in defense_out:
        h.fail_msg("defense missing iron law token")
    rc, _ = h.run_py("scripts/lib/defense.py", "--reject-single-layer")
    if rc == 0:
        h.fail_msg("defense --reject-single-layer should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/defense.py", "--reject-single-layer")
        if not re.search(r"^REJECT SINGLE LAYER:", reject, re.M):
            h.fail_msg("reject-single-layer missing REJECT line")
        else:
            h.pass_msg("defense --reject-single-layer hard-gates")
    rc, _ = h.run_py("scripts/lib/defense.py", "--reject-unlayered")
    if rc == 0:
        h.fail_msg("defense --reject-unlayered should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/defense.py", "--reject-unlayered")
        if not re.search(r"^REJECT UNLAYERED:", reject, re.M):
            h.fail_msg("reject-unlayered missing REJECT line")
        else:
            h.pass_msg("defense --reject-unlayered hard-gates")
    rc, layers_ok = h.run_py(
        "scripts/lib/defense.py",
        "--check-layers",
        "entry + business + environment",
    )
    if rc != 0 or "LAYERS OK:" not in layers_ok:
        h.fail_msg("defense --check-layers should accept multi-layer plan")
    else:
        h.pass_msg("defense --check-layers accepts multi-layer plan")
    rc, layers_bad = h.run_py(
        "scripts/lib/defense.py",
        "--check-layers",
        "only entry here",
    )
    if rc == 0 or "LAYERS FAIL:" not in layers_bad:
        h.fail_msg("defense --check-layers should reject single-layer plan")
    else:
        h.pass_msg("defense --check-layers rejects single-layer plan")
    _, defense_sh = h.run_sh("scripts/defense.sh")
    if not re.search(r"^DEFENSE checklist=yes", defense_sh, re.M):
        h.fail_msg("defense.sh missing checklist card")
    _, rout_defense = h.run_py("scripts/lib/route.py", "defense in depth")
    if "emperor-heal" not in rout_defense:
        h.fail_msg("route.py defense in depth → heal")
    else:
        h.pass_msg("route.py defense in depth → emperor-heal")




    # condition-based-waiting HARD-GATE
    h.section("condition-based-waiting HARD-GATE leaf")
    h.need("skills/emperor-heal/condition-based-waiting.md")
    h.need("references/condition-based-waiting.md")
    h.need("scripts/lib/condition_wait.py")
    h.need("scripts/condition-wait.sh")
    h.need("scripts/condition-wait.ps1")
    h.bash_n("scripts/condition-wait.sh", "condition-wait.sh syntax")
    h.py_compile("scripts/lib/condition_wait.py", "condition_wait.py compile")
    h.require_contains(
        "condition_wait.py",
        "scripts/condition-wait.sh",
        "condition-wait.sh does not call condition_wait.py",
    )
    h.require_contains(
        "condition_wait.py",
        "scripts/condition-wait.ps1",
        "condition-wait.ps1 does not call condition_wait.py",
    )
    h.require_contains(
        "wait",
        "scripts/emperor",
        "emperor bash missing wait",
    )
    h.require_contains(
        "'wait'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing wait",
    )
    h.require_contains(
        "wait",
        "scripts/emperor.cmd",
        "emperor.cmd missing wait",
    )
    h.require_contains(
        "wait",
        "scripts/emperor.zsh",
        "emperor.zsh missing wait",
    )
    h.require_contains(
        "condition-based-waiting.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing condition-based-waiting leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/condition-based-waiting.md",
        "condition-based-waiting leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/condition-based-waiting.md",
        "condition-based-waiting leaf missing source skill",
    )
    h.require_contains(
        "condition-based-waiting.md",
        "skills/emperor-heal/condition-based-waiting.md",
        "condition-based-waiting leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/condition-based-waiting.md",
        "condition-based-waiting reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/condition-based-waiting.md",
        "condition-based-waiting reference missing access date",
    )
    h.require_contains(
        "e89fec8400d6cd50f43407cec9fab50976ba4d55d0ec2eb51c0bd68036b54c26",
        "references/condition-based-waiting.md",
        "condition-based-waiting reference missing sha256",
    )
    h.require_contains(
        "NO ARBITRARY SLEEP",
        "skills/emperor-heal/condition-based-waiting.md",
        "condition-based-waiting leaf missing iron law text",
    )
    h.require_contains(
        "condition based waiting",
        "evals/triggers.json",
        "triggers missing condition based waiting phrase",
    )
    h.require_contains(
        "arbitrary sleep",
        "evals/triggers.json",
        "triggers missing arbitrary sleep phrase",
    )
    h.require_contains(
        "condition-based-waiting.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing condition-based-waiting leaf",
    )
    _, wait_out = h.run_py("scripts/lib/condition_wait.py")
    if not re.search(r"^WAIT checklist=yes", wait_out, re.M):
        h.fail_msg("condition_wait missing checklist=yes")
    if not re.search(r"^COND \d+ id=", wait_out, re.M):
        h.fail_msg("condition_wait missing COND line")
    if not re.search(r"^MUST:", wait_out, re.M):
        h.fail_msg("condition_wait missing MUST line")
    if "NO_ARBITRARY_SLEEP" not in wait_out:
        h.fail_msg("condition_wait missing iron law token")
    rc, _ = h.run_py("scripts/lib/condition_wait.py", "--reject-sleep")
    if rc == 0:
        h.fail_msg("condition_wait --reject-sleep should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/condition_wait.py", "--reject-sleep")
        if not re.search(r"^REJECT SLEEP:", reject, re.M):
            h.fail_msg("reject-sleep missing REJECT line")
        else:
            h.pass_msg("condition_wait --reject-sleep hard-gates")
    rc, _ = h.run_py("scripts/lib/condition_wait.py", "--reject-unguessed")
    if rc == 0:
        h.fail_msg("condition_wait --reject-unguessed should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/condition_wait.py", "--reject-unguessed")
        if not re.search(r"^REJECT UNGUESSED:", reject, re.M):
            h.fail_msg("reject-unguessed missing REJECT line")
        else:
            h.pass_msg("condition_wait --reject-unguessed hard-gates")
    rc, cond_ok = h.run_py(
        "scripts/lib/condition_wait.py",
        "--check-condition",
        "waitFor ready state",
    )
    if rc != 0 or "CONDITION OK:" not in cond_ok:
        h.fail_msg("condition_wait --check-condition should accept real condition")
    else:
        h.pass_msg("condition_wait --check-condition accepts real condition")
    rc, cond_bad = h.run_py(
        "scripts/lib/condition_wait.py",
        "--check-condition",
        "sleep 50ms and hope",
    )
    if rc == 0 or "CONDITION FAIL:" not in cond_bad:
        h.fail_msg("condition_wait --check-condition should reject bare sleep")
    else:
        h.pass_msg("condition_wait --check-condition rejects bare sleep")
    _, wait_sh = h.run_sh("scripts/condition-wait.sh")
    if not re.search(r"^WAIT checklist=yes", wait_sh, re.M):
        h.fail_msg("condition-wait.sh missing checklist card")
    _, rout_wait = h.run_py("scripts/lib/route.py", "condition based waiting")
    if "emperor-heal" not in rout_wait:
        h.fail_msg("route.py condition based waiting → heal")
    else:
        h.pass_msg("route.py condition based waiting → emperor-heal")


    # find-polluter HARD-GATE
    h.section("find-polluter HARD-GATE leaf")
    h.need("skills/emperor-heal/find-polluter.md")
    h.need("references/find-polluter.md")
    h.need("scripts/lib/polluter.py")
    h.need("scripts/find-polluter.sh")
    h.need("scripts/find-polluter.ps1")
    h.bash_n("scripts/find-polluter.sh", "find-polluter.sh syntax")
    h.py_compile("scripts/lib/polluter.py", "polluter.py compile")
    h.require_contains(
        "polluter.py",
        "scripts/find-polluter.sh",
        "find-polluter.sh does not call polluter.py",
    )
    h.require_contains(
        "polluter.py",
        "scripts/find-polluter.ps1",
        "find-polluter.ps1 does not call polluter.py",
    )
    h.require_contains(
        "polluter",
        "scripts/emperor",
        "emperor bash missing polluter",
    )
    h.require_contains(
        "'polluter'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing polluter",
    )
    h.require_contains(
        "polluter",
        "scripts/emperor.cmd",
        "emperor.cmd missing polluter",
    )
    h.require_contains(
        "polluter",
        "scripts/emperor.zsh",
        "emperor.zsh missing polluter",
    )
    h.require_contains(
        "find-polluter.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing find-polluter leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/find-polluter.md",
        "find-polluter leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/find-polluter.md",
        "find-polluter leaf missing source skill",
    )
    h.require_contains(
        "find-polluter.sh",
        "skills/emperor-heal/find-polluter.md",
        "find-polluter leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/find-polluter.md",
        "find-polluter reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/find-polluter.md",
        "find-polluter reference missing access date",
    )
    h.require_contains(
        "dd7b8f13c4cc2a24b33ff87b18da9248f3e1c80a085c3316224f69ff0fa5c43c",
        "references/find-polluter.md",
        "find-polluter reference missing sha256",
    )
    h.require_contains(
        "NO GUESS THE POLLUTER",
        "skills/emperor-heal/find-polluter.md",
        "find-polluter leaf missing iron law text",
    )
    h.require_contains(
        "find polluter",
        "evals/triggers.json",
        "triggers missing find polluter phrase",
    )
    h.require_contains(
        "test pollution",
        "evals/triggers.json",
        "triggers missing test pollution phrase",
    )
    h.require_contains(
        "find-polluter.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing find-polluter leaf",
    )
    _, pol_out = h.run_py("scripts/lib/polluter.py")
    if not re.search(r"^POLLUTER checklist=yes", pol_out, re.M):
        h.fail_msg("polluter missing checklist=yes")
    if not re.search(r"^STEP \d+ id=", pol_out, re.M):
        h.fail_msg("polluter missing STEP line")
    if not re.search(r"^MUST:", pol_out, re.M):
        h.fail_msg("polluter missing MUST line")
    if "NO_GUESS_THE_POLLUTER" not in pol_out:
        h.fail_msg("polluter missing iron law token")
    rc, _ = h.run_py("scripts/lib/polluter.py", "--reject-guess")
    if rc == 0:
        h.fail_msg("polluter --reject-guess should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/polluter.py", "--reject-guess")
        if not re.search(r"^REJECT GUESS:", reject, re.M):
            h.fail_msg("reject-guess missing REJECT line")
        else:
            h.pass_msg("polluter --reject-guess hard-gates")
    rc, _ = h.run_py("scripts/lib/polluter.py", "--reject-unbisected")
    if rc == 0:
        h.fail_msg("polluter --reject-unbisected should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/polluter.py", "--reject-unbisected")
        if not re.search(r"^REJECT UNBISECTED:", reject, re.M):
            h.fail_msg("reject-unbisected missing REJECT line")
        else:
            h.pass_msg("polluter --reject-unbisected hard-gates")
    rc, pol_ok = h.run_py(
        "scripts/lib/polluter.py",
        "--check-found",
        "FOUND POLLUTER Test: src/foo.test.ts Created: .git",
    )
    if rc != 0 or "POLLUTER OK:" not in pol_ok:
        h.fail_msg("polluter --check-found should accept FOUND POLLUTER + path")
    else:
        h.pass_msg("polluter --check-found accepts FOUND POLLUTER + path")
    rc, pol_bad = h.run_py(
        "scripts/lib/polluter.py",
        "--check-found",
        "probably the setup file",
    )
    if rc == 0 or "POLLUTER FAIL:" not in pol_bad:
        h.fail_msg("polluter --check-found should reject bare guess")
    else:
        h.pass_msg("polluter --check-found rejects bare guess")
    _, pol_sh = h.run_sh("scripts/find-polluter.sh")
    if not re.search(r"^POLLUTER checklist=yes", pol_sh, re.M):
        h.fail_msg("find-polluter.sh missing checklist card")
    _, rout_pol = h.run_py("scripts/lib/route.py", "find polluter")
    if "emperor-heal" not in rout_pol:
        h.fail_msg("route.py find polluter → heal")
    else:
        h.pass_msg("route.py find polluter → emperor-heal")


    # pressure/academic HARD-GATE
    h.section("pressure/academic HARD-GATE leaf")
    h.need("skills/emperor-heal/pressure-academic.md")
    h.need("references/pressure-academic.md")
    h.need("scripts/lib/pressure.py")
    h.need("scripts/pressure.sh")
    h.need("scripts/pressure.ps1")
    h.bash_n("scripts/pressure.sh", "pressure.sh syntax")
    h.py_compile("scripts/lib/pressure.py", "pressure.py compile")
    h.require_contains(
        "pressure.py",
        "scripts/pressure.sh",
        "pressure.sh does not call pressure.py",
    )
    h.require_contains(
        "pressure.py",
        "scripts/pressure.ps1",
        "pressure.ps1 does not call pressure.py",
    )
    h.require_contains(
        "pressure",
        "scripts/emperor",
        "emperor bash missing pressure",
    )
    h.require_contains(
        "'pressure'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing pressure",
    )
    h.require_contains(
        "pressure",
        "scripts/emperor.cmd",
        "emperor.cmd missing pressure",
    )
    h.require_contains(
        "pressure",
        "scripts/emperor.zsh",
        "emperor.zsh missing pressure",
    )
    h.require_contains(
        "pressure-academic.md",
        "skills/emperor-heal/SKILL.md",
        "emperor-heal missing pressure-academic leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-heal/pressure-academic.md",
        "pressure-academic leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "systematic-debugging",
        "skills/emperor-heal/pressure-academic.md",
        "pressure-academic leaf missing source skill",
    )
    h.require_contains(
        "test-pressure-1.md",
        "skills/emperor-heal/pressure-academic.md",
        "pressure-academic leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/pressure-academic.md",
        "pressure-academic reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/pressure-academic.md",
        "pressure-academic reference missing access date",
    )
    h.require_contains(
        "0b6a915db0054577819834c79be9eb614e97bddba10d73768e1fbe91cfed048a",
        "references/pressure-academic.md",
        "pressure-academic reference missing sha256",
    )
    h.require_contains(
        "NO SKIP UNDER PRESSURE",
        "skills/emperor-heal/pressure-academic.md",
        "pressure-academic leaf missing iron law text",
    )
    h.require_contains(
        "under pressure",
        "evals/triggers.json",
        "triggers missing under pressure phrase",
    )
    h.require_contains(
        "resist shortcut",
        "evals/triggers.json",
        "triggers missing resist shortcut phrase",
    )
    h.require_contains(
        "pressure-academic.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing pressure-academic leaf",
    )
    _, pr_out = h.run_py("scripts/lib/pressure.py")
    if not re.search(r"^PRESSURE checklist=yes", pr_out, re.M):
        h.fail_msg("pressure missing checklist=yes")
    if not re.search(r"^CASE \d+ id=", pr_out, re.M):
        h.fail_msg("pressure missing CASE line")
    if not re.search(r"^MUST:", pr_out, re.M):
        h.fail_msg("pressure missing MUST line")
    if not re.search(r"^ACADEMIC \d+ q=", pr_out, re.M):
        h.fail_msg("pressure missing ACADEMIC line")
    if "NO_SKIP_UNDER_PRESSURE" not in pr_out:
        h.fail_msg("pressure missing iron law token")
    rc, _ = h.run_py("scripts/lib/pressure.py", "--reject-shortcut")
    if rc == 0:
        h.fail_msg("pressure --reject-shortcut should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/pressure.py", "--reject-shortcut")
        if not re.search(r"^REJECT SHORTCUT:", reject, re.M):
            h.fail_msg("reject-shortcut missing REJECT line")
        else:
            h.pass_msg("pressure --reject-shortcut hard-gates")
    rc, _ = h.run_py("scripts/lib/pressure.py", "--reject-compromise")
    if rc == 0:
        h.fail_msg("pressure --reject-compromise should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/pressure.py", "--reject-compromise")
        if not re.search(r"^REJECT COMPROMISE:", reject, re.M):
            h.fail_msg("reject-compromise missing REJECT line")
        else:
            h.pass_msg("pressure --reject-compromise hard-gates")
    rc, pr_ok = h.run_py(
        "scripts/lib/pressure.py",
        "--check-academic",
        "Four phases: investigate pattern hypothesize implement. "
        "Before any fix complete Phase 1 root cause. Never skip. Option A follow process.",
    )
    if rc != 0 or "PRESSURE OK:" not in pr_ok:
        h.fail_msg("pressure --check-academic should accept four-phase answers")
    else:
        h.pass_msg("pressure --check-academic accepts four-phase answers")
    rc, pr_bad = h.run_py(
        "scripts/lib/pressure.py",
        "--check-academic",
        "just add a retry and ship",
    )
    if rc == 0 or "PRESSURE FAIL:" not in pr_bad:
        h.fail_msg("pressure --check-academic should reject bare shortcut")
    else:
        h.pass_msg("pressure --check-academic rejects bare shortcut")
    _, pr_sh = h.run_sh("scripts/pressure.sh")
    if not re.search(r"^PRESSURE checklist=yes", pr_sh, re.M):
        h.fail_msg("pressure.sh missing checklist card")
    _, rout_pr = h.run_py("scripts/lib/route.py", "under pressure")
    if "emperor-heal" not in rout_pr:
        h.fail_msg("route.py under pressure → heal")
    else:
        h.pass_msg("route.py under pressure → emperor-heal")


    # writing-good-tests HARD-GATE
    h.section("writing-good-tests HARD-GATE leaf")
    h.need("skills/emperor-tdd/writing-good-tests.md")
    h.need("references/writing-good-tests.md")
    h.need("scripts/lib/good_tests.py")
    h.need("scripts/good-tests.sh")
    h.need("scripts/good-tests.ps1")
    h.bash_n("scripts/good-tests.sh", "good-tests.sh syntax")
    h.py_compile("scripts/lib/good_tests.py", "good_tests.py compile")
    h.require_contains(
        "good_tests.py",
        "scripts/good-tests.sh",
        "good-tests.sh does not call good_tests.py",
    )
    h.require_contains(
        "good_tests.py",
        "scripts/good-tests.ps1",
        "good-tests.ps1 does not call good_tests.py",
    )
    h.require_contains(
        "good-tests",
        "scripts/emperor",
        "emperor bash missing good-tests",
    )
    h.require_contains(
        "'good-tests'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing good-tests",
    )
    h.require_contains(
        "good-tests",
        "scripts/emperor.cmd",
        "emperor.cmd missing good-tests",
    )
    h.require_contains(
        "good-tests",
        "scripts/emperor.zsh",
        "emperor.zsh missing good-tests",
    )
    h.require_contains(
        "writing-good-tests.md",
        "skills/emperor-tdd/SKILL.md",
        "emperor-tdd missing writing-good-tests leaf",
    )
    h.require_contains(
        "HARD-GATE",
        "skills/emperor-tdd/writing-good-tests.md",
        "writing-good-tests leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "test-driven-development",
        "skills/emperor-tdd/writing-good-tests.md",
        "writing-good-tests leaf missing source skill",
    )
    h.require_contains(
        "writing-good-tests.md",
        "skills/emperor-tdd/writing-good-tests.md",
        "writing-good-tests leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/writing-good-tests.md",
        "writing-good-tests reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/writing-good-tests.md",
        "writing-good-tests reference missing access date",
    )
    h.require_contains(
        "51471c853306ff92ca8bb41dcaea05f31c0e46b03651f8f3c99754b7172f4ae1",
        "references/writing-good-tests.md",
        "writing-good-tests reference missing sha256",
    )
    h.require_contains(
        "EVERY TEST NAMES THE BREAK",
        "skills/emperor-tdd/writing-good-tests.md",
        "writing-good-tests leaf missing iron law text",
    )
    h.require_contains(
        "name the break",
        "evals/triggers.json",
        "triggers missing name the break phrase",
    )
    h.require_contains(
        "mirror assertion",
        "evals/triggers.json",
        "triggers missing mirror assertion phrase",
    )
    h.require_contains(
        "writing-good-tests.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing writing-good-tests leaf",
    )
    _, gt_out = h.run_py("scripts/lib/good_tests.py")
    if not re.search(r"^GOOD checklist=yes", gt_out, re.M):
        h.fail_msg("good_tests missing checklist=yes")
    if not re.search(r"^PRIN \d+ id=", gt_out, re.M):
        h.fail_msg("good_tests missing PRIN line")
    if not re.search(r"^MUST:", gt_out, re.M):
        h.fail_msg("good_tests missing MUST line")
    if not re.search(r"^GATE rule=", gt_out, re.M):
        h.fail_msg("good_tests missing GATE line")
    if "EVERY_TEST_NAMES_THE_BREAK" not in gt_out:
        h.fail_msg("good_tests missing iron law token")
    rc, _ = h.run_py("scripts/lib/good_tests.py", "--reject-mirror")
    if rc == 0:
        h.fail_msg("good_tests --reject-mirror should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/good_tests.py", "--reject-mirror")
        if not re.search(r"^REJECT MIRROR:", reject, re.M):
            h.fail_msg("reject-mirror missing REJECT line")
        else:
            h.pass_msg("good_tests --reject-mirror hard-gates")
    rc, _ = h.run_py("scripts/lib/good_tests.py", "--reject-change-detector")
    if rc == 0:
        h.fail_msg("good_tests --reject-change-detector should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/good_tests.py", "--reject-change-detector")
        if not re.search(r"^REJECT CHANGE-DETECTOR:", reject, re.M):
            h.fail_msg("reject-change-detector missing REJECT line")
        else:
            h.pass_msg("good_tests --reject-change-detector hard-gates")
    rc, gt_ok = h.run_py(
        "scripts/lib/good_tests.py",
        "--check-named-break",
        "Name the break: wrong branch handler. Exercise the real component. "
        "Hand-derived literal want. Mutation check for empty return.",
    )
    if rc != 0 or "GOOD OK:" not in gt_ok:
        h.fail_msg("good_tests --check-named-break should accept named-break answers")
    else:
        h.pass_msg("good_tests --check-named-break accepts named-break answers")
    rc, gt_bad = h.run_py(
        "scripts/lib/good_tests.py",
        "--check-named-break",
        "just assert the mock exists",
    )
    if rc == 0 or "GOOD FAIL:" not in gt_bad:
        h.fail_msg("good_tests --check-named-break should reject bare mock claim")
    else:
        h.pass_msg("good_tests --check-named-break rejects bare mock claim")
    _, gt_sh = h.run_sh("scripts/good-tests.sh")
    if not re.search(r"^GOOD checklist=yes", gt_sh, re.M):
        h.fail_msg("good-tests.sh missing checklist card")
    _, rout_gt = h.run_py("scripts/lib/route.py", "name the break")
    if "emperor-tdd" not in rout_gt:
        h.fail_msg("route.py name the break → tdd")
    else:
        h.pass_msg("route.py name the break → emperor-tdd")


    # testing-skills HARD-GATE
    h.section("testing-skills HARD-GATE leaf")
    h.need("chains/chain-jail/testing-skills.md")
    h.need("references/testing-skills.md")
    h.need("scripts/lib/skill_test.py")
    h.need("scripts/skill-test.sh")
    h.need("scripts/skill-test.ps1")
    h.bash_n("scripts/skill-test.sh", "skill-test.sh syntax")
    h.py_compile("scripts/lib/skill_test.py", "skill_test.py compile")
    h.require_contains(
        "skill_test.py",
        "scripts/skill-test.sh",
        "skill-test.sh does not call skill_test.py",
    )
    h.require_contains(
        "skill_test.py",
        "scripts/skill-test.ps1",
        "skill-test.ps1 does not call skill_test.py",
    )
    h.require_contains(
        "skill-test",
        "scripts/emperor",
        "emperor bash missing skill-test",
    )
    h.require_contains(
        "'skill-test'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing skill-test",
    )
    h.require_contains(
        "skill-test",
        "scripts/emperor.cmd",
        "emperor.cmd missing skill-test",
    )
    h.require_contains(
        "skill-test",
        "scripts/emperor.zsh",
        "emperor.zsh missing skill-test",
    )
    h.require_contains(
        "testing-skills.md",
        "skills/emperor-capture/SKILL.md",
        "emperor-capture missing testing-skills leaf",
    )
    h.require_contains(
        "testing-skills.md",
        "chains/chain-jail/authoring-checklist.md",
        "authoring-checklist missing testing-skills companion",
    )
    h.require_contains(
        "HARD-GATE",
        "chains/chain-jail/testing-skills.md",
        "testing-skills leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "writing-skills",
        "chains/chain-jail/testing-skills.md",
        "testing-skills leaf missing source skill",
    )
    h.require_contains(
        "testing-skills-with-subagents.md",
        "chains/chain-jail/testing-skills.md",
        "testing-skills leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/testing-skills.md",
        "testing-skills reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/testing-skills.md",
        "testing-skills reference missing access date",
    )
    h.require_contains(
        "c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade",
        "references/testing-skills.md",
        "testing-skills reference missing sha256",
    )
    h.require_contains(
        "EVERY SKILL FACES COMBINED PRESSURE",
        "chains/chain-jail/testing-skills.md",
        "testing-skills leaf missing iron law text",
    )
    h.require_contains(
        "testing skills with subagents",
        "evals/triggers.json",
        "triggers missing testing skills with subagents phrase",
    )
    h.require_contains(
        "watch baseline fail without skill",
        "evals/triggers.json",
        "triggers missing watch baseline fail phrase",
    )
    h.require_contains(
        "testing-skills.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing testing-skills leaf",
    )
    _, st_out = h.run_py("scripts/lib/skill_test.py")
    if not re.search(r"^SKILLTEST checklist=yes", st_out, re.M):
        h.fail_msg("skill_test missing checklist=yes")
    if not re.search(r"^PRIN \d+ id=", st_out, re.M):
        h.fail_msg("skill_test missing PRIN line")
    if not re.search(r"^MUST:", st_out, re.M):
        h.fail_msg("skill_test missing MUST line")
    if not re.search(r"^GATE rule=", st_out, re.M):
        h.fail_msg("skill_test missing GATE line")
    if "EVERY_SKILL_FACES_COMBINED_PRESSURE" not in st_out:
        h.fail_msg("skill_test missing iron law token")
    rc, _ = h.run_py("scripts/lib/skill_test.py", "--reject-academic-only")
    if rc == 0:
        h.fail_msg("skill_test --reject-academic-only should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/skill_test.py", "--reject-academic-only")
        if not re.search(r"^REJECT ACADEMIC-ONLY:", reject, re.M):
            h.fail_msg("reject-academic-only missing REJECT line")
        else:
            h.pass_msg("skill_test --reject-academic-only hard-gates")
    rc, _ = h.run_py("scripts/lib/skill_test.py", "--reject-skip-red")
    if rc == 0:
        h.fail_msg("skill_test --reject-skip-red should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/skill_test.py", "--reject-skip-red")
        if not re.search(r"^REJECT SKIP-RED:", reject, re.M):
            h.fail_msg("reject-skip-red missing REJECT line")
        else:
            h.pass_msg("skill_test --reject-skip-red hard-gates")
    rc, st_ok = h.run_py(
        "scripts/lib/skill_test.py",
        "--check-pressure-baseline",
        "Combined pressure: time + sunk cost + exhaustion. Watch baseline FAIL "
        "without the skill. Capture rationalizations verbatim. Explicit negation "
        "per loophole. Stay green under max pressure.",
    )
    if rc != 0 or "SKILLTEST OK:" not in st_ok:
        h.fail_msg("skill_test --check-pressure-baseline should accept pressure answers")
    else:
        h.pass_msg("skill_test --check-pressure-baseline accepts pressure answers")
    rc, st_bad = h.run_py(
        "scripts/lib/skill_test.py",
        "--check-pressure-baseline",
        "just ask what the skill says",
    )
    if rc == 0 or "SKILLTEST FAIL:" not in st_bad:
        h.fail_msg("skill_test --check-pressure-baseline should reject academic-only claim")
    else:
        h.pass_msg("skill_test --check-pressure-baseline rejects academic-only claim")
    _, st_sh = h.run_sh("scripts/skill-test.sh")
    if not re.search(r"^SKILLTEST checklist=yes", st_sh, re.M):
        h.fail_msg("skill-test.sh missing checklist card")
    _, rout_st = h.run_py("scripts/lib/route.py", "testing skills with subagents")
    if "emperor-capture" not in rout_st:
        h.fail_msg("route.py testing skills with subagents → capture")
    else:
        h.pass_msg("route.py testing skills with subagents → emperor-capture")


    # persuasion-principles HARD-GATE
    h.section("persuasion-principles HARD-GATE leaf")
    h.need("chains/chain-jail/persuasion-principles.md")
    h.need("references/persuasion-principles.md")
    h.need("scripts/lib/persuasion.py")
    h.need("scripts/persuasion.sh")
    h.need("scripts/persuasion.ps1")
    h.bash_n("scripts/persuasion.sh", "persuasion.sh syntax")
    h.py_compile("scripts/lib/persuasion.py", "persuasion.py compile")
    h.require_contains(
        "persuasion.py",
        "scripts/persuasion.sh",
        "persuasion.sh does not call persuasion.py",
    )
    h.require_contains(
        "persuasion.py",
        "scripts/persuasion.ps1",
        "persuasion.ps1 does not call persuasion.py",
    )
    h.require_contains(
        "persuasion",
        "scripts/emperor",
        "emperor bash missing persuasion",
    )
    h.require_contains(
        "'persuasion'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing persuasion",
    )
    h.require_contains(
        "persuasion",
        "scripts/emperor.cmd",
        "emperor.cmd missing persuasion",
    )
    h.require_contains(
        "persuasion",
        "scripts/emperor.zsh",
        "emperor.zsh missing persuasion",
    )
    h.require_contains(
        "persuasion-principles.md",
        "skills/emperor-capture/SKILL.md",
        "emperor-capture missing persuasion-principles leaf",
    )
    h.require_contains(
        "persuasion-principles.md",
        "chains/chain-jail/authoring-checklist.md",
        "authoring-checklist missing persuasion companion",
    )
    h.require_contains(
        "HARD-GATE",
        "chains/chain-jail/persuasion-principles.md",
        "persuasion leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "writing-skills",
        "chains/chain-jail/persuasion-principles.md",
        "persuasion leaf missing source skill",
    )
    h.require_contains(
        "persuasion-principles.md",
        "chains/chain-jail/persuasion-principles.md",
        "persuasion leaf missing source file cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/persuasion-principles.md",
        "persuasion reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/persuasion-principles.md",
        "persuasion reference missing access date",
    )
    h.require_contains(
        "a51bc9bf75189ea73a27b3fb504a2fdfdb966fb1f7f1cdf03203230a216ccc03",
        "references/persuasion-principles.md",
        "persuasion reference missing sha256",
    )
    h.require_contains(
        "CRITICAL PRACTICE USES PERSUASION",
        "chains/chain-jail/persuasion-principles.md",
        "persuasion leaf missing iron law text",
    )
    h.require_contains(
        "persuasion principles",
        "evals/triggers.json",
        "triggers missing persuasion principles phrase",
    )
    h.require_contains(
        "hedged skill language",
        "evals/triggers.json",
        "triggers missing hedged skill language phrase",
    )
    h.require_contains(
        "persuasion-principles.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing persuasion-principles leaf",
    )
    _, pe_out = h.run_py("scripts/lib/persuasion.py")
    if not re.search(r"^PERSUADE checklist=yes", pe_out, re.M):
        h.fail_msg("persuasion missing checklist=yes")
    if not re.search(r"^PRIN \d+ id=", pe_out, re.M):
        h.fail_msg("persuasion missing PRIN line")
    if not re.search(r"^MUST:", pe_out, re.M):
        h.fail_msg("persuasion missing MUST line")
    if not re.search(r"^GATE rule=", pe_out, re.M):
        h.fail_msg("persuasion missing GATE line")
    if "CRITICAL_PRACTICE_USES_PERSUASION" not in pe_out:
        h.fail_msg("persuasion missing iron law token")
    rc, _ = h.run_py("scripts/lib/persuasion.py", "--reject-hedge")
    if rc == 0:
        h.fail_msg("persuasion --reject-hedge should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/persuasion.py", "--reject-hedge")
        if not re.search(r"^REJECT HEDGE:", reject, re.M):
            h.fail_msg("reject-hedge missing REJECT line")
        else:
            h.pass_msg("persuasion --reject-hedge hard-gates")
    rc, _ = h.run_py("scripts/lib/persuasion.py", "--reject-optional")
    if rc == 0:
        h.fail_msg("persuasion --reject-optional should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/persuasion.py", "--reject-optional")
        if not re.search(r"^REJECT OPTIONAL:", reject, re.M):
            h.fail_msg("reject-optional missing REJECT line")
        else:
            h.pass_msg("persuasion --reject-optional hard-gates")
    rc, pe_ok = h.run_py(
        "scripts/lib/persuasion.py",
        "--check-persuasion",
        "YOU MUST announce skill usage. Choose A, B, or C. Before proceeding "
        "every time.",
    )
    if rc != 0 or "PERSUADE OK:" not in pe_ok:
        h.fail_msg("persuasion --check-persuasion should accept persuasion answers")
    else:
        h.pass_msg("persuasion --check-persuasion accepts persuasion answers")
    rc, pe_bad = h.run_py(
        "scripts/lib/persuasion.py",
        "--check-persuasion",
        "consider writing tests when feasible",
    )
    if rc == 0 or "PERSUADE FAIL:" not in pe_bad:
        h.fail_msg("persuasion --check-persuasion should reject hedge claim")
    else:
        h.pass_msg("persuasion --check-persuasion rejects hedge claim")
    _, pe_sh = h.run_sh("scripts/persuasion.sh")
    if not re.search(r"^PERSUADE checklist=yes", pe_sh, re.M):
        h.fail_msg("persuasion.sh missing checklist card")
    _, rout_pe = h.run_py("scripts/lib/route.py", "persuasion principles")
    if "emperor-capture" not in rout_pe:
        h.fail_msg("route.py persuasion principles → capture")
    else:
        h.pass_msg("route.py persuasion principles → emperor-capture")


    # skill-discovery SDO HARD-GATE
    h.section("skill-discovery SDO HARD-GATE leaf")
    h.need("chains/chain-jail/skill-discovery.md")
    h.need("references/skill-discovery.md")
    h.need("scripts/lib/sdo.py")
    h.need("scripts/sdo.sh")
    h.need("scripts/sdo.ps1")
    h.bash_n("scripts/sdo.sh", "sdo.sh syntax")
    h.py_compile("scripts/lib/sdo.py", "sdo.py compile")
    h.require_contains(
        "sdo.py",
        "scripts/sdo.sh",
        "sdo.sh does not call sdo.py",
    )
    h.require_contains(
        "sdo.py",
        "scripts/sdo.ps1",
        "sdo.ps1 does not call sdo.py",
    )
    h.require_contains(
        "sdo",
        "scripts/emperor",
        "emperor bash missing sdo",
    )
    h.require_contains(
        "'sdo'",
        "scripts/emperor.ps1",
        "emperor.ps1 missing sdo",
    )
    h.require_contains(
        "sdo",
        "scripts/emperor.cmd",
        "emperor.cmd missing sdo",
    )
    h.require_contains(
        "sdo",
        "scripts/emperor.zsh",
        "emperor.zsh missing sdo",
    )
    h.require_contains(
        "skill-discovery.md",
        "skills/emperor-capture/SKILL.md",
        "emperor-capture missing skill-discovery leaf",
    )
    h.require_contains(
        "skill-discovery.md",
        "chains/chain-jail/authoring-checklist.md",
        "authoring-checklist missing skill-discovery companion",
    )
    h.require_contains(
        "HARD-GATE",
        "chains/chain-jail/skill-discovery.md",
        "skill-discovery leaf missing HARD-GATE heading",
    )
    h.require_contains(
        "writing-skills",
        "chains/chain-jail/skill-discovery.md",
        "skill-discovery leaf missing source skill",
    )
    h.require_contains(
        "Skill Discovery Optimization",
        "chains/chain-jail/skill-discovery.md",
        "skill-discovery leaf missing SDO heading cite",
    )
    h.require_contains(
        "obra/superpowers",
        "references/skill-discovery.md",
        "skill-discovery reference missing obra/superpowers cite",
    )
    h.require_contains(
        "2026-09-27",
        "references/skill-discovery.md",
        "skill-discovery reference missing access date",
    )
    h.require_contains(
        "bbdfe742f853562e643a3d40d64476359d47881e39cef80a189283fa26d11ab9",
        "references/skill-discovery.md",
        "skill-discovery reference missing sha256",
    )
    h.require_contains(
        "DESCRIPTION TRIGGERS NOT WORKFLOW",
        "chains/chain-jail/skill-discovery.md",
        "skill-discovery leaf missing iron law text",
    )
    h.require_contains(
        "skill discovery optimization",
        "evals/triggers.json",
        "triggers missing skill discovery optimization phrase",
    )
    h.require_contains(
        "description summarizes workflow",
        "evals/triggers.json",
        "triggers missing description summarizes workflow phrase",
    )
    h.require_contains(
        "skill-discovery.md",
        "chains/chain-jail/extract-aspect.md",
        "extract-aspect missing skill-discovery leaf",
    )
    _, sdo_out = h.run_py("scripts/lib/sdo.py")
    if not re.search(r"^SDO checklist=yes", sdo_out, re.M):
        h.fail_msg("sdo missing checklist=yes")
    if not re.search(r"^PRIN \d+ id=", sdo_out, re.M):
        h.fail_msg("sdo missing PRIN line")
    if not re.search(r"^MUST:", sdo_out, re.M):
        h.fail_msg("sdo missing MUST line")
    if not re.search(r"^GATE rule=", sdo_out, re.M):
        h.fail_msg("sdo missing GATE line")
    if "DESCRIPTION_TRIGGERS_NOT_WORKFLOW" not in sdo_out:
        h.fail_msg("sdo missing iron law token")
    rc, _ = h.run_py("scripts/lib/sdo.py", "--reject-workflow-summary")
    if rc == 0:
        h.fail_msg("sdo --reject-workflow-summary should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/sdo.py", "--reject-workflow-summary")
        if not re.search(r"^REJECT WORKFLOW-SUMMARY:", reject, re.M):
            h.fail_msg("reject-workflow-summary missing REJECT line")
        else:
            h.pass_msg("sdo --reject-workflow-summary hard-gates")
    rc, _ = h.run_py("scripts/lib/sdo.py", "--reject-no-trigger")
    if rc == 0:
        h.fail_msg("sdo --reject-no-trigger should exit non-zero")
    else:
        _, reject = h.run_py("scripts/lib/sdo.py", "--reject-no-trigger")
        if not re.search(r"^REJECT NO-TRIGGER:", reject, re.M):
            h.fail_msg("reject-no-trigger missing REJECT line")
        else:
            h.pass_msg("sdo --reject-no-trigger hard-gates")
    rc, sdo_ok = h.run_py(
        "scripts/lib/sdo.py",
        "--check-description",
        "Use when creating or editing skills and the YAML description "
        "might summarize the workflow",
    )
    if rc != 0 or "SDO OK:" not in sdo_ok:
        h.fail_msg("sdo --check-description should accept trigger descriptions")
    else:
        h.pass_msg("sdo --check-description accepts trigger descriptions")
    rc, sdo_bad = h.run_py(
        "scripts/lib/sdo.py",
        "--check-description",
        "Use when executing plans - dispatches subagent per task with "
        "code review between tasks",
    )
    if rc == 0 or "SDO FAIL:" not in sdo_bad:
        h.fail_msg("sdo --check-description should reject workflow summary")
    else:
        h.pass_msg("sdo --check-description rejects workflow summary")
    _, sdo_sh = h.run_sh("scripts/sdo.sh")
    if not re.search(r"^SDO checklist=yes", sdo_sh, re.M):
        h.fail_msg("sdo.sh missing checklist card")
    _, rout_sdo = h.run_py("scripts/lib/route.py", "skill discovery optimization")
    if "emperor-capture" not in rout_sdo:
        h.fail_msg("route.py skill discovery optimization → capture")
    else:
        h.pass_msg("route.py skill discovery optimization → emperor-capture")


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
