from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
BASE = 'assets/games-20260911/'

old_card = "{id:'arvion-my-pet-3d',name:'ARVION MY PET 3D',type:'game',tag:'Android Game',img:'',desc:'A 3D virtual pet game with interactive rooms, activities and animal companions.',details:true},"
new_card = "{id:'arvion-my-pet-3d',name:'ARVION MY PET 3D',type:'game',tag:'Android Game',img:'" + BASE + "phone/arvion-my-pet-3d/icon.png',desc:'A 3D virtual pet game with interactive rooms, activities and animal companions.',details:true},"
s = s.replace(old_card, new_card)

if "id:'arvion-breakout-watch'" not in s:
    anchor = "{id:'royal-chess-watch',name:'Royal Chess · Wear OS',type:'watchgame',tag:'Wear OS Game',img:'assets/imported-new-products/STRONA INTERNETOWA/SZACHY NA ZEGAREK/SZACHY NA ZEGAREK 1.png',desc:'Classic chess adapted for play directly on a compatible Wear OS watch.',details:true},"
    extra = "\n".join([
        anchor,
        "{id:'arvion-breakout-watch',name:'ARVION BREAKOUT',type:'watchgame',tag:'Wear OS Game',img:'" + BASE + "watch/arvion-breakout/screen-1.png',desc:'Classic brick-breaking arcade action designed for Wear OS smartwatches.',details:true},",
        "{id:'arvion-my-pet-3d-watch',name:'ARVION MY PET 3D · Wear OS',type:'watchgame',tag:'Wear OS Game',img:'" + BASE + "watch/arvion-my-pet-3d/icon.png',desc:'Your virtual 3D pet adapted for a compatible Wear OS smartwatch.',details:true},",
        "{id:'snake-watch',name:'SNAKE · Wear OS',type:'watchgame',tag:'Wear OS Game',img:'" + BASE + "watch/snake/screen-1.png',desc:'Classic Snake gameplay optimized for a smartwatch display.',details:true},"
    ])
    if anchor not in s:
        raise SystemExit('Royal Chess Wear OS card anchor not found')
    s = s.replace(anchor, extra, 1)

phone_pat = re.compile(r"productData\['arvion-my-pet-3d'\]=mkProduct\(\{.*?\}\);", re.S)
phone_new = "productData['arvion-my-pet-3d']=mkProduct({title:'ARVION MY PET 3D',icon:'" + BASE + "phone/arvion-my-pet-3d/icon.png',enSub:'Your interactive 3D virtual pet on Android.',plSub:'Twój interaktywny wirtualny pupil 3D na Androidzie.',en:'ARVION MY PET 3D is a virtual pet experience in a full 3D environment. Take care of your pet, watch its behavior, enjoy interactive moments and explore its world. The game is designed for simple, friendly play without ads or recurring subscriptions.',pl:'ARVION MY PET 3D to wirtualny pupil w pełnym środowisku 3D. Opiekuj się swoim zwierzakiem, obserwuj jego zachowanie, korzystaj z interakcji i odkrywaj jego świat. Gra została przygotowana do prostej, przyjaznej rozgrywki bez reklam i bez cyklicznych subskrypcji.',gallery:[{src:'" + BASE + "phone/arvion-my-pet-3d/screen-1.png',alt:'ARVION MY PET 3D screenshot 1'},{src:'" + BASE + "phone/arvion-my-pet-3d/screen-2.png',alt:'ARVION MY PET 3D screenshot 2'},{src:'" + BASE + "phone/arvion-my-pet-3d/screen-3.png',alt:'ARVION MY PET 3D screenshot 3'},{src:'" + BASE + "phone/arvion-my-pet-3d/demo.mp4',alt:'ARVION MY PET 3D gameplay video'}],play:'https://play.google.com/store/search?q=ARVION%20MY%20PET%203D&c=apps',noteEn:'Android phone game.',notePl:'Gra na telefon z Androidem.'});"
s, n = phone_pat.subn(phone_new, s, count=1)
if n != 1:
    raise SystemExit('Phone My Pet product data not found')

if "productData['arvion-breakout-watch']" not in s:
    marker = '// ARVION ORIGINAL IMAGE CATALOG START'
    block = """
productData['arvion-breakout-watch']=mkProduct({title:'ARVION BREAKOUT',icon:'assets/games-20260911/watch/arvion-breakout/screen-1.png',enSub:'Classic brick-breaking arcade action on your Wear OS watch.',plSub:'Klasyczna zręcznościowa rozgrywka Breakout na zegarku Wear OS.',en:'ARVION BREAKOUT is a classic arcade game created for smartwatch play. Bounce the ball, destroy blocks and chase higher scores with controls and a layout adapted to a compatible Wear OS display.',pl:'ARVION BREAKOUT to klasyczna gra zręcznościowa przygotowana do grania na smartwatchu. Odbijaj piłkę, niszcz kolejne bloki i poprawiaj rekordy, korzystając ze sterowania i układu dopasowanego do kompatybilnego ekranu Wear OS.',gallery:[{src:'assets/games-20260911/watch/arvion-breakout/screen-1.png',alt:'ARVION BREAKOUT screenshot 1'},{src:'assets/games-20260911/watch/arvion-breakout/screen-2.png',alt:'ARVION BREAKOUT screenshot 2'}],play:'https://play.google.com/store/search?q=ARVION%20BREAKOUT&c=apps',noteEn:'Wear OS game for compatible smartwatches.',notePl:'Gra Wear OS dla kompatybilnych smartwatchy.'});
productData['arvion-my-pet-3d-watch']=mkProduct({title:'ARVION MY PET 3D · Wear OS',icon:'assets/games-20260911/watch/arvion-my-pet-3d/icon.png',enSub:'Keep your virtual 3D pet close on a compatible Wear OS watch.',plSub:'Miej swojego wirtualnego pupila 3D zawsze przy sobie na Wear OS.',en:'ARVION MY PET 3D for smartwatch brings the virtual pet experience to your wrist. Check on your pet directly on a compatible Wear OS watch and enjoy a compact interface prepared for the smaller display.',pl:'ARVION MY PET 3D w wersji zegarkowej przenosi wirtualnego pupila na Twój nadgarstek. Sprawdzaj swojego zwierzaka bezpośrednio na kompatybilnym zegarku Wear OS i korzystaj z interfejsu przygotowanego do mniejszego ekranu.',gallery:[{src:'assets/games-20260911/watch/arvion-my-pet-3d/screen-1.png',alt:'ARVION MY PET 3D Wear OS screenshot 1'},{src:'assets/games-20260911/watch/arvion-my-pet-3d/screen-2.png',alt:'ARVION MY PET 3D Wear OS screenshot 2'},{src:'assets/games-20260911/watch/arvion-my-pet-3d/screen-3.png',alt:'ARVION MY PET 3D Wear OS screenshot 3'},{src:'assets/games-20260911/watch/arvion-my-pet-3d/demo-1.mp4',alt:'ARVION MY PET 3D Wear OS video 1'},{src:'assets/games-20260911/watch/arvion-my-pet-3d/demo-2.mp4',alt:'ARVION MY PET 3D Wear OS video 2'},{src:'assets/games-20260911/watch/arvion-my-pet-3d/demo-3.mp4',alt:'ARVION MY PET 3D Wear OS video 3'}],play:'https://play.google.com/store/search?q=ARVION%20MY%20PET%203D&c=apps',noteEn:'Wear OS game for compatible smartwatches.',notePl:'Gra Wear OS dla kompatybilnych smartwatchy.'});
productData['snake-watch']=mkProduct({title:'SNAKE · Wear OS',icon:'assets/games-20260911/watch/snake/screen-1.png',enSub:'The classic Snake formula redesigned for a smartwatch display.',plSub:'Klasyczny Snake zaprojektowany na nowo dla ekranu smartwatcha.',en:'SNAKE for Wear OS keeps the familiar arcade formula on your wrist. Guide the snake, collect items, grow longer and try to beat your best result using a layout optimized for a compatible smartwatch.',pl:'SNAKE na Wear OS przenosi klasyczną zręcznościową rozgrywkę na nadgarstek. Steruj wężem, zbieraj elementy, wydłużaj go i próbuj pobić swój rekord w układzie zoptymalizowanym dla kompatybilnego smartwatcha.',gallery:[{src:'assets/games-20260911/watch/snake/screen-1.png',alt:'SNAKE Wear OS screenshot 1'},{src:'assets/games-20260911/watch/snake/screen-2.png',alt:'SNAKE Wear OS screenshot 2'},{src:'assets/games-20260911/watch/snake/screen-3.png',alt:'SNAKE Wear OS screenshot 3'},{src:'assets/games-20260911/watch/snake/screen-4.png',alt:'SNAKE Wear OS screenshot 4'},{src:'assets/games-20260911/watch/snake/screen-5.png',alt:'SNAKE Wear OS screenshot 5'},{src:'assets/games-20260911/watch/snake/screen-6.png',alt:'SNAKE Wear OS screenshot 6'}],play:'https://play.google.com/store/search?q=ARVION%20SNAKE%20Wear%20OS&c=apps',noteEn:'Wear OS game for compatible smartwatches.',notePl:'Gra Wear OS dla kompatybilnych smartwatchy.'});
"""
    if marker not in s:
        raise SystemExit('Product marker not found')
    s = s.replace(marker, block + marker, 1)

old_thumb = "galleryStrip.innerHTML=resolved.map((x,i)=>`<button class=\"gallery-thumb${i===0?' active':''}\" data-i=\"${i}\" type=\"button\"><img src=\"${x.resolved}\" alt=\"${x.alt}\"></button>`).join('');"
new_thumb = "galleryStrip.innerHTML=resolved.map((x,i)=>{const v=/\\.(mp4|webm)(\\?|$)/i.test(x.resolved);return `<button class=\"gallery-thumb${i===0?' active':''}\" data-i=\"${i}\" type=\"button\">${v?'<span class=\"video-thumb\" aria-hidden=\"true\">▶ VIDEO</span>':`<img src=\"${x.resolved}\" alt=\"${x.alt}\">`}</button>`}).join('');"
s = s.replace(old_thumb, new_thumb)

if '.video-thumb{' not in s:
    s = s.replace('.gallery-thumb.active{border-color:var(--gold2);box-shadow:0 0 0 1px var(--gold2) inset}', '.gallery-thumb.active{border-color:var(--gold2);box-shadow:0 0 0 1px var(--gold2) inset}.video-thumb{width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#0b0b0b;color:var(--gold2);font-size:11px;font-weight:900;letter-spacing:.08em}')

s = s.replace('content="2026-09-11-games-update"', 'content="2026-09-11-games-media-final"')
p.write_text(s, encoding='utf-8')
print('index.html patched')
