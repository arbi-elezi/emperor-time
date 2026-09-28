# Jail pin — TypeScript Handbook tsc CLI Options (`tsc` … file.ts) for HELLO.ts

Contemporaneous manual pin for the lost-ts archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how TypeScript
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-ts/HELLO.ts` with
runnable dialect **VERIFIED** as TypeScript 5.6.3 (`tsc`) + Node.js 20.19.2
under Linux x86_64
(`tsc --target ES2020 --module commonjs HELLO.ts --outDir …` then
`node …/HELLO.js` →
`EMPEROR-TIME-TS-PROBE-OK`). Filename culture
(`.tsx` / `.mts` / `.cts` / project references) remains
**CONJECTURE** only for module-system / JSX labels. Identify fossils use `*.ts` only
(no `*.tsx` this leaf).
Bare `ts` is **allowed** as a route tag (two-letter abbreviation;
word-boundary). Bare `.ts` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.tsx` / `.tsbuildinfo` / `.mts` / `.cts`). Prefer `typescript` /
`typescript5` / `tsc` / `ts5` / `.ts`.
Toolchain is npm-local `typescript` 5.6.3 providing
`/tmp/ts-probe/node_modules/.bin/tsc` (not bun; bun≠tsc).
Node `/usr/bin/node` v20.19.2 runs the emitted JS. This note supplies
the Jail pin so excavate can name the **verified** TypeScript `tsc`
emit + `node` run shape without inventing a full type-system /
declaration emit / project-references suite claim for a
`console.log` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *TypeScript Handbook* — tsc CLI Options / Using the CLI |
| **Heading** | **Using the CLI** — `tsc index.ts` (emit JS for a TypeScript file with compiler defaults / CLI flags) |
| **Dialect pinned** | **TypeScript via tsc 5.6.3** with `console.log` source → CommonJS emit → `node` run — **not** full type-system / declaration emit / project-references suite claim |
| **URL** | https://www.typescriptlang.org/docs/handbook/compiler-options.html (TypeScript Handbook — tsc CLI Options / Using the CLI); npm package `typescript` 5.6.3; installed `tsc --version` |
| **Anchors** | `.ts` file path as compiler input; CLI emit of JavaScript; `--target` / `--module` / `--outDir` flags; runtime via Node on emitted `.js` |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from TypeScript Handbook — tsc CLI Options / Using the CLI)

> Running `tsc` locally will compile the closest project defined by a `tsconfig.json`, or you can compile a set of TypeScript files by passing in a glob of files you want. When input files are specified on the command line, `tsconfig.json` files are ignored.
>
> ```
> # Emit JS for just the index.ts with the compiler defaults
> tsc index.ts
> ```
>
> …
>
> ```
> # Emit a single .js file from two files via compiler options which take string arguments
> tsc app.ts util.ts --target esnext --outfile index.js
> ```

(Source: TypeScript Handbook, section
**tsc CLI Options — Using the CLI**,
https://www.typescriptlang.org/docs/handbook/compiler-options.html
accessed 2026-09-28 Europe/Tirane.
Installed `tsc --version` reports Version 5.6.3 and matches the
file-argument emit surface. Probe uses
`tsc --target ES2020 --module commonjs HELLO.ts --outDir …` so tsc
emits CommonJS JS, then `node` loads the emit and prints the probe
string. Language: TypeScript — see also the TypeScript Handbook.)

### Why this heading (HELLO.ts / excavate)

A minimal HELLO surface looks like:

```ts
console.log("EMPEROR-TIME-TS-PROBE-OK");
```

in a `.ts` file. That is exactly the pinned form:
**`tsc FILE.ts`** (with emit flags as needed), then **`node` on the
emitted `.js`**, observe string print at run time.
Pinning TypeScript Handbook tsc CLI Options lets excavate treat
`typescript` / `typescript5` / `tsc` / `ts5` / `.ts` + `console.log`
as **era evidence** (TypeScript / tsc emit) without rewriting the
fixture into a bun one-liner, a plain JS port, or an interactive REPL.
Identify surveys `*.ts` fossils on disk. `.ts` extension (boundary-safe
vs `.tsx` / `.tsbuildinfo` / `.mts` / `.cts`) and `typescript` /
`tsc` / `ts5` tags cover excavate intent. bun is not the verified
toolchain.
