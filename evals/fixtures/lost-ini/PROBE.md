# Boot probe — lost-ini / HELLO.ini

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~13:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `configparser` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `configparser.ConfigParser.read` / `get` |
| Reported | `Python 3.13.5` / stdlib `configparser` (`python3 --version`; `python3 -c 'import configparser; print(configparser.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `crudini` 0.9.6-1 apt simulated with `python3-iniparse` (~43 kB archives / ~185 kB Installed-Size across 2 new packages) — **REJECTED** vs zero-apt stdlib (tiny but unnecessary); still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `ConfigParser.read` / `get` on a minimal
INI section `[probe]` with option `token`.
Identify fossils use `*.ini` (INI config peer leaf after JSON). Prefer `ini` / `pyini` / `configparser` / `.ini`.
Bare `ini` is **allowed** as a route tag (language / format name; word-boundary for 3-char token).
Bare `pyini` / `configparser` are **allowed** as route tags (family / module).
Bare `.ini` is **allowed** with extension-boundary matching (do not invent
`.inifoo` / `.init` prefix hits). INI config leaf after JSON;
treats INI as peer fossil not house twin language. Do **not**
claim a full crudini / configobj / Windows Registry INI suite recovery from a CPython
stdlib `ConfigParser` probe alone — this leaf pins stdlib `configparser`
section/option lookup with the probe token printed. Do **not** claim Debian
`crudini` as the verified toolchain this leaf (apt REJECTED).

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import configparser; print(configparser.__file__)'
/usr/lib/python3.13/configparser.py

$ python3 -c "import configparser; p=configparser.ConfigParser(); p.read('HELLO.ini'); print(p.get('probe','token'))"
EMPEROR-TIME-INI-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `configparser` `ConfigParser.read`/`get` on this HELLO | VERIFIED |
| Windows Registry extended INI / configobj / TOML-as-INI-replacement are this dialect | CONJECTURE |
| Full crudini / multi-dialect INI suite recovery from this probe alone | UNVERIFIABLE |
