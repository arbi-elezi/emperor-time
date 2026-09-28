# Jail pin — GNU MARST Usage Example / outstring (HELLO.A60)

Contemporaneous manual pin for the lost-ALGOL-60 archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how ALGOL 60
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-a60/HELLO.A60` with
runnable dialect **VERIFIED** as GNU MARST 2.8
(`marst HELLO.A60 -o HELLO.c` then `gcc HELLO.c -lalgol -lm -o HELLO`).
Filename culture (`.A60` / 8.3 caps → ALGOL 60 *naming*) remains
**CONJECTURE** only. Identify fossils use `*.a60` (not `*.alg` — Algol 68
leaf). This note supplies the Jail pin so excavate can name the
**verified** marst Usage Example `outstring` shape without inventing a
full IFIP Modified Report vendor clause for a `marst` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *GNU MARST--Algol-to-C Translator* (marst.texi / GNU MARST package docs) |
| **Heading** | **Usage Example** — `outstring(1, "…")` plus `marst hello.alg -o hello.c` / `gcc hello.c -lalgol -lm -o hello` |
| **Dialect pinned** | **GNU MARST / IFIP ALGOL 60 subset** with ALGLIB `outstring` string output — **not** full Modified Report, **not** Algol 68 / Algol W |
| **URL** | https://www.gnu.org/software/marst/ |
| **Anchors** | Usage Example (marst-2.8 `doc/marst.texi` chapter) — `outstring` / `marst … -o …` / `gcc … -lalgol -lm` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from GNU MARST — Usage Example)

> At first, you prepare a source Algol 60 program, say, in a text file named `hello.alg`:
>
> ```algol60
> begin
>    outstring(1, "Hello, world!\n")
> end
> ```
>
> Then you translate this program to the C programming language:
>
> `marst hello.alg -o hello.c`
>
> and get the text file named `hello.c`, which you need to compile and link
> in an usual way (remember about specifying Algol and math libraries for
> the linker):
>
> `gcc hello.c -lalgol -lm -o hello`

(GNU MARST 2.8 / `marst` document the invoke surface used by probe
`marst HELLO.A60 -o HELLO.c` then `gcc … -lalgol -lm`. ALGLIB `outstring`
matches the probe program. Fixture uses `.A60` so identify fossils stay
distinct from Algol 68 `*.alg`.)

### Why this heading (HELLO.A60 / excavate)

A minimal HELLO surface looks like:

```algol60
begin
   outstring(1, "EMPEROR-TIME-A60-PROBE-OK\n")
end
```

in a `.A60` / `.a60` file. That is exactly the pinned form:
`marst` **translates the named source file to C**, then `gcc` links with
`-lalgol -lm`, observe `outstring` output at run time. Pinning Usage
Example lets excavate treat marst + `outstring` as **era evidence**
(ALGOL 60 translator / source file) without rewriting the fixture into
call-by-name Jensen devices, `own` storage, or a Python port.

**Dialect precision:** this pin authorizes GNU MARST reading of the
`outstring` / `.a60` shape only. It does **not** claim the lost tree is a
specific IFIP printing year, Algol 68, Algol W, or a period vendor
checkout compiler. Those are other manuals. HELLO’s “marst 2.8-ish /
ALGOL 60 subset” label remains **CONJECTURE** until a dialect-specific
vendor run is evidence — `marst` accepting the `outstring` shape and the
linked binary printing the probe string is the VERIFIED claim for this leaf.
