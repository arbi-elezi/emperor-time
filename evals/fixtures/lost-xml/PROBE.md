# Boot probe — lost-xml / HELLO.xml

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~12:13 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **libxml2-utils** 2.12.7+dfsg+really2.9.14-2.1+deb13u3 (Debian trixie) |
| Binary | `/usr/bin/xmllint` |
| Reported | libxml version 20914 (`xmllint --version`) |
| Install | apt this leaf (101 kB archive; Installed-Size 181 kB / ~185 kB disk; libxml2 already on box; Worthy Spend after XSLT; still prefer over TeXlive / C++ / openjdk / graphviz multi-dep apt) |

Probe used `xmllint --xpath 'string(/probe)' HELLO.xml` on a minimal
well-formed XML document with a single text node under `/probe`.
Identify fossils use `*.xml` (XML peer leaf after XSLT; XSLT still owns
`*.xsl` / `*.xslt` only). Prefer `xmllint` / `libxml2` / `xml` / `.xml`.
Bare `xml` is **allowed** as a route tag (three-letter language abbreviation; word-boundary).
Bare `xmllint` is **allowed** as a route tag (tool binary name).
Bare `libxml2` is **allowed** as a route tag (library / family name).
Bare `.xml` is **allowed** with extension-boundary matching (does not invent
`.xmlrpc` / `.xmlfoo` prefix hits). XML document leaf after XSLT;
treats XML as peer fossil not house twin language. Do **not**
claim a full XSD / RelaxNG / Schematron / HTML suite recovery from a Debian
`xmllint` XPath string probe alone — this leaf pins `xmllint` well-formed
parse + XPath string evaluation.

## Commands (VERIFIED)

```text
$ which xmllint
/usr/bin/xmllint

$ xmllint --version
xmllint: using libxml version 20914
   compiled with: Threads Tree Output Push Reader Patterns Writer SAXv1 FTP HTTP DTDValid HTML Legacy C14N Catalog XPath XPointer XInclude Iconv ISO8859X Unicode Regexps Automata Schemas Schematron Modules Debug Zlib Lzma

$ xmllint --xpath 'string(/probe)' HELLO.xml
EMPEROR-TIME-XML-PROBE-OK

$ xmllint --noout HELLO.xml && echo WELLFORMED_OK
WELLFORMED_OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `xmllint --xpath 'string(/probe)' HELLO.xml` → probe string | VERIFIED |
| Filename culture (XSD / RelaxNG / HTML / DocBook) maps to this dialect | CONJECTURE (probe uses plain well-formed XML + XPath string) |
| Full XSD / RelaxNG / Schematron / HTML feature recovery | UNVERIFIABLE from Debian xmllint XPath string probe alone |
| bare `xmlstarlet` / `saxon` as verified XML toolchain | REJECTED (not used this leaf) |
| bare `*.xml` as XSLT identify fossil | REJECTED on XSLT leaf; **allowed here** as XML peer fossil |
