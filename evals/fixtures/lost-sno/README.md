# lost-sno fixture

Synthetic lost SNOBOL4 tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, and `evals/fixtures/lost-obn/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.SNO` | DOS-era 8.3 caps filename; `OUTPUT =` prints `EMPEROR-TIME-SNO-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a SNOBOL interpreter runs)

**Named era+dialect from evidence alone:**

- Extension `.SNO` / `.sno` + 8.3 uppercase name → SNOBOL4 culture
  (CSNOBOL4 / Macro SNOBOL4 / SPITBOL family consuming the same
  `OUTPUT` / `END` surface).
- Source uses only `OUTPUT = "…"` / `END` — dialect-honest (string-print
  probe, not a full pattern-matching / REPLACE claim).
- No pattern match, no `INPUT`, no `TABLE()` — deliberately minimal.
- Fossils deliberately use `*.sno` only.

Until `snobol4` / another SNOBOL4 implementation runs against this file,
the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `snobol4`
executable or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-sno
# or: bash scripts/identify.sh evals/fixtures/lost-sno
```
