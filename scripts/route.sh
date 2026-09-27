#!/usr/bin/env bash
# Trigger→skill router MVP (no embeddings). Reads evals/triggers.json routes.
# Usage: route.sh "utterance"   OR   echo utterance | route.sh
# Prints: <target> — <reason>   exit 0 on match, 1 on no match, 2 on usage/error.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TRIGGERS="${EMPEROR_TRIGGERS:-$ROOT/evals/triggers.json}"

if [[ $# -gt 0 ]]; then
  UTTERANCE="$*"
else
  if [[ -t 0 ]]; then
    echo "usage: $0 <utterance>   or pipe stdin" >&2
    exit 2
  fi
  UTTERANCE=$(cat)
fi
UTTERANCE=$(printf '%s' "$UTTERANCE" | tr -s '[:space:]' ' ' | sed 's/^ //;s/ $//')
[[ -n "$UTTERANCE" ]] || { echo "usage: $0 <utterance>" >&2; exit 2; }
[[ -f "$TRIGGERS" ]] || { echo "route: missing $TRIGGERS" >&2; exit 2; }

export EMPEROR_ROUTE_UTTERANCE="$UTTERANCE"
export EMPEROR_ROUTE_TRIGGERS="$TRIGGERS"
python3 - <<'PY'
import json, os, re, sys

utterance = os.environ["EMPEROR_ROUTE_UTTERANCE"]
path = os.environ["EMPEROR_ROUTE_TRIGGERS"]
text = utterance.casefold()

with open(path, encoding="utf-8") as f:
    data = json.load(f)

routes = data.get("routes") or []

def matches(pattern: str) -> bool:
    p = pattern.casefold().strip()
    if not p:
        return False
    # Short tokens / tags: word-boundary to avoid "rom" in "from"
    compact = re.sub(r"[^a-z0-9]+", "", p)
    if len(compact) <= 3 or p.startswith("."):
        # escape and allow flexible non-alnum edges for extensions
        if p.startswith("."):
            return p in text
        return re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", text) is not None
    return p in text

for route in routes:
    pats = list(route.get("patterns") or [])
    tags = list(route.get("tags") or [])
    hit = None
    for p in pats:
        if matches(p):
            hit = p
            break
    if hit is None:
        for t in tags:
            if matches(t):
                hit = t
                break
    if hit is None:
        continue
    target = route.get("target") or ""
    reason = route.get("reason") or route.get("id") or "match"
    if not target:
        continue
    print(f"{target} — {reason}")
    sys.exit(0)

print("route: no match", file=sys.stderr)
sys.exit(1)
PY
