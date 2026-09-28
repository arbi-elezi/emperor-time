#!/usr/bin/env bash
# Thin twin: Steal consent-protocol HARD-GATE via Python core.
# Prints CONSENT card or validates a task dir / consent file.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/consent.py" "$@"
