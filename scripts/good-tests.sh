#!/usr/bin/env bash
# Thin twin: writing-good-tests HARD-GATE card via Python core.
# Prints GOOD / PRIN / GATE / MUST lines. Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/good_tests.py" "$@"
