# 08 · Legal, Ethics & Copyright

> **Not legal advice.** This chapter explains the landscape in plain language so you know which questions to ask. Laws differ by country and change fast. For paid or client work, read each tool's current terms and talk to a qualified lawyer in your jurisdiction.

## What it is (simply)

- **Copyright** — the legal right to control copying of an original creative work. In most countries it exists automatically when a *human* creates something original.
- **Licence / terms of service** — the contract you accept when you use a tool. It decides whether *you* may use outputs commercially, whether the company may use your uploads, and what you're not allowed to make.
- **Likeness / personality rights** — rights people have over their face, voice and identity.
- **Trademark** — protects brand names and logos (you can't put someone's logo in your ad without permission).

## The big question: can I copyright an AI film?

The **US Copyright Office** has published a three-part report on AI ([copyright.gov/ai](https://www.copyright.gov/ai/)):

- **Part 1: Digital Replicas** (31 July 2024).
- **Part 2: Copyrightability** (29 January 2025) — summary at [copyright.gov/newsnet/2025/1060.html](https://www.copyright.gov/newsnet/2025/1060.html). Key points:
  - Existing copyright principles apply to generative AI.
  - AI-generated output is protectable **only where a human contributed sufficient expressive elements** — for example a human-authored work perceptible in the output, or creative arrangement or modification by a human. **Prompts alone are not enough.**
  - Using AI to *assist* creation, or including AI material inside a larger human-made work, does **not** bar copyright in the human parts.
- **Part 3: Generative AI Training** (pre-publication version, 9 May 2025) — about whether training on copyrighted works is lawful; final version pending.

**What this means for you in practice:**
- Your **script, edit, selection and arrangement of shots, voice performance you recorded, original music you composed, and modifications you made** are your strongest copyright claims.
- Raw, unmodified AI clips from a prompt may not be protected by copyright in the US — someone else may be able to reuse them.
- **Document your human contribution**: keep script drafts, storyboards, prompt logs, edit project files and before/after versions. Git history helps (see [06](06-ai-engineer-technical-skills.md#9-version-control-for-creative-projects-git--git-lfs)).
- Outside the US (India, EU, UK, etc.) rules differ — check locally.

## Tool terms: commercial use checklist

Before using any output in paid work, check (and screenshot the terms with the date):

1. **Plan level** — free tiers usually forbid commercial use (e.g. ElevenLabs free has no commercial licence; Suno free songs are non-commercial; Kling/Luma/Pika free outputs are for testing).
2. **Revenue thresholds** — Midjourney requires Pro or Mega for companies earning over $1M/year; Stability AI's Community Licence is free for organisations under $1M/year; Topaz Studio allows only limited commercial use for organisations under $1M revenue (Studio Pro has full commercial use).
3. **Downloads** — Suno now limits commercial use to downloaded songs within a monthly allowance; Udio downloads are disabled (verify).
4. **Open-weight licences** — Wan 2.2 is Apache-2.0 (permissive). FLUX.2 [dev] weights are non-commercial. LTX-2 uses a community licence with separate commercial terms. "Open" does not always mean "free for business".
5. **Training on your uploads** — does the tool use your images/footage to train? Many let you opt out on paid tiers.
6. **Indemnity** — some enterprise plans (e.g. Adobe Firefly enterprise offerings) promise legal protection; most consumer plans do not.

Prices and terms referenced here were checked 2026-11-21; see [05 · Tools](05-ai-filmmaking-tools.md).

## Ethics: rules a professional follows

1. **Consent for faces and voices.** Never clone a real person's voice or face without **written permission**. Many tools ban it in their terms and many places have laws against it (the US Copyright Office's Part 1 report covers digital replicas).
2. **No impersonation or deception.** Don't make content that could be mistaken for real news or real statements by real people.
3. **Don't copy protected characters, logos or specific artworks.** Being "inspired by a genre" is fine; reproducing Mickey Mouse or a famous painting is not.
4. **Disclose AI use** where audiences, clients, platforms or festivals expect it. Platforms like YouTube and many festivals have AI-disclosure rules — read each one.
5. **Credit the humans.** Actors, voice artists, composers, editors — credit them, pay them fairly, and get releases.
6. **Respect labour agreements.** If you work with union performers or writers, their contracts may contain AI clauses.
7. **Avoid harmful stereotypes.** Models reproduce biases from training data; review casting and depictions deliberately.

## Simple paperwork kit

| Document | Use |
|---|---|
| **Talent release** | Permission to use a person's face/voice, including AI processing |
| **Voice-cloning consent form** | Specific, written consent: which voice, which project, how long |
| **Music licence / receipt** | Proof of your Suno/Soundraw plan and download date, or composer agreement |
| **Tool terms snapshot** | PDF/screenshot of each tool's terms on the date you generated |
| **Generation log** | Prompts, models, dates, seeds (the script in [06](06-ai-engineer-technical-skills.md) writes one) |
| **AI disclosure statement** | One paragraph in your credits/description describing how AI was used |

## Hands-on exercise: "Rights audit"

Take a finished short (yours or a classmate's). For every asset (each clip, voice, music cue, font, logo), fill a table: *source tool · plan · date · commercial use allowed? · human contribution · risk (low/med/high)*. Fix or replace every "high".

**Done when:** you could hand the table to a client's lawyer without embarrassment.

## How AI helps at this stage

- Summarise a tool's terms of service in plain language (then read the key clauses yourself).
- Draft release and consent forms as a starting point for a lawyer to review.
- Generate your disclosure statement and credits list from your generation log.
- **Never** rely on an AI's answer as legal advice.
