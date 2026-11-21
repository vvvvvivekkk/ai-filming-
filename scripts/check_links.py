#!/usr/bin/env python3
"""
check_links.py — check every link in the repo's Markdown files.

* Relative links: the target file must exist, and any #anchor must match a
  heading in that file (GitHub-style anchors).
* External links (http/https): requested with a HEAD/GET; anything that is not
  2xx/3xx is reported. Some sites block scripts (403/429) — re-check those by
  hand in a browser before deleting them.

Usage:
    python scripts/check_links.py            # relative + external
    python scripts/check_links.py --offline  # relative links only
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
BARE_URL_RE = re.compile(r"https?://[^\s<>\"')\],{}`*|]+")


def gh_anchor(heading: str) -> str:
    """Approximate GitHub's heading-to-anchor rule."""
    h = re.sub(r"[*_`]", "", heading.strip().lower())
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def anchors_in(md_file: Path) -> set[str]:
    anchors, counts = set(), {}
    in_code = False
    for line in md_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        m = re.match(r"#{1,6}\s+(.*)", line)
        if m:
            a = gh_anchor(m.group(1))
            n = counts.get(a, 0)
            anchors.add(a if n == 0 else f"{a}-{n}")
            counts[a] = n + 1
    return anchors


def check_external(url: str) -> str | None:
    headers = {"User-Agent": "Mozilla/5.0 (link-checker for ai-filming- repo)"}
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status < 400:
                    return None
        except urllib.error.HTTPError as e:
            if method == "GET":
                return f"HTTP {e.code}"
        except Exception as e:  # network errors, timeouts
            if method == "GET":
                return type(e).__name__
    return "unknown"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()

    md_files = sorted(p for p in ROOT.rglob("*.md") if "pdf/build" not in p.as_posix())
    problems, external = [], {}
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://")):
                external.setdefault(target, md)
                continue
            if target.startswith("mailto:"):
                continue
            path_part, _, frag = target.partition("#")
            dest = md if not path_part else (md.parent / path_part).resolve()
            if not dest.exists():
                problems.append(f"{md.relative_to(ROOT)}: missing file -> {target}")
                continue
            if frag and dest.suffix == ".md" and frag not in anchors_in(dest):
                problems.append(f"{md.relative_to(ROOT)}: missing anchor -> {target}")
        for url in BARE_URL_RE.findall(text):
            external.setdefault(url.rstrip(".,;:"), md)

    print(f"Checked {len(md_files)} Markdown files.")
    if not args.offline:
        print(f"Checking {len(external)} external URLs...")
        for url, md in sorted(external.items()):
            if "{" in url or "api.replicate.com" in url:
                continue
            err = check_external(url)
            if err:
                problems.append(f"{md.relative_to(ROOT)}: {err} -> {url}")

    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("All links OK.")


if __name__ == "__main__":
    main()
