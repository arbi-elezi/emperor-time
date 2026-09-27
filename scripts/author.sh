#!/usr/bin/env bash
# Thin twin: authoring iron-law / skill RGR checklist via Python core.
# Prints AUTHOR / STEP / MUST lines. Does not mutate the tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/lib/author.py" "$@"
