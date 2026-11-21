# 00 · The Zero-to-Pro Roadmap

**Who this is for:** anyone starting from zero — no film school, no coding — who wants to become an **AI filmmaking engineer**: someone who can tell a story *and* build the technical pipeline that turns it into a finished film using AI tools.

**How long it takes:** roughly **12 months** at 8–10 hours a week. Faster if you study full-time; slower is fine too. Each stage ends with a **checkpoint** — a small, concrete thing you must produce before moving on.

> **Two skill tracks run side by side.**
> 1. **Craft** — story, camera language, editing, sound. AI does not replace this; it amplifies it. A bad story rendered beautifully is still a bad film.
> 2. **Engineering** — prompting, consistency, ComfyUI, Python, APIs, FFmpeg, pipelines. This is what turns you from "someone who types prompts" into someone studios and agencies hire.

## The stages at a glance

| Stage | Timeline | Focus | Checkpoint (must produce) |
|---|---|---|---|
| 0 · Orientation | Week 1 | Set up accounts, folders, a free editing tool; watch AI shorts critically | A one-page "film taste" document: 5 films you love and why |
| 1 · Story foundations | Weeks 2–5 | Loglines, structure, short scripts, shot lists | A 2–3 page short script + logline + shot list |
| 2 · Visual language | Weeks 6–9 | Shot sizes, lenses, lighting, composition, colour | A 12-frame storyboard made with an image generator |
| 3 · Production & sound | Weeks 10–13 | Directing performance, blocking, sound design, voice | A 30-second scene with voice + SFX + music |
| 4 · Editing & colour | Weeks 14–18 | Cutting rhythm, continuity, colour grading in DaVinci Resolve | Re-edit of a scene two different ways (tension vs comedy) |
| 5 · AI tools fluency | Weeks 19–24 | Image → video generation, lip-sync, upscaling, consistency | A 60-second AI short with one consistent character |
| 6 · Engineering | Weeks 25–34 | Prompt systems, ComfyUI, Python + APIs, FFmpeg, Git | A script that batch-generates 10 shots from a CSV and stitches them |
| 7 · Production pipeline | Weeks 35–42 | Script → shot list → prompts → generation → edit, end to end | A 3–5 minute short made with your own pipeline |
| 8 · Career & distribution | Weeks 43–52 | Portfolio, festivals, freelancing, legal hygiene | Portfolio site + 2 festival submissions + 1 paid or spec project |

## Stage details

### Stage 0 — Orientation (Week 1)
- Install **DaVinci Resolve** (free). Create free accounts on one chat assistant (Claude, ChatGPT or Gemini), one image tool, and one video tool (Google Flow or Kling free credits).
- Make a project folder structure you will reuse: `01_script/ 02_refs/ 03_images/ 04_video/ 05_audio/ 06_edit/ 07_exports/`.
- Watch 5 AI-made shorts (e.g. from the [Runway AI Film Festival](https://aif.runwayml.com/2024)) and 5 traditional shorts. For each, write: what worked, what felt "AI-fake", and why.
- **Checkpoint:** your "film taste" page.

### Stage 1 — Story (Weeks 2–5) → [01 · Story & screenwriting](01-story-screenwriting.md)
- Learn loglines, three-act and five-beat short structures, character want vs need, scene goals.
- Write three loglines a day for a week. Pick one. Write a 2–3 page script.
- **Checkpoint:** script + logline + shot list (shot number, size, action, dialogue, duration).

### Stage 2 — Visual language (Weeks 6–9) → [02 · Cinematography](02-cinematography-visual-language.md)
- Shot sizes, angles, focal length, depth of field, three-point lighting, colour psychology.
- Translate every shot in your shot list into an image prompt using camera vocabulary.
- **Checkpoint:** a 12-frame storyboard with consistent character and lighting.

### Stage 3 — Production & sound (Weeks 10–13) → [03 · Production, directing & sound](03-production-directing-sound.md)
- Performance direction (for AI: describing micro-expressions and motion), blocking, the 180° rule, sound layers (dialogue, ambience, SFX, music).
- **Checkpoint:** a 30-second scene with voice, room tone, effects and score.

### Stage 4 — Editing & colour (Weeks 14–18) → [04 · Post-production](04-post-production-editing-color.md)
- Complete Blackmagic's free beginner training path for DaVinci Resolve.
- Cutting on action, J and L cuts, pacing, colour correction vs grading, matching shots from different AI models.
- **Checkpoint:** one scene cut two different ways.

### Stage 5 — AI tool fluency (Weeks 19–24) → [05 · Tools & costs](05-ai-filmmaking-tools.md)
- Image-to-video, start/end frames, camera-control prompts, lip-sync, voice cloning (with consent), upscaling.
- Learn character consistency with reference sheets.
- **Checkpoint:** 60-second short, one consistent character, no visible identity drift.

### Stage 6 — Engineering (Weeks 25–34) → [06 · AI engineer skills](06-ai-engineer-technical-skills.md)
- Prompt templates, ComfyUI image-to-video graphs, Python basics, calling video APIs with environment-variable keys, FFmpeg, Git + Git LFS, GPU/cloud basics.
- **Checkpoint:** a Python script that reads `prompts.csv`, generates clips through an API, downloads them, and uses FFmpeg to stitch a rough cut.

### Stage 7 — Pipeline (Weeks 35–42) → [07 · Workflow step by step](07-ai-film-workflow-step-by-step.md)
- Run the full workflow on a 3–5 minute short. Track cost per finished second.
- **Checkpoint:** finished short + a one-page "pipeline report" (tools, cost, time, what you'd automate next).

### Stage 8 — Career (Weeks 43–52) → [08 · Legal & ethics](08-legal-ethics-copyright.md) · [09 · Career](09-career-portfolio-festivals.md)
- Portfolio, showreel, festival strategy, freelance offers, contracts and disclosure.
- **Checkpoint:** portfolio live, two festival submissions, one real or spec client project.

## Weekly rhythm that works

| Day | Activity (1–2 h) |
|---|---|
| Mon | Learn (read/watch one lesson) |
| Tue | Practise the lesson's exercise |
| Wed | Generate / shoot |
| Thu | Edit |
| Fri | Engineering hour (code, ComfyUI, FFmpeg) |
| Sat | Make — work on the current checkpoint |
| Sun | Review: post your work, get feedback, update your [progress checklist](../learners/progress-checklist.md) |

## "Am I ready to move on?" self-test

- Can I explain *why* I chose each shot, not just what it shows?
- Could someone else follow my folder and file names?
- Do I know what this cost me in credits/money per finished second?
- Did I show it to at least one person and act on their notes?

If you answer yes to all four, move on.

## Two paths through this repo

- **Learners:** follow the [90-day self-study plan](../learners/90-day-self-study-plan.md) for Stages 0–5 + a first film, then continue with Stages 6–8 here.
- **Trainers:** use the [12-week syllabus](../trainers/course-syllabus-12-weeks.md), which compresses Stages 1–7 into a class.
