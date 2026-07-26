# SmileCare SDET Automation

Personal test automation project built while training for an SDET (5+ yrs level) role.
Target application: [SmileCare Medicine](https://www.smilecaremedicine.com/) (React + PocketBase + Stripe e-commerce site).
Full 12-week learning plan: see `SmileCare_SDET_12_Week_Roadmap.docx` (kept alongside this repo, not committed — see note below).

This is a **separate repo from the production app**. It only *tests* SmileCare; it never lives inside the app's own monorepo.

## Stack

- Python 3.x
- Playwright (UI automation)
- pytest (test runner / framework)
- requests (API automation)
- GitHub Actions + Jenkins (CI/CD)
- Grafana + Prometheus (test result observability) — added in Week 11

## Folder structure

```
config/         environment settings (base URLs, timeouts) read from .env
pages/          Page Object Model classes (one per SmileCare page)
api_clients/    one client class per PocketBase collection (users, products, cart, orders, categories)
tests/ui/       Playwright UI tests
tests/api/      API tests (requests-based)
tests/unit/     plain Python unit tests (no browser/API) — used in Week 1-2
utils/          shared helpers (test data builders, waits, etc.)
learning/       week-by-week lesson scripts and notes (not "real" framework code — this is scratch/practice)
.github/workflows/  GitHub Actions CI pipelines (added Week 9)
```

## Setup (do this once)

```bash
cd SmileCare-SDET-Automation
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install
copy .env.example .env       # then edit if needed
```

## Running tests (from Week 4 onward)

```bash
pytest -m smoke              # fast critical-path suite
pytest -m regression         # full suite
pytest tests/api             # API tests only
pytest tests/ui              # UI tests only
```

## Pushing this to your own GitHub (do this today, Week 1 Day 1)

Run these from inside this folder, in the VS Code terminal:

```bash
git init
git add .
git commit -m "chore: project scaffold"
```

Then on github.com: create a new **empty** repository (no README/license) named `smilecare-sdet-automation`, and run the two commands it shows you, e.g.:

```bash
git remote add origin https://github.com/<your-username>/smilecare-sdet-automation.git
git branch -M main
git push -u origin main
```

From then on, after each lesson: `git add . && git commit -m "week1 day2: ..." && git push`.

## Safety note

This targets a **live production site**. Never automate real checkout/payment submission, account deletion, or product create/update/delete against production — see `SmileCare Medicines API/README.md` and the SDET guide docx for which endpoints are safe (VERIFIED LIVE, read-only) vs. ones that needs a dedicated test account first (INFERRED, write endpoints).
