#!/usr/bin/env bash
# Thin twin: verification-before-completion / evidence checklist via Python core.
# Prints EVIDENCE / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/evidence.py" "$@"
