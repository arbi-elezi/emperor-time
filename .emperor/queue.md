# Emperor queue
# WIP=1 — one [~] active at a time.
# Statuses: [ ] ready · [~] active · [x] done · [!] blocked
# queue next: returns existing [~], else promotes first ready [ ] → [~].
#
# Empty state: no checkbox lines below. Add real work as:
#   - [ ] ship the widget
# Or connect gh / Linear. Lines matching (empty …) / parentheses-only
# titles are ignored by queue next and never promoted.

Local backlog when GitHub issues / Linear are not connected.
