# Contributing to Emperor Time

Thanks for looking. Keep changes small and honest. This repo is an Agent Skills
coding harness (Claude Code plugin + adapters). Product shipping for et-unlimited
is separate; this tree is the public skill.

## Install and try a tiny ask

Claude Code (plugin marketplace):

```
/plugin marketplace add arbi-elezi/emperor-time
/plugin install emperor-time@emperor-time
```

Open a **new** session in some other repo. Confirm the SessionStart activate
card. Ask a one-line nit ("fix typo in README"). It should stay **tiny**.

Shell copy install (macOS / Linux):

```bash
chmod +x scripts/*.sh
./scripts/install.sh claude-code user
./scripts/dowse.sh
```

PowerShell Core:

```powershell
.\scripts\install.ps1 -Harness claude-code -Scope user
```

OpenCode / ORI mid-model path: see README ("Mid-model live path") and
`adapters/opencode/ORI-REGRESSION.md`.

## What to change

- Docs, adapters honesty, evals, and small script hygiene are welcome.
- Do not invent stack claims. Do not bump the skill version unless the change
  truly requires it.
- Doctrine lives in `SKILL.md` and `references/`. Read before rewriting.

Useful pointers:

- When to engage: `references/meta/when-to-engage.md`
- Kill / hold: `references/kill-hold.md`
- Privacy: `PRIVACY.md`
- Security reports: `SECURITY.md`
- Conduct: `CODE_OF_CONDUCT.md`

## Issues

Use the issue forms (bug or feature). Say what you ran, what you expected, and
what you got. Include harness (Claude Code, OpenCode, etc.) and OS when it
matters. No need for AI-generated filler.

## Pull requests

1. Branch off current `main`.
2. One clear concern per PR.
3. Prefer tiny diffs. Show the command you used to check (install, cold check,
   or a script).
4. Do not force-push rewritten history on shared branches. Do not amend published
   commits on `main`.
5. Fill the PR body with what changed and how you verified. Leave merge to the
   maintainer unless they ask otherwise.

## Social preview (maintainer)

GitHub's repo social preview image is set in **Settings > General > Social
preview**. Upload `assets/shovel.png`, or a 1280×640 crop/resize of it. The API
path for OG images is limited; this is a Settings click, not a merge.

## License

Contributions land under the repo `LICENSE` (MIT unless that file says
otherwise).
