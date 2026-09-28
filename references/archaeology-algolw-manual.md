# Jail pin — Awe SYNOPSIS / EXAMPLES WRITE (HELLO.ALW)

Contemporaneous manual pin for the lost-Algol-W archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Algol W
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-alw/HELLO.ALW` with
runnable dialect **VERIFIED** as Awe 2026-05
(`awe HELLO.ALW -o HELLO` then `./HELLO`).
Filename culture (`.ALW` / 8.3 caps → Algol W *naming*) remains
**CONJECTURE** only. Identify fossils use `*.alw` (not `*.a60` / `*.a68` /
`*.alg` — other Algol-family leaves). This note supplies the Jail pin so
excavate can name the **verified** Awe SYNOPSIS / EXAMPLES `WRITE` shape
without inventing a full June 1972 Language Description vendor clause for
an `awe` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *awe(1)* — Awe ALGOL W compiler man page / README |
| **Heading** | **SYNOPSIS** / **EXAMPLES** — `awe source.alw... [-o executable]` plus standard I/O `WRITE` |
| **Dialect pinned** | **Awe / June 1972 ALGOL W subset** with standard `WRITE` string output — **not** full Language Description, **not** ALGOL 60 / Algol 68 |
| **URL** | https://github.com/glynawe/awe (awe.1.md SYNOPSIS / EXAMPLES) |
| **Anchors** | SYNOPSIS `awe source.alw... [-o executable]` — EXAMPLES `awe program.alw` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from awe(1) — SYNOPSIS / EXAMPLES)

> **SYNOPSIS**
>
> **awe** *source.alw*... [**flags**] [**-o** *executable* | **-c** *object.c* | **-p** *object.c*]
>
> **EXAMPLES**
>
> ```sh
> awe program.alw
> ```
>
> By default **awe** compiles an executable. The default name of the
> executable is the name of the last ALGOL W source file with its
> extension removed.

(Awe / `awe.1.md` document the invoke surface used by probe
`awe HELLO.ALW -o HELLO`. Standard I/O `WRITE` matches the probe
program. Fixture uses `.ALW` so identify fossils stay distinct from
ALGOL 60 `*.a60` and Algol 68 `*.a68` / `*.alg`.)

### Why this heading (HELLO.ALW / excavate)

A minimal HELLO surface looks like:

```algolw
begin
   write("EMPEROR-TIME-ALW-PROBE-OK")
end.
```

in a `.ALW` / `.alw` file. That is exactly the pinned form:
`awe` **compiles the named source file to an executable**, observe
`WRITE` output at run time. Pinning SYNOPSIS / EXAMPLES lets excavate
treat awe + `WRITE` as **era evidence** (Algol W compiler / source file)
without rewriting the fixture into records, complex arithmetic, or a
Python port.

**Dialect precision:** this pin authorizes Awe reading of the
`WRITE` / `.alw` shape only. It does **not** claim the lost tree is a
specific Stanford / OS/360 printing year, ALGOL 60, Algol 68, or a period
vendor checkout compiler. Those are other manuals. HELLO’s “awe 2026-05-ish /
Algol W subset” label remains **CONJECTURE** until a dialect-specific
vendor run is evidence — `awe` accepting the `WRITE` shape and the
linked binary printing the probe string is the VERIFIED claim for this leaf.
