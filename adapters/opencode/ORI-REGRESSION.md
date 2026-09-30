# ORI agent-regression contract (stranger checklist)

**Home:** `adapters/opencode/` (Activation / stranger path). Not Bakeoff. Not Astra.
**Version:** tip at ship time; stay **0.4.174** / Bakeoff PIN **0.4.171** (no swap).
**Example artefact:** `ori-regression.example.yaml` (lab default slug locked).

Goal: a stranger can pin one named model, one tools allowlist, one foreign tiny ask,
and triage the result without soft “it worked once” claims. Parallel lane to graph /
mid-flash doctrine under `references/` (that lane is out of scope here).

---

## 1. Clone / tip pin

1. Clone `emperor-time` (or pull) and record tip SHA.
2. Confirm version string is **0.4.174** (or the cool-down tip you were handed). Do
   **not** bump. Do **not** swap the Bakeoff PIN (**0.4.171**).
3. `export PATH="$HOME/.local/bin:$PATH"` so `opencode` resolves (PATH footgun is a
   common **blocked**).

---

## 2. Wire ET (boot, activate, ask-to-spec, done)

On a **foreign** disposable repo (not emperor-time itself, not bakeoff T1–T4 cells):

1. Copy tip `AGENTS.md` (or the short pointer from this adapter README).
2. Symlink or path `scripts/` to tip scripts so `boot` / `activate` / `done` resolve.
3. Copy `adapters/opencode/config.snippet.yaml` into foreign `.emperor/config.yaml`
   (judgment **off**; iron `always_hard` stays hard).
4. Run the structure path:

```bash
python3 $ET/scripts/lib/boot.py --root . --skip-eval
# read .emperor/host.env + survey.md

python3 $ET/scripts/lib/activate.py --cwd . -u "<foreign tiny ask>"
# open ACTIVATION next=

python3 $ET/scripts/lib/ask_spec.py --emit --effort-class tiny \
  --write .emperor/tasks/<id>/ask-spec.md "<foreign tiny ask>"

# …smallest honest change…

python3 $ET/scripts/lib/done.py .emperor/tasks/<id>
```

---

## 3. ORI live under a real TTY

ORI live PASS needs the **OpenCode binary** on a real TTY (Bet D hang class).

```bash
# GNU/util-linux
timeout 90 script -q -c \
  'opencode run -m openrouter/stealth/space-bunny-alpha --dir . "<ask>"' \
  /dev/null

# portable: python3 pty.spawn([...])
```

Agent/CI pipes often hang after `init` (EXIT 124). Bare `opencode run` without
`script`/`pty` is not an ORI live attempt. Direct OpenRouter HTTPS alone is a
compat probe, not ORI live PASS.

`OPENROUTER_API_KEY` lives in the environment only. Never print, commit, or paste
it into a receipt.

---

## 4. Named model slug (no silent swap)

Lock the slug in the contract artefact before you run. Lab default example:

`openrouter/stealth/space-bunny-alpha`

If that slug is unavailable, rate-limited, or renamed: mark **blocked** and ask PO.
Do **not** silently substitute another model and call it the same contract.

---

## 5. Tools allowlist

For the tiny ask, OpenCode/ORI may use only what the contract lists. Example minimum:

- read / list files in the foreign tree
- edit one small file (wording / one-liner class)
- bash for bounded probes (`timeout`, `script`, `python3` of tip scripts)

Do **not** open PRs, send messages, purchase, or touch secrets stores from the
smoke. Consent gates stay iron hard.

---

## 6. One foreign tiny ask

Pick a disposable foreign repo. One-line template (fill the blanks):

> In `<foreign-root>`, change `<one file>` so `<one observable>` holds; do not
> touch emperor-time or invent a Bakeoff cell.

Keep the ask tiny. One wording fix or one-liner is enough to exercise the path.

---

## 7. Triage (ET-bug vs model-FAIL vs blocked)

| Label | When |
|---|---|
| **PASS** | Structure path honest (done exit 0 + probes) and/or ORI live under TTY with the **named** slug did the tiny ask |
| **ET-bug** | Probes/config/scripts wrong; ET path failed before the model had a fair shot |
| **model-FAIL** | ET path correct; model output nonsense / refused the tiny ask / broke the tree |
| **blocked** | No OpenCode binary, PATH miss, non-TTY hang (124), missing key, slug unavailable |

File a short receipt under
`/workspace/field-receipts/receipts/<date>/…/` with CONTEXT / BEFORE / AFTER /
NOTES / claim. Label it **contract exercise** or **coding toolchain**, not a new
Bakeoff Run cell.

---

## 8. Hard invariants

- **Iron hard.** Judgment **off** for smoke. Secrets **env-only**.
- **No Bakeoff cell invention.** No PIN swap. Stay 0.4.174 / PIN 0.4.171.
- **Not Astra.** A green space-bunny smoke is not mid-flash = Astra and not
  equal-UX without a green OpenCode-binary foreign receipt **and** PO claim ACCEPT.
- **No silent model swap.** Unavailable slug means **BLOCKED** + ask PO.
- Do not edit `references/` from this contract (other lane).

---

## 9. Fail-closed

If anything above cannot be met honestly, stop and label **blocked** (or ET-bug /
model-FAIL). Soften nothing. Ask PO before changing the locked slug or claim bar.
