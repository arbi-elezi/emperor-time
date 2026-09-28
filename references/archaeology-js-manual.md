# Jail pin — Node.js Command-line API Synopsis (`node [options] [script]`) for HELLO.js

Contemporaneous manual pin for the lost-js archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how JS
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-js/HELLO.js` with
runnable dialect **VERIFIED** as Node.js 20.19.2
under Linux x86_64
(`node HELLO.js` →
`EMPEROR-TIME-JS-PROBE-OK`). Filename culture
(`.mjs` / `.cjs` / package.json `"type"`) remains
**CONJECTURE** only for module-system labels. Identify fossils use `*.js` only.
Bare `node` is **refused** as a route tag (common-English / tech "AST node" collision).
Bare `js` is **allowed** as a route tag (two-letter abbreviation;
word-boundary). Bare `.js` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.json` / `.jsx`). Prefer `nodejs` / `node20` / `javascript` / `.js`.
Debian package `nodejs` (20.19.2+dfsg-1+deb13u3) provides
`/usr/bin/node`. This note supplies the Jail pin so excavate
can name the **verified** JavaScript script-file evaluation shape
without inventing a full ECMAScript / npm / ESM graph
suite claim for a `console.log` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Node.js v20.x Documentation* — Command-line API / Synopsis |
| **Heading** | **Synopsis** — `node [options] [V8 options] [script.js | -e "script" | -] [--] [arguments]` |
| **Dialect pinned** | **JavaScript via Node.js 20.19** with `console.log` script-file surface — **not** full ECMAScript / npm / ESM graph suite claim |
| **URL** | https://nodejs.org/docs/latest-v20.x/api/cli.html (Node.js v20.x — Command-line API / Synopsis); package `nodejs` 20.19.2+dfsg-1+deb13u3 on Debian trixie; installed `node --version` |
| **Anchors** | script path as program entry point; `.js` loaded by CommonJS module loader by default; `console.log` for string output; stdout at run time |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Node.js v20.x Documentation — Command-line API / Synopsis)

> `node [options] [V8 options] [script.js | -e "script" | -] [--] [arguments]`
>
> …
>
> ### Program entry point
>
> The program entry point is a specifier-like string. If the string is not an
> absolute path, it's resolved as a relative path from the current working
> directory. That path is then resolved by CommonJS module loader, or by the
> ES module loader if `--experimental-default-type=module` is passed. If no
> corresponding file is found, an error is thrown.

(Source: Node.js v20.x Documentation, section
**Command-line API — Synopsis / Program entry point**,
https://nodejs.org/docs/latest-v20.x/api/cli.html
accessed 2026-09-28 Europe/Tirane.
Installed `node --version` reports v20.19.2 and matches the
script-file evaluation surface. Probe uses `node HELLO.js` so node
loads the `.js` entry and prints the probe string. Language: JavaScript —
see also ECMA-262.)

### Why this heading (HELLO.js / excavate)

A minimal HELLO surface looks like:

```js
console.log("EMPEROR-TIME-JS-PROBE-OK");
```

in a `.js` file. That is exactly the pinned form:
**`node FILE.js`**, observe string print at run time.
Pinning Node.js Command-line API Synopsis lets excavate treat `nodejs` /
`node20` / `javascript` / `.js` + `console.log` as **era evidence**
(JavaScript / script file) without rewriting the fixture into a shell
one-liner, a Python port, or an interactive REPL. Identify surveys `*.js`
fossils on disk. `.js` extension (boundary-safe vs `.json` / `.jsx`) and
`nodejs` / `node20` / `javascript` tags cover excavate intent.
