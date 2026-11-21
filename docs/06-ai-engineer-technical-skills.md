# 06 · AI Engineer Technical Skills

This chapter is what separates an **AI filmmaking engineer** from a **prompt user**. A prompt user types into a website and hopes. An engineer builds repeatable systems: consistent characters, controllable shots, automated batches, tracked costs, versioned projects.

**You do not need a computer science degree.** Every skill below starts from zero. Words are defined the first time they appear.

> **Costs on this page were checked 2026-11-21.** INR at ₹94.85/USD.

## Skills overview

| # | Skill | Time to learn (basics) | Cost to learn |
|---|---|---|---|
| 1 | Prompt engineering for video | 1–2 weeks | Free credits |
| 2 | Character & style consistency (incl. LoRA basics) | 2–3 weeks | Free–$20/mo |
| 3 | ComfyUI node workflows | 2–4 weeks | Free (own GPU) or ~$0.34/hr cloud |
| 4 | Python basics for automation | 4–6 weeks | Free |
| 5 | Using model APIs (keys, cost, rate limits) | 1–2 weeks | $5–$20 of API credit |
| 6 | GPU & cloud basics | 1 week | Free (Colab) / pay-per-hour |
| 7 | FFmpeg | 1 week | Free |
| 8 | Upscaling, interpolation, colour pipelines | 1–2 weeks | Free–$25/mo |
| 9 | Version control (Git + Git LFS) | 1 week | Free |
| 10 | Agentic pipelines | 3–6 weeks | API costs |

---

## 1. Prompt engineering for video

**What it is:** writing instructions a video model can follow reliably. A good video prompt is a *shot description*, not a story.

**Why it matters:** the same model gives amateur or professional results depending on prompt structure. Structure also makes prompts reusable in code.

**A reliable structure (fill in the brackets):**

```
[SHOT SIZE + ANGLE], [SUBJECT + key look], [ACTION — one clear verb],
[SETTING + time of day], [LIGHTING], [CAMERA MOVEMENT], [LENS],
[MOOD / COLOUR / FILM STOCK], [DURATION if supported]
Negative: [things to avoid]
```

Example: *"Medium close-up, low angle. A tired female astronaut, cracked visor, sweat on brow. She slowly lifts her visor and exhales. Inside a dim, red-lit airlock. Hard red emergency light from above, soft cyan fill. Slow dolly in. 50mm lens. Tense, desaturated, 35mm film grain. Negative: text, watermark, extra fingers, morphing face."*

**Vocabulary to master:** shot sizes (EWS, WS, MS, MCU, CU, ECU), angles (low, high, Dutch, OTS, POV), lenses (24/35/50/85/135mm, macro, anamorphic), lighting (key, rim, practical, motivated, golden hour, neon), camera moves (pan, tilt, dolly, truck, crane, orbit, handheld, whip pan, rack focus).

**Negative prompts:** a list of things you do *not* want. Not every model supports them (many newer ones ignore them); where unsupported, phrase positively ("clean frame, no on-screen text").

**Tips:** one action per shot; put camera info first; keep under ~60 words for most video models; use image-to-video when you need control over composition.

- **Learning resource:** practise with the [prompt library](../prompts/ai-video-prompt-library.md) and StudioBinder's free [shot-size and camera classes](https://www.studiobinder.com/online-film-school).
- **Cost:** free credits on Google Flow / Kling to practise. **Time:** 1–2 weeks.

## 2. Character & style consistency

**What it is:** keeping the same face, costume, and visual style across many shots — the #1 technical problem in AI film.

**Techniques, easiest first:**
1. **Character reference sheet** — one image showing the character from front, side, back, plus close-up expressions, on a plain background. Generate it once; reuse it everywhere. ([prompts](../prompts/ai-video-prompt-library.md#2-character-reference-sheets))
2. **Image-to-video** — generate the *still* first (where you control the face), then animate it. Far more consistent than text-to-video.
3. **Reference / "ingredients" features** — many tools accept reference images of a character or object (e.g. Flow's ingredients-to-video, Kling/Runway references, Nano Banana edits).
4. **Style references** — a reference image or style code that keeps the colour, texture and lighting consistent (Midjourney style references, image-to-image).
5. **Fixed text "bible"** — the exact same character description pasted into every prompt.
6. **LoRA basics** — a **LoRA** ("Low-Rank Adaptation") is a small add-on file (often 10–200 MB) trained on 15–40 images of your character or style. Loaded into an open model (e.g. in ComfyUI), it teaches the model that specific face or look. Training can be done locally with ~12–24 GB VRAM or on rented GPUs. **Only train on images you own or have permission to use.**

- **Learning resource:** [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) (free) for how diffusion and fine-tuning work.
- **Cost:** free–$20/month (image tool) + optional GPU time for LoRA training. **Time:** 2–3 weeks.

## 3. ComfyUI node workflows

**What it is:** [ComfyUI](https://github.com/Comfy-Org/ComfyUI) is a free, open-source (GPL-3.0) app that runs AI models as a **graph of nodes** — boxes connected by wires, each doing one step (load model → write prompt → load image → generate → save video). You can see and control every step and save the whole graph as a reusable file.

**Install (simple path):**
1. Go to the [official ComfyUI docs](https://docs.comfy.org/) → *Download & Install*. Desktop installers exist for Windows and macOS; Linux users install from GitHub.
2. Open ComfyUI → **Templates** (workflow browser) → *Video*.
3. Pick a **Wan 2.2 5B** text/image-to-video template. ComfyUI's docs say the Wan 2.2 5B version "should fit well on 8GB vram with the ComfyUI native offloading". Click *download missing models* (several GB).

**Run a basic image-to-video graph:**
1. **Load Image** node → choose your character still.
2. **Prompt** node → describe only the *motion*: "she turns her head toward the window, hair moves in a light breeze, slow push-in".
3. Set resolution (start small, e.g. 832×480), frames (~81 frames ≈ 5 s at 16 fps), and steps.
4. Click **Run** (Queue). The video appears in the Save node and in `ComfyUI/output/`.
5. Save the workflow (`.json`) into your project's Git repo.

**GPU reality check:** Wan's own repository lists its single-GPU 5B command at ≥24 GB VRAM and the 14B models at ≥80 GB **unquantized**; community quantized versions (smaller, slightly lower quality) run 14B on 16–24 GB. LTX-Video can run on 8 GB with heavy quantization and offloading. **No suitable GPU? Rent one** (see §6).

- **Learning resource:** [docs.comfy.org](https://docs.comfy.org/) (free); [Wan 2.2 repo](https://github.com/Wan-Video/Wan2.2); [LTX-Video repo](https://github.com/Lightricks/LTX-Video).
- **Cost:** free software; GPU you own, or ~$0.34–$0.69/hour for a rented RTX 4090. **Time:** 2–4 weeks.

## 4. Python basics for automation

**What it is:** Python is a beginner-friendly programming language. For filmmaking you need a small slice: variables, lists, loops, reading CSV files, calling web APIs, handling files, and running FFmpeg.

**Why it matters:** generating 60 shots by hand on a website takes days of clicking. A 100-line script does it overnight, logs every prompt and cost, and can re-run a single failed shot.

**Learn in this order:** variables & strings → lists & loops → functions → reading/writing CSV → `os.environ` for secrets → making HTTP requests → `subprocess` to run FFmpeg.

- **Learning resource:** [Google Colab](https://colab.research.google.com/) (free browser notebooks — no install) + any free beginner Python course; then read the working example below line by line.
- **Cost:** free. **Time:** 4–6 weeks at 1 hour/day.

## 5. Using model APIs: keys, cost per second, rate limits

**What it is:** an **API** (Application Programming Interface) lets code send a request ("make a 5-second video of…") to a company's servers and get a result back. You pay per use instead of a monthly plan.

**Three things to understand:**

1. **API keys** — a secret password for your account. Rules: store it in an **environment variable** or a `.env` file that is listed in `.gitignore`; **never** paste it in code, screenshots, or Git. If leaked, revoke it immediately in the provider's dashboard.
2. **Cost per second of video** (checked 2026-11-21):

| Provider / model | Price | 5-second clip |
|---|---|---|
| Runway API – Gen-4 Turbo | 5 credits/s × $0.01 = $0.05/s | $0.25 (₹24) |
| Runway API – Gen-4.5 | 12 credits/s = $0.12/s | $0.60 (₹57) |
| fal.ai – Wan 2.5 | $0.05/s | $0.25 (₹24) |
| fal.ai – Kling 2.5 Turbo Pro | $0.07/s | $0.35 (₹33) |
| Replicate – Kling v2.0 | $0.28/s | $1.40 (₹133) |
| Gemini API – Veo 3.1 Lite (720p) | $0.05/s | $0.25 (₹24) |
| Gemini API – Veo 3.1 Fast (720p) | $0.10/s | $0.50 (₹47) |
| Gemini API – Veo 3.1 Standard | $0.40/s | $2.00 (₹190) |

   Remember **retries**: if you keep 1 in 4 takes, a $0.25 clip really costs $1.00 per *usable* clip.
3. **Rate limits** — maximum requests per minute. Exceed them and you get **HTTP 429 "Too Many Requests"**. Good code waits and retries (the example does this).

Sources: [Runway API pricing](https://docs.dev.runwayml.com/guides/pricing/), [fal.ai pricing](https://fal.ai/pricing), [Replicate docs](https://replicate.com/docs), [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing).

- **Cost:** $5–$20 of credit is plenty to learn. **Time:** 1–2 weeks.

### Working example: batch-generate shots from a CSV

The full script is in [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py) and the sample input in [`prompts/example-shots.csv`](../prompts/example-shots.csv). It uses only Python's standard library and the Replicate HTTP API.

```bash
# 1. Put your key in the environment (never in the file)
export REPLICATE_API_TOKEN="r8_your_key_here"        # macOS / Linux
# $env:REPLICATE_API_TOKEN="r8_your_key_here"        # Windows PowerShell

# 2. Dry run: shows requests + estimated cost, spends nothing
python scripts/batch_generate_videos.py prompts/example-shots.csv --dry-run --price-per-second 0.10

# 3. Real run, then stitch a rough cut with FFmpeg
python scripts/batch_generate_videos.py prompts/example-shots.csv \
  --model bytedance/seedance-1-pro --price-per-second 0.10 --stitch
```

The core idea, simplified:

```python
import csv, json, os, time, urllib.request

token = os.environ["REPLICATE_API_TOKEN"]          # key comes from the environment
model = "bytedance/seedance-1-pro"                  # check the model's API tab for inputs

def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "Prefer": "wait"})
    return json.loads(urllib.request.urlopen(req).read())

with open("prompts/example-shots.csv", newline="") as f:
    for row in csv.DictReader(f):
        pred = post(f"https://api.replicate.com/v1/models/{model}/predictions",
                    {"input": {"prompt": row["prompt"]}})
        print(row["shot_id"], pred["status"], pred.get("urls", {}).get("get"))
        time.sleep(2)                                # be polite to rate limits
```

The full script adds polling until each job finishes, retries on HTTP 429, a cost estimate, a generation log, skip-if-already-downloaded, and FFmpeg stitching.

## 6. GPU & cloud basics

**What it is:** a **GPU** (graphics card) does the maths for AI models. **VRAM** is the GPU's own memory; models must fit in it (or be partly "offloaded" to normal RAM, which is slower).

| VRAM | What you can realistically run locally |
|---|---|
| 8 GB (e.g. RTX 4060) | Image models; Wan 2.2 5B and LTX with offloading/quantization; short, low-res video |
| 12–16 GB | Comfortable image work, LoRA training, quantized Wan 14B at 480p |
| 24 GB (RTX 4090) | Wan 2.2 comfortably, LTX-2 quantized at 720p |
| 32 GB+ (RTX 5090) / 80 GB (A100/H100) | Full-quality open video models, faster iteration |

**Local vs cloud:** local = one-time hardware cost, private, no hourly bill, but limited by your VRAM. Cloud = rent big GPUs by the hour.

| Option | Price (checked 2026-11-21) | Good for |
|---|---|---|
| [Google Colab](https://colab.research.google.com/) | Free (T4 when available); Pro $9.99/mo (100 compute units); Pro+ $49.99/mo | Learning, small tests |
| [RunPod](https://www.runpod.io/pricing) | RTX 4090 from $0.34/hr (Community) or $0.69/hr (Secure); A100 80GB from $1.19/hr | Running ComfyUI + Wan/LTX for hours |

**Habit:** always **stop** cloud machines when finished — you pay while they run.

- **Time:** 1 week.

## 7. FFmpeg for stitching, converting, frame extraction

**What it is:** [FFmpeg](https://ffmpeg.org/documentation.html) is a free command-line tool that can do almost anything with video files. Learn these and you can automate post-production chores.

```bash
# Convert any clip to a standard 1080p, 24 fps H.264 MP4
ffmpeg -i in.mov -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24" -c:v libx264 -crf 18 -preset veryfast -c:a aac out.mp4

# Stitch clips listed in list.txt (lines like: file 'S01.mp4')
ffmpeg -f concat -safe 0 -i list.txt -c copy rough_cut.mp4      # same format clips only

# Extract the LAST frame of a clip (use it as the start frame of the next shot!)
ffmpeg -sseof -0.1 -i S01.mp4 -frames:v 1 S01_last.png

# Extract one frame per second as images (for contact sheets / reviews)
ffmpeg -i S01.mp4 -vf fps=1 frames/S01_%03d.png

# Trim the wobbly first 0.3 s of an AI clip
ffmpeg -ss 0.3 -i S01.mp4 -c:v libx264 -crf 18 S01_trim.mp4

# Add music under a silent cut
ffmpeg -i rough_cut.mp4 -i score.mp3 -map 0:v -map 1:a -shortest -c:v copy -c:a aac with_music.mp4
```

The **last-frame trick** is a core continuity technique: chain shots by using the final frame of shot A as the first frame of shot B in image-to-video.

- **Cost:** free. **Time:** 1 week.

## 8. Upscaling, frame interpolation and colour pipelines

- **Upscaling** — AI-increase resolution (720p → 4K). Tools: Topaz Video ($29/mo or $299/yr), DaVinci Resolve Studio Super Scale, Krea upscaler.
- **Frame interpolation** — create in-between frames: 16 fps AI output → smooth 24/30 fps, or slow motion. Tools: Topaz, RIFE-based nodes in ComfyUI, Resolve's optical flow.
- **Recommended order:** pick takes → trim → **interpolate** to final frame rate → **upscale** → **grade** in Resolve → add grain last. (Grade after upscaling so the upscaler doesn't amplify colour noise; add grain last so it isn't "sharpened".)
- **Colour pipeline:** work in one colour space for the whole project (e.g. Rec.709 for web delivery); normalise every AI clip to it with a correction node; then apply one shared "look" node across all clips.

- **Cost:** free (Resolve free + ComfyUI) to ~$29/month. **Time:** 1–2 weeks.

## 9. Version control for creative projects (Git + Git LFS)

**What it is:** **Git** records every change to your project files so you can go back in time, try ideas on **branches**, and collaborate. **Git LFS** (Large File Storage) handles big media files without bloating the repository.

```bash
git init my-short && cd my-short
git lfs install
git lfs track "*.mp4" "*.mov" "*.wav" "*.png" "*.safetensors"
git add .gitattributes
echo ".env" >> .gitignore          # never commit API keys
git add . && git commit -m "Project skeleton"
```

What to version: scripts, shot lists, prompt CSVs, ComfyUI workflow `.json` files, Python code, Resolve project exports, selected final clips. What **not** to: API keys, huge raw generations you'll never use (keep those on an external drive or cloud bucket).

- **Learning resource:** [git-lfs.com](https://git-lfs.com/). **Cost:** free (GitHub has LFS storage quotas — check your plan). **Time:** 1 week.

## 10. Agentic pipelines: script → shot list → prompts → generation → edit

**What it is:** an **agentic pipeline** chains AI steps so each output becomes the next input, with you approving at checkpoints:

```
script.md ──(LLM)──▶ shot_list.csv ──(LLM + style bible)──▶ prompts.csv
   ──(image API)──▶ keyframes/ ──(you approve)──▶ (video API)──▶ clips/
   ──(FFmpeg)──▶ rough_cut.mp4 ──(you, in Resolve)──▶ final film
```

**How to build it step by step:**
1. **Script → shot list:** ask an LLM (Claude/ChatGPT/Gemini) to output a CSV with `shot_id, size, angle, action, duration, dialogue`. Validate the columns in Python.
2. **Shot list → prompts:** combine each row with your fixed **style bible** and **character bible** text in a template (no LLM needed — plain string formatting is more consistent).
3. **Prompts → keyframes:** generate stills with an image API; **human checkpoint**: pick the best per shot.
4. **Keyframes → clips:** image-to-video API calls (the script in §5).
5. **Clips → rough cut:** FFmpeg concat in shot order; import into Resolve for the real edit.
6. **Log everything:** prompt, model, seed, cost, time — so you can reproduce or fix any shot.

**Keep humans in the loop** for creative choices (story, takes, edit). This makes better films *and* strengthens your copyright position (see [08](08-legal-ethics-copyright.md)).

- **Cost:** API usage (a 2-minute film with 24 shots × 4 takes × 5 s at $0.07/s ≈ $34). **Time:** 3–6 weeks to build a version you trust.

## Learning path summary

| Week | Skill focus | Output |
|---|---|---|
| 1–2 | Prompting + consistency | 12 consistent keyframes |
| 3–4 | ComfyUI | Saved image-to-video workflow |
| 5–8 | Python | Script that reads a CSV and prints prompts |
| 9 | APIs | First paid API clip, key in env var |
| 10 | FFmpeg + Git | Automated rough cut, versioned repo |
| 11–14 | Agentic pipeline | Script → rough cut with checkpoints |
