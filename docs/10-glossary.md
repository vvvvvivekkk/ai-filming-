# 10 · Glossary

Plain-English definitions of every term used in this guide, alphabetical. For longer, step-by-step explanations of the AI ideas, read [11 · How AI video works](11-how-ai-video-works-explained.md).

| Term | Meaning |
|---|---|
| **ADR** | Automated Dialogue Replacement — re-recording dialogue after filming. |
| **Agentic pipeline** | A chain of AI steps where each output becomes the next input (script → shots → prompts → clips), with human checkpoints. |
| **Aggregator** | A platform that lets you use many companies' models under one subscription (Krea, Magnific, Higgsfield, invideo). |
| **Ambience / room tone** | The background sound of a location. |
| **Anamorphic** | A lens type that creates wide cinematic frames, oval bokeh and horizontal flares. |
| **Animatic** | A rough timed slideshow of storyboard frames with temp sound, used to test pacing. |
| **API** | Application Programming Interface — a way for code to use a service (e.g. generate a video) directly. |
| **API key** | A secret password that identifies your account to an API. Keep it in environment variables, never in code. |
| **Aspect ratio** | Frame shape: 16:9, 9:16, 2.39:1, 1:1. |
| **Beat** | The smallest unit of story change in a scene. |
| **Blocking** | Planning where actors and camera move in a scene. |
| **Bokeh** | The soft, blurred background from shallow depth of field. |
| **Character reference sheet** | One image showing a character from several angles/expressions, used to keep them consistent. |
| **Codec** | How video is compressed (H.264, H.265/HEVC, ProRes). |
| **Colour correction / grading** | Correction makes shots accurate and matching; grading applies the creative look. |
| **ComfyUI** | Free node-based app for running image/video AI models locally or in the cloud. |
| **Commercial licence** | Permission to use an output in something that earns money. Free tiers usually don't include it. |
| **Compute units** | Usage currency on some platforms (Colab, Krea). |
| **Container** | The file wrapper (.mp4, .mov) holding video, audio and metadata. |
| **Coverage** | The set of shots filmed/generated so a scene can be edited. |
| **Credits** | A tool's internal currency; each generation spends credits. |
| **CRF** | Constant Rate Factor — an FFmpeg quality setting (lower = higher quality, bigger file; 18–23 is typical). |
| **Denoising / steps** | Diffusion starts from random noise and cleans it a little each step; more steps usually = more detail but slower. |
| **Depth of field** | How much of the image is in focus. |
| **Diegetic sound** | Sound that exists in the story world. Non-diegetic: score, narration. |
| **Diffusion model** | The type of AI behind most image/video generators — it learns to turn noise into images step by step. |
| **Dolly / truck / crane** | Camera moves: forward/back, sideways, up/down. |
| **Environment variable** | A named value stored in your computer's environment (e.g. `REPLICATE_API_TOKEN`) that programs can read without hardcoding. |
| **Face drift** | When a character's face slowly changes during a clip or between shots. Fixed with reference images, shorter clips and image-to-video. |
| **FFmpeg** | Free command-line tool to convert, cut, join and analyse video/audio. |
| **Focal length** | Lens measurement in mm; low = wide, high = telephoto. |
| **Foley** | Everyday sound effects recreated and synced to picture. |
| **fps** | Frames per second. 24 fps is the cinema standard. |
| **Frame interpolation** | AI creation of in-between frames for smoother or slower motion. |
| **Git / Git LFS** | Version-control system / its extension for large media files. |
| **GPU / VRAM** | Graphics processor / its dedicated memory; AI models must fit in VRAM. |
| **Guidance / CFG** | A setting for how strictly the model follows your prompt. Too high = harsh, over-cooked images; too low = it ignores you. |
| **Image-to-video (I2V)** | Animating a still image into a clip — the most controllable way to generate shots. |
| **Inference** | Running a trained model to get an output. Every time you click Generate, the company runs inference on its GPUs. |
| **Ingredients / references** | Images you give a model so it includes a specific character, object or style. |
| **J-cut / L-cut** | Audio of the next shot starts before the picture cut (J), or audio continues after it (L). |
| **Key / fill / back (rim) light** | Main light, shadow-softening light, separating light from behind. |
| **Keyframe** | In this guide: the approved still image that becomes the first frame of a generated shot. |
| **Latent space** | A compressed 'idea space' where diffusion models work before turning results back into pixels — why generation is faster than drawing every pixel directly. |
| **Licensed training data** | Training data the AI company had permission to use (e.g. Moonvalley Marey, Adobe Firefly). Lower legal risk for commercial work. |
| **Lip-sync** | Changing a character's mouth movements to match an audio track. |
| **Logline** | One- or two-sentence summary of a story. |
| **Lookbook** | A collection of reference images defining a film's visual style. |
| **LoRA** | Low-Rank Adaptation — a small add-on file that teaches an open model a specific character or style. |
| **LUT** | Look-Up Table — a colour conversion preset. |
| **Mesh** | A 3D object made of connected points and flat faces; what Blender, Unreal and Meshy work with. |
| **Model** | The trained AI 'brain' — a big file of numbers learned from examples — that turns your prompt into an output. Kling 2.x, Veo 3.1 and Wan 2.2 are models; the app around them is the tool. |
| **Motion capture (mocap)** | Recording a real person's movement and applying it to a 3D/CG character. AI mocap (Move AI, Flow Studio) works from ordinary video, no suit needed. |
| **Motion transfer** | Copying the body movement from a reference video onto another character (Viggle, Kling motion control). |
| **Motivated lighting** | Light that seems to come from a believable source in the scene. |
| **Native audio** | Video models that generate sound (dialogue, effects, ambience) together with the picture, e.g. Veo 3.1, Kling. |
| **Negative prompt** | Text listing what you don't want in the output (not supported by all models). |
| **Node** | One box in a ComfyUI graph that does a single step. |
| **Offloading** | Moving parts of a model from VRAM to system RAM so it fits on smaller GPUs (slower). |
| **Open weights** | A model whose trained file you can download and run on your own computer (Wan 2.2, LTX Video). Not always 'open source' — check its licence. |
| **Pay-as-you-go** | Paying only for what you use (per second of video or per image), usually through an API, instead of a monthly plan. |
| **Previs** | Previsualisation — planning shots visually before production. |
| **Prompt** | Text instructions given to an AI model. |
| **Quantization** | Shrinking a model by storing numbers with less precision so it needs less VRAM (small quality loss). |
| **Rate limit** | Maximum API requests allowed per time period; exceeding it returns HTTP 429. |
| **Real-time engine** | Software (e.g. Unreal Engine) that renders 3D scenes instantly, like a video game, instead of waiting minutes per frame. |
| **Reference-to-video** | Giving the model one or more images of a character/object so it keeps them consistent in the generated clip. |
| **Relax mode** | Slower, unlimited generation queue on some plans (e.g. Midjourney Standard+). |
| **Resolution** | How many pixels in each frame: 720p (1280×720), 1080p (1920×1080), 4K (3840×2160). |
| **Royalty-free** | Music/footage you pay for once (or by subscription) and can use without paying per view — still under a licence with rules. |
| **180° rule** | Keep the camera on one side of an imaginary line between two characters so their screen positions stay consistent. |
| **Rule of thirds** | Placing key elements along lines dividing the frame in thirds. |
| **Screenplay format** | The standard layout of a film script (sluglines, action, character names, dialogue) that apps like Final Draft apply automatically. |
| **Seed** | A number that sets a generation's randomness; same seed + same settings ≈ similar result. |
| **Shot list** | Numbered list of every shot with size, angle, action and duration. |
| **Shot sizes** | EWS (extreme wide), WS (wide), MS (medium), MCU (medium close-up), CU (close-up), ECU (extreme close-up). |
| **Showreel** | A short montage of your best work. |
| **Slugline** | Scene heading in a script: `INT. KITCHEN – NIGHT`. |
| **Speech enhancement** | AI cleanup that removes noise and echo from recorded dialogue (Adobe Podcast Enhance, Resolve voice isolation). |
| **SRT** | A plain-text subtitle/caption file format. |
| **Stems** | Separate audio tracks of one song (drums, bass, vocals…), so you can mix them under dialogue. |
| **Storyboard** | A sequence of drawings/images showing each planned shot, in order, before you generate or film. |
| **Style bible** | Fixed text describing a project's look, pasted into every prompt for consistency. |
| **Temporal consistency** | Whether things stay the same from frame to frame (a face, a shirt, a sign). Weak consistency causes flicker and 'face drift'. |
| **Text-to-3D** | Generating a 3D model (a mesh you can rotate) from a text prompt or image (Meshy). |
| **Text-to-speech (TTS)** | Turning written text into spoken audio with an AI voice. |
| **Text-to-video (T2V)** | Generating a clip from a text prompt alone. |
| **Training data** | The examples (images, videos, text, audio) a model learned from. Who owned that data matters for copyright and ethics. |
| **Upscaling** | AI increase of resolution (e.g. 720p → 4K). |
| **Vector (SVG)** | Graphics made of shapes rather than pixels, so they stay sharp at any size — good for logos and titles (Recraft). |
| **Virtual production** | Filming or rendering inside a real-time 3D world (LED walls, Unreal Engine) instead of a physical location. |
| **Voice cloning** | Training a synthetic voice on recordings of a real person. Only ever clone a voice with that person's written consent. |
| **Watermark** | A logo/text stamped on free-tier outputs. |
