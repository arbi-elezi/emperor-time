# Jail pin — Forth source include + pforth (HELLO.FS)

Contemporaneous manual pin for the lost-Forth archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Forth
works” stays **CONJECTURE** until an include/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-fs/HELLO.FS` with
runnable dialect **VERIFIED** as pForth V2.0.0
(`pforth -q HELLO.FS`). Filename culture (`.FS` / 8.3 caps → Forth
*naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** include→interpret shape without inventing
a Gforth/SwiftForth vendor manual for a pForth Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *pForth README* — **How to Run pForth** (matches probe toolchain family) |
| **Heading** | **How to Run pForth** — `INCLUDE filename` and `pforth myprogram.fth` auto-include |
| **Dialect pinned** | **pForth** ANS-like source file with `."` / `CR` — **not** Gforth, **not** SwiftForth, **not** a specific Forth-2012 year claim |
| **URL** | https://github.com/philburk/pforth/blob/master/README.md |
| **Anchors** | heading `How to Run pForth` (INCLUDE / `pforth myprogram.fth`) |
| **Access date** | 2026-09-28 |

### Quote (from How to Run pForth)

> To compile source code files use:
>
>     INCLUDE filename
>
> …
>
> To run PForth and automatically include a forth file:
>     pforth myprogram.fth

(README documents the pForth invoke surface used by probe `pforth` 2.0.0 /
Debian `pforth` 1:2.0.1-1.)

### Why this heading (HELLO.FS / excavate)

A minimal HELLO surface looks like:

```forth
." EMPEROR-TIME-FORTH-PROBE-OK" CR
```

in a `.FS` / `.fs` / `.fth` file. That is exactly the pinned form: `pforth`
**auto-includes** the source file (or `INCLUDE` from the outer interpreter),
observe `."` output at run time. Pinning How to Run lets excavate treat
dot-quote + include as **era evidence** (Forth outer interpreter / source
file) without rewriting the fixture into CREATE/DOES>, vocabularies, or a
Python port.

**Dialect precision:** this pin authorizes pForth reading of the `."` /
`CR` / `.fs` shape only. It does **not** claim the lost tree is
Forth-2012 / ANS Forth verbatim, Gforth, or SwiftForth. Those are other
manuals. HELLO’s “Forth-ish / ANS family” label remains **CONJECTURE**
until a dialect-specific vendor run is evidence — `pforth` accepting the
subset is a modern portable probe, not a Forth-2012 jury pin.

### How it informs excavate without modernizing

1. Match the artifact’s extension + first tokens to the pinned production
   (`.fs`/`.FS`/`.fth`/`.4th` → Forth source; `."` / `:` / `CR`).
2. Prefer a period-era Forth or a pForth/Gforth that preserves the
   same surface — do not invent vocabularies, blocks, or CREATE/DOES>
   absent from the source.
3. Record any dialect leap (e.g. pForth vs Gforth vs FIG vs Forth-2012)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

pForth is based on ANSI-Forth but is not 100% compatible
(https://forth-standard.org/standard/words). That corroborates the
Forth-ish claim against the **verified** toolchain; do not upgrade the claim
to “Forth-2012 VERIFIED” without a quoted clause from a fetched standard PDF.
