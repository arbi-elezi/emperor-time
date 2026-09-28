# Jail pin — Poppler pdftotext for HELLO.pdf (Portable Document Format)

Contemporaneous manual pin for the lost-pdf archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PDF
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-pdf/HELLO.pdf` with
runnable dialect **VERIFIED** as Poppler `pdftotext` 25.03.0
under Linux x86_64
(`pdftotext -layout HELLO.pdf -` → stdout yields
`EMPEROR-TIME-PDF-PROBE-OK`). Filename culture
(Acrobat / LibreOffice / Ghostscript / ECMA-320 authoring / pptx / docx)
remains **CONJECTURE** only for naming collisions. Identify fossils use `*.pdf`.
Bare `pdf` / `pdftotext` / `poppler` are **allowed** as route tags (format / tool / family).
Bare `.pdf` is **allowed** as a route tag with
extension-boundary matching. Prefer `pdf` /
`pdftotext` / `poppler` / `.pdf`.
Bare `acrobat` / `adobe` / `ghostscript` / `libreoffice` / `soffice` are **refused** this leaf (suite discourse / apt surface; ghostscript remains PostScript leaf owner).
Do **not** steal plain `*.ps` or `*.pptx` or `*.docx` or `*.xlsx` ownership from prior leaves;
a `.pdf` is a distinct document fossil (ISO 32000 / PDF text extract via Poppler).
Toolchain is Debian `poppler-utils` already on box (**zero new apt**).
LibreOffice / ghostscript / qpdf / mutool apt were considered and **REJECTED**
as the verified leaf owner vs already-on-box poppler (same honesty as lost-jq already-on-box). This note supplies
the Jail pin so excavate can name the **verified** Poppler
`pdftotext -layout` shape on a PDF without inventing a full
Acrobat / LibreOffice / Ghostscript / ECMA PDF authoring suite claim for a
single-page probe. Distinct from the PPTX archaeology leaf (`*.pptx` /
zipfile), DOCX (`*.docx` / zipfile), XLSX (`*.xlsx` / zipfile), PostScript (`*.ps` /
ghostscript), HTML (`*.html` / tidy), and roff (`*.roff` / groff).
Chain Jail leaf only — excavate fossil pin, not a vendored anthropics document skill.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Poppler pdftotext(1) — Portable Document Format text extractor* + *ISO 32000 / PDF* |
| **Heading** | **`pdftotext -layout` on `.pdf`** — Extract text from a PDF page keeping (approximate) layout; write to stdout when output is `-` |
| **Dialect pinned** | **Poppler `pdftotext` 25.03.0 `-layout`** on a `.pdf` with Helvetica text operator drawing the probe token — **not** full Acrobat / LibreOffice / Ghostscript / ECMA PDF authoring suite claim |
| **URL** | https://poppler.freedesktop.org/ (Poppler); man `pdftotext(1)` on box; https://www.iso.org/standard/75839.html (ISO 32000-2 PDF); poppler-utils 25.03.0-5+deb13u4 on box |
| **Anchors** | `.pdf` path; `pdftotext -layout FILE -`; stdout text; Poppler pdftotext version line |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from pdftotext(1) + Poppler)

> pdftotext - Portable Document Format (PDF) to text converter (version 25.03.0)
>
> pdftotext [options] [PDF-file [text-file]]
>
> -layout : Maintain (as best as possible) the original physical layout of the text. The default is to undo physical layout (extracting text in content stream order) and eliminate redundant whitespace.
>
> If text-file is '-', the text is sent to stdout.

(Source: local `man pdftotext` / `pdftotext -v` on Debian poppler-utils 25.03.0-5+deb13u4,
accessed 2026-09-28 Europe/Tirane;
Poppler project https://poppler.freedesktop.org/
accessed 2026-09-28 Europe/Tirane.
Installed `pdftotext -v` reports pdftotext version 25.03.0.
Probe uses
`pdftotext -layout HELLO.pdf -`
so Poppler extracts the page text and prints the probe token.
Format: PDF-1.4 one-page MediaBox 612×792 with Type1 Helvetica text operator.)

### Why this heading (HELLO.pdf / excavate)

A minimal HELLO surface looks like a one-page PDF-1.4 with a Helvetica
text operator drawing the probe token. That is exactly the pinned form:
**Poppler `pdftotext -layout` on `.pdf`**, observe extracted text at run time.

### Honesty

- VERIFIED: Poppler `pdftotext` 25.03.0 `-layout` on this HELLO (PDF-1.4 one-page Helvetica text drawing the probe token).
- CONJECTURE: any claim that Acrobat / LibreOffice / Ghostscript / full ECMA PDF authoring are this dialect.
- UNVERIFIABLE: Debian libreoffice / ghostscript / qpdf / full multi-dialect PDF recovery from this probe alone.
- REJECTED this leaf: TeX/LaTeX, C++, CLIPS, embeddings/emperor.py, LibreOffice/ghostscript/qpdf/mutool as leaf owner (apt size / wrong owner); graphviz this turn (multi-dep); bare `acrobat` / `adobe` / `ghostscript` / `libreoffice` as verified PDF toolchain; stealing plain `*.ps` or `*.pptx` or `*.docx` or `*.xlsx` ownership from prior leaves; vendoring anthropics document skills as this Jail pin.
