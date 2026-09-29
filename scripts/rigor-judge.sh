#!/usr/bin/env bash
# Thin twin: rigor-judge via Python core (cheap effort_class recommendation).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/rigor_judge.py" "$@"
