# Jail pin — Fortran free-form PROGRAM unit (HELLO.F90)

Contemporaneous manual pin for the lost-Fortran archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Fortran
works” stays **CONJECTURE** until a compile/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-f90/HELLO.F90` with
runnable dialect **VERIFIED** as GNU Fortran 14.2 free-form F90-ish
(`gfortran -o`). Filename culture (`.F90` / 8.3 caps → Fortran 90 free-form
*naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** source-form shape without inventing an
Intel/NAG vendor manual for a gfortran Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *The GNU Fortran Compiler* (GCC 14.2.0) — section **2.2 Options controlling Fortran dialect** (matches probe toolchain family) |
| **Heading** | **`-ffree-form` / `-ffixed-form`** — free form introduced in Fortran 90; source form from file extension when neither flag is given |
| **Dialect pinned** | **GNU Fortran** free-form Fortran 90/95-compatible program unit — **not** Intel ifort, **not** NAG, **not** fixed-form columns, **not** OpenMP/coarray |
| **URL** | https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gfortran/Fortran-Dialect-Options.html |
| **Mirror (Standards)** | https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gfortran/Standards.html |
| **Access date** | 2026-09-27 |

### Quote (from §2.2 Options controlling Fortran dialect)

> `-ffree-form`
> `-ffixed-form`
>
> Specify the layout used by the source file. The free form layout was
> introduced in Fortran 90. Fixed form was traditionally used in older
> Fortran programs. When neither option is specified, the source form is
> determined by the file extension.

(Guide documents GCC 14.2 / GNU Fortran 14.x family; probe ran `gfortran` 14.2.0.)

### Why this heading (HELLO.F90 / excavate)

A minimal HELLO surface looks like:

```fortran
PROGRAM HELLO
  WRITE(*,'(A)') '…'
END PROGRAM HELLO
```

in a `.F90` / `.f90` file. That is exactly the pinned form: free-form layout
selected by the `.f90` extension family, `PROGRAM` … `END PROGRAM` unit, no
fixed-form column rules. Pinning §2.2 lets excavate treat free-form + program
unit as **era evidence** (Fortran 90 source-form split) without rewriting the
fixture into fixed-form `.f`, modules, or a Python port.

**Dialect precision:** this pin authorizes GNU Fortran reading of the free-form
shape only. It does **not** claim the lost tree is ISO 1539:1991 verbatim,
Intel ifort, NAG, or DEC/Compaq. Those are other manuals. HELLO’s
“F90-ish / free-form” label remains **CONJECTURE** until a dialect-specific
compiler run is evidence — `gfortran -o` accepting the subset is a modern
open-source probe, not an ISO jury pin.

### How it informs excavate without modernizing

1. Match the artifact’s extension + first tokens to the pinned production
   (`.f90`/`.F90` → free form; `PROGRAM` … `END PROGRAM`).
2. Prefer a period-era toolchain or a free-form compile that preserves the
   same surface — do not invent modules, coarrays, or OpenMP absent from the
   source.
3. Record any dialect leap (e.g. gfortran vs ifort vs NAG vs fixed-form f77)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

GNU Fortran §1.3 Standards states the compiler implements ISO/IEC 1539:1997
(Fortran 95) and can compile essentially all standard-compliant Fortran 90
programs. That corroborates the F90-ish claim against the **verified**
toolchain; do not upgrade the claim to “ISO 1539:1991 VERIFIED” without a
quoted ISO clause from a fetched PDF.
