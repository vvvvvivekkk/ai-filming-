#!/usr/bin/env python3
"""
batch_generate_videos.py — generate one AI video clip per row of a CSV, then
(optionally) stitch them into a rough cut with FFmpeg.

Beginner notes
--------------
* It uses the Replicate HTTP API (https://replicate.com/docs) and only Python's
  standard library, so there is nothing to `pip install`.
* Your API key is read from the REPLICATE_API_TOKEN environment variable.
  NEVER paste a key into this file or commit it to Git. Example:
      macOS/Linux:  export REPLICATE_API_TOKEN="r8_..."
      Windows PS :  $env:REPLICATE_API_TOKEN="r8_..."
* Start with --dry-run: it prints what it *would* send and an estimated cost,
  without spending money.

CSV format (see prompts/example-shots.csv)
------------------------------------------
shot_id,prompt,extra_inputs
S01,"Wide shot of a lighthouse at dawn ...","{""duration"": 5}"

`extra_inputs` is optional JSON merged into the model input. Input names differ
per model — open the model's "API" tab on replicate.com to see them.

Usage
-----
python scripts/batch_generate_videos.py prompts/example-shots.csv --dry-run
python scripts/batch_generate_videos.py prompts/example-shots.csv \
    --model bytedance/seedance-1-pro --price-per-second 0.10 --stitch
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.replicate.com/v1"
TERMINAL_OK = {"succeeded", "successful"}
TERMINAL_BAD = {"failed", "canceled", "cancelled"}


def http_json(method: str, url: str, token: str, body: dict | None = None,
              extra_headers: dict | None = None) -> dict:
    """Send a JSON request and return the decoded JSON response.
    Retries politely on rate limits (HTTP 429) and temporary server errors."""
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    headers.update(extra_headers or {})
    for attempt in range(6):
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                wait = int(e.headers.get("Retry-After", 2 ** attempt * 5))
                print(f"   ...HTTP {e.code}, waiting {wait}s and retrying", file=sys.stderr)
                time.sleep(wait)
                continue
            raise SystemExit(f"API error {e.code}: {e.read().decode()[:500]}")
    raise SystemExit("Gave up after repeated rate-limit/server errors.")


def create_prediction(model: str, inputs: dict, token: str) -> dict:
    owner_name = model.split(":")[0]
    url = f"{API}/models/{owner_name}/predictions"
    # 'Prefer: wait' asks the server to hold the connection up to 60 s; long
    # video jobs will still return early and we poll below.
    return http_json("POST", url, token, {"input": inputs}, {"Prefer": "wait"})


def wait_for(prediction: dict, token: str, poll_seconds: float = 5.0) -> dict:
    while prediction.get("status") not in TERMINAL_OK | TERMINAL_BAD:
        time.sleep(poll_seconds)
        prediction = http_json("GET", prediction["urls"]["get"], token)
        print(f"   status: {prediction.get('status')}")
    return prediction


def first_url(output) -> str | None:
    if isinstance(output, str):
        return output
    if isinstance(output, list) and output:
        return output[0] if isinstance(output[0], str) else None
    if isinstance(output, dict):
        for v in output.values():
            if isinstance(v, str) and v.startswith("http"):
                return v
    return None


def download(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url, timeout=300) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def stitch(clips: list[Path], out_file: Path) -> None:
    """Join clips with FFmpeg. Re-encodes so clips from different models
    (different sizes/frame rates) still join cleanly at 1920x1080, 24 fps."""
    if not shutil.which("ffmpeg"):
        print("FFmpeg not found — install it to use --stitch (https://ffmpeg.org).")
        return
    list_file = out_file.with_suffix(".txt")
    list_file.write_text("".join(f"file '{c.resolve().as_posix()}'\n" for c in clips))
    vf = ("scale=1920:1080:force_original_aspect_ratio=decrease,"
          "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file),
           "-vf", vf, "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
           "-an", str(out_file)]
    print("Stitching:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv_file", type=Path)
    p.add_argument("--model", default="bytedance/seedance-1-pro",
                   help="Replicate model as owner/name (check its API tab for inputs)")
    p.add_argument("--out", type=Path, default=Path("output/clips"))
    p.add_argument("--seconds", type=float, default=5, help="Expected seconds per clip (for cost estimate)")
    p.add_argument("--price-per-second", type=float, default=0.0,
                   help="USD per output second from the model page, for the estimate")
    p.add_argument("--pause", type=float, default=2.0, help="Seconds to wait between jobs (rate limits)")
    p.add_argument("--dry-run", action="store_true", help="Print requests and cost; call nothing")
    p.add_argument("--stitch", action="store_true", help="Join the clips with FFmpeg at the end")
    args = p.parse_args()

    with open(args.csv_file, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("prompt", "").strip()]
    if not rows:
        raise SystemExit("No rows with a 'prompt' column found.")

    est = len(rows) * args.seconds * args.price_per_second
    print(f"{len(rows)} shots · model {args.model} · estimated cost ${est:.2f} "
          f"(≈ ₹{est * 94.85:,.0f} at ₹94.85/USD)")

    token = os.environ.get("REPLICATE_API_TOKEN", "")
    if not args.dry_run and not token:
        raise SystemExit("Set REPLICATE_API_TOKEN in your environment first (see top of file).")

    args.out.mkdir(parents=True, exist_ok=True)
    log_path = args.out / "generation_log.csv"
    clips: list[Path] = []
    with open(log_path, "a", newline="", encoding="utf-8") as log_f:
        log = csv.writer(log_f)
        for i, row in enumerate(rows, 1):
            shot = (row.get("shot_id") or f"S{i:02d}").strip()
            inputs = {"prompt": row["prompt"].strip()}
            if row.get("extra_inputs", "").strip():
                inputs.update(json.loads(row["extra_inputs"]))
            dest = args.out / f"{shot}.mp4"
            print(f"\n[{i}/{len(rows)}] {shot}: {inputs['prompt'][:70]}...")
            if args.dry_run:
                print("   would send:", json.dumps({"input": inputs})[:300])
                continue
            if dest.exists():
                print("   already downloaded, skipping (delete the file to regenerate)")
                clips.append(dest)
                continue
            pred = wait_for(create_prediction(args.model, inputs, token), token)
            if pred.get("status") not in TERMINAL_OK:
                print(f"   FAILED: {pred.get('error')}")
                log.writerow([shot, "failed", pred.get("id"), pred.get("error")])
                continue
            url = first_url(pred.get("output"))
            if not url:
                print("   No file URL in output:", pred.get("output"))
                continue
            download(url, dest)
            clips.append(dest)
            log.writerow([shot, "ok", pred.get("id"), str(dest)])
            print(f"   saved {dest}")
            time.sleep(args.pause)

    if args.stitch and clips:
        stitch(clips, args.out.parent / "rough_cut.mp4")


if __name__ == "__main__":
    main()
