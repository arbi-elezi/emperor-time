# Jail pin — Prolog initialization/2 main + swipl (HELLO.PRO)

Contemporaneous manual pin for the lost-Prolog archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Prolog
works” stays **CONJECTURE** until a consult/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-prolog/HELLO.PRO` with
runnable dialect **VERIFIED** as SWI-Prolog 9.2.9
(`swipl -q -t halt HELLO.PRO`). Filename culture (`.PRO` / 8.3 caps → Prolog
*naming*) remains **CONJECTURE** only. Identify fossils use `*.pro` /
`*.prolog` only — **not** `*.pl` (Perl collision). This note supplies the
Jail pin so excavate can name the **verified** non-interactive main-goal
shape without inventing a GNU Prolog / SICStus vendor manual for a SWI
Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *SWI-Prolog Reference Manual* — **initialization/2** (matches probe toolchain family) |
| **Heading** | **main** role of `initialization/2` — last registered main goal runs at startup; toplevel defaults to `halt/0` |
| **Dialect pinned** | **SWI-Prolog** Edinburgh-ish source file with `write/1` / `nl/0` / `halt/0` + `initialization(Goal, main)` — **not** GNU Prolog, **not** SICStus, **not** a specific ISO/IEC 13211 year claim |
| **URL** | https://www.swi-prolog.org/pldoc/doc_for?object=(initialization)/2 |
| **Anchors** | role `main` under `initialization/2` (batch / application file run) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from initialization/2 — main)

> When Prolog starts, the last goal registered using `initialization(Goal, main)` is executed as main goal. If Goal fails or raises an exception, the process terminates with non-zero exit code. If not explicitly specified using the -t the toplevel goal is set to halt/0, causing the process to exit with status 0. An explicitly specified toplevel is executed normally. This implies that `-t prolog` causes the application to start the normal interactive toplevel after completing Goal.

(SWI-Prolog 9.2.9 / Debian `swi-prolog-nox` 9.2.9+dfsg-1+b1 document the
invoke surface used by probe `swipl -q -t halt HELLO.PRO` and
`swipl -q HELLO.PRO`.)

### Why this heading (HELLO.PRO / excavate)

A minimal HELLO surface looks like:

```prolog
:- initialization(main, main).
main :-
    write('EMPEROR-TIME-PROLOG-PROBE-OK'), nl,
    halt.
```

in a `.PRO` / `.pro` / `.prolog` file. That is exactly the pinned form:
`swipl` **runs the registered main goal** non-interactively (no REPL),
observe `write`/`nl` output at run time. Pinning `initialization/2` main
lets excavate treat write + main-goal file as **era evidence** (Prolog
interpreter / source file) without rewriting the fixture into DCGs, CLP,
or a Python port.

**Dialect precision:** this pin authorizes SWI reading of the `write` /
`nl` / `halt` / `initialization(..., main)` / `.pro` shape only. It does
**not** claim the lost tree is ISO Prolog verbatim, GNU Prolog, or
SICStus. Those are other manuals. HELLO’s “ISO/Edinburgh-ish” label
remains **CONJECTURE** until a dialect-specific vendor run is evidence —
`swipl` accepting the write/main shape is the VERIFIED claim for this leaf.
