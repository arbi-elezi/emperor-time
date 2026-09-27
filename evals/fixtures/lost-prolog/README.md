# lost-prolog fixture

Synthetic lost Prolog tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, and `evals/fixtures/lost-lisp/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.PRO` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-PROLOG-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Prolog runs)

**Named era+dialect from evidence alone:**

- Extension `.PRO` / `.pro` / `.prolog` + 8.3 uppercase name → Prolog
  source culture (ISO/Edinburgh family *or* SWI / GNU Prolog consuming the
  same `write` / `nl` / `halt` surface). **Not** `*.pl` — that fossil is
  reserved for Perl collision avoidance in identify.
- Source uses only `write/1`, `nl/0`, `halt/0`, and `initialization/2` with
  role `main` — Edinburgh-compatible enough that SWI-Prolog and other
  ISO-ish Prologs accepting that subset would both accept this surface.
- No DCG, no CLP, no modules, no operator declarations — deliberately
  dialect-honest (string-print probe, not an ISO year claim).

Until `swipl` / `gprolog` / another Prolog runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running consult or
emulator trace. See `references/archaeology.md` and prior ET lost-tree loop:
survey → name era+dialect → Jail-hunt one manual heading → boot probe →
characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-prolog
# or: bash scripts/identify.sh evals/fixtures/lost-prolog
```
