# Boot probe — lost-pl / HELLO.PL

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~08:11 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **perl** 5.40.1-6+deb13u1 (Debian; pulls **perl-base** 5.40.1-6+deb13u1, **perl-modules-5.40**) |
| Binary | `/usr/bin/perl` (Perl 5) |
| Reported | `This is perl 5, version 40, subversion 1 (v5.40.1)` |
| Install | preinstalled on this box (`apt` package `perl`) |

Probe used Perl programfile execution
(`perl HELLO.PL`)
on a minimal script that prints the probe string.
Identify fossils use `*.pl` and `*.pm`. Prefer `perl` / `perl5` / `.pm`.
Bare `perl` is **allowed** as a route tag (tool binary name). Bare `.pl` is
**refused** as a route tag (substring collision with PL/I `.pli` / `.pl1`).
Prolog fossils stay on `*.pro` / `*.prolog` so this leaf can reclaim `*.pl`.
Do not claim a full CPAN / XS / mod_perl / Perl 4 suite recovery from a
Perl 5 programfile print probe alone — this leaf pins Perl 5 `perl`
programfile invoke.

## Commands (VERIFIED)

```text
$ dpkg -l perl perl-base | awk '/^ii/ {print $2, $3}'
perl 5.40.1-6+deb13u1
perl-base 5.40.1-6+deb13u1

$ perl -v 2>&1 | head -4

This is perl 5, version 40, subversion 1 (v5.40.1) built for x86_64-linux-gnu-thread-multi
(with 70 registered patches, see perl -V for more detail)

$ which perl
/usr/bin/perl

$ cd evals/fixtures/lost-pl
$ perl HELLO.PL
EMPEROR-TIME-PERL-PROBE-OK
# exit 0
```

Note: perlrun(1) SYNOPSIS ends with `[ programfile ] [ argument ]...`.
With a programfile argument perl reads and executes that source file.
Documented VERIFIED form is **`perl HELLO.PL`**. The fixture is a single
`print` statement so the leaf pins interpreter programfile invocation, not
a module / XS / CGI jury.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Perl fossil named `HELLO.PL` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-pl` prints `1 *.pl` |
| Runs under Perl 5.40.1 programfile input | VERIFIED | `perl HELLO.PL` exit 0 |
| Prints known ASCII string | VERIFIED | stdout contains `EMPEROR-TIME-PERL-PROBE-OK` |
| Dialect is a specific Perl 4 / ActiveState / mod_perl claim | CONJECTURE | No other Perl jury beyond Perl 5 programfile of this input |
| Would run under period Perl 4 on original media | UNVERIFIABLE here | No period Perl 4 ROM run in this session |
| Full CPAN / XS / Embed suite | UNVERIFIABLE here | single programfile print probe only |

## Not done (honest gaps)

- No Jail-hunt of the full perlbook / perlsyn beyond
  SYNOPSIS programfile + DESCRIPTION file-on-command-line (deferred; pin is
  **perl FILE** — see `references/archaeology-perl-manual.md`).
- Bare `perl` allowed (tool binary name). Bare `.pl` refused (PL/I collision).
- No `*.t` / `*.cgi` / `*.psgi` fossil this leaf (`.pl` / `.pm` only; avoid
  test-harness and framework overclaim).
