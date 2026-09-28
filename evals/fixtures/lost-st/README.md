# lost-st fixture

Synthetic lost Smalltalk tree for Emperor Time archaeology drills.

Sister probe to `evals/fixtures/lost-pas/`, `evals/fixtures/lost-asm/`,
`evals/fixtures/lost-cbl/`, `evals/fixtures/lost-f90/`,
`evals/fixtures/lost-vhd/`, `evals/fixtures/lost-ada/`,
`evals/fixtures/lost-fs/`, `evals/fixtures/lost-lisp/`,
`evals/fixtures/lost-prolog/`, `evals/fixtures/lost-tcl/`,
`evals/fixtures/lost-erl/`, `evals/fixtures/lost-rex/`,
`evals/fixtures/lost-mod/`, `evals/fixtures/lost-a68/`,
`evals/fixtures/lost-a60/`, `evals/fixtures/lost-alw/`,
`evals/fixtures/lost-icn/`, `evals/fixtures/lost-obn/`,
`evals/fixtures/lost-sno/`, `evals/fixtures/lost-cim/`,
`evals/fixtures/lost-apl/`, `evals/fixtures/lost-bcpl/`,
and `evals/fixtures/lost-pli/`.

## Artifacts

| File | Role |
|------|------|
| `HELLO.ST` | DOS-era 8.3 caps filename; `Transcript show: …; cr.` prints `EMPEROR-TIME-ST-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a Smalltalk system runs)

**Named era+dialect from evidence alone:**

- Extension `.ST` / `.st` + 8.3 uppercase name → Smalltalk file-in culture
  (GNU Smalltalk / Smalltalk-80 family consuming the same `Transcript show:` /
  `cr` print surface).
- Source uses only `Transcript show: '…'; cr.` —
  dialect-honest (print probe, not a full Morphic / Pharo / Squeak image claim).
- No tradenames beyond the filename culture — deliberately minimal.
- Fossils deliberately use `*.st` only (not `*.cs` changeset — C# collision).

Until `gst` / another Smalltalk implementation runs against this file, the
dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running Smalltalk
image or file-in trace. See `references/archaeology.md`
and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one
manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-st
# or: bash scripts/identify.sh evals/fixtures/lost-st
```
