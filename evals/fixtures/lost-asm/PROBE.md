# Boot probe — lost-asm / FOO.ASM

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-27 ~12:04 CEST

## Toolchain

| Item | Value |
|------|-------|
| Assembler | `nasm` **2.16.03** (`nasm 2.16.03-1` Debian trixie) |
| Binary | `/usr/bin/nasm` |
| Linker | GNU `ld` from **binutils 2.44-3** (`ld --version` → 2.44) |
| Also present | GNU `as`/`gas` 2.44 (binutils) — **not** used for the verified build |
| Install | `sudo DEBIAN_FRONTEND=noninteractive apt-get install -y nasm` → exit **0** (`as`/`ld` already installed) |

MASM / TASM / DOSBox were **not** present. Probe used NASM Linux ELF64 because that is what can actually assemble+link+run on this box.

## Commands (VERIFIED)

Working directory for assemble/link/run: `/tmp/asm-probe` (copy of `FOO.ASM`; binary not committed).

```text
$ nasm -v
NASM version 2.16.03

$ nasm -f elf64 -o FOO.o FOO.ASM
# exit 0

$ ld -o FOO FOO.o
# exit 0

$ ./FOO
EMPEROR-TIME-ASM-PROBE-OK
# exit 0

$ file FOO
FOO: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is ASM fossil named `FOO.ASM` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-asm` prints `1 *.asm` |
| Assembles under NASM 2.16.03 elf64 | VERIFIED | `nasm -f elf64 -o FOO.o FOO.ASM` exit 0 |
| Links under GNU ld 2.44 | VERIFIED | `ld -o FOO FOO.o` exit 0 |
| Prints known string | VERIFIED | stdout exactly `EMPEROR-TIME-ASM-PROBE-OK` (plus trailing newline) |
| Dialect is MASM / DOS 16-bit | CONJECTURE only for filename culture | Runnable source is NASM Linux x86-64 syscalls; MASM not run |
| Would run under DOS MASM on original media | UNVERIFIABLE here | No DOS emulator / MASM in this session |

## Not done (honest gaps)

- No Jail-hunt of a contemporaneous MASM/NASM manual heading (deferred).
- No DOSBox / 16-bit rewrite.
- No AT&T `gas` rewrite of the same probe.
- No port to Python (forbidden by doctrine).
