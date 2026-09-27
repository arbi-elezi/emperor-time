#!/usr/bin/env bash
# Thin twin: trigger→skill router MVP via Python core (no embeddings).
# Usage: route.sh "utterance"   OR   echo utterance | route.sh
# Prints: <target> — <reason>   exit 0 on match, 1 on no match, 2 on usage/error.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/route.py" "$@"
