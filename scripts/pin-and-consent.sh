#!/usr/bin/env bash
# Thin twin: Jail pin-and-consent HARD-GATE via Python core.
# Prints PIN-CONSENT card or validates a task dir / pin / captured-skill.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/pin_consent.py" "$@"
