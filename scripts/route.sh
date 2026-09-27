#!/usr/bin/env bash
# Trigger→skill router MVP (no embeddings). Peer of route.ps1.
# Thin twin: delegates to scripts/lib/route.py.
# Usage: route.sh "utterance"   OR   echo utterance | route.sh
# Prints: <target> — <reason>   exit 0 on match, 1 on no match, 2 on usage/error.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TRIGGERS="${EMPEROR_TRIGGERS:-$ROOT/evals/triggers.json}"
PY="$ROOT/scripts/lib/route.py"

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
[[ -f "$PY" ]] || { echo "route: missing $PY" >&2; exit 2; }

export EMPEROR_ROUTE_UTTERANCE="$UTTERANCE"
export EMPEROR_ROUTE_TRIGGERS="$TRIGGERS"
exec python3 "$PY"
