# Jail pin — Algol 68 Genie Synopsis / Transput print (HELLO.A68)

Contemporaneous manual pin for the lost-Algol-68 archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Algol 68
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-a68/HELLO.A68` with
runnable dialect **VERIFIED** as Algol 68 Genie 3.1.2
(`a68g HELLO.A68`). Filename culture (`.A68` / 8.3 caps → Algol 68
*naming*) remains **CONJECTURE** only. Identify fossils use `*.a68` /
`*.alg`. This note supplies the Jail pin so excavate can name the
**verified** a68g invoke + standard-prelude `print` shape without inventing
a full Revised Report vendor clause for an `a68g` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Algol68G - an Algol 68 interpreter* (Algol 68 Genie docs) |
| **Heading** | **Synopsis and options** — `a68g [option \| file] ...` plus **Transput** standard-prelude `print` / `new line` |
| **Dialect pinned** | **Algol 68 Genie / Revised Report subset** with `print` string output — **not** full RR FORMAT/transput, **not** ALGOL 60 / Algol W |
| **URL** | https://algol68genie.nl/en/blog/algol-68-genie-1/ |
| **Anchors** | Synopsis — `a68g [option \| file] ...`; Transput — `PROC ([] ?SIMPLOUT) VOID write, print` / `new line` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Algol68G — Synopsis and options / Transput)

> From the command-line you would use
>
> - `a68g [option | file] ...`

> `PROC ([] ?SIMPLOUT) VOID write, print`
> `PROC (REF FILE) VOID close, space, new line`

(Algol 68 Genie / Debian `algol68g` 3.1.2 document the invoke surface used by
probe `a68g HELLO.A68`. Standard-prelude `print` + `new line` matches the
probe particular-program.)

### Why this heading (HELLO.A68 / excavate)

A minimal HELLO surface looks like:

```algol68
BEGIN
  print (("EMPEROR-TIME-A68-PROBE-OK", new line))
END
```

in a `.A68` / `.a68` file. That is exactly the pinned form:
`a68g` **interprets the named source file**, observe `print` output at run
time. Pinning Synopsis + Transput `print` lets excavate treat a68g +
`print` as **era evidence** (Algol 68 interpreter / source file) without
rewriting the fixture into FORMAT texts, drawing channels, or a Python port.

**Dialect precision:** this pin authorizes Algol 68 Genie reading of the
`print` / `.a68` shape only. It does **not** claim the lost tree is a
specific Revised Report printing year, ALGOL 60, or a period vendor
checkout compiler. Those are other manuals. HELLO’s “a68g 3.1-ish /
Genie subset” label remains **CONJECTURE** until a dialect-specific vendor
run is evidence — `a68g` accepting the `print` shape is the VERIFIED claim
for this leaf.
