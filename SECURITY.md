# Security Policy

## Supported versions

Security fixes apply to the current `main` tip of this public repository.
Pre-release tags such as `v1-alpha` are freeze labels, not a separate support
track.

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

Use GitHub's private vulnerability reporting for this repository:

1. Open https://github.com/arbi-elezi/emperor-time/security/advisories/new
2. Describe the issue, impact, and steps to reproduce
3. Wait for a maintainer response before any public disclosure

If private advisories are unavailable on your account, contact the repository
owner through GitHub (@arbi-elezi) and ask for a private channel. Do not paste
secrets, tokens, or personal data into public issues or pull requests.

## Scope notes

Emperor Time is local Markdown doctrine plus optional shell scripts. It has no
backend and collects no telemetry (see `PRIVACY.md`). Reports about third-party
harnesses (Claude Code, OpenCode, OpenRouter, and so on) belong with those
vendors unless the bug is in this repo's scripts or instructions.
