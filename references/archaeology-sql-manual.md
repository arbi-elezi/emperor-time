# Jail pin — SQLite CLI Reading SQL from a file (`.read` …) for HELLO.sql

Contemporaneous manual pin for the lost-sql archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how SQLite
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-sql/HELLO.sql` with
runnable dialect **VERIFIED** as SQLite 3.46.1 CLI
under Linux x86_64
(`sqlite3 -batch :memory: ".read HELLO.sql"` →
`EMPEROR-TIME-SQL-PROBE-OK`). Filename culture
(`.sqlite` / `.db` / `.sqlite3` binary DB files) remains
**CONJECTURE** only for on-disk database labels. Identify fossils use `*.sql` only
(no `*.sqlite` / `*.db` this leaf).
Bare `sql` is **allowed** as a route tag (three-letter language abbreviation;
word-boundary). Bare `sqlite` is **allowed** as a route tag (tool / language
name; word-boundary). Bare `.sql` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.sqlite` / `.sqlite3` / `.sqlitedb`). Prefer `sqlite` /
`sqlite3` / `sqlite3.46` / `.sql`.
Toolchain is Debian package `sqlite3` 3.46.1-7+deb13u2 providing
`/usr/bin/sqlite3`. This note supplies
the Jail pin so excavate can name the **verified** SQLite
CLI `.read` file-evaluation shape without inventing a full PostgreSQL /
MySQL / MSSQL suite claim for a
`SELECT` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *Command Line Shell For SQLite — Reading SQL from a file* |
| **Heading** | **7.2. Reading SQL from a file** — `.read FILE` takes SQL (and dot-commands) from a named script |
| **Dialect pinned** | **SQL via SQLite 3.46.1 CLI** with `SELECT` source → `.read` file evaluation on `:memory:` — **not** full PostgreSQL / MySQL / MSSQL suite claim |
| **URL** | https://sqlite.org/cli.html (Command Line Shell For SQLite — §7.2 Reading SQL from a file); Debian package `sqlite3` 3.46.1-7+deb13u2; installed `sqlite3 --version` |
| **Anchors** | `.sql` / script file path as `.read` argument; `-batch` non-interactive; `:memory:` transient database; stdin redirect also documented as launch-time file input |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from Command Line Shell For SQLite — §7.2 Reading SQL from a file)

> In interactive mode, sqlite3 reads input text (either SQL statements or
> dot-commands) from the keyboard. You can also redirect input from a file
> when you launch sqlite3, of course, but then you do not have the ability
> to interact with the program. Sometimes it is useful to run an SQL script
> contained in a file while entering other commands from the command-line.
> For this, the ".read" dot-command is provided.
>
> The ".read" command takes a single argument which is (usually) the name
> of a file from which to read input text.
>
> ```
> sqlite> .read myscript.sql
> ```
>
> The ".read" command temporarily stops reading from the keyboard and
> instead takes its input from the file named.

(Source: Command Line Shell For SQLite, section
**7.2. Reading SQL from a file**,
https://sqlite.org/cli.html
accessed 2026-09-28 Europe/Tirane.
Installed `sqlite3 --version` reports 3.46.1 and matches the
CLI `.read` / file-input surface. Probe uses
`sqlite3 -batch :memory: ".read HELLO.sql"` so sqlite3
loads and runs the named script non-interactively against a transient
in-memory database and prints the probe
string. Language: SQL / SQLite — see also the SQLite CLI documentation.)

### Why this heading (HELLO.sql / excavate)

A minimal HELLO surface looks like:

```sql
SELECT 'EMPEROR-TIME-SQL-PROBE-OK';
```

in a `.sql` file. That is exactly the pinned form:
**`sqlite3 -batch :memory: ".read FILE.sql"`**, observe string print at run time.
Pinning SQLite CLI §7.2 Reading SQL from a file lets excavate treat
`sqlite` / `sqlite3` / `sqlite3.46` / `.sql` + `SELECT`
as **era evidence** (SQL / SQLite CLI `.read`) without rewriting the
fixture into a Python one-liner, a PHP port, or a PostgreSQL `psql -f` claim.
Identify surveys `*.sql` fossils on disk. `.sql` extension (boundary-safe
vs `.sqlite` / `.sqlite3` / `.sqlitedb`) and `sqlite` /
`sqlite3` / `sqlite3.46` / `sql` tags cover excavate intent. Other SQL engines are not the verified
toolchain.
