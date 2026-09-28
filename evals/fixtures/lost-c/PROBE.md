# Boot probe — lost-c / HELLO.c

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~09:58 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **gcc** 4:14.2.0-1 (Depends **gcc-14** 14.2.0-19) |
| Binary | `/usr/bin/gcc` → `gcc-14` |
| Reported | `gcc (Debian 14.2.0-19) 14.2.0` |
| Install | already present on box (no apt this leaf) |

Probe used compile-then-run
(`gcc HELLO.c -o HELLO` → `./HELLO`)
on a minimal `main` / `puts` program. Identify fossils
use `*.c` only. GCC treats lowercase `.c` as C source that must be
preprocessed; uppercase `.C` is C++ (do not use `.C` for this leaf).
Prefer `gcc` / `gcc14` / `c11` / `.c`. Bare `c` is **refused** as a
route tag (single-letter / common-English collision). Bare `.c` is
**allowed** with extension-boundary matching (does not prefix-hit
`.cbl` / `.cl`). Systems compile-and-run leaf after Rust; toolchain
already on box (Worthy Spend vs TeXlive).
Do not claim a full ISO C standard library / multi-TU / linker-script
recovery from a `puts` probe alone — this leaf pins C
compile-and-run via `gcc` + binary execution.

## Commands (VERIFIED)

```text
$ dpkg -l gcc gcc-14 | awk '/^ii/ {print $2, $3}'
gcc 4:14.2.0-1
gcc-14 14.2.0-19

$ gcc --version | head -1
gcc (Debian 14.2.0-19) 14.2.0

$ which gcc
/usr/bin/gcc

$ gcc HELLO.c -o HELLO
$ ./HELLO
EMPEROR-TIME-C-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs GCC 14.2 and executes `HELLO` after `gcc HELLO.c -o HELLO` | VERIFIED |
| Filename culture (8.3 caps / mixed-case `.C`) maps to this dialect | CONJECTURE (GCC maps `.C` to C++) |
| Full freestanding / hosted ISO C / multi-file link recovery | UNVERIFIABLE from puts probe alone |
