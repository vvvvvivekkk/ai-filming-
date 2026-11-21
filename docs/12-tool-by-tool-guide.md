# 12 · Tool-by-Tool Beginner Guide

> **Who this is for:** beginners who open [05 · Tools & costs](05-ai-filmmaking-tools.md), see 66 tools and feel lost. This chapter explains **every category** and the **main tools in it**, in plain English: *what it is · when to use it · how to start · tips · pitfalls*. Prices and links are in [05](05-ai-filmmaking-tools.md) and [`data/tools-and-costs.csv`](../data/tools-and-costs.csv) (checked 2026-11-21). New words are explained in [11 · How AI video works](11-how-ai-video-works-explained.md) and the [glossary](10-glossary.md).

## What it is

A map of the AI filmmaking toolbox, ordered the way you'd use it on a real project:

**Write → Plan/storyboard → Design images → Generate video → Voice & lip-sync → Motion & 3D → Music & SFX → Edit & finish → Automate (APIs/open models).**

## Why it matters for AI film

No single tool does everything well. Pros pick **one main tool per job** and learn it deeply, instead of trying everything at once. Use this chapter to choose your first tool in each row, and ignore the rest until you need them.

**Golden rule for beginners:** pick **one** image tool + **one** video tool + **DaVinci Resolve**, and make three short films before you add anything else.

---

## 1. Writing & planning

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Claude** | AI chat assistant, strong at long writing and code | Story ideas, script drafts, shot lists, Python help | Free plan at claude.ai; paste your logline and ask for 5 versions | Ask it to *critique* your script, not just write it | It can't see your footage; check facts and maths |
| **ChatGPT** | OpenAI's assistant with image generation built in | Brainstorming, quick concept images, prompt rewriting | Free plan; Plus $20 for heavier use | Ask: "rewrite this as a video prompt with shot size, lens, light, move" | Free tier has limits and may show ads |
| **Gemini / Google AI plans** | Google's assistant; paid plans include Flow video credits and Nano Banana images | If you want writing + images + video in one Google bill | Free app; AI Plus $4.99 or AI Pro $19.99 for Flow credits | AI Pro is the best-value bundle for beginners | Credit amounts differ by plan; check monthly |
| **Final Draft 13** | Paid screenwriting app (industry standard) | When a producer or festival expects a properly formatted script | Free trial, then one-time purchase ($249.99 list, $199.99 on sale; $99.99 students) | Learn 6 elements: scene heading, action, character, dialogue, parenthetical, transition | Expensive for beginners; free apps are fine at first |
| **WriterDuet** | Online screenwriting app with live co-writing | Writing with a partner | Free tier (check current limits) | Export to PDF and .fdx (Final Draft format) | Paid tier needed for heavier use (verify price) |

**Start with:** Claude or ChatGPT free + WriterDuet free.

## 2. Storyboarding & pre-production

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Boords** | Storyboard and **animatic** app (an animatic is a timed slideshow of your frames with sound) | Planning every shot *before* spending credits; showing clients | Free plan (3 active scripts) | Time the animatic to your voiceover; it reveals pacing problems early | Free PDFs are watermarked; paid from $39/mo |
| **LTX Studio** | All-in-one script → storyboard → video studio | Planning a whole short in one place | Free 800 one-time credits (personal use) | Good for pitching an idea fast | Commercial use only on Standard ($35) and Pro |
| **Pen and paper / phone photos** | Stick figures and phone snapshots | Always, it's free | Draw 6–12 boxes per scene | Mark shot size and camera move on each box | — |

**Start with:** paper or Boords free. Planning saves more money than any discount.

## 3. Image & character design

Images are the foundation: you design each shot as a still, then animate it (image-to-video).

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Midjourney** | Image generator known for beautiful, cinematic looks | Mood boards, style frames, concept art | Basic plan $10/mo (no free tier) | Use `--sref` (style reference) and `--cref`/omni-reference for consistency | Images are public unless you buy Pro/Mega with Stealth |
| **Nano Banana (Gemini image)** | Google's image model, excellent at **editing** and keeping a character the same | Character sheets, changing outfits/angles of one character | Free in Gemini app (limited) | Upload your character and ask for "same person, new angle" | Limited free uses per day |
| **GPT Image (ChatGPT)** | OpenAI's image model | Readable text, edits, reference sheets | Free in ChatGPT (limited) | Great for title cards and posters | Can be slow at peak times |
| **FLUX** | Black Forest Labs' image models; some versions downloadable | High quality stills; local use in ComfyUI | Try via Krea, fal.ai or locally | The best "open" image option for local workflows | Licences differ by version; read them |
| **Adobe Firefly** | Adobe's image/video models trained on licensed content | Client work where legal safety matters; Photoshop users | Free credits with an Adobe account | Use Generative Fill in Photoshop to fix frames | Credits run out fast on video |
| **Leonardo AI** | Image + video suite with many fine-tuned models | Concept art, game-style characters | Free 150 tokens/day | Train a custom model on your character | Free images are public |
| **Ideogram** | Image model best at **text inside images** | Signs, posters, title cards inside a shot | Free (10 slow credits/week) | Generate the sign as a separate image and composite it | Free images are public |
| **Recraft** | Image + **vector** generator (vectors stay sharp at any size) | Logos, film titles, poster graphics | Free plan | Export SVG for titles in Resolve | Free outputs are owned by Recraft, not for commercial use |

**Start with:** Gemini (Nano Banana) free; add Midjourney Basic when you want a stronger look.

## 4. Video generation

This is where your stills start moving. Each clip is usually 5–10 seconds.

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Google Flow (Veo 3.1 / Gemini Omni)** | Google's filmmaking app with frames, "ingredients" (references) and scene builder | Cinematic shots **with sound** | 100 free credits/month; more with AI Plus/Pro | Use "frames to video" with your designed first frame | Fast models cost less; premium ones use credits quickly |
| **Kling AI** | Kuaishou's video model; strong human motion | Character movement, action, value for money | Small free credits; Standard $10 | Try motion control with a reference video | Free plan isn't for commercial use |
| **Runway** | Pro video platform with many models and editing tools | Controlled camera moves, references, all-round work | Free trial credits; Standard $15 | Use its references and camera controls; it also hosts partner models | Credits disappear fast on top models |
| **Seedance (Dreamina)** | ByteDance's model; good at multi-shot clips | Short multi-shot sequences, social content | Free daily credits on Dreamina | Also available inside Runway, Krea, Higgsfield | Promo prices change; check renewal price |
| **Hailuo (MiniMax)** | Expressive, low-cost video | Emotional close-ups, experiments | One-time trial pack (3 days) | Check checkout discounts | No refunds; trial expires quickly |
| **Luma** | Dream Machine / Luma Agents (Ray video models in a creative workspace) | Stylised and experimental shots, fast ideas | No free plan now; Plus $30 | Good for transitions with start/end frames | Pricier entry than Kling/Vidu |
| **Pika** | Playful effects and quick social videos | Fun edits, effects | Free plan (credit packs, no commercial licence); Starter $10 | Use for stylised social cut-downs | Less suited to long narrative work |
| **Vidu** | Shengshu's model, strong reference consistency | Same character across shots | Trial credits; Standard $10 | Upload 2–3 reference images of the character | No refunds |
| **PixVerse** | Fast, cheap clips with effect templates | Quick tests, social clips | 60 + 30 daily free credits | Good for testing ideas before premium models | Free = watermark and 540p |
| **Moonvalley Marey** | Model trained only on **licensed** footage | Commercial work where clean training data matters | No public price; contact sales (verify) | Ask clients if they need "clean data" models | Pricing and access may change (verify) |
| **Grok Imagine (xAI)** | xAI's image-to-video | Quick animated shots | SuperGrok or API | Short stylised motion | No free access now |
| **Higgsfield** | Aggregator focused on camera-motion presets | Dramatic camera moves | Free credits | Try presets like crash zoom or bullet time | Uses partner models; quality varies |
| ~~OpenAI Sora~~ | **Shut down in 2026** | — | — | Skip old Sora tutorials | — |

**Start with:** Google Flow free + Kling free. Upgrade one of them when you hit the limit.

## 5. Voice & lip-sync

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **ElevenLabs** | Leading AI voice tool: text-to-speech, cloning, dubbing, SFX | Narration, character voices, sound effects | Free plan (non-commercial, attribution) | Use the Starter plan ($6) the moment you publish anything commercial | Clone only voices you have consent for |
| **HeyGen** | Talking avatars and video translation | Presenter videos, dubbing to other languages | Free (watermark) | Good for explainers, less for drama | Avatar look can feel "corporate" |
| **Hedra** | Animates a face from **one image + audio** into an expressive talking character | Dialogue shots, talking creatures | No free plan; Basic $20 (2,000 credits) | Use a clear, front-facing face with a neutral mouth | Head movement is limited; keep shots short |
| **sync.so** | **Lip-sync** onto existing footage (re-times the mouth) | Fixing dialogue, dubbing your film into Hindi or Telugu | Hobbyist $5 + per-second usage (1-min max) | Works on real actors and AI characters | Pay-per-second adds up on long scenes |

**Start with:** ElevenLabs free → Starter. Use Kling or Flow built-in lip-sync before paying for a dedicated tool.

## 6. Motion capture & 3D (the "hybrid" path)

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Viggle** | **Motion transfer**: makes any character copy a reference video's movement | Dances, fights, specific gestures | Free daily credits (watermark) | Film yourself on a phone as the reference "actor" | Backgrounds can wobble; composite if needed |
| **Autodesk Flow Studio** (formerly Wonder Studio) | AI replaces a filmed actor with a CG character, with lighting and camera matched | Live-action + CG character shots | Free tier (limited) | Shoot with a steady camera and clear lighting | Learning curve; plan prices need verifying |
| **Move AI** | **Markerless mocap** (no suit) from phone video | Recording movement for 3D characters in Blender/Unreal | Move One iPhone app (from $15/mo) | Wear fitted clothes; film the full body | Pro pricing is custom |
| **Meshy** | Text/image-to-**3D model** | Props, set pieces, simple characters | 100 free credits/month | Clean up the model in Blender | Free outputs need attribution (CC BY 4.0) |
| **Blender** | Free, open-source 3D software | Building sets, previs, exact camera moves | Download free from blender.org | Follow a beginner "donut" tutorial first | Big learning curve, but worth it |
| **Unreal Engine** | Free real-time 3D engine used in virtual production | Virtual sets, real-time previs, cinematic rendering | Free if your company earns under $1M/year | Use free Fab/Quixel assets for realistic sets | Needs a strong GPU; heavy software |

**Start with:** Viggle free for fun; Blender when you want exact control.

## 7. Music & sound effects

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **Suno** | AI song generator (vocals + instruments) | Songs, themes, music videos | Free (no downloads) | Pro $8 includes downloads and commercial use | Download limits per month |
| **Udio** | AI music generator | Experiments only | Free credits | — | **Downloads disabled since Feb 2026**, so you can't use it for delivery |
| **AIVA** | AI composer for **orchestral/cinematic** scores you can edit | Film-style background score | Free (AIVA owns copyright); Standard €11 / Pro €33 per month billed yearly | Only the Pro plan gives *you* the copyright | Read the ownership terms by plan |
| **Stable Audio** | Music + sound-effect generator | Ambiences, risers, loops, SFX | 50 free credits with a commercial licence | Ask for "loopable" ambience for long scenes | Longer tracks need paid plans |
| **Soundraw** | Editable royalty-free AI music | Background tracks you can shape per section | Preview free, paid to download | Adjust energy per section to match your edit | No free downloads |
| **ElevenLabs SFX** | Text-to-sound-effect | Footsteps, doors, weather, sci-fi sounds | Included in ElevenLabs plans | Layer 2–3 sounds for realism | Commercial use needs a paid plan |
| **Epidemic Sound** | Licensed, human-made music + SFX library | Safe, cleared music for releases | Trial (verify) | Pick the plan that matches where you publish (own channel vs clients) | Licence is tied to your plan |
| **Artlist** | Licensed music, SFX, footage and AI credits | Music + stock footage in one subscription | No free plan | Social plan covers only your own channels | Client work needs a Pro plan |

**Start with:** YouTube Audio Library (free) + ElevenLabs SFX; add Suno Pro or Epidemic Sound when you publish.

## 8. Editing, colour, sound mix & finishing

| Tool | What it is | When to use it | How to start | Tips | Pitfalls |
|---|---|---|---|---|---|
| **DaVinci Resolve** | Free professional editor with colour grading and audio (Fairlight) | **Every project.** This is your home base | Free download from Blackmagic Design | Learn the Cut, Edit, Color and Fairlight pages, in that order | Needs a decent GPU for smooth playback |
| **Adobe Premiere Pro** | Industry-standard paid editor | If you or your clients use Adobe | Subscription | Pair with After Effects for titles | Monthly cost |
| **CapCut** | Easy editor for social video | Fast Reels/Shorts, auto-captions | Free | Great for 9:16 cut-downs | Some features paid; check terms for commercial use |
| **Descript** | Edit video by editing the transcript text | Interviews, narration-heavy pieces | Free plan | Delete words in the text to cut the video | Not for detailed film editing |
| **Topaz Video** | AI upscaling (e.g. 1080p → 4K), denoise and frame interpolation | Final delivery quality | Paid ($29/mo or $299/yr) | Upscale **only the final cut**, not every test clip | Slow on weak GPUs |
| **OpusClip** | Auto-cuts long videos into captioned short clips | Trailers, teasers, social promos of your film | Free 60 credits/month (watermark) | Review every auto-clip; it picks "viral" moments, not story moments | Free clips expire after 3 days |
| **Adobe Podcast Enhance Speech** | One-click AI cleanup of noisy dialogue | Rescuing voice recorded in a noisy room | Free (1 hr/day, files up to 30 min) | Blend the enhanced audio with a bit of the original for a natural sound | Too much enhancement sounds robotic |

**Start with:** DaVinci Resolve (free). It covers editing, colour and sound.

## 9. Aggregators (many models, one subscription)

| Tool | What it is | When to use it | Tips | Pitfalls |
|---|---|---|---|---|
| **Krea** | Real-time image, video, upscaling with many models | Trying many models without many subscriptions | Great free upscaler and real-time canvas | Promo prices change at checkout |
| **Magnific (formerly Freepik)** | Stock library + AI suite | Stock + AI in one place | Use stock for B-roll and AI for hero shots | Credits shared across many tools |
| **Higgsfield** | Camera-motion presets on top of partner models | Stylised camera moves | Quick dramatic shots | Quality depends on the underlying model |
| **invideo AI** | Prompt-to-full-video for explainers | Faceless YouTube-style videos | Fast for explainers | Not built for cinematic storytelling |

**When to choose an aggregator:** when you want to compare models side by side. **When not to:** when you've found your favourite model, because the direct subscription is often better value.

## 10. Open-source / local & automation (engineering path)

| Tool | What it is | When to use it | How to start | Pitfalls |
|---|---|---|---|---|
| **ComfyUI** | Free node-based app to run open models locally or in the cloud | Custom workflows, no queue, full control | Install from comfy.org; load a template workflow | Learning curve; GPU drivers |
| **Wan 2.2 / LTX Video** | Open-weights video models | Local video generation | Run inside ComfyUI | Needs VRAM (16 GB+ comfortable) |
| **Stable Diffusion / FLUX** | Open image models | Local images, LoRA training | Run inside ComfyUI | Licences vary |
| **Replicate / fal.ai / Runway API / Gemini API** | Pay-per-use APIs for models | Batch generation from code (see [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py)) | Get an API key; store it in an **environment variable**, never in code | Costs add up; set spending limits |
| **RunPod / Google Colab** | Rented cloud GPUs / browser notebooks | No GPU at home | Colab free tier for learning; RunPod by the hour | Remember to stop the machine or you keep paying |

**Start with:** nothing here until you've finished a few films with web tools. Then follow [06 · AI engineer skills](06-ai-engineer-technical-skills.md).

---

## Beginner starter kits

| Your situation | Kit |
|---|---|
| **₹0 budget, just learning** | Gemini app + Google Flow free + Kling free + ElevenLabs free + YouTube Audio Library + DaVinci Resolve |
| **~₹4,200/month, first real short** | The Starter stack in [05](05-ai-filmmaking-tools.md#three-budget-stacks): Google AI Pro + Kling Standard + ElevenLabs Starter + Suno Pro + Resolve |
| **Dialogue-heavy story** | Add Hedra Basic or use Kling/Flow lip-sync; ElevenLabs Creator for consistent character voices |
| **Action / dance / precise movement** | Viggle + Kling motion control; Blender for exact camera moves |
| **Client / commercial work** | Paid plans only; prefer licensed-data tools (Firefly, Marey) where the client asks; licensed music (Epidemic Sound/Artlist) |

## One hands-on exercise (60 minutes)

1. Choose **one tool per row** from the starter kit that fits your budget. Write them down.
2. Make a 3-shot sequence (wide → medium → close-up) of one character:
   - design the character in your image tool,
   - animate each shot in your video tool,
   - add one line of voice and one sound effect,
   - cut it in DaVinci Resolve.
3. Write down for each tool: what was easy, what was confusing, and how many credits you used.

## How AI helps

Ask an assistant: *"I'm a beginner with ₹X per month. Here is the tools CSV from this repo [paste]. Pick one tool per job for a 2-minute dialogue short, explain each choice in simple words, and estimate how many clips my credits will cover."* Then check its maths against [05](05-ai-filmmaking-tools.md).
