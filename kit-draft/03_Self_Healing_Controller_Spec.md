# 03: Controller spec (draft)

**Module ID:** `ARGON-VAULT-03`  
**Script:** `evaluate_funnel.py` in this folder, next to `engine_state.json`  
**Typo fixed:** the old heading said "Compouding." The word is "Compounding."

The script is advisory. It prints a suggestion. It does not pause an ad or move a budget.

## 1. Sample guardrails

These numbers are **samples**, matching the sample `engine_state.json`. They are not a live account.

- Sample starting pool: $1,000
- Sample active tranche: $100
- Sample reserve: $900
- Sample kill gate: $50 spent with 0 sales
- Sample scale gate: spend at least $50 and ROAS at least 2.0

ROAS means revenue divided by spend. If spend is 0, ROAS is 0. Do not divide by zero.

## 2. Rules

The script uses these gates, in this order. The first match wins.

| Rule | When it fires | Flag written locally | What a person does |
| --- | --- | --- | --- |
| Empty | Spend, impressions, clicks, and sales are all 0 | `ADD_SAMPLE_OR_REAL_NUMBERS` | Enter numbers. Nothing is wrong yet. |
| RULE-01 | Spend is at least $50 and sales are 0 | `KILL_SWITCH_TRIGGERED_REBUILD_HOOK` | Decide whether to pause the ads. The script will not do it. |
| RULE-04 | Spend is at least $50 and ROAS is at least 2.0 | `SCALE_WINNING_TRANCHE` | Decide whether to raise budget. The script will not do it. |
| RULE-02 | At least 1,500 impressions and CTR under 1.0% | `ROTATE_AD_CREATIVES` | Review the ads. |
| RULE-03 | CTR at least 1.5%, at least 100 clicks, and opt-in rate under 15% | `PATCH_FUNNEL_HEADLINE_AND_OFFER` | Review the page. |

CTR under 1.0% means clicks divided by impressions is under 0.01. The older script used 1.2% with no impression minimum. That disagreed with this table. This draft and `evaluate_funnel.py` use the table.

RULE-01 is checked before RULE-04. A $50 spend with 0 sales is a kill suggestion, not a scale suggestion, because ROAS is 0.

## 3. Compounding formula

This is arithmetic for a **sample**, not a result this project measured.

Next ad budget = $100 from the sample reserve + half of (revenue − spend), and only after RULE-04 has fired.

Half of the profit is the reinvestment sample. The other half stays unspent. Do not add that same half back into the reserve and also call it spent.

### Sample walkthrough

Label: **sample**. Not a campaign that ran.

1. Sample reserve starts at $900. Sample tranche of $100 is already set aside, so the reserve is not $1,000.
2. Sample ad set A spends $50 and records 0 sales. RULE-01 applies to that set. The $50 is spent. It is not recovered.
3. Sample ad set B spends the other $50 and records 2 sample sales at $97 each. 2 × $97 = $194. Tranche spend is $100. Revenue is $194. ROAS is 194 / 100 = 1.94. That is under 2.0, so RULE-04 does not fire.
4. A later sample row adds one $297 sale and no extra spend. Revenue is 194 + 297 = $491. Spend is still $100. ROAS is 491 / 100 = 4.91. Spend is at least $50 and ROAS is at least 2.0, so RULE-04 can fire as advice.
5. Sample profit is 491 − 100 = $391. Half is $195.50. The other half, $195.50, stays unspent.
6. The next sample tranche takes $100 from the $900 reserve. Reserve left is $800. Next ad budget is 100 + 195.50 = $295.50.
7. Original money still at risk includes the $100 already spent and the new $100 taken from reserve. It is not $0. The $195.50 kept back is not also sitting in the reserve as if it were never allocated to ads.

The old write-up said the reserve became $800 + $195.50 = $995.50 and that principal at risk was $0. That counted $195.50 twice and ignored the $100 already spent.

## 4. How to run it

State file path: the same folder as the script. Not `parent.parent`, and not `/controller/roas_governor.py`. That path was wrong for a zip that dropped the script in the top folder and left out `engine_state.json`.

```bash
cd kit-draft
python3 evaluate_funnel.py
```

If `engine_state.json` is missing, the script prints that path and exits. It does not invent a state file.

## 5. Cron

Check every 30 minutes. This replaces both the "every 15 minutes" sketch and the invalid `*/90` line.

```cron
*/30 * * * * cd /absolute/path/to/kit-draft && /usr/bin/python3 evaluate_funnel.py >> controller.log 2>&1
```

The job only prints advice and updates the local JSON flags.
