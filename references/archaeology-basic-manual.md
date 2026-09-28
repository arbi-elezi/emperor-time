# Jail pin — Bywater BASIC bwbasic file invocation (HELLO.BAS)

Contemporaneous manual pin for the lost-BASIC archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how BASIC
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-bas/HELLO.BAS` with
runnable dialect **VERIFIED** as Bywater BASIC 2.20 patch level 2
under Linux x86_64
(`bwbasic HELLO.BAS` →
`EMPEROR-TIME-BAS-PROBE-OK`). Filename culture
(`.BAS` / 8.3 caps → BASIC *naming*) remains **CONJECTURE** only.
Identify fossils use `*.bas` only. Bare English `basic` is refused as a
route tag (common-English collision). Bare `print` is refused as a route
tag (cross-dialect keyword). This note supplies the Jail pin so excavate
can name the **verified** bwbasic command-line file-invocation shape
without inventing a full period Microsoft BASICA / GW-BASIC / QuickBASIC /
Visual Basic / BBC BASIC / FreeBASIC claim for a print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *bwbasic(1)* — Debian manpage / Bywater BASIC Interpreter/Shell |
| **Heading** | **4.d. Command-Line Execution** — `bwbasic prog.bas` |
| **Dialect pinned** | **BASIC via Bywater bwbasic** with `PRINT` / `SYSTEM` surface — **not** full Microsoft GW-BASIC / QuickBASIC / Visual Basic / BBC BASIC / FreeBASIC claim |
| **URL** | https://manpages.debian.org/testing/bwbasic/bwbasic.1.en.html (bwbasic(1) §4.d Command-Line Execution); package `bwbasic` 2.20pl2-14 on Debian trixie |
| **Anchors** | 4.d. Command-Line Execution — filename on the command line is LOADed and RUN immediately (`bwbasic prog.bas`) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from bwbasic(1) — 4.d. Command-Line Execution)

> A filename can be specified on the command line and will be
> LOADed and RUN immediately, so that the command line
>
> `bwbasic prog.bas`
>
> will load and execute "prog.bas".

(Source: bwbasic(1) — Bywater BASIC Interpreter/Shell, Debian manpages
https://manpages.debian.org/testing/bwbasic/bwbasic.1.en.html , accessed
2026-09-28 Europe/Tirane. Probe uses
`bwbasic HELLO.BAS` so the interpreter
LOADs and RUNs the named source non-interactively.
`PRINT` + `SYSTEM` prints the probe string and exits.)

### Why this heading (HELLO.BAS / excavate)

A minimal HELLO surface looks like:

```basic
PRINT "EMPEROR-TIME-BAS-PROBE-OK"
SYSTEM
```

in a `.BAS` / `.bas` file. That is exactly the pinned form:
**`bwbasic`** LOADs and RUNs the named source file, observe
`PRINT` at run time. Pinning Command-Line Execution / file
arguments lets excavate treat `bwbasic` / `bywater` / `.bas` + `PRINT` /
`SYSTEM` as **era evidence** (Bywater / BASIC source
file) without rewriting the fixture into a GW-BASIC graphics
program, a QuickBASIC structured module, or a Python port.

**Dialect precision:** this pin authorizes Bywater bwbasic reading of
the `PRINT` / `SYSTEM` / file-invocation shape only. It does
**not** claim the lost tree is period Microsoft BASICA, GW-BASIC,
QuickBASIC, Visual Basic, BBC BASIC, FreeBASIC, or a working ANSI Full
BASIC suite on this host. Those are other manuals / toolchains. HELLO's
"Bywater-ish / PRINT subset" label remains **CONJECTURE** until a
dialect-specific vendor run is evidence — bwbasic accepting the `PRINT`
shape and printing the probe string is the VERIFIED claim for this leaf.
