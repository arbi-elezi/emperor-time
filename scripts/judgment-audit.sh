#!/usr/bin/env bash
# Alias twin: judgment-audit → claim-audit Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/claim-audit.sh" "$@"
