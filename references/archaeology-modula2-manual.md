# Jail pin — GNU Modula-2 Example compile and link (HELLO.MOD)

Contemporaneous manual pin for the lost-Modula-2 archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Modula-2
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-mod/HELLO.MOD` with
runnable dialect **VERIFIED** as GNU Modula-2 14.2.0
(`gm2 -g -x modula-2 HELLO.MOD`). Filename culture (`.MOD` / 8.3 caps →
Modula-2 *naming*) remains **CONJECTURE** only. Identify fossils use
`*.mod` / `*.def`. This note supplies the Jail pin so excavate can name the
**verified** gm2 Example-usage `WriteString` shape without inventing a
Wirth book clause or ISO 10514-1 vendor manual for a `gm2` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *The GNU Modula-2 Compiler* — GCC online docs (gm2) |
| **Heading** | **2.1 Example compile and link** — `hello.mod` with `FROM StrIO IMPORT WriteString, WriteLn` compiled via `gm2 -g hello.mod` |
| **Dialect pinned** | **GNU Modula-2 / PIM StrIO** with `WriteString` string output — **not** ISO STextIO-only, **not** a specific Wirth / Logitech / TopSpeed vendor claim |
| **URL** | https://gcc.gnu.org/onlinedocs/gm2/Example-usage.html |
| **Anchors** | Example compile and link — `MODULE hello` / `WriteString` / `gm2 -g hello.mod` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from The GNU Modula-2 Compiler — Example compile and link)

> This section describes how to compile and link a simple hello world program. Create a file called `hello.mod` in your current directory which contains:

```modula-2
MODULE hello ;
FROM StrIO IMPORT WriteString, WriteLn ;
BEGIN
   WriteString ('hello world') ; WriteLn
END hello.
```

> You can compile and link it by: `gm2 -g hello.mod`.

(GNU Modula-2 / Debian `gm2` 14.2.0 document the invoke surface used by probe
`gm2 -g -x modula-2 HELLO.MOD`. PIM StrIO WriteString matches the probe;
uppercase `.MOD` needs `-x modula-2`.)

### Why this heading (HELLO.MOD / excavate)

A minimal HELLO surface looks like:

```modula-2
MODULE Hello;
FROM StrIO IMPORT WriteString, WriteLn;
BEGIN
  WriteString("EMPEROR-TIME-MOD-PROBE-OK");
  WriteLn
END Hello.
```

in a `.MOD` / `.mod` file. That is exactly the pinned form:
`gm2` **compiles and links the named module file** (with `-x modula-2` when
the extension is uppercase), observe `WriteString` output at run time.
Pinning Example compile and link lets excavate treat gm2 + StrIO as **era
evidence** (Modula-2 compiler / source file) without rewriting the fixture
into ISO-only libraries, DEFINITION MODULE pairs, or a Python port.

**Dialect precision:** this pin authorizes GNU Modula-2 reading of the
`WriteString` / `.mod` shape only. It does **not** claim the lost tree is a
specific ISO 10514-1 year, Wirth edition, or commercial Modula-2. Those are
other manuals. HELLO’s “gm2 14-ish / PIM” label remains **CONJECTURE** until
a dialect-specific vendor run is evidence — `gm2` accepting the StrIO shape
is the VERIFIED claim for this leaf.
