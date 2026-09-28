# Boot probe — lost-yacc / HELLO.Y

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~07:43 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **bison** 2:3.8.2+dfsg-1+b2 (Debian package; GNU Bison) |
| Binary | `/usr/bin/bison` (GNU Bison); `/usr/bin/yacc` → alternatives → `bison.yacc` |
| Reported | `bison (GNU Bison) 3.8.2` |
| Install | `apt-get install bison` (Debian trixie); gcc already present for link |

Probe used bison grammar compilation
(`bison -o hello.c HELLO.Y` then `gcc -o hello hello.c` /
`bison -y HELLO.Y && gcc -o hello y.tab.c`)
on a minimal yacc input with `main` printing the probe string.
Identify fossils use `*.y`. Prefer `yacc` / `bison` /
`gnu-bison` / `.y`. Bare `yacc` and `bison` are **allowed** as route
tags because they are tool binary names (unlike English `scheme` /
`basic` collisions, and unlike refused bare `make` factory collision).
Do not claim a full POSIX Yacc / Berkeley Yacc / Bison++ suite
recovery from a GNU Bison compile-link print probe alone — this leaf
pins GNU Bison (yacc-compatible generator).

## Commands (VERIFIED)

```text
$ dpkg -l bison | awk '/^ii/ {print $2, $3}'
bison 2:3.8.2+dfsg-1+b2

$ bison --version | head -1
bison (GNU Bison) 3.8.2

$ ls -la /usr/bin/yacc
lrwxrwxrwx 1 root root 22 Oct 16  2024 /usr/bin/yacc -> /etc/alternatives/yacc

$ cd evals/fixtures/lost-yacc
$ bison -o hello.c HELLO.Y && gcc -o hello hello.c && ./hello
EMPEROR-TIME-YACC-PROBE-OK
# exit 0

$ bison -y HELLO.Y && gcc -o hello y.tab.c && ./hello
EMPEROR-TIME-YACC-PROBE-OK
# exit 0
```

Note: bison(1) SYNOPSIS is `bison [OPTION]... FILE`. With a FILE
argument bison reads the yacc grammar and writes the parser using the
input prefix (or to `-o` / `--output`). Documented VERIFIED
forms are **`bison -o hello.c HELLO.Y`** then compile/link with gcc,
and **`bison -y HELLO.Y`** → `y.tab.c` (POSIX yacc-compatible output
name). Uppercase `.Y` alone without `-o` / `-y` may emit `HELLO.tab.C`
(extension-case follow), which gcc rejects as a C source name — use
`-o` or `-y` for a portable probe. The fixture `main` prints the probe
string; the grammar is an empty `input` rule so the leaf pins generator
invocation, not a parse jury.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is yacc fossil named `HELLO.Y` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-yacc` prints `1 *.y` |
| Compiles under GNU Bison 3.8.2 file input | VERIFIED | `bison -o hello.c HELLO.Y` / `bison -y HELLO.Y` exit 0 |
| Links and prints known string | VERIFIED | `./hello` stdout contains `EMPEROR-TIME-YACC-PROBE-OK` |
| Dialect is a specific POSIX Yacc / Berkeley Yacc claim | CONJECTURE | No other yacc jury beyond GNU Bison compile of this input |
| Would run under period AT&T yacc on original media | UNVERIFIABLE here | No period AT&T yacc ROM run in this session |
| Full Bison GLR / IELR / midrule / %define suite | UNVERIFIABLE here | single compile-link print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Bison Texinfo manual beyond
  SYNOPSIS FILE arguments + Output Files `-o` / `--output` (deferred; pin is
  **bison FILE** — see `references/archaeology-yacc-manual.md`).
- Bare `yacc` / `bison` allowed (tool binary names).
- No `*.yy` / `*.ypp` / `*.gnu-bison` fossil this leaf (`.y` only).
