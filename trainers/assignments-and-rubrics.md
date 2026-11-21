# Assignments & Grading Rubrics

Five assignments plus a final project. All rubrics use the same five criteria from the course brief — **Story, Visuals, Consistency, Sound, Edit** — scored 1–4, plus assignment-specific criteria where relevant.

**Score levels:** 4 = Excellent · 3 = Proficient · 2 = Developing · 1 = Beginning

## Universal rubric (use for any film-based submission)

| Criterion | 4 – Excellent | 3 – Proficient | 2 – Developing | 1 – Beginning |
|---|---|---|---|---|
| **Story** | Clear character, goal and change; every shot serves the story; surprising or moving | Clear story with a minor unclear beat | Story present but confusing or flat | No discernible story |
| **Visuals** | Deliberate shot sizes, lenses, light and colour that create mood; strong composition | Mostly intentional choices; a few generic shots | Many generic or default-looking shots | Random visuals unrelated to intent |
| **Consistency** | Characters, wardrobe, lighting and colour match across every shot; no visible drift | Minor drift in 1–2 shots | Noticeable drift in several shots | Characters/look change constantly |
| **Sound** | Clean dialogue/VO, rich ambience, synced SFX, music supports emotion; balanced mix | All layers present; small level issues | Missing a layer or clear mix problems | Little or no sound design |
| **Edit** | Strong rhythm; artefacts hidden; purposeful cuts; correct delivery format | Good pacing with a few rough cuts | Pacing problems; visible glitches left in | Unedited or wrong format |

**Converting to a grade:** total out of 20 → 18–20 A · 15–17 B · 12–14 C · 9–11 D · below 9 resubmit.

---

## Assignment 1 — Script, logline & shot list (Week 3)
**Brief:** a 2–4 page script for a short you could make with AI, plus a logline and a numbered shot list (8–40 shots).
**Submit:** `script.pdf`, `logline.txt`, `shot_list.csv`.

| Criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| Story | Clear want/obstacle/stakes; scene goals; satisfying change | Clear but predictable | Unclear stakes | No structure |
| Visual writing | Every action line filmable; one action per shot | Mostly filmable | Many internal/abstract lines | Prose, not script |
| Format | Correct screenplay format, page count right | Minor format slips | Inconsistent format | Unformatted |
| Shot list | All columns complete, durations add up to runtime | Small gaps | Missing columns/durations | Missing |
| AI-awareness | Scope designed around AI strengths (limited lip-sync, few locations) | Mostly realistic | Hard-to-generate scenes unaddressed | Unrealistic for AI |

## Assignment 2 — Character sheet & 12-frame storyboard (Week 5)
**Brief:** a character reference sheet for your lead, and 12 storyboard keyframes from your shot list.
**Submit:** sheet PNG, 12 frames as a grid PDF, prompts used.

| Criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| Visuals | Intentional shot sizes/lenses/light per frame | Mostly intentional | Generic | Random |
| Consistency | Same identity, wardrobe, palette in all 12 | 1–2 frames drift | Several drift | No consistency |
| Story clarity | Story readable from frames alone | Mostly readable | Hard to follow | Unreadable |
| Prompt craft | Structured prompts with camera vocabulary and bibles | Mostly structured | Unstructured | Missing |

## Assignment 3 — 30-second "sound-first" scene (Week 7)
**Brief:** build the soundtrack first, then generate and edit visuals to it.
**Submit:** MP4 (30 s ±5), list of audio sources and licences.
**Rubric:** universal rubric (Story, Visuals, Consistency, Sound ×2 weight, Edit) + **Ethics**: consent/licences documented (pass/fail).

## Assignment 4 — Graded scene & delivery package (Week 9)
**Brief:** grade a 45–90 s edited scene built from clips from ≥2 different models; deliver a master, a 9:16 version and captions.
**Submit:** 1080p MP4, 9:16 MP4, SRT file, before/after stills.

| Criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| Consistency (colour match) | Shots from different models indistinguishable | Minor mismatch | Obvious mismatch | Ungraded |
| Visuals (look) | Look supports mood; natural skin | Good look; minor issues | Over/under-processed | No look |
| Edit | Tight, artefacts hidden | Minor issues | Glitches visible | Rough assembly |
| Sound | Balanced, clean | Small level issues | Mix problems | Poor/no sound |
| Delivery | All three files correct spec | One minor error | Missing a file | Wrong formats |

## Assignment 5 — Batch generation pipeline (Week 10)
**Brief:** use (or adapt) [`scripts/batch_generate_videos.py`](../scripts/batch_generate_videos.py) to generate ≥5 shots from your own `prompts.csv`, then stitch them with FFmpeg. Free alternative: run a ComfyUI image-to-video workflow for 5 shots and stitch.
**Submit:** prompts CSV, generation log, rough-cut MP4, short README (how to run, cost), Git repo link.

| Criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| Works end-to-end | Runs from a clean checkout following the README | Runs with minor fixes | Partially works | Doesn't run |
| Security | Keys only in env vars; `.env` in `.gitignore` | — | — | Key committed (automatic resubmit) |
| Cost awareness | Accurate estimate vs actual, cost per usable second reported | Estimate only | Vague | None |
| Consistency | Prompts use bibles; shots match | Mostly | Some drift | None |
| Documentation | Clear README, commit history | Adequate | Thin | None |

---

## Final project rubric

Use the **universal rubric** (×5 criteria, 20 points) **plus**:

| Extra criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| **Pipeline report** | Tools, cost, cost/second, time, lessons, next automation — clear and honest | Mostly complete | Thin | Missing |
| **Rights & disclosure** | Full rights audit, consents, AI disclosure in credits | Minor gaps | Major gaps | Missing |
| **Engineering** | Used automation/ComfyUI/FFmpeg meaningfully | Some automation | Manual only, documented | Undocumented |

Total out of 32 → 29–32 A · 24–28 B · 19–23 C · 14–18 D · below 14 resubmit.

## Peer-feedback template (2-minute format)
1. One moment that worked and why.
2. One moment that confused me.
3. One specific suggestion (shot, cut, sound).
