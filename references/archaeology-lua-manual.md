# Jail pin — lua(1) SYNOPSIS script + DESCRIPTION script-file evaluation (HELLO.LUA)

Contemporaneous manual pin for the lost-lua archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Lua
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-lua/HELLO.LUA` with
runnable dialect **VERIFIED** as Lua 5.4.7
under Linux x86_64
(`lua HELLO.LUA` →
`EMPEROR-TIME-LUA-PROBE-OK`). Filename culture
(`.LUA` / 8.3 caps → Lua script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.lua` only. Bare `lua` is allowed as a
route tag (tool binary name — word-boundary match). Bare `.lua` is
**allowed** as a route tag (no known peer excavate substring collision).
Debian package `lua5.4` provides `/usr/bin/lua5.4` and the
`lua` alternatives slave. This note supplies the Jail pin so excavate
can name the **verified** Lua script-file-evaluation shape
without inventing a full LuaJIT / C API / LuaRocks
suite claim for a `print` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *lua5.4(1)* — SYNOPSIS script / DESCRIPTION script-file evaluation |
| **Heading** | **SYNOPSIS** — `lua [ options ] [ script [ args ] ]`; **DESCRIPTION** — After handling the options, the Lua program in file script is loaded and executed |
| **Dialect pinned** | **Lua via PUC-Rio Lua 5.4** with `print` script-file surface — **not** full LuaJIT / Lua 5.1 / C API / LuaRocks suite claim |
| **URL** | https://manpages.debian.org/trixie/lua5.4/lua5.4.1.en.html (lua5.4(1)); package `lua5.4` 5.4.7-1+b2 on Debian trixie; installed `lua -v` |
| **Anchors** | script on the command line after options; `print` for string output (Lua 5.4 reference §6.1); optional `-e` / `-i` / `-l` not required for this probe |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie lua5.4(1) SYNOPSIS / DESCRIPTION)

> **SYNOPSIS**
> `lua [ options ] [ script [ args ] ]`

> **DESCRIPTION**
> lua is the standalone Lua interpreter. It loads and executes Lua
> programs, either in textual source form or in precompiled binary form.
> (Precompiled binaries are output by luac, the Lua compiler.) lua can be
> used as a batch interpreter and also interactively.
>
> After handling the options, the Lua program in file script is loaded
> and executed. The args are available to script as strings in a global
> table named arg and also as arguments to its main function. …

(Source: Debian manpages for package `lua5.4` 5.4.7-1+b2 on trixie,
https://manpages.debian.org/trixie/lua5.4/lua5.4.1.en.html sections
**SYNOPSIS** and **DESCRIPTION**,
accessed 2026-09-28 Europe/Tirane.
Installed `lua -v` reports Lua 5.4.7 and matches the
script-file surface. Probe uses `lua HELLO.LUA` so Lua loads and
executes the named script. Authors: R. Ierusalimschy, L. H. de
Figueiredo, W. Celes — see AUTHORS / SEE ALSO lua.org reference
manual §7.)

### Why this heading (HELLO.LUA / excavate)

A minimal HELLO surface looks like:

```lua
print("EMPEROR-TIME-LUA-PROBE-OK")
```

in a `.LUA` / `.lua` file. That is exactly the pinned form:
**`lua FILE`** (also **`lua5.4 FILE`**) loads and executes Lua
source from the named script, observe string print at run time.
Pinning SYNOPSIS script + DESCRIPTION script-file evaluation lets
excavate treat `lua` / `lua5.4` / `.lua` + `print` as
**era evidence** (PUC-Rio Lua / Lua script file) without rewriting
the fixture into a shell one-liner, a Python port, or an interactive
`-i` REPL session. Identify surveys `*.lua` fossils on disk.
Word-boundary matching on bare `lua` covers `hello.lua` utterances
alongside the `.lua` extension tag.

**Dialect precision:** this pin authorizes Lua reading of
the `print` / script-file-evaluation shape only. It does
**not** claim the lost tree is LuaJIT, Lua 5.1, the C API, or a full
LuaRocks recovery on this host.
Those are other manuals / toolchains. HELLO's "lua-ish / print
subset" label remains **CONJECTURE** until a dialect-specific vendor
run is evidence — Lua accepting the `print` shape and
printing the probe string is the VERIFIED claim for this leaf.
