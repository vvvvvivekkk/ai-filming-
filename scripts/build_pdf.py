#!/usr/bin/env python3
"""
build_pdf.py — combine README + docs + trainers + learners + prompts into one
PDF: cover page, clickable table of contents with page numbers, page numbers,
11pt body text, readable tables (the big tools table gets a landscape page),
clickable links, PDF bookmarks, and a final "Sources" section listing every URL.

Requirements:
    pandoc   (https://pandoc.org/installing.html)
    weasyprint  ->  pip install weasyprint

Usage (from the repo root or anywhere):
    python scripts/build_pdf.py
Output:
    pdf/AI-Filmmaking-Zero-to-Pro.pdf
"""
from __future__ import annotations

import csv
import datetime as dt
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "pdf" / "AI-Filmmaking-Zero-to-Pro.pdf"
TITLE = "AI Filmmaking Engineer: Zero to Pro"
SUBTITLE = "A complete learning hub for learners and trainers — story, craft, AI tools, engineering, and career"
REPO = "https://github.com/vvvvvivekkk/ai-filming-"

# Order matters: this is the order of the book.
PARTS = [
    ("Introduction", ["README.md"]),
    ("Part I · Core Guide", [
        "docs/00-roadmap.md",
        "docs/01-story-screenwriting.md",
        "docs/02-cinematography-visual-language.md",
        "docs/03-production-directing-sound.md",
        "docs/04-post-production-editing-color.md",
        "docs/05-ai-filmmaking-tools.md",
        "docs/06-ai-engineer-technical-skills.md",
        "docs/07-ai-film-workflow-step-by-step.md",
        "docs/08-legal-ethics-copyright.md",
        "docs/09-career-portfolio-festivals.md",
        "docs/10-glossary.md",
    ]),
    ("Part II · For Trainers", [
        "trainers/course-syllabus-12-weeks.md",
        "trainers/lesson-plans.md",
        "trainers/assignments-and-rubrics.md",
        "trainers/quizzes-with-answers.md",
    ]),
    ("Part III · For Learners", [
        "learners/90-day-self-study-plan.md",
        "learners/practice-projects.md",
        "learners/progress-checklist.md",
    ]),
    ("Part IV · Prompt Library", ["prompts/ai-video-prompt-library.md"]),
]

URL_RE = re.compile(r"https?://[^\s<>\"')\],{}`*]+")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-⛿✀-➿️]")

CSS = r"""
@page { size: A4; margin: 20mm 18mm 22mm 18mm;
  @bottom-center { content: counter(page); font: 9pt "DejaVu Sans", sans-serif; color: #666; }
  @top-right { content: string(chapter); font: 8pt "DejaVu Sans", sans-serif; color: #999; } }
@page cover { margin: 0; @bottom-center { content: none; } @top-right { content: none; } }
@page front { @bottom-center { content: counter(page, lower-roman); } @top-right { content: none; } }
@page wide { size: A4 landscape; margin: 12mm 10mm 16mm 10mm; }
html { font-family: "DejaVu Serif", serif; font-size: 11pt; line-height: 1.45; color: #1a1a1a; }
body { margin: 0; }
h1, h2, h3, h4 { font-family: "DejaVu Sans", sans-serif; color: #0b2545; line-height: 1.2;
  page-break-after: avoid; break-after: avoid; }
h1 { font-size: 20pt; string-set: chapter content(); border-bottom: 2px solid #13315c; padding-bottom: 4pt; margin-top: 0; }
h2 { font-size: 14pt; margin-top: 16pt; }
h3 { font-size: 12pt; margin-top: 12pt; }
h4 { font-size: 11pt; }
a { color: #1d4ed8; text-decoration: none; }
p, li { orphans: 2; widows: 2; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt; background: #f2f4f7; padding: 0 2pt; }
pre { background: #f2f4f7; border-left: 3px solid #13315c; padding: 6pt 8pt; font-size: 8pt;
  white-space: pre-wrap; word-wrap: break-word; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #8da9c4; margin: 8pt 0; padding: 2pt 10pt; color: #333; background: #f7f9fc; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 8.5pt; line-height: 1.3; }
th, td { border: 0.5pt solid #b8c4d4; padding: 3pt 4pt; vertical-align: top; text-align: left;
  overflow-wrap: anywhere; }
th { background: #13315c; color: white; font-family: "DejaVu Sans", sans-serif; }
tr:nth-child(even) td { background: #f5f7fb; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
section.chapter { page-break-before: always; }
section.part { page: front; page-break-before: always; text-align: center; padding-top: 80mm; }
section.part h1 { border: none; font-size: 26pt; string-set: chapter ""; }
.wide { page: wide; }
.wide table { font-size: 6.6pt; }
.wide th, .wide td { padding: 2pt 3pt; }
.wide table { table-layout: fixed; width: 93%; }
.wide th:nth-child(1) { width: 7%; }  .wide th:nth-child(2) { width: 6.5%; }
.wide th:nth-child(3) { width: 12%; } .wide th:nth-child(4) { width: 9%; }
.wide th:nth-child(5) { width: 10%; } .wide th:nth-child(6) { width: 14%; }
.wide th:nth-child(7) { width: 12%; } .wide th:nth-child(8) { width: 11%; }
.wide th:nth-child(9) { width: 5.5%; } .wide th:nth-child(10) { width: 4%; }
.wide th:nth-child(11) { width: 7%; }
.wide td, .wide th { overflow-wrap: anywhere; hyphens: auto; }
/* cover */
.cover { page: cover; height: 297mm; width: 210mm; background: linear-gradient(160deg, #0b2545 0%, #13315c 55%, #134074 100%);
  color: white; display: flex; flex-direction: column; justify-content: center; padding: 0 22mm; box-sizing: border-box; }
.cover .kicker { font-family: "DejaVu Sans", sans-serif; letter-spacing: 3pt; font-size: 10pt; color: #8da9c4; text-transform: uppercase; }
.cover h1 { color: white; border: none; font-size: 34pt; margin: 10pt 0; string-set: chapter ""; }
.cover .sub { font-size: 14pt; color: #dbe7f3; max-width: 150mm; }
.cover .meta { margin-top: 30mm; font-family: "DejaVu Sans", sans-serif; font-size: 10pt; color: #b9cde0; }
.cover .meta a { color: #ffffff; }
/* toc */
nav.toc { page: front; page-break-before: always; }
nav.toc h1 { string-set: chapter ""; }
nav.toc ul { list-style: none; padding-left: 0; }
nav.toc li { margin: 2pt 0; }
nav.toc li.part { font-family: "DejaVu Sans", sans-serif; font-weight: bold; margin-top: 10pt; color: #0b2545; }
nav.toc li.ch { padding-left: 10pt; }
nav.toc li.sec { padding-left: 24pt; font-size: 9.5pt; color: #333; }
nav.toc a { color: #1a1a1a; }
nav.toc a::after { content: leader('.') target-counter(attr(href), page); }
.sources ol { font-size: 8.5pt; overflow-wrap: anywhere; }
.note { font-size: 9pt; color: #555; }
input[type=checkbox] { width: 8pt; height: 8pt; }
"""


def slug_for(path: str) -> str:
    return "f-" + re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def md_to_html(md_text: str) -> str:
    res = subprocess.run(
        ["pandoc", "--from", "gfm-tex_math_dollars", "--to", "html5", "--no-highlight", "--wrap=none"],
        input=md_text, capture_output=True, text=True, check=True)
    return res.stdout


def prefix_ids(fragment: str, prefix: str) -> str:
    """Make heading ids unique per file: id="x" -> id="prefix--x"."""
    return re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}--{m.group(1)}"', fragment)


def rewrite_links(fragment: str, src: str, known: dict[str, str]) -> str:
    """Turn relative links to other Markdown files into in-PDF anchors;
    turn links to non-Markdown repo files (CSV, .py, PDF) into GitHub links."""
    src_dir = (ROOT / src).parent

    def fix(m: re.Match) -> str:
        href = html.unescape(m.group(1))
        if href.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        if href.startswith("#"):
            return f'href="#{slug_for(src)}--{href[1:]}"'
        target, _, frag = href.partition("#")
        resolved = (src_dir / target).resolve()
        try:
            rel = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return m.group(0)
        if rel in known:
            anchor = f"{known[rel]}--{frag}" if frag else known[rel]
            return f'href="#{anchor}"'
        return f'href="{REPO}/blob/main/{rel}"'

    return re.sub(r'href="([^"]+)"', fix, fragment)


def collect_urls(texts: list[str]) -> list[str]:
    seen, out = set(), []
    for t in texts:
        for u in URL_RE.findall(t):
            u = u.rstrip(".,;:")
            if u.endswith("/v1/models/") or "api.replicate.com" in u:
                continue  # code templates, not reference links
            if u not in seen:
                seen.add(u)
                out.append(u)
    return out


def main() -> None:
    if not shutil.which("pandoc"):
        sys.exit("pandoc is required: https://pandoc.org/installing.html")
    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("weasyprint is required: pip install weasyprint")

    known = {p: slug_for(p) for _, files in PARTS for p in files}
    all_text: list[str] = []
    toc_items: list[str] = []
    body: list[str] = []

    for part_title, files in PARTS:
        part_id = "p-" + re.sub(r"[^a-z0-9]+", "-", part_title.lower()).strip("-")
        if part_title != "Introduction":
            body.append(f'<section class="part" id="{part_id}"><h1>{html.escape(part_title)}</h1></section>')
            toc_items.append(f'<li class="part"><a href="#{part_id}">{html.escape(part_title)}</a></li>')
        for path in files:
            md = (ROOT / path).read_text(encoding="utf-8")
            all_text.append(md)
            md = EMOJI_RE.sub("", md)
            md = re.sub(r"^(\s*[-*]) \[ \]", r"\1 ☐", md, flags=re.M)
            md = re.sub(r"^(\s*[-*]) \[[xX]\]", r"\1 ☑", md, flags=re.M)
            frag = md_to_html(md)
            sid = known[path]
            frag = rewrite_links(prefix_ids(frag, sid), path, known)
            # first h1 becomes the chapter anchor
            m = re.search(r"<h1[^>]*>(.*?)</h1>", frag, re.S)
            title = html.unescape(re.sub("<[^>]+>", "", m.group(1)).strip()) if m else path
            toc_items.append(f'<li class="ch"><a href="#{sid}">{html.escape(title)}</a></li>')
            # h2 entries for core docs only (keeps TOC to a sensible length)
            if path.startswith("docs/") or path == "README.md":
                for hid, htxt in re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', frag, re.S):
                    t = html.unescape(re.sub("<[^>]+>", "", htxt).strip())
                    toc_items.append(f'<li class="sec"><a href="#{hid}">{html.escape(t)}</a></li>')
            # put the giant tools table on landscape pages
            if path == "docs/05-ai-filmmaking-tools.md":
                frag = re.sub(r"(<table>.*?Cheapest paid.*?</table>)",
                              r'<div class="wide">\1</div>', frag, count=1, flags=re.S)
            body.append(f'<section class="chapter" id="{sid}">{frag}</section>')

    # CSV files count as sources too
    for csv_path in ["data/tools-and-costs.csv", "data/resources.csv"]:
        all_text.append((ROOT / csv_path).read_text(encoding="utf-8"))
    urls = collect_urls(all_text)
    sources = "".join(f'<li><a href="{html.escape(u)}">{html.escape(u)}</a></li>' for u in urls)
    body.append(
        '<section class="chapter sources" id="sources"><h1>Sources</h1>'
        f'<p class="note">Every URL referenced in this guide and its data files ({len(urls)} links). '
        'Links were checked on 2026-11-21; prices are a dated snapshot.</p>'
        f'<ol>{sources}</ol></section>')
    toc_items.append('<li class="ch"><a href="#sources">Sources</a></li>')

    today = dt.date.today().isoformat()
    cover = (
        '<div class="cover">'
        '<div class="kicker">Learning hub · Learners &amp; Trainers</div>'
        f'<h1>{html.escape(TITLE)}</h1>'
        f'<div class="sub">{html.escape(SUBTITLE)}</div>'
        f'<div class="meta">Edition: {today}<br>Prices checked: 2026-11-21 · 1 USD = ₹94.85<br>'
        f'<a href="{REPO}">{REPO}</a><br>Licensed CC BY 4.0</div></div>')
    toc = f'<nav class="toc"><h1>Contents</h1><ul>{"".join(toc_items)}</ul></nav>'

    doc = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(TITLE)}</title>'
           f'<style>{CSS}</style></head><body>{cover}{toc}{"".join(body)}</body></html>')

    OUT.parent.mkdir(parents=True, exist_ok=True)
    build_dir = ROOT / "pdf" / "build"
    build_dir.mkdir(exist_ok=True)
    (build_dir / "book.html").write_text(doc, encoding="utf-8")
    HTML(string=doc, base_url=str(ROOT)).write_pdf(str(OUT))
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size/1e6:.1f} MB), {len(urls)} sources")


if __name__ == "__main__":
    main()
