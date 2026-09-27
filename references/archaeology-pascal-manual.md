# Jail pin — Pascal program heading (HELLO.PAS)

Contemporaneous manual pin for the lost-Pascal archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Pascal
works” stays **CONJECTURE** until a compiler/emulator run is ledgered.

**Related work:** open PR [#9](https://github.com/arbi-elezi/emperor-time/pull/9)
(`et-manager/archaeology-pas-probe`) adds `evals/fixtures/lost-pas/HELLO.PAS`
with dialect **CONJECTURE** ISO-ish / Turbo-adjacent and a Free Pascal boot
probe. This note does **not** depend on those paths; it only supplies the
Jail pin so excavate can name the era without modernizing the source.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | ISO/IEC 7185:1990 — *Information technology — Programming languages — Pascal* |
| **Heading** | **6.10 Programs** (program-heading) |
| **Dialect pinned** | **ISO 7185** (unextended / Standard Pascal) — **not** UCSD, **not** Turbo 7, **not** Delphi, **not** Free Pascal dialect extensions |
| **URL** | https://www.standardpascal.org/iso7185.pdf |
| **Mirror** | https://archive.org/details/iso-iec-7185-1990-Pascal (PDF: `iso-iec-7185-1990-Pascal.pdf`) |
| **Access date** | 2026-09-27 |

### Quote (from §6.10)

> **6.10 Programs**
>
> `program = program-heading ';' program-block '.' .`
>
> `program-heading = 'program' identifier [ '(' program-parameter-list ')' ] .`
>
> The identifier of the program-heading shall be the program name. It shall
> have no significance within the program.

(Also in the same clause: `program-parameter-list` is optional in the heading
syntax — square brackets in the production.)

### Why this heading (HELLO.PAS / excavate)

A minimal HELLO surface looks like:

```pascal
program Hello;
begin
  writeln('...')
end.
```

That is exactly the ISO 7185 program form: `program` + identifier, **no**
required `(input, output)` list in the production, then a block closed by
`end.`. Pinning §6.10 lets excavate treat `program` / `begin` / `end.` as
**era evidence** (Standard Pascal structure) without rewriting the fixture into
modern Free Pascal units, Delphi forms, or a Python port.

**Dialect precision:** this pin authorizes ISO-7185 reading of the heading and
block shape only. It does **not** claim the lost tree is UCSD p-System, Turbo
Pascal 5.5/7, Delphi Object Pascal, or FPC’s default Delphi mode. Those are
other manuals. HELLO’s “ISO-ish / Turbo-adjacent” label in PR #9 remains
**CONJECTURE** until `tpc` / a DOS emulator (or another dialect-specific run)
is evidence — `fpc -Miso` accepting the subset is a modern probe, not the pin.

### How it informs excavate without modernizing

1. Match the artifact’s first tokens to the pinned production (`program`
   identifier `;` … `end.`).
2. Prefer a period-era toolchain or an ISO-mode compile that preserves the
   same surface — do not invent `uses`, `{$…}`, units, or classes absent from
   the source.
3. Record any dialect leap (e.g. FPC default vs `-Miso` vs classic `tpc`) as
   **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

Contemporaneous Turbo Pascal agrees that the heading is optional / lightly
bound — useful for the “Turbo-adjacent” side of the CONJECTURE, but **ISO
§6.10 remains the Jail pin** (one heading).

| Field | Value |
|-------|--------|
| **Manual** | Borland *TURBO Pascal Version 3.0 Reference Manual* (1986) |
| **Heading** | Chapter 5 — **PROGRAM HEADING AND PROGRAM BLOCK** / **Program Heading** |
| **URL** | https://bitsavers.org/pdf/borland/turbo_pascal/Turbo_Pascal_Version_3.0_Reference_Manual_1986.pdf |
| **Access date** | 2026-09-27 |

> In TURBO Pascal, the program heading is purely optional and of no
> significance to the program. If present, it gives the program a name, and
> optionally lists the parameters through which the program communicates with
> the environment.

Examples in that section include `program Circles;` — same bare heading shape
as HELLO.

A 2026 blog post about Pascal is **secondary** and must not replace either of
the URLs above.
