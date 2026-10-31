# 01: The ARGON Grok-Bot Scout Playbook
## Autonomous Market Intelligence & Buyer Pain-Point Extraction Engine

**Module ID:** `ARGON-VAULT-01`  
**Target Output:** `/scout/market_intel.json`  
**Execution Cadence:** Every 6 Hours (`0 */6 * * *`)

---

## 1. Architecture Overview

The **Scout Node** is the sensory cortex of the Autonomous Revenue & Growth Operations Network (ARGON). Instead of guessing what hooks, angles, or offers will convert, the Scout Node deploys a persistent, headless or profile-authenticated browser agent to continuously harvest **verified buyer frustration** and **proven competitor ad spend** across three high-intent surfaces:

1. **Reddit High-Intent Subreddits** (Raw, unfiltered problem language & failed workarounds)
2. **X (Twitter) Search & Grok Synthesis** (Real-time sentiment velocity, viral complaints, and influencer blind spots)
3. **Meta Ad Library & TikTok Creative Center** (Active ads running > 14 days—proving positive unit economics)

All findings are normalized into a strict, deterministic schema (`/scout/market_intel.json`) consumed directly by the **Funnel Factory** (`Module 02`).

---

## 2. Cron Schedule & Daemon Configuration

Configure your persistent agent runner, system crontab, or AI scheduling daemon with the following schedule definitions:

```cron
# ==============================================================================
# ARGON SCOUT NODE CRON SCHEDULE
# ==============================================================================

# 1. Primary Deep Scrape & Market Intel Synthesis (Every 6 hours)
0 */6 * * * /usr/local/bin/argon-runner --module scout --mode full-harvest --output /scout/market_intel.json >> /var/log/argon_scout.log 2>&1

# 2. Competitor Ad Library Longevity Check (Daily at 02:00 UTC)
0 2 * * * /usr/local/bin/argon-runner --module scout --mode ad-longevity-audit --min-days-active 14 >> /var/log/argon_ad_audit.log 2>&1

# 3. Emergency Trend Spike Detector (Every 90 minutes during peak hours)
*/90 12-23 * * * /usr/local/bin/argon-runner --module scout --mode velocity-pulse --threshold 3.5x >> /var/log/argon_pulse.log 2>&1
```

---

## 3. Copy-Paste Autonomous Browser Agent Prompts

### Prompt 3.1: Master Multi-Surface Scout Prompt (Grok / Browser Agent)

Copy and paste this exact system instruction into your autonomous browser agent or Grok automation workflow:

```markdown
<SYSTEM_INSTRUCTION>
You are ARGON-SCOUT-01, an elite Quantitative Market Intelligence & Direct-Response Research Agent.
Your objective is to execute a multi-surface reconnaissance sweep across Reddit, X (Twitter), and the Meta Ad Library to extract high-converting buyer pain points, exact vernacular phrases, and validated competitor hooks.

### STEP 1: SURFACE 1 — REDDIT PAIN HARVEST
Navigate to or query the target niche subreddits (e.g., r/entrepreneur, r/SaaS, r/marketing, r/agency, r/Automate).
Execute search queries using these high-intent buyer frustration operators:
- `"how do I automate" OR "sick of manually"`
- `"wasted money on" OR "stopped working"`
- `"is there a tool that" OR "why is it so hard to"`
- `"spending hours every day" OR "margins are getting crushed"`

Extract the top 15 threads from the past 30 days sorted by upvote velocity and comment-to-upvote ratio (>0.4).
Record:
1. Exact verbatim quotes expressing acute financial or time pain.
2. Specific tools or solutions the market currently hates (and why).
3. The exact outcome they wish they could buy for under $100.

### STEP 2: SURFACE 2 — X (TWITTER) & GROK REAL-TIME PULSE
Execute advanced search queries on X:
- `("ai agent" OR "automation" OR "ad spend" OR "funnel") ("broken" OR "scam" OR "finally figured out" OR "printing") min_faves:25 -filter:links`
- `("ROAS" OR "CAC" OR "landing page") ("dying" OR "crushed" OR "playbook") min_faves:50`

Identify:
1. Emerging contrarian beliefs (what worked 6 months ago that no longer works today).
2. High-engagement "mechanism reveals" (threads where users beg for the workflow/repo in the replies).
3. Emotional trigger words used by frustrated operators.

### STEP 3: SURFACE 3 — META AD LIBRARY LONGEVITY AUDIT
Navigate to `https://www.facebook.com/ads/library/`.
Filter by:
- Location: United States, United Kingdom, Canada, Australia
- Ad Category: All Ads
- Active Status: Active Ads Only
- Keywords: `"autonomous agent"`, `"AI workflow"`, `"client acquisition"`, `"turnkey system"`, `"ROAS"`

Sort and filter strictly for ads that have been running continuously for **14+ days** (or have 3+ active variations using the same primary text). Longevity = profitability.
Deconstruct the top 5 longest-running ads into:
1. First-3-Second Visual / Text Hook
2. Primary Agitation Angle
3. Unique Mechanism Name
4. Offer Structure & Risk Reversal
5. CTA Framing

### STEP 4: DETERMINISTIC OUTPUT GENERATION
Compile all extracted intelligence into the exact JSON schema defined below and save it to `/scout/market_intel.json`. Do not include markdown prose outside the file write operation.
</SYSTEM_INSTRUCTION>
```

---

## 4. Target Output Specification (`/scout/market_intel.json`)

Your Scout Agent must write `/scout/market_intel.json` conforming strictly to this production schema so downstream Funnel and Creative agents can parse it without hallucination:

```json
{
  "schema_version": "1.0.0",
  "generated_at_utc": "2026-10-16T21:45:00Z",
  "project": "ARGON-01",
  "niche_category": "Autonomous AI Marketing & Revenue Systems",
  "market_sophistication_stage": 4,
  "buyer_persona": {
    "title": "Solo Technical Founder / Media Buyer / Micro-Agency Operator",
    "annual_revenue_range": "$50,000 - $500,000",
    "core_desire": "Predictable, hands-off customer acquisition without hiring media buyers or babysitting brittle Zapier chains",
    "acute_fears": [
      "Burning $1,000+ on Meta/TikTok ads with zero conversions",
      "Buying another $997 'prompt pack' course that requires 40 hours of manual setup",
      "Missing the autonomous agent wave while competitors automate their entire growth stack"
    ]
  },
  "verbatim_pain_points": [
    {
      "id": "PAIN-01",
      "source": "Reddit / r/SaaS",
      "intensity_score": 9.4,
      "verbatim_quote": "I don't need another wrapper or 10,000 ChatGPT prompts. I need an agent that actually watches my ad spend, kills the losers before I wake up broke, and ships new landing page angles automatically.",
      "underlying_objection": "Skepticism of passive templates vs. executable autonomous systems"
    },
    {
      "id": "PAIN-02",
      "source": "X / Operator Thread",
      "intensity_score": 9.1,
      "verbatim_quote": "Media buyers charge $3k/mo retainers just to check Ads Manager twice a week and let losing ad sets bleed past $200 before turning them off.",
      "underlying_objection": "High agency fees and slow human reaction times"
    },
    {
      "id": "PAIN-03",
      "source": "Reddit / r/entrepreneur",
      "intensity_score": 8.8,
      "verbatim_quote": "My landing page converts at 0.8% because I'm guessing what copy to write instead of pulling what buyers are actually complaining about right now.",
      "underlying_objection": "Disconnect between market research and funnel copy"
    }
  ],
  "validated_competitor_hooks": [
    {
      "hook_id": "HOOK-01",
      "days_active_in_ad_library": 38,
      "angle_type": "Mechanism vs. Old Way",
      "headline": "Stop Buying Prompt Packs. Deploy a Self-Healing Revenue Engine.",
      "primary_hook_copy": "99% of 'AI agencies' are still manually copying text between browser tabs. Here is the exact 3-node architecture that scrapes live buyer pain, builds the funnel in Cursor, and governs its own ad spend with hard $50 circuit breakers.",
      "visual_directive": "Dark-mode IDE terminal split-screen showing live `engine_state.json` telemetry alongside an automated ROAS kill-switch flowchart."
    },
    {
      "hook_id": "HOOK-02",
      "days_active_in_ad_library": 24,
      "angle_type": "Hard Math / Risk Reversal",
      "headline": "How a $50 Kill-Switch Saved Our $1,000 Testing Pool (And Found a 2.8x ROAS Winner by Tranche 3)",
      "primary_hook_copy": "Most founders lose money on ads because emotions get involved. An autonomous controller doesn't hope an ad set recovers—it cuts losers at $50 with 0 sales and compounds 2.0x ROAS winners automatically.",
      "visual_directive": "High-contrast financial tranche ledger showing Tranche 1 ($100) vs Reserve ($900) with green/red automated rules."
    }
  ],
  "winning_offer_positioning": {
    "unique_mechanism_name": "Closed-Loop Autonomous Tranche Architecture (Scout -> Funnel Factory -> Self-Healing Controller)",
    "value_anchor_comparison": "Replaces a $3,500/mo Media Buyer + $2,000 Funnel Copywriter",
    "price_framing": "$97 One-Time Vault Access (Less than 2 failed ad sets)",
    "order_bump_upsell_bridge": "Upgrade to the $297 Full Autonomous Orchestrator CLI & Live Webhook Pack"
  }
}
```

---

## 5. Verification & Quality Gate Checklist

Before the Scout Agent flips `self_healing_flags.current_status` in `engine_state.json`, it runs a 4-point validation check:

1. **Verbatim Authenticity Check:** Are there at least 3 verbatim quotes containing emotional/financial friction words (`wasted`, `bleeding`, `manual`, `broken`, `hours`)?
2. **Ad Longevity Proof:** Does every competitor hook in `validated_competitor_hooks` have `days_active_in_ad_library >= 14`?
3. **JSON Validity:** Does `jq . /scout/market_intel.json` exit with status code `0`?
4. **State Handoff:** Update `engine_state.json` -> `last_agent_run: "SCOUT_HARVEST_COMPLETE"` and trigger the Funnel Factory.
