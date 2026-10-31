# 01: Scout notes (draft)

**Module ID:** `ARGON-VAULT-01`  
**Status:** Draft. Not a running product.

There is no `argon-runner` program in this repo. A scout pass is something you do yourself in a browser, then save notes into a JSON file. Nothing here logs into an ad account.

## 1. What this note is

A checklist for collecting public posts and ad-library examples by hand. It does not prove that an ad is profitable. An ad that stays up is not, by itself, evidence of profit.

## 2. Schedule

Do not use this cron line. It is wrong:

```cron
*/90 12-23 * * * /usr/local/bin/argon-runner --module scout
```

`*/90` in the minute field is not "every 90 minutes." The minute field only accepts 0–59.

There is no scout command to schedule. If you later schedule the controller, use the 30-minute line in `README.md`. That command is `python3 evaluate_funnel.py` in this folder.

## 3. Manual pass

1. Pick one niche.
2. Read public posts. Copy only what you are allowed to store. Mark each quote `SAMPLE` until you have checked it.
3. Open the public ad library in a browser. Write down what you see. Do not treat days-on-screen as a ROAS figure.
4. Save the file yourself. There is no harvester binary.

### Sample prompt

The block below is a **sample prompt**, not a measured study. Numbers inside it are samples.

```markdown
SAMPLE PROMPT — not a live harvest.

Look at public posts in one niche from the last 30 days.
Record up to 15 threads you actually opened.
For each one, store the source URL, the date you read it, and a short quote.
Label the row "sample" if you have not verified it.
Do not invent a score, a ROAS, or a dollar loss.
```

## 4. Sample output shape

Every figure in this JSON is a **sample**. It is not telemetry from this project.

```json
{
  "_sample": true,
  "schema_version": "1.0.0-sample",
  "generated_at_utc": "SAMPLE-DATE",
  "niche_category": "SAMPLE niche",
  "verbatim_pain_points": [
    {
      "id": "SAMPLE-QUOTE-01",
      "label": "sample",
      "source": "SAMPLE source, not a checked post",
      "verbatim_quote": "SAMPLE quote. Replace this with a post you opened, or delete the row."
    }
  ],
  "validated_competitor_hooks": [
    {
      "hook_id": "SAMPLE-HOOK-01",
      "label": "sample",
      "days_active_in_ad_library": 0,
      "headline": "SAMPLE headline. Not a live ad result.",
      "note": "A day count is not a ROAS figure."
    }
  ]
}
```

## 5. Check before you keep a row

1. The quote is labeled `sample` until you have the source in front of you.
2. You did not invent a percentage, a dollar loss, or a ROAS.
3. The file is valid JSON.
4. You did not claim an ad account was changed.
