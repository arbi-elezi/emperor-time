# Boot probe — lost-pli / HELLO.PLI

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~04:39 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Iron Spring PL/I** 1.4.1 from http://www.iron-spring.com/pli-1.4.1.tgz |
| Binary | `/tmp/toolchain-probe/pli/pli-1.4.1/plic` (prefix after local extract) |
| Reported | `Iron Spring PL/I compiler 1.4.1  [Linux] 15 Apr, 2026` |
| Install | extract `pli-1.4.1.tgz` → use `plic` + `lib/libprf.a`; link needs binutils `ld` elf32-i386 (gcc-multilib / libc6-i386 on 64-bit hosts) |

Probe used non-interactive compile-link-run
(`plic -C -lixg -ew HELLO.PLI -o hello.o` then standalone `ld … -lprf` then `./hello`)
on a `PROCEDURE OPTIONS(MAIN)` / `PUT SKIP LIST` print source. Identify fossils
use `*.pli` and `*.pl1`. Prefer `plic` / `pli` / `pl1` / `iron-spring` / `.pli` /
`.pl1`; bare English tokens (`put` / `procedure` / `options` / `main`) alone are
**refused** as route tags (keyword collision class). Do not commit compiler
listings (`*.lst`), object (`hello.o`), map (`hello.map`), or the linked `hello`
binary from the probe.

## Commands (VERIFIED)

Working directory: any dir with the source (fixture dir used) and
`plic` on `PATH` with `-L` pointing at the distribution `lib/` (or
`libprf.a` installed system-wide).

```text
$ /tmp/toolchain-probe/pli/pli-1.4.1/plic -V
Iron Spring PL/I compiler 1.4.1  [Linux] 15 Apr, 2026
Copyright Iron Spring Software, 2024, 2025, 2026
(http://www.iron-spring.com)

$ export PATH=/tmp/toolchain-probe/pli/pli-1.4.1:$PATH
$ plic -C -lixg -ew HELLO.PLI -o hello.o
$ ld -z muldefs -Bstatic -e main -o hello hello.o \
    --oformat=elf32-i386 -melf_i386 \
    -L/tmp/toolchain-probe/pli/pli-1.4.1/lib -lprf
$ ./hello
EMPEROR-TIME-PLI-PROBE-OK
# exit 0  (PUT LIST may pad a trailing space before newline)
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is PL/I fossil named `HELLO.PLI` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-pli` prints `1 *.pli` |
| Compiles+links+runs under Iron Spring PL/I 1.4.1 (15 Apr 2026) | VERIFIED | `plic -C …` + `ld … -lprf` + `./hello` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-PLI-PROBE-OK` |
| Dialect is a specific IBM MVS/VM / Enterprise full claim | CONJECTURE | No mainframe / Enterprise jury beyond `PUT SKIP LIST` print |
| Would run under period IBM PL/I on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Iron Spring / IBM PL/I language reference
  (deferred; pin is **plic `-C`** compile + standalone **ld `-lprf`** link-run —
  see `references/archaeology-pli-manual.md`).
- No bare English keyword route tags (`put` / `procedure` / `options` / `main`).
