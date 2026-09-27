# Jail pin — Common Lisp batch lisp-file + clisp (HELLO.LISP)

Contemporaneous manual pin for the lost-Lisp archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Lisp
works” stays **CONJECTURE** until a load/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-lisp/HELLO.LISP` with
runnable dialect **VERIFIED** as GNU CLISP 2.49.95+
(`clisp -q -norc HELLO.LISP`). Filename culture (`.LISP` / 8.3 caps → Lisp
*naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** batch lisp-file shape without inventing
an SBCL/CCL vendor manual for a CLISP Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU CLISP Manual Page / Implementation Notes* — **clisp** (matches probe toolchain family) |
| **Heading** | **Non-Interactive (Batch) Mode** — Invoked with `_lisp-file_`, runs the specified lisp file |
| **Dialect pinned** | **GNU CLISP** ANSI-ish source file with `FORMAT` / `T` / `~%` — **not** SBCL, **not** CCL, **not** a specific ANSI CL year claim |
| **URL** | https://clisp.sourceforge.io/impnotes/clisp.html |
| **Anchors** | heading `Non-Interactive (Batch) Mode` (`-x` expressions / `_lisp-file_` batch run) |
| **Access date** | 2026-09-28 |

### Quote (from Non-Interactive (Batch) Mode)

> Invoked with `-c`, compiles the specified lisp files to a platform-independent bytecode which can be executed more efficiently.
>
> Invoked with `-x`, executes the specified lisp expressions.
>
> Invoked with `_lisp-file_`, runs the specified lisp file.

(Implementation notes document the CLISP invoke surface used by probe `clisp`
2.49.95+ / Debian `clisp` 1:2.49.20241228.gitc3ec11b-2.)

### Why this heading (HELLO.LISP / excavate)

A minimal HELLO surface looks like:

```lisp
(FORMAT T "EMPEROR-TIME-LISP-PROBE-OK~%")
```

in a `.LISP` / `.lisp` / `.lsp` / `.cl` file. That is exactly the pinned form:
`clisp` **runs the lisp-file** in batch mode (no REPL), observe `FORMAT`
output at run time. Pinning Non-Interactive (Batch) Mode lets excavate treat
FORMAT + batch lisp-file as **era evidence** (Common Lisp interpreter /
source file) without rewriting the fixture into CLOS, packages, or a
Python port.

**Dialect precision:** this pin authorizes CLISP reading of the `FORMAT` /
`T` / `~%` / `.lisp` shape only. It does **not** claim the lost tree is
ANSI Common Lisp verbatim, SBCL, or CCL. Those are other manuals. HELLO’s
“Common-Lisp-ish / ANSI family” label remains **CONJECTURE** until a
dialect-specific vendor run is evidence — `clisp` accepting the
FORMAT/batch shape is the VERIFIED claim for this leaf.
