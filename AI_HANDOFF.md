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

### 2026-10-31 — Gemini API Compliance Approved (gemini-3.5-flash)

Scope: `marketing/screen-recording-outline.md` (PR #12). Verdict pass, 0 compliance issues. Skipped 2 conversion suggestions as Karl's decisions: (1) trim Git/branch detail for a non-technical audience, (2) add a launch window and early-access perk/discount. Merged under Hybrid Auto-Merge (`marketing/` + `AI_HANDOFF.md` only).

### 2026-10-31 — Honest cleanup

Branch `grok/honest-cleanup`. The public pages are a free waitlist. No Stripe redirect.

Removed:

- `variant-b.html` and `funnel/variant-b.html` (the $2,491 line, the scout demo, and the named quotes).
- `vault-access.html` and `funnel/vault-access.html`.
- `downloads/` and `funnel/downloads/` (both zip copies).
- `vault_product/ARGON_Turnkey_Agent_Vault_v1.zip` and `vault_product/ARGON_Full_Boilerplate_Bundle_v1.zip`.
- The Pages workflow no longer copies those files. The next deploy replaces `gh-pages`, so those URLs drop after merge. This branch does not push `gh-pages` itself.

Changed:

- `index.html` and `funnel/index.html` are the same waitlist page. The button is "Join the Early Access Waitlist". The modal asks for an email and posts to `config.js` `leadWebhookUrl` only. The confirmation is "You're on the list! We'll notify you when the new training & toolkit launches". A failed submit keeps the email and asks for a retry. Sandbox Payment Links stay in `config.js` and the page does not use them.
- Footer: "Questions? Contact karl@redoxhealthrevolution.com" from `SUPPORT_EMAIL`, plus "Digital product and waitlist terms apply." No refund or guarantee text was added.
- `controller/evaluate_funnel.py` no longer points at variant B.
- Nurture notes that linked to `vault-access.html` or `#market-proof` now point at the waitlist section.
- `kit-draft/` holds a local controller draft: fixed path (state file beside the script), rules aligned with Module 03, a 30-minute cron line instead of `*/90`, a clear exit when the state file is missing, a sample `engine_state.json`, a README, and corrected copies of the three modules. Sample quotes and figures are labeled sample. `argon-runner` is not a command. The "Compouding" typo is corrected. The reserve example no longer counts the same profit twice. The kit is not linked from the site and is not copied to Pages. `robots.txt` disallows `/kit-draft/` in case a later setup serves the whole branch.
- The three original module files are still in `vault_product/`. They are not the corrected draft.

Deleting these files does not remove them from git history, and it does not remove a copy someone already downloaded. The repo should be made private, and the old Apps Script webhook should be rotated. The URL is not written here.

Gemini API Compliance Approved (gemini-3.5-flash), 2026-10-30. Waitlist copy reviewed: 0 compliance issues. Two conversion suggestions were skipped because they would invent details Karl hasn't decided: (1) naming a target audience plus 3 toolkit bullets, and (2) a launch date plus a 20% waitlist discount. Left for Karl. No copy changes were made.

### 2026-10-30 — Brutally Honest Product Audit (pre-Stripe-live)

Checked on current `master` (`758aa2d`). I unzipped every copy of the two product zips and counted lines with the same method as `wc -l`. Live zip URLs were checked with a header request only. No card was entered. No refund policy is written here. That decision is Karl's, and so is any support email.

The line counts in the brief match the zips GitHub Pages actually serves (`downloads/` and `funnel/downloads/`, byte-for-byte the same). They do not match `vault_product/ARGON_Full_Boilerplate_Bundle_v1.zip`. That third bundle is called out at the bottom of the inventory.

Word count of the three Vault essays is 3,372 (1,247 + 1,198 + 927). That is the "about 3,400 words" figure, and it is about 12 pages if you print at roughly 280 words a page. There is no PDF and no video in any zip.

#### 1. Inventory

**$97 file:** `ARGON_Turnkey_Agent_Vault_v1.zip`, 12,317 bytes. Same bytes in `downloads/`, `funnel/downloads/`, and `vault_product/`. Three files. No PDFs. No videos.

| File | Path inside the zip | Size | Lines | Verdict |
| --- | --- | --- | --- | --- |
| `01_Grok_Bot_Scout_Playbook.md` | zip root | 9,668 bytes | 181 | Thin. A cron recipe for a program that does not exist, plus ad headlines written as if a campaign already happened. |
| `02_Antigravity_Cursor_Funnel_Factory.md` | zip root | 8,701 bytes | 112 | Thin notes for building a page. Not a step-by-step that ends in a live site. |
| `03_Self_Healing_Controller_Spec.md` | zip root | 7,738 bytes | 149 | Thin, and the worked example does not add up. The rules do not match the only script we ship. |

**$297 file that Pages serves:** `ARGON_Full_Boilerplate_Bundle_v1.zip`, 25,238 bytes, in `downloads/` and `funnel/downloads/`. Eight files. The three essays above are repeated. The other five:

| File | Path inside the zip | Size | Lines | Verdict |
| --- | --- | --- | --- | --- |
| `index.html` | zip root | 19,700 bytes | 677 | This is the sales page itself, the same 677-line homepage as `funnel/index.html`. A buyer is getting the storefront, not a lesson. |
| `config.js` | zip root | 2,450 bytes | 74 | Sandbox Payment Links, with the live slots blank. Same file as the repo root. Not a product. It also means a paid zip contains the test checkout URLs. |
| `evaluate_funnel.py` | zip root | 7,780 bytes | 165 | The only runnable tool in the bundle. It crashes out of the box. It only reads and writes a JSON file and prints a verdict. It never talks to an ad account. |
| `AGENTS.md` | zip root | 3,483 bytes | 35 | Old internal agent notes. Current `AGENTS.md` on `master` is 57 lines. This copy is stale. |
| `argon-architecture.mdc` | zip root | 2,244 bytes | 30 | Internal editor rule. Same 30 lines as `.cursor/rules/argon-architecture.mdc`. Not a customer lesson. |

**Customer page, not inside the zip:** `vault-access.html` (and the identical `funnel/vault-access.html`) is 453 lines. It is the post-purchase page. Verdict below: it shows setup notes a buyer should not need, and the lock is fake.

**Not the same bundle:** `vault_product/ARGON_Full_Boilerplate_Bundle_v1.zip` is 29,599 bytes and is not what Pages serves. Its `index.html` is 40,884 bytes and 745 lines, not 677. Its `evaluate_funnel.py` is 7,329 bytes and 159 lines, not 165. The other six names match the Pages bundle, including `config.js` at 74 lines. Do not describe that zip as the $297 deliverable.

#### 2. Useful or thin

I could not find `argon-runner` anywhere in the repo. No script, no binary. Module 01 still tells the buyer to install cron lines that call `/usr/local/bin/argon-runner`. The third line is commented "Every 90 minutes" and written as `*/90` in the minute field. A minute field only runs from 0 to 59, so that is not "every 90 minutes." As written it can only land on minute 0.

The essays present made-up results as if they happened. Module 01 includes a finished headline, "How a $50 Kill-Switch Saved Our $1,000 Testing Pool (And Found a 2.8x ROAS Winner by Tranche 3)." Module 03 walks through Ad Set A, Ad Set B, $194 revenue, then $491, and a 4.91x ROAS. `engine_state.json` telemetry on `master` is still all zeros. Those numbers are not a measured result from this project.

Module 03's reserve math does not hold. The story spends the first $100, then takes another $100 out of the $900 reserve and also adds a $195.50 "reinvestment" into the next ad budget. It then puts that same $195.50 back into the reserve and says original principal at risk is now $0. The $195.50 cannot both be spent on ads and locked in the reserve. The $100 already spent is gone. Principal at risk is not zero.

The thresholds also disagree with `evaluate_funnel.py`:

- The spec kills at $50 with 0 sales and sets one action name. The script sets `KILL_OR_PIVOT`.
- The spec waits for 1,500 impressions and a CTR under 1.0%. The script flags CTR under 1.2% with no impression minimum.
- The spec wants CTR of at least 1.5% and 100 clicks before it calls the page the problem. The script flags any opt-in rate under 15% as soon as there is one click.
- The spec scales only when spend is at least $50 and ROAS is at least 2.0, and it names the action `SCALE_WINNING_TRANCHE`. The script scales whenever spend is above zero and ROAS is at least 2.0, and it names the action `SCALE_TRANCHE`.
- The spec tells the buyer to save a file at `/controller/roas_governor.py`. That file is not in the zip. The file they did get is `evaluate_funnel.py` sitting at the top of the zip.

I ran that script from a fresh unzip. It crashed with `FileNotFoundError` for `engine_state.json` one folder above the unzip directory (`parent.parent` of the script). The JSON file is not in the zip, and the path assumes a `controller/` folder the zip does not have. Nothing in the script calls an ad platform. It is advice printed in a terminal.

"Affiliate bridges" are a phrase, not a file. They show up in `config.js` ("the working funnel, controller, and affiliate bridges"), on the homepage bump, and on `vault-access.html`. Neither zip contains an affiliate template, a link map, or a module by that name.

The 15-minute checklist on `vault-access.html` sends the buyer to files the zips do not contain:

- Step 2 says open `engine_state.json`. It is not in either zip.
- Step 3 says run a scout pass into `scout/market_intel.json`. That file is not in either zip. The playbook markdown is only in the $97 zip.
- Step 5 says run `python controller/evaluate_funnel.py`. The $97 zip has no Python file. The $297 zip has `evaluate_funnel.py` at the top level, not under `controller/`, and it crashes as tested above.

The same page shows internal setup in the buyer's view: the $1,000 / $100 / $900 / $50 guardrails, instructions to point Stripe success URLs at `?tier=core` or `?tier=bundle`, and a banner that tells you to set those URLs yourself if no tier was attached. That is operator notes, sitting on the fulfillment page.

`variant-b.html` is live. A header request to `https://karllange.github.io/argon-autonomous-engine/variant-b.html` returned 200. The file is 826 lines. On that page I can see a struck-through "$2,491" value, a scout demo that invents "Est. CTR: 2.4%+", "1.9%+", and "2.1%+", the line "Why 91% of … lose money on paid traffic," and a "CONFIDENCE SCORE: 9.4/10." None of those figures exist as measured telemetry. The page also names @Anaya_sharma876, u/marketing_guy_37, and @0xPaulvibe and presents their posts as proof. I am not repeating the posts.

#### 3. Access leaks

The GitHub repo `karllange/argon-autonomous-engine` is public.

The zips return HTTP 200, with no login, at:

- `https://karllange.github.io/argon-autonomous-engine/downloads/ARGON_Turnkey_Agent_Vault_v1.zip`
- `https://karllange.github.io/argon-autonomous-engine/downloads/ARGON_Full_Boilerplate_Bundle_v1.zip`
- `https://karllange.github.io/argon-autonomous-engine/funnel/downloads/ARGON_Turnkey_Agent_Vault_v1.zip`
- `https://karllange.github.io/argon-autonomous-engine/funnel/downloads/ARGON_Full_Boilerplate_Bundle_v1.zip`

`.github/workflows/deploy-funnel.yml` copies `funnel/downloads/` onto both of those Pages paths on every deploy. Paying is not required.

`vault-access.html` decides the tier by reading `?tier=` in the browser. `?tier=bundle` shows the bundle download. `?tier=core` shows the core download. There is no server check and no Stripe session check. I did not need a receipt. The lock is the query string.

The old Apps Script webhook is still in git history. It is not in the current working tree. It still has to be rotated. The URL is not written here. Commits that introduced or carried it include `dc3d5ab`, `0996d4c`, and `6c06ee8`.

#### 4. Recommendation

Pivot. The honest product is practical, beginner-friendly AI and tech training, not an autonomous ad buyer. The $97 should be a real step-by-step guide: a PDF plus a 20–40 minute walkthrough video, screenshots, a starter template, fill-in prompts, and a troubleshooting section. The lesson should take someone from an empty folder to a live page with Stripe, GitHub Pages, and an AI coding agent. Fix the broken pieces above before that lesson claims the controller or the scout runner works.

Until that ships, sell the current files as $19–29 early access, as-is, with an honest scope statement, or do not sell them.

Cut the $297 bump. Or re-price today's kit at $27–47 and call it "the source files behind this site," and only after it is a clean, unbranded, documented template. Right now the bundle is the sales page, a crashing script, sandbox config, and internal notes.

Before any live Payment Link:

- Make the repo private.
- Remove the zips from GitHub Pages and from the deploy workflow.
- Deliver files with an expiring signed link (Gumroad, Lemon Squeezy, or a Stripe session check).
- Rotate the Apps Script webhook.
- Take down `variant-b.html`, or rewrite it so the value, the CTR lines, the 91% line, the confidence score, and the named posts are gone.

The refund policy and the support email are Karl's decision. This audit does not write either one.

`config.js` is still sandbox. Do not turn on live checkout against this product as it sits.

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
