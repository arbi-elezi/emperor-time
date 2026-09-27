# lost-erl fixture

Synthetic lost Erlang tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, and `evals/fixtures/lost-tcl/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ERL` | DOS-era 8.3 caps filename; escript `main/1` prints `EMPEROR-TIME-ERL-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Erlang runs)

**Named era+dialect from evidence alone:**

- Extension `.ERL` / `.erl` / `.hrl` + 8.3 uppercase name → Erlang / OTP
  script culture (OTP 27 family *or* any `escript` / `erl` consuming the
  same `main/1` + `io:format` surface).
- Source uses only escript header + `main/1` + `io:format` — dialect-honest
  (string-print probe, not a gen_server or release claim).
- No `-module` required for escript source form, no OTP app, no Elixir —
  deliberately minimal.

Until `escript` / another Erlang runs against this file, the dialect label
stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `escript` or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-erl
# or: bash scripts/identify.sh evals/fixtures/lost-erl
```
