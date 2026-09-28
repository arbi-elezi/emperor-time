# Boot probe — lost-dc / HELLO.DC

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~07:15 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **dc** 1.07.1-4 (`dc` Debian package; part of GNU bc) |
| Binary | `/usr/bin/dc` (GNU dc) |
| Reported | `dc (GNU bc 1.07.1) 1.4.1` |
| Install | `apt-get install dc` (Debian trixie) |

Probe used file evaluation
(`dc -f HELLO.DC` / `dc HELLO.DC`)
on a minimal `[string]P` print script. Identify fossils
use `*.dc` only. Prefer `dc` / `gnu-dc` / `.dc`. Bare `dc` is
**allowed** as a route tag because it is the tool binary name
(unlike English `scheme` / `basic` collisions, and unlike refused bare
`make` factory collision). Do not claim a full POSIX dc / BSD dc /
AT&T Seventh Edition dc suite recovery from a GNU dc
`[string]P` probe alone — this leaf pins GNU dc.

## Commands (VERIFIED)

```text
$ dpkg -l dc | awk '/^ii/ {print $2, $3}'
dc 1.07.1-4

$ dc --version | head -1
dc (GNU bc 1.07.1) 1.4.1

$ dc -f evals/fixtures/lost-dc/HELLO.DC
EMPEROR-TIME-DC-PROBE-OK
# exit 0

$ dc evals/fixtures/lost-dc/HELLO.DC
EMPEROR-TIME-DC-PROBE-OK
# exit 0
```

Note: GNU dc normally reads from standard input; if command
arguments are given, they are filenames and dc reads and executes
their contents (dc(1) DESCRIPTION / OPTIONS `-f` / `--file`).
Documented VERIFIED forms are **`dc -f HELLO.DC`** and
**`dc HELLO.DC`**. `[characters]P` pushes a string and prints it
without a trailing newline (Printing Commands / Strings).

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is dc fossil named `HELLO.DC` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-dc` prints `1 *.dc` |
| Runs under GNU dc 1.4.1 file evaluation | VERIFIED | `dc -f HELLO.DC` / `dc HELLO.DC` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-DC-PROBE-OK` |
| Dialect is a specific POSIX / BSD / AT&T claim | CONJECTURE | No other dc jury beyond `[string]P` under GNU dc |
| Would run under period AT&T / Seventh Edition dc ROM | UNVERIFIABLE here | No period dc ROM run in this session |
| Full GNU dc macro / register / array suite | UNVERIFIABLE here | single string-print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU dc manual beyond
  DESCRIPTION file arguments + OPTIONS `-f` / `--file` (deferred; pin is
  **dc -f FILE** — see `references/archaeology-dc-manual.md`).
- Bare `dc` is allowed (tool binary name); no English-collision refuse.
- No `*.gnu-dc` fossil this leaf (`.dc` only).
