# Jail pin — Ada procedure body + gnatmake (HELLO.ADB)

Contemporaneous manual pin for the lost-Ada archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Ada
works” stays **CONJECTURE** until a compile/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-ada/HELLO.ADB` with
runnable dialect **VERIFIED** as GNATMAKE 13.3.0
(`gnatmake HELLO.ADB` → `./HELLO`). Filename culture (`.ADB` / 8.3 caps →
Ada *naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** compile→bind→link shape without inventing
an ObjectAda/Janus vendor manual for a gnatmake Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNAT User's Guide for Native Platforms* — **Building Executable Programs with GNAT** (matches probe toolchain family) |
| **Heading** | **Building with gnatmake** / **Running gnatmake** — main program file as required argument; standard `.adb` / `.ads` extensions |
| **Dialect pinned** | **GNAT** library-level procedure body with `Ada.Text_IO` — **not** ObjectAda, **not** Janus/Ada, **not** a specific ISO/IEC 8652 year claim |
| **URL** | https://docs.adacore.com/gnat_ugn-docs/html/gnat_ugn/gnat_ugn/building_executable_programs_with_gnat.html |
| **Anchors** | `#building-with-gnatmake` / `#running-gnatmake` / `#examples-of-gnatmake-usage` |
| **Access date** | 2026-09-27 |

### Quote (from Building with gnatmake — Running gnatmake / Examples)

> **Running gnatmake**
>
> The usual form of the `gnatmake` command is
>
> `$ gnatmake [<switches>] <file_name> [<file_names>] [<mode_switches>]`
>
> The only required argument is one `file_name`, which specifies a compilation
> unit that is a main program. … If you are using standard file extensions
> (`.adb` and `.ads`), then the extension may be omitted from the `file_name`
> arguments.
>
> **Examples of gnatmake Usage**
>
> `gnatmake hello.adb`
> Compile all files necessary to bind and link the main program `hello.adb`
> (containing unit `Hello`) and bind and link the resulting object files to
> generate an executable file `hello`.

(Guide documents the GNAT invoke surface used by probe `gnatmake` 13.3.0.)

### Why this heading (HELLO.ADB / excavate)

A minimal HELLO surface looks like:

```ada
with Ada.Text_IO;
procedure Hello is
begin
   Ada.Text_IO.Put_Line ("…");
end Hello;
```

in a `.ADB` / `.adb` file. That is exactly the pinned form: `gnatmake` the
**procedure body** main unit, observe `Put_Line` at run time. Pinning
Building with gnatmake lets excavate treat procedure body + `gnatmake` as
**era evidence** (Ada compilation-unit / body file split) without rewriting
the fixture into packages, tasking, or a Python port.

**Dialect precision:** this pin authorizes GNAT reading of the procedure /
`Ada.Text_IO` / `.adb` shape only. It does **not** claim the lost tree is
ISO/IEC 8652:1995/2005/2012/2022 verbatim, ObjectAda, or Janus. Those are other
manuals. HELLO’s “Ada-ish / ISO 8652 family” label remains **CONJECTURE**
until a dialect-specific vendor run is evidence — `gnatmake` accepting the
subset is a modern open-source probe, not an ISO jury pin.

### How it informs excavate without modernizing

1. Match the artifact’s extension + first tokens to the pinned production
   (`.adb`/`.ADB`/`.ads`/`.ada` → Ada compilation units; `procedure` / `package body`).
2. Prefer a period-era Ada compiler or a GNAT gnatmake that preserves the
   same surface — do not invent packages, tasking, or generics absent from
   the source.
3. Record any dialect leap (e.g. gnat vs ObjectAda vs Janus vs ISO year)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

GNAT implements a large subset of ISO/IEC 8652 (Ada). That corroborates the
Ada-ish claim against the **verified** toolchain; do not upgrade the claim to
“ISO 8652-xxxx VERIFIED” without a quoted clause from a fetched ISO PDF.
