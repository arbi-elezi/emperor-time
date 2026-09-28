# Boot probe — lost-ps / HELLO.PS

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~05:19 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **GPL Ghostscript** 10.05.1 (`ghostscript` Debian package) |
| Binary | `/usr/bin/gs` |
| Reported | `GPL Ghostscript 10.05.1 (2025-04-29)` |
| Install | `apt-get install ghostscript` (Debian trixie; libs already present as `libgs10`) |

Probe used non-interactive file run
(`gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage HELLO.PS`)
on a minimal `%!PS` print source. Identify fossils
use `*.ps` + `*.eps`. Prefer `ghostscript` / `postscript`; bare `.ps`
is **refused** as a route tag (short-extension collision with `.ps1` /
PowerShell). Bare `gs` alone is **refused** as a route tag (two-letter
collision class with the Unix process-status command). Do not claim a
full Adobe Distiller / Level-3 RIP / printer-firmware recovery from a
print probe.

## Commands (VERIFIED)

```text
$ gs --version
10.05.1

$ gs -h | head -3
GPL Ghostscript 10.05.1 (2025-04-29)
Copyright (C) 2025 Artifex Software, Inc.  All rights reserved.
Usage: gs [switches] [file1.ps file2.ps ...]

$ gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage evals/fixtures/lost-ps/HELLO.PS
EMPEROR-TIME-PS-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is PostScript fossil named `HELLO.PS` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-ps` prints `1 *.ps` |
| Runs under GPL Ghostscript 10.05.1 file invocation | VERIFIED | `gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage HELLO.PS` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-PS-PROBE-OK` |
| Dialect is a specific Adobe PostScript Level / Distiller claim | CONJECTURE | No Level-1/2/3 or Distiller jury beyond `print` / `flush` / `quit` |
| Would run under period Adobe printer ROM / Display PostScript | UNVERIFIABLE here | No period Apple LaserWriter / NeXT DPS run in this session |
| Full PDF / EPS / overprint / spot-color pipeline | UNVERIFIABLE here | nullpage print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full PostScript Language Reference Manual
  (deferred; pin is **gs file invocation** — see
  `references/archaeology-postscript-manual.md`).
- No bare `.ps` route tag (short-extension collision with `.ps1`).
- No bare `gs` route tag (two-letter Unix `ps`/`gs` collision class).
