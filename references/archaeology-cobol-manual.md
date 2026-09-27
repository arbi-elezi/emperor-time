# Jail pin — COBOL identification heading (HELLO.CBL)

Contemporaneous manual pin for the lost-COBOL archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how COBOL
works” stays **CONJECTURE** until a compile/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-cbl/HELLO.CBL` with
runnable dialect **VERIFIED** as GnuCOBOL 3.2 fixed-format ANSI-85-ish
(`cobc -x`). Filename culture (`.CBL` / 8.3 caps → late-DOS / IBM-adjacent
*naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** division shape without inventing an IBM
mainframe manual for a GnuCOBOL Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GnuCOBOL Programmer’s Guide* — chapter **4 IDENTIFICATION DIVISION** (matches probe toolchain family) |
| **Heading** | **4 IDENTIFICATION DIVISION** — `PROGRAM-ID` required paragraph |
| **Dialect pinned** | **GnuCOBOL** fixed-format ANSI-85-compatible identification + procedure — **not** IBM Enterprise COBOL, **not** Micro Focus, **not** free-format `-free`, **not** OO COBOL |
| **URL** | https://gnucobol.sourceforge.io/HTML/gnucobpg.html#IDENTIFICATION-DIVISION |
| **Mirror (chapter)** | https://superbol.eu/gnucobol/gnucobpg/chapter4.html |
| **Access date** | 2026-09-27 |

### Quote (from §4 IDENTIFICATION DIVISION)

> While the actual `IDENTIFICATION DIVISION` or `ID DIVISION` header is
> optional, the `PROGRAM-ID` / `FUNCTION-ID` paragraphs are not; only one
> or the other, however, may be coded.
>
> The `PROGRAM-ID` and `FUNCTION-ID` paragraphs serve to identify the
> program to the external (i.e. operating system) environment. If there
> is no `AS` clause present, [the program name] will serve as that
> external identification.

(Guide documents July 2020 / GnuCOBOL 3.x family; probe ran `cobc` 3.2.0.)

### Why this heading (HELLO.CBL / excavate)

A minimal HELLO surface looks like:

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY "…".
           STOP RUN.
```

That is exactly the pinned form: optional-but-present `IDENTIFICATION
DIVISION.`, required `PROGRAM-ID.`, then procedure. Pinning §4 lets excavate
treat `IDENTIFICATION` / `PROGRAM-ID` / `PROCEDURE` as **era evidence**
(standard COBOL division structure) without rewriting the fixture into
free-format, OO classes, or a Python port.

**Dialect precision:** this pin authorizes GnuCOBOL reading of the
identification shape only. It does **not** claim the lost tree is IBM VS
COBOL II, Enterprise COBOL, Micro Focus, or ANS74 with AUTHOR/SECURITY
paragraphs. Those are other manuals. HELLO’s “ANSI-85-ish / IBM-adjacent”
label remains **CONJECTURE** until a dialect-specific compiler run is
evidence — `cobc -x` accepting the subset is a modern open-source probe,
not an IBM pin.

### How it informs excavate without modernizing

1. Match the artifact’s first tokens to the pinned production
   (`IDENTIFICATION DIVISION.` → `PROGRAM-ID.` … → `PROCEDURE DIVISION.`).
2. Prefer a period-era toolchain or a fixed-format compile that preserves
   the same surface — do not invent `SCREEN SECTION`, OO, or `-free` absent
   from the source.
3. Record any dialect leap (e.g. GnuCOBOL vs IBM Enterprise vs Micro Focus)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

ISO/IEC 1989 (COBOL) remains the international standard family; the public
GnuCOBOL guide is the pin because it matches the **verified** toolchain on
this box and quotes the same identification requirement. Do not upgrade the
claim to “ISO 1989 VERIFIED” without a quoted ISO clause from a fetched PDF.
