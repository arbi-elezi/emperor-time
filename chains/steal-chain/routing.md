# Routing — which agent for which work

**Contract:** given a task shape and the current roster, produce a
recommendation (agent + one-line reason) for the consent ask. Routing
recommends; the client decides; consent records. Defaults here yield to both.

## The routing table

| Work shape | Prefer | Reasoning | Fallback ladder |
|---|---|---|---|
| Bulk mechanical edits (renames, boilerplate, format migrations) | Local model (Ollama) or cheapest CLI | low judgment per edit; failure is cheap and obvious in quarantine; volume pricing matters | any available worker → solo |
| Test authoring | A capable agent that is **not the code's author** | author-blindness: whoever wrote the code tests what they believed, not what it does | different-family agent → same-family fresh session → solo with explicit blindness note in critique |
| Design review / architecture / hairy debugging | Strongest available model | judgment-dense; a weak reviewer rubber-stamps | strongest → solo (never a small local model as sole reviewer of hard problems) |
| Hetero-critique | **Different vendor/family than the author** | decorrelated failure modes are the product; same-family critique breaks only some correlation | different family → same family (marked partial) → self-critique only (recorded) |
| Web research | A harness with live web access | capability fit; stale knowledge is the risk being bought out | web-capable agent → client fetches → labeled UNVERIFIABLE |
| Privacy-sensitive content (client data, unreleased code, credentials-adjacent) | **Local only** (Ollama / local-backed opencode) — or solo | consent to an agent is consent to its data path; cloud vendors are a data path | local → solo. Cloud is not a fallback here — it's a new consent question |
| Long mechanical sequences with checkpoints (migrations, codemods) | CI-friendly exec-mode agent (e.g. codex exec) | headless single-session-to-completion fits scripted supervision | any headless agent → chunked solo |
| GitHub-context work (PRs, issues, Actions) | Copilot CLI / gh-adjacent tooling | native context access | any agent + gh CLI → solo + gh |
| Orchestration, admission, verdicts | **You. Always.** | delegating judgment re-imports every failure mode this system quarantines | none — this row has no fallback |

## Cross-cutting modifiers (adjust the table's answer)

- **Blast radius up → capability up.** A mechanical edit *inside auth code*
  routes like design work, not like boilerplate.
- **Context window**: local models get scoped fragments (one file, one
  function); a task that can't be scoped down isn't local-model work
  (dispatch's "minimum context" rule is load-bearing here).
- **Roster reality beats theory**: the observed notes column (past misses,
  timeouts, garbage rate per agent) outranks this table's priors. An agent
  that failed this task-shape twice is off that shape's ladder for the
  project (note says so; client can override).
- **Cost asymmetry**: verification cost is part of routing — an agent whose
  output is cheap to produce but expensive to quarantine (sprawling diffs,
  chatty reports) is expensive, whatever its pricing.

## Worked examples

- *"Rename `getUser` → `fetchUser` across 40 files"* → Ollama/qwen3, scoped
  to the file list, verify by grep + build. Cloud capability is wasted here.
- *"Why does the login flow deadlock under load?"* → strongest model
  available; if that's the orchestrator itself, solo with hetero-critique of
  the *conclusion* by a different family.
- *"Write tests for the module I just wrote"* → codex or opencode (not the
  author); prompt includes the spec, **not** the implementation rationale
  (blindness preserved on purpose).
- *"Summarize this client contract"* → local only or solo, regardless of what
  stronger cloud models would do better — the modifier row wins over quality
  preference, and the consent ask says why.

## Recommendation format (what consent-protocol.md consumes)

```
RECOMMEND: codex → test authoring ("not the author; exec mode fits")
ALT: opencode (same reasoning, different family)  |  SOLO viable: yes
DATA PATH: diff of src/parser only → OpenAI     COST NOTE: ~small
```

One recommendation, one alternative, the solo option's viability, and the
data path. The client decides in one glance.
