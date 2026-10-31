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

### 2026-10-30 — Gemini API Compliance Approved (gemini-3.5-flash)

Gemini verdicts: ads pass. Emails `needs_changes`, conversion only. No compliance issues.

Applied edits:

1. Post 1 now opens with "Want to build your own AI-driven revenue engine?" and states one-time email access.
2. Post 2 states the no-venture-capital premise directly.
3. Post 2 names The Blueprint, the $97 price, email access, and the real button label.
4. Post 3 now quotes the page sentence on power, leverage, and creative capacity. This fixes the misquote that said only "more leverage than the generation before you."
5. Ad 2 primary text names The Blueprint and the $97 one-time price.
6. Day 1 body thanks the reader and points the link at the offer.
7. Day 2 subject is "The AI wave is here".
8. Day 2 body uses the "precipice of a gigantic change" line and everyday builders.
9. Day 2 CTA is "Get the Blueprint — $97".
10. Day 3 subject is "No venture capital required".
11. Day 3 body uses the "for the first time in history" line from the page.
12. Day 4 subject is "Less than $300 a month in AI tools".
13. Day 4 preview is "The Blueprint is $97, one time."
14. Day 4 body quotes the tools-cost sentence and says that $300 is tool cost, not earnings.
15. Day 4 CTA is "Get the Blueprint — $97".
16. Day 5 body describes the $297 build kit as the working funnel, controller, and affiliate bridges, and says the unchecked total stays $97.00.

Rejected suggestions:

1. "Automate your revenue workflow without writing complex code". It invents capabilities.
2. Replacing Ad 3's "The AI wave is here" headline. That is the page H1, so the ad and the page should match.
3. "Speak to pain points". Partly accepted, with no invented problems.
4. "Transformational output". Partly accepted, with no outcome or income promise. "In days" was left out as a time-to-result claim.
5. "Get Instant Access". The page never says instant.
6. "Build Your AI Revenue Engine Now". It implies an outcome and drops the price.
7. Changing the Day 5 CTA "Choose $97 or $394 at checkout". Kept, because it avoids checkout surprise.

`config.js` is still sandbox. No ads or emails go out until live Payment Links are set and `mode` is `"live"`.

### 2026-10-31 — Grok Bot — marketing copy drafted, no PR

Branch `grok/argon-marketing-copy`. No pull request opened. Copy is waiting for the Gemini API compliance review before Karl is pinged.

- Added the Copy rules section to `AGENTS.md`.
- Drafted `marketing/b2b-ads-and-hooks.md` and `marketing/vault-upsell-emails.md` from `config.js` and the live homepage only. No new prices, stats, testimonials, refund terms, guarantees, or trials.
- `config.js` `mode` is still `"sandbox"`. Live Payment Links are still blank.

### 2026-10-31 — Grok Bot — funnel fixes on `grok/fix-funnel-and-marketing`

Local retest only. GitHub Pages still serves the previous deploy until this branch is merged. Playwright, headless Chrome, viewports 1440×900 and 390×844. Placeholder email `audit@example.com`. Pay was not clicked. No card data was entered.

What changed:

- `config.js` is the only place pages read Payment Links. `mode` is `"sandbox"`. `paymentLinks.live.core97`, `bundle394`, and `upsell297` are empty. Karl has to paste live-mode links and set `mode` to `"live"`. Sandbox links stay in `paymentLinks.sandbox` so the current test checkout still opens.
- Checkout appends `?prefilled_email=` when an email was entered. Observed on both `/` and `/funnel/index.html`: the opened Stripe URL contained `prefilled_email=audit%40example.com`, and the Stripe email field showed `audit@example.com`. Core checkout still showed The Blueprint at $97.00. With the build-kit box checked, the modal total was $394.00 and Stripe showed The Blueprint + Build Kit at $394.00. Both checkouts still show the Sandbox badge.
- First screen shows **$97** and **The Blueprint**, with the subhead "The practical guide to building your own AI-driven revenue engine." Header, hero, and `#vault-offer` buttons read **Get the Blueprint — $97**. Modal line is still The Blueprint at $97.00, button "Continue — $97.00".
- `#vault-offer` is a real section. Local `/#vault-offer` scrolled to about 993px and the heading "The Blueprint — $97" was in view. `/funnel/index.html#vault-offer` did the same (scroll about 1003px).
- The vault-access upgrade no longer uses the link that returned HTTP 403. With the live upsell link blank, the control has no `href`, `aria-disabled="true"`, and a note that Karl must paste `paymentLinks.live.upsell297`.
- Client pages no longer contain the Apps Script host. `leadWebhookUrl` in `config.js` and `engine_state.json` is empty. The same host was removed from the boilerplate zips. Recommend rotating that Apps Script deployment. The URL is not repeated here.
- GitHub Pages workflow now publishes only `config.js`, the three HTML pages, and the download zips, and deletes previously published internal files (including `engine_state.json`) from `gh-pages` on the next deploy. `/marketing` is not published.
- `/marketing` has a README, a QA log, and an experiment log. No stats were invented.

Local measurements:

| Page | Viewport | HTTP | Overflow | $97 in view | Hero CTA in view | CTA size |
| --- | --- | --- | --- | --- | --- | --- |
| `/` | 1440 | 200 | no | yes | yes (bottom 508 of 900) | 206×48 |
| `/` | 390 | 200 | no | yes | yes (bottom 447 of 844) | 206×48 |
| `/funnel/index.html` | 1440 | 200 | no | yes | yes | 206×48 |
| `/funnel/index.html` | 390 | 200 | no | yes | yes | 206×48 |

Header button was 182×44 on both widths. No horizontal overflow. Mobile checkout submit stayed in view (bottom 714 of 844). No page errors. The only console 404 was `/favicon.ico`, which this branch does not add.

"The $300/Month Empire" is still on the first screen, under the $97 price. Variant B still calls the product the Turnkey Agent Vault in its own headline. Checkout for that page now uses the same config and still charges The Blueprint at $97 in sandbox.

Untested: a real card, the Pay button, Stripe success URLs back to `vault-access.html`, and live-mode links (they are blank). Webhook delivery is untested because the URL was removed.

Screenshots (not committed): `local-root-desktop.png`, `local-root-mobile.png`, `local-funnel-desktop.png`, `local-funnel-mobile.png`, `local-root-vault-offer.png`, `local-funnel-vault-offer.png`, `local-root-modal-core.png`, `local-root-mobile-modal.png`, `local-stripe-core-nopay.png`, `local-vault-access-upgrade.png`.

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
