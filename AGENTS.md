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

Works only on `grok/*` branches and opens pull requests.

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

Grok Bot works only on `grok/*` branches and opens pull requests for human review. Karl Lange merges.

### Clipboard

Every agent reads `AI_HANDOFF.md` at the start of a session and updates it at the end of every session, with the date, the agent, and what changed.
