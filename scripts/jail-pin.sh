#!/usr/bin/env bash
# Alias twin: jail-pin → pin-and-consent Python core.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec bash "$ROOT/scripts/pin-and-consent.sh" "$@"
