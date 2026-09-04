from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove every older availability implementation first.
s = re.sub(
    r'\s*/\* ARVION AVAILABILITY START \*/.*?/\* ARVION AVAILABILITY END \*/\s*',
    '\n',
    s,
    flags=re.S,
)
s = re.sub(
    r'\s*<!-- ARVION AVAILABILITY SCRIPT START -->.*?<!-- ARVION AVAILABILITY SCRIPT END -->\s*',
    '\n',
    s,
    flags=re.S,
)

# Pure styling only. The labels themselves are rendered as normal HTML by the
# existing card renderer, so there is no MutationObserver and no extra runtime
# script that could freeze the page.
css = '''
/* ARVION AVAILABILITY START */
.availability-label{display:block;margin-top:12px;padding:9px 11px;border-radius:12px;font-size:11px;font-weight:900;letter-spacing:.035em;line-height:1.35;text-align:center}
.availability-label.soon{border:1px solid rgba(216,170,67,.55);background:rgba(216,170,67,.08);color:#f2d99d}
.availability-label.available{border:1px solid rgba(73,190,96,.65);background:rgba(36,125,54,.16);color:#bff5c9}
/* ARVION AVAILABILITY END */
'''
s = s.replace('</style>', css + '\n</style>', 1)

old = '<div class="body"><span class="tag">${p.tag}</span><h3>${p.name}</h3><p>${p.desc}</p></div></article>'
new = '<div class="body"><span class="tag">${p.tag}</span><h3>${p.name}</h3><p>${p.desc}</p><div class="availability-label ${p.id===\'obd\'?\'available\':\'soon\'}">${p.id===\'obd\'?\'DOSTĘPNA TERAZ · AVAILABLE NOW\':\'DOSTĘPNA WKRÓTCE · COMING SOON\'}</div></div></article>'

if old in s:
    s = s.replace(old, new, 1)
elif 'availability-label ${p.id===' not in s:
    raise SystemExit('Product card template not found; index.html was left unchanged.')

p.write_text(s, encoding='utf-8')
