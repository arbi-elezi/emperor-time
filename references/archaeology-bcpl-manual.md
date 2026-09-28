# Jail pin — Martin Richards BCPL Cintcode cintsys `-c` / `bcpl … to …` (HELLO.B)

Contemporaneous manual pin for the lost-BCPL archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how BCPL
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-bcpl/HELLO.B` with
runnable dialect **VERIFIED** as Martin Richards BCPL 32-bit Cintcode
(16 May 2026 system / 18 Apr 2026 compiler) under Linux x86_64
(`cintsys -q -c 'bcpl hello.b to hello; hello'` →
`EMPEROR-TIME-BCPL-PROBE-OK`). Filename culture (`.B` / 8.3 caps → BCPL
*naming*) remains **CONJECTURE** only. Identify fossils use `*.b` and
`*.bcpl`. This note supplies the Jail pin so excavate can name the
**verified** cintsys `-c` / `bcpl file.b to dest` shape without inventing
a full period Cambridge Tripos / native-code claim for a print probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Martin Richards BCPL Cintcode System* — `cintsys` help / distribution README (Linux installation; compile-run examples) |
| **Heading** | **Valid arguments** — `-c args` (pass args to interpreter as CLI input); README compile-run form `bcpl <file.b> to <dest>` |
| **Dialect pinned** | **BCPL via Martin Richards Cintcode** with `GET "libhdr"` / `writef` print surface — **not** full Tripos / native BCPL / floating-point claim |
| **URL** | https://www.cl.cam.ac.uk/~mr10/BCPL.html (project); distribution https://www.cl.cam.ac.uk/~mr10/BCPL/bcpl.tgz (`cintcode` README / `cintsys -h`) |
| **Anchors** | Valid arguments — `-c args`; README examples `bcpl com/echo.b to junk` / demo compile-run |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Martin Richards `cintsys -h` Valid arguments + distribution README)

> **Valid arguments:**
> `-c args` — Pass args to interpreter as CLI input
>
> (README Linux installation / try-out examples:)
> `bcpl com/echo.b to junk`
> `junk hello`

(Probe uses the quiet scripting form
`cintsys -q -c 'bcpl hello.b to hello; hello'`, which compiles the named
`.b` source to a Cintcode command then runs it. Fixture keeps `.B` 8.3
caps for sister-fixture culture; Martin Richards `bcpl` wants a
lowercase `hello.b` path, so the probe links/copies before compile.)

### Why this heading (HELLO.B / excavate)

A minimal HELLO surface looks like:

```bcpl
GET "libhdr"

LET start() = VALOF
{ writef("EMPEROR-TIME-BCPL-PROBE-OK*n")
  RESULTIS 0
}
```

in a `.B` / `.b` file. That is exactly the pinned form: `cintsys -c`
feeds CLI input that runs **`bcpl <file.b> to <dest>`** then executes
the compiled command, observe `writef` at run time. Pinning Valid
arguments / `-c` + `bcpl … to …` lets excavate treat `bcpl` / `cintsys` /
`cintcode` / `.bcpl` + `GET "libhdr"` / `writef` as **era evidence**
(BCPL Cintcode / source file) without rewriting the fixture into Tripos
syscalls, native codegen, or a Python port.

**Dialect precision:** this pin authorizes Martin Richards Cintcode
reading of the `GET "libhdr"` / `writef` / `bcpl … to …` shape only. It
does **not** claim the lost tree is period CTSS / Multics / other vendor
BCPL on original media, a specific Tripos release, or a working native
`natbcpl` build on this host. Those are other manuals / toolchains.
HELLO's "Cambridge-Cintcode-ish / libhdr subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence —
Cintcode accepting the `writef` shape and printing the probe string is
the VERIFIED claim for this leaf.
