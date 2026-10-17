#!/usr/bin/env python3
"""
Project ARGON (ARGON-01) — Self-Healing Funnel & ROAS Controller
Zero-dependency Python 3 diagnostic script that reads `engine_state.json`,
evaluates live funnel telemetry against circuit-breaker thresholds, updates
`self_healing_flags`, and prints a deterministic diagnostic report.

Circuit Breaker Rules:
1. Spend >= $50 with 0 sales       -> action_required = "KILL_OR_PIVOT"
2. CTR < 1.2% (when impressions>0) -> action_required = "REWRITE_HOOKS"
3. Opt-in rate < 15% (when clicks>0)-> action_required = "OPTIMIZE_HERO_UI"
4. ROAS >= 2.0 (when spend>0)      -> action_required = "SCALE_TRANCHE"
"""

import json
from pathlib import Path
from typing import Any, Dict, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT_DIR / "engine_state.json"


def load_state(path: Path = STATE_FILE) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state: Dict[str, Any], path: Path = STATE_FILE) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
        f.write("\n")


def evaluate_telemetry(state: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    pool = state.get("capital_pool", {})
    telemetry = state.get("telemetry", {})
    flags = state.get("self_healing_flags", {})

    spend_usd = float(telemetry.get("spend_usd", 0.0))
    revenue_usd = float(telemetry.get("revenue_usd", 0.0))
    impressions = int(telemetry.get("impressions", 0))
    clicks = int(telemetry.get("clicks", 0))
    opt_ins = int(telemetry.get("opt_ins", 0))
    sales = int(telemetry.get("sales", 0))

    max_spend_no_sale = float(pool.get("max_spend_without_sale_usd", 50.0))
    scale_roas_trigger = float(pool.get("scale_roas_trigger", 2.0))

    ctr_pct = (clicks / impressions * 100.0) if impressions > 0 else 0.0
    opt_in_rate_pct = (opt_ins / clicks * 100.0) if clicks > 0 else 0.0
    roas = (revenue_usd / spend_usd) if spend_usd > 0 else 0.0

    diagnosis = "AWAITING_INITIAL_TRAFFIC_TELEMETRY"
    triggered_rule = "NONE (BASELINE_READY_STATE)"

    # Preserve pre-traffic ready state when spend and impressions are both 0
    if spend_usd == 0 and impressions == 0 and clicks == 0 and sales == 0:
        flags["current_status"] = "FUNNEL_AND_CONTROLLER_READY"
        flags["action_required"] = "DISPATCH_GROK_SCOUT_AND_ADS"
        diagnosis = (
            "Zero traffic recorded yet. Funnel UI and Self-Healing Controller are armed. "
            "Ready to dispatch Grok Scout and launch Tranche #1 ads."
        )
    # 1. Hard $50 Spend with 0 Sales Circuit Breaker
    elif spend_usd >= max_spend_no_sale and sales == 0:
        triggered_rule = "CIRCUIT_BREAKER_1: SPEND_50_ZERO_SALES"
        flags["current_status"] = "CIRCUIT_BREAKER_TRIPPED"
        flags["action_required"] = "KILL_OR_PIVOT"
        diagnosis = (
            f"CRITICAL: Spend reached ${spend_usd:.2f} (limit ${max_spend_no_sale:.2f}) "
            "with 0 sales. Kill active ad sets immediately or pivot offer angle."
        )
    # 2. ROAS >= 2.0x Winner Scaling Trigger
    elif spend_usd > 0 and roas >= scale_roas_trigger:
        triggered_rule = "SNOWBALL_TRIGGER_4: ROAS_2X_ACHIEVED"
        flags["current_status"] = "PROFITABLE_TRANCHE_VALIDATED"
        flags["action_required"] = "SCALE_TRANCHE"
        diagnosis = (
            f"WINNER DETECTED: ROAS is {roas:.2f}x (target >= {scale_roas_trigger:.2f}x). "
            "Unlock next $100 capital tranche and compound 50% of net profit."
        )
    # 3. CTR < 1.2% Hook Fatigue / Scroll-Stop Failure
    elif impressions > 0 and ctr_pct < 1.2:
        triggered_rule = "DIAGNOSTIC_2: LOW_CTR_BELOW_1.2_PCT"
        flags["current_status"] = "HOOK_UNDERPERFORMING"
        flags["action_required"] = "REWRITE_HOOKS"
        diagnosis = (
            f"HOOK BOTTLENECK: CTR is {ctr_pct:.2f}% (< 1.20% threshold across {impressions} impressions). "
            "Regenerate ad hooks from /scout/market_intel.json."
        )
    # 4. Opt-in < 15% Hero / Funnel UI Friction
    elif clicks > 0 and opt_in_rate_pct < 15.0:
        triggered_rule = "DIAGNOSTIC_3: LOW_OPT_IN_BELOW_15_PCT"
        flags["current_status"] = "FUNNEL_CONVERSION_LEAK"
        flags["action_required"] = "OPTIMIZE_HERO_UI"
        diagnosis = (
            f"FUNNEL LEAK: Opt-in rate is {opt_in_rate_pct:.2f}% (< 15.00% threshold across {clicks} clicks). "
            "Optimize Hero headline and 60-Second Hook Generator UI."
        )
    else:
        triggered_rule = "HEALTHY_MONITORING"
        flags["current_status"] = "TRANCHE_ACTIVE_HEALTHY"
        flags["action_required"] = "CONTINUE_MONITORING"
        diagnosis = "Telemetry within healthy operating bounds. Continue tranche execution."

    flags["last_agent_run"] = "CONTROLLER_EVALUATE_FUNNEL"
    state["self_healing_flags"] = flags

    metrics_summary = {
        "active_tranche": telemetry.get("active_tranche", 1),
        "spend_usd": spend_usd,
        "revenue_usd": revenue_usd,
        "roas": round(roas, 2),
        "impressions": impressions,
        "clicks": clicks,
        "ctr_pct": round(ctr_pct, 2),
        "opt_ins": opt_ins,
        "opt_in_rate_pct": round(opt_in_rate_pct, 2),
        "sales": sales,
        "triggered_rule": triggered_rule,
        "diagnosis": diagnosis,
        "current_status": flags["current_status"],
        "action_required": flags["action_required"],
    }
    return state, metrics_summary


def print_diagnostic_report(state: Dict[str, Any], summary: Dict[str, Any]) -> None:
    pool = state.get("capital_pool", {})
    offer = state.get("offer", {})
    print("=" * 74)
    print(f"PROJECT {state.get('project', 'ARGON-01')} // SELF-HEALING CONTROLLER DIAGNOSTIC REPORT")
    print("=" * 74)
    print(f"Offer               : {offer.get('name')} (${offer.get('core_price_usd')} Core / ${offer.get('upsell_price_usd')} Bump)")
    print(f"Capital Pool        : ${pool.get('starting_budget_usd')} Total | ${pool.get('allocated_tranche_usd')} Active Tranche | ${pool.get('remaining_reserve_usd')} Reserve")
    print(f"Guardrails          : ${pool.get('max_spend_without_sale_usd')} Max No-Sale Kill-Switch | {pool.get('scale_roas_trigger')}x ROAS Scale Trigger")
    print("-" * 74)
    print(f"Active Tranche      : #{summary['active_tranche']}")
    print(f"Spend / Revenue     : ${summary['spend_usd']:.2f} Spend  /  ${summary['revenue_usd']:.2f} Revenue  (ROAS: {summary['roas']:.2f}x)")
    print(f"Traffic & CTR       : {summary['impressions']} Impressions  ->  {summary['clicks']} Clicks  (CTR: {summary['ctr_pct']:.2f}%)")
    print(f"Funnel Opt-Ins      : {summary['opt_ins']} Opt-Ins  (Opt-In Rate: {summary['opt_in_rate_pct']:.2f}%)")
    print(f"Closed Sales        : {summary['sales']} Sales")
    print("-" * 74)
    print(f"Triggered Rule      : {summary['triggered_rule']}")
    print(f"Current Status      : {summary['current_status']}")
    print(f"Action Required     : {summary['action_required']}")
    print(f"Diagnostic Summary  : {summary['diagnosis']}")
    print("=" * 74)


def main() -> None:
    state = load_state()
    updated_state, summary = evaluate_telemetry(state)
    save_state(updated_state)
    print_diagnostic_report(updated_state, summary)


if __name__ == "__main__":
    main()
