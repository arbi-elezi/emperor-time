# Jail pin — escript main/1 (HELLO.ERL)

Contemporaneous manual pin for the lost-Erlang archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of “how Erlang
works” stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-erl/HELLO.ERL` with
runnable dialect **VERIFIED** as OTP 27
(`escript HELLO.ERL`). Filename culture (`.ERL` / 8.3 caps → Erlang
*naming*) remains **CONJECTURE** only. Identify fossils use `*.erl` /
`*.hrl`. This note supplies the Jail pin so excavate can name the
**verified** non-interactive escript shape without inventing a gen_server /
OTP release vendor manual for an `escript` Linux probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *escript* — Erlang/OTP ERTS application reference (matches probe toolchain family) |
| **Heading** | **main/1** — an Erlang script file must always contain `main/1`; when run, `main/1` is called with the script arguments (batch / application file run via `escript`) |
| **Dialect pinned** | **OTP 27** escript with `main/1` + `io:format` — **not** a gen_server, **not** a specific EEP year claim, **not** an Elixir claim |
| **URL** | https://www.erlang.org/doc/apps/erts/escript_cmd.html |
| **Anchors** | Description — `main/1` requirement (batch / application file run) |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from escript Description — main/1)

> An Erlang script file must always contain the `main/1` function. When the script is run, the `main/1` function is called with a list of strings representing the arguments specified to the script (not changed or interpreted in any way).

(OTP 27 / Debian `erlang-base` 27.3.4.1 document the invoke surface used by probe
`escript HELLO.ERL`. Online doc page may show a newer OTP label; the
`main/1` contract matches the probe.)

### Why this heading (HELLO.ERL / excavate)

A minimal HELLO surface looks like:

```erlang
#!/usr/bin/env escript
%% -*- erlang -*-
main(_) ->
    io:format("EMPEROR-TIME-ERL-PROBE-OK~n").
```

in a `.ERL` / `.erl` / `.hrl` file. That is exactly the pinned form:
`escript` **runs the named script file** non-interactively (no REPL),
observe `io:format` output at run time. Pinning main/1 lets excavate
treat escript + main/1 as **era evidence** (Erlang interpreter / source
file) without rewriting the fixture into OTP applications, gen_servers, or a
Python port.

**Dialect precision:** this pin authorizes Erlang reading of the `main/1` /
`.erl` shape only. It does **not** claim the lost tree is a specific EEP,
OTP release, or Elixir. Those are other manuals. HELLO’s “OTP 27-ish”
label remains **CONJECTURE** until a dialect-specific vendor run is
evidence — `escript` accepting the main/1 shape is the VERIFIED claim for
this leaf.
