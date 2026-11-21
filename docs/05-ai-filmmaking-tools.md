# 05 · AI Filmmaking Tools and Costs

> **Price checked: 2026-11-21.** Every price below was looked up on that date, from the company's own pricing page wherever it would load. Where an official page did not show the number (some pages only render prices in a logged-in browser), we used a recent, dated third-party snapshot and marked it **(verify)**.
>
> **Currency:** USD first, INR in brackets. **Exchange rate used: 1 USD = ₹94.85** (Wise mid-market rate, checked 2026-11-21). Indian checkout prices are often *lower* than the converted USD figure because some companies (ChatGPT, CapCut, Google) use regional pricing, so always check the price shown at checkout.
>
> **Prices change monthly.** Treat this page as a snapshot. The same data is in [`data/tools-and-costs.csv`](../data/tools-and-costs.csv) so you can sort and filter it in a spreadsheet.

## How to read this page (for beginners)

- **Credits** — most AI video tools sell a monthly bag of "credits". Each generation spends some. A 5-second clip might cost 60 credits on one model and 400 on another. Credits usually **do not roll over** to the next month.
- **Free tier** — almost always watermarked and **not licensed for commercial use**. Fine for learning, not for client work.
- **Commercial use** — permission to use the output in something that earns money (ads, paid films, monetised YouTube). Read each tool's terms before client work.
- **Licensed training data** — some models (e.g. Moonvalley Marey, Adobe Firefly) say they were trained only on content they had permission to use. That lowers legal risk for client work.
- **One-time vs subscription** — Final Draft and DaVinci Resolve Studio are paid once; most AI tools charge every month.
- **API** — a way for *code* to use a model directly, usually paid per second of video or per image instead of a monthly plan. You need this for automation (see [06 · AI engineer skills](06-ai-engineer-technical-skills.md)).
- **Annual vs monthly** — "annual" prices look cheaper per month but you pay for the whole year up front.

## Important changes in 2026 you should know

- **OpenAI Sora is gone.** OpenAI's help centre says the Sora web and app experiences were discontinued on **26 April 2026** and the Sora API on **24 September 2026**. Old tutorials that use Sora will not work. ([source](https://help.openai.com/en/articles/20001152))
- **Freepik is now Magnific.** The pricing page title reads "Magnific (formerly Freepik)". ([source](https://www.magnific.com/pricing))
- **Udio downloads are disabled.** Udio's help centre says downloads were turned off on 17 February 2026 — you can make music there but cannot export it for a film. ([source](https://www.udio.com/pricing))
- **Suno now caps downloads**: Pro includes 20 song downloads/month and Premier 60; free accounts get none. ([source](https://suno.com/pricing))
- **Google changed AI plans** at I/O 2026: a new $99.99 AI Ultra tier, top Ultra tier cut from $249.99 to about $200, AI Pro stays $19.99 with 1,000 Flow credits. There is also a cheap **AI Plus** plan ($4.99, 200 Flow credits), and free accounts get 100 Flow credits a month. ([source](https://one.google.com/about/ai-premium/))
- **ChatGPT Pro is $200/month** (Go $8, Plus $20) per OpenAI's January 2026 pricing post.
- **New tool types added to this page:** storyboarding (Boords), screenwriting apps (Final Draft, WriterDuet), motion capture and 3D (Viggle, Flow Studio, Move AI, Meshy, Blender, Unreal Engine), talking-character and lip-sync tools (Hedra, sync.so), licensed music libraries (Epidemic Sound, Artlist, AIVA, Stable Audio), and short-clip/audio-cleanup helpers (OpusClip, Adobe Podcast). New to all of this? Read [11 · How AI video works](11-how-ai-video-works-explained.md) and [12 · Tool-by-tool guide](12-tool-by-tool-guide.md) first.
- **Veo on the Gemini API:** Google's video docs say the Veo 3.1 *Preview* was shut down and point to **Gemini Omni Flash**; the pricing page still lists paid Veo 3.1 models. **(verify which one you get)**

## The master table

Columns: Tool · Category · What it does · Best for · Free tier · Cheapest paid plan (USD / INR per month) · Pro plan · Commercial use · Skill level · Official link · Price checked.

| Tool | Category | What it does | Best for | Free tier | Cheapest paid (USD / INR per month) | Pro plan | Commercial use | Level | Link | Checked |
|---|---|---|---|---|---|---|---|---|---|---|
| **Claude** | Scripting/planning | Chat assistant for writing, story development, shot lists, code | Long scripts, story notes, Python help | Yes – Free plan with daily limits | $20/mo (₹1,897) – Pro (annual: $17/mo) | Max $100/mo (₹9,485) | Yes – you own outputs under Anthropic terms (verify for your use) | Beginner | [site](https://claude.com/pricing) | 2026-11-21 |
| **ChatGPT** | Scripting/planning | Chat assistant with built-in image generation | Brainstorms, loglines, quick images | Yes – Free plan (limited, may show ads) | $8/mo (₹759) – Go (Plus is $20/mo; Go price varies by country, e.g. lower in India) | Pro $200/mo (₹18,970) | Yes – per OpenAI terms (verify) | Beginner | [site](https://chatgpt.com/pricing) | 2026-11-21 |
| **Gemini / Google AI plans** | Scripting/planning | Google's assistant; paid plans bundle Flow video credits + Nano Banana images | All-in-one Google stack | Yes – Free Gemini app + 100 Flow credits/month | $4.99/mo (₹473) – AI Plus, 200 Flow credits (AI Pro is $19.99 with 1,000 credits) | AI Ultra $99.99/mo (₹9,484); top Ultra ~$200 | Yes (verify per product) | Beginner | [site](https://one.google.com/about/ai-premium/) | 2026-11-21 |
| **Final Draft 13** | Scripting/planning | Industry-standard screenwriting app (correct script format automatically) | Writing a properly formatted screenplay | Free trial | One-time $249.99 (₹23,711) list; on sale at $199.99 (Nov 2026); students $99.99 | Final Draft Suite (cloud) from $5.83/mo yearly | Yes – your script is yours | Beginner | [site](https://www.finaldraft.com/pricing) | 2026-11-21 |
| **WriterDuet** | Scripting/planning | Online screenwriting app with real-time co-writing | Writing scripts with a partner | Yes – free tier (limits: verify) | Paid plans (verify on site) | Paid tiers (verify) | Yes – your script is yours | Beginner | [site](https://www.writerduet.com/) | 2026-11-21 |
| **Boords** | Pre-production | Storyboards and animatics (timed slideshows) with AI frames and client review | Storyboarding before you generate | Yes – 3 active scripts, watermarked PDFs | $39/mo (₹3,699) – Solo monthly ($26/mo billed yearly) | Pro $75/mo (₹7,114); Team $125; Agency $250 | Yes | Beginner | [site](https://boords.com/pricing) | 2026-11-21 |
| **Midjourney** | Image/character design | Text-to-image with strong cinematic style; also short video | Look development, style frames | No free plan | $10/mo (₹948) – Basic (annual: $8/mo) | Pro $60/mo (₹5,691) – adds Stealth mode | Yes – but companies >$1M revenue need Pro or Mega | Beginner | [site](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans) | 2026-11-21 |
| **GPT Image (OpenAI)** | Image/character design | OpenAI image model inside ChatGPT and the API | Text-in-image, edits, reference sheets | Yes – limited in free ChatGPT | API: token-priced; ≈$0.01–$0.13 per 1024px image depending on model/quality (verify) | Via ChatGPT Plus $20/mo | Yes – per OpenAI terms (verify) | Beginner | [site](https://developers.openai.com/api/docs/pricing) | 2026-11-21 |
| **Nano Banana (Google Gemini image)** | Image/character design | Gemini image generation/editing; great at keeping a character consistent across edits | Character consistency, edits | Yes – limited in free Gemini app; not on free API tier | API: Nano Banana 2 $0.067 per 1K image; Nano Banana Pro $0.134 | Included in Google AI Pro $19.99/mo | Yes (verify) | Beginner | [site](https://ai.google.dev/gemini-api/docs/pricing) | 2026-11-21 |
| **FLUX (Black Forest Labs)** | Image/character design | Image models via API, plus open-weight versions you can run locally | Photoreal stills, local/ComfyUI use | Open weights (FLUX.2 [dev] is non-commercial licence) | API: 1 credit = $0.01; roughly $0.01–$0.07+ per image by model/size (verify) | Pay per use | API: yes. [dev] weights: non-commercial only | Intermediate | [site](https://docs.bfl.ai/quick_start/pricing) | 2026-11-21 |
| **Adobe Firefly** | Image/character design | Adobe's image/video/audio generator, trained on licensed content; credits for premium video | Commercially safer stills, Adobe users | Yes – limited free daily generations | $9.99/mo (₹948) – Firefly Standard, 2,000 credits | Firefly Pro $19.99/mo (₹1,896), 4,000 credits (promo $9.99 until 6 Dec 2026) | Yes – designed for commercial use | Beginner | [site](https://www.adobe.com/products/firefly/plans.html) | 2026-11-21 |
| **Leonardo AI** | Image/character design | Image + video suite with fine-tuned models and consistent characters | Concept art, character sheets | Yes – 150 tokens/day | $12/mo (₹1,138) – Apprentice, 8,500 tokens | Artisan $30/mo (₹2,846); Maestro $60 | Paid plans (free images are public) | Beginner | [site](https://leonardo.ai/pricing) | 2026-11-21 |
| **Ideogram** | Image/character design | Image model best at readable text inside pictures | Title cards, posters, signs in shots | Yes – public images, 10 slow credits/week | $20/mo (₹1,897) – Plus ($15/mo billed yearly) | Pro $60/mo (₹5,691) ($42 yearly) | Yes on paid plans (verify) | Beginner | [site](https://ideogram.ai/pricing) | 2026-11-21 |
| **Recraft** | Image/character design | Image + vector (SVG) generator for logos, icons and brand assets | Logos, film-poster graphics, style sets | Yes – images are public and owned by Recraft (not for commercial use) | $12/mo (₹1,138) – Basic | Pro $20/mo (₹1,897) | Paid plans only | Beginner | [site](https://www.recraft.ai/pricing) | 2026-11-21 |
| **Runway** | Video generation | Video generation (Gen-4.5, Aleph) plus third-party models and an editor | Image-to-video, video-to-video edits | Yes – 125 one-time credits | $15/mo (₹1,423) – Standard, 625 credits (annual: $12/mo) | Pro $35/mo (₹3,320), 2,250 credits; Max $95/mo | Paid plans: no watermark (check terms) | Beginner | [site](https://runway.com/pricing) | 2026-11-21 |
| **Kling AI** | Video generation | Kuaishou's video model; strong motion and native audio | Character motion, value per credit | Yes – Basic free plan, small credits (no commercial use) | $10/mo (₹948) – Standard list price, 660 credits (first month $6.99) | Pro $37/mo (₹3,509), 3,000 credits; Premier $92 | Paid plans only; free plan is not for commercial use | Beginner | [site](https://kling.ai/) | 2026-11-21 |
| **Google Flow (Veo 3.1 / Gemini Omni)** | Video generation | Google's AI filmmaking app: text/frames/ingredients-to-video, scene builder | Cinematic clips with sound | Yes – 100 free credits/month | $19.99/mo (₹1,896) – via Google AI Pro, 1,000 credits/mo | AI Ultra $99.99/mo (₹9,484), 10,000 credits (top Ultra 25,000) | Yes (verify per Google terms) | Beginner | [site](https://flow.google.com/pricing) | 2026-11-21 |
| **OpenAI Sora** | Video generation | DISCONTINUED: app/web shut 26 Apr 2026; API shut 24 Sep 2026 | Do not plan around it | N/A | Discontinued | Discontinued | N/A | — | [site](https://help.openai.com/en/articles/20001152) | 2026-11-21 |
| **Seedance (ByteDance)** | Video generation | ByteDance video model, sold inside Dreamina/CapCut and many aggregators | Multi-shot clips, references | Yes – ~225 shared daily credits on Dreamina | $15/mo (₹1,423) – Dreamina Basic, 1,575 credits (first-month promo often far lower) | Dreamina $36 / $79 / $520 tiers; also via Runway, Higgsfield, Krea | Yes on paid plans (verify) | Beginner | [site](https://dreamina.capcut.com/) | 2026-11-21 |
| **Luma (Dream Machine / Luma Agents)** | Video generation | Ray video models inside an agent-style creative workspace | Fast ideation, image-to-video | No free plan on current pricing page | $30/mo (₹2,846) – Plus, 10,000 credits (annual: $25/mo) | Pro $90/mo (₹8,537), 40,000 credits | Yes on paid plans | Beginner | [site](https://lumalabs.ai/pricing) | 2026-11-21 |
| **Hailuo AI (MiniMax)** | Video generation | MiniMax's video app (Hailuo / MiniMax H3 models) | Expressive motion at low cost | Yes – one-time trial pack (expires in 3 days) | $14.99/mo (₹1,422) – Standard list price, 1,000 credits; checkout often discounted (e.g. $10.50); no refunds | Pro $54.99/mo; Master $119.99; Max $216 | Paid plans: watermark-free (verify licence) | Beginner | [site](https://hailuoai.video/subscribe) | 2026-11-21 |
| **Pika** | Video generation | Playful video generation and effects (Pikaffects, swaps) | Social clips, effects | Free plan: credit packs only, no commercial licence | $10/mo (₹948) – Starter, 600 credits (annual: $8/mo) | Creator $35/mo (₹3,320), 2,600 credits | Starter and above | Beginner | [site](https://pika.art/pricing) | 2026-11-21 |
| **Higgsfield** | Video generation | Aggregator focused on camera-motion presets and cinema tools across many models | Camera moves, ads | Yes – limited use, no commercial | $15/mo (₹1,423) – Starter, 200 credits (per Higgsfield blog, Oct 2026 – verify) | Plus $49/mo; Ultra $129/mo | Paid plans: yes | Beginner | [site](https://higgsfield.ai/pricing) | 2026-11-21 |
| **Vidu** | Video generation | Shengshu's video model; strong reference-to-video consistency | Keeping one character across shots | Yes – limited trial credits | $10/mo (₹948) – Standard, 800 credits | Premium $43/mo (₹4,079); Ultimate $115 | Yes from Standard; no refunds | Beginner | [site](https://www.vidu.com/pricing) | 2026-11-21 |
| **PixVerse** | Video generation | Fast, cheap video generation with effects templates | Social clips, quick tests | Yes – 60 starting + 30 daily credits (watermark, 540p) | $10/mo (₹948) – Standard, 1,200 credits | Pro $30/mo (₹2,846); Premium $60; Ultra $199 | Paid plans (verify) | Beginner | [site](https://app.pixverse.ai/subscribe) | 2026-11-21 |
| **Moonvalley Marey** | Video generation | Video model trained only on licensed footage (lower copyright risk) | Commercial work needing clean training data | No (verify) | No public price on site; earlier reported from $14.99 for 100 credits (verify) | Contact sales for studio use | Yes – built for commercial use (verify terms) | Intermediate | [site](https://www.moonvalley.com/) | 2026-11-21 |
| **Grok Imagine (xAI)** | Video generation | xAI's image-to-video model inside Grok and the xAI API | Quick animated shots | No – free access ended | $30/mo (₹2,846) – SuperGrok subscription | API $0.05–$0.25 per second | Per xAI terms (verify) | Beginner | [site](https://docs.x.ai/docs/models/grok-imagine-video) | 2026-11-21 |
| **LTX Studio** | Video generation | Script-to-storyboard-to-video studio with consistent characters | Planning a whole short in one app | Yes – 800 one-time credits (personal use only) | $15/mo (₹1,423) – Lite, 8,000 credits/month | Standard $35/mo (₹3,320), 28,000 credits; Pro $125 | Standard and Pro only | Beginner | [site](https://ltx.io/studio/pricing) | 2026-11-21 |
| **ElevenLabs** | Voice & lip-sync / SFX | Text-to-speech, voice cloning, dubbing, sound effects, music | Narration, character voices, SFX | Yes – 10,000 credits/mo, no commercial licence | $6/mo (₹569) – Starter, 30,000 credits + commercial licence | Creator $22/mo (₹2,087); Pro $99/mo | Starter and above | Beginner | [site](https://elevenlabs.io/pricing) | 2026-11-21 |
| **HeyGen** | Voice & lip-sync | Talking avatars, lip-sync, video translation | Presenters, dubbing, lip-sync | Yes – 3 videos/mo, 1-min cap, watermark | $29/mo (₹2,751) – Creator, 600 credits (annual: $24/mo) | Pro from $49/mo (₹4,648), 4K | Paid plans | Beginner | [site](https://www.heygen.com/pricing) | 2026-11-21 |
| **Hedra** | Voice & lip-sync | Turns a still face + audio into a talking, expressive character | Talking-head and dialogue shots | No free plan listed (limited watermarked generations only) | $20/mo (₹1,897) – Basic, 2,000 credits | Pro $50/mo (₹4,743), 7,200 credits; Teams $75; Ultra from $100 | Yes – all paid plans | Beginner | [site](https://www.hedra.com/play/pricing) | 2026-11-21 |
| **sync.so** | Voice & lip-sync | Lip-sync: re-times a real or AI actor's mouth to new audio | Dubbing, fixing dialogue | No | $5/mo (₹474) – Hobbyist + usage (lipsync-2 $0.05/s; sync-3 ~$0.13/s); 1-min max video | Creator $19/mo (₹1,802), 5-min videos; Growth $49; Scale $249 | Yes (verify terms) | Intermediate | [site](https://sync.so/pricing) | 2026-11-21 |
| **Viggle** | Motion & 3D | Motion transfer: makes a character copy the movement in a reference video | Dance/action moves on any character | Yes – small daily free credits (watermark, 1-min uploads) | $7.99/mo (₹758) – Pro, 80 credits | Live $15.99; Max $63.99 (yearly 20% off) | Paid plans (verify) | Beginner | [site](https://viggle.ai/pricing) | 2026-11-21 |
| **Autodesk Flow Studio (ex-Wonder Studio)** | Motion & 3D | AI motion capture: swaps a filmed actor for a CG character automatically | CG characters in live-action plates | Yes – free plan | $10/mo (₹948) – Lite (third-party snapshot – verify) | Standard ≈$45; Pro ≈$95 (verify – official page hides prices) | Paid plans (verify) | Intermediate | [site](https://www.autodesk.com/products/flow-studio/compare) | 2026-11-21 |
| **Move AI** | Motion & 3D | Markerless motion capture from phone video | Recording body motion for 3D characters | No free plan listed on pricing page | $15/mo (₹1,423) – Move One (iPhone app, 1 person, 60-s captures) | Move Pro / Move Live: custom pricing | Yes (verify) | Intermediate | [site](https://www.move.ai/pricing) | 2026-11-21 |
| **Meshy** | Motion & 3D | Text/image-to-3D models (props, characters) for Blender/Unreal | Fast 3D props and set pieces | Yes – 100 credits/month (outputs CC BY 4.0) | $20/mo (₹1,897) – Pro, 1,000 credits ($240/yr) | Studio $60/mo (₹5,691) | Yes – paid plans; free outputs allowed with attribution | Intermediate | [site](https://www.meshy.ai/pricing) | 2026-11-21 |
| **Blender** | Motion & 3D | Free, open-source 3D software: modelling, animation, rendering, compositing | 3D sets, previs, camera moves | Yes – completely free (GPL) | Free | Free | Yes – what you make is yours | Intermediate | [site](https://www.blender.org/about/license/) | 2026-11-21 |
| **Unreal Engine** | Motion & 3D | Real-time 3D engine used for virtual production and animation | Virtual sets, previs, real-time rendering | Yes – free if your company earns under $1M/year | Free (under $1M annual revenue) | Over $1M revenue: seat licence $1,850/seat/yr | Yes – no royalty on rendered video | Advanced | [site](https://www.unrealengine.com/en-US/license) | 2026-11-21 |
| **Suno** | Music/SFX | Full songs with vocals from a text prompt | Score sketches, songs | Yes – 50 credits/day, no downloads, no commercial | $8/mo (₹759) – Pro, 2,500 credits, 20 downloads/mo (list $10) | Premier $24/mo (₹2,276), 60 downloads | Paid plans, for downloaded songs | Beginner | [site](https://suno.com/pricing) | 2026-11-21 |
| **Udio** | Music/SFX | AI music generation | Experiments only right now | Yes – 10 credits/day | $10/mo (₹948) – Standard (verify) | Pro $30/mo (verify) | Downloads disabled since Feb 2026 (Udio help center) – not usable for film delivery right now | Beginner | [site](https://www.udio.com/pricing) | 2026-11-21 |
| **Soundraw** | Music/SFX | Royalty-free AI background music you can edit by section | Safe background tracks for videos | No free plan (can preview) | $16.99/mo (₹1,612) – Creator, monthly (annual: $11.04/mo) | Artist Pro $35.99/mo (₹3,414) | Yes, all paid plans | Beginner | [site](https://soundraw.io/pricing) | 2026-11-21 |
| **ElevenLabs SFX** | Music/SFX | Text-to-sound-effects inside ElevenLabs | Footsteps, ambiences, whooshes | Yes – inside free ElevenLabs plan | $6/mo (₹569) – Same as ElevenLabs Starter | Same as ElevenLabs plans | Starter and above | Beginner | [site](https://elevenlabs.io/pricing) | 2026-11-21 |
| **AIVA** | Music/SFX | AI composer for orchestral/cinematic scores you can edit | Film-style background score | Yes – but AIVA owns copyright | Standard €11/mo billed yearly (≈€15 monthly) – AIVA still owns copyright | Pro €33/mo billed yearly (≈€49 monthly) – you own copyright | Pro plan for full ownership | Beginner | [site](https://www.aiva.ai/) | 2026-11-21 |
| **Stable Audio** | Music/SFX | Stability AI's music + sound effects generator | Ambiences, SFX, loops | Yes – 50 credits, commercial licence | $12/mo (₹1,138) – Solo | Session $30; Producer $90; Studio $199 | Yes (incl. free tier per pricing page) | Beginner | [site](https://stableaudio.com/pricing) | 2026-11-21 |
| **Epidemic Sound** | Music/SFX | Licensed (human-made) music + SFX library, some AI tools | Safe, cleared music for releases | Free trial (verify) | $9.99/mo (₹948) – Creator (billed yearly) – your own channels | Pro $16.99/mo yearly (client work); Business $30 | Yes – within plan licence | Beginner | [site](https://www.epidemicsound.com/pricing) | 2026-11-21 |
| **Artlist** | Music/SFX | Licensed music, SFX, footage + AI voice/image/video credits | Music + stock in one subscription | No | $9.99/mo (₹948) – Music & SFX Social (billed yearly; $14.99 monthly) | Music & SFX Pro ≈$24.92/mo yearly; Max ≈$39.99 (verify) | Pro plans for client work/ads | Beginner | [site](https://artlist.io/page/pricing) | 2026-11-21 |
| **Topaz Video** | Enhancement | AI upscaling, frame interpolation, denoise (formerly Topaz Video AI) | Upscaling AI clips to 4K, slow-mo | No free plan | $29/mo (₹2,751) – Topaz Video (web), 200 cloud credits; or $299/yr. Desktop app $59/mo ($39/mo annual) | Topaz Studio $79/mo or $499/yr; Studio Pro $799/yr (Black Friday promos running) | Studio: limited (orgs under $1M revenue); Studio Pro: full | Intermediate | [site](https://www.topazlabs.com/pricing) | 2026-11-21 |
| **DaVinci Resolve** | Editing/post | Full editor + color + audio (Fairlight) + VFX (Fusion) | Everything in post; pro color | Yes – very complete free version | Studio: $295 one-time (₹27,981); seen at $236 on sale | Same – one-time | Yes | Beginner→Advanced | [site](https://www.blackmagicdesign.com/products/davinciresolve) | 2026-11-21 |
| **Adobe Premiere Pro** | Editing/post | Industry-standard editor; Firefly generative extend | Agency/industry workflows | 7-day trial | $22.99/mo (₹2,181) – Annual plan billed monthly (month-to-month costs more) | Creative Cloud Pro (all apps) – verify | Yes | Intermediate | [site](https://www.adobe.com/products/premiere/plans.html) | 2026-11-21 |
| **CapCut** | Editing/post | Easy editor with templates, auto-captions, AI tools | Shorts, Reels, quick edits | Yes – free tier | $9.99/mo (₹948) – Standard (Pro is $19.99/mo or $179.99/yr; lower regional prices) | Pro $19.99/mo (₹1,896) | Check template/music licences | Beginner | [site](https://www.capcut.com/pricing) | 2026-11-21 |
| **Descript** | Editing/post | Edit video by editing the transcript; Studio Sound; AI voices | Dialogue edits, podcasts, rough cuts | Yes – 60 media minutes/mo | $24/mo (₹2,276) – Hobbyist (annual: $16/mo) | Creator $35/mo (₹3,320) (annual $24) | Yes | Beginner | [site](https://www.descript.com/pricing) | 2026-11-21 |
| **OpusClip** | Editing/post | AI cuts long videos into captioned vertical short clips | Trailers/teasers and social cut-downs | Yes – 60 credits/month, watermark, clips expire after 3 days | $15/mo (₹1,423) – Starter, 150 credits (monthly only) | Pro $29/mo (₹2,751) ($14.50/mo yearly) | Paid plans | Beginner | [site](https://www.opus.pro/pricing) | 2026-11-21 |
| **Adobe Podcast Enhance Speech** | Editing/post | One-click AI cleanup of noisy dialogue recordings | Rescuing bad voice/dialogue audio | Yes – 1 hr/day, files up to 30 min | Premium now sold via Firefly plans (verify price) | Firefly Pro (verify) | Yes | Beginner | [site](https://podcast.adobe.com/en/plans) | 2026-11-21 |
| **ComfyUI** | Open-source/local | Node-based app to run image/video models locally or in the cloud | Full control, custom pipelines | Free (GPL-3.0) | Free – hardware or cloud GPU cost only | Free | Yes (model licences vary) | Intermediate→Advanced | [site](https://github.com/Comfy-Org/ComfyUI) | 2026-11-21 |
| **Stable Diffusion (Stability AI)** | Open-source/local | Open image models (SD 3.5 etc.) for local use | Local image gen, LoRA training | Free weights | Free under Community Licence if your org earns <$1M/yr | Enterprise licence above $1M revenue | Yes under $1M revenue | Intermediate | [site](https://stability.ai/license) | 2026-11-21 |
| **Wan 2.2 (Alibaba)** | Open-source/local | Open video models (5B and 14B) for text/image-to-video | Local video gen in ComfyUI | Free (Apache-2.0) | Free – GPU: 5B ≈8 GB with ComfyUI offloading; 14B needs 16–24 GB quantized (80 GB unquantized) | Free | Yes (Apache-2.0) | Advanced | [site](https://github.com/Wan-Video/Wan2.2) | 2026-11-21 |
| **LTX Video (Lightricks)** | Open-source/local | Open video+audio models (LTX-2 / LTX-2.5) | Fast local video with sound | Free weights (community licence) | Free – GPU: 8 GB possible with quantization + 64 GB RAM; 24–32 GB for quality | Commercial licence terms at ltx.io | Check LTX community licence | Advanced | [site](https://github.com/Lightricks/LTX-Video) | 2026-11-21 |
| **invideo AI** | Aggregator | Prompt-to-full-video with stock, avatars and many generative models | Faceless/explainer videos | Not listed on pricing page (verify) | $10/mo (₹948) – Starter, billed annually (~$20 monthly), 400 credits | Plus $30/mo annual (₹2,846), 2,000 credits | Paid plans | Beginner | [site](https://invideo.io/pricing) | 2026-11-21 |
| **Magnific (formerly Freepik)** | Aggregator | Stock library + AI suite with many image/video models | One subscription, many models | Yes – limited | $20/mo (₹1,897) – Premium, 240K credits/yr (annual: $14.50/mo) | Plus $45/mo (₹4,268); Pro $110/mo | Paid plans | Beginner | [site](https://www.magnific.com/pricing) | 2026-11-21 |
| **Krea** | Aggregator | Real-time image gen, video, upscaling, many models in one place | Fast look-dev, upscaling | Yes – 100 compute units/day | $9/mo (₹854) – Basic list price; heavy promos shown (page showed $5) – verify at checkout | Pro ≈$35–42/mo list, $21/mo on promo (verify) | Paid plans | Beginner | [site](https://www.krea.ai/pricing) | 2026-11-21 |
| **Runway API** | API/infrastructure | Developer API for Runway and partner models | Batch generation from code | No free tier ($10 minimum top-up – verify) | $0.01 per credit: Gen-4 Turbo $0.05/s, Gen-4.5 $0.12/s | Pay per use | Yes | Advanced | [site](https://docs.dev.runwayml.com/guides/pricing/) | 2026-11-21 |
| **fal.ai** | API/infrastructure | Pay-per-use API for 600+ image/video/audio models | Cheapest API access to many models | Free starter credits sometimes (verify) | e.g. Wan 2.5 $0.05/s; Kling 2.5 Turbo Pro $0.07/s | Pay per use | Depends on model | Advanced | [site](https://fal.ai/pricing) | 2026-11-21 |
| **Replicate** | API/infrastructure | Run open and proprietary models via API | Easy async API, many models | No (pay as you go) | e.g. Kling v2.0 $0.28 per output second | Pay per use | Depends on model | Advanced | [site](https://replicate.com/docs) | 2026-11-21 |
| **Gemini API / Vertex AI (Veo)** | API/infrastructure | Google's API for Veo video and Nano Banana images | Veo from code | Not on free tier | Veo 3.1 Lite $0.05/s (720p); Fast $0.10/s; Standard $0.40/s | Pay per use | Yes (verify terms) | Advanced | [site](https://ai.google.dev/gemini-api/docs/pricing) | 2026-11-21 |
| **RunPod** | API/infrastructure | Rent cloud GPUs by the second | Running ComfyUI/Wan without your own GPU | No | RTX 4090 from $0.34/hr (Community) / $0.69/hr (Secure); A100 80GB from $1.19/hr | Pay per use | Yes | Advanced | [site](https://www.runpod.io/pricing) | 2026-11-21 |
| **Google Colab** | API/infrastructure | Browser Python notebooks with GPUs | Learning Python, small experiments | Yes – free T4 GPU when available | $9.99/mo (₹948) – Colab Pro, 100 compute units | Pro+ $49.99/mo (₹4,741) | Yes | Intermediate | [site](https://colab.research.google.com/) | 2026-11-21 |

## Which tool for which job (short version)

| Job | Start free with | Upgrade to |
|---|---|---|
| Write the script and shot list | Claude, ChatGPT or Gemini free plans | Claude Pro / ChatGPT Plus / Google AI Pro ($20/mo) |
| Design characters and locations | Gemini app (Nano Banana), ChatGPT images | Midjourney Basic ($10) or Nano Banana via API |
| Turn images into moving shots | Google Flow free credits, Kling free credits | Kling Standard ($10), Runway Standard ($15), Google AI Pro ($19.99) |
| Voices | ElevenLabs free (non-commercial) | ElevenLabs Starter ($6) — adds commercial licence |
| Lip-sync talking characters | HeyGen free (watermarked), Kling/Flow lip-sync features | HeyGen Creator ($29) |
| Music | Suno free (no downloads now), royalty-free libraries | Suno Pro ($8), Soundraw Creator ($16.99) |
| Sound effects | ElevenLabs SFX (free tier) | ElevenLabs Starter |
| Edit, color, mix | DaVinci Resolve (free) | DaVinci Resolve Studio ($295 one-time) |
| Upscale to 4K / smooth motion | DaVinci free tools, Krea free upscale | Topaz Video ($29/mo or $299/yr) |
| Storyboard before generating | Boords free (3 scripts), pen and paper | Boords Solo ($39) |
| Screenplay formatting | WriterDuet free tier | Final Draft 13 ($249.99 one-time) |
| Talking character from one photo | HeyGen free (watermark), Kling/Flow features | Hedra Basic ($20) |
| Re-sync lips to new dialogue | Kling/Flow built-in lip-sync | sync.so Hobbyist ($5 + per-second usage) |
| Copy a real movement onto a character | Viggle free (daily credits, watermark) | Viggle Pro ($7.99) |
| CG characters, 3D sets, previs | Blender (free), Unreal Engine (free) | Meshy Pro ($20), Flow Studio (verify) |
| Text on screen (titles, signs) | Ideogram free | Ideogram Plus ($20) |
| Cinematic orchestral score | AIVA free (AIVA owns it) | AIVA Pro (€33/mo yearly – you own copyright) |
| Fully licensed music for release | YouTube Audio Library | Epidemic Sound ($9.99 yearly) / Artlist ($9.99 yearly) |
| Clean up noisy dialogue | Adobe Podcast Enhance (1 hr/day free) | DaVinci Resolve Studio voice isolation |
| Trailer/teaser cut-downs | CapCut, OpusClip free | OpusClip Starter ($15) |
| Run open models yourself | ComfyUI + Wan 2.2 5B or LTX on your own GPU, Google Colab free | RunPod GPU rental (~$0.34–$0.69/hr for an RTX 4090) |

## Three budget stacks

All monthly totals use the **cheapest monthly price** listed above (not annual). INR at ₹94.85/USD.

### 1. Free stack — $0 / ₹0 per month

| Job | Tool | Notes |
|---|---|---|
| Script & shot list | Claude / ChatGPT / Gemini free | Daily message limits |
| Images & characters | Gemini app (Nano Banana), ChatGPT free images | Limited per day |
| Video | Google Flow free credits (100/month) + Kling free daily credits + Hailuo trial | Watermarks, short clips, slow queues |
| Voice & SFX | ElevenLabs free (10,000 credits) | No commercial licence; attribution required |
| Music | Royalty-free libraries (e.g. YouTube Audio Library, sign-in needed) | Suno free has no downloads now |
| Edit / color / sound | DaVinci Resolve free, CapCut free | Resolve free is a full professional editor |
| Storyboard / 3D (optional) | Boords free, Blender | Plan shots before spending credits |
| Local generation (optional) | ComfyUI + Wan 2.2 5B or LTX-Video | Needs an NVIDIA GPU (8 GB workable with offloading) |

**What you can realistically make:** a 30–90 second proof-of-concept short or a mood trailer: 10–20 generated shots, a narrated voice, simple music, edited in Resolve. Expect watermarks on some clips and **no commercial rights**. Perfect for learning, a portfolio piece, and festival "AI category" experiments where rules allow.

### 2. Starter stack — about $44/month (₹4,172)

| Tool | Plan | USD/mo | INR/mo |
|---|---|---|---|
| Google AI Pro | Gemini + Flow (1,000 credits) + Nano Banana | $19.99 | ₹1,896 |
| Kling AI | Standard (660 credits) | $10.00 | ₹949 |
| ElevenLabs | Starter (commercial licence) | $6.00 | ₹569 |
| Suno | Pro (20 downloads, commercial) | $8.00 | ₹759 |
| DaVinci Resolve | Free | $0 | ₹0 |
| **Total** | | **$43.99** | **₹4,172** |

Swap options inside the same budget: Runway Standard ($15) instead of Kling; Midjourney Basic ($10) for stronger stills; Claude Pro ($20) instead of Google AI Pro if you mainly need writing help (then use Kling for all video).

**What you can make:** a polished 2–4 minute short with consistent characters, clean voices, licensed music, and no watermarks — enough for festivals, a portfolio, and small paid jobs.

### 3. Pro stack — about $197/month (₹18,685)

| Tool | Plan | USD/mo | INR/mo |
|---|---|---|---|
| Claude | Pro (writing, planning, coding help) | $20 | ₹1,897 |
| Midjourney | Standard (unlimited Relax images) | $30 | ₹2,846 |
| Runway | Pro (2,250 credits) | $35 | ₹3,320 |
| Kling AI | Pro (3,000 credits) | $37 | ₹3,509 |
| ElevenLabs | Creator (professional voice cloning) | $22 | ₹2,087 |
| Suno | Premier (60 downloads) | $24 | ₹2,276 |
| Topaz Video | Video (web) monthly; $299/yr if paid annually | $29 | ₹2,751 |
| **Total** | | **$197** | **₹18,685** |

Add **DaVinci Resolve Studio** ($295 one-time, ₹27,981) when you need its extra AI tools, noise reduction and higher resolutions. Many pros also add **API pay-as-you-go** (fal.ai / Runway API / Gemini API) for batch work — budget $20–$50/month to start.

**What you can make:** 5–15 minute narrative shorts, music videos and client ads at 4K, with multiple models for different shot types.

## One-time costs (hardware)

GPU prices are unusually high in late 2026. These are **US** figures; Indian prices differ — check locally.

| Item | What you need | Price snapshot (checked 2026-11-21) |
|---|---|---|
| Computer for **cloud-only** AI filmmaking | Any recent laptop/desktop with 16 GB RAM, SSD, decent screen. All generation happens in the browser. | Use what you have; Resolve wants a GPU for smooth playback |
| GPU for **local** AI video (ComfyUI, Wan, LTX) | NVIDIA card. 8 GB = small models with offloading; **16 GB = workable**; **24–32 GB = comfortable** | RTX 5060 Ti 16GB: MSRP $429 (₹40,691) but selling ~$650–$800 (₹61,652–₹75,880). RTX 5070 Ti: MSRP $749, street ~$1,030–$1,400. RTX 5090 (32 GB): MSRP $1,999 (₹189,605), partner cards seen at $3,340+ |
| System RAM & storage | 32 GB RAM (64 GB if you offload big models), 1–2 TB NVMe SSD (video models are 10–30 GB each) | Check local prices |
| Microphone (scratch voice, ADR, VO) | USB condenser or dynamic mic | FIFINE K669B ≈ $30 (₹2,846); RØDE NT-USB Mini ≈ $89–$99 (₹8,442–₹9,390) |
| Phone or camera | Any modern phone shooting 1080p/4K is enough for reference footage, motion reference and hybrid shots | $0 if you use your own phone |
| Headphones | Closed-back headphones for mixing | Check local prices |

**No GPU?** Rent one. An RTX 4090 on RunPod Community Cloud is about **$0.34/hour** (₹32); a 30-hour month is roughly **$10** (₹967). Google Colab has a free tier and Pro at $9.99/month.

## How AI helps you choose

Ask Claude/ChatGPT: *"I have ₹5,000/month and want to make a 3-minute sci-fi short with two consistent characters and dialogue. Using the tools in this CSV [paste], propose a stack, a credit budget per shot, and where I'll run out first."* Then sanity-check its maths.

## Sources for this page

All official pricing links are in the table. Secondary, dated snapshots used where official pages did not show numbers: Kling (Zemith, checked 12 Nov 2026), Hailuo (Zemith/WaveSpeed, Nov 2026), Boords (Gappsy, 26 Oct 2026), OpusClip (Castmagic/eesel, 2026), Artlist (cchound, May 2026), Higgsfield (Higgsfield's own blog, Oct 2026), GPU prices (Tom's Hardware / PC Gamer / TechSpot, Nov 2026), microphones (fone.tips, gilricardo.com, 2026). See the full list in [`data/resources.csv`](../data/resources.csv).
