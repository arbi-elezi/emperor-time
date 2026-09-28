# Boot probe — lost-bc / HELLO.BC

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~08:35 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **bc** 1.07.1-4 (Debian; GNU bc) |
| Binary | `/usr/bin/bc` (GNU bc) |
| Reported | `bc 1.07.1` |
| Install | `apt-get install bc` (Debian trixie; deferred earlier on apt 500, now VERIFIED) |

Probe used file evaluation
(`bc HELLO.BC` / `bc -q HELLO.BC`)
on a minimal `print` + `quit` script. Identify fossils
use `*.bc` only. Prefer `bc` / `gnu-bc`. Bare `bc` is
**allowed** as a route tag because it is the tool binary name
(word-boundary match; does not false-hit `bcpl`). Bare `.bc` is
**refused** as a route tag (substring collision with BCPL `.bcpl`).
Do not claim a full POSIX bc / BSD bc / mathlib suite recovery from a
GNU bc `print`/`quit` probe alone — this leaf pins GNU bc file
evaluation. Companion to the dc leaf (`lost-dc`); both ship from the
GNU bc/dc package family.

## Commands (VERIFIED)

```text
$ dpkg -l bc | awk '/^ii/ {print $2, $3}'
bc 1.07.1-4

$ bc --version | head -1
bc 1.07.1

$ which bc
/usr/bin/bc

$ bc -q evals/fixtures/lost-bc/HELLO.BC
EMPEROR-TIME-BC-PROBE-OK
# exit 0

$ bc evals/fixtures/lost-bc/HELLO.BC
EMPEROR-TIME-BC-PROBE-OK
# exit 0
```

Note: GNU bc processes code from all files listed on the command line,
then would read stdin; the fixture ends with `quit` so the processor
halts without waiting for interactive input (bc(1) DESCRIPTION /
PSEUDO STATEMENTS `quit`). Documented VERIFIED forms are
**`bc HELLO.BC`** and **`bc -q HELLO.BC`**. There is no `-f` /
`--file` option on this GNU bc (unlike GNU dc).
`print "…\n"` is a GNU extension print statement (OPTIONS /
STATEMENTS print list).

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is bc fossil named `HELLO.BC` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-bc` prints `1 *.bc` |
| Runs under GNU bc 1.07.1 file evaluation | VERIFIED | `bc HELLO.BC` / `bc -q HELLO.BC` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-BC-PROBE-OK` |
| Dialect is a specific POSIX / BSD claim | CONJECTURE | No other bc jury beyond `print`/`quit` under GNU bc |
| Would run under period AT&T / POSIX-only bc | UNVERIFIABLE here | No period bc ROM / `-s` standard-only jury in this session |
| Full GNU bc mathlib / function suite | UNVERIFIABLE here | single print/quit probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU bc manual beyond
  DESCRIPTION file arguments + PSEUDO STATEMENTS `quit` + STATEMENTS
  `print` (deferred; pin is **bc FILE** with quit — see
  `references/archaeology-bc-manual.md`).
- Bare `bc` is allowed (tool binary name; word-boundary); bare `.bc`
  refused (BCPL `.bcpl` substring).
- No `*.gnu-bc` fossil this leaf (`.bc` only).
