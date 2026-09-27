#!/usr/bin/env bash
# Thin twin: git finish environment + integration menu via Python core.
# Does not merge, push, or delete. Agent + client choose; forge still needs consent.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/finish.py" "$@"
