from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

# MEDIA PRO: use the final public product name everywhere in the catalog.
s = s.replace("id:'media-player',name:'Media Player'", "id:'media-player',name:'MEDIA PRO'", 1)
s = s.replace("'media-player':mkProduct({title:'Media Player'", "'media-player':mkProduct({title:'MEDIA PRO'", 1)
s = s.replace("gallery:[{src:'assets/media.webp',alt:'Media Player'}]", "gallery:[{src:'assets/media.webp',alt:'MEDIA PRO'}]", 1)

# MEDIA PRO is now publicly available on Google Play: use the direct listing URL.
old_play = 'https://play.google.com/store/search?q=ARVION%20Media%20Player&c=apps'
new_play = 'https://play.google.com/store/apps/details?id=com.obdactiveexhaust.mediapro'
if old_play in s:
    s = s.replace(old_play, new_play, 1)
elif new_play not in s:
    raise SystemExit('MEDIA PRO Google Play link target was not found; index.html was left unchanged.')

# Mark MEDIA PRO as AVAILABLE NOW while preserving all products already marked live.
pattern = r"const availableNow=\[([^\]]*)\]\.includes\(p\.id\);"
match = re.search(pattern, s)
if not match:
    raise SystemExit('Availability list was not found; index.html was left unchanged.')
items = [x.strip() for x in match.group(1).split(',') if x.strip()]
if "'media-player'" not in items:
    items.append("'media-player'")
replacement = 'const availableNow=[' + ','.join(items) + '].includes(p.id);'
s = s[:match.start()] + replacement + s[match.end():]

# Bump the page version marker so browsers/CDNs can clearly identify the update.
s = re.sub(
    r'<meta name="arvion-site-version" content="[^"]+">',
    '<meta name="arvion-site-version" content="2026-09-17-media-pro-live">',
    s,
    count=1,
)

# Sanity checks before writing anything.
required = [
    "id:'media-player',name:'MEDIA PRO'",
    "'media-player':mkProduct({title:'MEDIA PRO'",
    new_play,
    "'media-player'",
]
missing = [value for value in required if value not in s]
if missing:
    raise SystemExit('MEDIA PRO update validation failed: ' + ', '.join(missing))

if s == original:
    print('MEDIA PRO is already fully configured and available.')
else:
    p.write_text(s, encoding='utf-8')
    print('MEDIA PRO configured as AVAILABLE NOW with direct Google Play link.')
