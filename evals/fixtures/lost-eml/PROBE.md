# Boot probe — lost-eml / HELLO.eml

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~14:38 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **Python 3.13.5** stdlib `email.parser` (already on box; module has no `__version__` attribute) |
| Binary / module | `/usr/bin/python3` + `email.parser.BytesParser.parsebytes` |
| Reported | `Python 3.13.5` / stdlib `email` (`python3 --version`; `python3 -c 'import email.parser; print(email.parser.__file__)'`) |
| Install | already on box (CPython stdlib) — **zero new Apt Worthy Spend** this leaf; Debian `mailutils` 1:3.19-1 apt simulated (pulls systemd/exim/cron stack; package Installed-Size ~961 kB alone plus large dep tree) — **REJECTED** vs zero-apt stdlib; Debian `mutt` 2.2.13 Installed-Size ~7113 kB also REJECTED; still prefer over deferred TeXlive / C++ / openjdk / graphviz multi-dep apt |

Probe used `python3` + stdlib `email.parser.BytesParser.parsebytes` on a minimal
RFC 5322 `.eml` and printed the `Subject` header value.
Identify fossils use `*.eml` (Internet message / RFC 822 peer leaf after plist). Prefer `eml` / `pyemail` / `email.parser` / `.eml`.
Bare `eml` is **allowed** as a route tag (format name; 3-char word-boundary).
Bare `pyemail` / `email.parser` are **allowed** as route tags (family / module).
Bare `email` is **refused** (discourse collision with "email the client" / send-mail utterances).
Bare `.eml` is **allowed** with extension-boundary matching (do not invent
`.emlfoo` / `.emlx` prefix hits). Message-format leaf after plist;
treats eml as peer fossil not house twin language. Do **not**
claim a full mailutils / mutt / IMAP / SMTP MUA suite recovery from a CPython
stdlib `BytesParser.parsebytes` Subject probe alone — this leaf pins stdlib
`email.parser` parse with the probe token printed. Do **not** claim Debian
`mailutils` / `mutt` as the verified toolchain this leaf (apt REJECTED).
Distinct from HTML (`*.html` / tidy) and from plist (`*.plist` / stdlib plistlib).

## Commands (VERIFIED)

```text
$ python3 --version
Python 3.13.5

$ python3 -c 'import email.parser; print(email.parser.__file__)'
/usr/lib/python3.13/email/parser.py

$ python3 -c "from email.parser import BytesParser; from email import policy; print(BytesParser(policy=policy.default).parsebytes(open('HELLO.eml','rb').read())['Subject'])"
EMPEROR-TIME-EML-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| CPython 3.13.5 stdlib `email.parser.BytesParser.parsebytes` Subject on this HELLO (RFC 5322 text) | VERIFIED |
| Full MIME multipart / IMAP / SMTP / MUA round-trip are this dialect | CONJECTURE |
| Full mailutils / mutt suite recovery from this probe alone | UNVERIFIABLE |
