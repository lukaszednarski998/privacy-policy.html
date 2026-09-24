from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

snake_play = 'https://play.google.com/store/apps/details?id=pl.obdstudio.retrosnakeclassic'

# Mark Retro Snake Classic as AVAILABLE NOW on the main catalog card.
pattern = r"const availableNow=\[([^\]]*)\]\.includes\(p\.id\);"
match = re.search(pattern, s)
if not match:
    raise SystemExit('Availability list was not found; index.html was left unchanged.')

items = [x.strip() for x in match.group(1).split(',') if x.strip()]
if "'snake-classic'" not in items:
    items.append("'snake-classic'")
replacement = 'const availableNow=[' + ','.join(items) + '].includes(p.id);'
s = s[:match.start()] + replacement + s[match.end():]

# Replace the obsolete non-clickable COMING SOON button in all 14 language
# descriptions with the direct Google Play listing button.
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

# Bump the marker to force browsers and GitHub Pages caches to recognize the update.
s = re.sub(
    r'<meta name="arvion-site-version" content="[^"]+">',
    '<meta name="arvion-site-version" content="2026-09-24-snake-live">',
    s,
    count=1,
)

required = [
    snake_play,
    "'snake-classic'",
    '2026-09-24-snake-live',
]
missing = [value for value in required if value not in s]
if missing:
    raise SystemExit('Retro Snake Classic update validation failed: ' + ', '.join(missing))

if s == original:
    print('Retro Snake Classic is already marked AVAILABLE NOW with Google Play buttons.')
else:
    p.write_text(s, encoding='utf-8')
    print('Retro Snake Classic marked AVAILABLE NOW with direct Google Play buttons in all 14 languages.')
