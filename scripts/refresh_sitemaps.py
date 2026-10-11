#!/usr/bin/env python3
"""Regenerate canonical XML/text sitemaps from all public ARVION HTML pages.

Maps index.html to / and apps/index.html to /apps/ so duplicate URLs
are not advertised. Excludes Google's HTML ownership-verification files.
Safe to run repeatedly, including after application/translation updates.
"""
from html import escape
from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://lukaszednarski998.github.io/privacy-policy.html/"
EXCLUDED = re.compile(r"^google[a-z0-9]+\.html$", re.IGNORECASE)

paths = sorted(
    [*ROOT.glob("*.html"), *(ROOT / "apps").rglob("*.html")],
    key=lambda p: p.relative_to(ROOT).as_posix()
)
urlset = set()
for file in paths:
    relative = file.relative_to(ROOT).as_posix()
    if EXCLUDED.fullmatch(relative):
        continue
    if relative == "index.html":
        path = ""
    elif relative == "apps/index.html":
        path = "apps/"
    else:
        path = quote(relative, safe="/-_.~")
    urlset.add(BASE + path)

urls = sorted(urlset, key=lambda url: (url != BASE, url != BASE + "apps/", url))
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
for url in urls:
    xml_lines += ["  <url>", f"    <loc>{escape(url)}</loc>", "  </url>"]
xml_lines.append("</urlset>")
xml = "\n".join(xml_lines) + "\n"
txt = "\n".join(urls) + "\n"

for filename, content in (
    ("sitemap.xml", xml),
    ("sitemap-google.xml", xml),
    ("sitemap.txt", txt),
):
    path = ROOT / filename
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")
        print("Updated", filename)
    else:
        print("Already current:", filename)

assert len(urls) == len(urlset)
assert all(url.startswith(BASE) for url in urls)
print(f"Sitemap coverage: {len(urls)} canonical URLs from {len(paths)} HTML files.")
