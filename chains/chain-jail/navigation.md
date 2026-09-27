# Navigation — what to steal, where to look

**Contract:** given a proven absence (capability sentence from `absence-check.md`)
and the current G1, pick *which catalogs to search* and *which skill names to
ask for*. Output: a NEED card + a 1–3 catalog shortlist. Then `hunt.md` runs
the queries. Do not search the whole internet first.

This is how Emperor Time stays small. The core holds vows, gates, and chains.
Abilities are bound on demand from public skills — Superpowers included — then
adapted, pinned, consented, and trialed. Assimilation is not copy-paste of a
foreign body into the always-on prompt.

## NEED card (write this first)

```
NEED: <verb-first capability sentence>
G1 it serves: <acceptance line>
Language / stack: <or any>
Harness that must run it: this | enlisted <agent>
Must-not: override vows; skip gates; touch credentials; phone home
Already local: <absence-check hits or none>
```

If the NEED is something a chain already does (scope, critique, heal, dispatch,
claim audit), **stop**. That is not missing. Jail disengages.

## Scope → first places to look

Re-verify URLs and tree paths this session (`--help`, raw GitHub, or clone).
This table is a map, not memory.

| If the gap is… | Ask catalogs for… | First repos / trees (2026 public) |
|---|---|---|
| Socratic design / visual mock before code | `brainstorming`, `grill`, `discuss` | `obra/superpowers` `skills/brainstorming`; Pocock grill skills |
| Fat executable plan | `writing-plans`, `executing-plans`, `subagent-driven-development` | Local first: `scripts/lib/work_order.py` + `executing-plans-checklist.md` + `emperor execute` (inline) or `subagent-driven-checklist.md` + `emperor subagent` (independent tasks + subagent tool). Superpowers those folders only if still insufficient |
| Parallel independent domains / concurrent agents | `dispatching-parallel-agents`, parallel dispatch | Local first: `parallel-dispatch-checklist.md` + `emperor parallel` (disjoint writable scopes). Sequential plan tasks stay `emperor subagent`. Steal Chain consent for external CLIs. Superpowers that folder only if still insufficient |
| TDD / failing-probe / RGR order | `tdd`, `red-green`, `failing probe` | Local first: `skills/emperor-tdd/red-green-refactor.md` + `emperor tdd`. Superpowers TDD only if runner-specific aspect still missing |
| Systematic debug for a stack | `systematic-debugging`, framework debug | Local first: `debug-four-phases.md` + `emperor heal`, `root-cause-tracing.md` + `emperor trace`. Superpowers that folder only if still insufficient |
| Isolated reviewer / request-review before merge | `requesting-code-review`, review personas | Local first: `skills/emperor-verify/request-review-checklist.md` + `emperor review`. Osmani personas / Superpowers only if still insufficient |
| Git worktree / finish-branch polish | `using-git-worktrees`, `finishing-a-development-branch` | Local first: `skills/emperor-forge/finish-menu.md` + `emperor finish`. Superpowers those folders only if still insufficient |
| Current library API (not training data) | `doc-lookup`, Context7-style | Superpowers doc-lookup; vendor docs skills |
| PDF/docx/xlsx/pptx | document skills | `anthropics/skills` |
| UI that does not look generic | `frontend-design` | official plugin marketplace / Anthropic frontend-design |
| Domain X (k8s, SQL, SEO…) | `<domain> SKILL.md` | vendor orgs, `awesome-agent-skills`, GitHub topic `agent-skills` |
| Skill-authoring craft | `writing-skills` | Local first: `authoring-checklist.md` + `emperor author` (Iron Law). Superpowers writing-skills only if still insufficient |
| Completion / pass / fixed claims without fresh proof | `verification-before-completion` | Local first: `skills/emperor-verify/verification-checklist.md` + `emperor evidence`. Superpowers that skill only if still insufficient |

Emperor Time already *is* the orchestrator. Do not steal `using-superpowers`
or another master router to replace `SKILL.md`. Steal **leaf** skills.

## Search order (narrow → wide)

1. Named tree above, exact path `skills/<name>/SKILL.md` or `SKILL.md`.
2. Same repo siblings (one listing, then stop).
3. GitHub code search: `"<capability>" filename:SKILL.md`.
4. Topics: `topic:agent-skills`, awesome lists found *this session*.
5. Adjacent formats (opencode, Cursor rules, gist). Format conversion is
   `adaptation.md`. Rejection for wrong format is sloppy hunting.

If step 1 yields a full-fit MIT/Apache skill, do not perform steps 3–5.
Worthy Spend: extra catalogs after a good hit are vanity.

## Assimilation stance (hand to hunt + adapt)

- Fetch bytes. Hash them. License gate lives in `hunt.md`.
- Adapt into `.emperor/captured-skills/<name>/` so it fires **inside** a phase.
- Strip anything that would skip G0–G5, enlist without consent, or write
  Co-Authored-By.
- Bind only after `pin-and-consent.md` + `trial-and-register.md`.
- The stolen skill remains foreign Nen: its advice is CONJECTURE until a probe
  you ran this session says otherwise.

## Superpowers as prey, not as master

When the client names Superpowers, navigate their *skill list* (re-read the
repo tree; do not recite from memory). Steal the one leaf that fills the NEED.
Do not vendor the whole Superpowers plugin into Emperor Time. Two orchestrators
in one session is a vow-of-phases collision.
