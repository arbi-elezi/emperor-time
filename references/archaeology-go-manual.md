# Jail pin — cmd/go Compile and run Go program (`go run`) for HELLO.go

Contemporaneous manual pin for the lost-go archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how Go
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-go/HELLO.go` with
runnable dialect **VERIFIED** as Go 1.24.4
under Linux x86_64
(`go run HELLO.go` →
`EMPEROR-TIME-GO-PROBE-OK`). Filename culture
(`.GO` / 8.3 caps → Go source *naming*) remains **CONJECTURE** only.
Identify fossils use `*.go` only. Bare `go` is **refused** as a
route tag (common-English collision — word-boundary would still fire
on "let's go"). Bare `.go` is **allowed** as a route tag (no known peer
excavate substring collision). Prefer `golang` / `go1.24` / `.go`.
Debian package `golang-go` (2:1.24~2) Depends `golang-1.24-go` and
provides `/usr/bin/go`. This note supplies the Jail pin so excavate
can name the **verified** Go compile-and-run shape
without inventing a full modules / workspace / cgo / race
suite claim for a `fmt.Println` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *cmd/go* — Compile and run Go program (`go run`) |
| **Heading** | **Compile and run Go program** — Usage `go run [build flags] [-exec xprog] package [arguments...]`; Run compiles and runs the named main Go package (typically a list of `.go` source files) |
| **Dialect pinned** | **Go via gc 1.24** with `package main` + `fmt.Println` compile-and-run surface — **not** full modules / workspace / cgo / race suite claim |
| **URL** | https://pkg.go.dev/cmd/go@go1.24.4#hdr-Compile_and_run_Go_program (cmd/go @ go1.24.4); package `golang-go` 2:1.24~2 / `golang-1.24-go` 1.24.4-1 on Debian trixie; installed `go version` |
| **Anchors** | `go run` compiles and runs named main package; `.go` source files from a single directory; `fmt.Println` for string output (package fmt); optional `-exec` / build flags not required for this probe |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from pkg.go.dev cmd/go@go1.24.4 Compile and run Go program)

> **Compile and run Go program**
>
> Usage:
>
> `go run [build flags] [-exec xprog] package [arguments...]`
>
> Run compiles and runs the named main Go package. Typically the
> package is specified as a list of .go source files from a single
> directory, but it may also be an import path, file system path, or
> pattern matching a single known package, as in `go run .` or
> `go run my/cmd`.

(Source: Go Packages documentation for `cmd/go` at go1.24.4,
https://pkg.go.dev/cmd/go@go1.24.4#hdr-Compile_and_run_Go_program
section **Compile and run Go program**,
accessed 2026-09-28 Europe/Tirane.
Installed `go version` reports go1.24.4 and matches the
compile-and-run surface. Probe uses `go run HELLO.go` so the go
command compiles and runs the named main package from the `.go`
source file. Language: Go — see https://go.dev/.)

### Why this heading (HELLO.go / excavate)

A minimal HELLO surface looks like:

```go
package main

import "fmt"

func main() {
	fmt.Println("EMPEROR-TIME-GO-PROBE-OK")
}
```

in a `.GO` / `.go` file. That is exactly the pinned form:
**`go run FILE`** loads, compiles, and runs a main package from the
named `.go` source file(s), observe string print at run time.
Pinning cmd/go Compile and run lets excavate treat `golang` /
`go1.24` / `.go` + `fmt.Println` as **era evidence** (Go / Go source
file) without rewriting the fixture into a shell one-liner, a Python
port, or an interactive `go` REPL. Identify surveys `*.go` fossils on
disk. Bare `go` stays refused so English utterances do not false-route;
`.go` extension and `golang` / `go1.24` tags cover excavate intent.
