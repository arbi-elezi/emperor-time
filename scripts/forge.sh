#!/usr/bin/env bash
# Thin twin: consent-gated PR forge via Python core.
# Usage: forge.sh <task-dir>
# Refuses without EMPEROR_CONSENT_PR=1 or ledger PR consent; runs DONE probes.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/forge.py" "$@"
