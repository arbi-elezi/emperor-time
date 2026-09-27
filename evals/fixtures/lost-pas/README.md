# lost-pas fixture

Synthetic lost Pascal tree for Emperor Time archaeology drills.

## Artifacts

| File | Role |
|------|------|
| `HELLO.PAS` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-PAS-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (not VERIFIED until a compiler runs)

**Named era+dialect from evidence alone:**

- Extension `.PAS` + 8.3 uppercase name → late-DOS / early-Windows Pascal source culture (Turbo Pascal / Borland-adjacent *or* Free Pascal ISO mode consuming the same surface).
- Source uses only `program` / `begin` / `writeln` / `end.` — ISO 7185–compatible enough that Free Pascal (`fpc -Miso` or default mode for this subset) and classic Turbo Pascal would both accept it.
- **No** Turbo-only units (`Crt`, `Dos`), no `{$…}` directives, no Object Pascal — deliberately dialect-honest and Turbo-adjacent without claiming a recovered floppy binary.

Until `fpc`/`tpc` (or an emulator) runs against this file, the dialect label stays **CONJECTURE**.

## Doctrine reminder

Do **not** port this to Python. Understanding is a running binary or emulator trace.
See `references/archaeology.md` and prior ET lost-tree loop: survey → name era+dialect → Jail-hunt one manual heading → boot probe → characterize → factory.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-pas
# or: bash scripts/identify.sh evals/fixtures/lost-pas
```

On main, `excavate` is not yet a first-class tool (open PR); `identify` is the survey.
