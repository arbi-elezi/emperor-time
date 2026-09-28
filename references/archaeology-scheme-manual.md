# Jail pin — CHICKEN csi script invocation (HELLO.SCM)

Contemporaneous manual pin for the lost-Scheme archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Scheme
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-scm/HELLO.SCM` with
runnable dialect **VERIFIED** as CHICKEN Scheme 5.3.0
under Linux x86_64
(`csi -s HELLO.SCM` →
`EMPEROR-TIME-SCM-PROBE-OK`). Filename culture
(`.SCM` / 8.3 caps → Scheme *naming*) remains **CONJECTURE** only.
Identify fossils use `*.scm` only. Bare English `scheme` is refused as a
route tag (common-English collision). This note supplies the Jail pin so excavate
can name the **verified** csi `-s` / `-script` file-invocation shape
without inventing a full Racket / Guile / Chez / MIT Scheme / R7RS
claim for a display probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *CHICKEN User's Manual* — Using the interpreter / csi command line format |
| **Heading** | **csi command line format** — `-s` / `-script PATHNAME` |
| **Dialect pinned** | **Scheme via CHICKEN csi** with `display` / `newline` surface — **not** full Racket / Guile / Chez / MIT Scheme / R7RS claim |
| **URL** | https://wiki.call-cc.org/man/5/Using%20the%20interpreter (Using the interpreter — csi command line format / `-s -script PATHNAME`); package `chicken-bin` 5.3.0-2 on Debian trixie |
| **Anchors** | `-s -script PATHNAME` — equivalent to `-batch -quiet -no-init PATHNAME` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from CHICKEN User's Manual — Using the interpreter / csi command line format)

> `-s -script PATHNAME`
>
> This is equivalent to `-batch -quiet -no-init PATHNAME`. Arguments
> following `PATHNAME` are available by using `command-line-arguments`
> and are not processed as interpreter options.

(Source: CHICKEN User's Manual — Using the interpreter, wiki.call-cc.org
https://wiki.call-cc.org/man/5/Using%20the%20interpreter , accessed
2026-09-28 Europe/Tirane. Probe uses
`csi -s HELLO.SCM` so the interpreter
loads and evaluates the named source non-interactively.
`display` + `newline` prints the probe string and exits.)

### Why this heading (HELLO.SCM / excavate)

A minimal HELLO surface looks like:

```scheme
(display "EMPEROR-TIME-SCM-PROBE-OK")
(newline)
```

in a `.SCM` / `.scm` file. That is exactly the pinned form:
**`csi -s`** loads and evaluates the named source file, observe
`display` at run time. Pinning csi script / `-s` / `-script`
lets excavate treat `csi` / `chicken` / `chicken-scheme` / `.scm` + `display` /
`newline` as **era evidence** (CHICKEN / Scheme source
file) without rewriting the fixture into a Racket module,
a Guile script, or a Python port.

**Dialect precision:** this pin authorizes CHICKEN csi reading of
the `display` / `newline` / script-invocation shape only. It does
**not** claim the lost tree is Racket, Guile, Chez Scheme, MIT Scheme,
Scheme48, or a working R7RS suite on this host. Those are other manuals /
toolchains. HELLO's "CHICKEN-ish / display subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — csi
accepting the `display` shape and printing the probe string is the
VERIFIED claim for this leaf.
