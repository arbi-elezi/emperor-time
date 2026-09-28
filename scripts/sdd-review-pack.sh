#!/usr/bin/env bash
# Thin twin: sdd-review-pack via Python core.
# Usage: sdd-review-pack.sh [args...]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/sdd_review_pack.py" "$@"
