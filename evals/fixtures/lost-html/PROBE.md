# Boot probe — lost-html / HELLO.html

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~12:58 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **tidy** 2:5.8.0-2 + **libtidy58** 2:5.8.0-2 (Debian trixie) |
| Binary | `/usr/bin/tidy` |
| Reported | HTML Tidy for Linux version 5.8.0 (`tidy --version`) |
| Install | apt this leaf (252 kB archives; Installed-Size sum 1170 kB / ~1198 kB disk; Worthy Spend after TOML; still prefer over TeXlive / C++ / openjdk / graphviz multi-dep apt) |

Probe used `tidy -q -utf8 --show-body-only yes -asxml HELLO.html` on a minimal
HTML5 document with a single text node under `<p id="probe">`.
Identify fossils use `*.html` / `*.htm` (HTML peer leaf after XML/TOML document chain). Prefer `tidy` / `html-tidy` / `tidy5.8` / `html` / `.html` / `.htm`.
Bare `html` is **allowed** as a route tag (language name; substring for 4+ char tokens).
Bare `tidy` is **allowed** as a route tag (tool binary name; word-boundary).
Bare `html-tidy` / `tidy5.8` are **allowed** as route tags (family / version).
Bare `.html` / `.htm` are **allowed** with extension-boundary matching (`.htm` does not prefix-hit `.html`; `.html` does not invent `.htmlfoo` hits). HTML document leaf after XML;
treats HTML as peer fossil not house twin language. Do **not**
claim a full HTML5 / WHATWG / CSS / browser suite recovery from a Debian
`tidy` body-only XHTML pretty-print probe alone — this leaf pins `tidy`
HTML parse + quiet body-only XHTML emit with the probe token preserved.

## Commands (VERIFIED)

```text
$ which tidy
/usr/bin/tidy

$ tidy --version
HTML Tidy for Linux version 5.8.0

$ tidy -q -utf8 --show-body-only yes -asxml HELLO.html 2>/dev/null
<p id="probe">EMPEROR-TIME-TIDY-PROBE-OK</p>

$ tidy -e -q HELLO.html; echo EXIT:$?
EXIT:0
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `tidy -q -utf8 --show-body-only yes -asxml HELLO.html` → body with probe token | VERIFIED |
| Filename culture (XHTML / HTML4 / polyglot / AMP) maps to this dialect | CONJECTURE (probe uses plain HTML5 + tidy XHTML emit) |
| Full HTML5 / WHATWG / CSS / browser feature recovery | UNVERIFIABLE from Debian tidy 5.8.0 body-only XHTML probe alone |
| bare `html5` / `prettier` / `jsoup` as verified HTML toolchain | REJECTED (not used this leaf; different CLI) |
| bare `*.html` as XML identify fossil | REJECTED on XML leaf; **allowed here** as HTML peer fossil |
