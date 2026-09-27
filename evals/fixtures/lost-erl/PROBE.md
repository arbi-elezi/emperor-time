# Boot probe — lost-erl / HELLO.ERL

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~01:09 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | `erlang-base` **1:27.3.4.1+dfsg-1+deb13u3** (Debian trixie) |
| Binary | `/usr/bin/escript` (+ `/usr/bin/erl`, `/usr/bin/erlc`) |
| Reported | OTP release **27** / erts **15.2.7** |
| Install | `sudo apt-get install -y erlang-base` on this box |

`erlc` + `erl -noshell -s Module` was **not** required for this string-print
probe. Probe used `escript` on OTP 27 because that runs a source file with
`main/1` without a separate beam step. Uppercase `HELLO.ERL` is accepted as
a source filename; that is normal Erlang scripting culture, not a probe
failure. Identify fossils use `*.erl` / `*.hrl` (no known collision with
other house fossils). Bare substring `erl` alone is **refused** as a route
tag for the Perl / "erlang" edge cases; prefer `escript` / `erlc` / `.erl` /
space-intent `erlang`.

## Commands (VERIFIED)

Working directory for load/run: fixture dir (and earlier `/tmp` copy).

```text
$ erl -noshell -eval 'io:format("~s~n",[erlang:system_info(otp_release)]), halt().'
27

$ escript HELLO.ERL
EMPEROR-TIME-ERL-PROBE-OK
# exit 0
```

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Erlang fossil named `HELLO.ERL` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-erl` prints `1 *.erl` |
| Runs under OTP 27 (`escript` file arg) | VERIFIED | `escript HELLO.ERL` exit 0 |
| Prints known string | VERIFIED | stdout is `EMPEROR-TIME-ERL-PROBE-OK` |
| Dialect is a specific OTP year/EEP claim beyond main/1 + io:format | CONJECTURE | No EEP jury; escript main/1 subset only |
| Would run under period Erlang/OTP on original media | UNVERIFIABLE here | No period vendor run in this session |

## Not done (honest gaps)

- No Jail-hunt of a purchased Armstrong book clause (deferred; pin is
  escript main/1 — see `references/archaeology-erlang-manual.md`).
- No OTP application / gen_server / release claim.
- No Dialyzer / HiPE / Elixir claim.
