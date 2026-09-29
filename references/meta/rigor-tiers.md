# Rigor tiers (effort_class ladder)

Thin extension of `effort_class` — **no parallel ladder**. Aliases: `standard→small`, `full→large`.

| Class | When | Caps posture |
|---|---|---|
| **tiny** | typo / one-line / wording / changelog-only | few tools; heavy paths forbidden; critique museum SKIP |
| **small** | flag / wire / thin twin / patch / fixture | light verify; optional critique |
| **medium** | feature / gate / schema / harness leaf | eight-count critique floor (config); worktree OK |
| **large** | refactor / migrate / excavate deep / full rigor | full FORCE_TABLE; iron gates unchanged |

Iron `always_hard` **never** softens with class: forge-pr-consent, pin-and-consent, quarantine, steal-consent, secrets-no-leak.

Judge: `scripts/lib/rigor_judge.py` (deterministic; no LLM on tiny).
Config: `emperor config get rigor.default_effort_class`.
