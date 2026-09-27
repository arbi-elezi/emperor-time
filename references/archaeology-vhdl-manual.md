# Jail pin — VHDL entity top unit + analyze/elaborate/run (HELLO.VHD)

Contemporaneous manual pin for the lost-VHDL archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how VHDL
works” stays **CONJECTURE** until an analyze/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-vhd/HELLO.VHD` with
runnable dialect **VERIFIED** as GHDL 5.0.1 mcode
(`ghdl -a` / `ghdl -e` / `ghdl -r`). Filename culture (`.VHD` / 8.3 caps →
VHDL *naming*) remains **CONJECTURE** only. This note supplies the Jail pin so
excavate can name the **verified** analyze→elaborate→run shape without inventing
a ModelSim/Vivado vendor manual for a ghdl Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GHDL* documentation — **Invoking GHDL** (matches probe toolchain family) |
| **Heading** | **Analysis [`-a`]** / **Elaboration [`-e`]** / **Run [`-r`]** — entity as top unit; mcode elaborates then simulates in memory |
| **Dialect pinned** | **GHDL** entity/architecture program unit with `report` — **not** ModelSim, **not** Vivado, **not** synthesis/`std_logic`, **not** a specific IEEE 1076 year claim |
| **URL** | https://ghdl.github.io/ghdl/using/InvokingGHDL.html |
| **Anchors** | `#analysis-a` / `#elaboration-e` / `#run-r` |
| **Access date** | 2026-09-27 |

### Quote (from Invoking GHDL — Analysis / Elaboration / Run)

> **Analysis [`-a`]**
> `-a [options...] file...`
>
> Analyzes/compiles one or more files, and creates an object file for each
> source file. … GHDL analyzes each filename in the given order, and stops
> the analysis in case of error (remaining files are not analyzed).
>
> **Elaboration [`-e`]**
> `-e [options...] [library.]top_unit [arch]`
>
> … The elaboration command, `-e`, must be followed by a `top_unit` name
> denoting either of: a configuration unit; an entity unit; an entity unit
> followed by a secondary unit (the name of an architecture unit). …
> If mcode is used, this command elaborates the design but does not generate
> anything. Since the run command also elaborates the design, this can be
> skipped.
>
> **Run [`-r`]**
> `-r [options...] [library.]top_unit [arch] [simulation_options...]`
>
> Runs/simulates a design. … mcode: the design is elaborated and the
> simulation is launched.

(Guide documents the GHDL invoke surface used by probe `ghdl` 5.0.1 mcode.)

### Why this heading (HELLO.VHD / excavate)

A minimal HELLO surface looks like:

```vhdl
entity hello is
end entity hello;

architecture behav of hello is
begin
  process is
  begin
    report "…";
    wait;
  end process;
end architecture behav;
```

in a `.VHD` / `.vhd` file. That is exactly the pinned form: analyze the file,
elaborate/run the **entity** top unit, observe `report` at simulation time.
Pinning Analysis/Elaboration/Run lets excavate treat entity+architecture +
`ghdl -a/-e/-r` as **era evidence** (VHDL design-unit split) without rewriting
the fixture into `std_logic`, synthesis attributes, or a Python port.

**Dialect precision:** this pin authorizes GHDL reading of the entity /
architecture / `report` shape only. It does **not** claim the lost tree is
IEEE Std 1076-1993/2008/2019 verbatim, ModelSim, or Vivado. Those are other
manuals. HELLO’s “VHDL-ish / IEEE 1076 family” label remains **CONJECTURE**
until a dialect-specific vendor run is evidence — `ghdl -r` accepting the
subset is a modern open-source probe, not an IEEE jury pin.

### How it informs excavate without modernizing

1. Match the artifact’s extension + first tokens to the pinned production
   (`.vhd`/`.VHD`/`.vhdl` → VHDL design units; `entity` … `architecture`).
2. Prefer a period-era simulator or a GHDL analyze/run that preserves the
   same surface — do not invent `std_logic`, clocks, or synthesis absent from
   the source.
3. Record any dialect leap (e.g. ghdl vs ModelSim vs Vivado vs IEEE year)
   as **CONJECTURE** or **VERIFIED** with a quoted run, separate from this pin.

---

## Corroboration (not the pin)

GHDL implements a large subset of IEEE Std 1076 (VHDL). That corroborates the
VHDL-ish claim against the **verified** toolchain; do not upgrade the claim to
“IEEE 1076-xxxx VERIFIED” without a quoted clause from a fetched IEEE PDF.
