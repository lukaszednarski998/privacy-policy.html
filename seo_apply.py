from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
BASE = "https://lukaszednarski998.github.io/privacy-policy.html"
TODAY = "2026-09-14"

apps = [
    ("obd-active-exhaust-pro", "OBD Active Exhaust Pro", "Android App", "OBD2 diagnostics Android, ELM327 live vehicle data, active exhaust control, car diagnostics app, ECU data and driver tools.", ["OBD2 diagnostics Android","ELM327 diagnostics","car diagnostics app","vehicle live data","active exhaust app","exhaust control Android","diagnostyka OBD2","aktywny wydech aplikacja"]),
    ("drive-recorder", "Drive Recorder", "Android App", "Full HD driving recorder with GPS, loop recording and road-focused tools for Android.", ["dash cam Android","driving recorder Android","GPS dashcam","loop recording dash cam","car camera app","rejestrator jazdy","kamera samochodowa telefon","nagrywanie trasy GPS"]),
    ("kalendarz-zmianowy", "Kalendarz Zmianowy", "Android App", "Shift calendar for work schedules, notes, history and everyday planning.", ["shift calendar Android","shift work calendar","work schedule app","rota planner","shift planner","kalendarz zmianowy","grafik pracy","harmonogram zmian"]),
    ("live-data-obd", "Live Data OBD", "Android App", "Real-time OBD2 and ECU vehicle parameters on Android through compatible ELM327 adapters.", ["OBD2 live data","ELM327 live data","ECU parameters Android","car sensor data","vehicle telemetry","parametry OBD na żywo","dane ECU","parametry samochodu"]),
    ("media-player", "Media Player", "Android App", "Local Android media playback with playlists, audio controls and visualizers.", ["local media player Android","offline music player","playlist player Android","audio visualizer","spectrum music player","odtwarzacz muzyki offline","lokalny odtwarzacz multimediów"]),
    ("arvion-pdf-toolbox", "ARVION PDF Toolbox Offline", "Android App", "Offline PDF editor, converter, OCR scanner and document toolbox for Android.", ["offline PDF editor Android","PDF converter Android","JPG to PDF offline","PDF to JPG Android","merge PDF","split PDF","compress PDF","OCR Android","scan to PDF","OCR to DOCX"]),
    ("arvion-phone-diagnostics", "ARVION Phone Diagnostics", "Android App", "Android diagnostics, hardware information, CPU, RAM and storage benchmarks and performance tools.", ["phone diagnostics Android","Android hardware info","CPU benchmark Android","RAM benchmark","storage benchmark","device diagnostics","phone performance test","diagnostyka telefonu"]),
    ("arvion-battery-guard", "ARVION Battery Guard", "Android App", "Battery monitoring, charging history, temperature alerts and battery-care analytics for Android.", ["battery monitor Android","battery health Android","charging history","battery temperature alert","charge limit alert","battery statistics","monitoring baterii","historia ładowania"]),
    ("arvion-calculator", "ARVION Calculator", "Android App", "Multi-calculator toolbox for Android with practical calculations and scan-assisted input.", ["calculator toolbox Android","multi calculator app","formula calculator Android","scan calculator","camera calculator","everyday calculators","kalkulatory Android","skanowanie zadania"]),
    ("private-iptv", "Private IPTV", "Android App", "Private IPTV player for user-provided M3U playlists and compatible streaming sources.", ["M3U IPTV player Android","private IPTV player","IPTV playlist player","user playlist IPTV","streaming player Android","M3U player Android","odtwarzacz IPTV"]),
    ("kids-time", "Kids Time", "Android App", "Parental time control with PIN protection, time limits, alerts and emergency access.", ["parental control Android","screen time Android","child phone timer","PIN parental control","kids time limit","parental timer app","kontrola rodzicielska","limit czasu telefonu"]),
    ("arvion-moto-speed", "ARVION Moto Speed", "Android / Wear OS", "GPS motorcycle speedometer and ride dashboard for Android phones and compatible Wear OS watches.", ["GPS motorcycle speedometer","motorcycle speedometer Android","Wear OS speedometer","GPS ride tracker","motorcycle dashboard","GPS speed tracker","motocyklowy licznik GPS"]),
    ("arvion-watch-faces", "ARVION Watch Faces", "Wear OS", "Wear OS watch faces in digital, classic, automotive, animated and artistic styles.", ["Wear OS watch faces","smartwatch watch faces","premium watch faces","digital watch face","animated watch face","automotive watch face","tarcze Wear OS"]),
    ("music-2-watch", "Music 2 Watch", "Android / Wear OS", "Music transfer and playback workflows between Android phones and compatible Wear OS smartwatches.", ["music on Wear OS","smartwatch music player","transfer music to smartwatch","phone to watch music","Wear OS music control","muzyka na zegarku","muzyka Wear OS"]),
    ("spy-2-watch", "Spy 2 Watch", "Android / Wear OS", "Phone camera preview and remote controls on a compatible Wear OS smartwatch.", ["Wear OS camera remote","phone camera preview smartwatch","smartwatch camera control","remote camera Wear OS","camera preview watch","podgląd kamery na zegarku"]),
    ("video-2-watch", "Video 2 Watch", "Android / Wear OS", "Transfer, stream and play your own video files on a compatible Wear OS smartwatch.", ["video on Wear OS","Wear OS video player","transfer video to smartwatch","smartwatch video player","phone to watch video","video streaming smartwatch","filmy na zegarku"]),
    ("checkers-royal", "Checkers Royal Game", "Android Game", "Classic checkers with AI and local play in a premium royal presentation.", ["checkers Android","checkers vs AI","two player checkers","offline checkers game","board game Android","warcaby Android","warcaby z komputerem"]),
    ("checkers-royal-wear-os", "Checkers Royal · Wear OS", "Wear OS Game", "Classic checkers designed for compatible Wear OS smartwatches.", ["checkers Wear OS","smartwatch checkers","board game smartwatch","checkers on watch","warcaby na zegarek","warcaby Wear OS"]),
    ("royal-chess", "Royal Chess", "Android Game", "Classic chess with AI, timers and a premium royal interface for Android.", ["chess Android","chess vs computer","AI chess Android","offline chess game","chess timer Android","szachy Android","szachy z komputerem"]),
    ("royal-chess-wear-os", "Royal Chess · Wear OS", "Wear OS Game", "Classic chess adapted for compatible Wear OS smartwatch displays.", ["chess Wear OS","smartwatch chess","play chess on watch","Wear OS board game","szachy na zegarek","szachy Wear OS"]),
    ("arvion-breakout-wear-os", "ARVION BREAKOUT", "Wear OS Game", "Brick-breaking arcade game created for compatible Wear OS smartwatches.", ["Breakout Wear OS","brick breaker smartwatch","brick breaking game Wear OS","smartwatch arcade game","Wear OS arcade"]),
    ("snake-wear-os", "SNAKE · Wear OS", "Wear OS Game", "Classic Snake gameplay optimized for compatible Wear OS smartwatches.", ["Snake Wear OS","smartwatch Snake game","classic Snake smartwatch","arcade game Wear OS","Snake na zegarek"]),
    ("arvion-my-pet-3d-wear-os", "ARVION MY PET 3D · Wear OS", "Wear OS Game", "A 3D virtual pet experience adapted for compatible Wear OS smartwatches.", ["virtual pet Wear OS","smartwatch virtual pet","pet game smartwatch","3D pet Wear OS","virtual animal watch game","wirtualny pupil zegarek"]),
    ("chicken-drop", "Chicken Drop", "Android Game", "Fast casual arcade gameplay for Android with simple controls and short sessions.", ["arcade game Android","casual arcade game","reflex game Android","quick mobile game","casual Android game","gra zręcznościowa Android"]),
    ("crystal-blocks", "Crystal Blocks", "Android Game", "Falling-block puzzle game with levels, combos and touch-friendly controls.", ["falling block puzzle Android","block puzzle Android","line clearing game","puzzle blocks game","falling blocks game","gra w spadające klocki"]),
    ("pixel-critters", "Pixel Critters", "Android Game", "Retro pixel-art virtual pet experience for Android.", ["virtual pet Android","pixel virtual pet","pixel art pet game","retro pet game","virtual creature Android","wirtualny pupil pixel art"]),
    ("pixel-critters-3d", "Pixel Critters 3D", "Android Game", "3D creature adventure with rooms, characters and mini-games.", ["3D virtual pet Android","creature game Android","pet adventure game","room exploration game","mini games Android","wirtualny pupil 3D"]),
    ("arvion-my-pet-3d", "ARVION MY PET 3D", "Android Game", "Interactive 3D virtual pet game with rooms, activities and animal companions.", ["3D virtual pet","pet simulator Android","virtual animal game","interactive pet game","virtual pet no ads","wirtualny pupil 3D"]),
    ("snake-classic", "Snake Classic", "Android Game", "Classic Snake game for Android with touch-friendly arcade gameplay.", ["Snake game Android","classic Snake game","offline Snake Android","arcade Snake game","touch Snake game","klasyczny Snake"]),
]


def page(slug, name, kind, desc, keywords):
    kw = ", ".join(keywords)
    canonical = f"{BASE}/apps/{slug}.html"
    json_ld = f'''{{
  "@context":"https://schema.org",
  "@type":"SoftwareApplication",
  "name":{name!r},
  "applicationCategory":{kind!r},
  "operatingSystem":"Android / Wear OS",
  "description":{desc!r},
  "url":{canonical!r},
  "author":{{"@type":"Organization","name":"ARVION"}}
}}'''.replace("'", '"')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(name)} | {escape(kind)} | ARVION</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{escape(name)} | ARVION">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<script type="application/ld+json">{json_ld}</script>
<style>body{{margin:0;background:#050505;color:#f5f5f5;font-family:Arial,sans-serif}}main{{max-width:900px;margin:auto;padding:48px 24px}}a{{color:#f1d17a}}h1{{font-size:42px;line-height:1.1}}h2{{color:#f1d17a;margin-top:34px}}p,li{{color:#c2c2c2;line-height:1.75}}.tag{{display:inline-block;border:1px solid #5f4a1c;border-radius:999px;padding:8px 12px;color:#f1d17a}}.keys{{border-top:1px solid #332b1b;margin-top:34px;padding-top:20px}}</style>
</head>
<body><main>
<p><a href="../">← ARVION apps</a> · <a href="{BASE}/">Home</a></p>
<span class="tag">{escape(kind)}</span>
<h1>{escape(name)}</h1>
<p>{escape(desc)}</p>
<h2>What this app is for</h2>
<p>{escape(desc)} ARVION focuses on practical Android and Wear OS software with clear functionality and straightforward access to official distribution where available.</p>
<div class="keys"><h2>Related searches and features</h2><p>{escape(kw)}.</p></div>
<p><a href="../">Browse all ARVION apps and games</a></p>
</main></body></html>'''

apps_dir = ROOT / "apps"
apps_dir.mkdir(exist_ok=True)

for slug, name, kind, desc, keywords in apps:
    (apps_dir / f"{slug}.html").write_text(page(slug, name, kind, desc, keywords), encoding="utf-8")

cards = "\n".join(
    f'<div class="c"><a href="{slug}.html">{escape(name)}</a><p>{escape(desc)}</p></div>'
    for slug, name, kind, desc, keywords in apps
)

apps_index = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Android & Wear OS Apps, Games and Tools | ARVION</title><meta name="description" content="ARVION Android and Wear OS apps and games: PDF and OCR tools, phone diagnostics, battery monitoring, OBD2 and ELM327, GPS motorcycle speedometer, smartwatch media, watch faces, parental controls, IPTV and mobile games."><link rel="canonical" href="{BASE}/apps/"><meta property="og:title" content="ARVION Android & Wear OS Apps"><meta property="og:description" content="Android and Wear OS tools, utilities and games across documents, diagnostics, automotive, smartwatch media and entertainment."><style>body{{margin:0;background:#050505;color:#f5f5f5;font-family:Arial,sans-serif}}.w{{max-width:1100px;margin:auto;padding:48px 24px}}a{{color:#f1d17a}}h1{{font-size:44px;line-height:1.08}}h2{{margin-top:42px;color:#f1d17a}}.lead,.topic p,.c p{{color:#bbb;line-height:1.75}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}.c{{border:1px solid #3b3320;border-radius:16px;padding:18px;background:#0b0b0b}}.c a{{font-size:20px;font-weight:700}}.topic{{border-top:1px solid #2d281b;margin-top:42px;padding-top:10px}}</style></head><body><main class="w"><p><a href="../">← ARVION home</a></p><h1>Android & Wear OS apps, tools and games</h1><p class="lead">Explore the complete ARVION catalog: offline PDF and OCR tools, Android phone diagnostics and benchmarks, battery monitoring, OBD2 and ELM327 vehicle data, GPS motorcycle tools, Wear OS watch faces, phone-to-watch music and video, parental controls, IPTV and Android or smartwatch games.</p><div class="grid">{cards}</div><section class="topic"><h2>Android apps and utilities</h2><p>ARVION covers offline document tools, calculators, battery monitoring, phone diagnostics, parental controls, media, driving tools and IPTV for user-provided sources.</p><h2>Wear OS apps and smartwatch software</h2><p>Browse watch faces, GPS motorcycle tools, phone-to-watch media workflows, camera controls and games designed for compatible Wear OS smartwatches.</p><h2>Automotive apps</h2><p>Use OBD2 and ELM327 data, live ECU parameters, active exhaust tools, driving recording and motorcycle GPS speed information.</p><h2>Games</h2><p>ARVION games include chess, checkers, Snake, Breakout, falling-block puzzles and virtual-pet experiences on Android and Wear OS.</p></section></main></body></html>'''
(apps_dir / "index.html").write_text(apps_index, encoding="utf-8")

# Improve homepage SEO without changing URL or layout.
index_path = ROOT / "index.html"
index = index_path.read_text(encoding="utf-8")
index = index.replace("<title>ARVION | Android Apps & Games</title>", "<title>ARVION Android & Wear OS Apps | OBD2, PDF, Diagnostics, Smartwatch & Games</title>")
index = index.replace('<meta name="description" content="ARVION Android apps and games.">', '<meta name="description" content="ARVION Android and Wear OS apps and games: OBD2 and ELM327 diagnostics, offline PDF and OCR tools, phone diagnostics, battery monitoring, GPS motorcycle speedometer, smartwatch media, watch faces, parental controls and mobile games.">')
if '<meta property="og:title"' not in index:
    marker = '<link rel="canonical" href="https://lukaszednarski998.github.io/privacy-policy.html/">'
    social = marker + '\n<meta property="og:title" content="ARVION Android & Wear OS Apps">\n<meta property="og:description" content="OBD2, PDF, diagnostics, battery, GPS, smartwatch media, Wear OS watch faces and Android games.">\n<meta property="og:type" content="website">\n<meta property="og:url" content="https://lukaszednarski998.github.io/privacy-policy.html/">'
    index = index.replace(marker, social)
index_path.write_text(index, encoding="utf-8")

urls = [f"{BASE}/", f"{BASE}/apps/"] + [f"{BASE}/apps/{slug}.html" for slug, *_ in apps]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for i, url in enumerate(urls):
    priority = "1.0" if i == 0 else ("0.9" if i == 1 else "0.8")
    sitemap += ["<url>", f"<loc>{url}</loc>", f"<lastmod>{TODAY}</lastmod>", "<changefreq>weekly</changefreq>", f"<priority>{priority}</priority>", "</url>"]
sitemap.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")

print(f"Generated {len(apps)} SEO product pages plus apps index and sitemap with {len(urls)} URLs.")
