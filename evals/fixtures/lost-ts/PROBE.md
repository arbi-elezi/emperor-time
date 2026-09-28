# Boot probe — lost-ts / HELLO.ts

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~10:41 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **typescript** 5.6.3 (npm-local under `/tmp/ts-probe`) |
| Binary | `/tmp/ts-probe/node_modules/.bin/tsc` |
| Reported | `Version 5.6.3` |
| Runtime | `/usr/bin/node` v20.19.2 (emit target) |
| Install | `npm install typescript@5.6.3 --prefix /tmp/ts-probe` (no apt this leaf; not bun) |

Probe used `tsc` emit then `node` run
(`tsc --target ES2020 --module commonjs HELLO.ts --outDir <out>` then
`node <out>/HELLO.js`)
on a minimal `console.log` program. Identify fossils
use `*.ts` only (no `*.tsx` this leaf). Prefer `typescript` /
`typescript5` / `tsc` / `ts5` / `.ts`.
Bare `ts` is **allowed** as a route tag (two-letter abbreviation;
word-boundary match). Bare `.ts` is **allowed** with extension-boundary
matching (does not prefix-hit `.tsx` / `.tsbuildinfo` / `.mts` / `.cts`).
Classic typed-compile leaf after Read Python; real `tsc` 5.6.3 via
npm-local install (prior this-upgrade rejected TypeScript because
bun≠tsc — that blocker is gone). Do **not** pin via bun. Do not claim
a full TypeScript type-system / declaration emit / project-references
recovery from a `console.log` probe alone — this leaf pins `tsc` emit
+ `node` run of the emitted JS.

## Commands (VERIFIED)

```text
$ npm install typescript@5.6.3 --prefix /tmp/ts-probe
$ /tmp/ts-probe/node_modules/.bin/tsc --version
Version 5.6.3

$ which node
/usr/bin/node

$ node --version
v20.19.2

$ /tmp/ts-probe/node_modules/.bin/tsc --target ES2020 --module commonjs HELLO.ts --outDir /tmp/et-ts-probe-out
$ node /tmp/et-ts-probe-out/HELLO.js
EMPEROR-TIME-TS-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `tsc` 5.6.3 and emits JS from `HELLO.ts`; `node` runs emit → probe string | VERIFIED |
| Filename culture (`.tsx` / `.mts` / `.cts` / project references) maps to this dialect | CONJECTURE (probe uses plain `.ts` + CLI flags, no tsconfig) |
| Full TypeScript type-system / declaration emit / project-references recovery | UNVERIFIABLE from console.log probe alone |
| bun as TypeScript compiler | REJECTED (bun≠tsc; not used this leaf) |
