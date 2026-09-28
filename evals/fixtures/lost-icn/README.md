# lost-icn fixture

Synthetic lost Icon tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, and `evals/fixtures/lost-alw/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ICN` | DOS-era 8.3 caps filename; `write` prints `EMPEROR-TIME-ICN-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Icon translator runs)

**Named era+dialect from evidence alone:**

- Extension `.ICN` / `.icn` + 8.3 uppercase name → Icon culture
  (University of Arizona Icon / Unicon family consuming the same `write` /
  `procedure main` surface).
- Source uses only `procedure main` / `write` / `end` — dialect-honest
  (string-print probe, not a full goal-directed / string-scanning claim).
- No scanning, no generators, no co-expressions — deliberately minimal.
- Fossils deliberately use `*.icn` only so identify does not invent
  Unicon-only extensions for this leaf.

Until `icont` / another Icon implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `icont`+`iconx`
icode binary or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-icn
# or: bash scripts/identify.sh evals/fixtures/lost-icn
```
