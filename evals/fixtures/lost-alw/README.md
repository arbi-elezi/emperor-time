# lost-alw fixture

Synthetic lost Algol W tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
and `evals/fixtures/lost-a60/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ALW` | DOS-era 8.3 caps filename; `WRITE` prints `EMPEROR-TIME-ALW-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Algol W compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.ALW` / `.alw` + 8.3 uppercase name → Algol W culture
  (Awe / OS/360 ALGOL W family consuming the same `WRITE` surface).
- Source uses only `begin` / `write` / `end.` — dialect-honest
  (string-print probe, not a full record / complex / call-by-name claim).
- No records, no complex, no name-parameter gymnastics — deliberately minimal.
- Fossils deliberately use `*.alw` (not `*.a60` / `*.a68` / `*.alg`) so
  identify does not collide with ALGOL 60 or Algol 68 leaves.

Until `awe` / another Algol W implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `awe` binary
or emulator trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-alw
# or: bash scripts/identify.sh evals/fixtures/lost-alw
```
