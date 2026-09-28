# Boot probe — lost-xsl / HELLO.xsl

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~12:00 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **xsltproc** 1.1.35-1.2+deb13u3 (Debian trixie) |
| Binary | `/usr/bin/xsltproc` |
| Reported | libxml 20914, libxslt 10135 (`xsltproc -V`) |
| Install | apt this leaf (115 kB archive; Installed-Size 151 kB; libxslt1.1 already on box; Worthy Spend after jq; still prefer over TeXlive / C++ / openjdk apt) |

Probe used `xsltproc HELLO.xsl HELLO.xml` on a minimal
XSLT 1.0 text-output stylesheet (`xsl:output method="text"`).
Identify fossils use `*.xsl` / `*.xslt` only (not bare `*.xml`). Prefer `xsltproc` /
`libxslt` / `xslt` / `.xsl` / `.xslt`.
Bare `xslt` is **allowed** as a route tag (language / tool family name; substring).
Bare `xsltproc` is **allowed** as a route tag (tool binary name).
Bare `.xsl` / `.xslt` are **allowed** with extension-boundary matching (`.xsl` does not
prefix-hit `.xslt` alone — both listed; neither invents `.xslfoo`). XML/XSLT leaf after jq;
treats XSLT as peer fossil not house twin language. Do **not**
claim a full Saxon / Xalan / MSXML / XSLT 2.0+ suite recovery from a Debian `xsltproc`
CLI probe alone — this leaf pins `xsltproc` stylesheet+xml evaluation
with text output.

## Commands (VERIFIED)

```text
$ which xsltproc
/usr/bin/xsltproc

$ xsltproc -V
Using libxml 20914, libxslt 10135 and libexslt 820
xsltproc was compiled against libxml 20914, libxslt 10135 and libexslt 820
libxslt 10135 was compiled against libxml 20914
libexslt 820 was compiled against libxml 20914

$ xsltproc HELLO.xsl HELLO.xml
EMPEROR-TIME-XSLT-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `xsltproc` on `HELLO.xsl` + `HELLO.xml` → probe string | VERIFIED |
| Filename culture (`.xslt` / XSLT 2.0+ / Saxon) maps to this dialect | CONJECTURE (probe uses plain XSLT 1.0 `.xsl` + companion XML) |
| Full Saxon / Xalan / MSXML / XSLT 2.0+ feature recovery | UNVERIFIABLE from Debian xsltproc (libxslt 1.1) CLI probe alone |
| bare `saxon` / `xalan` as verified XSLT toolchain | REJECTED (not used this leaf) |
| bare `*.xml` as XSLT identify fossil | REJECTED (too broad; every XML tree) |
