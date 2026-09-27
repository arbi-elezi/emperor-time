# lost-asm fixture

Synthetic lost assembly tree for Emperor Time archaeology drills.
Sister probe to `evals/fixtures/lost-pas/`.

## Artifacts

| File | Role |
|------|------|
| `FOO.ASM` | DOS-era 8.3 caps filename; prints `EMPEROR-TIME-ASM-PROBE-OK` |
| `PROBE.md` | Boot-probe log (VERIFIED or UNVERIFIABLE) |
| `identify-smoke.txt` | Captured `identify` survey snippet for this fixture |

## Dialect CONJECTURE (honest split)

**Filename culture (CONJECTURE from surface evidence):**

- Extension `.ASM` + 8.3 uppercase name → late-DOS / early-Windows assembly source culture (MASM / TASM-adjacent *naming* habit).

**Runnable dialect on this Linux box (see PROBE.md — VERIFIED):**

- **NASM** Intel syntax, **Linux x86-64 ELF**, raw `syscall` (sys_write / sys_exit).
- Assembled with `nasm -f elf64`, linked with GNU `ld`.
- **Not** MASM. **Not** TASM. **Not** 16-bit DOS `.COM` / `INT 21h`.
- GNU `as`/`gas` was present but unused for the verified probe (source is NASM syntax, not AT&T).

Claiming “MASM” or “DOS COM” would be a lie: those toolchains were not run here. The 8.3 caps name is archaeological costume; the binary that actually prints is NASM+ld ELF64.

## Doctrine reminder

Do **not** port this to Python / C. Understanding is a running binary or emulator trace.
See `references/archaeology.md`.

## Survey command

```bash
scripts/emperor identify evals/fixtures/lost-asm
# or: bash scripts/identify.sh evals/fixtures/lost-asm
```

On main, `excavate` is not yet a first-class tool (open PR); `identify` is the survey.
