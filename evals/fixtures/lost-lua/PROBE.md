# Boot probe — lost-lua / HELLO.LUA

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~09:01 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **lua5.4** 5.4.7-1+b2 (Debian; provides `/usr/bin/lua` via alternatives) |
| Binary | `/usr/bin/lua` → `/usr/bin/lua5.4` (Lua 5.4 / PUC-Rio) |
| Reported | `Lua 5.4.7  Copyright (C) 1994-2024 Lua.org, PUC-Rio` |
| Install | `apt-get install lua5.4` (Debian trixie) |

Probe used script-file evaluation
(`lua HELLO.LUA` / `lua5.4 HELLO.LUA`)
on a minimal `print` script. Identify fossils
use `*.lua` only. Prefer `lua` / `lua5.4` / `.lua`. Bare `lua`
is **allowed** as a route tag because it is the tool binary name
(word-boundary match). Bare `.lua` is **allowed** (no known substring
collision with peer excavate fossils). Do not claim a full Lua /
LuaJIT / LuaRocks / C API suite recovery from a `print` probe
alone — this leaf pins Lua standalone script-file evaluation.

## Commands (VERIFIED)

```text
$ dpkg -l lua5.4 | awk '/^ii/ {print $2, $3}'
lua5.4 5.4.7-1+b2

$ lua -v
Lua 5.4.7  Copyright (C) 1994-2024 Lua.org, PUC-Rio

$ which lua lua5.4
/usr/bin/lua
/usr/bin/lua5.4

$ lua evals/fixtures/lost-lua/HELLO.LUA
EMPEROR-TIME-LUA-PROBE-OK
# exit 0
```

Note: lua(1) SYNOPSIS is `lua [ options ] [ script [ args ] ]`.
Documented VERIFIED form is **`lua HELLO.LUA`** (also
`lua5.4 HELLO.LUA`). DESCRIPTION: after options, the Lua program
in file script is loaded and executed. `print` is the standard
library string-output function (Lua 5.4 reference §6.1).

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Lua fossil named `HELLO.LUA` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-lua` prints `1 *.lua` |
| Runs under Lua 5.4.7 script-file evaluation | VERIFIED | `lua HELLO.LUA` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-LUA-PROBE-OK` |
| Dialect is a specific LuaJIT / Lua 5.1 / C API claim | CONJECTURE | No LuaJIT / 5.1 / embedding jury beyond `print` under Lua 5.4 |
| Would run under period Lua 4 / non-PUC-Rio Lua | UNVERIFIABLE here | No period Lua ROM in this session |
| Full LuaRocks / C API / coroutines suite | UNVERIFIABLE here | single print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Lua reference manual beyond
  lua(1) SYNOPSIS script + DESCRIPTION script load/execute +
  `print` (deferred; pin is **lua FILE** — see
  `references/archaeology-lua-manual.md`).
- Bare `lua` is allowed (tool binary name; word-boundary); bare
  `.lua` allowed (no peer collision).
- No `*.luac` fossil this leaf (bytecode / luac out of scope for
  the print probe).
