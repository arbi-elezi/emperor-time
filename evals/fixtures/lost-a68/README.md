# lost-a68 fixture

Synthetic lost Algol 68 tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`, and
`evals/fixtures/lost-mod/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.A68` | DOS-era 8.3 caps filename; `print` prints `EMPEROR-TIME-A68-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until an Algol 68 interpreter runs)

**Named era+dialect from evidence alone:**

- Extension `.A68` / `.a68` / `.alg` + 8.3 uppercase name → Algol 68
  culture (Algol 68 Genie / a68g family *or* any Revised Report subset
  consuming the same `print` surface).
- Source uses only `BEGIN` / `print` / `new line` / `END` — dialect-honest
  (string-print probe, not a MODE / operator / parallel-clause claim).
- No `MODE`, no `OP`, no drawing / plotutils — deliberately minimal.

Until `a68g` / another Algol 68 implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running `a68g` binary or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-a68
# or: bash scripts/identify.sh evals/fixtures/lost-a68
```
