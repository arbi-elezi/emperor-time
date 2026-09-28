# Boot probe — lost-ruby / HELLO.RB

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~09:12 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **ruby** 1:3.3+b1 (Debian meta; Depends **ruby3.3** 3.3.8-2) |
| Binary | `/usr/bin/ruby` → `/usr/bin/ruby3.3` (MRI / Yukihiro Matsumoto) |
| Reported | `ruby 3.3.8 (2025-04-09 revision b200bad6cd) [x86_64-linux-gnu]` |
| Install | `apt-get install ruby` (Debian trixie) |

Probe used script-file evaluation
(`ruby HELLO.RB` / `ruby3.3 HELLO.RB`)
on a minimal `puts` script. Identify fossils
use `*.rb` only. Prefer `ruby` / `ruby3.3` / `.rb`. Bare `ruby`
is **allowed** as a route tag because it is the tool binary name
(word-boundary match). Bare `.rb` is **allowed** (no known substring
collision with peer excavate fossils). Do not claim a full Rails /
Bundler / RubyGems / Ractor suite recovery from a `puts` probe
alone — this leaf pins Ruby standalone script-file evaluation.

## Commands (VERIFIED)

```text
$ dpkg -l ruby ruby3.3 | awk '/^ii/ {print $2, $3}'
ruby 1:3.3+b1
ruby3.3 3.3.8-2

$ ruby -v
ruby 3.3.8 (2025-04-09 revision b200bad6cd) [x86_64-linux-gnu]

$ which ruby ruby3.3
/usr/bin/ruby
/usr/bin/ruby3.3

$ ruby evals/fixtures/lost-ruby/HELLO.RB
EMPEROR-TIME-RUBY-PROBE-OK
# exit 0
```

Note: ruby3.3(1) SYNOPSIS is
`ruby [options] [--] [program_file] [argument ...]`.
Documented VERIFIED form is **`ruby HELLO.RB`** (also
`ruby3.3 HELLO.RB`). DESCRIPTION: Ruby is an interpreted scripting
language; FEATURES Interpretive — programs written in Ruby execute
without recompile. `puts` is the Kernel string-output method.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Ruby fossil named `HELLO.RB` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-ruby` prints `1 *.rb` |
| Runs under Ruby 3.3.8 script-file evaluation | VERIFIED | `ruby HELLO.RB` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-RUBY-PROBE-OK` |
| Dialect is a specific Rails / JRuby / TruffleRuby claim | CONJECTURE | No Rails / alternate-VM jury beyond `puts` under MRI 3.3 |
| Would run under period Ruby 1.8 / non-MRI Ruby | UNVERIFIABLE here | No period Ruby ROM in this session |
| Full Rails / Bundler / RubyGems / Ractor suite | UNVERIFIABLE here | single puts probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Ruby reference manual beyond
  ruby3.3(1) SYNOPSIS program_file + DESCRIPTION interpretive
  scripting + `puts` (deferred; pin is **ruby FILE** — see
  `references/archaeology-ruby-manual.md`).
- Bare `ruby` is allowed (tool binary name; word-boundary); bare
  `.rb` allowed (no peer collision).
- No `*.rake` / Gemfile fossil this leaf (Rake / Bundler out of scope for
  the puts probe).
