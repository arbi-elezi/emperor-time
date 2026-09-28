# Boot probe — lost-icn / HELLO.ICN

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~02:39 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | Debian **icont** / **iconx** `9.5.24b-1` |
| Binary | `/usr/bin/icont` (translator), `/usr/bin/iconx` (executor) |
| Reported | `Icon Version 9.5.24b, November 19, 2024  (linux)` |
| Install | `apt-get install icont iconx` on this box |

Probe used `icont` (Icon 9.5.24b) to translate an Icon program with
standard `write` into an icode executable and run it. Identify fossils use
`*.icn` only. Prefer `icont` / `iconx` / `.icn`; bare English token `icon`
alone is **refused** as a route tag (UI-icon collision class), and bare
`write` is likewise refused. On Linux, `icont` lowercases the `.icn`
suffix when opening the source, so the probe links `hello.icn` →
`HELLO.ICN` before translate. Do not commit generated icode binaries or
`.u1` / `.u2` ucode files from the probe.

## Commands (VERIFIED)

Working directory for run: fixture dir (or any dir with the source).

```text
$ icont -V
Icon Version 9.5.24b, November 19, 2024  (linux)

$ ln -sf HELLO.ICN hello.icn
$ icont -s hello.icn
# exit 0

$ ./hello
EMPEROR-TIME-ICN-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Icon fossil named `HELLO.ICN` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-icn` prints `1 *.icn` |
| Translates under Icon 9.5.24b icont | VERIFIED | `icont -s hello.icn` exit 0 |
| Runs and prints known string | VERIFIED | stdout is `EMPEROR-TIME-ICN-PROBE-OK` |
| Dialect is a specific Icon book / Unicon full claim beyond write/main | CONJECTURE | No Griswold jury beyond IPD244 File Names + write; Unicon not claimed |
| Would run under period Icon on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Icon string-scanning / goal-directed set
  (deferred; pin is Icon 9 UNIX Manual Page SYNOPSIS / File Names —
  see `references/archaeology-icon-manual.md`).
- No Unicon claim (different dialect; not this leaf).
- No bare `icon` route tag (UI-icon English collision).
