# Graph / mid-flash doctrine

Why this page exists: strangers keep hearing “graph” and “multi-agent” and
reaching for a new runtime. Under **mid-flash** (mediocre local/API models on
the ORI stranger path), completion comes from orchestrator + verify + quarantine —
not debate theater. Emperor Time already owns the high-ROI graph pieces. Iron
gates stay hard.

## Graph → ET map

Fold of existing tip paths. Point; do not reimplement.

| Flavor people mean | ET already has | Tip path |
|---|---|---|
| Phased plan with gates (micro-waterfall / G0–G5) | One task = one waterfall = one ledger; gates open on evidence | `references/micro-waterfall.md` |
| Consent → quarantine → dispatch (Steal) | Steal chain: consent, sign-in handoff, dispatch, quarantine, routing | `chains/steal-chain/` |
| Claim audit / Judgment | Judgment chain: gatekeeping, claim-audit, critique, verdicts | `chains/judgment-chain/` + mechanical gates |
| Repo-as-graph / link extract | Structural Markdown → SQLite graph; **no embeddings** | `scripts/lib/md_graph.py` (+ `references/super-context.md`) |

Super-context is graph-over-grep and thoughttrail — not a retrieval product and
not GraphRAG. See `references/super-context.md`.

## Mid-model config defaults

Standing defaults in `scripts/lib/config.py` (schema v1). Document; do not invent knobs.

| Knob | Default | Mid-flash rule |
|---|---|---|
| `gates.always_hard` | `forge-pr-consent`, `pin-and-consent`, `quarantine`, `steal-consent`, `secrets-no-leak` | **Never soft** — `scale_with_effort` may soften *other* gates only |
| `judgment.provider` | `off` | Optional; stay off until a dispute needs it. Never required on tiny happy-path |
| `rigor.default_effort_class` | `tiny` | Escalate when the ask earns it; do not unlock large via soft docs |

`judgment.provider` may be `off` \| `openrouter` \| `openai_compat`. Soft refuse
returns `None`; existing gates decide. No tiny happy-path requires a judgment adapter.

## Dual-track footnote

| Track | Stance |
|---|---|
| Frontier “free the model” (Replit Free-the-models, 2026-09-29) | **Watch** — capable models may want less harness theater |
| ET iron for mediocre / mid-flash (ORI stranger path) | **Keep** — orchestrator-owned plan + mandatory verify + quarantine |

Do not copy frontier free-the-model into the ORI stranger path. Dual-track is a
footnote, not a roadmap reorder.

## Citations (accessed labels; no invented metrics)

| Source | Role here |
|---|---|
| [Growing Harness](https://arxiv.org/abs/2609.26760) | Held-out gate + rollback; mid/small models benefit disproportionately |
| [Empirical harness design](https://arxiv.org/abs/2609.20804) | Planning / tools / context conditional on model strength |
| Replit Free-the-models (2026-09-29) | Dual-track footnote only — frontier frees the model; not the ORI default |

Provenance fold (workspace memos; tip page stands alone): graph/local16b 2026-09-30, landscape 48h 2026-10-01, backlog shapes S2 2026-10-01.

## MoA-lite = CONJECTURE

Propose→aggregate as a *pattern* may inform Steal routing (orchestrator +
specialists, restricted cross-talk). Headline MoA bench numbers are theater —
not a ship claim. Label stays **CONJECTURE** until ET has its own verified
experiment.

## Kill list

Do not ship or chase as ET product / runtime:

| Kill | Why |
|---|---|
| LangGraph / AutoGen / Temporal as ET runtime | External runtimes; ET already maps the high-ROI graph |
| GraphRAG / embedding graph dependency | Tip `md_graph` is structure-only; no embeddings |
| Unguided homogeneous multi-~16B debate | Unrestricted debate often hurts; orchestrator + verify wins |
| Colibrì-as-harness | Colibrì = OpenAI-compat **inference** only (see `adapters/colibri/`); not a harness to own |
| Growing-Harness-optimizer | Cite the paper; do not build the optimizer product |
| OpenAPPA / LLM babysitter product | Oversight is process (kill/hold), not a platform; see `kill-hold.md` |
| Native equal-UX chase | Adapter HOLD until foreign green receipt + explicit claim ACCEPT |

## Headline for strangers

Completion under mid-flash comes from orchestrator + verify + quarantine — not
debate theater or a new graph runtime. ET already owns the high-ROI graph.
Frontier “free the model” is a dual-track footnote, not the stranger ORI path.
