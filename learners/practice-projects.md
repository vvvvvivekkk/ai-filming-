# Five Practice Projects (Easy → Hard)

Each project has a **brief**, the **tools** (with a free option), and **"done when"** criteria. Do them in order — each adds one major skill. Prices checked 2026-11-21 (see [docs/05](../docs/05-ai-filmmaking-tools.md)).

| # | Project | New skill | Length | Typical cost |
|---|---|---|---|---|
| 1 | One-shot mood piece | Prompting + camera language | 10–15 s | $0 |
| 2 | Consistent-character storyboard | Character consistency | 12 frames | $0–$10 |
| 3 | 30-second dialogue scene | Voice, lip-sync, sound, editing | 30 s | $0–$20 |
| 4 | Automated music video | Python/API or ComfyUI + FFmpeg | 45–60 s | $5–$20 |
| 5 | Festival-ready short | Full pipeline | 2–4 min | ~$44–$60 |

---

## Project 1 — The one-shot mood piece

**Brief:** Create a single 10–15 second shot that makes a viewer feel one specific emotion (dread, wonder, nostalgia...) with **no dialogue**. Add ambience and one sound effect.

**Tools:** an image generator (Gemini app / ChatGPT free) → Google Flow or Kling free credits for image-to-video → ElevenLabs free SFX → DaVinci Resolve free.

**Steps:** write the emotion and a one-sentence moment → design the frame with shot size, lens, light, colour → generate 3 stills, pick one → animate with one deliberate camera move → add sound → export.

**Done when:**
- [ ] Three people name the emotion you intended without being told.
- [ ] Your prompt uses shot size, lens, lighting and camera move vocabulary.
- [ ] Ambience + at least one SFX are synced.
- [ ] Exported as 1080p MP4.

---

## Project 2 — The consistent-character storyboard

**Brief:** Design one original character and produce a **12-frame storyboard** telling a tiny story (beginning, middle, end) in which the character is unmistakably the same person in every frame, across at least 3 locations and 2 lighting setups.

**Tools:** Nano Banana (Gemini app), GPT Image, or Midjourney Basic ($10/mo); the [character sheet prompts](../prompts/ai-video-prompt-library.md#2-character-reference-sheets).

**Done when:**
- [ ] A character reference sheet (front/side/back + 3 expressions) exists.
- [ ] Character bible and style bible text blocks are written and used in every prompt.
- [ ] All 12 frames pass a "spot the drift" check by a friend.
- [ ] The story is understandable from the frames alone.

---

## Project 3 — The 30-second dialogue scene

**Brief:** Two characters, one location, a short exchange (4–6 lines) with a turn — something changes by the end. Build sound first, then visuals.

**Tools:** ElevenLabs (free for practice; Starter $6/mo for commercial use) → HeyGen free / your video tool's lip-sync → Kling/Flow/Runway for shots → Resolve for edit, mix and grade.

**Done when:**
- [ ] Coverage includes a wide/master, two singles and one insert or reaction shot.
- [ ] The 180° rule is respected (eye-lines match).
- [ ] Lip-sync is convincing in at least the two most important lines (use over-the-shoulder or off-screen lines to avoid weak ones).
- [ ] Four sound layers present; dialogue clearly audible over music.
- [ ] Colour matches across all shots.

---

## Project 4 — The automated music video

**Brief:** Make a 45–60 second music video where all shots are generated from a **CSV** by code (or by a saved ComfyUI workflow), then stitched automatically and finished by hand.

**Tools:**
- **API route:** [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py) + Replicate/fal/Runway API ($5–$20 credit) + FFmpeg.
- **Free route:** ComfyUI + Wan 2.2 5B or LTX-Video on your GPU, Google Colab, or a rented RunPod GPU (~$0.34/hr).
- Music: Suno Pro ($8/mo, downloaded track for commercial rights) or a royalty-free track.

**Done when:**
- [ ] `prompts.csv` has 10–15 rows built from a template + style bible.
- [ ] The API key lives only in an environment variable; `.env` is in `.gitignore`.
- [ ] A generation log records prompt, model and status for every shot.
- [ ] FFmpeg produces a rough cut automatically; you finish the edit to the beat in Resolve.
- [ ] Project is in a Git repo with Git LFS for media and a README explaining how to run it.
- [ ] You report total cost and cost per usable second.

---

## Project 5 — The festival-ready short

**Brief:** A 2–4 minute short film with a clear story, made with the full [12-step workflow](../docs/07-ai-film-workflow-step-by-step.md), delivered to festival standard.

**Tools:** Starter stack (~$44/month, ₹4,172) or equivalent; DaVinci Resolve; FFmpeg; Git.

**Done when:**
- [ ] Script, shot list, prompts CSV, keyframes, animatic all exist in the project folder.
- [ ] One consistent main character; no visible identity drift.
- [ ] Graded, mixed, captioned; master 1080p (or 4K) + 9:16 teaser + poster frame.
- [ ] Credits include an AI disclosure statement and human credits.
- [ ] Rights audit completed (every asset has source, plan, licence).
- [ ] One-page pipeline report written.
- [ ] Published online with a breakdown, and submitted to at least one festival or challenge whose AI rules you have read.
- [ ] Self-scored with the [final project rubric](../trainers/assignments-and-rubrics.md#final-project-rubric) at 24/32 or above.
