# Boot probe — lost-obn / HELLO.OBN

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~02:57 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | Vishap Oberon Compiler (**voc**) from https://github.com/vishapoberon/compiler |
| Binary | `/tmp/toolchain-probe/voc/install/bin/voc` (local `make` install image) |
| Reported | `Oberon-2 compiler v2.1.0 [2026/09/28] for gcc LP64 on debian` |
| Install | `git clone https://github.com/vishapoberon/compiler.git && cd compiler && make` then `export PATH="$PWD/install/bin:$PATH"` |

Probe used `voc -M` (static main) on an Oakwood `Out` source with
`Out.String` / `Out.Ln`. Identify fossils use `*.obn` only — **not**
`*.mod` / `*.Mod` (Modula-2 leaf owns those case-insensitively). Prefer
`voc` / `oberon` / `oberon-2` / `oberon2` / `.obn`; bare English token
`module` alone is **refused** as a route tag (MODULE keyword collision
class). Do not commit generated `Hello` binaries or `Hello.c` from the
probe.

## Commands (VERIFIED)

Working directory for compile/run: fixture dir (or any dir with the source).

```text
$ voc
Oberon-2 compiler v2.1.0 [2026/09/28] for gcc LP64 on debian.
Based on Ofront by J. Templ and Software Templ OEG.
Further development by Norayr Chilingarian, David Brown and others.
Loaded from /tmp/toolchain-probe/voc/install/bin

$ voc -M HELLO.OBN
HELLO.OBN  Compiling Hello.  Main program.  393 chars.

$ ./Hello
EMPEROR-TIME-OBN-PROBE-OK
# exit 0
```

(`voc -m` also works but needs `LD_LIBRARY_PATH` to `install/lib` for
`libvoc-O2.so`. Probe documents `-M` static link, which runs without that.)

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Oberon fossil named `HELLO.OBN` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-obn` prints `1 *.obn` |
| Compiles under Vishap Oberon voc 2.1.0 (`voc -M`) | VERIFIED | `voc -M HELLO.OBN` exit 0 |
| Runs and prints known string | VERIFIED | stdout is `EMPEROR-TIME-OBN-PROBE-OK` |
| Dialect is a specific Wirth Oberon Report year / Oakwood full claim beyond Out | CONJECTURE | No Oakwood jury beyond Out.String/Out.Ln; ETH Oberon System not claimed |
| Would run under period ETH Oberon / Native Oberon on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of the full Oakwood Guidelines / Wirth Oberon-2 Report
  (deferred; pin is Vishap Compiling **Main module** — see
  `references/archaeology-oberon-manual.md`).
- No ETH Oberon System / Texts.Writer / Oberon.Log claim (Oakwood Out only).
- No `*.mod` / `*.Mod` fossil for this leaf (collides with lost-mod).
- No bare `module` route tag (MODULE keyword English collision).
