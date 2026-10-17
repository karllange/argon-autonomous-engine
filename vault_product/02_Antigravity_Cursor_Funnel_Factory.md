# 02: The Antigravity & Cursor Funnel Factory
## Autonomous Conversion Engineering: From `market_intel.json` to High-Converting Funnel UI + 10 Ad Creatives

**Module ID:** `ARGON-VAULT-02`  
**Input Dependency:** `/scout/market_intel.json` & `/engine_state.json`  
**Target Outputs:** `/funnel/index.html` (or Next.js route) + `/creatives/ad_matrix_10x.json` & `/creatives/*.md`

---

## 1. Architecture Overview

The **Funnel Factory** eliminates the bottleneck between market insight and live traffic. The moment `/scout/market_intel.json` is updated, the IDE Agent (Antigravity or Cursor) reads the extracted buyer pain points, maps them into a proven direct-response conversion architecture, and compiles:

1. **A High-Converting Direct-Response Landing Page (`/funnel`)** engineered for sub-second load speed, terminal/architect aesthetic credibility, instant value anchoring, and a frictionless \$97 core checkout + \$297 upsell path.
2. **A 10-Variant Ad Creative Matrix (`/creatives`)** spanning 5 distinct psychological angles (2 variants per angle) mapped directly to the verbatim pain quotes harvested by the Scout Node.

---

## 2. Drop-In `.cursor/rules/funnel-factory.mdc` (and Antigravity Rule Spec)

Copy the block below directly into `.cursor/rules/funnel-factory.mdc` (or include it in your root `AGENTS.md`) to turn your IDE into an autonomous Funnel & Creative compiler:

```markdown
---
description: Autonomous Funnel Factory & 10x Ad Creative Generator triggered when market_intel.json is updated or BUILD_FUNNEL_UI is active.
globs: ["funnel/**/*", "creatives/**/*", "scout/market_intel.json", "engine_state.json"]
alwaysApply: true
---

# ARGON FUNNEL FACTORY EXECUTION PROTOCOL

Whenever `engine_state.json` shows `action_required == "BUILD_FUNNEL_UI"` or `BUILD_CREATIVES`, execute the following deterministic pipeline:

## PHASE 1: CONTEXT INGESTION
1. Read `/engine_state.json` to extract exact pricing (`core_price_usd`: 97, `upsell_price_usd`: 297) and offer metadata (`The ARGON Turnkey Agent Vault`).
2. Read `/scout/market_intel.json` to extract:
   - `verbatim_pain_points` (for headline hooks and problem agitation)
   - `validated_competitor_hooks` (for structural framing)
   - `winning_offer_positioning.unique_mechanism_name`

## PHASE 2: HIGH-CONVERTING LANDING PAGE SYNTHESIS (`/funnel`)
Build a single-page, ultra-fast, conversion-obsessed landing page using the **7-Block Direct-Response Terminal Architecture**:

1. **Above-The-Fold Callout Bar:** Target audience filter + live system status badge (`ARGON-01 // AUTONOMOUS REVENUE ARCHITECTURE`).
2. **Hero Section (Hook + Mechanism + CTA):**
   - Headline derived from the highest `intensity_score` pain point in `market_intel.json`.
   - Subheadline explaining the **3-Node Closed-Loop System** (Scout -> Funnel Factory -> Self-Healing Controller) without requiring a $3,500/mo media buyer.
   - Primary CTA Button with price anchor (`Deploy The ARGON Vault — $97 Instant Access`).
3. **The "Old Way vs. ARGON Protocol" Comparison Grid:**
   - Contrast brittle prompt packs, emotional ad spend bleeding, and slow copywriting against deterministic JSON handoffs and hard $50 circuit breakers.
4. **Inside The $97 Turnkey Vault (3-Module Breakdown):**
   - Module 01: The Grok-Bot Scout Playbook (`market_intel.json` harvester)
   - Module 02: The Antigravity & Cursor Funnel Factory (Automated UI & 10x Ad Generator)
   - Module 03: The Self-Healing ROAS Controller ($50 Kill-Switch & 2.0x Snowball Engine)
5. **Interactive Capital Protection Proof (Telemetry Preview):**
   - Visual breakdown of the $1,000 Capital Pool split into $100 active tranches and $900 protected reserve.
6. **The $297 One-Click Order Bump / Upsell Preview:**
   - Position the $297 Autonomous Webhook & Live API Execution Pack as the natural accelerator.
7. **Risk-Reversal & FAQ Block:**
   - Address every `underlying_objection` listed in `market_intel.json`.

## PHASE 3: THE 10-CREATIVE AD MATRIX (`/creatives`)
Generate 10 complete, production-ready ad creatives structured across 5 conversion angles:
- **Creatives 01 & 02 (The "Verbatim Pain Mirror" Angle):** Opens with the exact Reddit/X quote from `market_intel.json`.
- **Creatives 03 & 04 (The "$50 Kill-Switch Math" Angle):** Focuses on capital preservation and eliminating emotional ad spend bleed.
- **Creatives 05 & 06 (The "Prompt Pack Autopsy" Contrarian Angle):** Calls out why 99% of AI courses fail and introduces stateful JSON agent orchestration.
- **Creatives 07 & 08 (The "IDE Live Build" Mechanism Reveal):** Walks through how Cursor/Antigravity reads `market_intel.json` and ships a funnel in 90 seconds.
- **Creatives 09 & 10 (The "Direct ROI / Agency Replacement" Angle):** Anchors $97 one-time against a $3,500/month retainer.

Each creative MUST contain:
1. `ad_id` (`ARGON-AD-01` through `ARGON-AD-10`)
2. `angle_category`
3. `scroll_stopper_visual_spec` (exact instructions for static image / terminal screenshot / 15s video B-roll)
4. `hook_first_line` (< 90 characters, mobile truncation safe)
5. `primary_text` (PAS or Mechanism-First framework)
6. `headline` (5–8 words max)
7. `description_strip` (social proof / instant delivery badge)
8. `utm_parameters` (`?utm_source=meta&utm_medium=paid&utm_campaign=tranche_{{active_tranche}}&utm_content={{ad_id}}`)

## PHASE 4: STATE COMMIT
Update `/engine_state.json`:
- Set `self_healing_flags.last_agent_run` to `"FUNNEL_FACTORY_BUILD"`
- Advance `self_healing_flags.current_status` and `action_required` to the next lifecycle stage.
```

---

## 3. Ready-to-Deploy 10-Creative Ad Matrix Template

Below is the master 10-ad creative specification that your Funnel Factory generates and updates each cycle:

| Ad ID | Angle | Hook (First Line) | Headline | Visual Spec |
| :--- | :--- | :--- | :--- | :--- |
| `ARGON-AD-01` | Verbatim Pain Mirror | *"I don't need 10,000 prompts. I need an agent that kills losing ads before I wake up broke."* | The \$97 Autonomous Agent Vault | Split-screen Reddit dark-mode comment + `engine_state.json` live terminal |
| `ARGON-AD-02` | Verbatim Pain Mirror | Still paying a media buyer \$3k/mo to check Ads Manager twice a week? | Replace Retainers With State JSON | Red/Green comparison chart: Human Agency vs. ARGON Tranche Controller |
| `ARGON-AD-03` | \$50 Kill-Switch Math | Never let a losing ad set bleed past \$50 again. Here is the exact JSON state controller. | Hard \$50 Circuit Breaker Spec | Flowchart showing \$1,000 pool -> \$100 Tranche -> \$50 Kill-Switch vs 2.0x Scale |
| `ARGON-AD-04` | \$50 Kill-Switch Math | How we protect \$900 in reserve while testing 10 hooks in a \$100 micro-tranche. | Tranche-Based Ad Capital Governance | Clean dark UI card highlighting `remaining_reserve_usd: 900` |
| `ARGON-AD-05` | Contrarian Autopsy | Prompt packs are dead. If your AI agents don't share a state file, you have a hobby, not a business. | Stateful Agents > Prompt Packs | Code diff showing unstructured chat vs deterministic `engine_state.json` |
| `ARGON-AD-06` | Contrarian Autopsy | Why 94% of landing pages flop: You're guessing the copy instead of scraping live buyer rage. | Scrape Pain -> Compile Funnel | Diagram of Grok Scout feeding `market_intel.json` into Cursor |
| `ARGON-AD-07` | IDE Mechanism Reveal | Watch Antigravity & Cursor turn `market_intel.json` into a live funnel and 10 ads in one run. | Autonomous Cursor Funnel Factory | IDE file tree showing `/scout`, `/funnel`, `/vault_product`, `/creatives`, `/controller` |
| `ARGON-AD-08` | IDE Mechanism Reveal | 3 Markdown specs + 1 JSON state engine = a self-healing digital product machine. | Clone The ARGON-01 Architecture | Terminal view of `.cursor/rules/argon-architecture.mdc` |
| `ARGON-AD-09` | Agency Replacement ROI | \$97 once vs. \$5,500/mo in copywriters and media buyers. You do the math. | Deploy ARGON-01 For \$97 Today | High-contrast receipt comparison graphic |
| `ARGON-AD-10` | Agency Replacement ROI | Everything inside the ARGON Turnkey Agent Vault: Scout Playbook, Funnel Rules & ROAS Controller. | Instant Access: The ARGON Vault | 3-module blueprint exploded view with instant download badge |

---

## 4. Conversion UI Engineering Checklist

Before deploying `/funnel/index.html` to production traffic, verify:
- [ ] **Zero External Bloat:** Page loads in `< 400ms` with high-contrast dark terminal typography (`Inter` / `JetBrains Mono`).
- [ ] **Dynamic Price Binding:** Checkout CTAs strictly reflect `engine_state.json` (`$97` core / `$297` upsell).
- [ ] **UTM Telemetry Capture:** Outbound checkout links preserve `utm_content=ARGON-AD-XX` so the Self-Healing Controller (`Module 03`) can attribute sales back to the exact creative.
