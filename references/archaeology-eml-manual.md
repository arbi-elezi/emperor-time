# Jail pin — Python email.parser.BytesParser.parsebytes for HELLO.eml

Contemporaneous manual pin for the lost-eml archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how eml
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-eml/HELLO.eml` with
runnable dialect **VERIFIED** as CPython 3.13.5 stdlib `email.parser`
under Linux x86_64
(`python3` + `BytesParser.parsebytes` on HELLO.eml → Subject
`EMPEROR-TIME-EML-PROBE-OK`). Filename culture
(mbox / Maildir / Apple `.emlx` / Outlook `.msg`)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.eml`.
Bare `eml` / `pyemail` / `email.parser` are **allowed** as route tags (format / family / module).
Bare `email` is **refused** (discourse collision with send-mail utterances).
Bare `.eml` is **allowed** as a route tag with
extension-boundary matching. Prefer `eml` /
`pyemail` / `email.parser` / `.eml`.
Toolchain is CPython stdlib `email.parser` already on box (**zero new apt**).
Debian `mailutils` 1:3.19-1 apt was simulated (pulls systemd/exim/cron) and **REJECTED**;
Debian `mutt` 2.2.13 (~7113 kB Installed-Size) also **REJECTED**. This note supplies
the Jail pin so excavate can name the **verified** stdlib `email.parser`
Subject parse shape without inventing a full
mailutils / mutt / IMAP / SMTP MUA suite claim for a
single-header probe. Distinct from the HTML archaeology leaf (`*.html` /
tidy) and from plist (`*.plist` / stdlib plistlib).

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Python 3 Library Reference — `email.parser`: Parsing email messages* |
| **Heading** | **`BytesParser.parsebytes`** — Parse a bytes-like object into a message object structure; then read header via mapping `__getitem__` |
| **Dialect pinned** | **CPython stdlib `email.parser.BytesParser.parsebytes`** with RFC 5322 `Subject` header → print value — **not** full mailutils / mutt / IMAP / SMTP MUA suite claim |
| **URL** | https://docs.python.org/3/library/email.parser.html (Python docs — `email.parser`); header access https://docs.python.org/3/library/email.message.html ; CPython 3.13.5 on box |
| **Anchors** | `.eml` document path; `BytesParser(policy=...).parsebytes(bytes)`; `msg['Subject']` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Python docs — `email.parser.BytesParser.parsebytes`)

> Similar to the parse() method, except it takes a bytes-like object instead of a file-like object. Calling this method on a bytes-like object is equivalent to wrapping bytes in a BytesIO instance first and calling parse().

(Source: Python 3 Library Reference, section
**email.parser: Parsing email messages — `BytesParser.parsebytes`**,
https://docs.python.org/3/library/email.parser.html
accessed 2026-09-28 Europe/Tirane.
Header access quote from email.message mapping interface:
"Return the value of the named header field. name does not include the colon field separator."
https://docs.python.org/3/library/email.message.html
Installed `python3 --version` reports Python 3.13.5.
Probe uses
`BytesParser(policy=policy.default).parsebytes(open('HELLO.eml','rb').read())['Subject']`
so stdlib email.parser loads the named `.eml` and prints the Subject.
Format: RFC 5322 Internet message text.)

### Why this heading (HELLO.eml / excavate)

A minimal HELLO surface looks like a one-header RFC 5322 message with
`Subject` holding a probe token. That is exactly the pinned form:
**stdlib `BytesParser.parsebytes`**, observe Subject at run time.

### Honesty

- VERIFIED: CPython 3.13.5 stdlib `email.parser.BytesParser.parsebytes` Subject on this HELLO (RFC 5322 text).
- CONJECTURE: any claim that mbox / Maildir / IMAP / SMTP MUA are this dialect.
- UNVERIFIABLE: mailutils / mutt / full multi-dialect mail recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, openjdk/Java (apt size); graphviz this turn (multi-dep); Debian `mailutils` / `mutt` apt (unnecessary vs stdlib / large deps); bare `email` as route tag (discourse collision); bare `mailutils` / `mutt` as verified toolchain; `*.cfg` / `*.conf` / `*.tsv` / `*.jsonl` fossils this leaf (defer); `*.msg` / `.emlx` fossils this leaf (defer).
