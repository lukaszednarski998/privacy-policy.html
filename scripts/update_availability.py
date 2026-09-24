from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

# MEDIA PRO: use the final public product name everywhere in the catalog.
s = s.replace("id:'media-player',name:'Media Player'", "id:'media-player',name:'MEDIA PRO'", 1)
s = s.replace("'media-player':mkProduct({title:'Media Player'", "'media-player':mkProduct({title:'MEDIA PRO'", 1)
s = s.replace("gallery:[{src:'assets/media.webp',alt:'Media Player'}]", "gallery:[{src:'assets/media.webp',alt:'MEDIA PRO'}]", 1)

# MEDIA PRO is publicly available on Google Play: use the direct listing URL.
old_media_play = 'https://play.google.com/store/search?q=ARVION%20Media%20Player&c=apps'
media_play = 'https://play.google.com/store/apps/details?id=com.obdactiveexhaust.mediapro'
if old_media_play in s:
    s = s.replace(old_media_play, media_play, 1)
elif media_play not in s:
    raise SystemExit('MEDIA PRO Google Play link target was not found; index.html was left unchanged.')

# Mark all currently published products as AVAILABLE NOW.
pattern = r"const availableNow=\[([^\]]*)\]\.includes\(p\.id\);"
match = re.search(pattern, s)
if not match:
    raise SystemExit('Availability list was not found; index.html was left unchanged.')
items = [x.strip() for x in match.group(1).split(',') if x.strip()]
for product_id in ("'media-player'", "'snake-classic'"):
    if product_id not in items:
        items.append(product_id)
replacement = 'const availableNow=[' + ','.join(items) + '].includes(p.id);'
s = s[:match.start()] + replacement + s[match.end():]

# RETRO SNAKE CLASSIC is already on sale: replace the obsolete non-clickable
# COMING SOON button in every language with the direct Google Play button.
snake_play = 'https://play.google.com/store/apps/details?id=pl.obdstudio.retrosnakeclassic'
start_marker = '/* RETRO SNAKE CLASSIC SEO OVERRIDE START */'
end_marker = '/* RETRO SNAKE CLASSIC SEO OVERRIDE END */'
start = s.find(start_marker)
end = s.find(end_marker, start)
if start == -1 or end == -1:
    raise SystemExit('Retro Snake Classic override block was not found; index.html was left unchanged.')

snake_block = s[start:end]
legacy_escaped = r'<span class=\"store-button\" style=\"cursor:default\">COMING SOON · DOSTĘPNA WKRÓTCE</span>'
button_escaped = (
    r'<a class=\"store-button\" href=\"' + snake_play +
    r'\" target=\"_blank\" rel=\"noopener\">GET IT ON GOOGLE PLAY</a>'
)
legacy_plain = '<span class="store-button" style="cursor:default">COMING SOON · DOSTĘPNA WKRÓTCE</span>'
button_plain = (
    '<a class="store-button" href="' + snake_play +
    '" target="_blank" rel="noopener">GET IT ON GOOGLE PLAY</a>'
)

snake_block = snake_block.replace(legacy_escaped, button_escaped)
snake_block = snake_block.replace(legacy_plain, button_plain)
s = s[:start] + snake_block + s[end:]

if 'COMING SOON · DOSTĘPNA WKRÓTCE' in snake_block:
    raise SystemExit('At least one obsolete Retro Snake Classic COMING SOON button remains.')
if snake_block.count(snake_play) < 14:
    raise SystemExit('Retro Snake Classic Google Play buttons were not added to all 14 language versions.')

# Bump the page version marker so browsers and CDNs clearly identify the update.
s = re.sub(
    r'<meta name="arvion-site-version" content="[^"]+">',
    '<meta name="arvion-site-version" content="2026-09-24-snake-live">',
    s,
    count=1,
)

# Sanity checks before writing anything.
required = [
    "id:'media-player',name:'MEDIA PRO'",
    "'media-player':mkProduct({title:'MEDIA PRO'",
    media_play,
    snake_play,
    "'snake-classic'",
    '2026-09-24-snake-live',
]
missing = [value for value in required if value not in s]
if missing:
    raise SystemExit('Availability update validation failed: ' + ', '.join(missing))

if s == original:
    print('MEDIA PRO and Retro Snake Classic are already fully configured and available.')
else:
    p.write_text(s, encoding='utf-8')
    print('Retro Snake Classic marked AVAILABLE NOW with direct Google Play buttons in all 14 languages.')
