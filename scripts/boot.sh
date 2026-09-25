#!/usr/bin/env bash
# Silent session defaults. User never types this.
# Writes .emperor/host.env and .emperor/survey.md. Optionally .emperor/eval.log.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
# shellcheck disable=SC1091
. "$HERE/lib/host.sh"
mkdir -p .emperor
emperor_host_report > .emperor/host.env
bash "$HERE/identify.sh" . > .emperor/survey.md 2>/dev/null || true
if [[ -f "$HERE/eval.sh" && -f SKILL.md ]]; then
  bash "$HERE/eval.sh" > .emperor/eval.log 2>&1 || true
fi
if [[ "${EMPEROR_BOOT_VERBOSE:-0}" == 1 ]]; then
  cat .emperor/host.env
fi
exit 0
