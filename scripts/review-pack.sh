#!/usr/bin/env bash
# Thin twin: isolated review pack via Python core.
# Usage: review-pack.sh <task-dir> [base] [head]
# Emits meta + acceptance criteria + diff. No author CoT.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/review_pack.py" "$@"
