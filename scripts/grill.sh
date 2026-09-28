#!/usr/bin/env bash
# Thin twin: grill/brainstorm checklist + path-taxonomy HARD-GATE via Python core.
# Prints GRILL / STEP / MUST lines. --reject-no-path / --reject-stage-skip /
# --reject-impl-before-approval / --check-path refuse missing path, skipped
# stage, or impl before stage approval. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/grill.py" "$@"
