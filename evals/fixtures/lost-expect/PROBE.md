# Boot probe — lost-expect / HELLO.EXP

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~08:49 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **expect** 5.45.4-4 (Debian; pulls **tcl-expect**) |
| Binary | `/usr/bin/expect` (Expect 5 / Don Libes) |
| Reported | `expect version 5.45.4` |
| Install | `apt-get install expect` (Debian trixie) |

Probe used script-file evaluation
(`expect HELLO.EXP`)
on a minimal `puts` + `exit 0` script. Identify fossils
use `*.exp` only. Prefer `expect` / `tcl-expect` / `.exp`. Bare `expect`
is **allowed** as a route tag because it is the tool binary name
(word-boundary match). Bare `.exp` is **allowed** (no known substring
collision with peer excavate fossils). Do not claim a full Expect /
spawn/expect/send dialogue suite recovery from a `puts`/`exit` probe
alone — this leaf pins Expect cmdfile evaluation. Companion to the Tcl
leaf (`lost-tcl`); Expect is a Tcl-based programmed-dialogue tool.

## Commands (VERIFIED)

```text
$ dpkg -l expect | awk '/^ii/ {print $2, $3}'
expect 5.45.4-4

$ expect -v
expect version 5.45.4

$ which expect
/usr/bin/expect

$ expect evals/fixtures/lost-expect/HELLO.EXP
EMPEROR-TIME-EXPECT-PROBE-OK
# exit 0
```

Note: Expect reads `cmdfile` for a list of commands to execute
(expect(1) USAGE). Documented VERIFIED form is **`expect HELLO.EXP`**.
Optional `expect -f HELLO.EXP` is the same surface when `-f` is used
(#! notation / USAGE). `puts` is Tcl string output; `exit 0` terminates
with status 0 (COMMANDS `exit`).

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Expect fossil named `HELLO.EXP` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-expect` prints `1 *.exp` |
| Runs under Expect 5.45.4 cmdfile evaluation | VERIFIED | `expect HELLO.EXP` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-EXPECT-PROBE-OK` |
| Dialect is a specific Expectk / libexpect claim | CONJECTURE | No Expectk / C libexpect jury beyond `puts`/`exit` under Expect |
| Would run under period Expect 4 / non-Tcl Expect | UNVERIFIABLE here | No period Expect ROM in this session |
| Full spawn/expect/send dialogue suite | UNVERIFIABLE here | single puts/exit probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Expect manual beyond
  SYNOPSIS cmdfile + USAGE "Expect reads cmdfile" + COMMANDS `puts`
  (Tcl) / `exit` (deferred; pin is **expect FILE** — see
  `references/archaeology-expect-manual.md`).
- Bare `expect` is allowed (tool binary name; word-boundary); bare
  `.exp` allowed (no peer collision).
- No `*.tcl` fossil this leaf (Tcl already has `lost-tcl`); Expect
  scripts commonly use `.exp`.
