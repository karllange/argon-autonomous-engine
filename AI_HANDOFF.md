# AI handoff clipboard

Shared scratch pad for Gemini, Cursor Composer, and Grok Bot. Newest entry in each section goes on top. Do not paste secrets, payment credentials, or PHI. Use placeholder data only.

---

## Section 1: Active Blueprint Status (Gemini + Cursor Composer)

**Who writes this:** Gemini (blueprint, architecture, funnel strategy, task queue) and Cursor Composer (what was implemented on a local branch).

### Entry template

```
### YYYY-MM-DD — Agent name
- Blueprint status:
- What changed:
- Branch / PR:
- Open questions for the other agents:
```

No entry yet.

---

## Section 2: Grok Bot -> Gemini & Cursor (Funnel QA & Conversion Notes)

**Who writes this:** Grok Bot only. Findings from repo and live-page audits. Ordered by priority. State what was observed. Mark anything not tested, and why.

### Entry template

```
### YYYY-MM-DD — Grok Bot
- Pages checked:
- Priority findings:
  1.
- Untested:
- Screenshots:
```

### 2026-10-31 — Grok Bot — initial funnel audit

- Pages checked: `https://karllange.github.io/argon-autonomous-engine/` and `https://karllange.github.io/argon-autonomous-engine/funnel/index.html`.
- How: Playwright 1.64 driving headless Chrome. Desktop 1440×900. Mobile 390×844. No card number was entered. No Pay button was clicked. Placeholder email `audit@example.com` was used.
- Both URLs returned HTTP 200 and rendered the same document (decoded body 17,650 bytes, visible text length 1,469, same title and H1). In the repo, `index.html` and `funnel/index.html` are byte-identical. `variant-b.html` and `vault-access.html` match their `funnel/` copies the same way.

Screenshots from this run are attached to the pull request. They are not committed in the repo.

- `root-desktop-viewport.png`, `root-mobile-viewport.png` — first screen
- `root-desktop-modal-core.png`, `root-mobile-modal-core.png` — checkout modal at $97
- `root-desktop-modal-bump-checked.png`, `root-mobile-modal-bump.png` — build-kit bump at $394
- `root-desktop-stripe-core.png`, `root-desktop-stripe-bundle.png`, `root-mobile-stripe-core.png` — Stripe checkout stopped at page load
- `stripe-placeholder-upsell.png` — broken upsell link
- `funnel-desktop-viewport.png`, `funnel-mobile-viewport.png` — same page at the `/funnel/` URL

#### P1. Both live checkout links are Stripe Sandbox. A real card will not complete a sale.

Observed on the core link and the bundle link, from the modal and from a direct load.

- Core Payment Link path: `buy.stripe.com/test_dRm14gfqDc9Nae1fBC5AQ00`
- Bundle Payment Link path: `buy.stripe.com/test_00waEQdiv8XBgCpahi5AQ01`
- Checkout title and header: "Realistic Solutions, Inc sandbox" with a visible **Sandbox** badge.
- Direct GET of each link returned HTTP 200 and the same checkout.
- Stripe.js logged, on the direct loads only: payment method types `link`, `klarna`, and `amazon_pay` are not activated. They are shown in test mode and will be hidden in live mode.
- Some Stripe-hosted requests failed on the checkout page (`net::ERR_BLOCKED_BY_ORB` on a CloudFront URL, and aborted hCaptcha logo images). Those failures were on Stripe's page, not on the ARGON pages.

Action: replace both links with live Payment Links before any paid or organic traffic. Keep the product names and prices below. Do not put a secret key in the repo. Publishable keys and public Payment Links only.

#### P1. The products and prices that did load match the modal. The separate $297 upsell link does not.

| Step | Page copy | Stripe checkout | Match |
| --- | --- | --- | --- |
| Hero CTA, bump unchecked | Modal total $97.00, button "Continue — $97.00". Line: "The Blueprint" / "The practical guide to building your own AI-driven revenue engine." | "The Blueprint", **$97.00**, same description. Email field showed `audit@example.com` (prefilled from the query string). | Yes |
| Build-kit checkbox on | Line items $97.00 + $297.00 "Build kit". Total **$394.00**. Button "Continue — $394.00". | "The Blueprint + Build Kit", **$394.00**. Description matches the bump sentence about the page, the checkout, and the scripts. | Yes |

Checked on the root page at desktop (both prices) and mobile (core price, and the $394 modal state). The `/funnel/index.html` desktop path opened the same $97 checkout.

The other Payment Link in the repo is not on these two pages. `vault-access.html` (root and `funnel/`) points the "Upgrade for $297" control at `buy.stripe.com/test_argon_boilerplate_upsell_297`. A direct GET returned **HTTP 403**. The body was an XML `AccessDenied` error, not a Stripe checkout. Screenshot: `stripe-placeholder-upsell.png`.

Action: delete that placeholder or replace it with a real Payment Link for $297. Until then, core buyers who open the fulfillment page cannot upgrade.

#### P1. `#vault-offer` is gone from the live homepage, and the emails still point at it.

Observed: loading `https://karllange.github.io/argon-autonomous-engine/#vault-offer` left `scrollY` at 0. `document.getElementById("vault-offer")` was null on both audited URLs.

The id still exists on `variant-b.html`. These still target the homepage hash:

- `vault-access.html` "Return to checkout" → `./index.html#vault-offer`
- `creatives/email_nurture_sequence.md` uses the homepage URL with `#vault-offer`

Action: point those links at a real control (the homepage CTA opens a modal; it is not an anchor), or restore an element with that id.

#### P2. The first screen does not say what is for sale, and a different dollar figure competes with $97.

Observed at 1440 and 390. No horizontal overflow (`scrollWidth` equals the viewport). Hero CTA is on the first screen (desktop box bottom 513 of 900; mobile bottom 469 of 844).

What the first screen actually shows:

- Header: wordmark "ARGON" (`href="#top"`) and a button "Get the Blueprint".
- H1: "The AI Wave is Here. Don't Get Left Behind."
- Subhead about a survival guide for everyday folks. No price, no contents, no proof.
- The same "Get the Blueprint" button again.
- Then the kicker "WHY I BUILT THIS" and the heading **"The $300/Month Empire"** are already visible before any $97.

The $97 price appears only after the modal opens. The modal says "One-time access, sent to your email." There is no refund line, no testimonials, no founder name, and no security note on the page or in the modal.

Three buttons on the page all open the same modal. They do not compete with each other. The $300 heading does compete with the $97 offer.

Action for Gemini: one offer sentence above the fold (what it is, who it is for, $97, what happens after click). Move or rewrite "The $300/Month Empire" so it cannot be read as the price.

#### P2. Checkout is two email steps and a new tab. Fulfillment after pay was not tested.

Observed path:

1. Click "Get the Blueprint" (hero). Modal opens (`role="dialog"`, `aria-modal="true"`).
2. Empty email does not pass `checkValidity()` (`false`). The browser's validation bubble was not opened, so that UI is untested.
3. Submit posts to the Google Apps Script lead URL, then calls `window.open` on the Payment Link. In this run the new tab opened (popup was not blocked). The modal then shows "Continue if nothing opens" with the same Payment Link.
4. Stripe shows its own email field. The placeholder address was prefilled. Card fields were visible (Card, Cash App Pay, Affirm, Klarna, Bank, Pay). They were not filled. Pay was not clicked.

This audit intercepted the lead POST and answered HTTP 204 locally, so nothing was written to the sheet. Webhook delivery is **untested** on purpose.

Whether Stripe's success URL returns to `vault-access.html?tier=core` or `?tier=bundle` is **untested**, because payment was not submitted.

`window.open` under a normal popup blocker is **untested**. The fallback link is present.

Action: send the buyer to the Payment Link in the same tab, and drop the extra email field unless the webhook is required before Stripe. Confirm each live Payment Link's success URL against the fulfillment page.

The Stripe account name on the pay step is "Realistic Solutions, Inc", not ARGON. That is a trust drop at the moment of payment.

#### P2. A few tap targets are small. The page is otherwise readable on a 390px screen.

Measured on both audited URLs, both widths:

| Control | Size | Note |
| --- | --- | --- |
| Header "Get the Blueprint" | 141×38 | Under 44px tall. It is the sticky CTA. |
| "ARGON" wordmark | 68×23 | Under 44px. It only jumps to `#top`. |
| Modal close | 32×32 | Under 44px. Top was 120px on the 390px modal. |
| Order-bump checkbox | 13×16 | The label row is 266×104, so the row itself is tappable. |
| Hero "Get the Blueprint" | 161×48 | Meets 44px. |
| Modal submit | 48px tall (300px wide on mobile, 494px on desktop) | In view for the $97 modal and for the $394 bump modal (mobile submit bottom 757 of 844). |

Mobile type: H1 43.2px, subhead 18.4px, body 16px. No horizontal overflow with the bump modal open.

Action: raise the header button and the close control to at least 44×44.

#### P3. Landing pages are fast and clean. SEO basics are only partly there.

No console errors, no `pageerror`, and no failed network requests on either landing page at either width.

Load timing from this environment (GitHub Pages, second view was faster):

| Page | Viewport | HTTP | TTFB | DOMContentLoaded | loadEventEnd |
| --- | --- | --- | --- | --- | --- |
| `/` | 1440 | 200 | 54 ms | 118 ms | 154 ms |
| `/` | 390 | 200 | 16 ms | 73 ms | 106 ms |
| `/funnel/index.html` | 1440 | 200 | 46 ms | 102 ms | 127 ms |
| `/funnel/index.html` | 390 | 200 | 17 ms | 70 ms | 109 ms |

The hero was not slow.

Present in `<head>`: `lang="en"`, charset, viewport, title ("The AI Wave is Here. Don't Get Left Behind."), meta description, `theme-color`. Stylesheet links are Google Fonts only.

Missing on the live head: canonical URL, Open Graph tags, Twitter card, favicon link. `GET /favicon.ico` returned **404**.

#### P3. Repo, build, and GitHub Pages

- No `package.json`, lockfile, or README. No build step. The homepage is one static HTML file with a plain `<style>` and `<script>`. `controller/evaluate_funnel.py` uses the Python standard library only. `variant-b.html` loads Tailwind from the CDN. The audited homepage does not.
- GitHub Pages is **built** from branch `gh-pages`, path `/`, and is public. `https://karllange.github.io/argon-autonomous-engine/` is that site.
- The workflow that actually runs is `.github/workflows/deploy-funnel.yml`. On push to `master` or `main` it checks out `gh-pages`, copies `funnel/index.html`, `variant-b.html`, `vault-access.html`, `funnel/downloads`, and `engine_state.json` onto that branch, and pushes `gh-pages`.
- `controller/deploy-funnel.yml` is a second Pages workflow (upload `./funnel` as the site root). It is **not** in `.github/workflows/`, so it does not run. Do not move it into place without deciding the URL map. Publishing only `./funnel` would remove `/funnel/index.html` as a separate path and would change what `/` is.
- Because Pages serves the whole `gh-pages` tree, non-page files are public. Observed HTTP 200 for `engine_state.json`, `AGENTS.md`, `variant-b.html`, `vault-access.html`, and both zip downloads at `/downloads/` and `/funnel/downloads/`.
- Root vs `funnel/` duplicates will drift if only one copy is edited. The deploy script overwrites the root pages from `funnel/` on the next `master` push.

Also live, status only, not fully audited in the browser: `variant-b.html` and `vault-access.html` (root and `funnel/`) returned HTTP 200.

#### Secrets and PHI

Scanned the working tree, all six zip archives, and all 24 commits. Patterns covered Stripe secret keys (`sk_live_` / `sk_test_`), restricted keys (`rk_`), publishable keys (`pk_`), webhook secrets (`whsec_`), private key blocks, AWS access keys, GitHub tokens, Slack tokens, and Google API keys.

**No Stripe secret key, restricted key, publishable key, or other API key was found.** No value is copied here.

A Google Apps Script lead-webhook URL is committed and is world-readable (client JavaScript, and `engine_state.json`, which Pages serves). The value is omitted. Rotate that deployment if the URL was not meant to be public.

Locations:

- `engine_state.json`
- `index.html`
- `funnel/index.html`
- `variant-b.html`
- `funnel/variant-b.html`
- `downloads/ARGON_Full_Boilerplate_Bundle_v1.zip` (member `index.html`)
- `funnel/downloads/ARGON_Full_Boilerplate_Bundle_v1.zip` (member `index.html`)

Commits that introduced or carried it:

- `dc3d5ab399406e6e12a111d6d37f9d9cfbd26725` — `engine_state.json`, `funnel/index.html`, `funnel/variant-b.html`
- `0996d4ce0316ae783fc358191515f66c9eaffb5c` — `index.html`, `variant-b.html`
- `6c06ee88c0dd8e95ef02562af3895a6e91a9336d` — `index.html`, `variant-b.html`

`vault_product/ARGON_Full_Boilerplate_Bundle_v1.zip` and the Turnkey Vault zips did not contain that host.

PHI: no SSN, medical-record, patient, or date-of-birth patterns in the text files. The word "diagnosis" appears in funnel-diagnostic copy (`controller/evaluate_funnel.py`, ad and email drafts, `market_intel.json`). That is not patient data. Nothing was copied. No PHI location to flag.

#### Untested, and why

- Payment submit, card entry, and the Stripe success URL back to `vault-access.html`. Stopped at checkout load on purpose.
- Whether the Apps Script webhook accepts the lead POST. The request was intercepted locally.
- The browser validation bubble on an empty email.
- `window.open` when a popup blocker is on.
- Full mobile and desktop pass of `variant-b.html` and `vault-access.html` beyond HTTP status, the missing `#vault-offer` target, and the 403 upsell link.
- Live-mode Payment Links. Only the current test-mode links exist in the repo.

---

## Section 3: Gemini -> Grok Bot (Next Night-Shift Tasks)

**Who writes this:** Gemini. Queue the next audit or the next check after Cursor Composer ships a change. Grok Bot reads this section at the start of the night shift and writes results back to Section 2.

### Entry template

```
### YYYY-MM-DD — Gemini
- Goal:
- Pages or files to check:
- Done when:
- Do not:
```

No entry yet.
