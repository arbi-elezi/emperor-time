#!/usr/bin/env python3
"""Optional judgment adapter stub (PR3 / v0.4.172).

Interface: judge(prompt, context) -> {decision, rationale} | None

Config (.emperor/config.yaml)::

    judgment:
      provider: off   # off | openrouter | openai_compat
      model: null     # no concrete model slug shipped (JEV)
      timeout_s: 8
      use_for: [effort_class_dispute, ship_no_ship, critique_conflict]

Env (openai_compat / openrouter only):
  EMPEROR_JUDGMENT_API_KEY
  EMPEROR_JUDGMENT_BASE_URL  — required for openai_compat; openrouter has default

Soft refuse → None (existing gates decide):
  provider off | missing key | missing model | timeout | HTTP/network error |
  use_case not in use_for | tiny_clear / happy-path marker in context |
  any attempt to *require* judgment for core factory

NEVER required for core factory. Callers (rigor_judge) must skip tiny clear
happy-path; this module also soft-refuses when context marks tiny_clear.

JEV — optional prompt template (doc/comment only; no concrete model slug)::

    # System: You are an optional Emperor Time judgment aide. Reply JSON only:
    # {"decision":"<short>","rationale":"<short>"}. Do not invent gates.
    # User: {prompt}
    # Context: {context_json}

Thin twins: scripts/judgment.sh / scripts/judgment.ps1
CLI: emperor judgment [--prompt TEXT] [--use-case CASE] [--as-json]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Mapping, Sequence

_LIB = Path(__file__).resolve().parent
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

import config as et_config  # noqa: E402

PROVIDERS = ("off", "openrouter", "openai_compat")
DEFAULT_USE_FOR = (
    "effort_class_dispute",
    "ship_no_ship",
    "critique_conflict",
)
OPENROUTER_DEFAULT_BASE = "https://openrouter.ai/api/v1"
ENV_KEY = "EMPEROR_JUDGMENT_API_KEY"
ENV_BASE = "EMPEROR_JUDGMENT_BASE_URL"

# JEV prompt template — comment/doc only; never bind a concrete model slug.
_PROMPT_TEMPLATE_DOC = (
    'System: You are an optional Emperor Time judgment aide. Reply JSON only: '
    '{"decision":"<short>","rationale":"<short>"}. Do not invent gates.\n'
    "User: {prompt}\n"
    "Context: {context_json}"
)


def judgment_config(root: Path | None = None) -> dict[str, Any]:
    """Return normalized judgment block from merged config."""
    cfg = et_config.load_config(root)
    block = cfg.get("judgment") or {}
    if not isinstance(block, dict):
        return {
            "provider": "off",
            "model": None,
            "timeout_s": 8,
            "use_for": list(DEFAULT_USE_FOR),
        }
    return {
        "provider": str(block.get("provider", "off")).lower().strip() or "off",
        "model": block.get("model"),
        "timeout_s": block.get("timeout_s", 8),
        "use_for": list(block.get("use_for") or list(DEFAULT_USE_FOR)),
    }


def _as_float_timeout(raw: Any, default: float = 8.0) -> float:
    try:
        t = float(raw)
    except (TypeError, ValueError):
        return default
    if t <= 0:
        return 0.001  # near-immediate soft timeout
    return t


def _soft_none(_reason: str = "") -> None:
    """Always soft — never raise for adapter refusal."""
    return None


def _parse_decision_payload(text: str) -> dict[str, str] | None:
    text = (text or "").strip()
    if not text:
        return None
    # Tolerate markdown fences / leading chatter.
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            chunk = part.strip()
            if chunk.startswith("json"):
                chunk = chunk[4:].strip()
            if chunk.startswith("{"):
                text = chunk
                break
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        text = text[start : end + 1]
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    decision = data.get("decision")
    rationale = data.get("rationale")
    if decision is None:
        return None
    return {
        "decision": str(decision).strip(),
        "rationale": "" if rationale is None else str(rationale).strip(),
    }


def _chat_completions(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    context: Mapping[str, Any],
    timeout_s: float,
) -> dict[str, str] | None:
    url = base_url.rstrip("/") + "/chat/completions"
    # Build messages from JEV template (no model slug in template).
    ctx_json = json.dumps(
        {k: v for k, v in dict(context).items() if not str(k).startswith("_")},
        ensure_ascii=False,
        default=str,
    )
    user_content = _PROMPT_TEMPLATE_DOC.format(
        prompt=prompt, context_json=ctx_json
    )
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Optional Emperor Time judgment aide. "
                    'Reply JSON only: {"decision":"...","rationale":"..."}.'
                ),
            },
            {"role": "user", "content": user_content},
        ],
        "temperature": 0,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except Exception:
        # timeout, HTTPError, URLError, OSError — all soft None
        return _soft_none("transport")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return _soft_none("bad-json")
    choices = payload.get("choices") if isinstance(payload, dict) else None
    if not isinstance(choices, list) or not choices:
        return _soft_none("no-choices")
    msg = choices[0].get("message") if isinstance(choices[0], dict) else None
    content = ""
    if isinstance(msg, dict):
        content = str(msg.get("content") or "")
    return _parse_decision_payload(content)


def judge(
    prompt: str,
    context: Mapping[str, Any] | None = None,
    *,
    root: Path | None = None,
) -> dict[str, str] | None:
    """Optional judgment. Returns {decision, rationale} or None (soft refuse).

    Never raises for missing provider/key/timeout. Never required for core
    factory — even if context.request_required is set, still returns None
    when the adapter cannot produce a decision (refuse-soft).
    """
    ctx: dict[str, Any] = dict(context or {})
    # Happy-path / tiny clear — never call provider.
    if ctx.get("tiny_clear") or ctx.get("happy_path") or ctx.get("skip_judgment"):
        return _soft_none("tiny-clear")
    # Explicit require cannot harden the adapter.
    _ = bool(ctx.get("require") or ctx.get("request_required"))

    # Test-only stubs (fixtures) — no network.
    stub = ctx.get("_stub")
    if stub == "ok":
        return {
            "decision": str(ctx.get("_stub_decision") or "advisory"),
            "rationale": str(ctx.get("_stub_rationale") or "fixture stub"),
        }
    if stub in ("timeout", "refuse", "error", "none"):
        return _soft_none(str(stub))

    jcfg = judgment_config(root)
    provider = str(jcfg.get("provider") or "off").lower().strip()
    if provider in ("", "off", "false", "no", "none", "0"):
        return _soft_none("provider-off")
    if provider not in ("openrouter", "openai_compat"):
        return _soft_none("unknown-provider")

    use_for = [str(x) for x in (jcfg.get("use_for") or list(DEFAULT_USE_FOR))]
    use_case = str(ctx.get("use_case") or ctx.get("for") or "").strip()
    if use_case and use_case not in use_for:
        return _soft_none("use-case-not-enabled")
    # Default use_case when omitted: effort_class_dispute (rigor_judge hook).
    if not use_case:
        use_case = "effort_class_dispute"
        if use_case not in use_for:
            return _soft_none("use-case-not-enabled")

    api_key = (os.environ.get(ENV_KEY) or "").strip()
    if not api_key:
        return _soft_none("no-key")

    model = jcfg.get("model")
    if model is None or str(model).strip() in ("", "null", "None"):
        # JEV: no concrete model slug shipped — refuse soft until operator sets one.
        return _soft_none("no-model")
    model_s = str(model).strip()

    timeout_s = _as_float_timeout(jcfg.get("timeout_s", 8))

    if provider == "openrouter":
        base = (os.environ.get(ENV_BASE) or "").strip() or OPENROUTER_DEFAULT_BASE
    else:
        base = (os.environ.get(ENV_BASE) or "").strip()
        if not base:
            return _soft_none("no-base-url")

    return _chat_completions(
        base_url=base,
        api_key=api_key,
        model=model_s,
        prompt=prompt or "",
        context=ctx,
        timeout_s=timeout_s,
    )


def format_card() -> str:
    return (
        "JUDGMENT checklist=yes\n"
        "JUDGMENT provider=optional\n"
        "JUDGMENT iron=NEVER_REQUIRED_FOR_CORE_FACTORY\n"
        "STEP 1 id=off name=provider off / no key / no model → None "
        "et=existing gates decide\n"
        "STEP 2 id=use name=use_for allowlist "
        "et=effort_class_dispute|ship_no_ship|critique_conflict\n"
        "STEP 3 id=tiny name=Never call on tiny happy-path "
        "et=rigor_judge skips clear tiny; context.tiny_clear soft-refuses\n"
        "STEP 4 id=timeout name=Timeout / transport → None "
        "et=soft refuse; no HARD fail\n"
        "\n"
        "MUST: Soft None when unavailable; keep iron gates deciding.\n"
        "MUST-NOT: invent model slug; require for core factory; call on tiny clear.\n"
        "HONESTY: JEV prompt template is doc/comment only — no concrete model slug.\n"
        f"ENV: {ENV_KEY} + {ENV_BASE} (openai_compat/openrouter)\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="emperor-judgment",
        description="Optional judgment adapter stub (soft None when off/unavailable)",
    )
    p.add_argument("--root", default=None, help="Project root")
    p.add_argument("--prompt", default=None, help="Judgment prompt")
    p.add_argument(
        "--use-case",
        default=None,
        help="effort_class_dispute|ship_no_ship|critique_conflict",
    )
    p.add_argument(
        "--tiny-clear",
        action="store_true",
        help="Mark tiny happy-path (must soft-refuse)",
    )
    p.add_argument(
        "--require",
        action="store_true",
        help="Attempt require (still soft-refuses when unavailable)",
    )
    p.add_argument("--as-json", action="store_true", help="Print JSON (null if None)")
    p.add_argument(
        "--show-config",
        action="store_true",
        help="Print normalized judgment config and exit",
    )
    p.add_argument(
        "positional_prompt",
        nargs="?",
        default=None,
        help="Prompt text (positional)",
    )
    args = p.parse_args(list(argv) if argv is not None else None)

    root = Path(args.root).resolve() if args.root else None

    if args.show_config:
        sys.stdout.write(json.dumps(judgment_config(root), indent=2) + "\n")
        return 0

    prompt = args.prompt or args.positional_prompt or ""
    if not prompt and not args.tiny_clear and args.prompt is None and args.positional_prompt is None:
        if sys.stdin.isatty():
            sys.stdout.write(format_card())
            return 0
        prompt = sys.stdin.read()

    ctx: dict[str, Any] = {}
    if args.use_case:
        ctx["use_case"] = args.use_case
    if args.tiny_clear:
        ctx["tiny_clear"] = True
    if args.require:
        ctx["require"] = True

    result = judge(prompt, ctx, root=root)
    if args.as_json:
        sys.stdout.write(json.dumps(result, indent=2) + "\n")
    else:
        if result is None:
            print("judgment: None")
            print("soft: yes")
            print("note: existing gates decide")
        else:
            print(f"decision: {result.get('decision', '')}")
            print(f"rationale: {result.get('rationale', '')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
