# 02 · Cinematography & Visual Language

## What it is (simply)

**Cinematography** is the art of choosing what the camera sees and how: framing, lens, movement, light and colour. **Visual language** is the shared "grammar" audiences understand without being taught — a close-up feels intimate, a low angle makes someone powerful, cold blue light feels lonely.

Key words defined:
- **Shot size** — how much of the subject fills the frame (extreme wide → wide → medium → close-up → extreme close-up).
- **Focal length** — lens "zoom" in millimetres. 14–24 mm = wide, stretches space; 35–50 mm = natural; 85–135 mm = telephoto, flattens and isolates.
- **Depth of field** — how much is in focus. Shallow = blurry background (bokeh).
- **Key / fill / back light** — the three basic lights: main light, softer light filling shadows, light from behind separating subject from background.
- **Aspect ratio** — frame shape: 16:9 (TV/YouTube), 2.39:1 (cinema widescreen), 9:16 (phones).

## Why it matters for AI filmmaking specifically

- **Image and video models were trained on captioned photos and film stills.** Camera vocabulary ("85mm lens, shallow depth of field, rim light, low angle") is the most reliable way to control them. People who know the words get better results faster.
- **Consistency across shots** — a film needs lighting and colour that match from shot to shot. Without a visual plan, AI clips look like a random playlist.
- **Camera motion is now promptable** (dolly in, crane up, orbit). Knowing *why* you'd use each move keeps you from overusing flashy motion.

## Core concepts

**Beginner**
- Shot sizes and what each communicates.
- Rule of thirds, headroom, lead room, eye-line.
- Camera angles: eye-level, high, low, Dutch tilt, over-the-shoulder, POV.
- Three-point lighting; hard vs soft light; time of day (golden hour, blue hour).
- Basic colour: warm vs cool, complementary palettes.

**Intermediate**
- Lenses and their emotional effect; depth of field as storytelling.
- Camera movement vocabulary: pan, tilt, dolly, truck, crane, handheld, Steadicam, orbit, push-in.
- Coverage: master shot + mediums + close-ups + inserts; the 180° rule and screen direction.
- Motivated lighting (every light should have a believable source).
- Building a **lookbook** (reference frames, palette, lens list).

**Advanced**
- Visual motifs and colour arcs across a film.
- Matching shots across *different* AI models (grain, contrast, colour temperature).
- Simulated film stocks, anamorphic characteristics, lens flares used deliberately.
- Previsualisation: blocking a whole sequence in images before generating any video.
- Hybrid shooting: real footage of actors on a plain background, AI-generated environments (see Curious Refuge's hybrid course below).

## Free resources

| Resource | What you get | Link |
|---|---|---|
| StudioBinder Online Film School | Free cinematography and shot-composition master classes | [studiobinder.com/online-film-school](https://www.studiobinder.com/online-film-school) |
| StudioBinder – Best cinematography online courses | Curated list of free and paid cinematography courses with prices | [studiobinder.com/blog/best-cinematography-online-course](https://www.studiobinder.com/blog/best-cinematography-online-course/) |
| FutureLearn filmmaking collection | Free-to-start courses on production and visual storytelling | [futurelearn.com/courses/collections/filmmaking](https://www.futurelearn.com/courses/collections/filmmaking) |
| Google Flow / Kling free credits | Practise camera-move prompts | see [05 · Tools](05-ai-filmmaking-tools.md) |

## Paid resources

Prices from the StudioBinder list, checked 2026-11-21:

| Resource | Cost | Link |
|---|---|---|
| Cinematography Masterclass (Julian Melanson, Udemy) | $94.99 one-time (Udemy prices vary with sales) | via [StudioBinder's list](https://www.studiobinder.com/blog/best-cinematography-online-course/) |
| Cinematography Basics: Lighting (Zak Mulligan, Skillshare) | ~$18/month, 7-day free trial | via StudioBinder's list |
| Become a Cinematographer (LinkedIn Learning) | ~$19.99/month | via StudioBinder's list |
| Curious Refuge – Hybrid AI Filmmaking | $749 single course | [curiousrefuge.com/hybrid-ai-filmmaking](https://curiousrefuge.com/hybrid-ai-filmmaking) |
| Midjourney Basic (for lookbooks) | $10/month | [Midjourney plans](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans) |

## Hands-on exercise: "One moment, six ways"

Take one moment from your script (e.g. *a woman finds a letter*). Generate it as **six frames** with the same character and setting, changing one variable at a time:

1. Extreme wide, eye level, 24 mm, daylight.
2. Medium, eye level, 50 mm.
3. Close-up, 85 mm, shallow depth of field.
4. Extreme close-up on the letter, insert shot.
5. Low angle, hard side light, night.
6. High angle, cool blue palette, rain on window.

Put them side by side and write one sentence per frame on **how it changes the feeling**.

**Done when:** you can predict the emotional effect *before* generating.

## How AI helps at this stage

- **Instant previs:** storyboards and lookbooks in hours instead of days.
- **Learning by contrast:** generate the same shot with 24 mm vs 85 mm to *see* the difference.
- **Reference analysis:** upload a film still you love and ask "describe the lighting setup, lens and colour palette so I can recreate the *technique*" (do not copy protected characters or exact frames — see [08](08-legal-ethics-copyright.md)).
- **Style references** in Midjourney or image-to-image tools keep a whole sequence in one look.
- **Watch out for:** models ignoring lens/angle words when the prompt is long. Put camera info early and keep it short.

Prompts for this stage: [cinematic shots](../prompts/ai-video-prompt-library.md#3-cinematic-shots) and [camera movements](../prompts/ai-video-prompt-library.md#4-camera-movements).
