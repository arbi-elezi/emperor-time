#!/usr/bin/env bash
# Thin twin: diagnosing HARD-GATE card + cite-or-fail report skeleton via Python core.
# Prints DIAGNOSE / INTAKE / CITE / REPORT / MUST lines.
# --reject-uncited / --reject-skip-intake / --reject-no-report always fail;
# --check-citation / --check-report enforce path:line + report skeleton.
# Does not mutate.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/diagnose.py" "$@"
