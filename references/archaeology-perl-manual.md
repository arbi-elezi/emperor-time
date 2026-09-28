# Jail pin — Perl perlrun(1) SYNOPSIS programfile + DESCRIPTION file-on-command-line (HELLO.PL)

Contemporaneous manual pin for the lost-pl archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Perl
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-pl/HELLO.PL` with
runnable dialect **VERIFIED** as Perl 5.40.1
under Linux x86_64
(`perl HELLO.PL` →
`EMPEROR-TIME-PERL-PROBE-OK`). Filename culture
(`.PL` / 8.3 caps → Perl script *naming*) remains **CONJECTURE** only.
Identify fossils use `*.pl` and `*.pm`. Bare `perl` is allowed as a
route tag (tool binary name — not an English collision like
`scheme` / `basic`, and not a factory collision like refused bare
`make`). Bare `.pl` is **refused** as a route tag (substring collision
with PL/I `.pli` / `.pl1`). Prolog already left `*.pl` alone for this
reclaim. This note supplies the Jail pin so excavate
can name the **verified** perl programfile shape
without inventing a full CPAN / XS / mod_perl / Perl 4
suite claim for a `print` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *perlrun(1)* — SYNOPSIS programfile / DESCRIPTION file on the command line |
| **Heading** | **SYNOPSIS** — `[ programfile ] [ argument ]...`; **DESCRIPTION** — file specified by the first filename on the command line |
| **Dialect pinned** | **Perl via Perl 5** with programfile input → print surface — **not** full Perl 4 / ActiveState / mod_perl / CPAN suite claim |
| **URL** | https://manpages.debian.org/trixie/perl-doc/perlrun.1.en.html (perlrun(1)); package `perl` 5.40.1-6+deb13u1 on Debian trixie; also https://perldoc.perl.org/perlrun ; installed `perl -v` |
| **Anchors** | positional `programfile` is Perl source; DESCRIPTION place 2: "Contained in the file specified by the first filename on the command line" |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Debian trixie perlrun(1) SYNOPSIS / DESCRIPTION)

> **SYNOPSIS**
> `perl [ -gsTtuUWX ] … [ [-e|-E] 'command' ] [ -- ] [ programfile ] [ argument ]...`

> **NAME**
> perlrun - how to execute the Perl interpreter

> **DESCRIPTION**
> The normal way to run a Perl program is by making it directly executable,
> or else by passing the name of the source file as an argument on the
> command line. … Upon startup, Perl looks for your program in one of the
> following places:
>
> 2. Contained in the file specified by the first filename on the command
>    line. (Note that systems supporting the "#!" notation invoke
>    interpreters this way.)

(Source: Debian manpages for package `perl-doc` / `perl` 5.40.1 on trixie,
https://manpages.debian.org/trixie/perl-doc/perlrun.1.en.html sections
**SYNOPSIS**, **NAME**, and **DESCRIPTION**, accessed
2026-09-28 Europe/Tirane.
Installed `perl -v` on Perl 5.40.1 matches the programfile invoke surface.
Probe uses `perl HELLO.PL` so the interpreter reads the named
script and prints the probe string.
Upstream mirror: https://perldoc.perl.org/perlrun .)

### Why this heading (HELLO.PL / excavate)

A minimal HELLO surface looks like:

```perl
print "EMPEROR-TIME-PERL-PROBE-OK\n";
```

in a `.PL` / `.pl` file. That is exactly the pinned form:
**`perl [programfile]`** (typically **`perl FILE`**)
reads Perl source from the named file, observe print at run time.
Pinning SYNOPSIS programfile + DESCRIPTION file-on-command-line
lets excavate treat `perl` / `perl5` / `.pm` + perl
programfile input as **era evidence** (Perl 5 / Perl script file) without
rewriting the fixture into a Python one-liner, a shell port, or an
interactive debugger session. Bare `.pl` stays off the route table so
PL/I `.pli` / `.pl1` utterances do not false-route here; identify still
surveys `*.pl` fossils on disk.

**Dialect precision:** this pin authorizes Perl 5 reading of
the programfile / `print` shape only. It does
**not** claim the lost tree is Perl 4, ActiveState, mod_perl, or a
specific CPAN distribution on this host. Those are other manuals /
toolchains. HELLO's "perl5-ish / print subset" label remains
**CONJECTURE** until a dialect-specific vendor run is evidence — Perl 5
accepting the FILE input shape and printing the probe
string is the VERIFIED claim for this leaf.
