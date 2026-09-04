from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Keep the public product name requested by the owner.
s = s.replace("name:'OBD Active Exhaust Pro'", "name:'OBD Active Sound'", 1)
s = s.replace("title:'OBD Active Exhaust Pro'", "title:'OBD Active Sound'", 1)

# Availability labels are rendered with CSS only. No MutationObserver or
# post-load JavaScript is needed, which keeps the public page responsive.
css = '''
/* ARVION AVAILABILITY START */
.card[data-product] .body::after{content:"DOSTĘPNA WKRÓTCE · COMING SOON";display:block;margin-top:12px;padding:9px 11px;border:1px solid rgba(216,170,67,.55);border-radius:12px;background:rgba(216,170,67,.08);color:#f2d99d;font-size:11px;font-weight:900;letter-spacing:.035em;line-height:1.35;text-align:center}
.card[data-product="obd"] .body::after{content:"DOSTĘPNA TERAZ · AVAILABLE NOW";border-color:rgba(73,190,96,.65);background:rgba(36,125,54,.16);color:#bff5c9}
/* ARVION AVAILABILITY END */
'''

css_pattern = r'/\* ARVION AVAILABILITY START \*/.*?/\* ARVION AVAILABILITY END \*/'
if re.search(css_pattern, s, flags=re.S):
    s = re.sub(css_pattern, css.strip(), s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

# Remove the old dynamic availability script. It used a MutationObserver and
# could repeatedly mutate the same modal, causing the browser to lock up.
s = re.sub(
    r'\s*<!-- ARVION AVAILABILITY SCRIPT START -->.*?<!-- ARVION AVAILABILITY SCRIPT END -->\s*',
    '\n',
    s,
    flags=re.S,
)

p.write_text(s, encoding='utf-8')
