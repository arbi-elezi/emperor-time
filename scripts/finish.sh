#!/usr/bin/env bash
# Thin twin: git finish ENV/MENU + suite-green HARD-GATE via Python core.
# Does not merge, push, or delete. Agent + client choose; forge still needs consent.
# --reject-red-suite / --require-green <task-dir> refuse menu without green suite.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/finish.py" "$@"
