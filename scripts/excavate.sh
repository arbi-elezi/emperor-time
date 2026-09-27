#!/usr/bin/env bash
# Thin alias: same survey as identify via Python core. First-class excavate tool name.
# Calls identify.py directly (no twin hop) so bash↔ps1 cannot drift.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/identify.py" "$@"
