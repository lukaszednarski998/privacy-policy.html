#!/usr/bin/env python3
"""Ensure consent-based ARVION GA4 tracking is loaded on every public HTML page.

Only includes the existing shared opt-in scripts: GA4 is not contacted unless
a visitor has accepted analytics. Idempotent and safe to rerun after SEO updates.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECK = "--check" in sys.argv
DOCS = sorted(ROOT.glob("*.html")) + sorted((ROOT / "apps").rglob("*.html"))
MARKERS = ("assets/analytics-config.js", "assets/site-analytics.js")

processed = 0
already = 0
changed = []
skipped = []

for file in DOCS:
    # Verification endpoints require their exact original body.
    if re.fullmatch(r"google[a-z0-9]+\.html", file.name, re.IGNORECASE):
        continue
    source = file.read_bytes().decode("utf-8")
    original = source
    source = re.sub(r"""(<script\b[^>]*\bsrc=[\'"])([^\'"]*assets/site-analytics\.js)(?:\?[^\'"]*)?([\'"])""", r"\1\2?v=20261014-social2\3", source, flags=re.IGNORECASE)
    existing = source.lower()
    missing = [name for name in MARKERS if name not in existing]
    processed += 1
    if not missing:
        if source != original:
            changed.append(file.relative_to(ROOT).as_posix())
            if not CHECK:
                file.write_bytes(source.encode("utf-8"))
        else:
            already += 1
        continue

    # Avoid replacing or restructuring the site's existing scripts and markup.
    closes = list(re.finditer(r"</body\s*>", source, re.IGNORECASE))
    if not closes:
        closes = list(re.finditer(r"</html\s*>", source, re.IGNORECASE))
    if not closes:
        skipped.append(file.relative_to(ROOT).as_posix())
        continue

    path = file.relative_to(ROOT)
    prefix = "../" * (len(path.parts) - 1)
    newline = "\r\n" if "\r\n" in source else "\n"
    fragment = "".join(
        '<script defer src="' + prefix + (name + '?v=20261014-social2' if name == 'assets/site-analytics.js' else name) + '"></script>' + newline
        for name in missing
    )
    last = closes[-1]
    updated = source[:last.start()] + fragment + source[last.start():]
    changed.append(path.as_posix())
    if not CHECK:
        file.write_bytes(updated.encode("utf-8"))

print(
    f"ARVION GA4: html={len(DOCS)} eligible={processed} "
    f"already={already} {'missing' if CHECK else 'updated'}={len(changed)} "
    f"skipped_no_closing_tag={len(skipped)}"
)
if changed:
    print("Affected pages (first 20):", ", ".join(changed[:20]))
if skipped:
    print("Skipped:", ", ".join(skipped))
if CHECK and (changed or skipped):
    raise SystemExit("Some public HTML pages are missing GA4 opt-in scripts")
if skipped:
    raise SystemExit("Some public HTML pages have no valid closing tags")
