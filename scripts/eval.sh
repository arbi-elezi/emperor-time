#!/usr/bin/env bash
# Thin twin: structural evals via Python core.
# Does not spawn a model. Exit 0 = EVALS PASSED, 1 = EVALS FAILED.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/eval.py" "$@"
