# Screen recording outline

Talking outline for about 15 minutes. Read the bullets. Do not add prices, results, or promises that are not on the live site.

The public site is a free waitlist: https://karllange.github.io/argon-autonomous-engine/

The training and toolkit are being rebuilt. This recording shows the phone-to-GitHub workflow that exists today. It does not show a finished course.

## 0:00–1:30 — Hook

- Say you run a small-business workflow from your phone.
- You send a plain instruction to an AI assistant.
- That assistant hands the work to cloud coding agents.
- Those agents work on `grok/*` branches in the GitHub repo `argon-autonomous-engine`. They open a pull request. They do not push straight to `master`.
- Show the live waitlist page. Read the line on the page: the beginner-friendly AI and tech training and toolkit is being rebuilt, and joining the waitlist is free.
- Say the rest of the video is that path, once, on screen. No income claim.

## 1:30–3:30 — What you need

- A phone you can message the assistant from.
- A GitHub account, and this repo.
- The three roles already written in `AGENTS.md`:
  - Gemini keeps the blueprint, the architecture, the funnel strategy, and the task queue. Gemini writes sections 1 and 3 of `AI_HANDOFF.md`.
  - Cursor Composer builds on a local branch from that blueprint. Cursor writes what it built into section 1.
  - Grok Bot checks the repo and the live pages, works only on `grok/*` branches, and opens pull requests. Grok writes section 2.
- GitHub Pages. It is what hosts the waitlist after a merge to `master`. Say "check current pricing" for GitHub and for any AI account. Do not name a dollar amount.
- A Mac for this recording. The workflow itself is the phone plus GitHub, not a special Mac app in this repo.

## 3:30–6:00 — How the pieces fit

- Open `AI_HANDOFF.md`. Call it the clipboard.
- Say every agent reads it at the start of a session and updates it at the end, with the date, the agent, and what changed.
- Point at the three sections:
  - Section 1 is for Gemini and Cursor Composer (blueprint and what got built).
  - Section 2 is for Grok Bot (checks and notes).
  - Section 3 is for Gemini to leave the next tasks for Grok Bot.
- Open `AGENTS.md` at Hybrid Auto-Merge.
- Say a docs-only change (`marketing/`, `kit-draft/`, `AI_HANDOFF.md`, `AGENTS.md`, or a README) can be squash-merged after the `gemini-3.5-flash` review passes and any fixes from that review are applied.
- Say a change to a live HTML page, live CSS or JS, or `config.js` stays open until you tap approve. If one pull request mixes those with docs, the whole request waits.
- Say agents still never push directly to `main` or `master`.
- Mention `kit-draft/evaluate_funnel.py` only as a local draft. It reads a sample `engine_state.json` in that same folder and prints advice. It does not log into an ad account, pause an ad, or spend money. It is not on the public site. `robots.txt` disallows `/kit-draft/` if the whole branch were ever published. The Pages workflow does not copy that folder.

## 6:00–11:00 — Live demo

Do one small docs note, not a redesign of the live page. A live-page edit would have to wait for your tap, which is a true sentence to say on camera, but it makes a long silent wait.

- 6:00 — On the phone, send one instruction. Example you can read aloud: "Add a dated note to section 2 of AI_HANDOFF.md that says the waitlist page was checked, and open a pull request. Do not change the HTML."
- 6:45 — On the computer, open the repo on GitHub. Show a new `grok/*` branch. Say the agent is not committing on `master`.
- 7:30 — Open the pull request. Show the diff is the handoff note, not the live page.
- 8:15 — Open `AI_HANDOFF.md` on that branch. Show the new dated entry: date, agent, what changed.
- 9:00 — Say the Gemini review (`gemini-3.5-flash`) runs before a docs merge. If it asks for a fix, that fix is applied first. If it has not finished, say so and do not pretend it passed.
- 9:45 — If this pull request only touches a docs file and the review has passed, squash-merge it and delete the branch. If the review has not passed, stop and say it is waiting. Do not merge a live HTML change in this demo.
- 10:15 — After a real merge to `master`, show GitHub Actions: "Sync Funnel to GitHub Pages" runs on that push, then the Pages build. The workflow copies the homepage, `config.js`, and `robots.txt` onto `gh-pages`. It does not publish `kit-draft/`.
- 10:40 — Reload https://karllange.github.io/argon-autonomous-engine/ and show the same waitlist. Say the page updates only after that deploy finishes. If you did not merge, say the live page is unchanged and that is expected.

## 11:00–13:00 — Safety rules

- Never push straight to `main` or `master`. Work stays on a `grok/*` branch until a pull request merges.
- Secrets stay out of the repo, the commits, the logs, and `AI_HANDOFF.md`. Stripe secret keys and restricted keys stay in an environment variable or a secret store. Only publishable keys and public Payment Links are allowed in client code, and this waitlist page does not use them.
- If a secret shows up, say you would note the file path and rotate it. Do not read the value on camera.
- No protected health information and no patient-identifiable data in the repo, issues, pull requests, screenshots, or handoff notes. Use placeholders.
- You approve live HTML, CSS, JS, and `config.js`. One tap. Mixed pull requests wait too.
- The copy rules still apply: do not invent a refund or a guarantee, do not invent stats or testimonials, and do not add health claims.

## 13:00–14:15 — What it cannot do

- It does not run ads, pause ads, or change an ad budget. `evaluate_funnel.py` only prints advice from numbers in a local JSON file.
- It does not guarantee customers, sales, or income.
- It does not ship a finished training course. The site says the training and toolkit are being rebuilt.
- An agent can miss a file or write a weak note. That is why the handoff exists and why live pages wait for you.
- A merge does not update the public site by itself. The Pages workflow has to succeed.
- There is no `argon-runner` command in this repo.

## 14:15–15:00 — Close

- Restate the path in one sentence: phone instruction, `grok/*` branch, pull request, Gemini review, merge only when the rules allow, then Pages updates the waitlist.
- Invite people to the waitlist. Read the button label: "Join the Early Access Waitlist".
- Read the confirmation they see after a successful submit: "You're on the list! We'll notify you when the new training & toolkit launches".
- If the form fails, say the email stays on screen and the page asks them to try again. Do not promise the form always succeeds.
- Point at the footer line "Digital product and waitlist terms apply." Do not add a refund or a guarantee.
- Stop. Do not name a price.

## Recording tips

Have these open before you start, on the computer:

- The live waitlist in a browser.
- The GitHub repo, the pull-request list, and Actions.
- `AGENTS.md` scrolled to Hybrid Auto-Merge.
- `AI_HANDOFF.md` at section 2.
- Optional, if you mention the local tool: `kit-draft/README.md`. Do not demo an ad account.

Blur or cover before you record:

- API keys, tokens, and passwords.
- Email addresses, including the footer contact line if you do not want it in the video.
- Webhook URLs. Do not read one aloud.
- Any patient or health detail. There should be none. If you see one, stop the recording.

Do not show Stripe secret keys. The waitlist page does not use a Payment Link. Leave checkout out of this video.
