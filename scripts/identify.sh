#!/usr/bin/env bash
# Language-agnostic artifact survey. No preferred stack. Always exits 0.
set -uo pipefail
ROOT="${1:-.}"
echo "== identify $ROOT =="
if command -v find >/dev/null 2>&1; then
  echo "-- extensions --"
  find "$ROOT" -type f ! -path '*/.git/*' ! -path '*/.emperor/*' ! -path '*/node_modules/*' \
    | sed 's/.*\.//' | grep -E '^[A-Za-z0-9]+$' | tr '[:upper:]' '[:lower:]' \
    | sort | uniq -c | sort -nr | head -n 40 || true
fi
echo "-- named fossils --"
for pat in '*.pas' '*.pp' '*.dpr' '*.lpr' '*.asm' '*.s' '*.inc' '*.cbl' '*.cob' '*.for' '*.f' '*.f90' '*.vhd' '*.vhdl' '*.rel' '*.hex' '*.bin' '*.rom' 'Makefile' 'makefile' '*.mak'; do
  n=$(find "$ROOT" -type f \( -iname "$pat" -o -name "$pat" \) ! -path '*/.git/*' 2>/dev/null | wc -l | tr -d ' ')
  if [[ "${n:-0}" != 0 ]]; then
    echo "$n $pat"
  fi
done
echo "-- shebangs --"
find "$ROOT" -type f ! -path '*/.git/*' -size -200k 2>/dev/null | head -n 200 | while IFS= read -r f; do
  line=$(head -n1 "$f" 2>/dev/null || true)
  case "$line" in
    '#!'*) echo "$f: $line" ;;
  esac
done | head -n 30 || true
echo "identify: done (read-only)"
exit 0
