# Boot probe — lost-make / Makefile

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~07:02 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **make** 4.4.1-2 (`make` Debian package; `gmake` → `make`) |
| Binary | `/usr/bin/make` (GNU Make); `/usr/bin/gmake` symlink |
| Reported | `GNU Make 4.4.1` |
| Install | preinstalled on this box (`dpkg -l make`) |

Probe used default-name makefile discovery and `-f` file form
(`make -C …` / `make -f HELLO.MK`)
on a minimal `.PHONY: all` recipe. Identify fossils use
`Makefile` / `makefile` / `*.mak` / `*.mk`. Prefer `gmake` /
`gnu-make` / `.mk` / `.mak` / `makefile`. Bare English `make` is
**refused** as a route tag because it collides with factory speech
("make software") and common English — unlike bare `ed` / `m4` /
`sed` / `awk` tool-binary tags. Do not claim a full POSIX make /
BSD make / Automake suite recovery from a GNU Make
`.PHONY`/`echo` probe alone — this leaf pins GNU Make.

## Commands (VERIFIED)

```text
$ dpkg -l make | awk '/^ii/ {print $2, $3}'
make 4.4.1-2

$ make --version | head -1
GNU Make 4.4.1

$ make -C evals/fixtures/lost-make
EMPEROR-TIME-MAKE-PROBE-OK
# exit 0

$ make -f evals/fixtures/lost-make/HELLO.MK
EMPEROR-TIME-MAKE-PROBE-OK
# exit 0

$ gmake -f evals/fixtures/lost-make/HELLO.MK
EMPEROR-TIME-MAKE-PROBE-OK
# exit 0
```

Note: GNU Make reads a makefile named `GNUmakefile`, `makefile`, or
`Makefile` by default, or a named file via `-f` / `--file` /
`--makefile` (make(1) DESCRIPTION / OPTIONS). Documented VERIFIED
forms are **`make -C lost-make`** (default `Makefile`) and
**`make -f HELLO.MK`**.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source includes Makefile + HELLO.MK fossils | VERIFIED | identify prints `Makefile` / `makefile` / `*.mk` |
| Runs under GNU Make 4.4.1 default-name / `-f` | VERIFIED | `make -C` and `make -f HELLO.MK` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-MAKE-PROBE-OK` |
| Dialect is a specific POSIX / BSD / Automake claim | CONJECTURE | No other make jury beyond `.PHONY`/`echo` under GNU Make |
| Would run under period AT&T / Seventh Edition make ROM | UNVERIFIABLE here | No period make ROM run in this session |
| Full GNU Make implicit-rule / secondary-expansion suite | UNVERIFIABLE here | single recipe probe only |

## Not done (honest gaps)

- No Jail-hunt of the full GNU Make manual beyond
  make(1) DESCRIPTION default-name search + OPTIONS `-f` /
  `--file` / `--makefile` (deferred; pin is **Makefile /
  make -f FILE** — see `references/archaeology-make-manual.md`).
- Bare English `make` is refused (factory / common-English collision).
- No `*.gnu-make` fossil this leaf (`Makefile` / `HELLO.MK` only).
