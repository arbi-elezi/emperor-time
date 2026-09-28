#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
if [[ $# -eq 0 ]]; then exec bash "$HERE/context.sh" trail list; fi
if [[ "${1:-}" =~ ^(append|list|link)$ ]]; then exec bash "$HERE/context.sh" trail "$@"; fi
exec bash "$HERE/context.sh" "$@"
