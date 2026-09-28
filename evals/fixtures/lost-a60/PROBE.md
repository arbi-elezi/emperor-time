# Boot probe — lost-a60 / HELLO.A60

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~02:18 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | GNU MARST **2.8** (built from https://ftpmirror.gnu.org/marst/marst-2.8.tar.gz) |
| Binary | `/usr/local/bin/marst` |
| Reported | `MARST--Algol-to-C Translator, Version 2.8` (`marst -v`) |
| Install | `./configure --prefix=/usr/local && make && sudo make install` on this box |

Probe used `marst` (GNU MARST 2.8) to translate an ALGOL 60 program with
ALGLIB `outstring` to C, then `gcc … -lalgol -lm` to link and run. Identify
fossils use `*.a60` (not `*.alg` — that fossil is already claimed by the
Algol 68 leaf). Prefer `marst` / `algol60` / `.a60` / space-intent `algol 60`;
bare English token `outstring` alone is **refused** as a route tag. Do not
commit generated `.c` or linked binaries from the probe.

## Commands (VERIFIED)

Working directory for run: fixture dir (or any dir with the source).

```text
$ marst -v 2>&1 | sed -n '/MARST--/p'
MARST--Algol-to-C Translator, Version 2.8

$ marst HELLO.A60 -o HELLO.c
# exit 0

$ gcc HELLO.c -lalgol -lm -o HELLO
# exit 0

$ ./HELLO
EMPEROR-TIME-A60-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is ALGOL 60 fossil named `HELLO.A60` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-a60` prints `1 *.a60` |
| Translates under marst 2.8 | VERIFIED | `marst HELLO.A60 -o HELLO.c` exit 0 |
| Links and prints known string | VERIFIED | `gcc … -lalgol -lm` then stdout is `EMPEROR-TIME-A60-PROBE-OK` |
| Dialect is a specific IFIP Modified Report year / full Level-0 claim beyond outstring | CONJECTURE | No IFIP jury; MARST subset `outstring` program only |
| Would run under period ALGOL 60 (ALGOL 60R / Elliott / Burroughs) on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Modified Report procedure set
  (deferred; pin is GNU MARST Usage Example `outstring` —
  see `references/archaeology-algol60-manual.md`).
- No Algol 68 / Algol W claim (different language family; Algol 68 is a
  separate leaf at `lost-a68`).
- No claim on `*.alg` fossil naming for this leaf (shared Algol-family
  culture; identify fossil for ALGOL 60 here is `*.a60` only).
