#!/usr/bin/env bash
# Alias twin: steal-consent → consent Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/consent.sh" "$@"
