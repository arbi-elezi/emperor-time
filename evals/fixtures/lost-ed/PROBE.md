# Boot probe — lost-ed / HELLO.ED

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~06:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **ed** 1.21.1-1 (`ed` Debian package) |
| Binary | `/usr/bin/ed` (GNU ed) |
| Reported | `GNU ed 1.21.1` |
| Install | `apt-get install ed` (Debian trixie) |

Probe used script-mode stdin redirection
(`ed -s < HELLO.ED`)
on a minimal `a` / `,p` / `Q` ed script. Identify fossils
use `*.ed` only. Prefer `ed` / `gnu-ed` / `.ed`. Bare `ed` is
**allowed** as a route tag because it is the tool binary name
(unlike English `scheme` / `basic` collisions, and unlike refused bare
`gs` two-letter process-status collision). Do not claim a full POSIX
ed / BSD ed / Plan 9 ed suite recovery from a GNU ed
`a`/`,p`/`Q` probe alone — this leaf pins GNU ed.

## Commands (VERIFIED)

```text
$ dpkg -l ed | awk '/^ii/ {print $2, $3}'
ed 1.21.1-1

$ ed --version | head -1
GNU ed 1.21.1

$ ed -s < evals/fixtures/lost-ed/HELLO.ED
EMPEROR-TIME-ED-PROBE-OK
# exit 0
```

Note: GNU ed reads editing commands from standard input
(Invoking ed / `-s` / `--script`). Documented VERIFIED form is
**`ed -s < HELLO.ED`** with classic append / print / quit commands.
`-s` suppresses byte counts so the probe string is the only stdout.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is ed fossil named `HELLO.ED` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-ed` prints `1 *.ed` |
| Runs under GNU ed 1.21.1 script-mode stdin | VERIFIED | `ed -s < HELLO.ED` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-ED-PROBE-OK` |
| Dialect is a specific POSIX / BSD / Plan 9 claim | CONJECTURE | No other ed jury beyond `a`/`,p`/`Q` under GNU ed |
| Would run under period AT&T / Seventh Edition ed ROM | UNVERIFIABLE here | No period ed ROM run in this session |
| Full GNU ed regex / global / restricted (`red`) suite | UNVERIFIABLE here | single append/print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU ed manual beyond
  Invoking ed / `-s` / `--script` (deferred; pin is **ed -s < FILE**
  — see `references/archaeology-ed-manual.md`).
- Bare `ed` is allowed (tool binary name); no English-collision refuse.
- No `*.gnu-ed` fossil this leaf (`.ed` only).
