#!/usr/bin/env bash
# Thin twin: request-review checklist via Python core (emperor-verify path).
# Prints REVIEW / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/review_req.py" "$@"
