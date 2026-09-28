# Jail pin — PHP CLI Usage (`php` … file) for HELLO.php

Contemporaneous manual pin for the lost-php archaeology drill.
Doctrine: one heading, URL + access date + quote. Memory of "how PHP
works" stays **CONJECTURE** until a source/run is ledgered.

**Related work:** this leaf adds `evals/fixtures/lost-php/HELLO.php` with
runnable dialect **VERIFIED** as PHP 8.4.26 (cli)
under Linux x86_64
(`php HELLO.php` →
`EMPEROR-TIME-PHP-PROBE-OK`). Filename culture
(`.phtml` / `.phar` / web SAPI) remains
**CONJECTURE** only for web / packaging labels. Identify fossils use `*.php` only
(no `*.phtml` this leaf).
Bare `php` is **allowed** as a route tag (tool binary name;
word-boundary). Bare `.php` is **allowed** as a route tag with
extension-boundary matching (does not prefix-hit peer forms
`.php3` / `.php4` / `.php5` / `.phps`). Prefer `php` /
`php8` / `php8.4` / `php-cli` / `.php`.
Toolchain is Debian packages `php-cli` 2:8.4+96 and
`php8.4-cli` 8.4.26-1~deb13u1 providing
`/usr/bin/php`. This note supplies
the Jail pin so excavate can name the **verified** PHP
CLI file-argument run shape without inventing a full web SAPI /
Apache / Nginx / HHVM suite claim for an
`echo` probe.

---

## Pin (primary)

| Field | Value |
|-------|--------|
| **Manual** | *PHP Manual — Command line usage / Executing PHP files* |
| **Heading** | **Executing PHP files** — tell PHP to execute a certain file (`php my_script.php`) |
| **Dialect pinned** | **PHP via PHP 8.4.26 (cli)** with `echo` source → CLI file run — **not** full web SAPI / Apache / Nginx / HHVM suite claim |
| **URL** | https://www.php.net/manual/en/features.commandline.usage.php (PHP: Usage — Executing PHP files); Debian packages `php-cli` 2:8.4+96 / `php8.4-cli` 8.4.26-1~deb13u1; installed `php --version` |
| **Anchors** | `.php` / script file path as CLI argument; `-f` optional; CLI SAPI non-interactive file evaluation; `$argv[0]` set to the script name |
| **Access date** | 2026-09-28 (Europe/Tirane) |

### Quote (from PHP Manual — Executing PHP files)

> There are three different ways of supplying the CLI SAPI with PHP code
> to be executed:
>
> 1. Tell PHP to execute a certain file.
>
> ```
> $ php my_script.php
>
> $ php -f my_script.php
> ```
>
> Both ways (whether using the `-f` switch or not) execute the file
> `my_script.php`.

(Source: PHP Manual, section
**Executing PHP files**,
https://www.php.net/manual/en/features.commandline.usage.php
accessed 2026-09-28 Europe/Tirane.
Installed `php --version` reports PHP 8.4.26 (cli) and matches the
CLI file-argument surface. Probe uses
`php HELLO.php` so php
loads and runs the named script non-interactively and prints the probe
string. Language: PHP — see also the PHP CLI SAPI documentation.)

### Why this heading (HELLO.php / excavate)

A minimal HELLO surface looks like:

```php
<?php
echo "EMPEROR-TIME-PHP-PROBE-OK\n";
```

in a `.php` file. That is exactly the pinned form:
**`php FILE.php`**, observe string print at run time.
Pinning PHP Manual Executing PHP files lets excavate treat
`php` / `php8` / `php8.4` / `php-cli` / `.php` + `echo`
as **era evidence** (PHP / CLI file run) without rewriting the
fixture into a Node one-liner, a Python port, or an Apache virtual host.
Identify surveys `*.php` fossils on disk. `.php` extension (boundary-safe
vs `.php3` / `.php4` / `.php5` / `.phps`) and `php` /
`php8` / `php8.4` / `php-cli` tags cover excavate intent. web SAPI / HHVM is not the verified
toolchain.
