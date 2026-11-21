# AI Video Prompt Library (35 prompts)

Copy, paste, and replace the `[BRACKETS]`. Each prompt has a short **why it works** note so you learn the pattern, not just the words. Prompts are model-agnostic; tweak for each tool (some ignore negative prompts, some prefer shorter prompts).

**Golden rules:** one action per shot · camera info early · describe *visible* things · reuse the same character and style bible text in every prompt · prompt only the **motion** when doing image-to-video.

**Reusable blocks** (paste into any image/video prompt):

```
STYLE BIBLE: [e.g. 1970s sci-fi realism, practical lighting, muted teal and amber palette, 35mm film grain, anamorphic lens flares, 2.39:1]
CHARACTER BIBLE – [NAME]: [age, build, face shape, skin tone, hair, eyes, signature clothing, one distinctive detail]
```

---

## 1. Script and story

**1 · Logline brainstorm**
```
Act as a story editor. Generate 15 loglines for a [GENRE] short film (2–4 minutes) about [THEME].
Each must name a specific flawed protagonist, a concrete goal, an obstacle, and stakes.
Constraints: max 2 characters, max 2 locations, little or no lip-synced dialogue.
Make 5 of them unexpected or genre-mixing. Number them; no explanations.
```
*Why it works:* the formula and constraints force usable, AI-friendly ideas; asking for "unexpected" fights generic output.

**2 · Logline critic**
```
Here is my logline: "[LOGLINE]".
Critique it as a festival programmer. What is unclear, clichéd, or low-stakes?
Ask me 3 questions that would sharpen it. Do NOT rewrite it for me.
```
*Why it works:* keeps you as the author (good for craft and copyright) while getting sharp feedback.

**3 · Beat outline**
```
Turn this logline into a 5-beat outline for a [LENGTH]-minute short:
1 Hook, 2 Inciting incident, 3 Escalation, 4 Climax/turn, 5 Resolution image.
For each beat give one visual action we can SEE, approx. duration in seconds, and the emotion.
Logline: "[LOGLINE]"
```
*Why it works:* visual actions + durations translate directly into shots.

**4 · Script page to shot list (CSV)**
```
Convert this scene into a shot list as CSV with columns:
shot_id,scene,shot_size,angle,lens_mm,camera_movement,action,dialogue_or_vo,duration_s,notes
Rules: one visible action per shot; 3–8 seconds each; use standard shot sizes (EWS, WS, MS, MCU, CU, ECU);
prefer over-the-shoulder or off-screen angles for long dialogue. Output only the CSV.
Scene: [PASTE SCENE]
```
*Why it works:* a strict schema gives you a file your scripts and spreadsheets can use immediately.

**5 · Dialogue punch-up with subtext**
```
Rewrite these lines so characters never state their feelings directly; reveal them through
action, evasion, and subtext. Keep each line under 12 words. Mark one physical action per line.
[PASTE DIALOGUE]
```
*Why it works:* short lines are easier to lip-sync; subtext makes AI scenes feel human.

**6 · Show-don't-tell converter**
```
For each line below, replace internal feelings with one filmable action or micro-expression.
Format: original → filmable version.
[PASTE ACTION LINES]
```
*Why it works:* models can only render what's visible.

---

## 2. Character reference sheets

**7 · Turnaround sheet**
```
Character reference sheet of [CHARACTER BIBLE]. Full-body turnaround: front view, three-quarter view,
side profile, back view, evenly spaced on a plain light-grey background. Neutral standing pose,
consistent proportions, flat even studio lighting, no shadows on background, clean concept-art style,
labelled views. No text other than labels.
```
*Why it works:* plain background + even light gives a clean reference for image-to-video and ingredient features.

**8 · Expression sheet**
```
Expression sheet of [CHARACTER BIBLE]: 3x3 grid of head-and-shoulders close-ups showing neutral, happy,
sad, angry, afraid, surprised, suspicious, exhausted, determined. Same face, same hair, same lighting,
plain background, consistent camera height, photoreal.
```
*Why it works:* locks the face across emotions you'll need later.

**9 · Costume & prop detail sheet**
```
Costume and prop detail sheet for [CHARACTER NAME]: close-ups of [JACKET], [SHOES], [ACCESSORY], and
[KEY PROP], each in its own panel, plain background, product-photo lighting, matching colours and
materials to: [CHARACTER BIBLE].
```
*Why it works:* small details (buttons, logos, wear) are where consistency usually breaks.

**10 · Character in context test**
```
[CHARACTER BIBLE], standing in [LOCATION], [LIGHTING]. Medium shot, 50mm lens, eye level.
Match the attached reference sheet exactly: same face, hairstyle, outfit, and colours. [STYLE BIBLE]
```
*Why it works:* tests whether identity survives new lighting before you commit to a sequence.

**11 · Location reference sheet**
```
Location design sheet for [LOCATION]: establishing wide shot, reverse angle, close detail of [KEY
FEATURE], and top-down floor plan sketch. Same time of day, same weather, consistent architecture.
[STYLE BIBLE]
```
*Why it works:* gives you coverage angles and a plan for blocking and the 180° rule.

---

## 3. Cinematic shots

**12 · Establishing shot**
```
Extreme wide establishing shot, [LOCATION] at [TIME OF DAY], [WEATHER]. A tiny figure of [CHARACTER]
in the lower third for scale. 24mm lens, deep focus, [LIGHTING]. Slow push-in. [STYLE BIBLE]
Negative: text, watermark, distorted architecture.
```
*Why it works:* scale figure + lower-third placement tells the audience where and who in one image.

**13 · Dialogue — over-the-shoulder**
```
Over-the-shoulder medium close-up from behind [CHARACTER A]'s left shoulder (soft, out of focus),
looking at [CHARACTER B] who [ACTION WHILE SPEAKING]. 85mm lens, shallow depth of field, motivated
window light from the right, static camera. [STYLE BIBLE]
```
*Why it works:* OTS hides one mouth (less lip-sync risk) and keeps eye-lines consistent.

**14 · Dialogue — clean single (reverse)**
```
Medium close-up of [CHARACTER A], eyes looking slightly camera-left, [MICRO-EXPRESSION], listening.
85mm lens, same window light as previous shot now from the left, background softly blurred. Static.
```
*Why it works:* matching light direction and eye-line makes shot/reverse-shot cut cleanly.

**15 · Action — chase**
```
Low-angle tracking shot running alongside [CHARACTER] sprinting through [LOCATION], debris flying,
motion blur on background, handheld energy, 28mm lens, fast shutter feel, harsh [LIGHT]. 5 seconds.
Negative: slow motion, floating movement.
```
*Why it works:* explicit speed words + "no slow motion" counter the floaty default of many models.

**16 · Action — impact moment**
```
Medium shot, [CHARACTER] catches [OBJECT] mid-air just before it hits the ground, sudden stop,
dust burst, 50mm lens, high contrast side light, quick snap-zoom in at the moment of the catch.
```
*Why it works:* one decisive action with a clear beginning and end is easy for models to animate.

**17 · Emotional close-up**
```
Close-up of [CHARACTER]'s face, [EMOTION SHOWN AS ACTION: e.g. eyes fill with tears, jaw tightens,
she forces a small smile]. 100mm lens, very shallow depth of field, soft key light at 45 degrees,
gentle rim light, slow push-in. Subtle film grain. [STYLE BIBLE]
```
*Why it works:* emotions described as physical changes are renderable; long lens + push-in = intimacy.

**18 · Insert / detail shot**
```
Extreme close-up insert of [CHARACTER]'s hand [ACTION WITH OBJECT], macro lens, shallow focus,
[LIGHT], static camera, 3 seconds.
```
*Why it works:* inserts are cheap, reliable, and perfect for hiding cuts and artefacts.

**19 · Silhouette / mood**
```
Wide shot, [CHARACTER] silhouetted against [BRIGHT BACKGROUND: sunset / neon sign / doorway],
backlit, no fill light, long shadow toward camera, symmetrical composition, static. [STYLE BIBLE]
```
*Why it works:* silhouettes avoid face consistency issues and look instantly cinematic.

**20 · POV shot**
```
First-person POV of [CHARACTER] looking down at [OBJECT/SCENE] in their hands, slight handheld sway,
24mm lens, natural [LIGHT], their [SLEEVE/GLOVES] visible at frame edges.
```
*Why it works:* POV puts the audience inside the character and needs no face at all.

---

## 4. Camera movements

*Use with image-to-video: describe only motion + camera, not the whole scene again.*

**21 · Dolly in**
```
Slow, smooth dolly in toward [SUBJECT]'s face over 5 seconds, subject stays still except for
[SMALL ACTION], background parallax, no zoom, stable horizon.
```
*Why it works:* "no zoom" and "parallax" make it a physical move, which looks more expensive.

**22 · Dolly out / reveal**
```
Slow dolly out from a close-up of [DETAIL] to reveal [SURPRISING WIDER CONTEXT], steady movement,
5 seconds.
```
*Why it works:* reveals create story beats from a single shot.

**23 · Crane up**
```
Camera cranes up and back from [CHARACTER] at ground level to a high wide view of [LOCATION],
smooth continuous motion, character keeps [ACTION], 6 seconds.
```
*Why it works:* rising camera = ending/isolation/scale; continuous action keeps it alive.

**24 · Crane down / descend**
```
Camera descends from above the [ROOFTOPS/TREES] down to eye level with [CHARACTER], smooth,
ending in a medium shot.
```
*Why it works:* a classic "entering the world" opening move with a clear end frame.

**25 · Handheld**
```
Handheld camera, subtle natural shake, follows [CHARACTER] from behind as they [ACTION] through
[LOCATION], documentary feel, 35mm lens.
```
*Why it works:* "subtle" stops overdone shake; documentary feel adds realism that hides AI polish.

**26 · Orbit / arc**
```
Camera orbits 180 degrees around [CHARACTER] at chest height as they [STAND STILL / TURN HEAD],
constant distance, smooth, background rotates behind them, 6 seconds.
```
*Why it works:* "constant distance" and "chest height" stop the camera drifting or the face morphing.

**27 · Truck / lateral move**
```
Camera trucks left to right alongside [CHARACTER] walking, keeping them centred in a medium shot,
foreground objects pass by for depth.
```
*Why it works:* foreground elements sell real camera motion.

**28 · Whip pan transition**
```
Fast whip pan from [CHARACTER A] to [CHARACTER B / NEW LOCATION] with strong motion blur,
ends sharp and steady on the new subject.
```
*Why it works:* whip pans hide cuts between two generated shots — stitch at the blur.

**29 · Rack focus**
```
Static shot. Focus pulls from [FOREGROUND OBJECT] (sharp) to [CHARACTER] in the background
(becoming sharp) over 3 seconds; foreground blurs.
```
*Why it works:* directs attention without moving the camera — great for reveals.

**30 · Start/end frame controlled move** (for tools that accept two frames)
```
Start frame: [IMAGE A]. End frame: [IMAGE B]. Smooth single camera move connecting them,
no cuts, consistent lighting, [CHARACTER] performs [ACTION] during the move.
```
*Why it works:* two keyframes give the model exact composition at both ends — maximum control.

---

## 5. Music and voice

**31 · Score cue (Suno / music tools)**
```
Instrumental cinematic underscore, [MOOD], [TEMPO] BPM, [INSTRUMENTS: e.g. felt piano, low strings,
soft synth pad], slow build from quiet to a swell at 0:45, no vocals, no drums until the swell,
ends on a sustained chord. Length about 1 minute.
```
*Why it works:* timing landmarks ("swell at 0:45") let you cut picture to music.

**32 · Song for a montage**
```
[GENRE] song, [MOOD], female/male vocals, lyrics about [THEME] without naming real people or brands,
catchy chorus, [TEMPO] BPM, radio-friendly 2-minute structure: intro, verse, chorus, verse, chorus, outro.
```
*Why it works:* explicit structure gives clean edit points; avoiding real names avoids rights issues.

**33 · Narrator voice design (ElevenLabs-style)**
```
Voice: warm, low, slightly raspy [AGE]-year-old narrator, [ACCENT], unhurried, intimate, like
reading a bedtime story to an adult. Pause briefly after each sentence. Script: "[TEXT]"
```
*Why it works:* concrete age, texture, pace and a familiar reference situation produce consistent reads.

**34 · Emotional line delivery**
```
Line: "[DIALOGUE]". Delivery: whispered, holding back tears, voice cracks on the last word,
short breath before speaking. Context: [WHAT JUST HAPPENED].
```
*Why it works:* giving context and physical cues (breath, crack) beats one-word emotion tags.

**35 · Sound effects (ElevenLabs SFX-style)**
```
[SOUND], [ENVIRONMENT], [DISTANCE: close/distant], [DURATION] seconds.
Examples: "Heavy rain on a tin roof with distant thunder, inside a small cabin, 10 seconds."
"Old wooden door slowly creaking open, close-mic, 3 seconds."
```
*Why it works:* source + space + distance + length is how sound designers describe effects.

---

## Bonus: negative prompt starter list
Use only where the model supports negatives:
```
text, subtitles, watermark, logo, extra fingers, deformed hands, morphing face, identity change,
flicker, jitter, slow motion, warped architecture, duplicate people, low resolution, oversharpened
```

## Prompt log template
Keep a CSV log for every generation (the [batch script](../scripts/batch_generate_videos.py) writes one automatically):
`date, shot_id, tool, model, prompt, seed, settings, credits_or_cost, kept(y/n), notes`
