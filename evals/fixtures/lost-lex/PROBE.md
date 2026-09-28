# Boot probe — lost-lex / HELLO.L

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~07:28 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **flex** 2.6.4-8.2+b4 (Debian package; The Flex Project) |
| Binary | `/usr/bin/flex` (GNU flex); `/usr/bin/lex` → `flex` |
| Reported | `flex 2.6.4` |
| Install | `apt-get install flex` (Debian trixie); gcc already present for link |

Probe used flex file compilation
(`flex HELLO.L` → `lex.yy.c`, then `gcc -o hello lex.yy.c -lfl` /
`flex -o hello.c HELLO.L && gcc -o hello hello.c -lfl`)
on a minimal lex input with `main` printing the probe string.
Identify fossils use `*.l` and `*.lex`. Prefer `lex` / `flex` /
`gnu-flex` / `.lex`. Bare `lex` and `flex` are **allowed** as route
tags because they are tool binary names (unlike English `scheme` /
`basic` collisions, and unlike refused bare `make` factory collision).
Bare `.l` alone is **refused** as a route tag (short-extension
collision class — `.l` matches `.lisp` / `.lsp` substrings). Do not
claim a full AT&T lex / POSIX lex / Flex++ suite recovery from a GNU
flex compile-link print probe alone — this leaf pins GNU flex
(lex-compatible generator).

## Commands (VERIFIED)

```text
$ dpkg -l flex | awk '/^ii/ {print $2, $3}'
flex 2.6.4-8.2+b4

$ flex --version
flex 2.6.4

$ ls -la /usr/bin/lex
lrwxrwxrwx 1 root root 4 Jan  4  2025 /usr/bin/lex -> flex

$ cd evals/fixtures/lost-lex
$ flex HELLO.L
$ gcc -o hello lex.yy.c -lfl
$ ./hello
EMPEROR-TIME-LEX-PROBE-OK
# exit 0

$ flex -o hello.c HELLO.L && gcc -o hello hello.c -lfl && ./hello
EMPEROR-TIME-LEX-PROBE-OK
# exit 0
```

Note: flex(1) SYNOPSIS is `flex [OPTIONS] [FILE]...`. With a FILE
argument flex reads the lex input and writes the scanner to
`lex.yy.c` by default (or to `-o` / `--outfile`). Documented VERIFIED
forms are **`flex HELLO.L`** then compile/link with gcc + `-lfl`, and
**`flex -o hello.c HELLO.L`**. The fixture `main` prints the probe
string; rules are a no-op `.|\n` ignore so the leaf pins generator
invocation, not a token-scan jury.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is lex fossil named `HELLO.L` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-lex` prints `1 *.l` |
| Compiles under GNU flex 2.6.4 file input | VERIFIED | `flex HELLO.L` / `flex -o hello.c HELLO.L` exit 0 |
| Links and prints known string | VERIFIED | `./hello` stdout contains `EMPEROR-TIME-LEX-PROBE-OK` |
| Dialect is a specific AT&T lex / POSIX lex claim | CONJECTURE | No other lex jury beyond GNU flex compile of this input |
| Would run under period AT&T lex on original media | UNVERIFIABLE here | No period AT&T lex ROM run in this session |
| Full Flex scanner / start-condition / yylineno suite | UNVERIFIABLE here | single compile-link print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Flex Texinfo manual beyond
  SYNOPSIS FILE arguments + FILES `-o` / `--outfile` (deferred; pin is
  **flex FILE** — see `references/archaeology-lex-manual.md`).
- Bare `lex` / `flex` allowed (tool binary names); bare `.l` refused
  (short-extension collision with `.lisp`).
- No `*.gnu-flex` fossil this leaf (`.l` / `.lex` only).
