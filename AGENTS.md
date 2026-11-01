# Agent workflow

Three agents share this repo. Read `AI_HANDOFF.md` at the start of every session. Update it before the session ends.

## Master Project Blueprint Manager (Karl, Nov 1 2026)

Every agent that works in `argon-autonomous-engine` (Grok Bot, Gemini, Cursor) follows the same loop:

1. **Start of session:** read `AGENTS.md`, then `AI_HANDOFF.md`, before touching anything.
2. **During the session:** work only on a `grok/*` branch (or the agent's own feature branch) and open a pull request. Never push to the default branch. Never force-push.
3. **End of session:** update `AI_HANDOFF.md`: Completed Today (dated), Pending Tasks, the Next Immediate Micro-Step (tagged `[Phone-Friendly]` or `[Mac/PC Deep Build]`), and the Gemini Review Log when a review ran. Record facts only: what changed, which PR or commit, and what is still open.

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

## Pre-Production PHI Lockout Gate (Final-Stage Security Gate)

- Grok Bot has full repo access during the architecture, UI, and synthetic-data phases of development.
- **HALT condition.** Before any clinical or local Gemma project moves from synthetic test data to live clinical or PHI integration, or connects to any `@physioworks.clinic` BAA endpoint, Grok Bot and Gemini must both **stop work** and tell Karl to revoke Grok's access or switch to a Fine-Grained Token that excludes that repo. No agent continues on that repo until Karl confirms the access change.
- **Zero-PHI, always.** No protected health information and no patient-identifiable data in the repo, commits, branches, issues, pull requests, logs, test fixtures, screenshots, or handoff notes. That includes names, dates of birth, contact details, record or claim numbers, referral documents, and diagnoses tied to a person. Use synthetic or placeholder data only.
- If PHI is found: stop. Do not copy it anywhere. Record only its location (file path or URL) in `AI_HANDOFF.md` and tell Karl.

## Secrets (all agents, in addition to the Stripe rule above)

- Never commit, paste, or log secrets: Stripe secret or restricted keys, `GEMINI_API_KEY`, GitHub or other access tokens, private keys, passwords, or webhook URLs.
- Secrets live in environment variables or a secret store, never in the repo or in `AI_HANDOFF.md`.
- If a secret is found, report the file path only and recommend rotating it. Never paste the value.

## gemini-3.5-flash API Audit

1. Save the PR diff to a file and run `python3 /home/box/tools/gemini_review.py <diff-file> gemini-3.5-flash`.
2. Apply only the fixes that follow Karl's rules in this file. Do not add prices, guarantees, refund terms, discounts, or claims because a reviewer suggested them. Those are Karl's decisions.
3. If the review flags a real compliance or safety issue that cannot be fixed within these rules, leave the PR open and tell Karl why.
4. Log the result in `AI_HANDOFF.md` (Gemini Review Log) as **"Gemini API Compliance Approved (gemini-3.5-flash)"** with the date, the PR, the verdict, what was applied, and what was skipped and why.

## Copy and identity rules

- Always "Karl Lange, PT". Never "Dr.".
- No treat, cure, diagnose, or prevent claims. Cellular structure/function language only when health topics come up. No invented stats or testimonials.
- Never invent refund, guarantee, trial, or risk-free policies. Those are Karl's decisions.
- No "pain" in section headers.
- This repo is **public** and `gh-pages` serves the published files. Anything committed here can be read by anyone. Keep only `master` and `gh-pages` as long-lived branches.
- Hybrid Auto-Merge allowlist for this repo: `/marketing/`, `kit-draft/`, `AI_HANDOFF.md`, `AGENTS.md`, and documentation/README files. Served HTML (`index.html`, `funnel/`), `config.js`, `controller/`, `engine_state.json`, and `.github/workflows/` are gated.

### Clipboard

Every agent reads `AI_HANDOFF.md` at the start of a session and updates it at the end of every session, with the date, the agent, and what changed.
