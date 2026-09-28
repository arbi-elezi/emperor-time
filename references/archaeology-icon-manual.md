# Jail pin — Icon 9 UNIX Manual Page SYNOPSIS / File Names (HELLO.ICN)

Contemporaneous manual pin for the lost-Icon archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Icon
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-icn/HELLO.ICN` with
runnable dialect **VERIFIED** as Icon 9.5.24b
(`ln -sf HELLO.ICN hello.icn` then `icont -s hello.icn` then `./hello`).
Filename culture (`.ICN` / 8.3 caps → Icon *naming*) remains
**CONJECTURE** only. Identify fossils use `*.icn` only. This note supplies
the Jail pin so excavate can name the **verified** Icon 9 UNIX Manual Page
SYNOPSIS / File Names shape without inventing a full Griswold book claim
for an `icont` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Icon 9 UNIX Manual Page* (IPD244d) — Ralph E. Griswold |
| **Heading** | **SYNOPSIS** / **File Names** — `icont [option ...] file ... [-x arg ...]` with `.icn` source suffix |
| **Dialect pinned** | **Icon Version 9 translator (`icont`) / icode** with standard `write` string output — **not** Unicon, **not** full string-scanning / goal-directed claim |
| **URL** | https://www2.cs.arizona.edu/icon/docs/ipd244.htm |
| **Anchors** | SYNOPSIS `icont [option ...] file ... [-x arg ...]` — File Names `.icn` suffix |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from IPD244d — SYNOPSIS / File Names)

> **SYNOPSIS**
>
> `icont` [ option ... ] file ... [`-x` arg ... ]
>
> **File Names:** Files whose names end in `.icn` are assumed to be Icon
> source files. The `.icn` suffix may be omitted; if it is not present, it
> is supplied. ... The name of the executable file is the base name of the
> first input file, formed by deleting the suffix, if present.

(IPD244d documents the invoke surface used by probe
`icont -s hello.icn`. Standard I/O `write` / `procedure main` matches the
probe program. Fixture keeps `.ICN` 8.3 caps for sister-fixture culture;
Linux `icont` lowercases the `.icn` suffix when opening, so the probe
links `hello.icn` → `HELLO.ICN`.)

### Why this heading (HELLO.ICN / excavate)

A minimal HELLO surface looks like:

```icon
procedure main()
   write("EMPEROR-TIME-ICN-PROBE-OK")
end
```

in a `.ICN` / `.icn` file. That is exactly the pinned form:
`icont` **translates the named source file to an icode executable**,
observe `write` output at run time. Pinning SYNOPSIS / File Names lets
excavate treat icont + `.icn` + `write` as **era evidence** (Icon
translator / source file) without rewriting the fixture into scanning,
generators, or a Python port.

**Dialect precision:** this pin authorizes Icon 9 `icont` reading of the
`write` / `procedure main` / `.icn` shape only. It does **not** claim the
lost tree is Unicon, a specific printing of *The Icon Programming
Language* book, or a period Arizona tape checkout. Those are other
manuals. HELLO's "Icon 9.5-ish / write subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — `icont`
accepting the `write` shape and the icode binary printing the probe
string is the VERIFIED claim for this leaf.
