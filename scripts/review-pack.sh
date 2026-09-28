#!/usr/bin/env bash
# Thin twin: isolated review pack + hetero-critique isolation HARD-GATE.
# Usage:
#   review-pack.sh <task-dir> [base] [head]          # emit pack
#   review-pack.sh --check-isolation <task-dir>      # isolation check
#   review-pack.sh --reject-unisolated               # always fail
#   review-pack.sh --reject-author-diary             # always fail
#   review-pack.sh                                   # ISOLATION card
# Emits meta + acceptance criteria + diff. No author CoT.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/review_pack.py" "$@"
