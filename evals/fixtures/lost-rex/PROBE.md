# Boot probe — lost-rex / HELLO.REX

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~01:26 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `regina-rexx` **3.9.5+dfsg1-0.1+b1** (Debian trixie) |
| Binary | `/usr/bin/rexx` (+ `/usr/bin/regina`) |
| Reported | REXX-Regina_**3.9.5** 5.00 25 Jun 2022 (64 bit) |
| Install | already present on this box (`regina-rexx`) |

Probe used `rexx` (Regina 3.9.5) on a source file with `SAY`. Uppercase
`HELLO.REX` is accepted as a source filename; that is normal REXX scripting
culture, not a probe failure. Identify fossils use `*.rex` / `*.rexx` (no
known collision with other house fossils). Bare English keyword `say` alone
is **refused** as a route tag; prefer `regina` / `.rex` / `.rexx` /
space-intent `rexx`.

## Commands (VERIFIED)

Working directory for load/run: fixture dir (and earlier `/tmp` copy).

```text
$ rexx -v
rexx: REXX-Regina_3.9.5 5.00 25 Jun 2022 (64 bit)

$ rexx HELLO.REX
EMPEROR-TIME-REX-PROBE-OK
# exit 0

$ regina HELLO.REX
EMPEROR-TIME-REX-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is REXX fossil named `HELLO.REX` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-rex` prints `1 *.rex` |
| Runs under Regina 3.9.5 (`rexx` / `regina` file arg) | VERIFIED | `rexx HELLO.REX` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-REX-PROBE-OK` |
| Dialect is a specific ANSI year / TRL-2 claim beyond SAY | CONJECTURE | No ANSI jury; SAY subset only |
| Would run under period CMS / TSO / OS/2 REXX on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased Cowlishaw book clause (deferred; pin is
  Classic Rexx SAY — see `references/archaeology-rexx-manual.md`).
- No ooRexx / NetRexx / ADDRESS command host claim.
- No Regina external-function / GCI claim.
