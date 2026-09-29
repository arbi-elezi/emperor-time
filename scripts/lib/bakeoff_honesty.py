#!/usr/bin/env python3
"""Prove bakeoff.md / this-upgrade.md honesty against disk leaves.

Local mechanism paths must exist and be named in bakeoff.md.
Live defect-rate vs Superpowers must stay labeled UNVERIFIABLE in both
docs. No fake numbers — this helper only checks labels and presence.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# (short name, path relative to repo root, substrings bakeoff.md must contain)
LEAVES: list[tuple[str, str, tuple[str, ...]]] = [
    ("plans", "scripts/lib/work_order.py", ("plans", "work_order", "Task-N", "reject-tbd")),
    ("claim-audit", "scripts/lib/claim_audit.py", ("claim-audit", "claim_audit", "reject-unaudited", "CLAIM AUDIT")),
    ("quarantine", "scripts/lib/quarantine.py", ("quarantine", "reject-unquarantined", "CONJECTURE", "ADMITTED")),
    ("consent", "scripts/lib/consent.py", ("consent", "reject-no-consent", "CONSENT", "consent-protocol")),
    ("steal-flow", "scripts/lib/steal_flow.py", ("steal-flow", "reject-no-signin", "reject-no-dispatch-layout", "reject-unbounded-swarm")),
    ("pin-and-consent", "scripts/lib/pin_consent.py", ("pin-and-consent", "reject-unpinned", "reject-no-skill-consent", "check-pin-consent")),
    ("ask-spec", "scripts/lib/ask_spec.py", ("ask-spec", "reject-no-spec", "require-spec", "check-ask-spec", "effort_class")),
    ("proportionality", "scripts/lib/proportionality.py", ("proportionality", "reject-over-verify", "check-proportionality", "record-cycle", "bump_and_check", "MISSING_CLASS_DEFAULTS_TINY")),
    ("forge-pr-consent", "scripts/lib/forge.py", ("forge", "reject-no-pr-consent", "check-pr-consent", "EMPEROR_CONSENT_PR")),
    ("heal-verify", "scripts/lib/heal_verify.py", ("heal-verify", "reject-no-triad", "reject-no-postmortem", "heal-and-verify")),
    ("reproduce", "scripts/lib/reproduce.py", ("reproduce", "reject-no-repro", "reject-no-combat-ledger", "reproduce-and-bisect")),
    ("triage", "scripts/lib/triage.py", ("triage", "reject-no-triage", "reject-no-snapshot", "holy-triage")),
    ("process-heal", "scripts/lib/process_heal.py", ("process-heal", "reject-no-register", "reject-no-reentry", "process-healing")),
    ("review-isolation", "scripts/lib/review_pack.py", ("review-pack", "reject-unisolated", "reject-author-diary", "check-isolation", "hetero-critique isolation")),
    ("super-context", "scripts/lib/context.py", ("super-context", "thoughttrail", "reject-no-graph", "reject-no-trail", "check-context", "GRAPH_THEN_TRAIL")),
    ("blind-secrets-broker", "scripts/lib/secrets_broker.py", ("secrets list", "reject-secret-leak", "check-env-redacted", "blind-secrets-broker")),
    ("workspace-env", "scripts/lib/workspace_env.py", ("env show", "env sync", "managed.env", "blind-secrets-broker")),
    ("sandbox-engine", "scripts/lib/sandbox_engine.py", ("sandbox plan", "runtime use", "podman", "k8s", "isolate", "sandbox-engine")),
    ("sot-artifact-sync", "scripts/lib/super_context.py", ("sot add-plugin", "artifacts sync", "clone --mirror", "sot-artifact-sync")),
    ("critique", "scripts/lib/critique.py", ("critique", "reject-incomplete-critique", "eight-count", "Checked")),
    ("verdict", "scripts/lib/verdict.py", ("verdict", "reject-hidden-breach", "Breach Register", "claim audit")),
    ("finish", "skills/emperor-forge/finish-menu.md", ("finish",)),
    ("finish-py", "scripts/lib/finish.py", ("finish.py", "finish menu", "reject-red-suite", "require-green")),
    ("activate", "scripts/lib/activate.py", ("activate", "must-route")),
    ("must-route", "skills/emperor-resume/must-route.md", ("must-route",)),
    ("grill", "skills/emperor-require-design/grill-checklist.md", ("grill", "reject-no-path", "check-path", "path taxonomy")),
    ("grill-py", "scripts/lib/grill.py", ("grill.py", "reject-no-path", "reject-stage-skip", "check-path")),
    (
        "debug-phases",
        "skills/emperor-heal/debug-four-phases.md",
        ("debug", "four"),
    ),
    ("tdd", "skills/emperor-tdd/red-green-refactor.md", ("tdd",)),
    (
        "worktree-iso",
        "skills/emperor-worktree/isolation-checklist.md",
        ("worktree", "isolation"),
    ),
    (
        "review",
        "skills/emperor-verify/request-review-checklist.md",
        ("request-review",),
    ),
    (
        "receive-review",
        "skills/emperor-verify/receive-review-checklist.md",
        ("receive-review", "receive"),
    ),
    (
        "execute-plans",
        "skills/emperor-build/executing-plans-checklist.md",
        ("execute", "executing-plans"),
    ),
    (
        "subagent-driven",
        "skills/emperor-build/subagent-driven-checklist.md",
        ("subagent", "subagent-driven"),
    ),
    (
        "parallel-dispatch",
        "skills/emperor-dispatch/parallel-dispatch-checklist.md",
        ("parallel", "parallel-dispatch"),
    ),
    (
        "author",
        "chains/chain-jail/authoring-checklist.md",
        ("authoring",),
    ),
    (
        "evidence",
        "skills/emperor-verify/verification-checklist.md",
        ("evidence", "verification"),
    ),
    ("arch-pas", "evals/fixtures/lost-pas/HELLO.PAS", ("lost-pas",)),
    ("arch-asm", "evals/fixtures/lost-asm/FOO.ASM", ("lost-asm",)),
    ("arch-cbl", "evals/fixtures/lost-cbl/HELLO.CBL", ("lost-cbl",)),
    ("arch-f90", "evals/fixtures/lost-f90/HELLO.F90", ("lost-f90",)),
    ("arch-vhd", "evals/fixtures/lost-vhd/HELLO.VHD", ("lost-vhd",)),
    ("arch-ada", "evals/fixtures/lost-ada/HELLO.ADB", ("lost-ada",)),
    ("arch-fs", "evals/fixtures/lost-fs/HELLO.FS", ("lost-fs",)),
    ("arch-lisp", "evals/fixtures/lost-lisp/HELLO.LISP", ("lost-lisp",)),
    ("arch-prolog", "evals/fixtures/lost-prolog/HELLO.PRO", ("lost-prolog",)),
    ("arch-tcl", "evals/fixtures/lost-tcl/HELLO.TCL", ("lost-tcl",)),
    ("arch-erl", "evals/fixtures/lost-erl/HELLO.ERL", ("lost-erl",)),
    ("arch-rex", "evals/fixtures/lost-rex/HELLO.REX", ("lost-rex",)),
    ("arch-mod", "evals/fixtures/lost-mod/HELLO.MOD", ("lost-mod",)),
    ("arch-a68", "evals/fixtures/lost-a68/HELLO.A68", ("lost-a68",)),
    ("arch-a60", "evals/fixtures/lost-a60/HELLO.A60", ("lost-a60",)),
    ("arch-alw", "evals/fixtures/lost-alw/HELLO.ALW", ("lost-alw",)),
    ("arch-icn", "evals/fixtures/lost-icn/HELLO.ICN", ("lost-icn",)),
    ("arch-obn", "evals/fixtures/lost-obn/HELLO.OBN", ("lost-obn",)),
    ("arch-sno", "evals/fixtures/lost-sno/HELLO.SNO", ("lost-sno",)),
    ("arch-cim", "evals/fixtures/lost-cim/HELLO.SIM", ("lost-cim",)),
    ("arch-apl", "evals/fixtures/lost-apl/HELLO.APL", ("lost-apl",)),
    ("arch-bcpl", "evals/fixtures/lost-bcpl/HELLO.B", ("lost-bcpl",)),
    ("arch-pli", "evals/fixtures/lost-pli/HELLO.PLI", ("lost-pli",)),
    ("arch-st", "evals/fixtures/lost-st/HELLO.ST", ("lost-st",)),
    ("arch-ps", "evals/fixtures/lost-ps/HELLO.PS", ("lost-ps",)),
    ("arch-bas", "evals/fixtures/lost-bas/HELLO.BAS", ("lost-bas",)),
    ("arch-scm", "evals/fixtures/lost-scm/HELLO.SCM", ("lost-scm",)),
    ("arch-awk", "evals/fixtures/lost-awk/HELLO.AWK", ("lost-awk",)),
    ("arch-sed", "evals/fixtures/lost-sed/HELLO.SED", ("lost-sed",)),
    ("arch-m4", "evals/fixtures/lost-m4/HELLO.M4", ("lost-m4",)),
    ("arch-ed", "evals/fixtures/lost-ed/HELLO.ED", ("lost-ed",)),
    ("arch-make", "evals/fixtures/lost-make/Makefile", ("lost-make",)),
    ("arch-dc", "evals/fixtures/lost-dc/HELLO.DC", ("lost-dc",)),
    ("arch-lex", "evals/fixtures/lost-lex/HELLO.L", ("lost-lex",)),
    ("arch-yacc", "evals/fixtures/lost-yacc/HELLO.Y", ("lost-yacc",)),
    ("arch-roff", "evals/fixtures/lost-roff/HELLO.ROFF", ("lost-roff",)),
    ("arch-perl", "evals/fixtures/lost-pl/HELLO.PL", ("lost-pl",)),
    ("arch-bc", "evals/fixtures/lost-bc/HELLO.BC", ("lost-bc",)),
    ("arch-expect", "evals/fixtures/lost-expect/HELLO.EXP", ("lost-expect",)),
    ("arch-lua", "evals/fixtures/lost-lua/HELLO.LUA", ("lost-lua",)),
    ("arch-ruby", "evals/fixtures/lost-ruby/HELLO.RB", ("lost-ruby",)),
    ("arch-go", "evals/fixtures/lost-go/HELLO.go", ("lost-go",)),
    ("arch-rust", "evals/fixtures/lost-rust/HELLO.rs", ("lost-rust",)),
    ("arch-c", "evals/fixtures/lost-c/HELLO.c", ("lost-c",)),
    ("arch-js", "evals/fixtures/lost-js/HELLO.js", ("lost-js",)),
    ("arch-py", "evals/fixtures/lost-py/HELLO.py", ("lost-py",)),
    ("arch-ts", "evals/fixtures/lost-ts/HELLO.ts", ("lost-ts",)),
    ("arch-bash", "evals/fixtures/lost-sh/HELLO.sh", ("lost-sh",)),
    ("arch-php", "evals/fixtures/lost-php/HELLO.php", ("lost-php",)),
    ("arch-sql", "evals/fixtures/lost-sql/HELLO.sql", ("lost-sql",)),
    ("arch-jq", "evals/fixtures/lost-jq/HELLO.jq", ("lost-jq",)),
    ("arch-xslt", "evals/fixtures/lost-xsl/HELLO.xsl", ("lost-xsl",)),
    ("arch-xml", "evals/fixtures/lost-xml/HELLO.xml", ("lost-xml",)),
    ("arch-yaml", "evals/fixtures/lost-yaml/HELLO.yaml", ("lost-yaml",)),
    ("arch-toml", "evals/fixtures/lost-toml/HELLO.toml", ("lost-toml",)),
    ("arch-html", "evals/fixtures/lost-html/HELLO.html", ("lost-html",)),
    ("arch-csv", "evals/fixtures/lost-csv/HELLO.csv", ("lost-csv",)),
    ("arch-json", "evals/fixtures/lost-json/HELLO.json", ("lost-json",)),
    ("arch-ini", "evals/fixtures/lost-ini/HELLO.ini", ("lost-ini",)),
    ("arch-plist", "evals/fixtures/lost-plist/HELLO.plist", ("lost-plist",)),
    ("arch-eml", "evals/fixtures/lost-eml/HELLO.eml", ("lost-eml",)),
    ("arch-zip", "evals/fixtures/lost-zip/HELLO.zip", ("lost-zip",)),
    ("arch-tar", "evals/fixtures/lost-tar/HELLO.tar", ("lost-tar",)),
    ("arch-gz", "evals/fixtures/lost-gz/HELLO.gz", ("lost-gz",)),
    ("arch-targz", "evals/fixtures/lost-targz/HELLO.tar.gz", ("lost-targz",)),
    ("arch-whl", "evals/fixtures/lost-whl/HELLO.whl", ("lost-whl",)),
    ("arch-jar", "evals/fixtures/lost-jar/HELLO.jar", ("lost-jar",)),
    ("arch-war", "evals/fixtures/lost-war/HELLO.war", ("lost-war",)),
    ("arch-apk", "evals/fixtures/lost-apk/HELLO.apk", ("lost-apk",)),
    ("arch-docx", "evals/fixtures/lost-docx/HELLO.docx", ("lost-docx",)),
    ("arch-xlsx", "evals/fixtures/lost-xlsx/HELLO.xlsx", ("lost-xlsx",)),
    ("arch-tsv", "evals/fixtures/lost-tsv/HELLO.tsv", ("lost-tsv",)),
    ("arch-jsonl", "evals/fixtures/lost-jsonl/HELLO.jsonl", ("lost-jsonl",)),
    ("arch-pptx", "evals/fixtures/lost-pptx/HELLO.pptx", ("lost-pptx",)),
    ("arch-pdf", "evals/fixtures/lost-pdf/HELLO.pdf", ("lost-pdf",)),
    ("arch-png", "evals/fixtures/lost-png/HELLO.png", ("lost-png",)),
    ("arch-wav", "evals/fixtures/lost-wav/HELLO.wav", ("lost-wav",)),
    ("arch-jpg", "evals/fixtures/lost-jpg/HELLO.jpg", ("lost-jpg",)),
    ("gate-py", "scripts/lib/gate.py", ("gate.py", "mechanical")),
    ("identify-py", "scripts/lib/identify.py", ("identify.py", "survey")),
    ("eval-py", "scripts/lib/eval.py", ("eval.py", "structural eval")),
    ("route-py", "scripts/lib/route.py", ("route", "fortran", ".f90", "vhdl", ".vhd", "ada", ".adb", "forth", ".fs", "pforth", "lisp", ".lisp", "clisp", "prolog", ".pro", "swipl", "tcl", ".tcl", "tclsh", "erlang", ".erl", "escript", "rexx", ".rex", "regina", "modula", ".mod", "gm2", "algol", ".a68", "a68g", "marst", ".a60", "algol60", "awe", ".alw", "algolw", "icont", ".icn", "iconx", "voc", ".obn", "oberon", "snobol4", ".sno", "snobol", "cim", ".sim", "simula", "apl", ".apl", "gnu-apl", "bcpl", "cintsys", "cintcode", ".bcpl", "plic", "pli", "pl1", "iron-spring", ".pli", ".pl1", "gst", "smalltalk", "gnu-smalltalk", "ghostscript", "postscript", "bwbasic", "bywater", ".bas", "csi", "chicken", "chicken-scheme", ".scm", "gawk", "awk", "nawk", ".awk", "sed", "gsed", ".sed", "m4", "gm4", ".m4", "ed", "gnu-ed", ".ed", "gmake", "gnu-make", ".mk", ".mak", "makefile", "dc", "gnu-dc", ".dc", "lex", "flex", "gnu-flex", ".lex", "yacc", "bison", "gnu-bison", ".y", "roff", "nroff", "groff", "gnu-groff", ".roff", "perl", "perl5", ".pm", "bc", "gnu-bc", "expect", "tcl-expect", ".exp", "lua", "lua5.4", ".lua", "ruby", "ruby3.3", ".rb", "golang", "go1.24", ".go", "rust", "rustc", "rust1.85", ".rs", "gcc", "gcc14", "c11", ".c", "nodejs", "node20", "javascript", ".js", "python3", "python3.13", "cpython", ".py", "typescript", "typescript5", "tsc", "ts5", ".ts", "bash", "bash5", "bash5.2", "gnu-bash", ".sh", "php", "php8", "php8.4", "php-cli", ".php", "sqlite", "sqlite3", "sqlite3.46", ".sql", "jq", "jq1.7", "jqlang", ".jq", "xsltproc", "libxslt", "xslt", ".xsl", ".xslt", "xmllint", "libxml2", "xml", ".xml", "yq", "kislyuk-yq", "yq3.4", "yaml", ".yaml", ".yml", "tomlq", "kislyuk-tomlq", "tomlq3.4", "toml", ".toml", "tidy", "html-tidy", "tidy5.8", "html", ".html", ".htm", "csv", "pycsv", "csv1.0", ".csv", "pyjson", "json2.0", ".json", "ini", "pyini", "configparser", ".ini", "plist", "pyplist", "plistlib", ".plist", "eml", "pyemail", "email.parser", ".eml", "zip", "pyzip", "zipfile", ".zip", "tar", "pytar", "tarfile", ".tar", "gzip", "pygzip", "gzipfile", ".gz", "targz", "tarball", "pytargz", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz", "whl", "pywhl", "wheel", ".whl", "jar", "pyjar", "java-archive", ".jar", "war", "pywar", "web-archive", ".war", "apk", "pyapk", "android-package", ".apk", "docx", "pydocx", "ooxml-word", ".docx", "xlsx", "pyxlsx", "ooxml-excel", ".xlsx", "tsv", "pytsv", "tab-separated", ".tsv", "jsonl", "pyjsonl", "ndjson", ".jsonl", "pptx", "pypptx", "ooxml-pptx", ".pptx", "pdf", "pdftotext", "poppler", ".pdf", "png", "pillow", "pil", ".png", "wav", "ffmpeg", "ffprobe", ".wav", "jpeg", "jpg", ".jpg", ".jpeg")),
    ("done-py", "scripts/lib/done.py", ("done.py", "DONE probes")),
    (
        "silent-boot-zsh",
        "scripts/emperor.zsh",
        ("emperor.zsh", "silent-boot"),
    ),
    ("queue-py", "scripts/lib/queue.py", ("queue.py", "queue")),
    ("forge-py", "scripts/lib/forge.py", ("forge.py", "forge")),
    ("review-pack-py", "scripts/lib/review_pack.py", ("review_pack.py", "review-pack")),
    ("dowse-py", "scripts/lib/dowse.py", ("dowse.py", "dowse")),
    ("install-py", "scripts/lib/install.py", ("install.py", "install")),
    ("host-py", "scripts/lib/host.py", ("host.py", "host.env")),
    ("boot-py", "scripts/lib/boot.py", ("boot.py", "silent-boot")),
    (
        "worktree-py",
        "scripts/lib/worktree.py",
        ("worktree.py", "worktree"),
    ),
    (
        "excavate-alias",
        "scripts/excavate.sh",
        ("excavate thin", "identify.py"),
    ),
    (
        "session-discovery",
        "scripts/lib/session_discovery.py",
        ("session_discovery.py", "session-discovery"),
    ),
    (
        "diagnose",
        "scripts/lib/diagnose.py",
        ("diagnose.py", "diagnose"),
    ),
    (
        "root-cause",
        "scripts/lib/root_cause.py",
        ("root_cause.py", "trace"),
    ),
    (
        "defense-in-depth",
        "scripts/lib/defense.py",
        ("defense.py", "defense"),
    ),
    (
        "condition-based-waiting",
        "scripts/lib/condition_wait.py",
        ("condition_wait.py", "wait"),
    ),
    (
        "find-polluter",
        "scripts/lib/polluter.py",
        ("polluter.py", "polluter"),
    ),
    (
        "pressure-academic",
        "scripts/lib/pressure.py",
        ("pressure.py", "pressure"),
    ),
    (
        "writing-good-tests",
        "scripts/lib/good_tests.py",
        ("good_tests.py", "good-tests"),
    ),
    (
        "testing-skills",
        "scripts/lib/skill_test.py",
        ("skill_test.py", "skill-test"),
    ),
    (
        "persuasion-principles",
        "scripts/lib/persuasion.py",
        ("persuasion.py", "persuasion"),
    ),
    (
        "skill-discovery",
        "scripts/lib/sdo.py",
        ("sdo.py", "sdo"),
    ),
    (
        "sdd-workspace",
        "scripts/lib/sdd_workspace.py",
        ("sdd_workspace.py", "sdd-workspace"),
    ),
    (
        "task-brief",
        "scripts/lib/task_brief.py",
        ("task_brief.py", "task-brief"),
    ),
    (
        "task-start",
        "scripts/lib/task_start.py",
        ("task_start.py", "task-start"),
    ),
    (
        "task-done",
        "scripts/lib/task_done.py",
        ("task_done.py", "task-done"),
    ),
    (
        "sdd-review-pack",
        "scripts/lib/sdd_review_pack.py",
        ("sdd_review_pack.py", "sdd-review-pack"),
    ),
]


BAKEOFF = Path("evals/bakeoff.md")
UPGRADE = Path("evals/fixtures/this-upgrade.md")

# Both docs must keep live bake-off rate honestly unlabeled as measured.
LIVE_RATE_NEEDLES = (
    "UNVERIFIABLE",
    "defect-rate",
    "Superpowers",
)


def _fail(msg: str) -> int:
    print(f"BAKEOFF HONESTY FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--cwd",
        type=Path,
        default=Path.cwd(),
        help="repo root (default: cwd)",
    )
    args = ap.parse_args()
    root: Path = args.cwd.resolve()

    bakeoff_path = root / BAKEOFF
    upgrade_path = root / UPGRADE
    if not bakeoff_path.is_file():
        return _fail(f"missing {BAKEOFF}")
    if not upgrade_path.is_file():
        return _fail(f"missing {UPGRADE}")

    bakeoff = bakeoff_path.read_text(encoding="utf-8")
    upgrade = upgrade_path.read_text(encoding="utf-8")
    bakeoff_l = bakeoff.lower()

    for name, rel, needles in LEAVES:
        path = root / rel
        if not path.is_file():
            return _fail(f"leaf {name}: missing path {rel}")
        for needle in needles:
            if needle.lower() not in bakeoff_l:
                return _fail(
                    f"leaf {name}: bakeoff.md missing mention {needle!r}"
                )

    for label, text in (("bakeoff.md", bakeoff), ("this-upgrade.md", upgrade)):
        for needle in LIVE_RATE_NEEDLES:
            if needle not in text:
                return _fail(f"{label} missing honesty needle {needle!r}")
        # Guard against inventing a measured win-rate.
        for bad in ("% better", "defect rate:", "wins N%", "N% lower"):
            if bad.lower() in text.lower():
                return _fail(f"{label} looks like a fake number phrase: {bad!r}")

    # Local mechanism must be labeled TESTED or VERIFIED somewhere in bakeoff.
    if "TESTED" not in bakeoff and "VERIFIED" not in bakeoff:
        return _fail("bakeoff.md missing TESTED/VERIFIED for local mechanism")

    print("BAKEOFF HONESTY OK")
    print(f"LEAVES checked={len(LEAVES)}")
    print("LIVE_DEFECT_RATE=UNVERIFIABLE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
