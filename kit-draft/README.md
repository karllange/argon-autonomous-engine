# Kit draft

This folder is a local draft of the controller notes. It is not linked from the website. `.github/workflows/deploy-funnel.yml` does not copy it to GitHub Pages.

The site root `robots.txt` that the workflow does publish says `Disallow: /kit-draft/`. That line only matters if a later setup serves the whole branch. Today, Pages receives the waitlist page, `config.js`, and `robots.txt` — not this folder.

Do not put customer data in these files. The JSON values are samples.

## What `evaluate_funnel.py` does

It reads `engine_state.json` in this folder, compares the numbers with the four rules in `03_Self_Healing_Controller_Spec.md`, writes the suggested flag back into that same JSON file, and prints a report.

## What it does not do

It does not log into an ad account. It does not pause an ad, change a budget, or send email. A "kill" or "scale" line in the report is advice for a person to read.

## Setup

```bash
cd kit-draft
python3 evaluate_funnel.py
```

The state file must sit next to the script. If it is missing, the script prints where it looked and exits. It does not create a file and it does not guess a path two folders up.

## Cron

Standard cron cannot express "every 90 minutes" with `*/90` in the minute field. That field only runs from 0 to 59, so `*/90` is not a 90-minute pulse.

The spec and this script use a 30-minute check. Replace the path with the absolute path on your machine:

```cron
*/30 * * * * cd /absolute/path/to/kit-draft && /usr/bin/python3 evaluate_funnel.py >> controller.log 2>&1
```

There is no `argon-runner` binary. Do not schedule one.
