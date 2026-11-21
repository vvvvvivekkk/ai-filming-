# 11 · How AI Video Actually Works — Explained From Zero

> **Who this is for:** complete beginners. No maths, no code needed. Every new word is explained the first time it appears, and is also in the [glossary](10-glossary.md). Read this before the tool pages ([05](05-ai-filmmaking-tools.md), [12](12-tool-by-tool-guide.md)) and everything else will make more sense.

## What it is

When you type "a lighthouse in a storm, slow push-in, cinematic" and get a 5-second clip back, a lot happens behind the button. This chapter explains that process in plain English, so you can:

- understand **why** results go wrong (melting hands, changing faces, flicker),
- choose the **right tool** for each shot,
- spend **fewer credits** by getting closer on the first try.

## Why it matters for AI film

Filmmakers who understand the machine direct it better. Think of a cinematographer who knows how a lens works: they don't need to grind glass, but knowing *what* a lens does lets them choose the right one. This chapter is your "how the lens works".

---

## 1. What "AI" and a "model" are

**Artificial intelligence (AI)** here means software that learned a skill from examples instead of being programmed rule by rule.

A **model** is the result of that learning: one very large file full of numbers, sometimes billions of them, called **weights**. Those numbers store patterns the model saw during training, like "this is what waves look like when the camera moves" or "this is how a smile changes a face".

- **Training** = the learning phase. The company shows the model millions of examples (images, video clips, sounds) along with descriptions of them. This takes huge numbers of expensive **GPUs** (graphics chips that do many calculations at once) running for weeks.
- **Inference** = using the finished model. Each time you press *Generate*, the company runs your request through the model on its GPUs. That GPU time is what your **credits** pay for.

**Model vs tool.** *Kling 2.x*, *Veo 3.1*, *Wan 2.2* and *Seedance* are **models**. *Kling AI*, *Google Flow*, *Krea* and *ComfyUI* are **tools**: apps that let you use models. One tool can offer many models (an **aggregator** like Krea or Higgsfield), and one model can appear in many tools (Seedance is in Dreamina, Runway and Krea).

## 2. Diffusion — how images and video come out of noise

Almost every image and video generator today is a **diffusion model**. Here is the idea in four steps:

1. **Start with static.** The model begins with pure random noise, like a TV with no signal.
2. **Guess and clean.** It asks itself: "If this noise were secretly a *lighthouse in a storm*, what would it look like slightly less noisy?" Then it removes a little noise in that direction.
3. **Repeat.** It does this over many **steps** (often 20–50). Each step makes the picture a bit clearer. You can sometimes see this as a blurry preview that sharpens.
4. **Finish.** After the last step you have a clean image. For video, it cleans a whole stack of frames together, so they agree with each other.

**How did it learn to clean?** During training, researchers took real images, added noise on purpose, and taught the model to undo it. Do that millions of times, with text descriptions attached, and the model learns how words connect to pictures.

**Latent space (why it's fast enough to be possible).** Cleaning millions of pixels directly would be painfully slow. So models first squash images into a compact "idea" form called **latent space**, do the cleaning there, and expand the result back into pixels at the end. You don't need to touch this; just know it is why generation takes seconds or minutes rather than hours.

**Guidance (CFG).** Many tools have a slider called *guidance*, *CFG* or *prompt strength*. It controls how strictly the model sticks to your words:

- too low → it wanders and ignores you;
- too high → colours and contrast look harsh and "over-cooked";
- the default is usually right for beginners.

## 3. Prompts — what the model actually "reads"

A **prompt** is the text instruction you give. The model doesn't understand it like a person does. It matches your words to patterns it learned. That's why:

- **Concrete words beat vague ones.** "Wide shot, 24mm lens, low angle, wet cobblestones reflecting orange streetlight" works better than "make it look cool".
- **Order and focus matter.** Put the most important thing (subject + action) first.
- **Film vocabulary works**, because training videos were often described with it. That's why chapters [02](02-cinematography-visual-language.md) and the [prompt library](../prompts/ai-video-prompt-library.md) matter.
- **A negative prompt** (in some tools) lists what you *don't* want ("blurry, extra fingers, text").

A simple template you can reuse:

> **[Shot size] of [subject] [doing action] in [place], [lighting], [camera move], [lens/style], [mood].**
> Example: *Medium close-up of an old fisherman mending a net on a dock at dawn, soft golden backlight, slow push-in, 50mm, shallow depth of field, quiet and hopeful.*

## 4. Text-to-video vs image-to-video vs reference-to-video

| Method | You give it | Best for | Beginner tip |
|---|---|---|---|
| **Text-to-video (T2V)** | Only words | Quick ideas, B-roll, establishing shots | Least control; expect several tries |
| **Image-to-video (I2V)** | A starting image + words | Keeping the look you designed | **The main method for films.** Design the frame in an image tool first, then animate it |
| **First + last frame** | A start image and an end image | Controlled transitions and camera moves | Great for matching cuts |
| **Reference-to-video / "ingredients"** | One or more images of a character, object or place | Keeping the **same character** across shots | Use a clean, front-facing character sheet |
| **Video-to-video / motion transfer** | A real video + a target look or character | Copying real acting, dance, fights | Film yourself on a phone as the "actor" |

**Rule of thumb for beginners:** make the picture first (image tool), then make it move (video tool). It's cheaper and far more consistent than text-to-video alone.

## 5. Credits, seeds, resolution, fps and duration — the settings that cost money

**Credits.** A tool's in-app money. Each generation spends credits based on **model**, **length**, **resolution** and sometimes **audio**. A 5-second clip might cost 20 credits on a "fast" model and 400 on a premium one. Most plans' credits **expire monthly**. So before you buy, work out roughly how many clips your plan really gives you.

**Seed.** The number that decides the starting noise. Same prompt + same seed + same settings → very similar result. Change the seed → a different version. Writing down the seed of a shot you like lets you make small variations of it later.

**Resolution.** Pixels per frame. **720p** (1280×720) is cheap and fine for tests. **1080p** (1920×1080) is the normal delivery size. **4K** (3840×2160) is usually made by **upscaling** a 1080p clip later (e.g. Topaz Video), not by generating in 4K directly.

**fps (frames per second).** How many still images make one second of video. **24 fps** looks like cinema; 30 fps looks like TV or phone video. Many models generate at 24 fps. Keep your whole edit at one frame rate. **Frame interpolation** tools can invent in-between frames for slow motion.

**Duration.** Most models give **5–10 seconds** per clip, some up to ~15–20. Films are built from many short clips, just like real films are built from many short shots. That's normal, not a limitation to fight.

**Aspect ratio.** The shape of the frame. 16:9 for YouTube/TV, 9:16 for Reels/Shorts, 2.39:1 for a "widescreen cinema" feel (generate 16:9, then crop).

## 6. Why faces drift, hands melt and things flicker

The model doesn't "know" your character is one person. It just predicts frames that look plausible. Common problems:

| Problem | Why it happens | Fixes |
|---|---|---|
| **Face drift**: the character slowly looks like someone else | Each frame is generated with some freedom; small changes add up | Image-to-video from a strong starting frame, reference images, shorter clips (5 s), fewer big head turns |
| **Different face in every shot** | Each generation starts fresh | Character reference sheet, the same reference images every time, a LoRA (a small add-on model trained on your character; see [06](06-ai-engineer-technical-skills.md)) |
| **Melting hands / extra fingers** | Hands are small, complex and move a lot | Hide or simplify hands, use medium shots, regenerate, fix in edit |
| **Flicker / boiling textures** | Weak **temporal consistency** (frames don't fully agree) | Lower motion, better model, upscaler with temporal smoothing, edit around it |
| **Physics fails** (water, cloth, crowds) | Hard to learn from video alone | Simpler action, cut away early, combine with real footage |
| **Garbled text on signs** | Letters are tiny patterns | Use text-strong image tools (Ideogram, GPT Image, Nano Banana) for the first frame, or add text in the edit |

**Directing mindset:** treat each clip like a take on set. Generate 2–4 takes, pick the best, and plan your edit to hide weak moments.

## 7. How AI voices, voice cloning and lip-sync work

**Text-to-speech (TTS).** A model trained on many hours of recorded speech learns how written words become sound: rhythm, pitch and emotion. You type a line, pick a voice, and get audio. Tools like ElevenLabs let you steer emotion with punctuation, tags and stability settings.

**Voice cloning.** You upload recordings of one person. The model learns that person's voice "fingerprint" and can say new lines in it. **Only clone voices with written consent.** Cloning someone without it can break platform rules and the law (see [08 · Legal](08-legal-ethics-copyright.md)).

**Lip-sync.** A model looks at the face in a video and the sound waves of the dialogue, then redraws just the mouth area so lips match the words. Some tools animate a whole face from **one photo** (Hedra, HeyGen); others **re-time the mouth** on existing footage (sync.so). Several video models now produce **native audio**, meaning dialogue and sound generated together with the picture (Veo 3.1, Kling).

**AI music.** Music models (Suno, Stable Audio, AIVA) learned patterns of melody, rhythm and instruments. **Read the licence**: who owns the song, and can you use it commercially? It differs by plan.

## 8. Motion capture, 3D and real-time engines (the "hybrid" path)

Pure AI video struggles with exact control. Many pros mix in 3D:

- **Motion capture (mocap)** records how a real body moves. **AI mocap** (Move AI, Autodesk Flow Studio) does it from ordinary phone video, with no special suit.
- **3D software** (Blender, free) lets you build a set, place a virtual camera and animate exact moves. **Text-to-3D** tools (Meshy) create props quickly.
- **Real-time engines** (Unreal Engine) render 3D instantly like a video game, so you can see a scene and move the camera live.
- **Hybrid workflow:** block the scene in 3D (exact camera move) → render a rough pass → use it as the input for a video model (video-to-video) to get a polished, consistent look.

You don't need this on day one. It becomes valuable once you want shots that are *exactly* repeatable.

## 9. Open weights vs closed models

| | **Closed (hosted) models** | **Open-weights models** |
|---|---|---|
| Examples | Veo, Kling, Runway, Midjourney | Wan 2.2, LTX Video, FLUX (some versions), Stable Diffusion |
| Where it runs | On the company's servers; you use a website or API | You can download it and run it on **your own GPU** or a rented cloud GPU |
| Cost | Subscription or pay per second | Free model; you pay for hardware/electricity or GPU rental |
| Control | Limited to the company's settings | Full control: custom workflows, LoRAs, no content queue |
| Difficulty | Easy | Harder (ComfyUI, drivers, VRAM) |

**"Open weights" isn't always "open source".** Some licences limit commercial use or big companies. Always read the licence file.

**VRAM** is the memory on your graphics card. Video models need a lot: 8 GB works only with tricks (**quantization**, which shrinks the model, and **offloading**, which borrows normal RAM), 16 GB is workable, and 24–32 GB is comfortable. See [06](06-ai-engineer-technical-skills.md) for setup.

## 10. Where the money and the risk go

- **Credits** pay for GPU inference. Premium models, longer clips, higher resolution and audio all cost more.
- **Free tiers** usually add watermarks and **don't allow commercial use**.
- **Training data** affects legal risk. Models trained on **licensed data** (e.g. Adobe Firefly, Moonvalley Marey) are designed to be safer for client work.
- **Copyright of outputs:** in the US, purely AI-generated material isn't protected by copyright; your human creative choices (script, edit, arrangement) can be. Details are in [08 · Legal](08-legal-ethics-copyright.md).

---

## One hands-on exercise (45 minutes, free)

**Goal:** *see* the ideas from this chapter.

1. In a free image tool (Gemini app or ChatGPT), make **one** character portrait using the template in section 3. Save it.
2. In Google Flow's free credits (or Kling's free tier), make **two clips** of the same idea:
   - Clip A: text-to-video only (no image).
   - Clip B: image-to-video from your saved portrait.
3. Compare: which kept the face better? Which matched your idea?
4. Regenerate Clip B once with a different seed (or just "regenerate") and note what changed.
5. Write three sentences: what drifted, what stayed, and which method you'd use for a real film.

## How AI helps

Paste this chapter's headings into Claude, ChatGPT or Gemini and ask: *"Quiz me with 10 beginner questions on how diffusion video models work, then explain anything I get wrong using a cooking analogy."* Then ask it to explain any word in [the glossary](10-glossary.md) "like I'm 12".

## Free resources to go deeper

| Resource | What it is | Link |
|---|---|---|
| Google Flow help | How Flow's credits, frames and ingredients work | <https://flow.google.com/pricing> |
| ComfyUI docs | Official docs for the free node-based tool | <https://docs.comfy.org/> |
| Hugging Face Diffusers docs | Beginner-friendly explanations of diffusion pipelines | <https://huggingface.co/docs/diffusers/index> |
| US Copyright Office AI page | Official guidance on AI and copyright | <https://www.copyright.gov/ai/> |
