# 02: Page and ad notes (draft)

**Module ID:** `ARGON-VAULT-02`  
**Status:** Draft. The public site is a free waitlist, not a $97 checkout.

This note describes how a person can turn research notes into a page and into ad drafts. It does not ship a page by itself, and it does not buy traffic.

## 1. What you actually have

- Input you type: a JSON file of notes, and `engine_state.json` if you want the controller to read it.
- Output you build: HTML and ad copy you are willing to stand behind.
- The live ARGON page collects a waitlist email. It does not sell a vault.

Do not paste this note into a personal `AGENTS.md`. If you want an editor rule, put it in a project rule file and keep sample numbers labeled `sample`.

## 2. Sample prices

These are **sample** numbers from the old config, not a live offer:

- Sample core price: $97
- Sample add-on price: $297

The waitlist page does not show these prices. Do not put them back on the public page unless the product and the terms are real.

## 3. Page blocks worth keeping

1. One sentence that says what the training is, and that it is still being rebuilt.
2. One button: "Join the Early Access Waitlist".
3. An email field and the confirmation line already used on the site.
4. A support email and the line "Digital product and waitlist terms apply."
5. No invented conversion rate, no struck-through "value" price, and no quote presented as proof unless you have the source.

## 4. Sample ad rows

Each row is a **sample**. It is not a result.

| Id | Label | First line | Do not treat this as |
| --- | --- | --- | --- |
| SAMPLE-AD-01 | sample | SAMPLE first line about the waitlist. | A measured CTR |
| SAMPLE-AD-02 | sample | SAMPLE first line. No dollar promise. | A customer quote |
| SAMPLE-AD-03 | sample | SAMPLE first line. The controller only prints advice. | An ad account action |

## 5. Before you publish a page

- The button does not send anyone to Stripe.
- No file under `kit-draft/` is linked.
- Quotes that are still examples stay marked `sample`.
- You did not add a refund or a guarantee. Those are not in `config.js`.
