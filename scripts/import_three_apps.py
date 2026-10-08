import zipfile, pathlib, json, re, html
z=zipfile.ZipFile('DO STRONY.zip')
page=pathlib.Path('index.html')
s=page.read_text(encoding='utf-8')
apps=[('FILE 2 WATCH','file-2-watch','watch','Wear OS App'),('INSPECT 2 WATCH','inspect-2-watch','watch','Wear OS App'),('KIDS REMOTE LOCK','kids-remote-lock','phone','Android App')]
cards=[]; details=[]
for name,slug,kind,tag in apps:
 prefix='DO STRONY/'+name+'/'
 images=[x for x in z.namelist() if x.startswith(prefix) and x.lower().endswith(('.png','.jpg'))]
 source=next(x for x in z.namelist() if x.startswith(prefix) and x.endswith('.txt'))
 assert images
 gallery=[]
 for i,img in enumerate(images):
  dest=pathlib.Path('assets/coming-soon')/(slug+'-'+str(i+1)+'.png')
  dest.parent.mkdir(parents=True,exist_ok=True)
  dest.write_bytes(z.read(img))
  gallery.append({'src':str(dest),'alt':name+' screenshot '+str(i+1)})
 t=z.read(source).decode('utf-8-sig').replace('\r','')
 if slug=='file-2-watch': markers=['ENGLISH - en-US','POLSKI - pl-PL']
 elif slug=='inspect-2-watch': markers=['[en-US] English','[pl-PL] Polski']
 else: markers=['JĘZYK / LOCALE: EN','JĘZYK / LOCALE: PL']
 def fields(marker):
  section=t[t.index(marker):]
  m=re.search(r'(?:Pełny opis|Full description)\s*\n\*?\s*\n?',section,re.I)
  short=re.search(r'(?:Krótki opis|Short description)\s*\n\*?\s*\n?([^\n]+)',section,re.I)
  assert m and short,(slug,marker)
  full=re.split(r'\n={20,}',section[m.end():],maxsplit=1)[0].strip()
  return short.group(1).strip(),full
 en,enfull=fields(markers[0]); pl,plfull=fields(markers[1])
 esc=lambda x:html.escape(x).replace('\n','<br>')
 card={'id':slug,'name':name,'type':kind,'tag':tag,'img':gallery[0]['src'],'desc':en,'details':True}
 cards.append('{'+','.join(k+':'+json.dumps(v,ensure_ascii=False) for k,v in card.items())+'}')
 detail={'title':name,'icon':gallery[0]['src'],'subtitle':{'en':en,'pl':pl},'gallery':gallery,'copy':{'en':'<h3>'+name+'</h3><p>'+esc(enfull)+'</p><p>COMING SOON — Not available yet.</p>','pl':'<h3>'+name+'</h3><p>'+esc(plfull)+'</p><p>DOSTĘPNE WKRÓTCE — Jeszcze niedostępne.</p>'}}
 details.append(json.dumps(slug)+':'+json.dumps(detail,ensure_ascii=False))
if 'id:"file-2-watch"' not in s:
 s=s.replace('const products=[','const products=[\n'+',\n'.join(cards)+',',1)
 s=s.replace('const productData={','const productData={\n'+',\n'.join(details)+',',1)
 page.write_text(s,encoding='utf-8')
print('Added 3 coming soon cards, assets and two language descriptions.')
