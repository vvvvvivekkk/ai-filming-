# AI Filmmaking Engineer: Zero to Pro

*(repository: `ai-filming-`)*

A free, open learning hub for becoming an **AI filmmaking engineer** — someone who can tell a story with film craft **and** build the technical pipeline (prompts, ComfyUI, Python, APIs, FFmpeg) that turns it into a finished film with AI tools.

**📘 Download the whole guide as a PDF:** [`pdf/AI-Filmmaking-Zero-to-Pro.pdf`](pdf/AI-Filmmaking-Zero-to-Pro.pdf)

> **Prices and tool facts were checked on 2026-11-21.** USD first, INR in brackets at **1 USD = ₹94.85** (Wise mid-market, 2026-11-21). AI tools change monthly — anything we couldn't confirm on an official page is marked **(verify)**. Notably, **OpenAI shut down Sora in 2026**, so older tutorials that rely on it no longer work.

## Who it's for

| You are… | Start here |
|---|---|
| **A learner** studying on your own, from zero | [90-day self-study plan](learners/90-day-self-study-plan.md) → [practice projects](learners/practice-projects.md) → [progress checklist](learners/progress-checklist.md) |
| **A trainer** running a class or workshop | [12-week syllabus](trainers/course-syllabus-12-weeks.md) → [lesson plans](trainers/lesson-plans.md) → [assignments & rubrics](trainers/assignments-and-rubrics.md) → [quizzes](trainers/quizzes-with-answers.md) |
| **Already making AI videos** and want the engineering side | [06 · AI engineer technical skills](docs/06-ai-engineer-technical-skills.md) and [07 · Workflow](docs/07-ai-film-workflow-step-by-step.md) |
| **Just want to know what tools cost** | [05 · Tools & costs](docs/05-ai-filmmaking-tools.md) or the spreadsheet [`data/tools-and-costs.csv`](data/tools-and-costs.csv) |

## How to use this repo

1. Read the [roadmap](docs/00-roadmap.md) (10 minutes) to see the whole journey: 9 stages, each ending in a checkpoint you must produce.
2. Pick your path (learner or trainer) from the table above.
3. **Complete beginner?** Read [11 · How AI video works](docs/11-how-ai-video-works-explained.md) first — it explains every basic idea in plain English. Then work through the topic chapters in order; each has *what it is → why it matters for AI film → core concepts → free & paid resources → one hands-on exercise → how AI helps*.
4. Use the [prompt library](prompts/ai-video-prompt-library.md) while you practise, and the [batch script](scripts/batch_generate_videos.py) when you reach the engineering stage.
5. Tick off the [progress checklist](learners/progress-checklist.md) every week.

**You don't need to spend money to start.** The free stack (DaVinci Resolve + free tiers) covers the first 40 days. The recommended Starter stack is about **$44/month (₹4,172)**; a Pro stack is about **$197/month (₹18,685)** — see [budget stacks](docs/05-ai-filmmaking-tools.md#three-budget-stacks).

## Table of contents

### Core guide (`docs/`)
| # | Chapter | What you'll learn |
|---|---|---|
| 00 | [The zero-to-pro roadmap](docs/00-roadmap.md) | Stages, timelines, checkpoints |
| 01 | [Story & screenwriting](docs/01-story-screenwriting.md) | Loglines, structure, scripts, shot lists |
| 02 | [Cinematography & visual language](docs/02-cinematography-visual-language.md) | Shot sizes, lenses, light, colour, camera moves |
| 03 | [Production, directing & sound](docs/03-production-directing-sound.md) | Directing AI performance, voice, SFX, music |
| 04 | [Post-production: editing & colour](docs/04-post-production-editing-color.md) | DaVinci Resolve, matching models, finishing |
| 05 | [AI filmmaking tools & costs](docs/05-ai-filmmaking-tools.md) | 66 tools priced (video, image, voice, music, 3D/mocap, storyboarding, editing), 3 budget stacks, hardware |
| 06 | [AI engineer technical skills](docs/06-ai-engineer-technical-skills.md) | Prompt systems, consistency/LoRA, ComfyUI, Python, APIs, GPUs, FFmpeg, Git, agentic pipelines |
| 07 | [AI film workflow, step by step](docs/07-ai-film-workflow-step-by-step.md) | The 12-step pipeline from idea to release |
| 08 | [Legal, ethics & copyright](docs/08-legal-ethics-copyright.md) | US Copyright Office guidance, licences, consent |
| 09 | [Career, portfolio & festivals](docs/09-career-portfolio-festivals.md) | Portfolio, festivals, getting paid |
| 10 | [Glossary](docs/10-glossary.md) | Every term in plain English |
| 11 | [How AI video actually works (beginner explainer)](docs/11-how-ai-video-works-explained.md) | Models, diffusion, prompts, seeds, credits, fps, why faces drift, lip-sync, voice cloning, open weights |
| 12 | [Tool-by-tool beginner guide](docs/12-tool-by-tool-guide.md) | For every tool category: what it is, when to use it, how to start, tips, pitfalls |

### For trainers (`trainers/`)
- [12-week course syllabus](trainers/course-syllabus-12-weeks.md)
- [Lesson plans (weeks 1–12)](trainers/lesson-plans.md)
- [Assignments & grading rubrics](trainers/assignments-and-rubrics.md)
- [Quizzes with answer keys (9 modules × 10 questions)](trainers/quizzes-with-answers.md)

### For learners (`learners/`)
- [90-day self-study plan (day by day)](learners/90-day-self-study-plan.md)
- [5 practice projects, easy → hard](learners/practice-projects.md)
- [Progress checklist](learners/progress-checklist.md)

### Prompts (`prompts/`)
- [AI video prompt library — 35 prompts with explanations](prompts/ai-video-prompt-library.md)
- [Example shot CSV for the batch script](prompts/example-shots.csv)

### Data (`data/`)
- [Tools and costs (CSV)](data/tools-and-costs.csv)
- [All resources and sources (CSV)](data/resources.csv)

### Scripts (`scripts/`)
- [`batch_generate_videos.py`](scripts/batch_generate_videos.py) — generate clips from a CSV via API (key from environment variable), log them, stitch with FFmpeg
- [`build_pdf.py`](scripts/build_pdf.py) — rebuilds the PDF from all Markdown files
- [`check_links.py`](scripts/check_links.py) — checks every relative link, anchor and external URL in the Markdown files

### PDF (`pdf/`)
- [AI-Filmmaking-Zero-to-Pro.pdf](pdf/AI-Filmmaking-Zero-to-Pro.pdf)

## Rebuild the PDF

```bash
pip install weasyprint            # also needs pandoc installed (https://pandoc.org)
python scripts/build_pdf.py       # writes pdf/AI-Filmmaking-Zero-to-Pro.pdf
```

## Contributing

Prices go stale fast. If you spot a changed price or dead link, open an issue or PR with the new value, the official source link, and the date you checked it. Please keep the "Price checked" dates and **(verify)** markers honest.

## License

Content is licensed under **[CC BY 4.0](LICENSE)** — free to share and adapt with attribution. Product names belong to their owners. Not legal or financial advice.
