# Git Cheat Sheet — SDET Daily Reference

Two lists to memorize. List A happens **once per project**. List B happens **every single day** you touch the code, for your entire career.

## A. One-time setup (brand-new project)

1. `git init` — turn this folder into a Git repo
2. Write/create your first files
3. `git add .` — stage everything
4. `git commit -m "chore: initial commit"` — first snapshot
5. On GitHub: create a new **empty** repo (no README/license — avoids conflicts with step 6)
6. `git remote add origin <repo-url>` — link local repo to GitHub
7. `git branch -M main` — name the default branch `main`
8. `git push -u origin main` — upload, and remember this link for future pushes

After this, steps 5-8 never happen again for this project. You're in List B forever.

## B. The daily loop (memorize this — you'll type it hundreds of times)

1. `git status` — what changed since my last commit?
2. `git diff` — show me the exact line-by-line changes (read this *before* staging — catches mistakes early)
3. `git add <file>` (a specific file) or `git add .` (everything) — stage what you want in this commit
4. `git commit -m "type: short description"` — snapshot it
5. `git push` — upload to GitHub

Mnemonic: **S-D-A-C-P** — Status, Diff, Add, Commit, Push. Say it in order and you've got the whole daily loop.

## Commit message convention (used at real companies)

Prefix your message with what kind of change it is:

- `feat:` — new functionality (e.g. a new test, a new page object)
- `fix:` — fixing a bug
- `test:` — adding/changing tests specifically
- `docs:` — documentation only (README, notes)
- `chore:` — setup/config/maintenance, no logic change
- `refactor:` — restructuring code, behavior unchanged

Example: `git commit -m "test: add smoke tests for login page"`

## Habits to build now, not later

- Keep commits small and focused — one logical change per commit, not "did a bunch of stuff today"
- Always `git diff` before `git add` — never stage something you haven't actually looked at
- Never commit secrets (passwords, API tokens, `.env` files) — that's exactly what `.gitignore` is for
- Write the commit message as if someone else has to understand your change with zero other context — because eventually, someone will (including future you)

## Coming later (added to this file as we cover them)

- `git log` / `git blame` — find which commit/who introduced a specific change (real debugging tool)
- `git checkout -b feature/xyz` — branching, so you can build a new test without touching main
- `git checkout main && git merge feature/xyz` — bringing a branch's work back in
- Pull requests, code review, resolving a merge conflict
- `git pull` — pulling down teammates' changes (matters once you're not the only one committing)
- `git stash` — temporarily shelve unfinished changes
