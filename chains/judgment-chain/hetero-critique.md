# Hetero-Critique — borrowed prosecutors

**Contract:** package the work for an independent agent, instruct it to
refute, verify its findings before acting on any. Output: the critic's
verified findings merged into the critique record, with the critic's identity
in provenance. Runs after self-critique, never instead of it.

Why a second prosecutor: your failure modes correlate with themselves. The
author's blind spot survives the author's critique precisely because it is a
blind spot. A different model family fails differently — that decorrelation,
not extra volume, is what you're buying.

## Step 1 — Pick the critic

- **Different vendor/family than the author** of the work, whenever the
  roster allows (the routing rationale lives in `chains/steal-chain/routing.md`).
- Consent rules apply — an unenlisted agent can't be a critic; if none is
  enlisted and available, record `hetero-critique: unavailable this task` in
  the critique and proceed. The record is mandatory; the critique isn't
  silently skipped.
- A *human* reviewer offered by the client counts as the strongest available
  critic; package the same brief.

## Step 2 — Package the brief

Write to `.emperor/runs/<task-id>/<critic>/prompt.md`:

```markdown
ROLE: adversarial reviewer. Your job is to REFUTE this work — find reasons it
is wrong, incomplete, unproven, or unsafe. Default to skepticism; a clean pass
must name what you checked and found solid.

REQUIREMENTS (verbatim): <G1 criteria + out-of-scope>
THE CHANGE: <diff or artifact>
AUTHOR'S CLAIMS: <claim-ledger rows relevant to the change, statuses included>
CONSTRAINTS: report findings as a list; for each: what's wrong, where
(file:line), how you know (what you ran/read), severity (blocker /
should-fix / note). Separate VERIFIED-by-you findings from suspicions —
suspicions are welcome but must be marked. Do not fix anything; only report.
```

What goes in: requirements, the change, the claims. What stays out: your
self-critique findings (anchoring — the second prosecutor's value is
independent eyes; giving it your findings converts it into a reviewer of your
review), secrets (never), and flattery-bait framing ("I think this is solid,
but check it") that primes agreement.

## Step 3 — Dispatch and collect

Mechanics per `chains/steal-chain/dispatch.md` (headless form from the
registry, output to `.emperor/runs/<task-id>/<critic>/out.txt`, timeout set).
The critique brief is read-only work — grant the critic no write access to
the task's files.

## Step 4 — Verify before acting (critics hallucinate too)

Each critic finding is a **claim in CONJECTURE**:

1. Reproduce it: does the defect exist at the cited location, the way it says?
2. Verified → merge into the critique with disposition (fix / condition /
   pooled), credited: `[critic: opencode/qwen3]`.
3. Refuted → record *that* with your evidence — refuted findings are kept, not
   deleted; they are the record of what the second prosecutor tried.
4. Vague but suggestive ("error handling seems thin") → treat as a pointer:
   examine the named area yourself under the relevant count; the resulting
   finding (if any) is yours, credited "prompted by critic".

**Anti-capitulation rule:** you do not fix things merely because a critic
asserted them — that's confidence transfer, the exact failure quarantine
exists to stop. Every acted-on finding carries your verification evidence.

## Step 5 — Close

- Findings merged; critic identity, prompt file, and output file in the
  provenance table.
- Disagreements you refuted: summarized in one line each (the client may
  weigh them differently — they get to see what the second prosecutor
  believed).
- Hand the combined critique to `verdicts-and-breaches.md` for the ruling.

## Degraded modes

- **Critic returns garbage/timeout** → one retry with a sharpened brief
  (quote the failure back). Second failure → `hetero-critique: attempted,
  failed (<reason>)` in the record; proceed on self-critique alone.
- **Only same-family agents available** → still worth running (fresh context
  breaks *some* correlation); mark the record `same-family critic —
  decorrelation partial`.
