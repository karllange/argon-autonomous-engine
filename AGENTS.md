# Project ARGON (`ARGON-01`) — Autonomous Agent Governance Rules

> **STANDALONE BUSINESS UNIT DECLARATION:**  
> Project ARGON (`ARGON-01`) operates as an independent, standalone autonomous revenue business unit under `PERSONAL_ZERO_PHI` governance.
>
> **CRITICAL DIRECTIVE FOR ALL IDE & AUTONOMOUS AGENTS:**  
> You MUST read [`engine_state.json`](file:///c:/argon-autonomous-engine/engine_state.json) at the start of every run and update [`engine_state.json`](file:///c:/argon-autonomous-engine/engine_state.json) immediately upon completing any task.

---

## 1. Standalone Bot Topology & Loop Ownership Table

| Loop / Role | Assigned Autonomous Owner | Scope, Responsibility & Artifact Target |
| :--- | :--- | :--- |
| **Triage & Handoff Router** | **Main Grok Dispatcher Bot** | Sorts & routes incoming triggers and state transitions only (zero execution bloat). |
| **Loop 1 (Market Recon Owner)** | **`Researchy`** | Scrapes 14-day X/Reddit verbatim complaints & validated links $\to$ [`scout/market_intel.json`](file:///c:/argon-autonomous-engine/scout/market_intel.json). |
| **Loop 2 & 4 (Factory & Self-Healing Controller Owner)** | **Google Antigravity / Cursor** | Compiles & optimizes [`funnel/index.html`](file:///c:/argon-autonomous-engine/funnel/index.html) and executes [`controller/evaluate_funnel.py`](file:///c:/argon-autonomous-engine/controller/evaluate_funnel.py) circuit breakers. |
| **Loop 3 (Traffic & Distribution Owner)** | **`O Marketing`** | Deploys paid & organic distribution in strictly capped **\$100 tranches** using [`creatives/tranche_1_ads.md`](file:///c:/argon-autonomous-engine/creatives/tranche_1_ads.md). |

---

## 2. State Synchronization Protocol (`engine_state.json`)
- **Before starting work:** Read [`engine_state.json`](file:///c:/argon-autonomous-engine/engine_state.json) to verify `business_unit`, `agent_ownership`, `offer`, `capital_pool`, `telemetry`, and `self_healing_flags` (`current_status`, `action_required`, `last_agent_run`).
- **After completing work:** Update `self_healing_flags.current_status`, advance `self_healing_flags.action_required` to the next pipeline action, and record your agent identifier in `self_healing_flags.last_agent_run`.

---

## 3. System Directory Topology
- `/scout` — Autonomous pain-point and 14-day X/Reddit reconnaissance owned by `Researchy` ([`scout/market_intel.json`](file:///c:/argon-autonomous-engine/scout/market_intel.json)).
- `/funnel` — Direct-response landing page UI and conversion checkout flows (\$97 core / \$297 upsell) owned by Google Antigravity / Cursor ([`funnel/index.html`](file:///c:/argon-autonomous-engine/funnel/index.html)).
- `/vault_product` — The \$97 Turnkey Agent Vault customer deliverables + packaged archive ([`vault_product/ARGON_Turnkey_Agent_Vault_v1.zip`](file:///c:/argon-autonomous-engine/vault_product/ARGON_Turnkey_Agent_Vault_v1.zip)).
- `/creatives` — 10-variant ad creative matrices and viral organic posts executed by `O Marketing` ([`creatives/tranche_1_ads.md`](file:///c:/argon-autonomous-engine/creatives/tranche_1_ads.md)).
- `/controller` — Self-healing ROAS/CTR diagnostic scripts (\$50 kill-switch & 2.0x ROAS snowball scaler) owned by Google Antigravity / Cursor ([`controller/evaluate_funnel.py`](file:///c:/argon-autonomous-engine/controller/evaluate_funnel.py)).

See [`.cursor/rules/argon-architecture.mdc`](file:///c:/argon-autonomous-engine/.cursor/rules/argon-architecture.mdc) for full IDE rule metadata.
