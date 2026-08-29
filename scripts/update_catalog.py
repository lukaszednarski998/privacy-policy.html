from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# ARVION catalog rebuild.
# The images referenced below are the ORIGINAL PNG files extracted from the
# user's split archive. This script never resizes, converts or recompresses them.

css_block = r'''
/* ARVION CATALOG LAYOUT START */
.catalog-section{padding:42px 0 46px}.catalog-section+.catalog-section{padding-top:16px}.catalog-section .section-head{padding-bottom:3px}.catalog-section .section-note{color:#9f9f9f}.catalog-divider{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);width:min(1220px,calc(100% - 32px));margin:0 auto}.image-placeholder{color:#6f6f6f;font-size:12px;font-weight:800;letter-spacing:.16em;text-align:center;padding:24px}.product-head.no-image{grid-template-columns:1fr}.gallery-main.empty-gallery:after{content:'NEW IMAGES COMING SOON';color:#6f6f6f;font-size:12px;font-weight:800;letter-spacing:.16em;text-align:center;padding:24px}.gallery-main.empty-gallery img{display:none}
/* ARVION CATALOG LAYOUT END */
'''
if '/* ARVION CATALOG LAYOUT START */' in s:
    s = re.sub(r'/\* ARVION CATALOG LAYOUT START \*/.*?/\* ARVION CATALOG LAYOUT END \*/\n?', css_block, s, count=1, flags=re.S)
else:
    # Remove the temporary placeholder-only style if it is present.
    s = re.sub(r'\n\.image-placeholder\{.*?\.gallery-main\.empty-gallery img\{display:none\}\n', '\n', s, count=1, flags=re.S)
    s = s.replace('</style>', css_block + '\n</style>', 1)

# Header navigation.
s = re.sub(
    r'<nav>.*?</nav>',
    '<nav><a href="#phone-apps">Phone Apps</a><a href="#watch-apps">Watch Apps</a><a href="#games">Games</a><a href="#promise">Our promise</a></nav>',
    s,
    count=1,
    flags=re.S,
)


# Keep Contact action in the header next to Support.
if 'id="contactOpen"' not in s:
    s = s.replace('<button class="support-link" id="supportOpen" type="button">Support</button>', '<button class="support-link" id="contactOpen" type="button">Contact</button><button class="support-link" id="supportOpen" type="button">Support</button>', 1)

# Replace the old single filterable catalog with three fixed sections.
catalog_html = r'''<section id="phone-apps" class="catalog-section"><div class="wrap"><div class="section-head"><div><div class="eyebrow">Android smartphones</div><h2>Phone Apps</h2></div><p class="section-note">Android applications for driving, media, diagnostics and everyday tools. Apps that work together with Wear OS are also shown here because they include a phone application. Open a product to view original screenshots, Polish/English descriptions and Google Play access.</p></div><div class="grid" id="phoneGrid"></div></div></section>
<div class="catalog-divider"></div>
<section id="watch-apps" class="catalog-section"><div class="wrap"><div class="section-head"><div><div class="eyebrow">Wear OS</div><h2>Watch Apps</h2></div><p class="section-note">Applications and watch software designed for compatible Wear OS smartwatches and phone-to-watch workflows. Products with both phone and watch components are intentionally listed in both sections.</p></div><div class="grid" id="watchGrid"></div></div></section>
<div class="catalog-divider"></div>
<section id="games" class="catalog-section"><div class="wrap"><div class="section-head"><div><div class="eyebrow">ARVION Games</div><h2>Games</h2></div><p class="section-note">Android and Wear OS games with no advertising and no recurring subscriptions. Wear OS editions are listed separately where supplied.</p></div><div class="grid" id="gameGrid"></div></div></section>'''
s, n = re.subn(r'<section id="apps">.*?</section>\n<div class="quality"', catalog_html + '\n<div class="quality"', s, count=1, flags=re.S)
if n != 1 and 'id="phone-apps"' not in s:
    raise SystemExit('Could not replace catalog section')

# Product cards in the requested order: phone apps, watch apps, then games.
base = 'assets/imported-new-products/STRONA INTERNETOWA/'
products_js = f'''const products=[
{{id:'obd',name:'OBD Active Exhaust Pro',type:'phone',tag:'Android App',img:'{base}OBD GLOWNA/OBD 1.png',desc:'Active exhaust, diagnostics, live vehicle data and driver tools.',details:true}},
{{id:'drive-recorder',name:'Drive Recorder',type:'phone',tag:'Android App',img:'{base}REJESTRATOR JAZDY/REJESTRATOR 1.png',desc:'Full HD driving recorder with GPS and loop recording.',details:true}},
{{id:'kalendarz-zmianowy',name:'Kalendarz Zmianowy',type:'phone',tag:'Android App',img:'{base}KALENDARZ ZMIAN/KALENDARZ ZMIAN 1.png',desc:'Shift calendar with schedules, notes and work information.',details:true}},
{{id:'live-data',name:'Live Data',type:'phone',tag:'Android App',img:'{base}LIVE DATA/LIVE DATA 1.png',desc:'Real-time vehicle parameters through compatible OBD/ELM327.',details:true}},
{{id:'media-player',name:'Media Player',type:'phone',tag:'Android App',img:'{base}MEDIA/MEDIA 1.png',desc:'Local media playback with playlists and visualizers.',details:true}},
{{id:'watch-faces',name:'ARVION Watch Faces',type:'watch',tag:'Phone · Wear OS',img:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 1.png',desc:'Premium watch faces managed from Android for compatible Wear OS smartwatches.',details:true}},
{{id:'music-2-watch',name:'Music 2 Watch',type:'watch',tag:'Phone · Wear OS',img:'{base}MUSIC 2 WATCH/MUSIC 2 WATCH 1.png',desc:'Music features connecting Android phone and smartwatch.',details:true}},
{{id:'spy-2-watch',name:'Spy 2 Watch',type:'watch',tag:'Phone · Wear OS',img:'{base}SPY 2 WATCH/SPY 2 WATCH 1.png',desc:'Phone-camera preview and controls designed for smartwatch use.',details:true}},
{{id:'video-2-watch',name:'Video 2 Watch',type:'watch',tag:'Phone · Wear OS',img:'{base}VIDEO 2 WATCH/VIDEO 2 WATCH 1.png',desc:'Transfer and play your own videos on a compatible smartwatch.',details:true}},
{{id:'checkers-royal',name:'Checkers Royal Game',type:'game',tag:'Android Game',img:'{base}WARCABY/WARCABY 1.png',desc:'Royal checkers for Android with a premium board presentation.',details:true}},
{{id:'checkers-royal-watch',name:'Checkers Royal · Wear OS',type:'game',tag:'Wear OS Game',img:'{base}WARCABY NA ZEGAREK/WARCABY 1.png',desc:'Royal checkers designed specifically for compatible Wear OS watches.',details:true}},
{{id:'royal-chess',name:'Royal Chess',type:'game',tag:'Android Game',img:'{base}SZACHY/SZACHY 1.png',desc:'Classic chess with AI in a premium royal presentation.',details:true}},
{{id:'royal-chess-watch',name:'Royal Chess · Wear OS',type:'game',tag:'Wear OS Game',img:'{base}SZACHY NA ZEGAREK/SZACHY NA ZEGAREK 1.png',desc:'Classic chess adapted for play directly on a compatible Wear OS watch.',details:true}},
{{id:'chicken-drop',name:'Chicken Drop',type:'game',tag:'Android Game',img:'{base}CHICKEN DROP/CHICKEN DROP 1.png',desc:'Fast and simple arcade gameplay for Android.',details:true}},
{{id:'crystal-blocks',name:'Crystal Blocks',type:'game',tag:'Android Game',img:'{base}CRYSTAL BLOCKS/CRYSTAL BLOCKS 1.png',desc:'A crystal-themed falling-block puzzle game.',details:true}},
{{id:'pixel-critters',name:'Pixel Critters',type:'game',tag:'Android Game',img:'{base}PIXEL CRITERS 1.0/PIXEL CRITERS 1.0 1.png',desc:'A retro pixel virtual-pet experience for Android.',details:true}},
{{id:'pixel-critters-3d',name:'Pixel Critters 3D',type:'game',tag:'Android Game',img:'{base}PIXEL CRITTERS 3 D/PIXEL CRITERS 3 D 1.png',desc:'A 3D creature adventure with rooms and mini-games.',details:true}},
{{id:'snake-classic',name:'Snake Classic',type:'game',tag:'Android Game',img:'{base}SNAKE/snake 1.png',desc:'A modern Android edition of the classic Snake game.',details:true}}
];'''
s, n = re.subn(r'const products=\[\n.*?\n\];', products_js, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace products array')

# Remove the old temporary global image wipe.
s = s.replace("products.forEach(p=>{p.img=''});Object.values(productData).forEach(p=>{p.icon='';p.gallery=[]});\n", '')

# Add/refresh the original-image galleries and two new Wear OS game detail records.
original_block = f'''// ARVION ORIGINAL IMAGE CATALOG START
productData['checkers-royal-watch']=mkProduct({{title:'Checkers Royal · Wear OS',icon:'',enSub:'Royal checkers designed for compatible Wear OS smartwatches.',plSub:'Królewskie warcaby zaprojektowane dla kompatybilnych smartwatchy Wear OS.',en:'Play classic checkers directly on your wrist in a royal black, gold and emerald presentation. The Wear OS edition uses touch controls adapted to a smartwatch display and is intended for quick games without reaching for the phone.',pl:'Graj w klasyczne warcaby bezpośrednio na nadgarstku w królewskiej czarno-złoto-szmaragdowej oprawie. Wersja Wear OS wykorzystuje sterowanie dotykowe dopasowane do ekranu smartwatcha i pozwala rozgrywać partie bez sięgania po telefon.',gallery:[],play:'https://play.google.com/store/apps/details?id=com.aplikacjeandroid.checkersroyalgame',noteEn:'Wear OS edition for compatible smartwatches.',notePl:'Wersja Wear OS dla kompatybilnych smartwatchy.'}});
productData['royal-chess-watch']=mkProduct({{title:'Royal Chess · Wear OS',icon:'',enSub:'Classic chess adapted for compatible Wear OS smartwatches.',plSub:'Klasyczne szachy dostosowane do kompatybilnych smartwatchy Wear OS.',en:'Take Royal Chess to your wrist. The Wear OS edition presents the chessboard and controls in a layout adapted to a smartwatch display so you can play classic chess directly on a compatible watch.',pl:'Przenieś Royal Chess na nadgarstek. Wersja Wear OS prezentuje szachownicę i sterowanie w układzie dopasowanym do ekranu smartwatcha, dzięki czemu możesz grać w klasyczne szachy bezpośrednio na kompatybilnym zegarku.',gallery:[],play:'https://play.google.com/store/search?q=Royal%20Chess%20ARVION&c=apps',noteEn:'Wear OS edition for compatible smartwatches.',notePl:'Wersja Wear OS dla kompatybilnych smartwatchy.'}});
const originalCatalogBase='{base}';
const originalCatalog={{
'obd':['OBD GLOWNA/OBD 1.png','OBD GLOWNA/OBD 2.png','OBD GLOWNA/OBD 3.png'],
'drive-recorder':['REJESTRATOR JAZDY/REJESTRATOR 1.png','REJESTRATOR JAZDY/REJESTRATOR 2.png','REJESTRATOR JAZDY/REJESTRATOR 3.png'],
'kalendarz-zmianowy':['KALENDARZ ZMIAN/KALENDARZ ZMIAN 1.png','KALENDARZ ZMIAN/KALENDARZ ZMIAN 2.png','KALENDARZ ZMIAN/KALENDARZ ZMIAN 3.png'],
'live-data':['LIVE DATA/LIVE DATA 1.png','LIVE DATA/LIVE DATA 2.png','LIVE DATA/LIVE DATA 3.png'],
'media-player':['MEDIA/MEDIA 1.png','MEDIA/MEDIA 2.png','MEDIA/MEDIA 3.png'],
'music-2-watch':['MUSIC 2 WATCH/MUSIC 2 WATCH 1.png','MUSIC 2 WATCH/MUSIC 2 WATCH 2.png','MUSIC 2 WATCH/MUSIC 2 WATCH 3.png'],
'spy-2-watch':['SPY 2 WATCH/SPY 2 WATCH 1.png','SPY 2 WATCH/SPY 2 WATCH 2.png','SPY 2 WATCH/SPY 2 WATCH 3.png'],
'video-2-watch':['VIDEO 2 WATCH/VIDEO 2 WATCH 1.png','VIDEO 2 WATCH/VIDEO 2 WATCH 2.png','VIDEO 2 WATCH/VIDEO 2 WATCH 3.png'],
'checkers-royal':['WARCABY/WARCABY 1.png','WARCABY/WARCABY 2.png','WARCABY/WARCABY 3.png'],
'checkers-royal-watch':['WARCABY NA ZEGAREK/WARCABY 1.png','WARCABY NA ZEGAREK/WARCABY 2.png','WARCABY NA ZEGAREK/WARCABY 3.png'],
'royal-chess':['SZACHY/SZACHY 1.png','SZACHY/SZACHY 2.png','SZACHY/SZACHY 3.png'],
'royal-chess-watch':['SZACHY NA ZEGAREK/SZACHY NA ZEGAREK 1.png','SZACHY NA ZEGAREK/SZACHY NA ZEGAREK 2.png','SZACHY NA ZEGAREK/SZACHY NA ZEGAREK 3.png'],
'chicken-drop':['CHICKEN DROP/CHICKEN DROP 1.png','CHICKEN DROP/CHICKEN DROP 2.png','CHICKEN DROP/CHICKEN DROP 3.png'],
'crystal-blocks':['CRYSTAL BLOCKS/CRYSTAL BLOCKS 1.png','CRYSTAL BLOCKS/CRYSTAL BLOCKS 2.png','CRYSTAL BLOCKS/CRYSTAL BLOCKS 3.png'],
'pixel-critters':['PIXEL CRITERS 1.0/PIXEL CRITERS 1.0 1.png','PIXEL CRITERS 1.0/PIXEL CRITERS 1.0 2.png','PIXEL CRITERS 1.0/PIXEL CRITERS 1.0 3.png'],
'pixel-critters-3d':['PIXEL CRITTERS 3 D/PIXEL CRITERS 3 D 1.png','PIXEL CRITTERS 3 D/PIXEL CRITERS 3 D 2.png','PIXEL CRITTERS 3 D/PIXEL CRITERS 3 D 3.png'],
'snake-classic':['SNAKE/snake 1.png','SNAKE/snake 2.png','SNAKE/snake 3.png']
}};
Object.entries(originalCatalog).forEach(([id,files])=>{{const data=productData[id];if(!data)return;data.icon=originalCatalogBase+files[0];data.gallery=files.map((src,i)=>({{src:originalCatalogBase+src,alt:`${{data.title}} original image ${{i+1}}`}}));}});
productData['watch-faces'].icon='assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 1.png';productData['watch-faces'].gallery=[{{src:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 1.png',alt:'ARVION Watch Faces original image 1'}},{{src:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 2.png',alt:'ARVION Watch Faces original image 2'}},{{src:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 3.png',alt:'ARVION Watch Faces original image 3'}},{{src:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 4.png',alt:'ARVION Watch Faces original image 4'}},{{src:'assets/imported-new-products/ARVION WATCH FACE/ARVION WATCH FACE/ARVION WATCH FACE 5.png',alt:'ARVION Watch Faces original image 5'}}];
// ARVION ORIGINAL IMAGE CATALOG END
'''
if '// ARVION ORIGINAL IMAGE CATALOG START' in s:
    s = re.sub(r'// ARVION ORIGINAL IMAGE CATALOG START.*?// ARVION ORIGINAL IMAGE CATALOG END\n?', original_block, s, count=1, flags=re.S)
else:
    s = s.replace('const supportCopy=', original_block + 'const supportCopy=', 1)

# Three destination grids instead of one filterable grid.
s = s.replace(
    "const grid=document.getElementById('grid'),productModal=",
    "const grids={phone:document.getElementById('phoneGrid'),watch:document.getElementById('watchGrid'),game:document.getElementById('gameGrid')},productModal=",
    1,
)

# Phone + Wear OS applications intentionally appear in both Phone Apps and Watch Apps.
render_js = r'''function render(){Object.entries(grids).forEach(([type,grid])=>{const list=products.filter(p=>type==='phone'?(p.type==='phone'||p.type==='watch'):p.type===type);grid.innerHTML=list.map(p=>`<article class="card${p.details?' details':''}" ${p.details?`tabindex="0" role="button" data-product="${p.id}" aria-label="Open ${p.name}"`:''}><div class="pic">${p.img?`<img src="${p.img}" alt="${p.name}" loading="lazy">`:'<span class="image-placeholder">NEW IMAGES COMING SOON</span>'}${p.details?'<span class="details-badge">View details</span>':''}</div><div class="body"><span class="tag">${p.tag}</span><h3>${p.name}</h3><p>${p.desc}</p></div></article>`).join('')});document.querySelectorAll('[data-product]').forEach(c=>{c.onclick=()=>openProduct(c.dataset.product);c.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openProduct(c.dataset.product)}}})}'''
s, n = re.subn(r"function render\(filter='all'\)\{.*?\}\nasync function buildGallery", render_js + '\nasync function buildGallery', s, count=1, flags=re.S)
if n != 1:
    s, n = re.subn(r"function render\(\)\{.*?\}\nasync function buildGallery", render_js + '\nasync function buildGallery', s, count=1, flags=re.S)
if n != 1 and "type==='phone'?(p.type==='phone'||p.type==='watch')" not in s:
    raise SystemExit('Could not patch render()')

# Remove obsolete filter click handlers.
s = s.replace("document.querySelectorAll('.filter').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');render(b.dataset.filter)});", '')

# Show the correct platform label in each product detail window.
old_open = "async function openProduct(id){currentProduct=id;const data=productData[id];document.getElementById('productTitle').textContent=data.title;"
new_open = "async function openProduct(id){currentProduct=id;const data=productData[id];const cardData=products.find(p=>p.id===id);document.getElementById('productEyebrow').textContent=cardData?cardData.tag:'ARVION';document.getElementById('productTitle').textContent=data.title;"
s = s.replace(old_open, new_open, 1)

p.write_text(s, encoding='utf-8')
print('ARVION catalog rebuilt: Phone Apps includes phone + Wear OS companion apps; Watch Apps keeps the Wear OS subset; Games remain separate.')
