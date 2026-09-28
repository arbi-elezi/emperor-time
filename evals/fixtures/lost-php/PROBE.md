# Boot probe — lost-php / HELLO.php

Host: Debian GNU/Linux 13 (trixie), x86_64  
Clock: box local Europe/Tirane (CEST / UTC+2)  
Probe date: 2026-09-28 ~11:11 CEST

## Toolchain

| Item | Value |
|------|-------|
| Package | **php8.4-cli** 8.4.26-1~deb13u1 + meta **php-cli** 2:8.4+96 (Debian trixie) |
| Binary | `/usr/bin/php` → php8.4 |
| Reported | `PHP 8.4.26 (cli) (built: Sep 24 2026 17:16:18) (NTS)` |
| Install | `sudo apt-get install -y php-cli` this leaf (apt Worthy Spend after Bash zero-install) |

Probe used `php HELLO.php` on a minimal `echo` program.
Identify fossils use `*.php` only (no `*.phtml` this leaf). Prefer `php` /
`php8` / `php8.4` / `php-cli` / `.php`.
Bare `php` is **allowed** as a route tag (tool binary name; word-boundary).
Bare `.php` is **allowed** with extension-boundary matching (does not
prefix-hit `.php3` / `.php4` / `.php5` / `.phps`). Classic scripting leaf after
Bash; treats PHP as peer fossil not house twin language. Do **not**
claim a full PHP web SAPI / Apache / Nginx / HHVM recovery from an `echo`
CLI probe alone — this leaf pins `php` file-argument CLI run.

## Commands (VERIFIED)

```text
$ which php
/usr/bin/php

$ php --version | head -1
PHP 8.4.26 (cli) (built: Sep 24 2026 17:16:18) (NTS)

$ php HELLO.php
EMPEROR-TIME-PHP-PROBE-OK
```

## Dialect labels

| Claim | Status |
|-------|--------|
| Host runs `php` 8.4.26 CLI on `HELLO.php` → probe string | VERIFIED |
| Filename culture (`.phtml` / `.phar` / web SAPI) maps to this dialect | CONJECTURE (probe uses plain `.php` + `php` file arg) |
| Full PHP web SAPI / Apache / Nginx / HHVM recovery | UNVERIFIABLE from echo CLI probe alone |
| bare `hhvm` as verified php toolchain | REJECTED (not used this leaf) |
