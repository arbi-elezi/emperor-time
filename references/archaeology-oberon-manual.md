# Jail pin — Vishap Oberon Compiling Main module (HELLO.OBN)

Contemporaneous manual pin for the lost-Oberon archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Oberon
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-obn/HELLO.OBN` with
runnable dialect **VERIFIED** as Vishap Oberon Compiler (voc) 2.1.0
(`voc -M HELLO.OBN` then `./Hello`). Filename culture (`.OBN` / 8.3 caps
→ Oberon *naming*) remains **CONJECTURE** only. Identify fossils use
`*.obn` only (not `*.mod` / `*.Mod` — Modula-2 leaf). This note supplies
the Jail pin so excavate can name the **verified** Vishap Compiling
Main module shape without inventing a full Wirth Oberon-2 Report claim
for a `voc` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Vishap Oberon* — Compiling (doc/Compiling.md) |
| **Heading** | **Main module** — `voc` options `-m` / `-M` designate the main module and generate a loadable binary |
| **Dialect pinned** | **Oberon-2 via Vishap voc C backend** with Oakwood `Out.String` / `Out.Ln` — **not** ETH Oberon System Texts.Writer / Oberon.Log, **not** full Oakwood Guidelines claim |
| **URL** | https://github.com/vishapoberon/compiler/blob/master/doc/Compiling.md |
| **Anchors** | Main module — `-m` dynamic / `-M` static main binary |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Vishap Compiling.md — Main module)

> ### Main module
>
> The main module should be the last module compiled as it imports all
> other modules.
>
> The program logic should be started from the main module's
> initialisation code.
>
> The following options designate the main module:
>
> | Compiler option | Use |
> | :-: | --- |
> | `-m` | Generate loadable binary using dynamic library loading |
> | `-M` | Generate loadable binary with all library references statically linked |

(Vishap Compiling.md documents the invoke surface used by probe
`voc -M HELLO.OBN`. Oakwood `Out` matches the probe program and the
sister ReadMe.md Hello application. Fixture keeps `.OBN` 8.3 caps for
sister-fixture culture; `voc` accepts `.obn` / `.OBN` / `.Mod` source
names, but identify fossils pin `*.obn` only to avoid Modula-2
collision.)

### Why this heading (HELLO.OBN / excavate)

A minimal HELLO surface looks like:

```oberon
MODULE Hello;
  IMPORT Out;
BEGIN
  Out.String("EMPEROR-TIME-OBN-PROBE-OK");
  Out.Ln
END Hello.
```

in a `.OBN` / `.obn` file. That is exactly the pinned form:
`voc` **compiles the named main module to a loadable binary** (`-M`
static), observe `Out.String` output at run time. Pinning Main module
lets excavate treat voc + `.obn` + `Out` as **era evidence** (Oberon-2
compiler / source file) without rewriting the fixture into Oberon.Log,
Texts.Writer, or a Python port.

**Dialect precision:** this pin authorizes Vishap voc reading of the
`Out.String` / `MODULE` / main-module `-M` shape only. It does **not**
claim the lost tree is ETH Native Oberon, a specific printing of the
Wirth Oberon-2 Report, or a period Oakwood tape checkout. Those are
other manuals. HELLO's "Oberon-2-ish / Out subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — `voc`
accepting the `Out` shape and the binary printing the probe string is
the VERIFIED claim for this leaf.
