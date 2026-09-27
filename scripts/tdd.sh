#!/usr/bin/env bash
# Thin twin: TDD iron-law / RGR checklist via Python core (emperor-tdd path).
# Prints TDD / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/tdd.py" "$@"
