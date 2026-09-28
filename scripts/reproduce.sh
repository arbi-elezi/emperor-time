#!/usr/bin/env bash
# Thin twin: reproduce-and-bisect fingerprint + combat ledger HARD-GATE via Python core.
# Prints REPRODUCE card or validates a task dir / reproduce file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/reproduce.py" "$@"
