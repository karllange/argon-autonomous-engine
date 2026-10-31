# Agent workflow

Three agents share this repo. Read `AI_HANDOFF.md` at the start of every session. Update it before the session ends.

## Agents

### Gemini — Lead Architect & Conversion Strategist

Owns the blueprint, the architecture, the funnel and conversion strategy, and the task queue.

Writes Section 1 and Section 3 of `AI_HANDOFF.md`.

### Cursor Composer — Local Builder

Implements the blueprint on local branches. Does not invent a new offer or a new architecture.

Writes what was built into Section 1 of `AI_HANDOFF.md`.

### Grok Bot — 24/7 Cloud Scout, Funnel QA & Conversion Auditor

Audits the repo and the live pages. Checks CTAs, payment-link routing, console errors, mobile layout, and conversion friction. Reports findings. Does not patch the funnel unless a handoff task says to.

Writes Section 2 of `AI_HANDOFF.md`.

Works only on `grok/*` branches and opens pull requests. See Hybrid Auto-Merge for when Karl must approve and when the agent may merge.

## Strict rules

### Zero-PHI / HIPAA boundary

No protected health information and no patient-identifiable data anywhere: the repo, commits, issues, pull requests, logs, test data, screenshots, or handoff notes.

Use placeholder data only.

If PHI is found: stop. Do not copy it. Flag only its location in `AI_HANDOFF.md`.

### Secrets

Never expose private API keys or Stripe secret keys.

Stripe secret keys (`sk_live_` / `sk_test_`) and restricted keys (`rk_`) must never go in the repo, the client code, commits, logs, or the handoff.

Only publishable keys and public Payment Links may appear client-side.

Secrets go in environment variables or a secret store.

If a secret is found: report the file path and recommend rotating it. Never paste the value.

### Branches

Grok Bot must never push directly to `main`. This repo's default branch is `master`. Do not push to `master` either.

Grok Bot works only on `grok/*` branches and opens pull requests. Whether a PR waits for Karl is set in Hybrid Auto-Merge below.

## Hybrid Auto-Merge (set by Karl, Oct 31, 2026)

1. **Auto-merge permitted (no need to wait for Karl).** Once the `gemini-3.5-flash` compliance/quality review (`/home/box/tools/gemini_review.py`) passes and its fixes that follow Karl's copy rules are applied, the agent may open the PR, Squash & Merge it, and delete the branch itself, for any PR that ONLY touches: `/marketing/`, `kit-draft/`, `AI_HANDOFF.md`, `AGENTS.md`, or documentation/README files. After merging, send Karl a brief summary.
2. **Manual approval required (wait for Karl's 1-tap approval).** Any PR that changes live public HTML pages (`index.html` or any other served HTML), live CSS/JS, or `config.js` (pricing, Stripe links, webhooks) must stay open until Karl approves it. If a PR mixes allowed and gated files, the whole PR waits.
3. Unchanged: never push directly to main/master; always work on `grok/*` branches. The copy rules above (no invented refund/guarantee policies, cellular structure/function language only, no stats/testimonials) still apply to everything auto-merged.

### Clipboard

Every agent reads `AI_HANDOFF.md` at the start of a session and updates it at the end of every session, with the date, the agent, and what changed.
