# Project ARGON (`ARGON-01`) — 5-Part Autonomous Nurture Sequence

**Audience:** Operators who unlocked the Free 60-Second Niche & Ad Generator (`custom_market_intel.json`) and have not bought.  
**Source event:** `handleBlueprintOptIn` POST `{ email, niche, timestamp, utm_source }` → `LEAD_WEBHOOK_URL`.  
**Live engine:** https://karllange.github.io/argon-autonomous-engine/  
**Core offer:** The ARGON Turnkey Agent Vault — **$97** one-time.  
**Upsell:** Self-Healing Funnel Boilerplate + Affiliate Stack — **$297**.  
**Bundle (max AOV):** Vault + Boilerplate — **$394**.  
**Sender voice:** Operator to operator. Short sentences. No fake countdown clocks.  
**Merge fields:** `{{email}}`, `{{niche}}` (fallback: "your niche"), `{{utm_source}}`.

Every CTA carries UTM tags so `controller/evaluate_funnel.py` can separate nurture clicks from paid tranche traffic.

---

## Email 1 — Day 0 (send immediately after opt-in)

**Subject:** Your 60-second ARGON blueprint is unlocked  
**Preview:** The JSON is yours. Here is what to do with it in the next 10 minutes.

**Body:**

{{email}},

You just ran the Free 60-Second Niche & Ad Generator for **{{niche}}**. The blueprint download is the same file the Scout node writes in production: three pain-point hooks and a 3-step funnel map.

Use it today, in this order:

1. Open `custom_market_intel.json` and steal the hook you would actually run as an ad.
2. Replay the live generator if the niche was too broad: https://karllange.github.io/argon-autonomous-engine/#hook-generator
3. If the hooks are sharper than what you are running, the rest of the system is the **$97 ARGON Turnkey Agent Vault** — the Scout playbook, the Funnel Factory rules, and the ROAS controller spec.

The generator is the front door. The Vault is the repo those hooks come from.

**CTA:** Unlock the $97 Turnkey Agent Vault  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d0&utm_content=vault_97#vault-offer

You will get the files from the fulfillment portal the moment Stripe confirms payment.

—

Project ARGON (`ARGON-01`)  
https://karllange.github.io/argon-autonomous-engine/

---

## Email 2 — Day 1

**Subject:** The $400 you lose babysitting Ads Manager  
**Preview:** Prompt packs do not watch the account at 2 AM. You do.

**Body:**

Most operators who ran the generator yesterday are still the bottleneck this morning.

The pattern we keep harvesting from founders in **{{niche}}**:

> "I can ship a full-stack feature in a weekend, but the moment I open Ads Manager I burn $400 on dead clicks."

A prompt pack cannot see spend. A 25-step Zap cannot kill an ad set. You close the laptop, and the losing campaign keeps spending because nobody coded a rule.

ARGON-01 is that rule, written down:

- **$1,000** Cycle 1 pool
- **$100** active tranche, **$900** locked in reserve
- **$50** hard stop if sales are still zero
- **2.0x ROAS** before another dollar comes out of reserve

The free generator showed you the hooks. The controller is what stops the bleed.

**CTA:** See the $97 Vault and the $50 kill-switch  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d1&utm_content=kill_switch#vault-offer

Re-run your niche first if you want fresh hooks:  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d1&utm_content=generator#hook-generator

---

## Email 3 — Day 2

**Subject:** What is actually inside the $97 Vault  
**Preview:** Three markdown specs. No video course. No retainer.

**Body:**

Here is the entire $97 ARGON Turnkey Agent Vault, with nothing padded in:

**Module 01 — Grok-Bot Scout Playbook**  
Browser prompts and a 6-hour cadence that scrape Reddit, X, and ads active 14+ days into `market_intel.json`. This is the engine behind the generator you already used.

**Module 02 — Antigravity & Cursor Funnel Factory**  
Drop-in `.cursor/rules` that ingest that JSON and compile a direct-response page plus a 10-ad matrix. The live page you opted in on was built this way:  
https://karllange.github.io/argon-autonomous-engine/

**Module 03 — Self-Healing ROAS Controller Spec**  
The decision tree: kill at $50 with 0 sales, rewrite hooks when CTR is under 1.2%, fix the hero when opt-in is under 15%, scale the tranche at 2.0x ROAS. Includes the zero-dependency Python evaluator.

Standalone prices people quote for pieces of this stack run $497, $997, and $997. The Vault is **$97 once**. No subscription.

If you only buy one file, buy this one and deploy Module 01 against **{{niche}}** tonight.

**CTA:** Get the $97 Turnkey Agent Vault  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d2&utm_content=modules#vault-offer

---

## Email 4 — Day 3

**Subject:** Your hook worked. Your page might still be leaking.  
**Preview:** CTR under 1.2% and opt-in under 15% are different failures.

**Body:**

Day 3 is where operators usually blame "the ads" and kill a campaign that was one diagnostic away from working.

The controller separates those failures on purpose:

| Signal | What it means | What ARGON does |
| :--- | :--- | :--- |
| CTR under 1.2% | The hook never stopped the scroll | `REWRITE_HOOKS` from `market_intel.json` |
| CTR is fine, opt-in under 15% | The hero is leaking | `OPTIMIZE_HERO_UI` — a contrarian variant is already built |
| $50 spent, 0 sales | The offer and the traffic do not match | `KILL_OR_PIVOT` |
| ROAS at or above 2.0x | The unit economics hold | `SCALE_TRANCHE` |

You felt the first half of that loop when the generator wrote hooks for **{{niche}}**. The missing half is a page and a script that act on the numbers without a standup meeting.

Two ways to buy:

- **$97 — Turnkey Agent Vault.** The three specs and the state engine. You implement.
- **$394 — Full Bundle.** The Vault plus the production funnel boilerplate, the wired controller, and the affiliate stack. You deploy.

Both land on the same fulfillment portal after Stripe. Core buyers can still add the boilerplate later for **$297**.

**CTA:** Deploy the $97 Vault  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d3&utm_content=vault_97#vault-offer

**CTA:** Take the $394 Bundle (Vault + Boilerplate)  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d3&utm_content=bundle_394#vault-offer

---

## Email 5 — Day 4

**Subject:** $97 to install the engine, or $394 to skip the build  
**Preview:** Last note in this sequence. Pick a tier or stay on the free generator.

**Body:**

This is the close of the five-day sequence. After this, we will not keep tapping you about the same decision.

You already have the free tool:

https://karllange.github.io/argon-autonomous-engine/#hook-generator

It will keep generating hooks for **{{niche}}**. It will not install the Scout cron, the funnel rules, or the $50 kill-switch. That is the product.

**Choose one:**

1. **Stay on the free generator.** Rational if you are not spending on traffic yet.
2. **$97 Turnkey Agent Vault.** Best if you want the specs and you will wire Stripe and the controller yourself. Success redirect: `vault-access.html?tier=core`.
3. **$394 Full Bundle.** Best if you want the boilerplate and the affiliate stack in the same afternoon. That is the $97 Vault plus the $297 upgrade, paid once. Success redirect: `vault-access.html?tier=bundle`.

Core buyers who want the boilerplate later use the $297 upgrade card inside the portal. You do not pay $394 twice.

The capital rule does not change either way: $100 in the test, $900 in reserve, dead ad sets die at $50.

**CTA — $97 Vault:**  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d4&utm_content=vault_97#vault-offer

**CTA — $394 Bundle:**  
https://karllange.github.io/argon-autonomous-engine/?utm_source=nurture&utm_medium=email&utm_campaign=argon_d4&utm_content=bundle_394#vault-offer

If you buy, download from the portal and run the First 15 Minutes Quickstart before you touch Ads Manager.

—

Project ARGON (`ARGON-01`)  
Live engine: https://karllange.github.io/argon-autonomous-engine/  
Governance: `PERSONAL_ZERO_PHI`

---

## ESP wiring notes

| Day | Internal ID | Delay from opt-in | Primary goal |
| :--- | :--- | :--- | :--- |
| 0 | `ARGON-NURTURE-D0` | 0 minutes | Deliver the win, introduce the $97 Vault |
| 1 | `ARGON-NURTURE-D1` | 1 day | Agitate babysitting / dead ad spend |
| 2 | `ARGON-NURTURE-D2` | 2 days | Unpack the three Vault modules |
| 3 | `ARGON-NURTURE-D3` | 3 days | Teach the diagnostic tree, offer both prices |
| 4 | `ARGON-NURTURE-D4` | 4 days | Force the $97 vs $394 decision |

- Suppress the rest of the sequence on `sales >= 1` for that email.
- Core buyers who have not taken the $297 upgrade may receive Day 4's bundle block only; do not resend Day 0–3.
- Map `utm_source` from the webhook onto the contact so paid (`omarketing`) and nurture replies stay distinct in telemetry.
- Webhook field contract: `email`, `niche`, `timestamp` (ISO-8601), `utm_source` (empty string when the landing URL has no parameter).
