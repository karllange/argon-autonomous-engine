#!/usr/bin/env python3
"""
Advisory funnel check for the kit-draft folder.

Reads engine_state.json in this same folder, compares the SAMPLE or real
numbers you typed in against the rules in 03_Self_Healing_Controller_Spec.md,
updates the local flags, and prints a report.

It does not log into an ad account, pause an ad, or spend money.
If engine_state.json is missing, it exits with a short message.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, Tuple

ROOT_DIR = Path(__file__).resolve().parent
STATE_FILE = ROOT_DIR / "engine_state.json"

# Same gates as Module 03. CTR values are ratios (0.01 == 1%).
RULES = {
    "kill_spend_usd": 50.0,
    "scale_spend_usd": 50.0,
    "scale_roas": 2.0,
    "weak_hook_impressions": 1500,
    "weak_hook_ctr": 0.01,
    "funnel_leak_ctr": 0.015,
    "funnel_leak_clicks": 100,
    "funnel_leak_opt_in": 0.15,
}


def load_state(path: Path = STATE_FILE) -> Dict[str, Any]:
    if not path.is_file():
        print(f"No state file at {path}.")
        print("Add engine_state.json in this folder. Nothing was called on an ad account.")
        sys.exit(1)
    try:
        with path.open("r", encoding="utf-8") as handle:
            state = json.load(handle)
    except json.JSONDecodeError as err:
        print(f"engine_state.json is not valid JSON: {err}")
        print("Fix the file and run again. Nothing was called on an ad account.")
        sys.exit(1)
    if not isinstance(state, dict):
        print("engine_state.json must be a JSON object.")
        sys.exit(1)
    return state


def save_state(state: Dict[str, Any], path: Path = STATE_FILE) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)
        handle.write("\n")


def evaluate_telemetry(state: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    pool = state.get("capital_pool") if isinstance(state.get("capital_pool"), dict) else {}
    telemetry = state.get("telemetry") if isinstance(state.get("telemetry"), dict) else {}
    flags = state.get("self_healing_flags") if isinstance(state.get("self_healing_flags"), dict) else {}

    spend_usd = float(telemetry.get("spend_usd") or 0)
    revenue_usd = float(telemetry.get("revenue_usd") or 0)
    impressions = int(telemetry.get("impressions") or 0)
    clicks = int(telemetry.get("clicks") or 0)
    opt_ins = int(telemetry.get("opt_ins") or 0)
    sales = int(telemetry.get("sales") or 0)

    kill_spend = float(pool.get("max_spend_without_sale_usd") or RULES["kill_spend_usd"])
    scale_roas_trigger = float(pool.get("scale_roas_trigger") or RULES["scale_roas"])
    scale_spend = float(RULES["scale_spend_usd"])

    ctr = (clicks / impressions) if impressions > 0 else 0.0
    opt_in_rate = (opt_ins / clicks) if clicks > 0 else 0.0
    roas = (revenue_usd / spend_usd) if spend_usd > 0 else 0.0

    if spend_usd == 0 and impressions == 0 and clicks == 0 and sales == 0:
        triggered_rule = "NONE (SAMPLE OR EMPTY TELEMETRY)"
        flags["current_status"] = "NO_TELEMETRY_YET"
        flags["action_required"] = "ADD_SAMPLE_OR_REAL_NUMBERS"
        diagnosis = (
            "Spend, impressions, clicks, and sales are all 0. "
            "No rule fired. This script did not contact an ad account."
        )
    elif spend_usd >= kill_spend and sales == 0:
        triggered_rule = "RULE-01"
        flags["current_status"] = "ADVISORY_KILL_SWITCH"
        flags["action_required"] = "KILL_SWITCH_TRIGGERED_REBUILD_HOOK"
        diagnosis = (
            f"Advisory: spend is ${spend_usd:.2f} and sales are 0 "
            f"(gate is ${kill_spend:.2f}). Review the ads yourself. This script did not pause them."
        )
    elif spend_usd >= scale_spend and roas >= scale_roas_trigger:
        triggered_rule = "RULE-04"
        flags["current_status"] = "ADVISORY_SCALE"
        flags["action_required"] = "SCALE_WINNING_TRANCHE"
        diagnosis = (
            f"Advisory: spend is ${spend_usd:.2f} and ROAS is {roas:.2f}x "
            f"(gates are ${scale_spend:.2f} and {scale_roas_trigger:.2f}x). "
            "This script did not move a budget."
        )
    elif impressions >= RULES["weak_hook_impressions"] and ctr < RULES["weak_hook_ctr"]:
        triggered_rule = "RULE-02"
        flags["current_status"] = "ADVISORY_WEAK_HOOK"
        flags["action_required"] = "ROTATE_AD_CREATIVES"
        diagnosis = (
            f"Advisory: CTR is {ctr * 100:.2f}% across {impressions} impressions "
            "(gate is under 1.00% after at least 1,500 impressions)."
        )
    elif ctr >= RULES["funnel_leak_ctr"] and clicks >= RULES["funnel_leak_clicks"] and opt_in_rate < RULES["funnel_leak_opt_in"]:
        triggered_rule = "RULE-03"
        flags["current_status"] = "ADVISORY_FUNNEL_LEAK"
        flags["action_required"] = "PATCH_FUNNEL_HEADLINE_AND_OFFER"
        diagnosis = (
            f"Advisory: CTR is {ctr * 100:.2f}% with {clicks} clicks and "
            f"opt-in rate {opt_in_rate * 100:.2f}% "
            "(gates are CTR at least 1.50%, at least 100 clicks, opt-in under 15%)."
        )
    else:
        triggered_rule = "NONE (INSIDE THE GATES)"
        flags["current_status"] = "NO_RULE_FIRED"
        flags["action_required"] = "KEEP_WATCHING"
        diagnosis = "No rule fired. This script did not change an ad account."

    flags["last_agent_run"] = "KIT_DRAFT_EVALUATE_FUNNEL_ADVISORY"
    state["self_healing_flags"] = flags

    summary = {
        "active_tranche": telemetry.get("active_tranche", 1),
        "spend_usd": spend_usd,
        "revenue_usd": revenue_usd,
        "roas": round(roas, 2),
        "impressions": impressions,
        "clicks": clicks,
        "ctr_pct": round(ctr * 100.0, 2),
        "opt_ins": opt_ins,
        "opt_in_rate_pct": round(opt_in_rate * 100.0, 2),
        "sales": sales,
        "triggered_rule": triggered_rule,
        "diagnosis": diagnosis,
        "current_status": flags["current_status"],
        "action_required": flags["action_required"],
    }
    return state, summary


def print_diagnostic_report(summary: Dict[str, Any]) -> None:
    print("ARGON kit-draft — advisory report")
    print("This report does not pause ads or spend money.")
    print("-" * 60)
    print(f"Spend / revenue     : ${summary['spend_usd']:.2f} / ${summary['revenue_usd']:.2f}  (ROAS {summary['roas']:.2f}x)")
    print(f"Impressions / clicks: {summary['impressions']} / {summary['clicks']}  (CTR {summary['ctr_pct']:.2f}%)")
    print(f"Opt-ins / sales     : {summary['opt_ins']} opt-ins ({summary['opt_in_rate_pct']:.2f}%) / {summary['sales']} sales")
    print(f"Rule                : {summary['triggered_rule']}")
    print(f"Status              : {summary['current_status']}")
    print(f"Suggested next step : {summary['action_required']}")
    print(f"Note                : {summary['diagnosis']}")


def main() -> None:
    state = load_state()
    updated, summary = evaluate_telemetry(state)
    save_state(updated)
    print_diagnostic_report(summary)


if __name__ == "__main__":
    main()
