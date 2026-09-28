# Boot probe — lost-go / HELLO.go

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~09:33 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **golang-go** 2:1.24~2 (Debian meta; Depends **golang-1.24-go** 1.24.4-1) |
| Binary | `/usr/bin/go` |
| Reported | `go version go1.24.4 linux/amd64` |
| Install | already present on box (no apt this leaf) |

Probe used compile-and-run
(`go run HELLO.go`)
on a minimal `package main` / `fmt.Println` program. Identify fossils
use `*.go` only. Go on case-sensitive hosts requires a lowercase `.go` extension (uppercase `.GO` is not treated as a Go source file). Prefer `golang` / `go1.24` / `.go`. Bare `go`
is **refused** as a route tag because it is common English
("let's go", "go ahead"; word-boundary would still fire). Bare `.go` is
**allowed** (no known substring collision with peer excavate fossils).
Do not claim a full modules / workspace / cgo / race-detector suite
recovery from a `fmt.Println` probe alone — this leaf pins Go
compile-and-run via `go run`.

## Commands (VERIFIED)

```text
$ dpkg -l golang-go golang-1.24-go | awk '/^ii/ {print $2, $3}'
golang-1.24-go 1.24.4-1
golang-go:amd64 2:1.24~2

$ go version
go version go1.24.4 linux/amd64

$ which go
/usr/bin/go

$ go run HELLO.go
EMPEROR-TIME-GO-PROBE-OK
# (from evals/fixtures/lost-go; also works: go run evals/fixtures/lost-go/HELLO.go from repo root)
# exit 0
```

Note: cmd/go "Compile and run Go program" Usage is
`go run [build flags] [-exec xprog] package [arguments...]`.
Documented VERIFIED form is **`go run HELLO.go`**. Long help:
Run compiles and runs the named main Go package; typically the
package is specified as a list of .go source files from a single
directory. `fmt.Println` is the standard-library string-output call.

## Status

| Claim | Status | Evidence |
|-------|--------|----------|
| Source is Go fossil named `HELLO.go` | VERIFIED | `scripts/identify.sh evals/fixtures/lost-go` prints `1 *.go` |
| Runs under Go 1.24.4 compile-and-run | VERIFIED | `go run HELLO.go` exit 0 |
| Prints known string | VERIFIED | stdout contains `EMPEROR-TIME-GO-PROBE-OK` |
| Dialect is a specific modules / workspace / cgo claim | CONJECTURE | No go.mod / cgo / race jury beyond `fmt.Println` under go1.24.4 |
| Would run under period Go 1.0 / gccgo | UNVERIFIABLE here | No period Go ROM in this session |
| Full modules / workspace / cgo / race suite | UNVERIFIABLE here | single Println probe only |

## Not done (honest gaps)

- No Jail-hunt of the full Go language specification beyond
  cmd/go Compile and run (`go run`) + `fmt.Println` (deferred; pin is
  **`go run FILE`** — see `references/archaeology-go-manual.md`).
- Bare `go` is refused (common-English collision); use `golang` /
  `go1.24` / `.go`. Bare `.go` allowed (no peer collision).
- No `go.mod` / `go.work` fossil this leaf (modules / workspaces out of
  scope for the Println probe).
