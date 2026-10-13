#!/usr/bin/env python3
"""Publish five user-uploaded October apps on all fourteen ARVION locales."""
from pathlib import Path
from html import escape
import re, shutil, subprocess, unicodedata, json

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'.october-five-extracted'
subprocess.run(['7z','x',str(ROOT/'STRONA INTERNETOWA.zip'),'-o'+str(TMP),'-y'],check=True,stdout=subprocess.DEVNULL)
SOURCE=TMP/'STRONA INTERNETOWA'
assert SOURCE.is_dir()
LANGS=['en','pl','de','fr','es','it','pt-br','ja','ko','zh-cn','tr','id','ru','uk']
LOCALES=['en-US','pl-PL','de-DE','fr-FR','es-ES','it-IT','pt-BR','ja-JP','ko-KR','zh-CN','tr-TR','id-ID','ru-RU','uk-UA']
LABELS=['Coming soon','Dostępne wkrótce','Demnächst verfügbar','Próximamente','Bientôt disponible','Prossimamente','Em breve','近日公開','출시 예정','即将推出','Yakında','Segera hadir','Скоро','Незабаром']
# label mapping above assigned by dictionary to avoid language order error
SOON=dict(zip(LANGS,['Coming soon','Dostępne wkrótce','Demnächst verfügbar','Bientôt disponible','Próximamente','Prossimamente','Em breve','近日公開','출시 예정','即将推出','Yakında','Segera hadir','Скоро','Незабаром']))
NAMES=[
 ('obd','AI ACTIVE EXHAUST PRO – OBD2','AI ACTIVE EXHAUST PRO – OBD2','phone','obd-active-exhaust-pro'),
 ('car-media-2-watch','CAR MEDIA 2 WATCH PRO','CAR MEDIA 2 WATCH','watch','car-media-2-watch-pro'),
 ('note-vault-pro','NOTE VAULT PRO','NOTE VAULT PRO','phone','note-vault-pro'),
 ('voice-recorder-pro-ai','VOICE RECORDER PRO AI','VOICE RECORDER PRO AL','phone','voice-recorder-pro-ai'),
 ('zoomstrike-ai-1000x','ZOOMSTRIKE AI 1000X','ZOOMSTRIKE ALL 1000X','phone','zoomstrike-ai-1000x')
]
DESC={
 'obd':'OBD2 diagnostics, live data and active exhaust sound controls for compatible vehicles.',
 'car-media-2-watch':'Media features and playback controls for Android phones and compatible Wear OS watches.',
 'note-vault-pro':'Create, organize and manage notes on Android and compatible smartwatches.',
 'voice-recorder-pro-ai':'Record, organize and manage audio recordings on Android.',
 'zoomstrike-ai-1000x':'Camera zoom and imaging utilities on compatible Android devices.'
}
desc_pl={
 'obd':'Diagnostyka OBD2, dane na żywo i sterowanie dźwiękiem wydechu.',
 'car-media-2-watch':'Multimedia i sterowanie odtwarzaniem na Androidzie oraz Wear OS.',
 'note-vault-pro':'Twórz i organizuj notatki na telefonie i zegarku.',
 'voice-recorder-pro-ai':'Nagrywaj i organizuj nagrania dźwiękowe na Androidzie.',
 'zoomstrike-ai-1000x':'Zoom aparatu i narzędzia obrazu na kompatybilnym Androidzie.'
}
assets={}
for key,name,folder,kind,slug in NAMES:
    src=SOURCE/folder
    assert src.is_dir(),str(src)
    dst=ROOT/'assets'/'october-20261013'/slug
    dst.mkdir(parents=True,exist_ok=True)
    images=sorted((p for p in src.iterdir() if p.suffix.lower() in ('.png','.jpg','.jpeg','.webp')),key=lambda p:p.name)
    assert images,key
    im=[]
    for i,p in enumerate(images,1):
        target=dst/(f'{i:02d}'+p.suffix.lower())
        shutil.copyfile(p,target)
        im.append(target.relative_to(ROOT).as_posix())
    txts=sorted(src.glob('*.txt'))
    for p in txts:
        shutil.copyfile(p,dst/'source-description.txt')
    assets[key]=im
assert len(assets)==5
# The original OBD slot remains, replacing its images/text and disabling purchase links.
data={}
for key,name,folder,kind,slug in NAMES:
    im=assets[key]
    data[key]={'title':name,'icon':im[0],'subtitle':{'en':DESC[key],'pl':desc_pl[key]},
      'gallery':[{'src':src,'alt':name+' image '+str(i)} for i,src in enumerate(im,1)],
      'copy':{'en':f'<h3>{escape(name)}</h3><p>{escape(DESC[key])}</p><p><strong>Coming soon</strong></p>',
              'pl':f'<h3>{escape(name)}</h3><p>{escape(desc_pl[key])}</p><p><strong>Dostępne wkrótce</strong></p>'}}
snippet='\n// OCTOBER 13 FIVE APPS START\n'+''.join("productData["+json.dumps(k)+"]="+json.dumps(v,ensure_ascii=False)+";\n" for k,v in data.items())+'// OCTOBER 13 FIVE APPS END\n'
for lang in LANGS:
    path=ROOT/('index.html' if lang=='en' else f'index-{lang}.html')
    s=path.read_text(encoding='utf8')
    # Older card remains in the same existing OBD position.
    s=s.replace("['obd','pixel-critters'","['pixel-critters'")
    s=s.replace('"obd":"com.obdactiveeeexhaust.pro",','')
    s=re.sub(r'// OCTOBER 13 FIVE APPS START.*?// OCTOBER 13 FIVE APPS END\n','',s,flags=re.S)
    # New categories placed at start and never repeated.
    for key,name,folder,kind,slug in NAMES[1:]:
        if re.search(r'\bid:[\x27"]'+re.escape(key)+r'[\x27"]',s):continue
        card={'id':key,'name':name,'type':kind,'tag':'Wear OS App' if kind=='watch' else 'Android App','img':assets[key][0],'desc':DESC[key],'details':True}
        # JS object is legal with JSON quoted keys too.
        assert 'const products=[' in s
        s=s.replace('const products=[','const products=[\n'+json.dumps(card,ensure_ascii=False)+',',1)
    # OBD card name and image updated, without duplicate.
    s=re.sub(r"(\bid:'obd',name:)'[^']+'",r"\g<1>'AI ACTIVE EXHAUST PRO – OBD2'",s,count=1)
    s=re.sub(r"(\bid:'obd',name:'AI ACTIVE EXHAUST PRO – OBD2',type:'phone',tag:'Android App',img:)'[^']+'",lambda m:m.group(1)+"'"+assets['obd'][0]+"'",s,count=1)
    marker='// ARVION ORIGINAL IMAGE CATALOG START'
    assert marker in s,path
    s=s.replace(marker,snippet+marker,1)
    # Other original image catalog code might reset OBD gallery. Our canonical override must be LAST.
    s=s.replace('// ARVION ORIGINAL IMAGE CATALOG END','// ARVION ORIGINAL IMAGE CATALOG END\n'+snippet,1)
    s=s.replace('DOSTĘPNA WKRÓTCE · COMING SOON',SOON[lang].upper()+' · COMING SOON') if lang!='en' else s
    # one click navigation to app details remains enabled, without buy buttons
    path.write_text(s,encoding='utf8')

# Create 14-language dedicated pages for four new apps; update existing 14 OBD pages
base='https://lukaszednarski998.github.io/privacy-policy.html/'
for key,name,folder,kind,slug in NAMES:
  imgs=assets[key]
  for lang,locale in zip(LANGS,LOCALES):
    suffix='' if lang=='en' else '-'+lang
    dest=ROOT/'apps'/(slug+suffix+'.html')
    title=escape(name)
    summary=escape(desc_pl[key] if lang=='pl' else DESC[key])
    links='\n'.join(f'<link rel="alternate" hreflang="{lc}" href="{base}apps/{slug+("-"+ll if ll!="en" else "")}.html">' for ll,lc in zip(LANGS,LOCALES))
    nav=' '.join(f'<a href="{slug+("-"+ll if ll!="en" else "")}.html" hreflang="{lc}">{ll.upper()}</a>' for ll,lc in zip(LANGS,LOCALES))
    gallery=''.join(f'<figure><img src="../{escape(src,quote=True)}" alt="{title} — {i}" loading="lazy"><figcaption>{title} · {i}</figcaption></figure>' for i,src in enumerate(imgs,1))
    status=SOON[lang]
    page=f'''<!doctype html><html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | ARVION</title><meta name="description" content="{summary} {escape(status)}"><link rel="canonical" href="{base}apps/{slug}{suffix}.html">{links}<link rel="icon" type="image/svg+xml" href="../assets/arvion-logo.svg"><style>body{{background:#08090b;color:#f4f4f6;font:16px/1.7 system-ui,Arial,sans-serif;margin:0}}main{{max-width:1080px;margin:auto;padding:20px}}a{{color:#e9bc57}}nav{{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}}h1{{line-height:1.2}}.soon{{display:inline-block;border:1px solid #b88b42;border-radius:12px;padding:9px 16px;color:#ffd783;font-weight:750}}.gallery{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-top:20px}}figure{{margin:0;background:#181a1f;border:1px solid #30343b;border-radius:14px;overflow:hidden}}figure img{{display:block;width:100%;height:auto}}figcaption{{padding:8px 12px;color:#b6b8be}}</style></head><body><main><p><a href="../{("index-"+lang+".html") if lang!="en" else ""}">← ARVION</a> · <a href="index{suffix}.html">Apps</a></p><nav aria-label="Language versions">{nav}</nav><h1>{title}</h1><p>{summary}</p><p class="soon">{escape(status)}</p><section><h2>Screenshots / Galeria</h2><div class="gallery">{gallery}</div></section></main><script defer src="../assets/analytics-config.js"></script><script defer src="../assets/site-analytics.js"></script></body></html>'''
    dest.write_text(page,encoding='utf8')

# Multilingual /apps/ catalog: add missing cards, OBD already present (mark upcoming).
for lang in LANGS:
  path=ROOT/'apps'/('index.html' if lang=='en' else f'index-{lang}.html')
  s=path.read_text(encoding='utf8')
  if '<!-- OCTOBER 13 APPS START -->' in s:
      s=re.sub(r'<!-- OCTOBER 13 APPS START -->.*?<!-- OCTOBER 13 APPS END -->','',s,flags=re.S)
  cards=[]
  for key,name,folder,kind,slug in NAMES:
      href=slug+('' if lang=='en' else '-'+lang)+'.html'
      cards.append(f'<article class="october-card"><a href="{href}">{escape(name)}</a><p>{escape(desc_pl[key] if lang=="pl" else DESC[key])}</p><strong>{escape(SOON[lang])}</strong></article>')
  block='<!-- OCTOBER 13 APPS START --><section aria-label="October new applications"><h2>'+escape(SOON[lang])+'</h2><div class="october-grid">'+''.join(cards)+'</div></section><style>.october-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}.october-card{background:#16181d;border:1px solid #453921;border-radius:12px;padding:20px}.october-card a{font-weight:bold;color:#efca7e}.october-card strong{color:#d9ad59}</style><!-- OCTOBER 13 APPS END -->'
  assert '</main>' in s,path
  s=s.replace('</main>',block+'</main>',1)
  path.write_text(s,encoding='utf8')

# checks
for lang in LANGS:
  home=(ROOT/('index.html' if lang=='en' else f'index-{lang}.html')).read_text(encoding='utf8')
  for key,*_ in NAMES:
    assert 'productData['+json.dumps(key)+']' in home
  assert '"obd":"com.obdactiveeeexhaust.pro"' not in home
for key,name,folder,kind,slug in NAMES:
  for lang in LANGS:
    assert (ROOT/'apps'/(slug+('' if lang=='en' else '-'+lang)+'.html')).exists()
print('Published five apps in 14 languages, preserving existing Google Play links except OBD in upcoming group.')
shutil.rmtree(TMP)
