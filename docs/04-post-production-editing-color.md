# 04 · Post-Production: Editing & Colour

## What it is (simply)

**Post-production** is everything after the footage exists: **editing** (choosing and ordering shots so the story flows), **colour** (making shots match and setting the mood), **sound mixing**, **visual effects**, titles, and **delivery** (exporting the right file for each platform). Editors often say the film is "rewritten" in the edit.

Key words defined:
- **Timeline** — where clips are arranged in order in an editing app.
- **Cut** — the change from one shot to the next. **J-cut / L-cut** — audio from the next/previous shot overlaps the picture change.
- **Colour correction** — fixing exposure and white balance so shots look natural and consistent. **Colour grading** — the creative look on top (teal-orange, desaturated, warm nostalgia).
- **LUT** — "look-up table", a preset that converts colours (e.g. from flat camera footage to a standard look).
- **Codec / container** — how video is compressed (H.264, H.265, ProRes) and wrapped (.mp4, .mov).
- **Upscaling** — increasing resolution (e.g. 720p → 4K) with AI. **Frame interpolation** — creating in-between frames for smoother or slow motion.

## Why it matters for AI filmmaking specifically

- **AI clips are raw material, not finished shots.** Most need trimming (models often wobble at the first and last frames), speed changes, stabilising, and grading.
- **Different models = different colours.** A Kling shot, a Runway shot and a Flow shot side by side look like three films until you grade them to match.
- **Editing hides artefacts.** Cutting away just before a hand distorts, or covering a glitch with a reaction shot, is a core AI editing skill.
- **Delivery specs matter** for festivals and clients (resolution, frame rate, loudness, captions).

## Core concepts

**Beginner**
- DaVinci Resolve interface: Media, Cut, Edit, Fusion, Color, Fairlight, Deliver pages.
- Organising media with bins and naming conventions.
- Basic cuts, trims, transitions (use sparingly), titles.
- Matching frame rate (24 fps for a cinematic feel) and resolution across clips.
- Exporting H.264 MP4 for the web.

**Intermediate**
- Pacing and rhythm; cutting on action; cutting on emotion.
- J/L cuts, sound bridges, montage.
- Colour correction with scopes (waveform, vectorscope) — numbers, not just eyes.
- Shot matching across AI models; adding consistent film grain to unify.
- Speed ramps, stabilisation, reframing for 9:16 vertical versions.

**Advanced**
- Node-based grading in Resolve; power windows and tracking; skin-tone protection.
- Compositing in Fusion: sky replacement, adding generated elements over real footage.
- AI upscaling (Topaz, Resolve Studio Super Scale) and interpolation in a proper order (see [06](06-ai-engineer-technical-skills.md#8-upscaling-frame-interpolation-and-colour-pipelines)).
- Mastering: loudness, captions (SRT), deliverables list, archiving the project.

## Free resources

| Resource | What you get | Link |
|---|---|---|
| DaVinci Resolve official training | Free video courses for Edit, Color, Fairlight and Fusion pages + training books (*Beginner's Guide*, *Editor's Guide*, *Colorist Guide* to DaVinci Resolve 20) with lesson files | [blackmagicdesign.com/products/davinciresolve/training](https://www.blackmagicdesign.com/products/davinciresolve/training) |
| DaVinci Resolve (free version) | Full professional editor/colour/audio/VFX app | [blackmagicdesign.com/products/davinciresolve](https://www.blackmagicdesign.com/products/davinciresolve) |
| StudioBinder Online Film School | Free editing and post-production classes | [studiobinder.com/online-film-school](https://www.studiobinder.com/online-film-school) |
| CapCut free | Fast vertical edits and auto-captions | [capcut.com/pricing](https://www.capcut.com/pricing) |
| FFmpeg documentation | Free command-line video tool for conversions and batch work | [ffmpeg.org/documentation.html](https://ffmpeg.org/documentation.html) |

## Paid resources

| Resource | Cost (checked 2026-11-21) | Link |
|---|---|---|
| DaVinci Resolve Studio | $295 one-time (seen at $236 on sale) | [blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve) |
| Adobe Premiere Pro | $22.99/month (annual plan billed monthly) | [adobe.com/products/premiere/plans](https://www.adobe.com/products/premiere/plans.html) |
| Descript Hobbyist | $24/month ($16 annual) | [descript.com/pricing](https://www.descript.com/pricing) |
| Topaz Video | $29/month or $299/year (web); desktop $59/month | [topazlabs.com/pricing](https://www.topazlabs.com/pricing) |
| DaVinci Resolve training books (print) | Varies on Amazon; PDFs listed on the training page | [training page](https://www.blackmagicdesign.com/products/davinciresolve/training) |

## Hands-on exercise: "Same footage, two films"

1. Generate or collect 12–15 clips for one short scene (include 2–3 "spare" reaction/insert shots).
2. Cut **Version A as a thriller**: short shots, tension, cold grade, low music.
3. Cut **Version B as a comedy or romance**: longer holds, warmer grade, different music.
4. Match colour across all clips in each version using scopes.
5. Export both as 1080p H.264 MP4 and a 9:16 vertical teaser.

**Done when:** viewers correctly guess the genre of each version without being told.

## How AI helps at this stage

- **Rough cuts from transcripts** (Descript, Resolve's AI tools) — edit dialogue by editing text.
- **Auto-captions** in Resolve/CapCut/Descript.
- **Audio clean-up** (Descript Studio Sound, Resolve voice isolation in Studio).
- **Upscaling and interpolation** with Topaz or Resolve Studio.
- **Generative extend / fill** to add a few frames to a clip that ends too early.
- **Edit notes:** export a frame-by-frame list or describe your cut and ask an assistant "where is the pacing slow?"
- **Watch out for:** over-processing (plastic skin from heavy upscaling), inconsistent grain, and transitions used to hide weak cuts.
