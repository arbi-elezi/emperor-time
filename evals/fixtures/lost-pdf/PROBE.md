# Boot probe — lost-pdf / HELLO.pdf

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~20:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **poppler-utils** 25.03.0-5+deb13u4 (Debian trixie) |
| Binary | `/usr/bin/pdftotext` (+ `pdfinfo`) |
| Reported | `pdftotext version 25.03.0` (`pdftotext -v`) |
| Install | already on box this leaf — **zero new Apt Worthy Spend**; Debian `poppler-utils` already present (Installed-Size 723 kB; archive ~213 kB); still prefer over deferred TeXlive / C++ / graphviz multi-dep apt; LibreOffice / ghostscript / qpdf / mutool REJECTED as leaf owner vs already-on-box poppler `pdftotext` |

Probe used `pdftotext -layout HELLO.pdf -` on a minimal
one-page PDF-1.4 with a Helvetica text operator drawing the probe token.
Identify fossils use `*.pdf`. Prefer `pdf` / `pdftotext` / `poppler` / `.pdf`.
Bare `pdf` / `pdftotext` / `poppler` are **allowed** as route tags (format / tool / family).
Bare `.pdf` is **allowed** with extension-boundary matching (do not invent
`.pdffoo` prefix hits). Bare `acrobat` / `adobe` / `ghostscript` / `libreoffice` / `soffice` refused this leaf (suite discourse / apt surface; ghostscript remains the PostScript leaf owner).
PDF document leaf after PPTX; treats PDF as peer document fossil not house twin language.
Do **not** claim a full Acrobat / LibreOffice / Ghostscript / ECMA PDF suite recovery from a
Poppler `pdftotext` probe alone — this leaf pins `pdftotext -layout` text extraction
with the probe token printed. Do **not** claim LibreOffice / ghostscript / qpdf as the verified
toolchain this leaf (apt REJECTED as owner; poppler already on box).
Distinct from PPTX (`*.pptx` / zipfile), DOCX (`*.docx` / zipfile), XLSX (`*.xlsx` / zipfile),
PostScript (`*.ps` / ghostscript), HTML (`*.html` / tidy), and roff (`*.roff` / groff).
Do **not** steal plain `*.ps` or `*.pptx` or `*.docx` or `*.xlsx` ownership — those remain prior leaves.
Defer TeX/LaTeX / C++ / openjdk-as-owner / graphviz / CLIPS / embeddings this turn.

## Commands (VERIFIED)

```text
$ which pdftotext
/usr/bin/pdftotext

$ pdftotext -v
pdftotext version 25.03.0
Copyright 2005-2025 The Poppler Developers - http://poppler.freedesktop.org
Copyright 1996-2011, 2022 Glyph & Cog, LLC

$ dpkg -l poppler-utils | awk '/poppler-utils/ {print $2, $3}'
poppler-utils 25.03.0-5+deb13u4

$ pdftotext -layout HELLO.pdf -
EMPEROR-TIME-PDF-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Poppler `pdftotext` 25.03.0 `-layout` on this HELLO (PDF-1.4 one-page Helvetica text drawing the probe token) | VERIFIED |
| Full Acrobat / LibreOffice / Ghostscript / ECMA PDF authoring suite are this dialect | CONJECTURE |
| Full Debian libreoffice/ghostscript/qpdf suite recovery from this probe alone | UNVERIFIABLE |
