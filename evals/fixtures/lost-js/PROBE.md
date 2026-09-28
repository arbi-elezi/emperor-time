# Boot probe — lost-js / HELLO.js

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~10:17 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **nodejs** 20.19.2+dfsg-1+deb13u3 |
| Binary | `/usr/bin/node` |
| Reported | `v20.19.2` |
| Install | already present on box (no apt this leaf) |

Probe used script-file evaluation
(`node HELLO.js`)
on a minimal `console.log` program. Identify fossils
use `*.js` only. Prefer `nodejs` / `node20` / `javascript` / `.js`.
Bare `node` is **refused** as a route tag (common-English / tech "AST node" collision).
Bare `js` is **allowed** as a route tag (two-letter language abbreviation;
word-boundary match). Bare `.js` is **allowed** with extension-boundary
matching (does not prefix-hit `.json` / `.jsx`). Classic scripting /
runtime leaf after C; toolchain already on box (Worthy Spend vs TeXlive).
Do not claim a full ECMAScript / npm / ESM graph recovery from a
`console.log` probe alone — this leaf pins JavaScript script-file
evaluation via `node` + stdout.

## Commands (VERIFIED)

```text
$ dpkg -l nodejs | awk '/^ii/ {print $2, $3}'
nodejs 20.19.2+dfsg-1+deb13u3

$ node --version
v20.19.2

$ which node
/usr/bin/node

$ node HELLO.js
EMPEROR-TIME-JS-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs Node.js 20.19 and executes `HELLO.js` via `node HELLO.js` | VERIFIED |
| Filename culture (`.mjs` / `.cjs` / `"type":"module"`) maps to this dialect | CONJECTURE (probe uses CommonJS-default `.js`) |
| Full ECMAScript / npm workspace / ESM graph recovery | UNVERIFIABLE from console.log probe alone |
