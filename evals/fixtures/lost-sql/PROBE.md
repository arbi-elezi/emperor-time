# Boot probe — lost-sql / HELLO.sql

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~11:25 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **sqlite3** 3.46.1-7+deb13u2 (Debian trixie) |
| Binary | `/usr/bin/sqlite3` |
| Reported | `3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1 (64-bit)` |
| Install | `sudo apt-get install -y sqlite3` this leaf (apt Worthy Spend ~601 kB after PHP; still prefer over TeXlive / C++ apt) |

Probe used `sqlite3 -batch :memory: ".read HELLO.sql"` on a minimal
`SELECT` program.
Identify fossils use `*.sql` only (no `*.sqlite` / `*.db` / `*.sqlite3` this leaf). Prefer `sqlite` /
`sqlite3` / `sqlite3.46` / `.sql`.
Bare `sql` is **allowed** as a route tag (three-letter language abbreviation; word-boundary).
Bare `sqlite` is **allowed** as a route tag (tool / language name; word-boundary).
Bare `.sql` is **allowed** with extension-boundary matching (does not
prefix-hit `.sqlite` / `.sqlite3` / `.sqlitedb`). SQL scripting leaf after
PHP; treats SQLite SQL as peer fossil not house twin language. Do **not**
claim a full PostgreSQL / MySQL / MSSQL recovery from a sqlite3 CLI probe
alone — this leaf pins `sqlite3` `.read` file evaluation on a transient
`:memory:` database.

## Commands (VERIFIED)

```text
$ which sqlite3
/usr/bin/sqlite3

$ sqlite3 --version
3.46.1 2024-08-13 09:16:08 c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69aalt1 (64-bit)

$ sqlite3 -batch :memory: ".read HELLO.sql"
EMPEROR-TIME-SQL-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `sqlite3` 3.46.1 CLI `.read` on `HELLO.sql` → probe string | VERIFIED |
| Filename culture (`.sqlite` / `.db` / `.sqlite3` binary DB files) maps to this dialect | CONJECTURE (probe uses plain `.sql` + `.read`) |
| Full PostgreSQL / MySQL / MSSQL / other SQL engine recovery | UNVERIFIABLE from sqlite3 CLI probe alone |
| bare `psql` / `mysql` as verified sqlite toolchain | REJECTED (not used this leaf) |
