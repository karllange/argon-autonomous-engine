# 03: The Self-Healing Controller Specification
## Automated ROAS, CTR & Funnel Diagnostic Rulebook ($50 Kill-Switch & 2.0x ROAS Snowball Engine)

**Module ID:** `ARGON-VAULT-03`  
**State Source of Truth:** `/engine_state.json`  
**Controller Directory:** `/controller`

---

## 1. Core Philosophy: Emotionless Capital Governance

Human media buyers lose money because of **sunk-cost fallacy** ("let's give this ad set another \$50 to optimize") and **slow reaction loops** (checking dashboards once a day).

The **ARGON Self-Healing Controller** treats ad spend as strict algorithmic tranche allocation governed by `/engine_state.json`:
- **Total Starting Capital Pool:** `\$1,000` (`starting_budget_usd: 1000`)
- **Active Testing Tranche:** `\$100` (`allocated_tranche_usd: 100`)
- **Protected Vault Reserve:** `\$900` (`remaining_reserve_usd: 900`)
- **Hard Circuit Breaker (Kill-Switch):** `\$50` maximum spend without a sale (`max_spend_without_sale_usd: 50`)
- **Snowball Scale Trigger:** `2.0x ROAS` (`scale_roas_trigger: 2.0`)

---

## 2. The Diagnostic Decision Matrix (CTR, CVR & ROAS Rules)

Every 30 minutes, the Controller evaluates `engine_state.json -> telemetry` against four deterministic diagnostic gates:

| Rule ID | Condition Trigger | Root Cause Diagnosis | Automated Self-Healing Action | State Flag Update (`action_required`) |
| :--- | :--- | :--- | :--- | :--- |
| **`RULE-01`**<br>*Hard Kill-Switch* | `spend_usd >= 50` **AND** `sales == 0` | Offer-to-traffic mismatch or broken conversion path; capital bleed detected. | **PAUSE ACTIVE AD SET IMMEDIATELY.** Lock remaining tranche capital. Trigger root-cause diagnostic (check CTR vs Opt-in CVR). | `"KILL_SWITCH_TRIGGERED_REBUILD_HOOK"` |
| **`RULE-02`**<br>*Creative Fatigue / Weak Hook* | `impressions >= 1500` **AND** `CTR < 1.0%` (`clicks / impressions < 0.01`) | Ad hook is failing to stop the scroll in the feed. Landing page is not yet the bottleneck. | Pause bottom 80% of creatives by CTR. Instruct **Funnel Factory** (`Module 02`) to generate 5 new hooks from `market_intel.json`. | `"ROTATE_AD_CREATIVES"` |
| **`RULE-03`**<br>*Funnel Leak / Offer Friction* | `CTR >= 1.5%` **AND** `clicks >= 100` **AND** `opt_ins / clicks < 15%` (or `sales == 0` at `\$50` spend) | Ad hook works (high curiosity/intent), but `/funnel` headline, mechanism explanation, or checkout friction is failing. | Keep winning ad hooks alive in draft; instruct **Funnel Factory** to rewrite `/funnel` Hero Headline & Risk Reversal block. | `"PATCH_FUNNEL_HEADLINE_AND_OFFER"` |
| **`RULE-04`**<br>*2.0x ROAS Snowball Scale* | `spend_usd >= 50` **AND** `ROAS >= 2.0` (`revenue_usd / spend_usd >= 2.0`) | Validated profitable unit economics! Offer + Hook + Funnel are in resonance. | **SNOWBALL PROTOCOL:** Unlock next `\$100` tranche from `remaining_reserve_usd`, plus reinvest `50%` of net profit into winning ad IDs. Clone winning hook into 3 visual variations. | `"SCALE_WINNING_TRANCHE"` |

---

## 3. The 2.0x ROAS Snowball Compouding Formula

When `roas = revenue_usd / spend_usd >= 2.0`, the Controller executes the **Tranche Snowball Algorithm** toward `target_revenue_cycle_1_usd: 2000`:

$$
\text{Next Tranche Budget} = \text{Base Tranche (\$100)} + 0.50 \times (\text{Revenue}_{\text{current}} - \text{Spend}_{\text{current}})
$$

### Example Cycle Walkthrough:
1. **Tranche 1 (`\$100` allocated, `\$900` reserve):**
   - Ad Set A spends `\$50` with `0` sales -> **KILLED by `RULE-01`** at exact `\$50.00` mark (`\$0` wasted beyond threshold).
   - Ad Set B spends `\$50` and generates **2 Core Sales (`2 x \$97 = \$194`)**.
   - Tranche 1 Total: `spend_usd = 100`, `revenue_usd = 194` (`ROAS = 1.94x`). Near threshold—Ad Set B continues with remaining optimization window, lands 1 Upsell (`\$297`), bringing `revenue_usd = 491` (`ROAS = 4.91x`).
2. **Snowball Trigger (`ROAS = 4.91x >= 2.0x`):**
   - Net Profit = `\$491 - \$100 = \$391`.
   - Reinvestment Bonus = `0.50 * \$391 = \$195.50`.
   - **Tranche 2 Active Allocation:** `\$100 (from reserve) + \$195.50 (profit) = \$295.50` deployed strictly into Ad Set B variations.
   - Protected Vault Reserve remains `\$800 + \$195.50 (locked profit) = \$995.50`—meaning **total capital at risk is now \$0 of original principal**.

---

## 4. Reference Python / Node Controller Logic (`/controller/roas_governor.py`)

Buyers can drop this reference evaluator into `/controller/roas_governor.py` and run it on a 15-minute cron job:

```python
#!/usr/bin/env python3
"""
ARGON-01 Self-Healing ROAS & Telemetry Controller
Reads /engine_state.json, evaluates kill-switch & snowball rules, and updates state flags.
"""
import json
from pathlib import Path

STATE_PATH = Path(__file__).resolve().parent.parent / "engine_state.json"


def evaluate_engine_state() -> dict:
    with STATE_PATH.open("r", encoding="utf-8") as f:
        state = json.load(f)

    pool = state["capital_pool"]
    telemetry = state["telemetry"]
    flags = state["self_healing_flags"]

    spend = float(telemetry["spend_usd"])
    revenue = float(telemetry["revenue_usd"])
    impressions = int(telemetry["impressions"])
    clicks = int(telemetry["clicks"])
    sales = int(telemetry["sales"])

    max_no_sale_spend = float(pool["max_spend_without_sale_usd"])
    scale_roas_trigger = float(pool["scale_roas_trigger"])

    ctr = (clicks / impressions) if impressions > 0 else 0.0
    roas = (revenue / spend) if spend > 0 else 0.0

    # RULE-01: Hard $50 Kill-Switch
    if spend >= max_no_sale_spend and sales == 0:
        flags["current_status"] = "AD_SET_KILLED_CIRCUIT_BREAKER"
        flags["action_required"] = (
            "PATCH_FUNNEL_HEADLINE_AND_OFFER" if ctr >= 0.015 else "ROTATE_AD_CREATIVES"
        )
    # RULE-04: 2.0x ROAS Snowball Trigger
    elif spend >= max_no_sale_spend and roas >= scale_roas_trigger:
        net_profit = max(0.0, revenue - spend)
        reinvest_bonus = round(net_profit * 0.50, 2)
        base_tranche = 100.0 if pool["remaining_reserve_usd"] >= 100 else pool["remaining_reserve_usd"]

        pool["remaining_reserve_usd"] = round(pool["remaining_reserve_usd"] - base_tranche, 2)
        pool["allocated_tranche_usd"] = round(base_tranche + reinvest_bonus, 2)
        telemetry["active_tranche"] += 1

        flags["current_status"] = f"SCALING_ROAS_{roas:.2f}X"
        flags["action_required"] = "SCALE_WINNING_TRANCHE"
    # RULE-02: Early CTR Fatigue Warning
    elif impressions >= 1500 and ctr < 0.01:
        flags["current_status"] = "LOW_CTR_WARNING"
        flags["action_required"] = "ROTATE_AD_CREATIVES"

    flags["last_agent_run"] = "CONTROLLER_ROAS_GOVERNOR"

    with STATE_PATH.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    return state


if __name__ == "__main__":
    updated = evaluate_engine_state()
    print(json.dumps(updated["self_healing_flags"], indent=2))
```

---

## 5. Closed-Loop Recovery Sequence

```
[Ad Traffic Live]
       │
       ▼
[Controller Polls Telemetry Every 15m]
       │
       ├──► Spend >= $50 & Sales == 0 ──► [KILL AD SET]
       │                                        │
       │                          ┌─────────────┴─────────────┐
       │                          ▼                           ▼
       │                    CTR < 1.5%?                 CTR >= 1.5%?
       │                          │                           │
       │                          ▼                           ▼
       │               [Regenerate 10 Ad Hooks]    [Rewrite Funnel Headline]
       │
       └──► Spend >= $50 & ROAS >= 2.0x ──► [SNOWBALL: Unlock $100 Tranche + 50% Profit]
```
