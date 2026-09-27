# Isolation checklist — worktree HARD-GATE

**Provenance (aspect, not whole skill):**
- source: https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md
- source-hash: sha256:8cfb86f121269e8f7f12361e6795c4f6738828340e28964c9229d365666c9edd
- heading: Step 0 Detect Existing Isolation + Step 1 Create + Step 2 Setup + Step 3 Baseline
- license: MIT
- issue-context: emperor-worktree had create scripts but no enforceable detect→native/git→ignore-safety→baseline card; Chain Jail extract-aspect names isolation HARD-GATE only (not whole using-git-worktrees skill, not rationalization essays)

**Contract:** before standard or heavy BUILD that mutates a client checkout, complete the isolation checklist. Detect first. Prefer native harness tools. Fall back to git worktree only when no native tool exists. Never create under an unignored directory. Prove a green baseline before implementing. Emperor Time stays the orchestrator via emperor-worktree + BUILD; do **not** announce or load whole `using-git-worktrees`.

Mechanical card: `scripts/emperor iso` (Python: `scripts/lib/worktree_iso.py`).
Create helper (after checklist): `scripts/emperor worktree <id>`.

## HARD-GATE — Detect before create

```
NO MUTATE WITHOUT ISOLATION DETECT FIRST
```

Skip Step 1 detection and jump straight to `git worktree add`? **Stop.** Run detect.
Already in a linked worktree (and not a submodule)? Stay — do not nest another.
Submodule (`git rev-parse --show-superproject-working-tree` returns a path)? Treat as normal repo.

Trivial tasks may stay on the current tree. Record `worktree: skipped (trivial)` in the ledger and still quote Step 1 detect result.

## Isolation steps

Complete each step before the next. Mechanical `--advance` rejects skips.
`--reject-blind-create` always fails (hard gate when creating without detect).

### Step 1: DETECT — Existing isolation

Run:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
git rev-parse --show-superproject-working-tree 2>/dev/null
git branch --show-current
```

- `GIT_DIR != GIT_COMMON` and **not** a submodule → already isolated. Skip create. Report path + branch (or detached).
- Else → normal checkout (or submodule). Continue.

ET: ledger `isolation: linked | normal | submodule` before any create.

### Step 2: PREFER-NATIVE — Harness tool or consent

If already isolated (Step 1), skip to Step 5 setup/baseline.

Else: prefer a native worktree tool (`EnterWorktree`, `/worktree`, `--worktree`) when the host has one. Only fall back to git when none exists.

Honor standing client preference. If none is declared and create would touch a dirty primary checkout, ask consent once. Declined → work in place; still run baseline (Step 5).

### Step 3: DIR-SAFETY — Location + check-ignore

Priority: explicit client preference → existing `.worktrees/` → existing `worktrees/` → default `.worktrees/`.

**MUST** verify ignore before create:

```bash
git check-ignore -q .worktrees || git check-ignore -q worktrees
```

Not ignored? Add to `.gitignore`, commit that ignore change alone, then proceed. Unignored worktree dirs commit the whole tree into the repo.

### Step 4: CREATE-ENTER — Isolated workspace

Native tool if Step 2 chose it. Else:

```bash
git worktree add "$LOCATION/$BRANCH_NAME" -b "$BRANCH_NAME"
# or: scripts/emperor worktree <task-id>
cd "$LOCATION/$BRANCH_NAME"
```

Sandbox/permission denial → report, work in place, continue to Step 5. Do not invent success.

### Step 5: SETUP-BASELINE — Deps + green suite

Auto-detect install (`package.json` / `Cargo.toml` / `requirements.txt` / `pyproject.toml` / `go.mod`). Then run the project suite.

- Failures: report; ask whether to proceed or investigate. Do not silently BUILD on a dirty baseline.
- Pass: report ready path + suite summary. Then BUILD / TDD may start.

## Rationalizations (refuse)

| Excuse | Reality |
|---|---|
| "Obviously not in a worktree" | Run Step 1. Harness isolation and submodules fool eyeballing. |
| "`git worktree add` is faster than hunting native tools" | Native tools own placement, branch, cleanup. Bypassing them creates phantom state. |
| "Directory is surely ignored" | Run `git check-ignore`. |
| "Baseline can wait; tree is fresh" | Dirty baseline makes every later failure ambiguous. |

## ET mapping

| Step | ET home |
|---|---|
| 1 DETECT | emperor-worktree + ledger |
| 2 PREFER-NATIVE | consent / host tool |
| 3 DIR-SAFETY | `.gitignore` + Vow of Evidence |
| 4 CREATE-ENTER | `scripts/emperor worktree` |
| 5 SETUP-BASELINE | BUILD entry / scientific-method |

After G4 PASS, finish menu owns merge/PR/keep and owned-worktree cleanup (`skills/emperor-forge/finish-menu.md`).
