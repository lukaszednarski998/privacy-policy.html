from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parent
BASE = "https://lukaszednarski998.github.io/privacy-policy.html"
TODAY = "2026-09-17"

apps = [
    {"slug":"obd-active-exhaust-pro","name":"OBD Active Exhaust Pro","kind":"Android App","seo":"OBD2 Live Vehicle Data & Active Exhaust","desc":"Read live OBD2 and ELM327 vehicle data, monitor real-time parameters and use active exhaust controls and practical driver tools on Android.","pl":"Odczytuj dane OBD2 i ELM327 na żywo, monitoruj parametry pojazdu w czasie rzeczywistym i korzystaj ze sterowania aktywnym wydechem.","features":["OBD2 live vehicle data","ELM327 real-time parameters","active exhaust control","Android driver tools"]},
    {"slug":"drive-recorder","name":"Drive Recorder","kind":"Android App","seo":"Android Dash Cam with GPS & Loop Recording","desc":"Turn an Android phone into a Full HD dash cam with GPS trip information, loop recording and practical road-focused recording controls.","pl":"Używaj telefonu z Androidem jako kamery samochodowej Full HD z GPS, nagrywaniem w pętli i narzędziami do rejestracji trasy.","features":["Android dash cam","Full HD driving recorder","GPS trip information","loop recording"]},
    {"slug":"kalendarz-zmianowy","name":"Kalendarz Zmianowy","kind":"Android App","seo":"Shift Work Calendar & Schedule Planner","desc":"Plan rotating shifts, work schedules, notes and everyday duties in an Android calendar designed for shift workers and repeating work patterns.","pl":"Planuj pracę zmianową, grafik, notatki i codzienne obowiązki w kalendarzu dla systemów zmianowych i powtarzalnych cykli pracy.","features":["shift work calendar","work schedule planner","rota planning","notes and shift history"]},
    {"slug":"live-data-obd","name":"Live Data OBD","kind":"Android App","seo":"OBD2 Live Data, ECU Sensors & ELM327 Parameters","desc":"Read real-time OBD2 and ECU parameters through compatible ELM327 adapters and monitor live vehicle sensor values on Android.","pl":"Odczytuj parametry OBD2 i ECU na żywo przez kompatybilny adapter ELM327 i monitoruj bieżące dane czujników pojazdu.","features":["OBD2 live data","ELM327 live parameters","ECU sensor values","vehicle telemetry"]},
    {"slug":"media-player","name":"MEDIA PRO","kind":"Android App","seo":"Offline Music & Media Player for Android","desc":"Play local audio and media files on Android with playlists, playback controls and visualizers without relying on cloud streaming.","pl":"Odtwarzaj lokalne pliki audio i multimedia na Androidzie z playlistami, sterowaniem odtwarzaniem i wizualizacjami bez chmury.","features":["offline media player","local music playback","playlists","audio visualizer"]},
    {"slug":"arvion-pdf-toolbox","name":"ARVION PDF Toolbox Offline","kind":"Android App","seo":"Offline PDF Converter, OCR, Scanner, Merge & Split","desc":"Create, convert, merge, split and scan PDF documents offline on Android, with OCR, JPG-to-PDF and PDF-to-image tools in one app.","pl":"Twórz, konwertuj, łącz, dziel i skanuj pliki PDF offline na Androidzie. Korzystaj z OCR, JPG do PDF i konwersji PDF do obrazów.","features":["JPG to PDF offline","PDF to JPG","merge and split PDF","OCR scanner","scan to PDF"]},
    {"slug":"arvion-phone-diagnostics","name":"ARVION Phone Diagnostics","kind":"Android App","seo":"Android Phone Hardware Info, Storage, Battery & System Tools","desc":"Check Android phone hardware and system information with quick access to storage, installed apps, battery data and device-management tools.","pl":"Sprawdzaj informacje o sprzęcie i systemie telefonu oraz szybko otwieraj dane pamięci, aplikacji, baterii i narzędzia urządzenia.","features":["Android hardware information","storage information","battery information","installed apps","system tools"]},
    {"slug":"arvion-battery-guard","name":"ARVION Battery Guard","kind":"Android App","seo":"Android Battery Monitor, Charging History & Temperature","desc":"Monitor Android battery information, charging history, temperature and useful battery statistics in one practical battery dashboard.","pl":"Monitoruj baterię Androida, historię ładowania, temperaturę i przydatne statystyki dotyczące pracy i kondycji baterii.","features":["battery monitor Android","charging history","battery temperature","battery statistics"]},
    {"slug":"arvion-calculator","name":"ARVION Calculator","kind":"Android App","seo":"100 Calculators with Explanations & Camera Input","desc":"Use 100 practical Android calculators with explanations, formulas and camera-assisted input for faster everyday calculations.","pl":"Korzystaj ze 100 praktycznych kalkulatorów z objaśnieniami, wzorami i wprowadzaniem danych wspomaganym kamerą.","features":["100 calculators","formula tools","calculation explanations","camera-assisted input"]},
    {"slug":"private-iptv","name":"Private IPTV","kind":"Android App","seo":"M3U IPTV Player for Your Own Playlists on Android","desc":"Play user-provided M3U playlists and compatible streaming sources on Android in a private IPTV player designed for your own content.","pl":"Odtwarzaj własne playlisty M3U i kompatybilne źródła strumieniowe na Androidzie w prywatnym odtwarzaczu IPTV.","features":["M3U IPTV player","user-provided playlists","Android streaming player","private IPTV playback"]},
    {"slug":"kids-time","name":"Kids Time","kind":"Android App","seo":"Screen Time Limits & Parental Controls for Android","desc":"Manage child device time with PIN protection, usage limits, alerts and emergency access in a straightforward Android parental-control app.","pl":"Zarządzaj czasem korzystania z telefonu dziecka za pomocą PIN-u, limitów czasu, alertów i dostępu awaryjnego.","features":["parental control Android","screen time limits","PIN protection","child phone timer"]},
    {"slug":"arvion-moto-speed","name":"ARVION Moto Speed","kind":"Android / Wear OS","seo":"GPS Motorcycle Speedometer & Ride Dashboard","desc":"Use GPS speed information and a motorcycle-focused ride dashboard on Android phones and compatible Wear OS smartwatches.","pl":"Korzystaj z prędkości GPS i motocyklowego kokpitu na telefonie z Androidem oraz kompatybilnym zegarku Wear OS.","features":["GPS motorcycle speedometer","motorcycle dashboard","Wear OS speedometer","GPS ride information"]},
    {"slug":"arvion-watch-faces","name":"ARVION Watch Faces","kind":"Wear OS","seo":"Wear OS Watch Faces: Digital, Classic, Animated & Automotive","desc":"Browse digital, classic, automotive, animated and artistic watch faces made for compatible Wear OS smartwatches.","pl":"Wybieraj cyfrowe, klasyczne, motoryzacyjne, animowane i artystyczne tarcze dla kompatybilnych smartwatchy Wear OS.","features":["Wear OS watch faces","digital watch faces","animated watch faces","automotive watch faces"]},
    {"slug":"music-2-watch","name":"Music 2 Watch","kind":"Android / Wear OS","seo":"Transfer Music from Android Phone to Wear OS Watch","desc":"Transfer and play music between an Android phone and compatible Wear OS smartwatch with simple phone-to-watch music workflows.","pl":"Przesyłaj i odtwarzaj muzykę między telefonem z Androidem a kompatybilnym smartwatchem Wear OS.","features":["music on Wear OS","transfer music to smartwatch","phone to watch music","smartwatch music playback"]},
    {"slug":"spy-2-watch","name":"Spy 2 Watch","kind":"Android / Wear OS","seo":"Wear OS Camera Remote & Phone Camera Preview","desc":"Preview a phone camera and use remote camera controls from a compatible Wear OS smartwatch for phone-to-watch camera operation.","pl":"Wyświetlaj podgląd aparatu telefonu i korzystaj ze zdalnego sterowania kamerą na kompatybilnym zegarku Wear OS.","features":["Wear OS camera remote","phone camera preview on smartwatch","remote camera controls","smartwatch camera preview"]},
    {"slug":"video-2-watch","name":"Video 2 Watch","kind":"Android / Wear OS","seo":"Transfer & Play Videos on a Wear OS Smartwatch","desc":"Transfer, stream and play your own video files on a compatible Wear OS smartwatch from an Android phone.","pl":"Przesyłaj, strumieniuj i odtwarzaj własne pliki wideo na kompatybilnym smartwatchu Wear OS z telefonu Android.","features":["video on Wear OS","smartwatch video player","transfer video to smartwatch","phone to watch video"]},
    {"slug":"checkers-royal","name":"Checkers Royal Game","kind":"Android Game","seo":"Checkers vs AI & Local Two-Player Game for Android","desc":"Play classic checkers on Android against AI or locally with two players in a premium royal board presentation.","pl":"Graj w klasyczne warcaby na Androidzie przeciwko AI lub lokalnie w dwie osoby w królewskiej oprawie planszy.","features":["checkers Android","checkers vs AI","two-player checkers","offline board game"]},
    {"slug":"checkers-royal-wear-os","name":"Checkers Royal · Wear OS","kind":"Wear OS Game","seo":"Checkers Game for Wear OS Smartwatches","desc":"Play classic checkers directly on a compatible Wear OS smartwatch with controls adapted to a small touch display.","pl":"Graj w klasyczne warcaby bezpośrednio na kompatybilnym smartwatchu Wear OS ze sterowaniem dopasowanym do małego ekranu.","features":["checkers Wear OS","smartwatch checkers","board game on watch","warcaby na zegarek"]},
    {"slug":"royal-chess","name":"Royal Chess","kind":"Android Game","seo":"Chess vs AI with Levels & Timers on Android","desc":"Play classic chess against the computer on Android with AI levels, match timers and a premium royal interface.","pl":"Graj w klasyczne szachy przeciwko komputerowi na Androidzie, wybieraj poziom AI i korzystaj z zegarów partii.","features":["chess Android","chess vs computer","AI chess","chess timers"]},
    {"slug":"royal-chess-wear-os","name":"Royal Chess · Wear OS","kind":"Wear OS Game","seo":"Chess Game for Wear OS Smartwatches","desc":"Play classic chess directly on a compatible Wear OS smartwatch with a board and controls adapted for the watch display.","pl":"Graj w klasyczne szachy bezpośrednio na kompatybilnym smartwatchu Wear OS z planszą dopasowaną do ekranu zegarka.","features":["chess Wear OS","smartwatch chess","play chess on watch","szachy na zegarek"]},
    {"slug":"arvion-breakout-wear-os","name":"ARVION BREAKOUT","kind":"Wear OS Game","seo":"Brick Breaker Arcade Game for Wear OS Smartwatches","desc":"Play classic brick-breaking arcade action on a compatible Wear OS smartwatch with controls designed for a watch display.","pl":"Graj w klasyczną zręcznościową grę w rozbijanie cegieł na kompatybilnym smartwatchu Wear OS.","features":["brick breaker Wear OS","Breakout smartwatch game","Wear OS arcade","brick breaking game"]},
    {"slug":"snake-wear-os","name":"SNAKE · Wear OS","kind":"Wear OS Game","seo":"Classic Snake Game for Wear OS Smartwatches","desc":"Play classic Snake on a compatible Wear OS smartwatch with touch-friendly controls optimized for the wrist.","pl":"Graj w klasycznego Snake'a na kompatybilnym smartwatchu Wear OS ze sterowaniem zoptymalizowanym dla zegarka.","features":["Snake Wear OS","smartwatch Snake game","classic Snake on watch","Wear OS arcade game"]},
    {"slug":"arvion-my-pet-3d-wear-os","name":"ARVION MY PET 3D · Wear OS","kind":"Wear OS Game","seo":"3D Virtual Pet Game for Wear OS Smartwatches","desc":"Care for a 3D virtual pet on a compatible Wear OS smartwatch in a pet-game experience adapted to the watch display.","pl":"Opiekuj się wirtualnym pupilem 3D na kompatybilnym smartwatchu Wear OS w grze dostosowanej do ekranu zegarka.","features":["virtual pet Wear OS","3D pet smartwatch game","virtual animal on watch","pet game Wear OS"]},
    {"slug":"chicken-drop","name":"Chicken Drop","kind":"Android Game","seo":"Casual Reflex Arcade Game for Android","desc":"Play a fast casual Android arcade game built around simple controls, quick reactions and short mobile gaming sessions.","pl":"Graj w szybką zręcznościową grę na Androida opartą na prostym sterowaniu, refleksie i krótkich sesjach.","features":["arcade game Android","casual reflex game","quick mobile game","simple touch controls"]},
    {"slug":"crystal-blocks","name":"Crystal Blocks","kind":"Android Game","seo":"Falling Block Puzzle with Line Clearing & Combos","desc":"Arrange falling blocks, clear lines, build combos and progress through a touch-friendly crystal-themed puzzle game on Android.","pl":"Układaj spadające klocki, usuwaj linie, twórz kombosy i przechodź poziomy w kryształowej grze logicznej na Androida.","features":["falling block puzzle","block puzzle Android","line clearing game","touch puzzle game"]},
    {"slug":"pixel-critters","name":"Pixel Critters","kind":"Android Game","seo":"Pixel Art Virtual Pet Game for Android","desc":"Raise a retro pixel-art virtual pet on Android in a nostalgic creature-care game inspired by classic handheld pets.","pl":"Opiekuj się wirtualnym pupilem w stylu pixel art na Androidzie w nostalgicznej grze inspirowanej klasycznymi elektronicznymi zwierzakami.","features":["virtual pet Android","pixel art pet game","retro pet game","virtual creature"]},
    {"slug":"pixel-critters-3d","name":"Pixel Critters 3D","kind":"Android Game","seo":"3D Virtual Pet Adventure with Rooms & Mini-Games","desc":"Explore rooms, interact with 3D creatures and play mini-games in a virtual-pet adventure designed for Android.","pl":"Zwiedzaj pokoje, opiekuj się stworzeniami 3D i graj w minigry w przygodzie z wirtualnym pupilem na Androida.","features":["3D virtual pet Android","creature adventure","room exploration","mini-games"]},
    {"slug":"arvion-my-pet-3d","name":"ARVION MY PET 3D","kind":"Android Game","seo":"3D Virtual Pet Simulator with Rooms & Activities","desc":"Care for interactive 3D animal companions, move between rooms and use activities in a virtual-pet game for Android.","pl":"Opiekuj się interaktywnymi zwierzakami 3D, przechodź między pokojami i korzystaj z aktywności w grze z wirtualnym pupilem.","features":["3D virtual pet","pet simulator Android","interactive animal game","virtual pet rooms"]},
    {"slug":"snake-classic","name":"Snake Classic","kind":"Android Game","seo":"Classic Snake Arcade Game for Android","desc":"Play a modern Android version of classic Snake with simple touch-friendly arcade controls and familiar score-chasing gameplay.","pl":"Graj w nowoczesną wersję klasycznego Snake'a na Androidzie z prostym sterowaniem dotykowym i biciem rekordów.","features":["Snake game Android","classic Snake","offline arcade game","touch Snake game"]},
]


def os_for(kind):
    if kind in ("Wear OS", "Wear OS Game"):
        return "Wear OS"
    if "Android / Wear OS" in kind:
        return "Android, Wear OS"
    return "Android"


def category_for(kind):
    return "GameApplication" if "Game" in kind else "UtilitiesApplication"


def related_apps(app, limit=4):
    same_group = [a for a in apps if a["slug"] != app["slug"] and ("Game" in a["kind"]) == ("Game" in app["kind"])]
    return same_group[:limit]


def app_page(app):
    canonical = f"{BASE}/apps/{app['slug']}.html"
    title = f"{app['seo']} | {app['name']}"
    software_schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": app["name"],
        "applicationCategory": category_for(app["kind"]),
        "operatingSystem": os_for(app["kind"]),
        "description": app["desc"],
        "url": canonical,
        "author": {"@type": "Organization", "name": "ARVION"},
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type":"ListItem","position":1,"name":"Android & Wear OS apps","item":f"{BASE}/"},
            {"@type":"ListItem","position":2,"name":"Apps by function","item":f"{BASE}/apps/"},
            {"@type":"ListItem","position":3,"name":app["seo"],"item":canonical},
        ],
    }
    feature_html = "\n".join(f"<li>{escape(item)}</li>" for item in app["features"])
    related_html = "\n".join(
        f'<li><a href="{escape(r["slug"])}.html">{escape(r["seo"])}</a></li>'
        for r in related_apps(app)
    )
    use_cases = ", ".join(app["features"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(app['desc'])}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(app['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(app['desc'])}">
<script type="application/ld+json">{json.dumps(software_schema, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(breadcrumb_schema, ensure_ascii=False)}</script>
<style>body{{margin:0;background:#050505;color:#f5f5f5;font-family:Arial,sans-serif}}main{{max-width:900px;margin:auto;padding:48px 24px}}a{{color:#f1d17a}}h1{{font-size:42px;line-height:1.1;margin-bottom:10px}}h2{{color:#f1d17a;margin-top:34px}}p,li{{color:#c2c2c2;line-height:1.75}}.tag{{display:inline-block;border:1px solid #5f4a1c;border-radius:999px;padding:8px 12px;color:#f1d17a}}.appname{{font-size:18px;color:#f1d17a;margin-top:0}}.pl,.related{{border-top:1px solid #332b1b;margin-top:34px;padding-top:20px}}</style>
</head>
<body><main>
<p><a href="../">← Android &amp; Wear OS apps</a> · <a href="./">Apps by function</a></p>
<span class="tag">{escape(app['kind'])}</span>
<h1>{escape(app['seo'])}</h1>
<p class="appname">{escape(app['name'])}</p>
<p>{escape(app['desc'])}</p>
<h2>What this app does</h2>
<ul>{feature_html}</ul>
<p>Useful for people looking for {escape(use_cases)} on {escape(os_for(app['kind']))}.</p>
<section class="pl" lang="pl">
<h2>Funkcje aplikacji</h2>
<p>{escape(app['pl'])}</p>
<ul>{feature_html}</ul>
</section>
<section class="related">
<h2>Related Android &amp; Wear OS apps</h2>
<ul>{related_html}</ul>
<p><a href="./">Browse all apps by function</a> · <a href="../">ARVION app catalog</a></p>
</section>
</main></body></html>'''


apps_dir = ROOT / "apps"
apps_dir.mkdir(exist_ok=True)
for app in apps:
    (apps_dir / f"{app['slug']}.html").write_text(app_page(app), encoding="utf-8")

cards = "\n".join(
    f'<article class="c"><a href="{a["slug"]}.html">{escape(a["seo"])}</a><strong>{escape(a["name"])}</strong><p>{escape(a["desc"])}</p><p class="uses">Functions: {escape(", ".join(a["features"]))}</p></article>'
    for a in apps
)
item_schema = json.dumps({
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": a["seo"], "url": f"{BASE}/apps/{a['slug']}.html"}
        for i, a in enumerate(apps)
    ],
}, ensure_ascii=False)

apps_index = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Android &amp; Wear OS Apps by Function: OBD2, PDF OCR, GPS, Watch Tools &amp; Games</title>
<meta name="description" content="Find Android and Wear OS apps by function: OBD2 live data, ELM327, offline PDF OCR, battery monitor, GPS speedometer, smartwatch media, watch faces and games.">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{BASE}/apps/">
<meta property="og:title" content="Android & Wear OS Apps by Function | OBD2, PDF, GPS, Watch Tools & Games">
<meta property="og:description" content="Browse apps by what they do: OBD2 live data, ELM327, offline PDF/OCR, battery, GPS motorcycle speed, Wear OS media, watch faces and games.">
<meta property="og:type" content="website"><meta property="og:url" content="{BASE}/apps/">
<script type="application/ld+json">{item_schema}</script>
<style>body{{margin:0;background:#050505;color:#f5f5f5;font-family:Arial,sans-serif}}.w{{max-width:1100px;margin:auto;padding:48px 24px}}a{{color:#f1d17a}}h1{{font-size:44px;line-height:1.08}}h2{{margin-top:42px;color:#f1d17a}}.lead,.topic p,.c p{{color:#bbb;line-height:1.75}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}.c{{border:1px solid #3b3320;border-radius:16px;padding:18px;background:#0b0b0b}}.c a{{display:block;font-size:20px;font-weight:700;margin-bottom:7px}}.c strong{{display:block;color:#eee;font-size:13px}}.c .uses{{font-size:12px;color:#999}}.topic{{border-top:1px solid #2d281b;margin-top:42px;padding-top:10px}}</style>
</head><body><main class="w">
<p><a href="../">← ARVION home</a></p>
<h1>Android &amp; Wear OS apps by function</h1>
<p class="lead">Find apps by what you need: OBD2 and ELM327 live vehicle data, active exhaust controls, Android dash cam recording, offline PDF conversion and OCR, phone hardware information, battery monitoring, GPS motorcycle speed, Wear OS watch faces, phone-to-watch music and video, parental controls, IPTV and mobile games.</p>
<section class="topic">
<h2>OBD2, ELM327 and automotive apps</h2><p>Live OBD2 data, ECU sensor parameters, active exhaust controls, Android dash cam recording and GPS motorcycle speed tools.</p>
<h2>PDF, OCR, phone and battery tools</h2><p>Offline JPG to PDF, PDF to JPG, merge and split PDF, OCR scanning, Android hardware information, storage, battery temperature and charging history.</p>
<h2>Wear OS and smartwatch apps</h2><p>Wear OS watch faces, music and video transfer, camera remote controls, GPS speed information and smartwatch games.</p>
<h2>Android and Wear OS games</h2><p>Chess, checkers, Snake, Breakout, falling-block puzzles, arcade games and 3D or pixel-art virtual pets.</p>
<section lang="pl"><h2>Aplikacje według funkcji</h2><p>Znajdziesz tu odczyt danych OBD2 i ELM327 na żywo, narzędzia PDF i OCR offline, monitoring baterii, informacje o telefonie, licznik GPS na motocykl, aplikacje Wear OS oraz gry na telefon i smartwatch.</p></section>
</section>
<div class="grid">{cards}</div>
</main></body></html>'''
(apps_dir / "index.html").write_text(apps_index, encoding="utf-8")

# Homepage SEO head only: keep the existing visual catalog untouched.
index_path = ROOT / "index.html"
index = index_path.read_text(encoding="utf-8")
home_title = "Android & Wear OS Apps: OBD2 Live Data, PDF OCR, GPS & Watch Tools"
home_desc = "Android and Wear OS apps for OBD2 and ELM327 live data, offline PDF OCR, phone and battery tools, GPS motorcycle speed, smartwatch media, watch faces and games."
index = re.sub(r"<title>.*?</title>", f"<title>{home_title}</title>", index, count=1, flags=re.S)
index = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{home_desc}">', index, count=1)
index = re.sub(r"\n?<!-- ARVION SEO HEAD START -->.*?<!-- ARVION SEO HEAD END -->\n?", "\n", index, flags=re.S)
home_schema = json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Android & Wear OS Apps by Function","url":f"{BASE}/","publisher":{"@type":"Organization","name":"ARVION"}}, ensure_ascii=False)
home_items = json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a["seo"],"url":f"{BASE}/apps/{a['slug']}.html"} for i,a in enumerate(apps)]}, ensure_ascii=False)
seo_head = f'''<!-- ARVION SEO HEAD START -->
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{BASE}/">
<meta property="og:title" content="{home_title}">
<meta property="og:description" content="{home_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{home_title}">
<meta name="twitter:description" content="{home_desc}">
<script type="application/ld+json">{home_schema}</script>
<script type="application/ld+json">{home_items}</script>
<!-- ARVION SEO HEAD END -->'''
needle = f'<meta name="description" content="{home_desc}">'
if needle in index:
    index = index.replace(needle, needle + "\n" + seo_head, 1)
else:
    index = index.replace("<style>", seo_head + "\n<style>", 1)
index_path.write_text(index, encoding="utf-8")

# Keep both sitemap filenames synchronized. Search Console currently uses sitemap-google.xml.
urls = [f"{BASE}/", f"{BASE}/apps/"] + [f"{BASE}/apps/{a['slug']}.html" for a in apps]
sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    sitemap_lines += ["  <url>", f"    <loc>{url}</loc>", f"    <lastmod>{TODAY}</lastmod>", "  </url>"]
sitemap_lines.append("</urlset>")
sitemap_text = "\n".join(sitemap_lines) + "\n"
(ROOT / "sitemap.xml").write_text(sitemap_text, encoding="utf-8")
(ROOT / "sitemap-google.xml").write_text(sitemap_text, encoding="utf-8")
(ROOT / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\nSitemap: {BASE}/sitemap-google.xml\n",
    encoding="utf-8",
)

print(f"Generated {len(apps)} function-first SEO pages and {len(urls)} sitemap URLs.")
