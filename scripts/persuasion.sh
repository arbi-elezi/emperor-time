#!/usr/bin/env bash
# Thin twin: persuasion-principles HARD-GATE card via Python core.
# Prints PERSUADE / PRIN / GATE / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/persuasion.py" "$@"
