# 03 · Production, Directing & Sound

## What it is (simply)

**Production** is the stage where the film actually gets made — traditionally the shoot; in AI filmmaking, the generation sessions. **Directing** is making decisions about performance, staging (who stands where and moves how — called **blocking**), and rhythm so every shot serves the story. **Sound** is everything the audience hears: dialogue, ambience, sound effects (SFX), music. Audiences forgive mediocre images far more easily than bad sound.

Key words defined:
- **Blocking** — positions and movements of characters and camera in a scene.
- **Coverage** — the set of shots that lets an editor build a scene.
- **Room tone / ambience** — the background sound of a place. Silence in a film is never truly silent.
- **Foley** — everyday sounds (footsteps, cloth, cups) recreated and synced to picture.
- **ADR** — re-recording dialogue after the shoot.
- **Diegetic sound** — sound that exists in the story world (a radio playing); **non-diegetic** — sound only the audience hears (the score).

## Why it matters for AI filmmaking specifically

- **AI "actors" need directing too.** Models default to generic expressions and floaty motion. You direct with precise action verbs, timing, and micro-expressions ("her jaw tightens, she looks away, then back").
- **Production management = credit management.** Every take costs credits. Directors who plan shots tightly finish films; those who "just try things" run out of budget.
- **Sound hides AI flaws.** Strong ambience, foley and music make slightly imperfect visuals feel real. Many AI shorts fail purely on sound.
- **Voice tools raise consent questions.** Cloning a real person's voice without permission is an ethical and legal problem (see [08](08-legal-ethics-copyright.md)).

## Core concepts

**Beginner**
- Pre-production checklist: script, shot list, lookbook, character sheets, schedule, budget.
- Directing with verbs: what the character *does*, not what they "feel".
- The 180° rule and eye-lines so cuts make sense.
- The four sound layers: dialogue, ambience, SFX, music.
- Recording clean scratch voice with a phone or USB mic in a soft room (closet with clothes).

**Intermediate**
- Blocking a scene as a top-down diagram before generating.
- Performance continuity across shots (same emotion level, same props, same wardrobe).
- Voice design: casting AI voices, emotion tags, pacing, breaths.
- Sound design: building a soundscape from layers; using SFX generators.
- Music: temp tracks vs licensed or generated scores; spotting (deciding where music starts/stops).

**Advanced**
- Running a "generation day" like a shoot: call sheet of shots, credit budget per shot, take log.
- Hybrid production: directing real actors for motion/performance reference, then restyling.
- Lip-sync workflows and dialogue scene construction (shot/reverse-shot with consistent voices).
- Mixing basics: levels (dialogue around −12 to −6 dBFS peaks is a common starting point), EQ, compression, loudness targets for platforms (check each platform's spec).

## Free resources

| Resource | What you get | Link |
|---|---|---|
| StudioBinder Online Film School | Free classes on directing, blocking and production planning | [studiobinder.com/online-film-school](https://www.studiobinder.com/online-film-school) |
| FutureLearn filmmaking collection | Free-to-start courses incl. production, from BFI/NFTS/The Production Guild | [futurelearn.com/courses/collections/filmmaking](https://www.futurelearn.com/courses/collections/filmmaking) |
| DaVinci Resolve training – *The Fairlight Audio Guide* | Official free video lessons + training book for audio in Resolve | [blackmagicdesign.com/products/davinciresolve/training](https://www.blackmagicdesign.com/products/davinciresolve/training) |
| ElevenLabs free plan | 10,000 credits/month for voices and SFX (non-commercial) | [elevenlabs.io/pricing](https://elevenlabs.io/pricing) |

## Paid resources

| Resource | Cost (checked 2026-11-21) | Link |
|---|---|---|
| ElevenLabs Starter / Creator | $6 / $22 per month | [elevenlabs.io/pricing](https://elevenlabs.io/pricing) |
| HeyGen Creator (lip-sync, avatars) | $29/month | [heygen.com/pricing](https://www.heygen.com/pricing) |
| Suno Pro (music) | $8/month (list $10) | [suno.com/pricing](https://suno.com/pricing) |
| Soundraw Creator (royalty-free BGM) | $16.99/month | [soundraw.io/pricing](https://soundraw.io/pricing) |
| USB microphone | ~$30 (FIFINE K669B) to ~$99 (RØDE NT-USB Mini) | see [05 · Tools](05-ai-filmmaking-tools.md#one-time-costs-hardware) |

## Hands-on exercise: "Sound first"

1. Take a 30-second scene from your shot list.
2. **Before generating any video**, build the soundtrack: record or generate the dialogue/voice-over, add room tone, 5+ SFX, and a music bed.
3. Now generate the visuals *to fit the sound* (timing each shot to the audio beats).
4. Edit in DaVinci Resolve. Then mute the audio and watch — notice how much weaker it feels.

**Done when:** a friend watching with eyes closed can describe where the scene takes place and what happens.

## How AI helps at this stage

- **Production planning:** generate call sheets, credit budgets and take logs from your shot list.
- **Performance prompts:** turn "she's sad" into concrete, filmable actions.
- **Voices:** text-to-speech for narration, dialogue drafts and temp tracks; voice cloning only with written consent.
- **SFX on demand:** "rain on a tin roof, distant thunder, 10 seconds" via ElevenLabs SFX.
- **Music sketches:** Suno for temp score ideas; Soundraw for safe background music.
- **Lip-sync:** HeyGen or the lip-sync features in Kling/Runway/Flow for talking shots.
- **Watch out for:** robotic emotional delivery — regenerate lines with emotion tags or record a scratch performance yourself and use voice conversion.

Prompts: [music and voice prompts](../prompts/ai-video-prompt-library.md#5-music-and-voice).
