#!/usr/bin/env python3
"""Rigor judge — cheap deterministic effort_class recommendation (PR2).

Stamps recommended effort_class before gates when no explicit override.
Heuristics from ask text + cheap repo signals (scope, blast radius,
secrets/auth/forge paths, archaeology markers). NO LLM loop on tiny.
Optional judgment adapter (scripts/lib/judgment.py) hooks only when
class is ambiguous AND judgment.provider != off; still skips clear tiny.
Provider off / no key / timeout → None; existing gates decide.

Precedence (user override always wins):
  1. explicit --effort-class / effort_class arg
  2. ask phrases: "use full rigor" / "full rigor" / "maximum rigor"
  3. config rigor.default when auto_detect_little=false
  4. deterministic heuristics (ask + repo signals)
  5. config default (tiny)

CLI: emperor rigor-judge [--ask TEXT|--ask-file PATH] [--root PATH]
     [--effort-class CLASS] [--as-json]
Thin twins: scripts/rigor-judge.sh / scripts/rigor-judge.ps1
Light skill: skills/meta-rigor/SKILL.md + references/meta/*
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Sequence

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import config as et_config  # noqa: E402

LEAF = "references/meta/rigor-tiers.md"
EFFORT_CLASSES = et_config.EFFORT_CLASSES
_CLASS_RANK = {"tiny": 0, "small": 1, "medium": 2, "large": 3}

_TINY_HINTS = re.compile(
    r"(?i)\b("
    r"typo|rename|one[- ]line|1[- ]line|two[- ]line|2[- ]line|"
    r"bump\s+version|fix\s+typo|single[- ]file|one[- ]file|"
    r"trivial|nit|wording|changelog\s+only|docs?\s+typo"
    r")\b"
)
_SMALL_HINTS = re.compile(
    r"(?i)\b("
    r"add\s+flag|wire|thin\s+twin|alias|fixture|HARD-GATE|"
    r"lockstep|version\s+bump|small\s+fix|patch|knob"
    r")\b"
)
_LARGE_HINTS = re.compile(
    r"(?i)\b("
    r"refactor|rewrite|migrate|migration|architecture|overhaul|"
    r"multi[- ]repo|platform|redesign|from\s+scratch"
    r")\b"
)
_FULL_RIGOR = re.compile(
    r"(?i)\b("
    r"use\s+full\s+rigor|full\s+rigor|maximum\s+rigor|"
    r"effort[_ -]?class\s*[:=]\s*(?:full|large)|"
    r"force\s+(?:full|large)\s+class"
    r")\b"
)
_SECRETS_AUTH = re.compile(
    r"(?i)\b("
    r"secret|secrets|credential|credentials|auth(?:entication|orization)?|"
    r"token|api[_ -]?key|password|vault|1password|"
    r"pin[- ]?and[- ]?consent|forge|pull\s+request|\bPR\b|"
    r"quarantine|steal[- ]?consent|enlist"
    r")\b"
)
_ARCHAEOLOGY = re.compile(
    r"(?i)\b("
    r"excavate|archaeolog|lost\s+tree|ancient|pascal|\.pas\b|cobol|"
    r"fortran|assembly|\.asm\b|vhdl|ada\b|forth|rom\b|unmarked\s+binar|"
    r"museum|identify\s+stack"
    r")\b"
)
_BLAST = re.compile(
    r"(?i)\b("
    r"multi[- ]file|across\s+packages?|public\s+API|breaking\s+change|"
    r"wide\s+blast|many\s+files|whole\s+(?:module|package|crate)|"
    r"cross[- ]cutting"
    r")\b"
)
_MEDIUM_HINTS = re.compile(
    r"(?i)\b("
    r"feature|endpoint|schema|new\s+command|gate|HARD-GATE|"
    r"worktree|dispatch|critique|harness"
    r")\b"
)

# Cheap path probes under repo root (existence only — no deep walk).
_SECRET_PATHS = (
    ".emperor/secrets",
    "scripts/lib/secrets_broker.py",
    "scripts/lib/forge.py",
    "scripts/lib/pin_consent.py",
)
_ARCH_PATHS = (
    "skills/emperor-excavate/SKILL.md",
    "references/archaeology.md",
)
_FORGE_PATHS = (
    "skills/emperor-forge/SKILL.md",
    "scripts/lib/forge.py",
)


def _primary_reason(reasons: list[str]) -> str:
    """Decisive class-changing step: last bump, else sole/last base reason."""
    bumps = [r for r in reasons if "bump" in r]
    if bumps:
        return bumps[-1]
    if reasons:
        return reasons[-1]
    return ""


@dataclass
class Judgment:
    effort_class: str
    reasons: list[str] = field(default_factory=list)
    signals: dict[str, Any] = field(default_factory=dict)
    override: bool = False
    source: str = "heuristics"
    primary_reason: str = ""

    def __post_init__(self) -> None:
        if not self.primary_reason:
            self.primary_reason = _primary_reason(self.reasons)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _max_class(a: str, b: str) -> str:
    if _CLASS_RANK.get(a, 0) >= _CLASS_RANK.get(b, 0):
        return a
    return b


def _repo_signals(root: Path | None) -> dict[str, Any]:
    """Cheap existence probes — no recursive archaeology museum walk."""
    out: dict[str, Any] = {
        "secrets_paths": False,
        "forge_paths": False,
        "archaeology_paths": False,
        "archaeology_depth": "off",
        "sandbox_enabled": False,
        "sot_enabled": False,
    }
    if root is None:
        return out
    root = Path(root)
    out["secrets_paths"] = any((root / p).exists() for p in _SECRET_PATHS)
    out["forge_paths"] = any((root / p).exists() for p in _FORGE_PATHS)
    out["archaeology_paths"] = any((root / p).exists() for p in _ARCH_PATHS)
    try:
        cfg = et_config.load_config(root)
        feats = cfg.get("features") or {}
        if isinstance(feats, dict):
            out["archaeology_depth"] = str(feats.get("archaeology_depth", "off"))
            out["sandbox_enabled"] = bool(feats.get("sandbox", False))
            out["sot_enabled"] = bool(feats.get("sot", False))
    except Exception:
        pass
    return out


def recommend_effort_class(
    ask: str,
    *,
    root: Path | None = None,
    explicit_class: str | None = None,
) -> Judgment:
    """Recommend effort_class. User override always wins."""
    ask = (ask or "").strip()
    root_resolved = et_config._resolve_root(root) if root is not None else (
        et_config._resolve_root(None)
    )
    signals = _repo_signals(root_resolved)
    signals["ask_len"] = len(ask)

    # 1. Explicit class override
    if explicit_class:
        try:
            cls = et_config.normalize_effort_class(explicit_class)
        except ValueError as exc:
            raise ValueError(str(exc)) from exc
        return Judgment(
            cls,
            reasons=[f"explicit override → {cls}"],
            signals=signals,
            override=True,
            source="explicit",
        )

    # 2. Ask phrase: use full rigor
    if ask and _FULL_RIGOR.search(ask):
        return Judgment(
            "large",
            reasons=["ask requests full/maximum rigor → large"],
            signals=signals,
            override=True,
            source="ask-override",
        )

    # 3. Config default when auto_detect_little is off
    if not et_config.auto_detect_little(root_resolved):
        cls = et_config.default_effort_class(root_resolved)
        return Judgment(
            cls,
            reasons=[f"auto_detect_little=false → config default {cls}"],
            signals=signals,
            override=False,
            source="config-default",
        )

    # 4. Deterministic heuristics
    reasons: list[str] = []
    cls = "tiny"

    if not ask:
        cls = et_config.default_effort_class(root_resolved)
        reasons.append(f"empty ask → config default {cls}")
        return Judgment(cls, reasons=reasons, signals=signals, source="heuristics")

    if _LARGE_HINTS.search(ask) or len(ask) >= 800:
        cls = "large"
        reasons.append("large-hint or long ask")
    elif _TINY_HINTS.search(ask) or len(ask) <= 80:
        cls = "tiny"
        reasons.append("tiny-hint or short ask")
    elif _SMALL_HINTS.search(ask) or len(ask) <= 240:
        cls = "small"
        reasons.append("small-hint or medium-short ask")
    elif _MEDIUM_HINTS.search(ask) or len(ask) <= 500:
        cls = "medium"
        reasons.append("medium-hint or mid-length ask")
    else:
        cls = "large"
        reasons.append("fallback long ask → large")

    # Blast radius bump
    if _BLAST.search(ask):
        prev = cls
        cls = _max_class(cls, "medium")
        if cls != prev:
            reasons.append(f"blast-radius bump {prev}→{cls}")

    # Secrets / auth / forge in ask → at least small (iron consent stays)
    if _SECRETS_AUTH.search(ask):
        prev = cls
        cls = _max_class(cls, "small")
        if cls != prev:
            reasons.append(f"secrets/auth/forge ask bump {prev}→{cls}")
        # Public forge / PR language → medium floor
        if re.search(r"(?i)\b(pull\s+request|\bPR\b|forge|public)\b", ask):
            prev = cls
            cls = _max_class(cls, "medium")
            if cls != prev:
                reasons.append(f"forge/PR bump {prev}→{cls}")

    # Archaeology markers in ask
    if _ARCHAEOLOGY.search(ask):
        depth = str(signals.get("archaeology_depth") or "off")
        # Excavate/lost-tree asks are never tiny; depth only raises the floor.
        floor = "medium"
        if depth in ("full", "2"):
            floor = "large"
        prev = cls
        cls = _max_class(cls, floor)
        if cls != prev:
            reasons.append(f"archaeology ask bump {prev}→{cls} (depth={depth})")

    # Repo path signals only nudge when ask already touches those domains
    # (avoid inflating every tiny typo because forge.py exists in-tree).
    if signals.get("secrets_paths") and _SECRETS_AUTH.search(ask):
        signals["repo_secrets_nudge"] = True
    if signals.get("archaeology_paths") and _ARCHAEOLOGY.search(ask):
        signals["repo_arch_nudge"] = True

    # features.sandbox / sot: informational only here (gated elsewhere)
    signals["recommended"] = cls

    result = Judgment(cls, reasons=reasons, signals=signals, source="heuristics")
    return _maybe_optional_judgment(ask, result, root_resolved)


def _is_clear_tiny(ask: str, judgment: Judgment) -> bool:
    """Tiny happy-path — NEVER call optional judgment provider."""
    if judgment.override:
        return judgment.effort_class == "tiny"
    if judgment.effort_class != "tiny":
        return False
    ask = ask or ""
    if _TINY_HINTS.search(ask) or len(ask) <= 80:
        return True
    return False


def _is_ambiguous(ask: str, judgment: Judgment) -> bool:
    """True when heuristics leave class disputed / mid-zone (not clear tiny)."""
    if judgment.override:
        return False
    if judgment.source != "heuristics":
        return False
    if _is_clear_tiny(ask, judgment):
        return False
    ask = ask or ""
    strong_tiny = bool(_TINY_HINTS.search(ask))
    strong_large = bool(_LARGE_HINTS.search(ask) or _FULL_RIGOR.search(ask))
    bump_n = sum(1 for r in judgment.reasons if "bump" in r)
    # Competing strong hints or multiple bumps → dispute
    if strong_tiny and strong_large:
        return True
    if bump_n >= 1 and judgment.effort_class in ("small", "medium"):
        return True
    # Mid-length ask without a single strong class hint
    if 80 < len(ask) < 800 and not strong_tiny and not strong_large:
        if not _SMALL_HINTS.search(ask) and not _MEDIUM_HINTS.search(ask):
            return True
        # small/medium hint present but another domain signal also fired
        if bump_n >= 1:
            return True
    # Explicit dispute marker from callers
    return False


def _maybe_optional_judgment(
    ask: str, judgment: Judgment, root: Path | None
) -> Judgment:
    """Optional judgment hook — only ambiguous + provider != off; skip tiny clear."""
    if _is_clear_tiny(ask, judgment):
        judgment.signals["optional_judgment"] = "skipped_tiny_clear"
        return judgment
    try:
        provider = et_config.judgment_provider(root)
    except Exception:
        judgment.signals["optional_judgment"] = "skipped_config_error"
        return judgment
    if provider == "off":
        judgment.signals["optional_judgment"] = "skipped_provider_off"
        return judgment
    if not _is_ambiguous(ask, judgment):
        judgment.signals["optional_judgment"] = "skipped_not_ambiguous"
        return judgment
    try:
        import judgment as et_judgment  # local scripts/lib
    except Exception:
        judgment.signals["optional_judgment"] = "skipped_import_error"
        return judgment
    ctx = {
        "use_case": "effort_class_dispute",
        "heuristic_class": judgment.effort_class,
        "reasons": list(judgment.reasons),
        "ask_len": len(ask or ""),
    }
    prompt = (
        "Resolve effort_class dispute. Heuristic recommends "
        f"{judgment.effort_class}. Ask follows.\n\n{ask}"
    )
    try:
        out = et_judgment.judge(prompt, ctx, root=root)
    except Exception:
        out = None
    if out is None:
        judgment.signals["optional_judgment"] = None
        judgment.signals["optional_judgment_soft"] = "none"
        return judgment
    judgment.signals["optional_judgment"] = out
    # Soft advisory only — never overrides user override (already returned earlier).
    # May nudge heuristics class when decision names a valid effort_class.
    decision = str(out.get("decision") or "").strip().lower()
    try:
        nudged = et_config.normalize_effort_class(decision)
    except ValueError:
        return judgment
    if nudged != judgment.effort_class:
        judgment.reasons.append(
            f"optional judgment nudge {judgment.effort_class}→{nudged}"
        )
        judgment.effort_class = nudged
        judgment.source = "optional-judgment"
        judgment.signals["recommended"] = nudged
    judgment.primary_reason = _primary_reason(judgment.reasons)
    return judgment


def format_card() -> str:
    return (
        "RIGOR-JUDGE checklist=yes\n"
        f"RIGOR-JUDGE leaf={LEAF}\n"
        "RIGOR-JUDGE iron=USER_OVERRIDE_WINS\n"
        "STEP 1 id=override name=Honor explicit class / full-rigor phrase "
        "et=--effort-class or 'use full rigor' always wins\n"
        "STEP 2 id=detect name=Cheap heuristics (no LLM on tiny) "
        "et=ask hints + blast/secrets/forge/archaeology signals\n"
        "STEP 3 id=stamp name=Stamp effort_class on ask→spec emit "
        "et=when auto_detect_little and no class declared\n"
        "STEP 4 id=meta name=Load meta pack on demand "
        "et=references/meta/* (SessionStart lists paths only)\n"
        "\n"
        "MUST: Recommend before gates when no override; never LLM-loop on tiny.\n"
        "MUST-NOT: invent k8s/Nen/museum; soften iron consent; ignore user class.\n"
        "HONESTY: primary_reason = last class-changing bump (else sole base); "
        "reasons list kept for full trail.\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="emperor-rigor-judge",
        description="Cheap deterministic effort_class recommendation (no LLM)",
    )
    p.add_argument("--root", default=None, help="Project root")
    p.add_argument("--ask", default=None, help="Ask text")
    p.add_argument("--ask-file", type=Path, default=None, help="Read ask from file")
    p.add_argument(
        "--effort-class",
        default=None,
        help="Explicit override (aliases standard→small, full→large)",
    )
    p.add_argument("--as-json", action="store_true", help="Print Judgment JSON")
    p.add_argument(
        "positional_ask",
        nargs="?",
        default=None,
        help="Ask text (positional)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    ask = ""
    if args.ask_file is not None:
        if not args.ask_file.is_file():
            print(f"rigor-judge FAIL: no such ask file: {args.ask_file}", file=sys.stderr)
            return 2
        ask = args.ask_file.read_text(encoding="utf-8", errors="replace")
    elif args.ask:
        ask = args.ask
    elif args.positional_ask:
        ask = args.positional_ask
    elif not sys.stdin.isatty():
        ask = sys.stdin.read()

    if not ask and not args.effort_class and args.ask is None and args.ask_file is None and args.positional_ask is None:
        # No input → card
        if not sys.stdin.isatty():
            pass
        else:
            sys.stdout.write(format_card())
            return 0

    root = Path(args.root).resolve() if args.root else None
    try:
        j = recommend_effort_class(
            ask, root=root, explicit_class=args.effort_class
        )
    except ValueError as exc:
        print(f"rigor-judge FAIL: {exc}", file=sys.stderr)
        return 2

    if args.as_json:
        sys.stdout.write(json.dumps(j.to_dict(), indent=2) + "\n")
    else:
        print(f"effort_class: {j.effort_class}")
        print(f"source: {j.source}")
        print(f"override: {'yes' if j.override else 'no'}")
        print(f"reason: {j.primary_reason}")
        if len(j.reasons) > 1:
            for r in j.reasons:
                print(f"detail: {r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
