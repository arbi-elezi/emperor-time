#!/usr/bin/env bash
# Thin twin: thoughttrail + super-context via Python core.
# Prints CONTEXT card or runs build|query|path|explain|trail|HARD-GATE checks.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/context.py" "$@"
