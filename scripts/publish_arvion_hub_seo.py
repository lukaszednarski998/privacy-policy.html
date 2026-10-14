#!/usr/bin/env python3
"""Build useful, static ARVION Hub pages; preserve unrelated site content.
Capabilities checked against user-supplied ARVION Watch Media Hub v1.10.20 source.
    Localized copy is maintained in scripts/arvion_hub_content.json.
No fabricated ratings, price, downloads, codecs or universal compatibility.
"""
from __future__ import annotations
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://lukaszednarski998.github.io/privacy-policy.html/'
PLAY = 'https://play.google.com/store/apps/details?id=pl.arvion.watchmediahub'
LOCALES = [('en','English'),('pl','Polski'),('de','Deutsch'),('fr','Français'),('es','Español'),('it','Italiano'),('pt-BR','Português (Brasil)'),('ja','日本語'),('ko','한국어'),('zh-CN','简体中文'),('tr','Türkçe'),('id','Bahasa Indonesia'),('ru','Русский'),('uk','Українська')]
D = json.loads((ROOT / 'scripts/arvion_hub_content.json').read_text(encoding='utf-8'))
GALLERY = json.loads((ROOT / 'assets/arvion-watch-media-hub/gallery.json').read_text(encoding='utf-8'))
GALLERY_LABELS = {'en':'App gallery','pl':'Galeria aplikacji','de':'App-Galerie','fr':'Galerie de l’application','es':'Galería de la aplicación','it':'Galleria dell’app','pt-BR':'Galeria do app','ja':'アプリギャラリー','ko':'앱 갤러리','zh-CN':'应用图库','tr':'Uygulama galerisi','id':'Galeri aplikasi','ru':'Галерея приложения','uk':'Галерея застосунку'}
COMING_SOON = {'en':'Coming soon','pl':'Dostępna wkrótce','de':'Demnächst verfügbar','fr':'Bientôt disponible','es':'Próximamente','it':'Disponibile a breve','pt-BR':'Em breve','ja':'近日公開','ko':'출시 예정','zh-CN':'即将推出','tr':'Yakında','id':'Segera hadir','ru':'Скоро','uk':'Незабаром'}

CSS = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#070707;color:#f5f5f5;font:17px/1.75 Arial,Helvetica,sans-serif}a{color:#f1d17a;text-underline-offset:4px}a:focus-visible,summary:focus-visible{outline:3px solid #f1d17a;outline-offset:5px}.wrap{width:min(1120px,calc(100% - 40px));margin:auto}header{border-bottom:1px solid #3b3320;background:#0d0d0d}header .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:18px 0;flex-wrap:wrap}.brand{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:.12em;text-decoration:none}.brand img{width:40px;height:40px}nav{display:flex;gap:16px;flex-wrap:wrap;font-size:14px}.hero{padding:54px 0 38px}.eyebrow{color:#f1d17a;font-size:13px;letter-spacing:.08em}h1{font-size:clamp(30px,5vw,56px);line-height:1.15;margin:16px 0 22px;max-width:1020px;overflow-wrap:anywhere}.lead{max-width:860px;color:#d2d2d2;font-size:20px;line-height:1.75}.actions{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin:26px 0}.cta{display:inline-flex;align-items:center;justify-content:center;background:#f1d17a;color:#18130a;text-decoration:none;font-weight:800;line-height:1.4;padding:14px 22px;border-radius:12px;min-height:48px;max-width:100%;text-align:center}.cta:hover{background:#ffe5a5}.languages{padding:20px 0;border-top:1px solid #3b3320;border-bottom:1px solid #3b3320}.languages a{padding:6px 9px;border:1px solid #3b3320;border-radius:8px}.languages a[aria-current=page]{background:#f1d17a;color:#18130a}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:32px 0 46px}.feature{background:#101010;border:1px solid #3b3320;border-radius:18px;padding:25px}.feature h2{font-size:23px;line-height:1.35;color:#f1d17a;margin:0 0 16px}.feature p{margin:0;color:#cecece}.faq{margin:0 0 50px}.faq h2{font-size:30px;line-height:1.3}.faq details{border-bottom:1px solid #3b3320;padding:16px 0}.faq summary{font-weight:700;cursor:pointer}.faq p{color:#cecece;max-width:930px}.closing{padding:25px;border:1px solid #3b3320;border-radius:18px;background:#101010;margin-bottom:40px}.closing h2{line-height:1.3;margin-top:0}footer{border-top:1px solid #3b3320;padding:24px 0 40px;color:#aaa;font-size:14px}footer p{overflow-wrap:anywhere}@media(max-width:680px){.wrap{width:calc(100% - 32px)}.hero{padding:30px 0 24px}.lead{font-size:18px}.grid{grid-template-columns:1fr;gap:14px}.feature{padding:20px}.cta{width:100%}header nav{gap:13px}body{font-size:16px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''

def suffix(lang):
    return '' if lang == 'en' else '-' + lang.lower()
def page_name(lang):
    return 'arvion-watch-media-hub' + suffix(lang) + '.html'
def home_path(lang):
    return 'index' + suffix(lang) + '.html'
def url_for(lang):
    return BASE + 'apps/' + page_name(lang)
def esc(value):
    return html.escape(str(value), quote=True)
def language_nav(lang):
    return '\n'.join('<a href="'+page_name(k)+'" hreflang="'+k+'" lang="'+k+'"'+(' aria-current="page"' if k == lang else '')+'>'+esc(name)+'</a>' for k,name in LOCALES)

CSS += '''.app-gallery{margin:32px 0}.app-gallery h2{font-size:28px;line-height:1.3}.gallery-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.gallery-grid a{display:block;border:1px solid #3b3320;border-radius:12px;overflow:hidden;background:#101010}.gallery-grid img{display:block;width:100%;height:auto}.gallery-grid a:hover{border-color:#f1d17a}@media(max-width:680px){.gallery-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}@media(max-width:420px){.gallery-grid{grid-template-columns:1fr}}'''

def gallery_html(lang):
    images = []
    for index,item in enumerate(GALLERY,1):
        src = '../'+item['src']
        alt = 'ARVION Watch Media Hub — '+GALLERY_LABELS[lang]+' '+str(index)
        images.append(f'<a href="{esc(src)}" target="_blank" rel="noopener noreferrer"><img src="{esc(src)}" alt="{esc(alt)}" width="{item["width"]}" height="{item["height"]}" loading="lazy" decoding="async"></a>')
    return '<section class="app-gallery" aria-labelledby="gallery-title"><h2 id="gallery-title">'+esc(GALLERY_LABELS[lang])+'</h2><div class="gallery-grid">'+''.join(images)+'</div></section>'

def render(lang):
    d = D[lang]
    label = d['labels']
    home = '../' if lang == 'en' else '../' + home_path(lang)
    catalog = './' if lang == 'en' else home_path(lang)
    alts = '\n'.join('<link rel="alternate" hreflang="'+k+'" href="'+url_for(k)+'">' for k,_ in LOCALES)
    alts += '\n<link rel="alternate" hreflang="x-default" href="'+url_for('en')+'">'
    schema = {'@context':'https://schema.org','@graph':[
        {'@type':'WebPage','@id':url_for(lang)+'#webpage','url':url_for(lang),'name':d['title'],'description':d['description'],'inLanguage':lang,'mainEntity':{'@id':url_for(lang)+'#app'}},
        {'@type':'SoftwareApplication','@id':url_for(lang)+'#app','name':'ARVION Watch Media Hub','alternateName':'ARVION Hub','operatingSystem':'Android, Wear OS','applicationCategory':'MultimediaApplication','url':url_for(lang),'description':d['description'],'featureList':[x[0] for x in d['sections'][:4]],'image':[BASE+x['src'] for x in GALLERY],'publisher':{'@type':'Organization','name':'ARVION','url':BASE}},
        {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':label[1],'item':BASE+('' if lang=='en' else home_path(lang))},{'@type':'ListItem','position':2,'name':label[2],'item':BASE+'apps/'+('' if lang=='en' else home_path(lang))},{'@type':'ListItem','position':3,'name':'ARVION Watch Media Hub','item':url_for(lang)}]}
    ]}
    blocks = '\n'.join('<section class="feature" id="feature-'+str(i)+'"><h2>'+esc(h)+'</h2><p>'+esc(p)+'</p></section>' for i,(h,p) in enumerate(d['sections'],1))
    faq = '\n'.join('<details open><summary>'+esc(q)+'</summary><p>'+esc(a)+'</p></details>' for q,a in d['questions'])
    json_ld = json.dumps(schema, ensure_ascii=False, separators=(',',':')).replace('<','\\u003c')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(d['title'])}</title>
<meta name="description" content="{esc(d['description'])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url_for(lang)}">
{alts}
<link rel="icon" type="image/svg+xml" href="../assets/arvion-logo.svg">
<link rel="stylesheet" href="../assets/arvion-hub-product.css">
<meta name="theme-color" content="#070707">
<meta property="og:type" content="website">
<meta property="og:url" content="{url_for(lang)}">
<meta property="og:title" content="{esc(d['title'])}">
<meta property="og:description" content="{esc(d['description'])}">
<meta property="og:image" content="{BASE+GALLERY[0]['src']}">
<meta property="og:image:alt" content="ARVION Watch Media Hub">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE+GALLERY[0]['src']}">
<meta name="twitter:title" content="{esc(d['title'])}">
<meta name="twitter:description" content="{esc(d['description'])}">
<script type="application/ld+json">{json_ld}</script>
</head>
<body>
<header><div class="wrap"><a class="brand" href="{home}"><img src="../assets/arvion-logo.svg" alt="ARVION" width="40" height="40">ARVION</a><nav><a href="{home}">{esc(label[1])}</a><a href="{catalog}">{esc(label[2])}</a><a href="../ARVION-WATCH-MEDIA-HUB-PRIVACY.html">{esc(label[3])}</a></nav></div></header>
<main class="wrap">
<section class="hero"><div class="eyebrow">ARVION Watch Media Hub · {esc(label[6])}</div><h1>{esc(d['title'])}</h1><p class="lead">{esc(d['intro'])}</p><div class="actions"><a class="cta" href="#features">{esc(label[7])}</a><a href="#availability">{esc(d['availability_label'])}</a></div></section>
<nav class="languages" aria-label="Language">{language_nav(lang)}</nav>
{gallery_html(lang)}
<section class="closing" id="availability" style="margin-top:28px"><h2>{esc(d['availability_label'])}</h2><p>{esc(d['availability'])}</p></section>
<div class="grid" id="features">{blocks}</div>
<section class="faq"><h2>{esc(label[4])}</h2>{faq}</section>
<section class="closing"><h2>{esc(label[5])}</h2><p>{esc(d['description'])}</p><a class="cta" href="#availability">{esc(d['availability_label'])}</a></section>
</main>
<footer><div class="wrap"><nav><a href="{home}">{esc(label[1])}</a><a href="{catalog}">{esc(label[2])}</a><a href="../ARVION-WATCH-MEDIA-HUB-PRIVACY.html">{esc(label[3])}</a></nav><p>ARVION Watch Media Hub · MUSIC 2 WATCH · VIDEO 2 WATCH · CAM 2 WATCH</p></div></footer>
<script defer src="../assets/analytics-config.js"></script>
<script defer src="../assets/site-analytics.js"></script>
</body>
</html>
'''

MARK_A = '<!-- ARVION HUB DISCOVERY START -->'
MARK_B = '<!-- ARVION HUB DISCOVERY END -->'

HUB_ID = 'arvion-watch-media-hub'
HUB_CARD_A = '// ARVION HUB CARD START'
HUB_CARD_B = '// ARVION HUB CARD END'
CATALOG_A = '<!-- ARVION HUB CATALOG CARD START -->'
CATALOG_B = '<!-- ARVION HUB CATALOG CARD END -->'

def remove_banner(text):
    return re.sub(re.escape(MARK_A)+r'.*?'+re.escape(MARK_B)+r'\n{0,2}', '', text, flags=re.S)

def modal_data():
    copy = {}
    for lang,_ in LOCALES:
        d = D[lang]
        sections = ''.join('<h3>'+esc(h)+'</h3><p>'+esc(p)+'</p>' for h,p in d['sections'])
        copy[lang] = '<p>'+esc(d['intro'])+'</p>'+sections+'<h3>'+esc(d['availability_label'])+'</h3><p>'+esc(d['availability'])+'</p><p><a href="apps/'+page_name(lang)+'">'+esc(d['labels'][5])+'</a></p>'
    return {'title':'ARVION Watch Media Hub','icon':GALLERY[0]['src'],
            'subtitle':{lang:D[lang]['description'] for lang,_ in LOCALES},
            'languages':[{'key':lang,'label':name} for lang,name in LOCALES],
            'gallery':[{'src':item['src'],'alt':'ARVION Watch Media Hub — '+str(i)} for i,item in enumerate(GALLERY,1)],
            'copy':copy}

def integrate_home(text, lang):
    text = remove_banner(text)
    text = re.sub(re.escape(HUB_CARD_A)+r'.*?'+re.escape(HUB_CARD_B)+r'\n?', '', text, flags=re.S)
    text = re.sub(r'<script id="arvion-hub-catalog-data">.*?</script>\n?', '', text, flags=re.S)
    products = re.search(r'const products=\[(.*?)\n\];',text,re.S)
    if not products:
        raise ValueError('Product array is missing')
    anchor = re.search(r"(?m)^[^\n]*\bid['\"]?\s*:\s*['\"]video-2-watch['\"][^\n]*\n",products.group(1))
    if not anchor:
        raise ValueError('VIDEO 2 WATCH catalog position is missing')
    card = {'id':HUB_ID,'name':'ARVION Watch Media Hub','type':'watch','tag':'Android + Wear OS','img':GALLERY[0]['src'],'desc':D[lang]['description'],'details':True}
    block = HUB_CARD_A+'\n'+json.dumps(card,ensure_ascii=False)+',\n'+HUB_CARD_B+'\n'
    offset = products.start(1)+anchor.end()
    text = text[:offset]+block+text[offset:]
    payload = json.dumps(modal_data(),ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    script = '<script id="arvion-hub-catalog-data">\nproductData['+json.dumps(HUB_ID)+']='+payload+';\n</script>\n'
    if '</body>' not in text:
        raise ValueError('Closing body is missing')
    return text.replace('</body>',script+'</body>',1)

def integrate_catalog(text, lang):
    text = remove_banner(text)
    text = re.sub(r'\n'+re.escape(CATALOG_A)+r'.*?'+re.escape(CATALOG_B)+r'\n?', '', text, flags=re.S)
    desc = esc(D[lang]['description'])
    link = '<a class="product" href="'+page_name(lang)+'">ARVION Watch Media Hub</a>'
    if lang == 'en':
        card = '<article class="c" data-hub-catalog-card>'+link+'<strong>Android + Wear OS</strong><p>'+desc+'</p><p class="uses">'+esc(COMING_SOON[lang])+'</p></article>'
        anchor = re.search(r'<article class="c">(?:(?!</article>).)*href="video-2-watch.html".*?</article>',text,re.S)
    else:
        card = '<li data-hub-catalog-card>'+link+'<p>'+desc+'</p><div class="labels"><span>Android + Wear OS</span><span class="soon">'+esc(COMING_SOON[lang])+'</span></div></li>'
        anchor = re.search(r'<li>(?:(?!</li>).)*href="video-2-watch'+suffix(lang)+r'.html".*?</li>',text,re.S)
    if not anchor:
        raise ValueError('Video card missing in '+home_path(lang))
    block = '\n'+CATALOG_A+'\n'+card+'\n'+CATALOG_B+'\n'
    offset = anchor.end()
    text = text[:offset]+block+text[offset:]
    def schema_update(match):
        data = json.loads(match.group(1))
        itemlist = data if data.get('@type') == 'ItemList' else data.get('mainEntity',{})
        items = itemlist.get('itemListElement')
        if isinstance(items,list):
            items[:] = [item for item in items if item.get('url') != url_for(lang)]
            index = next((i+1 for i,item in enumerate(items) if 'video-2-watch' in item.get('url','')),len(items))
            items.insert(index,{'@type':'ListItem','position':index+1,'name':'ARVION Watch Media Hub','url':url_for(lang)})
            for i,item in enumerate(items,1):
                item['position'] = i
        return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')+'</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema_update,text,flags=re.S)

def build():
    assert set(D) == {k for k,_ in LOCALES}
    policy = ROOT / 'ARVION-WATCH-MEDIA-HUB-PRIVACY.html'
    if 'pl.arvion.watchmediahub' not in policy.read_text(encoding='utf-8'):
        raise ValueError('Product package does not match the source privacy policy')
    pending = {}
    for lang,_ in LOCALES:
        pending['apps/'+page_name(lang)] = render(lang)
        for prefix in ('','apps/'):
            path = prefix+home_path(lang)
            original = (ROOT/path).read_bytes().decode('utf-8')
            pending[path] = integrate_catalog(original,lang) if prefix else integrate_home(original,lang)
    pending['assets/arvion-hub-product.css'] = CSS+'\n'
    new_urls = []
    for filename in ('sitemap.xml', 'sitemap-google.xml'):
        sitemap = (ROOT/filename).read_bytes().decode('utf-8')
        doc = ET.fromstring(sitemap)
        known = {node.text for node in doc.findall('.//{*}loc')}
        additions = [url_for(k) for k,_ in LOCALES if url_for(k) not in known]
        if filename == 'sitemap.xml':
            new_urls = additions
        if additions:
            addition = ''.join('  <url><loc>'+esc(url)+'</loc></url>\n' for url in additions)
            if '</urlset>' not in sitemap:
                raise ValueError('Unsupported sitemap format')
            sitemap = sitemap.replace('</urlset>',addition+'</urlset>',1)
        ET.fromstring(sitemap)
        pending[filename] = sitemap
    sitemap_text = (ROOT/'sitemap.txt').read_bytes().decode('utf-8')
    known_text = set(sitemap_text.splitlines())
    text_additions = [url_for(k) for k,_ in LOCALES if url_for(k) not in known_text]
    pending['sitemap.txt'] = sitemap_text.rstrip()+'\n'+'\n'.join(text_additions)+'\n' if text_additions else sitemap_text
    # Validate every output before changing any tracked file.
    for lang,_ in LOCALES:
        body = pending['apps/'+page_name(lang)]
        assert body.count('<h1>') == 1
        assert body.count('rel="canonical"') == 1
        assert body.count('rel="alternate"') == 15
        assert body.count('<section class="feature"') == 6
        assert body.count('<details open>') >= 3
        assert '<html lang="'+lang+'">' in body
        assert 'noindex' not in body
        for script in re.findall(r'<script type="application/ld\+json">(.*?)</script>',body,re.S):
            json.loads(script)
        for other,_ in LOCALES:
            assert 'hreflang="'+other+'" href="'+url_for(other)+'"' in body
        assert body.count('class="gallery-grid"') == 1
        assert body.count('loading="lazy"') == 9
        for prefix in ('','apps/'):
            assert MARK_A not in pending[prefix+home_path(lang)]
        assert pending[home_path(lang)].count(HUB_CARD_A) == 1
        assert pending['apps/'+home_path(lang)].count(CATALOG_A) == 1
    changed = []
    for relative, content in pending.items():
        path = ROOT/relative
        if path.exists() and path.read_bytes().decode('utf-8') == content:
            continue
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(content.encode('utf-8'))
        changed.append(relative)
    print(json.dumps({'product_pages':14,'localized_catalog_cards':28,'original_images':len(GALLERY),'new_sitemap_urls':len(new_urls),'changed_files':changed,'checks':'passed'},ensure_ascii=False,indent=2))
    return changed

if __name__ == '__main__':
    build()
