#!/usr/bin/env bash
# Thin twin: testing-skills HARD-GATE card via Python core.
# Prints SKILLTEST / PRIN / GATE / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/skill_test.py" "$@"
