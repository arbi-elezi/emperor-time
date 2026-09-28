# Changelog

## 0.4.116

- Archaeology PDF / Poppler pdftotext-on-`.pdf` Jail pin: `evals/fixtures/lost-pdf/` + `references/archaeology-pdf-manual.md` (Poppler `pdftotext` 25.03.0 on HELLO.pdf → EMPEROR-TIME-PDF-PROBE-OK; zero new apt; LibreOffice/ghostscript/qpdf REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.pdf`; route tags `pdf` / `pdftotext` / `poppler` / `.pdf`; does not steal plain `*.ps` or `*.pptx` or `*.docx`
- Plugin, marketplace, and SKILL.md at 0.4.116

## 0.4.115

- Archaeology PPTX / stdlib zipfile-on-`.pptx` Jail pin: `evals/fixtures/lost-pptx/` + `references/archaeology-pptx-manual.md` (CPython stdlib `zipfile` on HELLO.pptx → EMPEROR-TIME-PPTX-PROBE-OK; zero new apt; Debian unzip/zip/LibreOffice REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.pptx`; route tags `pptx` / `pypptx` / `ooxml-pptx` / `.pptx`; does not steal plain `*.zip` or `*.docx` or `*.xlsx`
- Plugin, marketplace, and SKILL.md at 0.4.115

## 0.4.114

- Archaeology JSONL / stdlib json.loads-per-line-on-`.jsonl` Jail pin: `evals/fixtures/lost-jsonl/` + `references/archaeology-jsonl-manual.md` (CPython stdlib `json` on HELLO.jsonl → EMPEROR-TIME-JSONL-PROBE-OK; zero new apt; Debian jsonlint REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.jsonl`; route tags `jsonl` / `pyjsonl` / `ndjson` / `.jsonl`; does not steal plain `*.json`
- Plugin, marketplace, and SKILL.md at 0.4.114


## 0.4.113

- Archaeology TSV / stdlib csv.DictReader-on-`.tsv` (tab delimiter) Jail pin: `evals/fixtures/lost-tsv/` + `references/archaeology-tsv-manual.md` (CPython stdlib `csv` on HELLO.tsv → EMPEROR-TIME-TSV-PROBE-OK; zero new apt; Debian csvkit/miller/tsv-utils REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.tsv`; route tags `tsv` / `pytsv` / `tab-separated` / `.tsv`; does not steal plain `*.csv`
- Plugin, marketplace, and SKILL.md at 0.4.113

## 0.4.112

- Archaeology XLSX / stdlib zipfile-on-`.xlsx` Jail pin: `evals/fixtures/lost-xlsx/` + `references/archaeology-xlsx-manual.md` (CPython stdlib `zipfile` on HELLO.xlsx → EMPEROR-TIME-XLSX-PROBE-OK; zero new apt; Debian unzip/zip/LibreOffice/openpyxl/xlsxwriter REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.xlsx`; route tags `xlsx` / `pyxlsx` / `ooxml-excel` / `.xlsx`; does not steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk` or `*.docx`
- Plugin, marketplace, and SKILL.md at 0.4.112


## 0.4.111

- Archaeology DOCX / stdlib zipfile-on-`.docx` Jail pin: `evals/fixtures/lost-docx/` + `references/archaeology-docx-manual.md` (CPython stdlib `zipfile` on HELLO.docx → EMPEROR-TIME-DOCX-PROBE-OK; zero new apt; Debian unzip/zip/LibreOffice/pandoc REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.docx`; route tags `docx` / `pydocx` / `ooxml-word` / `.docx`; does not steal plain `*.zip` or `*.whl` or `*.jar` or `*.war` or `*.apk`
- Plugin, marketplace, and SKILL.md at 0.4.111


## 0.4.110

- Archaeology APK / stdlib zipfile-on-`.apk` Jail pin: `evals/fixtures/lost-apk/` + `references/archaeology-apk-manual.md` (CPython stdlib `zipfile` on HELLO.apk → EMPEROR-TIME-APK-PROBE-OK; zero new apt; Debian unzip/zip/android-sdk/aapt REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.apk`; route tags `apk` / `pyapk` / `android-package` / `.apk`; does not steal plain `*.zip` or `*.whl` or `*.jar` or `*.war`
- Plugin, marketplace, and SKILL.md at 0.4.110


## 0.4.109

- Archaeology WAR / stdlib zipfile-on-`.war` Jail pin: `evals/fixtures/lost-war/` + `references/archaeology-war-manual.md` (CPython stdlib `zipfile` on HELLO.war → EMPEROR-TIME-WAR-PROBE-OK; zero new apt; Debian unzip/zip/openjdk/tomcat REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.war`; route tags `war` / `pywar` / `web-archive` / `.war`; does not steal plain `*.zip` or `*.whl` or `*.jar`
- Plugin, marketplace, and SKILL.md at 0.4.109


## 0.4.108

- Archaeology JAR / stdlib zipfile-on-`.jar` Jail pin: `evals/fixtures/lost-jar/` + `references/archaeology-jar-manual.md` (CPython stdlib `zipfile` on HELLO.jar → EMPEROR-TIME-JAR-PROBE-OK; zero new apt; Debian unzip/zip/openjdk REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.jar`; route tags `jar` / `pyjar` / `java-archive` / `.jar`; does not steal plain `*.zip` or `*.whl`
- Plugin, marketplace, and SKILL.md at 0.4.108

## 0.4.107

- Archaeology wheel / stdlib zipfile-on-`.whl` Jail pin: `evals/fixtures/lost-whl/` + `references/archaeology-whl-manual.md` (CPython stdlib `zipfile` on HELLO.whl → EMPEROR-TIME-WHL-PROBE-OK; zero new apt; Debian unzip/zip REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.whl`; route tags `whl` / `pywhl` / `wheel` / `.whl`; does not steal plain `*.zip`
- Plugin, marketplace, and SKILL.md at 0.4.107

## 0.4.106

- Archaeology compressed-TAR / stdlib tarfile Jail pin: `evals/fixtures/lost-targz/` + `references/archaeology-targz-manual.md` (CPython stdlib `tarfile` `r:gz`/`r:bz2`/`r:xz` → EMPEROR-TIME-TARGZ-PROBE-OK; zero new apt; Debian tar/gzip/bzip2/xz-utils REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.tar.gz` / `*.tgz` / `*.tar.bz2` / `*.tar.xz`; route tags `targz` / `tarball` / `pytargz` / `.tar.gz` / `.tgz` / `.tar.bz2` / `.tar.xz`
- Plugin, marketplace, and SKILL.md at 0.4.106

## 0.4.105

- Archaeology gzip/stdlib gzip Jail pin: `evals/fixtures/lost-gz/` + `references/archaeology-gzip-manual.md` (CPython stdlib `gzip.open`/read → EMPEROR-TIME-GZIP-PROBE-OK; zero new apt; Debian gzip REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.gz`; route tags `gzip` / `pygzip` / `gzipfile` / `.gz`
- Plugin, marketplace, and SKILL.md at 0.4.105


## 0.4.104

- Archaeology tar/tarfile Jail pin: `evals/fixtures/lost-tar/` + `references/archaeology-tar-manual.md` (CPython stdlib `tarfile.open`/`getmembers`/`extractfile` → EMPEROR-TIME-TAR-PROBE-OK; zero new apt; Debian tar REJECTED as leaf owner)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.tar`; route tags `tar` / `pytar` / `tarfile` / `.tar`
- Plugin, marketplace, and SKILL.md at 0.4.104


## 0.4.103

- Archaeology zip/zipfile Jail pin: `evals/fixtures/lost-zip/` + `references/archaeology-zip-manual.md` (CPython stdlib `ZipFile.namelist`/`read` → EMPEROR-TIME-ZIP-PROBE-OK; zero new apt; unzip/zip REJECTED)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.zip`; route tags `zip` / `pyzip` / `zipfile` / `.zip`
- Plugin, marketplace, and SKILL.md at 0.4.103


## 0.4.102

- Archaeology eml/email.parser Jail pin: `evals/fixtures/lost-eml/` + `references/archaeology-eml-manual.md` (CPython stdlib `BytesParser.parsebytes` Subject → EMPEROR-TIME-EML-PROBE-OK; zero new apt; mailutils/mutt REJECTED)
- identify/route/eval/honesty/bakeoff/catalog lockstep; fossils `*.eml`; route tags `eml` / `pyemail` / `email.parser` / `.eml` (bare `email` refused)
- Plugin, marketplace, and SKILL.md at 0.4.102


## 0.4.101

- Archaeology plist leaf: `evals/fixtures/lost-plist/HELLO.plist` + identify smoke; CPython 3.13.5 stdlib `plistlib` boot probe VERIFIED (`plistlib.load` → `EMPEROR-TIME-PLIST-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.plist`; bare `plist` / `pyplist` / `plistlib` allowed as route tags; bare `.plist` allowed with extension-boundary matching; prefer `plist` / `pyplist` / `plistlib` / `.plist`; CPython stdlib already on box — **zero new Apt Worthy Spend** this leaf; Debian `libplist-utils` 2.6.0-2+b1 apt REJECTED (~68 kB archives with libplist-2.0-4; unnecessary vs stdlib); property-list leaf after INI; treats plist as peer fossil not house twin language; distinct from XML (`*.xml` / xmllint) and JSON (`*.json` / stdlib json); TeX/LaTeX still deferred; C++ still deferred; graphviz still deferred; `*.tsv` / `*.jsonl` still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-plist-manual.md` — Python plistlib.load
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the sixtieth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, YAML, TOML, HTML, CSV, JSON, and INI; route triggers gain `plist` / `pyplist` / `plistlib` / `.plist`; eval locks `*.plist` identify on lost-plist
- Plugin, marketplace, and SKILL.md at 0.4.101

## 0.4.100

- Archaeology INI leaf: `evals/fixtures/lost-ini/HELLO.ini` + identify smoke; CPython 3.13.5 stdlib `configparser` boot probe VERIFIED (`ConfigParser.read`/`get` → `EMPEROR-TIME-INI-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.ini`; bare `ini` / `pyini` / `configparser` allowed as route tags; bare `.ini` allowed with extension-boundary matching; prefer `ini` / `pyini` / `configparser` / `.ini`; CPython stdlib already on box — **zero new Apt Worthy Spend** this leaf; Debian `crudini` 0.9.6-1 apt REJECTED (~43 kB with python3-iniparse; unnecessary vs stdlib); INI config leaf after JSON; treats INI as peer fossil not house twin language; distinct from TOML (`*.toml` / tomlq) and JSON (`*.json` / stdlib json); TeX/LaTeX still deferred; C++ still deferred; graphviz still deferred; `*.tsv` / `*.jsonl` still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-ini-manual.md` — Python configparser ConfigParser.read/get
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-ninth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, YAML, TOML, HTML, CSV, and JSON; route triggers gain `ini` / `pyini` / `configparser` / `.ini`; eval locks `*.ini` identify on lost-ini
- Plugin, marketplace, and SKILL.md at 0.4.100

## 0.4.99

- Archaeology JSON leaf: `evals/fixtures/lost-json/HELLO.json` + identify smoke; CPython 3.13.5 stdlib `json` 2.0.9 boot probe VERIFIED (`json.load` → `EMPEROR-TIME-JSON-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.json`; bare `pyjson` / `json2.0` allowed as route tags; bare `json` refused (substring collision with jsonl/json5/jsonc); bare `.json` allowed with extension-boundary matching; prefer `pyjson` / `json2.0` / `.json`; CPython stdlib already on box — **zero new Apt Worthy Spend** this leaf; Debian `jsonlint` 1.11.0-2 apt REJECTED (~15 kB; unnecessary vs stdlib); JSON document leaf after CSV; treats JSON as peer fossil not house twin language; distinct from jq (`*.jq` filters) and JS (`.js` already bounds away from `.json`); TeX/LaTeX still deferred; C++ still deferred; graphviz still deferred; `*.tsv` still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-json-manual.md` — Python json module load
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-eighth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, YAML, TOML, HTML, and CSV; route triggers gain `pyjson` / `json2.0` / `.json`; eval locks `*.json` identify on lost-json
- Plugin, marketplace, and SKILL.md at 0.4.99

## 0.4.98

- Archaeology CSV leaf: `evals/fixtures/lost-csv/HELLO.csv` + identify smoke; CPython 3.13.5 stdlib `csv` 1.0 boot probe VERIFIED (`csv.DictReader` → `EMPEROR-TIME-CSV-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.csv`; bare `csv` / `pycsv` / `csv1.0` allowed as route tags; bare `.csv` allowed with extension-boundary matching; prefer `csv` / `pycsv` / `csv1.0` / `.csv`; CPython stdlib already on box — **zero new Apt Worthy Spend** this leaf; Debian `csvkit` 2.0.1-3 apt REJECTED (~10.6 MB archives / ~53 MB Installed-Size / 29 new packages); CSV tabular leaf after HTML; treats CSV as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; graphviz still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-csv-manual.md` — Python csv module DictReader
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-seventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, YAML, TOML, and HTML; route triggers gain `csv` / `pycsv` / `csv1.0` / `.csv`; eval locks `*.csv` identify on lost-csv
- Plugin, marketplace, and SKILL.md at 0.4.98

## 0.4.97

- Archaeology HTML leaf: `evals/fixtures/lost-html/HELLO.html` + identify smoke; HTML Tidy 5.8.0 boot probe VERIFIED (`tidy -q -utf8 --show-body-only yes -asxml HELLO.html` → body containing `EMPEROR-TIME-TIDY-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.html` / `*.htm`; bare `html` / `tidy` / `html-tidy` / `tidy5.8` allowed as route tags; bare `.html` / `.htm` allowed with extension-boundary matching (`.htm` does not prefix-hit `.html`); prefer `tidy` / `html-tidy` / `tidy5.8` / `html` / `.html` / `.htm`; Debian packages `tidy` 2:5.8.0-2 + `libtidy58` 2:5.8.0-2 apt-installed this leaf (~252 kB archives; Installed-Size sum ~1170 kB / ~1198 kB disk); HTML document leaf after XML/TOML; treats HTML as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; csvkit/CSV still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-html-manual.md` — HTML Tidy documentation Running Tidy in a Terminal (CLI …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-sixth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, YAML, and TOML; route triggers gain `tidy` / `html-tidy` / `tidy5.8` / `html` / `.html` / `.htm`; eval locks `*.html` identify on lost-html
- Plugin, marketplace, and SKILL.md at 0.4.97

## 0.4.96

- Archaeology TOML leaf: `evals/fixtures/lost-toml/HELLO.toml` + identify smoke; kislyuk/tomlq 3.4.3 boot probe VERIFIED (`tomlq -r .probe HELLO.toml` → `EMPEROR-TIME-TOMLQ-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.toml`; bare `toml` / `tomlq` / `kislyuk-tomlq` / `tomlq3.4` allowed as route tags; bare `.toml` allowed with extension-boundary matching; prefer `tomlq` / `kislyuk-tomlq` / `tomlq3.4` / `toml` / `.toml`; Debian `yq` 3.4.3-2 already on box from YAML leaf ships `/usr/bin/tomlq` — **zero new Apt Worthy Spend** this leaf; TOML document leaf after YAML; treats TOML as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; tidy/HTML still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-toml-manual.md` — yq documentation TOML support (tomlq …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-fifth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, XML, and YAML; route triggers gain `tomlq` / `kislyuk-tomlq` / `tomlq3.4` / `toml` / `.toml`; eval locks `*.toml` identify on lost-toml
- Plugin, marketplace, and SKILL.md at 0.4.96

## 0.4.95

- Archaeology YAML leaf: `evals/fixtures/lost-yaml/HELLO.yaml` + identify smoke; kislyuk/yq 3.4.3 boot probe VERIFIED (`yq -r .probe HELLO.yaml` → `EMPEROR-TIME-YQ-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.yaml` / `*.yml`; bare `yaml` / `yq` / `kislyuk-yq` / `yq3.4` allowed as route tags; bare `.yaml` / `.yml` allowed with extension-boundary matching; prefer `yq` / `kislyuk-yq` / `yq3.4` / `yaml` / `.yaml` / `.yml`; Debian package `yq` 3.4.3-2 apt-installed this leaf (~267 kB archive with python3-yaml siblings; Installed-Size sum ~1063 kB; jq already on box); YAML document leaf after jq/XML; treats YAML as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-yaml-manual.md` — yq documentation Synopsis (jq filter + YAML file …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-fourth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, XSLT, and XML; route triggers gain `yq` / `kislyuk-yq` / `yq3.4` / `yaml` / `.yaml` / `.yml`; eval locks `*.yaml` identify on lost-yaml
- Plugin, marketplace, and SKILL.md at 0.4.95

## 0.4.94

- Archaeology XML leaf: `evals/fixtures/lost-xml/HELLO.xml` + identify smoke; xmllint (libxml2 2.9.14) boot probe VERIFIED (`xmllint --xpath 'string(/probe)' HELLO.xml` → `EMPEROR-TIME-XML-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.xml` (XML peer after XSLT; XSLT still owns `*.xsl` / `*.xslt` only); bare `xml` / `xmllint` / `libxml2` allowed as route tags; bare `.xml` allowed with extension-boundary matching; prefer `xmllint` / `libxml2` / `xml` / `.xml`; Debian package `libxml2-utils` 2.12.7+dfsg+really2.9.14-2.1+deb13u3 apt-installed this leaf (101 kB archive; Installed-Size 181 kB; libxml2 already on box); XML document leaf after XSLT; treats XML as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-xml-manual.md` — xmllint(1) SYNOPSIS (XML-FILE + `--xpath` …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-third pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, jq, and XSLT; route triggers gain `xmllint` / `libxml2` / `xml` / `.xml`; eval locks `*.xml` identify on lost-xml
- Plugin, marketplace, and SKILL.md at 0.4.94

## 0.4.93

- Archaeology XSLT leaf: `evals/fixtures/lost-xsl/HELLO.xsl` + identify smoke; xsltproc 1.1.35 (libxslt) boot probe VERIFIED (`xsltproc HELLO.xsl HELLO.xml` → `EMPEROR-TIME-XSLT-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.xsl` / `*.xslt` only (not bare `*.xml`); bare `xslt` / `xsltproc` / `libxslt` allowed as route tags; bare `.xsl` / `.xslt` allowed with extension-boundary matching (`.xsl` does not alone prefix-hit `.xslt` — both listed); prefer `xsltproc` / `libxslt` / `xslt` / `.xsl` / `.xslt`; Debian package `xsltproc` 1.1.35-1.2+deb13u3 apt-installed this leaf (115 kB archive; Installed-Size 151 kB; libxslt1.1 already on box); XML/XSLT leaf after jq; treats XSLT as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-xslt-manual.md` — xsltproc(1) SYNOPSIS (stylesheet + XML-FILE …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-second pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, SQL/SQLite, and jq; route triggers gain `xsltproc` / `libxslt` / `xslt` / `.xsl` / `.xslt`; eval locks `*.xsl` identify on lost-xsl
- Plugin, marketplace, and SKILL.md at 0.4.93

## 0.4.92

- Archaeology jq leaf: `evals/fixtures/lost-jq/HELLO.jq` + identify smoke; jq 1.7 CLI boot probe VERIFIED (`jq -nr -f HELLO.jq` → `EMPEROR-TIME-JQ-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.jq` only; bare `jq` allowed as route tag (tool binary name; word-boundary); bare `.jq` allowed as route tag with extension-boundary matching (does not prefix-hit `.jquery`); prefer `jq` / `jq1.7` / `jqlang` / `.jq`; Debian package `jq` 1.7.1-6+deb13u4 already on box this leaf (Worthy Spend 0 B apt; Installed-Size 125 kB); JSON filter leaf after SQL; treats jq as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-jq-manual.md` — jq 1.7 Manual Invoking jq (`-f` / `--from-file` …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifty-first pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, PHP, and SQL/SQLite; route triggers gain `jq` / `jq1.7` / `jqlang` / `.jq`; eval locks `*.jq` identify on lost-jq
- Plugin, marketplace, and SKILL.md at 0.4.92

## 0.4.91

- Archaeology SQL/SQLite leaf: `evals/fixtures/lost-sql/HELLO.sql` + identify smoke; SQLite 3.46.1 CLI boot probe VERIFIED (`sqlite3 -batch :memory: ".read HELLO.sql"` → `EMPEROR-TIME-SQL-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.sql` only (no `*.sqlite` / `*.db` / `*.sqlite3` this leaf); bare `sql` allowed as route tag (three-letter language abbreviation; word-boundary); bare `sqlite` allowed as route tag (tool / language name; word-boundary); bare `.sql` allowed as route tag with extension-boundary matching (does not prefix-hit `.sqlite` / `.sqlite3` / `.sqlitedb`); prefer `sqlite` / `sqlite3` / `sqlite3.46` / `.sql`; Debian package `sqlite3` 3.46.1-7+deb13u2 apt-installed this leaf (~601 kB); SQL scripting leaf after PHP; treats SQLite SQL as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-sql-manual.md` — SQLite CLI §7.2 Reading SQL from a file (`.read` …)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fiftieth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, Bash, and PHP; route triggers gain `sqlite` / `sqlite3` / `sqlite3.46` / `sql` / `.sql`; eval locks `*.sql` identify on lost-sql
- Plugin, marketplace, and SKILL.md at 0.4.91

## 0.4.90

- Archaeology PHP leaf: `evals/fixtures/lost-php/HELLO.php` + identify smoke; PHP 8.4.26 (cli) boot probe VERIFIED (`php HELLO.php` → `EMPEROR-TIME-PHP-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.php` only (no `*.phtml` this leaf); bare `php` allowed as route tag (tool binary name; word-boundary); bare `.php` allowed as route tag with extension-boundary matching (does not prefix-hit `.php3` / `.php4` / `.php5` / `.phps`); prefer `php` / `php8` / `php8.4` / `php-cli` / `.php`; Debian packages `php-cli` 2:8.4+96 / `php8.4-cli` 8.4.26-1~deb13u1 apt-installed this leaf; scripting leaf after Bash; treats PHP as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-php-manual.md` — PHP Manual Executing PHP files (`php` … file)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-ninth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, TypeScript, and Bash; route triggers gain `php` / `php8` / `php8.4` / `php-cli` / `.php`; eval locks `*.php` identify on lost-php
- Plugin, marketplace, and SKILL.md at 0.4.90

## 0.4.89

- Archaeology Bash leaf: `evals/fixtures/lost-sh/HELLO.sh` + identify smoke; GNU Bash 5.2.37 boot probe VERIFIED (`bash HELLO.sh` → `EMPEROR-TIME-BASH-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.sh` only (no `*.bash` this leaf); bare `bash` allowed as route tag (tool binary name; word-boundary); bare `sh` refused as route tag (POSIX / dash ambiguity; verified toolchain is bash); bare `.sh` allowed as route tag with extension-boundary matching (does not prefix-hit `.sha` / `.shar` / `.shtml`); prefer `bash` / `bash5` / `bash5.2` / `gnu-bash` / `.sh`; Debian package `bash` 5.2.37-2+b10 already on box; shell-script leaf after TypeScript; treats Bash as peer fossil not house twin language; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-bash-manual.md` — bash(1) ARGUMENTS (`bash` … file)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-eighth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, Python, and TypeScript; route triggers gain `bash` / `bash5` / `bash5.2` / `gnu-bash` / `.sh`; bare `sh` refused; eval locks `*.sh` identify on lost-sh
- Plugin, marketplace, and SKILL.md at 0.4.89

## 0.4.88

- Archaeology TypeScript leaf: `evals/fixtures/lost-ts/HELLO.ts` + identify smoke; TypeScript 5.6.3 (`tsc`) + Node.js 20.19.2 boot probe VERIFIED (`tsc --target ES2020 --module commonjs HELLO.ts --outDir …` then `node …/HELLO.js` → `EMPEROR-TIME-TS-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.ts` only (no `*.tsx` this leaf); bare `ts` allowed as route tag (two-letter abbreviation; word-boundary); bare `.ts` allowed as route tag with extension-boundary matching (does not prefix-hit `.tsx` / `.tsbuildinfo` / `.mts` / `.cts`); prefer `typescript` / `typescript5` / `tsc` / `ts5` / `.ts`; npm-local `typescript` 5.6.3 provides real `tsc` (not bun; bun≠tsc); typed-compile after Python; TeX/LaTeX still deferred; C++ still deferred; CLIPS / embeddings still deferred
- Jail pin `references/archaeology-typescript-manual.md` — TypeScript Handbook tsc CLI Options / Using the CLI (`tsc index.ts`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-seventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, JavaScript, and Python; route triggers gain `typescript` / `typescript5` / `tsc` / `ts5` / `ts` / `.ts`; eval locks `*.ts` identify on lost-ts
- Plugin, marketplace, and SKILL.md at 0.4.88

## 0.4.87

- Archaeology Python leaf: `evals/fixtures/lost-py/HELLO.py` + identify smoke; Python 3.13.5 boot probe VERIFIED (`python3 HELLO.py` → `EMPEROR-TIME-PY-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.py` only; bare `python` refused as route tag (ET meta / house-tooling discourse collision); bare `py` allowed as route tag (two-letter abbreviation; word-boundary); bare `.py` allowed as route tag with extension-boundary matching (does not prefix-hit `.pyc` / `.pyo` / `.pyw` / `.pyx` / `.pyi`); prefer `python3` / `python3.13` / `cpython` / `.py`; Debian package `python3` 3.13.5-1 already on box; classic scripting / runtime after JavaScript; treats Python as peer fossil not house language; TeX/LaTeX still deferred; C++ still deferred; TypeScript still deferred
- Jail pin `references/archaeology-python-manual.md` — Python 3.13 Command line Synopsis (`python … script`) + print
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-sixth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, C, and JavaScript; route triggers gain `python3` / `python3.13` / `cpython` / `py` / `.py`; bare `python` refused; eval locks `*.py` identify on lost-py
- Plugin, marketplace, and SKILL.md at 0.4.87

## 0.4.86

- Archaeology JavaScript leaf: `evals/fixtures/lost-js/HELLO.js` + identify smoke; Node.js 20.19.2 boot probe VERIFIED (`node HELLO.js` → `EMPEROR-TIME-JS-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.js` only; bare `node` refused as route tag (common-English / tech collision); bare `js` allowed as route tag (two-letter abbreviation; word-boundary); bare `.js` allowed as route tag with extension-boundary matching (does not prefix-hit `.json` / `.jsx`); prefer `nodejs` / `node20` / `javascript` / `.js`; Debian package `nodejs` 20.19.2+dfsg-1+deb13u3 already on box; classic scripting / runtime after C; TeX/LaTeX still deferred; C++ still deferred
- Jail pin `references/archaeology-js-manual.md` — Node.js Command-line API Synopsis (`node … script.js`) + console.log
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-fifth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, Rust, and C; route triggers gain `nodejs` / `node20` / `javascript` / `js` / `.js`; bare `node` refused; eval locks `*.js` identify on lost-js
- Plugin, marketplace, and SKILL.md at 0.4.86

## 0.4.85

- Archaeology C leaf: `evals/fixtures/lost-c/HELLO.c` + identify smoke; GCC 14.2.0 boot probe VERIFIED (`gcc HELLO.c -o HELLO` → `./HELLO` → `EMPEROR-TIME-C-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.c` only; bare `c` refused as route tag (single-letter / common-English collision); bare `.c` allowed as route tag with extension-boundary matching (does not prefix-hit `.cbl` / `.cl`); prefer `gcc` / `gcc14` / `c11` / `.c`; Debian packages `gcc` 4:14.2.0-1 / `gcc-14` 14.2.0-19 already on box; systems compile-and-run after Rust; TeX/LaTeX still deferred
- Jail pin `references/archaeology-c-manual.md` — GCC Overall Options (`file.c` / `-o file`) + puts
- Route extension match: suffixes now require non-alnum/end after the pattern so `.c` cannot prefix-hit `.cbl` / `.cl` (honesty for short extensions)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-fourth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, Go, and Rust; route triggers gain `gcc` / `gcc14` / `c11` / `.c`; eval locks `*.c` identify on lost-c
- Plugin, marketplace, and SKILL.md at 0.4.85

## 0.4.84

- Archaeology Rust leaf: `evals/fixtures/lost-rust/HELLO.rs` + identify smoke; rustc 1.85.1 boot probe VERIFIED (`rustc HELLO.rs` → `./HELLO` → `EMPEROR-TIME-RUST-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.rs` only; bare `rust` allowed as route tag (language name; word-boundary); bare `.rs` allowed as route tag (no known peer excavate substring collision); prefer `rust` / `rustc` / `rust1.85` / `.rs`; Debian package `rustc` 1.85.1+dfsg1-1+deb13u1 already on box; systems compile-and-run after Go; TeX/LaTeX still deferred
- Jail pin `references/archaeology-rust-manual.md` — rustc Basic usage (`rustc FILE`) + println!
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-third pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, Ruby, and Go; route triggers gain `rust` / `rustc` / `rust1.85` / `.rs`; eval locks `*.rs` identify on lost-rust
- Plugin, marketplace, and SKILL.md at 0.4.84

## 0.4.83

- Archaeology Go leaf: `evals/fixtures/lost-go/HELLO.go` + identify smoke; Go 1.24.4 boot probe VERIFIED (`go run HELLO.go` → `EMPEROR-TIME-GO-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.go` only; bare `go` refused as route tag (common-English collision); bare `.go` allowed as route tag (no known peer excavate substring collision); prefer `golang` / `go1.24` / `.go`; Debian packages `golang-go` 2:1.24~2 / `golang-1.24-go` 1.24.4-1 already on box; systems compile-and-run after Ruby; TeX/LaTeX still deferred
- Jail pin `references/archaeology-go-manual.md` — cmd/go Compile and run (`go run`) + fmt.Println
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-second pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, Lua, and Ruby; route triggers gain `golang` / `go1.24` / `.go`; eval locks `*.go` identify on lost-go
- Plugin, marketplace, and SKILL.md at 0.4.83

## 0.4.82

- Archaeology Ruby leaf: `evals/fixtures/lost-ruby/HELLO.RB` + identify smoke; Ruby 3.3.8 boot probe VERIFIED (`ruby HELLO.RB` → `EMPEROR-TIME-RUBY-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.rb` only; bare `ruby` allowed as route tag (tool binary name; word-boundary); bare `.rb` allowed as route tag (no known peer excavate substring collision); Debian package `ruby` 1:3.3+b1 (Depends `ruby3.3`); classic scripting after Lua
- Jail pin `references/archaeology-ruby-manual.md` — ruby3.3(1) SYNOPSIS program_file + DESCRIPTION interpretive scripting + puts
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the forty-first pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, Expect, and Lua; route triggers gain `ruby` / `ruby3.3` / `.rb`; eval locks `*.rb` identify on lost-ruby
- Plugin, marketplace, and SKILL.md at 0.4.82

## 0.4.81

- Archaeology Lua leaf: `evals/fixtures/lost-lua/HELLO.LUA` + identify smoke; Lua 5.4.7 boot probe VERIFIED (`lua HELLO.LUA` → `EMPEROR-TIME-LUA-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.lua` only; bare `lua` allowed as route tag (tool binary name; word-boundary); bare `.lua` allowed as route tag (no known peer excavate substring collision); Debian package `lua5.4` (provides `lua` via alternatives); classic embeddable scripting after Expect
- Jail pin `references/archaeology-lua-manual.md` — lua(1) SYNOPSIS script + DESCRIPTION script-file evaluation + print
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fortieth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, bc, and Expect; route triggers gain `lua` / `lua5.4` / `.lua`; eval locks `*.lua` identify on lost-lua
- Plugin, marketplace, and SKILL.md at 0.4.81

## 0.4.80

- Archaeology Expect leaf: `evals/fixtures/lost-expect/HELLO.EXP` + identify smoke; Expect 5.45.4 boot probe VERIFIED (`expect HELLO.EXP` → `EMPEROR-TIME-EXPECT-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.exp` only; bare `expect` allowed as route tag (tool binary name; word-boundary); bare `.exp` allowed as route tag (no known peer excavate substring collision); companion to Tcl leaf (Expect sits on Tcl / Don Libes); Debian packages `expect` + `tcl-expect`
- Jail pin `references/archaeology-expect-manual.md` — Expect SYNOPSIS cmdfile + USAGE script-file evaluation + COMMANDS exit / Tcl puts
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-ninth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, Perl, and bc; route triggers gain `expect` / `tcl-expect` / `.exp`; eval locks `*.exp` identify on lost-expect
- Plugin, marketplace, and SKILL.md at 0.4.80

## 0.4.79

- Archaeology bc leaf: `evals/fixtures/lost-bc/HELLO.BC` + identify smoke; GNU bc 1.07.1 boot probe VERIFIED (`bc HELLO.BC` / `bc -q HELLO.BC` → `EMPEROR-TIME-BC-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.bc` only; bare `bc` allowed as route tag (tool binary name; word-boundary); bare `.bc` refused as route tag (substring collision with BCPL `.bcpl`); companion to dc leaf (GNU bc/dc family); deferred earlier on apt 500, now installed
- Jail pin `references/archaeology-bc-manual.md` — GNU bc DESCRIPTION file arguments + STATEMENTS `print` + PSEUDO STATEMENTS `quit`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-eighth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, roff, and Perl; route triggers gain `bc` / `gnu-bc`; eval locks `*.bc` identify on lost-bc
- Plugin, marketplace, and SKILL.md at 0.4.79

## 0.4.78

- Archaeology Perl leaf: `evals/fixtures/lost-pl/HELLO.PL` + identify smoke; Perl 5.40.1 boot probe VERIFIED (`perl HELLO.PL` → `EMPEROR-TIME-PERL-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.pl` / `*.pm`; bare `perl` allowed as route tag (tool binary name); bare `.pl` refused as route tag (substring collision with PL/I `.pli` / `.pl1`); Prolog already left `*.pl` alone for this reclaim
- Jail pin `references/archaeology-perl-manual.md` — Perl perlrun(1) SYNOPSIS programfile + DESCRIPTION file-on-command-line
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-seventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, yacc, and roff; route triggers gain `perl` / `perl5` / `.pm`; eval locks `*.pl` identify on lost-pl
- Plugin, marketplace, and SKILL.md at 0.4.78

## 0.4.77

- Archaeology roff leaf: `evals/fixtures/lost-roff/HELLO.ROFF` + identify smoke; GNU groff 1.23.0 boot probe VERIFIED (`groff -Tascii HELLO.ROFF` → `EMPEROR-TIME-ROFF-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.roff` only; bare `roff` / `nroff` / `groff` allowed as route tags (tool binary names)
- Jail pin `references/archaeology-roff-manual.md` — GNU groff groff(1) SYNOPSIS file operands + Options `-T` / output-device
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-sixth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, lex, and yacc; route triggers gain `roff` / `nroff` / `groff` / `gnu-groff` / `.roff`; eval locks `*.roff` identify on lost-roff
- Plugin, marketplace, and SKILL.md at 0.4.77

## 0.4.76

- Jail pin `references/archaeology-yacc-manual.md` — GNU Bison bison(1) SYNOPSIS FILE arguments + Output Files `-o` / `--output`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-fifth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, dc, and lex; route triggers gain `yacc` / `bison` / `gnu-bison` / `.y`; eval locks `*.y` identify on lost-yacc
- Plugin, marketplace, and SKILL.md at 0.4.76

## 0.4.75
- Archaeology lex leaf: `evals/fixtures/lost-lex/HELLO.L` + identify smoke; GNU flex 2.6.4 boot probe VERIFIED (`flex HELLO.L` → `lex.yy.c` → `gcc -o hello lex.yy.c -lfl` / `flex -o hello.c HELLO.L` → `EMPEROR-TIME-LEX-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.l` / `*.lex`; bare `lex` / `flex` allowed as route tags (tool binary names); bare `.l` refused (short-extension collision with `.lisp`)
- Jail pin `references/archaeology-lex-manual.md` — GNU flex flex(1) SYNOPSIS FILE arguments + FILES `-o` / `--outfile`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-fourth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, Make, and dc; route triggers gain `lex` / `flex` / `gnu-flex` / `.lex`; eval locks `*.l` identify on lost-lex
- Plugin, marketplace, and SKILL.md at 0.4.75

## 0.4.74
- Archaeology dc leaf: `evals/fixtures/lost-dc/HELLO.DC` + identify smoke; GNU dc 1.4.1 (GNU bc 1.07.1) boot probe VERIFIED (`dc -f HELLO.DC` / `dc HELLO.DC` → `EMPEROR-TIME-DC-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.dc` only; bare `dc` allowed as route tag (tool binary name)
- Jail pin `references/archaeology-dc-manual.md` — GNU dc dc(1) DESCRIPTION file arguments + OPTIONS `-f` / `--file`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-third pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, ed, and Make; route triggers gain `dc` / `gnu-dc` / `.dc`; eval locks `*.dc` identify on lost-dc
- Plugin, marketplace, and SKILL.md at 0.4.74

## 0.4.73
- Archaeology Make leaf: `evals/fixtures/lost-make/Makefile` + `HELLO.MK` + identify smoke; GNU Make 4.4.1 boot probe VERIFIED (`make -C lost-make` / `make -f HELLO.MK` → `EMPEROR-TIME-MAKE-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `Makefile` / `makefile` / `*.mak` / `*.mk`; bare English `make` refused as route tag (factory / common-English collision with "make software")
- Jail pin `references/archaeology-make-manual.md` — GNU Make make(1) DESCRIPTION default-name search + OPTIONS `-f` / `--file` / `--makefile`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-second pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, m4, and ed; route triggers gain `gmake` / `gnu-make` / `.mk` / `.mak` / `makefile` (bare `make` refused); eval locks Makefile identify on lost-make
- Plugin, marketplace, and SKILL.md at 0.4.73

## 0.4.72
- Archaeology ed leaf: `evals/fixtures/lost-ed/HELLO.ED` + identify smoke; GNU ed 1.21.1 boot probe VERIFIED (`ed -s < HELLO.ED` → `EMPEROR-TIME-ED-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.ed` only; bare `ed` allowed as route tag (tool binary name — not English collision)
- Jail pin `references/archaeology-ed-manual.md` — GNU ed Invoking ed / `-s` / `--script`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirty-first pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, sed, and m4; route triggers gain `ed` / `gnu-ed` / `.ed`; eval locks `*.ed` identify on lost-ed
- Plugin, marketplace, and SKILL.md at 0.4.72

## 0.4.71
- Archaeology m4 leaf: `evals/fixtures/lost-m4/HELLO.M4` + identify smoke; GNU M4 1.4.19 boot probe VERIFIED (`m4 HELLO.M4` → `EMPEROR-TIME-M4-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.m4` only; bare `m4` allowed as route tag (tool binary name — not English collision)
- Jail pin `references/archaeology-m4-manual.md` — GNU M4 Invoking m4 / Command line files (FILE args)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirtieth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, AWK, and sed; route triggers gain `m4` / `gm4` / `.m4`; eval locks `*.m4` identify on lost-m4
- Plugin, marketplace, and SKILL.md at 0.4.71

## 0.4.70
- Archaeology sed leaf: `evals/fixtures/lost-sed/HELLO.SED` + identify smoke; GNU sed 4.9 boot probe VERIFIED (`sed -f HELLO.SED` → `EMPEROR-TIME-SED-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.sed` only; bare `sed` allowed as route tag (POSIX / tool binary name — not English collision)
- Jail pin `references/archaeology-sed-manual.md` — GNU sed Command-Line Options / `-f` / `--file=script-file`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-ninth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, Scheme, and AWK; route triggers gain `sed` / `gsed` / `.sed`; eval locks `*.sed` identify on lost-sed
- Plugin, marketplace, and SKILL.md at 0.4.70

## 0.4.69
- Archaeology AWK leaf: `evals/fixtures/lost-awk/HELLO.AWK` + identify smoke; GNU Awk 5.2.1 boot probe VERIFIED (`gawk -f HELLO.AWK` → `EMPEROR-TIME-AWK-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.awk` only; bare `awk` allowed as route tag (POSIX / tool binary name — not English collision)
- Jail pin `references/archaeology-awk-manual.md` — GAWK Effective AWK Programming Command-Line Options / `-f` / `--file source-file`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-eighth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, BASIC, and Scheme; route triggers gain `gawk` / `awk` / `nawk` / `.awk`; eval locks `*.awk` identify on lost-awk
- Plugin, marketplace, and SKILL.md at 0.4.69

## 0.4.68
- Archaeology Scheme leaf: `evals/fixtures/lost-scm/HELLO.SCM` + identify smoke; CHICKEN 5.3.0 boot probe VERIFIED (`csi -s HELLO.SCM` → `EMPEROR-TIME-SCM-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.scm` only; bare English `scheme` refused as route tag (common-English collision)
- Jail pin `references/archaeology-scheme-manual.md` — CHICKEN User's Manual Using the interpreter / csi `-s` / `-script PATHNAME`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-seventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, PostScript, and BASIC; route triggers gain `csi` / `chicken` / `chicken-scheme` / `.scm` (bare English `scheme` refused); eval locks `*.scm` identify on lost-scm
- Plugin, marketplace, and SKILL.md at 0.4.68

## 0.4.67
- Archaeology BASIC leaf: `evals/fixtures/lost-bas/HELLO.BAS` + identify smoke; Bywater BASIC 2.20pl2 boot probe VERIFIED (`bwbasic HELLO.BAS` → `EMPEROR-TIME-BAS-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.bas` only; bare English `basic` refused as route tag (common-English collision); bare `print` refused as route tag (cross-dialect keyword)
- Jail pin `references/archaeology-basic-manual.md` — bwbasic(1) §4.d Command-Line Execution / `bwbasic prog.bas`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-sixth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, Smalltalk, and PostScript; route triggers gain `bwbasic` / `bywater` / `.bas` (bare English `basic` refused); eval locks `*.bas` identify on lost-bas
- Plugin, marketplace, and SKILL.md at 0.4.67

## 0.4.66
- Archaeology PostScript leaf: `evals/fixtures/lost-ps/HELLO.PS` + identify smoke; GPL Ghostscript 10.05.1 boot probe VERIFIED (`gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage HELLO.PS` → `EMPEROR-TIME-PS-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.ps` + `*.eps`; bare `.ps` refused as route tag (short-extension collision with `.ps1`); bare `gs` refused as route tag (two-letter collision)
- Jail pin `references/archaeology-postscript-manual.md` — Ghostscript User Guide Invoking Ghostscript / `gs [options] {filename …}`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-fifth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, PL/I, and Smalltalk; route triggers gain `ghostscript` / `postscript` (bare `.ps` and bare `gs` refused); eval locks `*.ps` identify on lost-ps
- Plugin, marketplace, and SKILL.md at 0.4.66

## 0.4.65
- Archaeology Smalltalk leaf: `evals/fixtures/lost-st/HELLO.ST` + identify smoke; GNU Smalltalk 3.2.5 boot probe VERIFIED (`./gst -q HELLO.ST` → `EMPEROR-TIME-ST-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.st` only; bare `.st` refused as route tag (short-extension collision)
- Jail pin `references/archaeology-smalltalk-manual.md` — GNU Smalltalk User's Guide Invocation / `gst [ flags … ] [ file … ]`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-fourth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, BCPL, and PL/I; route triggers gain `gst` / `smalltalk` / `gnu-smalltalk` (bare English keyword tags and bare `.st` refused); eval locks `*.st` identify on lost-st
- Plugin, marketplace, and SKILL.md at 0.4.65

## 0.4.64
- Archaeology PL/I leaf: `evals/fixtures/lost-pli/HELLO.PLI` + identify smoke; Iron Spring PL/I 1.4.1 (15 Apr 2026) boot probe VERIFIED (`plic -C -lixg -ew HELLO.PLI -o hello.o` + `ld … -lprf` + `./hello` → `EMPEROR-TIME-PLI-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.pli` + `*.pl1`
- Jail pin `references/archaeology-pli-manual.md` — Iron Spring Programming Guide Running the Compiler / `plic` `-C` + readme_linux SA_make `ld … -lprf`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-third pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, APL, and BCPL; route triggers gain `plic` / `pli` / `pl1` / `iron-spring` / `.pli` / `.pl1` (bare English keyword tags refused); eval locks `*.pli` identify on lost-pli
- Plugin, marketplace, and SKILL.md at 0.4.64

## 0.4.63
- Archaeology BCPL leaf: `evals/fixtures/lost-bcpl/HELLO.B` + identify smoke; Martin Richards BCPL 32-bit Cintcode (16 May 2026 / compiler 18 Apr 2026) boot probe VERIFIED (`cintsys -q -c 'bcpl hello.b to hello; hello'` → `EMPEROR-TIME-BCPL-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.b` + `*.bcpl`; bare `.b` refused as route tag (short-extension collision)
- Jail pin `references/archaeology-bcpl-manual.md` — Martin Richards `cintsys` Valid arguments `-c args` / README `bcpl <file.b> to <dest>`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-second pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, Simula, and APL; route triggers gain `bcpl` / `cintsys` / `cintcode` / `.bcpl` (bare English keyword tags and bare `.b` refused); eval locks `*.b` identify on lost-bcpl

## 0.4.62
- Archaeology APL leaf: `evals/fixtures/lost-apl/HELLO.APL` + identify smoke; GNU APL 2.0 (source build, `--with-optional_libs=no`) boot probe VERIFIED (`apl -s --OFF -f HELLO.APL` → `EMPEROR-TIME-APL-PROBE-OK`); prebuilt `apl_2.0-1_amd64.deb` needs `libgsl.so.27` (trixie has `libgsl28`) so UNVERIFIABLE here; dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.apl` only
- Jail pin `references/archaeology-apl-manual.md` — GNU APL `apl(1)` SYNOPSIS (`apl [options]`) / OPTIONS `-f file`
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twenty-first pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, SNOBOL4, and Simula; route triggers gain `apl` / `gnu-apl` / `.apl` (bare English keyword tags refused); eval locks `*.apl` identify on lost-apl
- Plugin, marketplace, and SKILL.md at 0.4.62

## 0.4.61
- Archaeology Simula leaf: `evals/fixtures/lost-cim/HELLO.SIM` + identify smoke; Portable Simula 2.0 (Setup R21) / Temurin JDK 21 boot probe VERIFIED (`java -jar simula.jar … HELLO.SIM` → `EMPEROR-TIME-CIM-PROBE-OK`); GNU Cim 3.37 built but segfaults here (UNVERIFIABLE); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.sim` only
- Jail pin `references/archaeology-simula-manual.md` — Portable Simula Usage synopsis (`java -jar simula.jar [options] sourceFile`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twentieth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, Oberon, and SNOBOL4; route triggers gain `cim` / `simula` / `.sim` (bare English `begin` / `outtext` / `outimage` refused); eval locks `*.sim` identify on lost-cim
- Plugin, marketplace, and SKILL.md at 0.4.61

## 0.4.60
- Archaeology SNOBOL4 leaf: `evals/fixtures/lost-sno/HELLO.SNO` + identify smoke; CSNOBOL4B 2.3.4 boot probe VERIFIED (`snobol4 -b HELLO.SNO` → `EMPEROR-TIME-SNO-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.sno` only
- Jail pin `references/archaeology-snobol-manual.md` — CSNOBOL4 snobol4cmd(1) SYNOPSIS (`snobol4 [ options ... ] [ file ... ]`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the nineteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, Icon, and Oberon; route triggers gain `snobol4` / `snobol` / `csnobol4` / `.sno` (bare English `output` refused); eval locks `*.sno` identify on lost-sno
- Plugin, marketplace, and SKILL.md at 0.4.60


## 0.4.59
- Archaeology Oberon leaf: `evals/fixtures/lost-obn/HELLO.OBN` + identify smoke; Vishap Oberon voc 2.1.0 boot probe VERIFIED (`voc -M HELLO.OBN` → `EMPEROR-TIME-OBN-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.obn` only (not `*.mod` / `*.Mod` — Modula-2 leaf)
- Jail pin `references/archaeology-oberon-manual.md` — Vishap Compiling Main module (`voc` `-m` / `-M`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the eighteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, Algol W, and Icon; route triggers gain `voc` / `oberon` / `oberon-2` / `oberon2` / `.obn` (bare English `module` refused); eval locks `*.obn` identify on lost-obn
- Plugin, marketplace, and SKILL.md at 0.4.59


## 0.4.58
- Archaeology Icon leaf: `evals/fixtures/lost-icn/HELLO.ICN` + identify smoke; Icon 9.5.24b boot probe VERIFIED (`ln -sf HELLO.ICN hello.icn` then `icont -s hello.icn` → `EMPEROR-TIME-ICN-PROBE-OK`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.icn` only
- Jail pin `references/archaeology-icon-manual.md` — Icon 9 UNIX Manual Page (IPD244d) SYNOPSIS / File Names (`icont` + `.icn`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the seventeenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, ALGOL 60, and Algol W; route triggers gain `icont` / `iconx` / `.icn` (bare English `icon` / `write` refused); eval locks `*.icn` identify on lost-icn
- Plugin, marketplace, and SKILL.md at 0.4.58


## 0.4.57
- Archaeology Algol W leaf: `evals/fixtures/lost-alw/HELLO.ALW` + identify smoke; Awe 2026-05 boot probe VERIFIED (`awe HELLO.ALW -o HELLO`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.alw` only (not `*.a60` / `*.a68` / `*.alg`)
- Jail pin `references/archaeology-algolw-manual.md` — Awe SYNOPSIS / EXAMPLES `WRITE` (`awe source.alw... [-o executable]`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the sixteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, Algol 68, and ALGOL 60; route triggers gain `awe` / `algolw` / `algol-w` / `.alw` / space-intent `algol w` (bare English `write` refused); eval locks `*.alw` identify on lost-alw
- Plugin, marketplace, and SKILL.md at 0.4.57

## 0.4.56
- Archaeology ALGOL 60 leaf: `evals/fixtures/lost-a60/HELLO.A60` + identify smoke; GNU MARST 2.8 boot probe VERIFIED (`marst HELLO.A60` → `gcc -lalgol -lm`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.a60` (not `*.alg` — Algol 68 leaf)
- Jail pin `references/archaeology-algol60-manual.md` — GNU MARST Usage Example / `outstring` (`marst … -o …` / `gcc … -lalgol -lm`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fifteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, Modula-2, and Algol 68; route triggers gain `marst` / `algol60` / `.a60` / space-intent `algol 60` (bare English `outstring` refused); eval locks `*.a60` identify on lost-a60
- Plugin, marketplace, and SKILL.md at 0.4.56

## 0.4.55
- Archaeology Algol 68 leaf: `evals/fixtures/lost-a68/HELLO.A68` + identify smoke; Algol 68 Genie 3.1.2 boot probe VERIFIED (`a68g HELLO.A68`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.a68` / `*.alg`
- Jail pin `references/archaeology-algol68-manual.md` — Algol 68 Genie Synopsis / Transput `print` (`a68g [option | file] ...`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the fourteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, REXX, and Modula-2; route triggers gain `a68g` / `algol68g` / `algol68` / `.a68` / `.alg` (space-padded `algol`; bare English `print` refused); eval locks `*.a68` identify on lost-a68
- Plugin, marketplace, and SKILL.md at 0.4.55

## 0.4.54
- Archaeology Modula-2 leaf: `evals/fixtures/lost-mod/HELLO.MOD` + identify smoke; GNU Modula-2 14.2.0 boot probe VERIFIED (`gm2 -g -x modula-2 HELLO.MOD`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.mod` / `*.def`
- Jail pin `references/archaeology-modula2-manual.md` — GNU Modula-2 Example compile and link (`WriteString` / `gm2 -g hello.mod`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the thirteenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, Erlang, and REXX; route triggers gain `gm2` / `modula-2` / `modula2` / `.mod` / `.def` (space-padded `modula`; bare token `mod` refused); eval locks `*.mod` identify on lost-mod
- Plugin, marketplace, and SKILL.md at 0.4.54

## 0.4.53
- Archaeology REXX leaf: `evals/fixtures/lost-rex/HELLO.REX` + identify smoke; Regina 3.9.5 boot probe VERIFIED (`rexx HELLO.REX`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.rex` / `*.rexx`
- Jail pin `references/archaeology-rexx-manual.md` — Classic Rexx `SAY` (default output stream)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the twelfth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, Tcl, and Erlang; route triggers gain `regina` / `.rex` / `.rexx` (space-padded `rexx`; bare English `say` refused); eval locks `*.rex` identify on lost-rex
- Plugin, marketplace, and SKILL.md at 0.4.53

## 0.4.52
- Archaeology Erlang leaf: `evals/fixtures/lost-erl/HELLO.ERL` + identify smoke; OTP 27 boot probe VERIFIED (`escript HELLO.ERL`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.erl` / `*.hrl`
- Jail pin `references/archaeology-erlang-manual.md` — escript `main/1` (batch / application file run)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the eleventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, Prolog, and Tcl; route triggers gain `escript` / `erlc` / `.erl` / `.hrl` (space-padded `erlang`; bare `erl` tag word-bounded so Perl does not collide); eval locks `*.erl` identify on lost-erl
- Plugin, marketplace, and SKILL.md at 0.4.52

## 0.4.51
- Archaeology Tcl leaf: `evals/fixtures/lost-tcl/HELLO.TCL` + identify smoke; Tcl 8.6.16 boot probe VERIFIED (`tclsh HELLO.TCL`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.tcl` / `*.tk`
- Jail pin `references/archaeology-tcl-manual.md` — tclsh SCRIPT FILES (batch / application file run)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the tenth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, Common Lisp, and Prolog; route triggers gain `tclsh` / `.tcl` / `.tk` (space-padded `tcl`); eval locks `*.tcl` identify on lost-tcl
- Plugin, marketplace, and SKILL.md at 0.4.51


## 0.4.50
- Archaeology Prolog leaf: `evals/fixtures/lost-prolog/HELLO.PRO` + identify smoke; SWI-Prolog 9.2.9 boot probe VERIFIED (`swipl -q -t halt`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due); identify fossils `*.pro` / `*.prolog` only (no `*.pl` — Perl collision)
- Jail pin `references/archaeology-prolog-manual.md` — SWI-Prolog `initialization/2` main role (batch / application file run)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the ninth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, Forth, and Common Lisp; route triggers gain `swipl` / `gprolog` / `.pro` / `.prolog` (space-padded `prolog` to avoid bare substring); eval locks `*.pro` identify on lost-prolog
- Plugin, marketplace, and SKILL.md at 0.4.50

## 0.4.49
- Archaeology Common Lisp leaf: `evals/fixtures/lost-lisp/HELLO.LISP` + identify smoke; GNU CLISP 2.49.95+ boot probe VERIFIED (`clisp -q -norc`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-lisp-manual.md` — CLISP Non-Interactive (Batch) Mode (`_lisp-file_` / `-x`)
- Catalog + SKILL.md + archaeology.md + language-agnostic.md link the eighth pin alongside Pascal, ASM, COBOL, Fortran, VHDL, Ada, and Forth; route triggers gain `clisp` / `sbcl` / `.lisp` / `.lsp` / `.cl` (space-padded `lisp` to avoid `ellipsis` substring); eval locks `*.lisp` identify on lost-lisp
- Plugin, marketplace, and SKILL.md at 0.4.49

## 0.4.48
- Archaeology Forth leaf: `evals/fixtures/lost-fs/HELLO.FS` + identify smoke; pForth V2.0.0 boot probe VERIFIED (`pforth -q`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-forth-manual.md` — pForth README How to Run (INCLUDE / `pforth myprogram.fth`)
- Catalog + SKILL.md + archaeology.md link the seventh pin alongside Pascal, ASM, COBOL, Fortran, VHDL, and Ada; route triggers gain `pforth` / `gforth` / `.fs` / `.fth` / `.4th` (space-padded `forth` to avoid `fortran` substring); eval locks `*.fs` identify on lost-fs
- Plugin, marketplace, and SKILL.md at 0.4.48

## 0.4.47
- Skill-discovery (SDO) HARD-GATE leaf: `scripts/lib/sdo.py` prints SDO / PRIN / GATE / MUST card (Description = When to Use, NOT What the Skill Does)
- Thin `sdo.sh` / `sdo.ps1`; emperor peers gain `sdo`; `--reject-workflow-summary` / `--reject-no-trigger` HARD-GATEs; `--check-description` validator (Use when / trigger signals, reject workflow-summary tokens)
- Chain Jail leaf `chains/chain-jail/skill-discovery.md` + `references/skill-discovery.md` cite obra/superpowers writing-skills SKILL.md SDO heading (URL + 2026-09-27 + sha256)
- Route/triggers → emperor-capture; bakeoff + honesty inventory; companion wiring on authoring-checklist / extract-aspect / capture / catalog; plugin/marketplace/SKILL lockstep 0.4.47

## 0.4.46
- Persuasion-principles HARD-GATE leaf: `scripts/lib/persuasion.py` prints PERSUADE / PRIN / GATE / MUST card (Authority / Commitment / Scarcity / Social Proof / Unity / Reciprocity / Liking)
- Thin `persuasion.sh` / `persuasion.ps1`; emperor peers gain `persuasion`; `--reject-hedge` / `--reject-optional` HARD-GATEs; `--check-persuasion` validator (authority + commitment plus scarcity / social-proof / unity signals)
- Skill leaf `chains/chain-jail/persuasion-principles.md` + `references/persuasion-principles.md` cite obra/superpowers writing-skills persuasion-principles.md (URL + 2026-09-27 + sha256); Chain Jail extract-aspect + authoring companion + capture SKILL + catalog lockstep
- Route/triggers → emperor-capture; bakeoff + honesty inventory; plugin/marketplace/SKILL at 0.4.46

## 0.4.45
- Testing-skills HARD-GATE leaf: `scripts/lib/skill_test.py` prints SKILLTEST / PRIN / GATE / MUST card (combined pressure / watch baseline fail / verbatim rationalizations / explicit negation / stay green)
- Thin `skill-test.sh` / `skill-test.ps1`; emperor peers gain `skill-test`; `--reject-academic-only` / `--reject-skip-red` HARD-GATEs; `--check-pressure-baseline` validator (combined-pressure + watch-baseline / verbatim / explicit-negation / stay-green signals)
- Skill leaf `chains/chain-jail/testing-skills.md` + `references/testing-skills.md` cite obra/superpowers writing-skills testing-skills-with-subagents.md (URL + 2026-09-27 + sha256); Chain Jail extract-aspect + authoring companion + capture SKILL + catalog lockstep
- Route/triggers → emperor-capture; bakeoff + honesty inventory; plugin/marketplace/SKILL at 0.4.45

## 0.4.44
- Writing-good-tests HARD-GATE leaf: `scripts/lib/good_tests.py` prints GOOD / PRIN / GATE / MUST card (name the break / exercise the real thing / hand-derived want / mutation check)
- Thin `good-tests.sh` / `good-tests.ps1`; emperor peers gain `good-tests`; `--reject-mirror` / `--reject-change-detector` HARD-GATEs; `--check-named-break` validator (name-break + real-thing / hand-derived / mutation signals)
- Skill leaf `skills/emperor-tdd/writing-good-tests.md` + `references/writing-good-tests.md` cite obra/superpowers MIT (test-driven-development writing-good-tests.md aspect); does **not** vendor whole test-driven-development
- Route/triggers for writing-good-tests phrases → emperor-tdd; companion after RGR iron-law; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.44

## 0.4.43
- Pressure/academic HARD-GATE leaf: `scripts/lib/pressure.py` prints PRESSURE / CASE / MUST / ACADEMIC card (resist skip under emergency / sunk-cost / authority; academic four-phase self-check)
- Thin `pressure.sh` / `pressure.ps1`; emperor peers gain `pressure`; `--reject-shortcut` / `--reject-compromise` HARD-GATEs; `--check-academic` validator (four-phase + root-cause-first signals)
- Skill leaf `skills/emperor-heal/pressure-academic.md` + `references/pressure-academic.md` cite obra/superpowers MIT (systematic-debugging test-pressure-*.md + test-academic.md aspect); does **not** vendor whole systematic-debugging
- Route/triggers for pressure/academic phrases → emperor-heal; companion after find-polluter; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.43

## 0.4.42
- Find-polluter HARD-GATE leaf: `scripts/lib/polluter.py` prints POLLUTER / STEP / MUST card (find which test creates unwanted files/state / do not guess)
- Thin `find-polluter.sh` / `find-polluter.ps1`; emperor peers gain `polluter`; `--reject-guess` / `--reject-unbisected` HARD-GATEs; `--check-found` validator (FOUND POLLUTER + path / identity signals)
- Skill leaf `skills/emperor-heal/find-polluter.md` + `references/find-polluter.md` cite obra/superpowers MIT (systematic-debugging find-polluter.sh aspect); does **not** vendor whole systematic-debugging
- Route/triggers for polluter phrases → emperor-heal; Phase-1/2 shared-state companion after condition-based-waiting; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.42

## 0.4.41
- Condition-based-waiting HARD-GATE leaf: `scripts/lib/condition_wait.py` prints WAIT / COND / MUST card (wait for the actual condition / not a guess about timing)
- Thin `condition-wait.sh` / `condition-wait.ps1`; emperor peers gain `wait`; `--reject-sleep` / `--reject-unguessed` HARD-GATEs; `--check-condition` validator (strong tokens / waitFor pattern)
- Skill leaf `skills/emperor-heal/condition-based-waiting.md` + `references/condition-based-waiting.md` cite obra/superpowers MIT (systematic-debugging condition-based-waiting aspect); does **not** vendor whole systematic-debugging
- Route/triggers for CBW phrases → emperor-heal; Phase-4 flaky/timing companion after defense-in-depth; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.41

## 0.4.40
- Defense-in-depth HARD-GATE leaf: `scripts/lib/defense.py` prints DEFENSE / LAYER / MUST card (validate at every layer / four layers)
- Thin `defense.sh` / `defense.ps1`; emperor peers gain `defense`; `--reject-single-layer` / `--reject-unlayered` HARD-GATEs; `--check-layers` validator (≥2 distinct layer ids)
- Skill leaf `skills/emperor-heal/defense-in-depth.md` + `references/defense-in-depth.md` cite obra/superpowers MIT (systematic-debugging defense-in-depth aspect); does **not** vendor whole systematic-debugging
- Route/triggers for defense phrases → emperor-heal; Phase-4 companion after `emperor trace` source fix; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.40

## 0.4.39
- Root-cause tracing HARD-GATE leaf: `scripts/lib/root_cause.py` prints TRACE / STEP / MUST card (trace backward / fix at source / no symptom-only patch)
- Thin `trace.sh` / `trace.ps1`; emperor peers gain `trace`; `--reject-symptom-fix` / `--reject-untraced` HARD-GATEs; `--check-chain` validator (≥2 backward links)
- Skill leaf `skills/emperor-heal/root-cause-tracing.md` + `references/root-cause-tracing.md` cite obra/superpowers MIT (systematic-debugging root-cause-tracing aspect); does **not** vendor whole systematic-debugging
- Route/triggers for trace phrases → emperor-heal; Phase-1 companion to `emperor heal`; eval/bakeoff/honesty lockstep
- Plugin, marketplace, and SKILL.md at 0.4.39

## 0.4.38
- Archaeology Ada leaf: `evals/fixtures/lost-ada/HELLO.ADB` + identify smoke; GNATMAKE 13.3.0 boot probe VERIFIED (`gnatmake` / run); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-ada-manual.md` — GNAT User's Guide Building with gnatmake (procedure body as main unit)
- Catalog + SKILL.md + archaeology.md link the sixth pin alongside Pascal, ASM, COBOL, Fortran, and VHDL; route triggers gain `ada` / `gnat` / `gnatmake` / `.adb` / `.ads`; eval locks `*.adb` identify on lost-ada
- Plugin, marketplace, and SKILL.md at 0.4.38


## 0.4.37
- Diagnosing HARD-GATE leaf: `scripts/lib/diagnose.py` prints DIAGNOSE / INTAKE / CITE / MUST card (citation iron law + intake-before-analysis)
- Thin `diagnose.sh` / `diagnose.ps1`; emperor peers gain `diagnose`; `--reject-uncited` / `--reject-skip-intake` HARD-GATEs; `--check-citation` validator
- Skill leaf `skills/emperor-heal/diagnosing.md` + `references/diagnosing.md` cite obra/superpowers MIT (Core principle + Intake before analysis); does **not** vendor diagnosing-superpowers
- Route/triggers for diagnose phrases → emperor-heal; eval/bakeoff/honesty lockstep

## 0.4.36
- Session-discovery Python core: `scripts/lib/session_discovery.py` prints SESSION / PATH / STATUS / MUST locate card; probes Claude Code + Cursor/agent transcript roots read-only; VERIFIED only when path exists
- Thin `session-discovery.sh` / `session-discovery.ps1`; emperor peers gain `session-discovery`; `--reject-guess` HARD-GATE (always-fail) for claim-without-path
- Skill leaf `skills/emperor-heal/session-discovery.md` + `references/session-discovery.md` (obra/superpowers diagnosing locate aspect, MIT); route triggers for session transcript locate → emperor-heal
- Unblocks a future diagnosing HARD-GATE without vendoring whole diagnosing-superpowers; eval/bakeoff/honesty/plugin lockstep
- Plugin, marketplace, and SKILL.md at 0.4.36


## 0.4.35
- Archaeology VHDL leaf: `evals/fixtures/lost-vhd/HELLO.VHD` + identify smoke; GHDL 5.0.1 boot probe VERIFIED (`ghdl -a` / `-e` / `-r`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-vhdl-manual.md` — GHDL Invoking GHDL Analysis / Elaboration / Run (entity as top unit)
- Catalog + SKILL.md + archaeology.md link the fifth pin alongside Pascal, ASM, COBOL, and Fortran; route triggers gain `vhdl` / `ghdl` / `.vhd` / `.vhdl`; eval locks `*.vhd` identify on lost-vhd
- Plugin, marketplace, and SKILL.md at 0.4.35


## 0.4.34
- Excavate thin-alias polish: `scripts/excavate.sh` / `excavate.ps1` call `scripts/lib/identify.py` directly (no hop through identify twins)
- Closes deferred bash↔ps1 alias drift surface after identify.py / worktree.py cores — excavate stays a first-class tool name with one Python survey core
- Eval locks thin excavate twins → identify.py + line caps + survey smoke parity with identify; bakeoff + honesty name the leaf
- Plugin, marketplace, and SKILL.md at 0.4.34


## 0.4.33
- Worktree create Python core: `scripts/lib/worktree.py` owns id/base resolve, `.worktrees/<id>` layout, `emperor/<id>` branch, EXISTS short-circuit, and `git worktree add`
- Thin `worktree.sh` / `worktree.ps1` twins — closes bash↔ps1 twin drift on the mutate path after isolation HARD-GATE (`emperor iso` / worktree_iso.py stays the checklist card)
- Eval locks compile + thin twins + usage refuse + not-a-repo refuse + tempfile create/EXISTS smoke; bakeoff + honesty name the leaf
- Plugin, marketplace, and SKILL.md at 0.4.33


## 0.4.32
- Silent-boot Python core: `scripts/lib/host.py` owns host detect + host.env report line; `scripts/lib/boot.py` owns `.emperor/host.env` + survey.md + optional eval.log
- Thin `boot.sh` / `boot.ps1` twins — closes bash↔ps1 twin drift (host.sh C.UTF-8 + cmd/powershell/pwsh WSL interop vs host.ps1 UTF-8 + cmd-only)
- `emperor_host_report` / `Write-EmperorHostReport` delegate to `host.py`; shell twins keep sourceable EMPEROR_* + path helpers for the dispatcher
- Eval locks compile + thin twins + report keys + `--as-json` + boot smoke (`--skip-eval`); bakeoff + honesty name the leaf
- Plugin, marketplace, and SKILL.md at 0.4.32


## 0.4.31
- Install Python core: `scripts/lib/install.py` owns harness map, dest resolve, copy set, chain expose, activation tips, and dry-run
- Thin `install.sh` / `install.ps1` twins — closes bash↔ps1 twin drift (ps1 previewed chain destinations before copy; first-run tip said `dowse.ps1` vs `dowse.sh`)
- Unified first-run tip to host-agnostic `scripts/emperor dowse`; dry-run lists planned chains when `--with-chain-skills`; eval locks compile + thin twins + dry-run + unknown harness reject
- Plugin, marketplace, and SKILL.md at 0.4.31


## 0.4.30
- Parallel-dispatch HARD-GATE leaf: Superpowers `dispatching-parallel-agents` → Identify Independent Domains / Focused Agent Tasks / Parallel Dispatch / Review and Integrate only, adapted into `skills/emperor-dispatch/parallel-dispatch-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/parallel.py` prints PARALLEL/STEP/MUST card, rejects step skips (`--advance`), hard-gates shared writable scope (`--reject-shared-scope`); thin `parallel.sh` / `parallel.ps1`; `emperor parallel` on bash/ps1/zsh/cmd peers
- emperor-dispatch MUST the checklist for 2+ independent domains; companion to sequential `emperor subagent` / inline `emperor execute`; catalog + navigation + bakeoff point local-first; eval locks card + skip rejection + reject-shared-scope
- Plugin, marketplace, and SKILL.md at 0.4.30

## 0.4.29
- Subagent-driven HARD-GATE leaf: Superpowers `subagent-driven-development` → Fresh subagent per task / Task review after each / Fix loop R of 5 / Final whole-branch review only, adapted into `skills/emperor-build/subagent-driven-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/subagent.py` prints SUBAGENT/STEP/MUST card, rejects step skips (`--advance`), hard-gates skipped task review (`--reject-skip-review`); thin `subagent.sh` / `subagent.ps1`; `emperor subagent` on bash/ps1/zsh/cmd peers
- emperor-build MUST the checklist for subagent plan runs (companion to `emperor execute` inline path); catalog + navigation + bakeoff point local-first; eval locks card + skip rejection + reject-skip-review
- Plugin, marketplace, and SKILL.md at 0.4.29

## 0.4.28
- Executing-plans HARD-GATE leaf: Superpowers `executing-plans` → Continuous execution / Four stops / Rulings not stalls / Task Loop / Completion contract only, adapted into `skills/emperor-build/executing-plans-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/execute.py` prints EXECUTE/STEP/MUST card, rejects step skips (`--advance`), hard-gates check-in theater (`--reject-checkin`); thin `execute.sh` / `execute.ps1`; `emperor execute` on bash/ps1/zsh/cmd peers
- emperor-build MUST the checklist for inline plan runs; catalog + navigation point local-first; eval locks card + skip rejection + reject-checkin
- Hygiene: backfill CHANGELOG 0.4.27 (missed on #44); `emperor.cmd` gains missed `receive` peer alongside `execute`
- Plugin, marketplace, and SKILL.md at 0.4.28

## 0.4.27
- Receive-review HARD-GATE leaf: Superpowers `receiving-code-review` → The Response Pattern / Forbidden Responses / When To Push Back only, adapted into `skills/emperor-verify/receive-review-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/receive.py` prints RECEIVE/STEP/MUST card, rejects step skips (`--advance`), hard-gates blind implement (`--reject-blind-implement`); thin `receive.sh` / `receive.ps1`; `emperor receive` on bash/ps1/zsh peers
- emperor-verify MUST the checklist before implementing review feedback; catalog + bakeoff + honesty name the leaf; eval locks card + skip rejection + reject-blind-implement
- Plugin, marketplace, and SKILL.md at 0.4.27


## 0.4.26
- Dowse Python core: `scripts/lib/dowse.py` owns read-only agent roster scan (PATH detect, bounded --version / auth probes, table + `--as-json`)
- Thin `dowse.sh` / `dowse.ps1` twins — closes bash↔ps1 twin drift (ps1 had `-AsJson` + Binary/Headless/SignIn metadata; bash was table-only)
- Factory dogfood: system-dowsing + agent-registry + bakeoff point at the Python lock; eval locks compile + thin twins + AsJson richer roster + `--as-json` on both peers
- Plugin, marketplace, and SKILL.md at 0.4.26

## 0.4.25
- Review-pack Python core: `scripts/lib/review_pack.py` owns meta SHAs, acceptance-criteria extract, diff/diffstat, claims copy
- Thin `review-pack.sh` / `review-pack.ps1` twins — closes bash↔ps1 twin drift (ps1 copied entire work-order into criteria.md; bash awk kept only `## Acceptance criteria`)
- Factory dogfood: mechanical-gates + emperor-verify + request-review checklist point at the Python lock; eval locks compile + thin twins + criteria extract (no Plan header / Out of scope leak) + meta SHAs
- Plugin, marketplace, and SKILL.md at 0.4.25


## 0.4.24
- Forge PR Python core: `scripts/lib/forge.py` owns consent (env or ledger), DONE probes, title + G1..G2 PR body, gh create / DRY
- Thin `forge.sh` / `forge.ps1` twins — closes bash↔ps1 twin drift (ps1 hardcoded title and dumped full ledger into PR.md)
- Factory dogfood: software-factory + mechanical-gates + emperor-forge skill point at the Python lock; eval locks compile + thin twins + refuse + DRY title + G1/DONE body (no G0 leak)
- Plugin, marketplace, and SKILL.md at 0.4.24

## 0.4.23
- Queue picker Python core: `scripts/lib/queue.py` owns list/next/add/done (WIP=1, placeholder skip, gh → Linear → local)
- Thin `queue.sh` / `queue.ps1` twins — closes bash↔ps1 twin drift (ps1 list lacked Linear notice + git worktree guard)
- Factory dogfood: software-factory + emperor-queue skill point at the Python lock; eval locks compile + thin twins + empty UX + WIP refuse + done

## 0.4.22
- Silent-boot zsh parity: `scripts/emperor.zsh` auto-boots when `.emperor/host.env` missing; `host`/`boot`/`identify`/`excavate` special-cases match bash `scripts/emperor` (closes twin gap after PS silent-boot parity)
- Eval locks + Cursor adapter document the `emperor.zsh` silent-boot path
- Plugin, marketplace, and SKILL.md at 0.4.22

## 0.4.21
- DONE probes Python core: `scripts/lib/done.py` owns probe:/expect: execution (bash -lc, substring match, empty-expect parity)
- Thin `done.sh` / `done.ps1` twins — closes bash↔ps1 twin drift risk on the load-bearing Stop-hook / forge gate
- Fixtures `evals/fixtures/done-probes/{ok,fail,no-probes}` + eval locks (compile, thin caps, smoke, dogma pointer)
- Plugin, marketplace, and SKILL.md at 0.4.21

## 0.4.20
- Route enrichment (JSON MVP): excavate patterns gain Fortran family (`fortran`, `gfortran`, `.f90`, `.f95`, `.for`, `f90`) so extension utterances like `hello.f90` and `gfortran build` map to excavate — closes gap after the v0.4.15 Fortran archaeology leaf
- Thin `route.sh` / `route.ps1` twins (normalize + argv/stdin live in `scripts/lib/route.py`) — closes route twin bloat vs other Python cores
- Eval locks: `.f90` / fortran / gfortran → excavate, thin-twin line caps, triggers presence
- Plugin, marketplace, and SKILL.md at 0.4.20

## 0.4.19
- Structural eval Python core: `scripts/lib/eval.py` owns the full assertion suite (presence, twins, gates, identify, fixtures, route, leaf HARD-GATEs, bakeoff honesty)
- Thin `eval.sh` / `eval.ps1` twins — closes bash↔ps1 twin drift (ps1 was a ~35-line presence stub while bash held ~600 lines of locks)
- `references/mechanical-gates.md` + bakeoff inventory point at the Python lock; eval self-locks compile + thin twins
- Plugin, marketplace, and SKILL.md at 0.4.19

## 0.4.18
- Finish menu Python core: `scripts/lib/finish.py` owns ENV/MENU detection (worktree kind, origin/HEAD base_guess, cleanup_owned)
- Thin `finish.sh` / `finish.ps1` twins — closes bash↔ps1 twin drift (ps1 had dropped origin/HEAD fallback)
- `skills/emperor-forge/finish-menu.md` + bakeoff inventory point at the Python lock; eval locks compile + thin twins + ENV/MENU smoke
- Plugin, marketplace, and SKILL.md at 0.4.18

## 0.4.17
- Artifact survey Python core: `scripts/lib/identify.py` owns extensions + named fossils + shebangs (always exit 0)
- Thin `identify.sh` / `identify.ps1` twins — closes bash↔ps1 twin drift (ps1 had dropped shebangs section; fossil/Makefile counting diverged)
- `excavate` stays alias through the thin twin; boot survey + archaeology fixtures consume one core
- `references/archaeology.md` + bakeoff inventory point at the Python survey; eval locks compile + thin twins + shebangs + lost-pas smoke
- Plugin, marketplace, and SKILL.md at 0.4.17

## 0.4.16
- Mechanical gates Python core: `scripts/lib/gate.py` owns G0–G5 (prior stamps, plan-header via `work_order.py`, G4 quoted-VERIFIED hard fail + CONJECTURE warn)
- Thin `gate.sh` / `gate.ps1` twins — closes bash↔ps1 twin drift (ps1 had dropped CONJECTURE warn)
- `references/mechanical-gates.md` + iron-laws / work-order / purpose point at the Python lock; eval locks compile + thin twins + unordered prior refuse + bakeoff inventory
- Plugin, marketplace, and SKILL.md at 0.4.16

## 0.4.15
- Archaeology Fortran leaf: `evals/fixtures/lost-f90/HELLO.F90` + identify smoke; GNU Fortran 14.2 boot probe VERIFIED (`gfortran -o`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-fortran-manual.md` — GNU Fortran Compiler §2.2 free-form dialect / file-extension source form
- Catalog + SKILL.md + archaeology.md link the fourth pin alongside Pascal, ASM, and COBOL; eval locks `*.f90` identify on lost-f90
- Plugin, marketplace, and SKILL.md at 0.4.15

## 0.4.14
- Verification-before-completion / evidence HARD-GATE leaf: Superpowers `verification-before-completion` → **The Iron Law** + **The Gate Function** only, adapted into `skills/emperor-verify/verification-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/evidence.py` prints EVIDENCE/STEP/MUST card, rejects step skips (`--advance`), hard-gates unverified completion claims (`--reject-unverified`); thin `evidence.sh` / `evidence.ps1`; `emperor evidence` on bash/ps1/zsh/cmd peers
- emperor-verify MUST the checklist before any completion / pass / fixed / done claim; catalog + navigation point local-first; eval locks card + skip rejection + reject-unverified
- Honest bake-off refresh: `evals/bakeoff.md` + `evals/fixtures/this-upgrade.md` inventory mechanism/activation/leaf gates (plans, finish, activate/must-route, grill, debug phases, TDD, worktree iso, review, author, evidence, archaeology pas/asm/cbl); local mechanism TESTED/VERIFIED; live defect-rate vs Superpowers UNVERIFIABLE; `scripts/lib/bakeoff_honesty.py` + eval lock — no version bump
- Plugin, marketplace, and SKILL.md at 0.4.14

## 0.4.13
- Authoring iron-law / skill-RGR leaf: Superpowers `writing-skills` → **The Iron Law (Same as TDD)** + skill RED-GREEN-REFACTOR only, adapted into `chains/chain-jail/authoring-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/author.py` prints AUTHOR/STEP/MUST card, rejects step skips (`--advance`), hard-gates untested skill writes (`--reject-untested`); thin `author.sh` / `author.ps1`; `emperor author` on bash/ps1/zsh/cmd peers
- Chain Jail authoring.md + emperor-capture MUST the checklist before skill body; catalog + navigation point local-first; eval locks card + skip rejection + reject-untested
- Plugin, marketplace, and SKILL.md at 0.4.13

## 0.4.12
- Archaeology COBOL leaf: `evals/fixtures/lost-cbl/HELLO.CBL` + identify smoke; GnuCOBOL 3.2 boot probe VERIFIED (`cobc -x`); dialect labels honest (CONJECTURE / UNVERIFIABLE where due)
- Jail pin `references/archaeology-cobol-manual.md` — GnuCOBOL Programmer’s Guide §4 IDENTIFICATION DIVISION / PROGRAM-ID
- Catalog + SKILL.md + archaeology.md link the third pin alongside Pascal and ASM; eval locks `*.cbl` identify on lost-cbl
- Plugin, marketplace, and SKILL.md at 0.4.12

## 0.4.11
- Request-review HARD-GATE leaf: Superpowers `requesting-code-review` → When / How / Act-on-feedback only, adapted into `skills/emperor-verify/request-review-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/review_req.py` prints REVIEW/STEP/MUST card, rejects step skips (`--advance`), hard-gates author self-review (`--reject-self-review`); thin `review.sh` / `review.ps1`; `emperor review` on bash/ps1/zsh/cmd peers
- emperor-verify MUST the checklist before merge / major feature / subagent task done; reuses `review-pack` at Step 3; eval locks card + skip rejection + reject-self-review

## 0.4.10
- Worktree isolation leaf: Superpowers `using-git-worktrees` → detect / native-or-git / check-ignore / baseline HARD-GATE only, adapted into `skills/emperor-worktree/isolation-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/worktree_iso.py` prints WORKTREE/STEP/MUST card, rejects step skips (`--advance`), hard-gates blind create (`--reject-blind-create`); thin `iso.sh` / `iso.ps1`; `emperor iso` on bash/ps1/zsh/cmd peers
- emperor-worktree + emperor-build MUST the checklist before standard/heavy mutate; `.worktrees/` gitignored; eval locks card + skip rejection + reject-blind-create

## 0.4.9
- TDD iron-law / RGR leaf: Superpowers `test-driven-development` → **The Iron Law** + **Red-Green-Refactor** HARD-GATE only, adapted into `skills/emperor-tdd/red-green-refactor.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/tdd.py` prints TDD/STEP/MUST card, rejects step skips (`--advance`), hard-gates prod-before-fail (`--reject-prod`); thin `tdd.sh` / `tdd.ps1`; `emperor tdd` on bash/ps1/zsh/cmd peers
- emperor-tdd + emperor-build MUST the checklist before production code; eval locks card + skip rejection + reject-prod

## 0.4.8
- Grill/brainstorm leaf: Superpowers `brainstorming` → **HARD-GATE** only, adapted into `skills/emperor-require-design/grill-checklist.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/grill.py` prints GRILL/STEP/MUST card, rejects step skips (`--advance`), hard-gates impl jumps (`--reject-impl`); thin `grill.sh` / `grill.ps1`; `emperor grill` on bash/ps1/zsh/cmd peers
- require-design MUST the checklist before BUILD; eval locks card + skip rejection + reject-impl

## 0.4.7
- Heal four-phase leaf: Superpowers `systematic-debugging` → **The Four Phases** only, adapted into `skills/emperor-heal/debug-four-phases.md` (Chain Jail extract-aspect)
- Python core `scripts/lib/debug_phases.py` prints DEBUG/PHASE/MUST card and rejects phase skips (`--advance`); thin `heal.sh` / `heal.ps1`; `emperor heal` on bash/ps1/zsh/cmd peers
- Holy Chain router + emperor-heal skill MUST the checklist before proposing fixes; eval locks card + skip rejection

## 0.4.6
- MUST-route doctrine bite: Load law + AGENTS.md standing order require one governing skill/file (or `emperor route` / `emperor activate`) before creative work, clarifying questions, or exploring
- Python-first router: `scripts/lib/route.py` owns matching; `route.sh` / `route.ps1` are thin twins (same exits 0/1/2)
- Adapter SessionStart notes: cursor/codex/kimi-cli/ollama/opencode/generic document host-agnostic silent boot + MUST-route
- Honest `references/sdlc-comparison.md` refresh: Router MVP, excavate alias, remote CI `eval.yml`, adapter MUST-route notes
- Eval locks `route.py` presence + `finish the branch` → forge; SessionStart MUST-route language retained

## 0.4.5
- Silent activation MUST-route: Superpowers `using-superpowers` 1% leaf adapted into `skills/emperor-resume/must-route.md` — SessionStart fires without waiting for "emperor time"
- Python core `scripts/lib/activate.py` prints ACTIVATION/MUST card from disk state or utterance; thin `activate.sh` / `activate.ps1`; `emperor activate` on bash/ps1/zsh/cmd peers
- SessionStart hook runs activate after boot; eval locks the card + utterance route smoke

## 0.4.4
- Finish menu: Superpowers finish-branch aspect adapted into `skills/emperor-forge/finish-menu.md` (merge locally / PR / keep; typed `discard`; owned-worktree cleanup)
- `scripts/finish.sh` / `finish.ps1` twins detect env and print the menu (no merge/push); `emperor finish` wired on bash/ps1/zsh/cmd peers
- Route triggers: finish the branch / implementation complete / merge locally → forge; eval locks the aspect + script output

## 0.4.3
- Silent-boot PS parity: `boot.ps1` sources `lib/host.ps1` + `Write-EmperorHostReport` (same host.env keys as bash); `emperor.ps1` auto-boots when `.emperor/host.env` missing; Cursor adapter documents `emperor boot` / Windows silent-boot contract
- Archaeology: Jail-pin NASM 2.16.03 §7.3 SECTION for FOO.ASM (`references/archaeology-asm-manual.md`)
- Route trigger harden: blocked/WIP → queue; red build/derail → heal; missing capability/jail → capture; nasm/assembler → excavate
- Catalog links: archaeology Jail pins (pascal + asm) from `archaeology.md`, skill-catalog, and SKILL.md
- Queue empty UX: comment-only empty `.emperor/queue.md`; `queue.sh`/`queue.ps1` skip `(empty…)` / parentheses-only placeholder lines so `queue next` never promotes junk (WIP=1 kept)
- Plugin, marketplace, SKILL.md, excavate + queue skill frontmatter at 0.4.3

## 0.4.2
- Wave merge: CI eval workflow; adapter silent-boot parity; SDLC comparison; Pascal Jail pin (ISO 7185 §6.10)
- Queue Kanban maturity (WIP=1 statuses); trigger→skill `route` MVP (sh/ps1 twins)
- First-class `excavate` alias + usage hygiene across emperor peers
- Archaeology probes: `lost-pas` HELLO.PAS + `lost-asm` FOO.ASM fixtures with dialect-honest identify smokes
- Plugin, marketplace, and SKILL.md at 0.4.2

## 0.4.1
- Silent boot: `scripts/boot.sh` / `boot.ps1` write `.emperor/host.env`, `survey.md`, and optional `eval.log` with no user ritual
- Identify is internal: fossils and `scripts/emperor identify <path>` for foreign trees; agents read survey, do not ask the client to run identify
- Excavate router: lost/ancient/unmarked codebases via `skills/emperor-excavate` and Dowsing excavate
- Plugin, marketplace, and SKILL.md at 0.4.1 (archaeology keywords)
- Audit-fixes merge: `emperor.cmd` hook peer, eval twins for queue/forge/identify/boot, +x on factory scripts

## 0.3.3
- Plugin and marketplace register `emperor-tdd` and `emperor-worktree`
- `references/iron-laws.md` and `templates/state.md` (names SKILL.md already used)
- Self-application fixture: `evals/fixtures/this-upgrade.md`

## 0.3.2
- SKILL.md rewritten as orchestrator (vows + five chains kept)
- TDD iron law skill, worktree skill, SessionStart hook, STATE resume

## 0.3.0
- Work-order, review-pack, gate.sh, eval.sh, phase skills, jail pin-and-consent

## 0.2.0
- Plugin marketplace packaging, privacy policy
