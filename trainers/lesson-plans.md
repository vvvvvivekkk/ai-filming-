# Lesson Plans (Weeks 1–12)

Each session is **3 hours** with a 10-minute break. Timings are a guide. "Demo" = trainer shares screen; "Activity" = students work. Prices/tools checked 2026-11-21.

**Standard session shape:** 10 min recap & homework review → 40 min concept → 30 min demo → 10 min break → 70 min activity → 20 min share & critique.

---

## Week 1 — Orientation: the AI film landscape
- **Duration:** 3 h · **Materials:** projector, 3 AI shorts from the [Runway AI Film Festival](https://aif.runwayml.com/2024), 2 traditional shorts, folder template from [docs/07](../docs/07-ai-film-workflow-step-by-step.md#project-folder-copy-this).
- **Concept (40 min):** what an AI filmmaking engineer does; craft vs engineering tracks; the 12-step pipeline; why story still wins.
- **Demo (30 min):** install DaVinci Resolve; create the project folder; generate one image and one 5-s clip live with free credits; show cost per clip.
- **Activity (70 min):** watch the shorts; in pairs fill a critique grid (story / visuals / consistency / sound / "AI tells"). Create accounts on one assistant, one image tool, one video tool.
- **Share:** each pair presents one "AI tell" and how they'd avoid it.
- **Exit ticket:** one sentence — what film do you want to make?

## Week 2 — Story & loglines
- **Materials:** logline formula handout ([docs/01](../docs/01-story-screenwriting.md)), timer.
- **Concept:** want vs need, stakes, three-act and five-beat shorts, designing stories for AI's strengths.
- **Demo:** use an AI assistant as a *critic*, not an author: paste a weak logline, ask for weaknesses, rewrite it yourself.
- **Activity:** 10-minute logline sprints ×3; peer "pitch speed-dating" (60 s each); vote-free feedback.
- **Share:** top 3 loglines per student with one sentence on stakes.

## Week 3 — Scripting & shot lists
- **Materials:** StudioBinder screenwriting app, shot-list CSV template.
- **Concept:** screenplay format, visual action lines, limiting dialogue, 1 page ≈ 1 minute.
- **Demo:** convert one page into a shot list (shot_id, size, angle, action, duration); then ask an LLM to do it and compare.
- **Activity:** draft scripts; convert first scene to a shot list.
- **Share:** read one scene aloud; class marks any un-filmable line.
- **Homework:** **Assignment 1**.

## Week 4 — Visual language & lookbooks
- **Materials:** film stills for analysis (use stills legally — educational fair use varies by country), image tool access.
- **Concept:** shot sizes, lenses, angles, three-point and motivated light, colour palettes.
- **Demo:** same prompt with 24 mm vs 85 mm, high vs low angle, warm vs cool — project side by side.
- **Activity:** "one moment, six ways" exercise; start a lookbook (palette, lens list, 8 refs).
- **Share:** gallery walk of six-frame grids.

## Week 5 — Characters & consistency
- **Materials:** character sheet prompts from the [prompt library](../prompts/ai-video-prompt-library.md#2-character-reference-sheets).
- **Concept:** why identity drifts; reference sheets; character/style bibles; image-to-video; intro to LoRA.
- **Demo:** build a turnaround sheet; reuse it for 4 shots in different lighting; show a failure and fix.
- **Activity:** each student makes a main-character sheet and 12-frame storyboard.
- **Share:** "spot the drift" — peers flag frames where the character changes.
- **Homework:** **Assignment 2**.

## Week 6 — Image-to-video & camera motion
- **Materials:** free/paid credits on Flow, Kling or Runway; credit log sheet.
- **Concept:** I2V vs T2V; prompting motion only; start/end frames; camera vocabulary; draft vs final models; cost per usable second.
- **Demo:** animate one keyframe with dolly-in, orbit and handheld; extract the last frame with FFmpeg to chain the next shot.
- **Activity:** animate 6 storyboard frames; log credits per take and keep rate.
- **Share:** best and worst take; what changed between them.

## Week 7 — Directing performance, voice & sound
- **Materials:** headphones, ElevenLabs free accounts, consent form template from [docs/08](../docs/08-legal-ethics-copyright.md#simple-paperwork-kit).
- **Concept:** directing with verbs and micro-expressions; four sound layers; voice ethics and consent; lip-sync options.
- **Demo:** build a 20-s soundscape from scratch (ambience → foley/SFX → voice → music); lip-sync one line.
- **Activity:** "sound first" scene — audio before visuals.
- **Share:** eyes-closed listening; class guesses location and action.
- **Homework:** **Assignment 3**.

## Week 8 — Editing in DaVinci Resolve
- **Materials:** a shared footage pack (12–15 AI clips) so everyone edits the same material.
- **Concept:** rhythm, cutting on action, J/L cuts, cutting around artefacts, first-frame wobble.
- **Demo:** assemble → rough → fine cut in Resolve's Cut and Edit pages.
- **Activity:** "same footage, two films" (thriller vs comedy).
- **Share:** blind screening — class guesses each genre.

## Week 9 — Colour, enhancement & finishing
- **Materials:** clips from 3 different models; Resolve Color page; Topaz or Krea demo account (trainer only is fine).
- **Concept:** correction vs grading; scopes; matching models; interpolation → upscale → grade → grain order; delivery specs and captions.
- **Demo:** normalise three mismatched clips with scopes; one shared look node; export master + 9:16 + SRT.
- **Activity:** grade and deliver last week's edit.
- **Homework:** **Assignment 4**.

## Week 10 — Engineering: ComfyUI, Python/API, FFmpeg, Git
- **Materials:** Google Colab notebook or RunPod pod with ComfyUI (trainer sets up in advance), [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py), [`prompts/example-shots.csv`](../prompts/example-shots.csv), a class API key held by the trainer (**never shown on screen**).
- **Concept:** what an API is; keys in environment variables; cost per second; rate limits; ComfyUI nodes; Git LFS.
- **Demo:** run a ComfyUI image-to-video template; run the batch script in `--dry-run`, then a 2-shot live run; stitch with FFmpeg; commit to Git.
- **Activity:** students write their own `prompts.csv` from their shot list and run the dry run; pairs with keys run 5 shots.
- **Homework:** **Assignment 5**.

## Week 11 — Pipeline production + legal & ethics
- **Materials:** rights-audit template ([docs/08](../docs/08-legal-ethics-copyright.md#hands-on-exercise-rights-audit)).
- **Concept (30 min only):** US Copyright Office guidance (human authorship; prompts alone insufficient), tool licences, consent, disclosure.
- **Activity (2 h):** studio time on final films with trainer 1-on-1s (10 min each); students complete rights audit.
- **Share:** 3 volunteers show work-in-progress for notes.

## Week 12 — Screening, portfolio & festivals
- **Materials:** projector + good speakers, feedback cards.
- **Session:** screening (each film + 2-minute pipeline talk: tools, cost, cost per second, one lesson learned); peer feedback; 30 min portfolio/festival planning with [docs/09](../docs/09-career-portfolio-festivals.md).
- **Close:** certificates, next steps (Stages 6–8 of the [roadmap](../docs/00-roadmap.md)).

## Trainer tips
- Re-check tool availability and prices the week before each cohort — this field changes monthly (Sora shut down in 2026).
- Keep a "plan B" tool for every demo in case a site is down.
- Model the ethics: show disclosure in your own demos.
- Collect anonymised cost logs each cohort to give future students realistic budgets.
