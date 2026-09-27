# Boot probe — lost-prolog / HELLO.PRO

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~00:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `swi-prolog-nox` **9.2.9+dfsg-1+b1** (Debian trixie) |
| Binary | `/usr/bin/swipl` |
| Reported | `SWI-Prolog version 9.2.9 for x86_64-linux` |
| Install | `sudo apt-get update && sudo apt-get install -y swi-prolog-nox` → exit **0** |

GNU Prolog (`gprolog`) was **not** installed on this box for the probe. Probe
used SWI-Prolog 9.2.9 on Linux because that is what can actually consult+run
on this host. Uppercase `HELLO.PRO` is accepted as a source filename; that is
documented SWI scripting culture (extension need not be `.pl`), not a probe
failure. Identify fossils deliberately omit `*.pl` (Perl collision).

## Commands (VERIFIED)

Working directory for load/run: `/tmp/prolog-probe` (copy of `HELLO.PRO`;
no `.qlf` / saved-state committed).

```text
$ swipl --version
SWI-Prolog version 9.2.9 for x86_64-linux

$ swipl -q -t halt HELLO.PRO
EMPEROR-TIME-PROLOG-PROBE-OK
# exit 0

$ swipl -q HELLO.PRO
EMPEROR-TIME-PROLOG-PROBE-OK
# exit 0 (initialization(..., main) sets toplevel to halt/0)
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Prolog fossil named `HELLO.PRO` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-prolog` prints `1 *.pro` |
| Runs under SWI-Prolog 9.2.9 (`initialization/2` main) | VERIFIED | `swipl -q -t halt HELLO.PRO` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-PROLOG-PROBE-OK` |
| Dialect is ISO Prolog specifically | CONJECTURE | No ISO/IEC 13211 jury PDF; `write/1` / `nl/0` / `halt/0` subset only |
| Would run under period DEC-10 / Quintus on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased ISO/IEC 13211 clause book (deferred; pin is
  SWI-Prolog `initialization/2` main role — see
  `references/archaeology-prolog-manual.md`).
- No GNU Prolog / SICStus compile.
- No DCG / CLP(FD) / module claim.
