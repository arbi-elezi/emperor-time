# Jail pin — Classic Rexx SAY (HELLO.REX)

Contemporaneous manual pin for the lost-REXX archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how REXX
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-rex/HELLO.REX` with
runnable dialect **VERIFIED** as Regina 3.9.5
(`rexx HELLO.REX`). Filename culture (`.REX` / 8.3 caps → REXX
*naming*) remains **CONJECTURE** only. Identify fossils use `*.rex` /
`*.rexx`. This note supplies the Jail pin so excavate can name the
**verified** Classic Rexx `SAY` shape without inventing an ooRexx /
ADDRESS host vendor manual for a `rexx` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Classic Rexx Tutorial* — Kilowatt Software (Language Level 4.00 / TRL-2; matches Regina Classic Rexx surface) |
| **Heading** | **Say instruction** — `SAY [expression]` computes the expression and sends the result as a line to the default output stream (often the program console) |
| **Dialect pinned** | **Classic Rexx / Regina 3.9.5** with `SAY` string output — **not** ooRexx, **not** NetRexx, **not** a specific CMS/TSO ADDRESS host claim |
| **URL** | http://manmrk.net/tutorials/rexx/krexx/Say.htm |
| **Anchors** | Say instruction — `SAY [expression]` (default output stream) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Classic Rexx Tutorial — Say instruction)

> The SAY instruction computes the value of its optional expression, and sends the result as a line to the default output stream. Often this will be the program's console. When the expression is absent, the empty string is written.

(Regina 3.9.5 / Debian `regina-rexx` 3.9.5 document the invoke surface used by probe
`rexx HELLO.REX`. Classic Rexx TRL-2 SAY matches the probe.)

### Why this heading (HELLO.REX / excavate)

A minimal HELLO surface looks like:

```rexx
#!/usr/bin/env rexx
/* comment */
SAY "EMPEROR-TIME-REX-PROBE-OK"
```

in a `.REX` / `.rex` / `.rexx` file. That is exactly the pinned form:
`rexx` / `regina` **runs the named script file** non-interactively (no REPL),
observe `SAY` output at run time. Pinning SAY lets excavate treat Regina +
SAY as **era evidence** (REXX interpreter / source file) without rewriting
the fixture into ADDRESS hosts, ooRexx classes, or a Python port.

**Dialect precision:** this pin authorizes Classic Rexx reading of the `SAY` /
`.rex` shape only. It does **not** claim the lost tree is a specific ANSI
year, CMS/TSO host, or ooRexx. Those are other manuals. HELLO’s “Regina
3.9-ish” label remains **CONJECTURE** until a dialect-specific vendor run is
evidence — `rexx` accepting the SAY shape is the VERIFIED claim for
this leaf.
