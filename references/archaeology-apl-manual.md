# Jail pin — GNU APL SYNOPSIS (HELLO.APL)

Contemporaneous manual pin for the lost-APL archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how APL
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-apl/HELLO.APL` with
runnable dialect **VERIFIED** as GNU APL 2.0 (source build,
`--with-optional_libs=no`) under Linux x86_64
(`apl -s --OFF -f HELLO.APL` → `EMPEROR-TIME-APL-PROBE-OK`).
Filename culture (`.APL` / 8.3 caps → APL *naming*) remains
**CONJECTURE** only. Identify fossils use `*.apl` only. This note
supplies the Jail pin so excavate can name the **verified** GNU APL
SYNOPSIS / `-f file` shape without inventing a full ISO 13751 Extended
nested-array claim for a print probe. The prebuilt
`apl_2.0-1_amd64.deb` needs `libgsl.so.27` (trixie has `libgsl28`) —
**not** the VERIFIED toolchain for this leaf.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU APL* — `apl(1)` man page (distributed with GNU APL 2.0; man date 2014 July 28) |
| **Heading** | **SYNOPSIS** — `apl [options]` (and OPTIONS `-f file` — read APL input from file) |
| **Dialect pinned** | **APL via GNU APL** with `⎕←` print surface — **not** full ISO 13751 nested-array / ⎕SQL / ⎕FFT claim, **not** prebuilt deb VERIFIED on this host |
| **URL** | https://www.gnu.org/software/apl/ (project); man page from https://mirrors.kernel.org/gnu/apl/apl-2.0.tar.gz (`doc/apl.1`) |
| **Anchors** | SYNOPSIS — `apl [options]`; OPTIONS `-f file` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU APL `apl(1)` — SYNOPSIS / OPTIONS `-f`)

> **SYNOPSIS**
> `apl` [options]
>
> **`-f file`**
> read input from *file* rather than from the keyboard. When the end of
> the file is reached, input is switched back to the keyboard.
> If you want to terminate the APL interpreter after executing the file,
> then use )OFF as last line in the file.

(Probe uses the scripting shortcut `-s --OFF -f HELLO.APL`, which
combines `--silent --noCIN --noCONT --noColor` with automatic `)OFF`
after the input file. Fixture keeps `.APL` 8.3 caps for sister-fixture
culture.)

### Why this heading (HELLO.APL / excavate)

A minimal HELLO surface looks like:

```apl
⎕←'EMPEROR-TIME-APL-PROBE-OK'
```

in a `.APL` / `.apl` file. That is exactly the pinned form:
`apl -f` **reads the named APL source file** after options, observe
`⎕←` at run time. Pinning SYNOPSIS / `-f file` lets excavate treat
`apl` / `gnu-apl` / `.apl` + `⎕←` as **era evidence** (APL interpreter /
source file) without rewriting the fixture into nested arrays, tradfn
workspaces, or a Python port.

**Dialect precision:** this pin authorizes GNU APL reading of the
`⎕←` / command-line `-f file` shape only. It does **not** claim the
lost tree is period IBM APL\360 / APL2 on original media, a specific
printing of ISO 13751, or a working prebuilt Debian `apl` deb on this
host. Those are other manuals / toolchains. HELLO's "ISO-13751-ish /
quad-assign subset" label remains **CONJECTURE** until a dialect-specific
vendor run is evidence — GNU APL accepting the `⎕←` shape and printing
the probe string is the VERIFIED claim for this leaf.
