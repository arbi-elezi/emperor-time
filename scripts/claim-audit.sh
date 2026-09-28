#!/usr/bin/env bash
# Thin twin: Judgment claim-audit HARD-GATE via Python core.
# Prints CLAIM-AUDIT card or validates a task dir / claims file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/claim_audit.py" "$@"
