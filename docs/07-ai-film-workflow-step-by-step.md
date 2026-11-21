# 07 · AI Film Workflow, Step by Step

A complete, repeatable workflow for a **2–5 minute AI short**. Each step lists the goal, the tools, the output file, and a quality gate (don't move on until it passes).

```
1 Idea → 2 Script → 3 Shot list → 4 Look & characters → 5 Keyframes
→ 6 Animatic → 7 Video generation → 8 Voice & sound → 9 Edit
→ 10 Enhance & grade → 11 Mix & deliver → 12 Release & review
```

## Project folder (copy this)

```
my-short/
├── 01_script/        script.md, logline.txt
├── 02_shotlist/      shot_list.csv, prompts.csv
├── 03_refs/          lookbook/, character_sheets/
├── 04_keyframes/     S01_v1.png, S01_v2.png ...
├── 05_clips/         S01_take1.mp4 ...
├── 06_audio/         dialogue/, sfx/, music/
├── 07_edit/          resolve_project.drp, exports/
├── 08_delivery/      final_1080p.mp4, final_9x16.mp4, captions.srt
├── logs/             generation_log.csv, cost_log.csv
└── .gitignore        (.env, raw renders)
```

## Step 1 — Idea (½ day)
- **Goal:** one logline you're excited about, scoped to what AI does well.
- **Tools:** notebook, Claude/ChatGPT/Gemini for brainstorming.
- **Output:** `logline.txt`.
- **Gate:** can you say it in one breath? Is there a character who changes?

## Step 2 — Script (1–3 days)
- **Goal:** 2–5 pages, few locations, limited lip-synced dialogue.
- **Tools:** StudioBinder's free screenwriting app or any writer; LLM for critique.
- **Output:** `script.md`.
- **Gate:** read aloud; every action line is filmable.

## Step 3 — Shot list (1 day)
- **Goal:** every shot numbered, 3–8 s each, one action per shot.
- **Columns:** `shot_id, scene, size, angle, lens, movement, action, dialogue/VO, duration, notes`.
- **Output:** `shot_list.csv` (open in any spreadsheet).
- **Gate:** total duration ≈ target runtime; no shot asks for two complex actions.

## Step 4 — Look & characters (1–2 days)
- **Goal:** a visual bible everybody (including your future self) can follow.
- **Make:** lookbook (8–12 reference frames, palette, lens list), **character reference sheets** (front/side/back + expressions), **location sheets**, a 3–5 line **style bible** text block and **character bible** text block pasted into every prompt.
- **Tools:** Midjourney / Nano Banana / GPT Image / Flux.
- **Gate:** the same character is instantly recognisable across all sheets.

## Step 5 — Keyframes (2–3 days)
- **Goal:** one approved still per shot (the first frame of each video).
- **How:** build `prompts.csv` from shot list + bibles; generate 2–4 options per shot; pick one.
- **Tools:** image tool of choice; [prompt library](../prompts/ai-video-prompt-library.md).
- **Output:** `04_keyframes/S01_final.png` etc.
- **Gate:** lay all keyframes in a grid — lighting, colour and character match.

## Step 6 — Animatic (½ day)
- **Goal:** test timing *before* spending video credits.
- **How:** drop keyframes into DaVinci Resolve at the planned durations; add scratch voice and temp music.
- **Gate:** the story works as a slideshow. If not, fix it now — it's cheap here, expensive later.

## Step 7 — Video generation (3–7 days)
- **Goal:** usable clips for every shot.
- **How:** image-to-video from each keyframe; prompt only the **motion and camera**. Use start+end frames for controlled moves. For continuity, use the **last frame** of one clip as the first of the next (FFmpeg command in [06](06-ai-engineer-technical-skills.md#7-ffmpeg-for-stitching-converting-frame-extraction)).
- **Budget:** plan 3–4 takes per shot. Track in `cost_log.csv`.
- **Tools:** Kling, Runway, Flow/Veo, Hailuo, Seedance, or local Wan/LTX in ComfyUI; batch via [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py).
- **Gate:** no identity drift, no melting hands in hero moments, motion matches the animatic.

## Step 8 — Voice & sound (2–3 days)
- **Dialogue/VO:** ElevenLabs (commercial licence from Starter); lip-sync with HeyGen or the video tool's lip-sync feature.
- **Ambience & SFX:** ElevenLabs SFX, libraries, your own recordings (foley with household objects).
- **Music:** Suno (paid, downloaded songs) or Soundraw; or a human composer.
- **Gate:** eyes-closed test — the soundtrack alone tells you where and when you are.

## Step 9 — Edit (2–4 days)
- **How:** replace animatic stills with chosen takes; trim the first/last wobbly frames; cut around artefacts with reaction/insert shots; J/L cuts for dialogue.
- **Tools:** DaVinci Resolve (free).
- **Gate:** watch it with someone who hasn't seen it; note where they look away or get confused.

## Step 10 — Enhance & grade (1–2 days)
- **Order:** interpolate to 24 fps → upscale (if delivering 4K) → colour-correct each clip to match → apply one shared look → film grain last.
- **Tools:** Topaz Video or Resolve Studio; Resolve Color page.
- **Gate:** scopes look consistent shot-to-shot; skin tones natural.

## Step 11 — Mix & deliver (1 day)
- **Mix:** dialogue clear above music; consistent levels; check on headphones *and* phone speaker.
- **Deliver:** 1080p or 4K H.264/H.265 MP4 master, 9:16 teaser, captions `.srt`, poster frame, credits that disclose AI tools used.
- **Gate:** watch the exported file start to finish on the device your audience will use.

## Step 12 — Release & review (ongoing)
- Post, submit to festivals (see [09](09-career-portfolio-festivals.md)), and write a one-page **pipeline report**: tools, total cost, cost per finished second, hours spent, what to automate next time.

## Typical budget for a 3-minute short (Starter stack)

| Item | Estimate |
|---|---|
| ~36 shots × 3–4 takes × 5 s | Covered by Google AI Pro + Kling Standard credits ($29.99/mo combined) — may need a top-up |
| Voices & SFX | ElevenLabs Starter $6 |
| Music | Suno Pro $8 |
| Editing | DaVinci Resolve free |
| **Total** | **≈ $44–$60 for one month (₹4,172–₹5,691)** |

Prices checked 2026-11-21; see [05 · Tools & costs](05-ai-filmmaking-tools.md).

## Common failure points and fixes

| Problem | Fix |
|---|---|
| Character face changes between shots | Image-to-video from approved keyframes; reference images; same character bible text; LoRA for long projects |
| Motion is floaty or slow-motion | Ask for specific speed ("quick", "snaps"), shorter clips, interpolate later instead of asking for slow-mo |
| Hands/text glitch | Frame them out, cut away, or use inserts generated separately |
| Colours don't match across models | Normalise in Resolve with scopes; shared look node; add uniform grain |
| Running out of credits | Animatic first; cheaper "draft" models (e.g. Gen-4 Turbo, Veo Lite) for tests, premium models for finals |
| Lip-sync looks uncanny | Fewer on-screen talking shots; voice-over; over-the-shoulder angles; dedicated lip-sync tool |
