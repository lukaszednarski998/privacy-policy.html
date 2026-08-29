from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Temporary image cleanup while the ARVION catalog is being refreshed.
# Keep the product cards, descriptions and Google Play links, but remove
# all current game/app/watch product imagery from the rendered website.

css = r'''
.image-placeholder{color:#6f6f6f;font-size:12px;font-weight:800;letter-spacing:.16em;text-align:center;padding:24px}.product-head.no-image{grid-template-columns:1fr}.gallery-main.empty-gallery:after{content:'NEW IMAGES COMING SOON';color:#6f6f6f;font-size:12px;font-weight:800;letter-spacing:.16em;text-align:center;padding:24px}.gallery-main.empty-gallery img{display:none}
'''
if '.image-placeholder{' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

s = s.replace(
    'Click a highlighted ARVION product to see screenshots, features and Google Play access.',
    'Product images are being refreshed. Details and Google Play access remain available.'
)

cleanup = "products.forEach(p=>{p.img=''});Object.values(productData).forEach(p=>{p.icon='';p.gallery=[]});\n"
if cleanup not in s:
    s = s.replace('const supportCopy=', cleanup + 'const supportCopy=', 1)

new_render = r'''function render(filter='all'){const list=products.filter(p=>filter==='all'||p.type===filter);grid.innerHTML=list.map(p=>`<article class="card${p.details?' details':''}" ${p.details?`tabindex="0" role="button" data-product="${p.id}" aria-label="Open ${p.name}"`:''}><div class="pic">${p.img?`<img src="${p.img}" alt="${p.name}" loading="lazy">`:'<span class="image-placeholder">NEW IMAGES COMING SOON</span>'}${p.details?'<span class="details-badge">View details</span>':''}</div><div class="body"><span class="tag">${p.tag}</span><h3>${p.name}</h3><p>${p.desc}</p></div></article>`).join('');document.querySelectorAll('[data-product]').forEach(c=>{c.onclick=()=>openProduct(c.dataset.product);c.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();openProduct(c.dataset.product)}}})}'''
s, n = re.subn(r"function render\(filter='all'\)\{.*?\}\nasync function buildGallery", new_render + '\nasync function buildGallery', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not patch render()')

new_gallery = r'''async function buildGallery(data){galleryStrip.innerHTML='';const frame=galleryMain.parentElement;if(!data.gallery||!data.gallery.length){galleryMain.removeAttribute('src');galleryMain.alt='';galleryMain.style.display='none';frame.classList.add('empty-gallery');return}frame.classList.remove('empty-gallery');galleryMain.style.display='block';const resolved=[];for(const item of data.gallery){try{resolved.push({...item,resolved:await imageSrc(item)})}catch(e){console.error(e)}}if(!resolved.length){galleryMain.style.display='none';frame.classList.add('empty-gallery');return}galleryMain.src=resolved[0].resolved;galleryMain.alt=resolved[0].alt;galleryStrip.innerHTML=resolved.map((x,i)=>`<button class="gallery-thumb${i===0?' active':''}" data-i="${i}" type="button"><img src="${x.resolved}" alt="${x.alt}"></button>`).join('');galleryStrip.querySelectorAll('button').forEach(b=>b.onclick=()=>{const x=resolved[+b.dataset.i];galleryMain.src=x.resolved;galleryMain.alt=x.alt;galleryStrip.querySelectorAll('button').forEach(y=>y.classList.remove('active'));b.classList.add('active')})}'''
s, n = re.subn(r"async function buildGallery\(data\)\{.*?\}\nfunction setProductLang", new_gallery + '\nfunction setProductLang', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not patch buildGallery()')

new_open = r'''async function openProduct(id){currentProduct=id;const data=productData[id];document.getElementById('productTitle').textContent=data.title;const icon=document.getElementById('productIcon');const head=document.querySelector('.product-head');head.classList.toggle('no-image',!data.icon);if(data.icon){icon.src=data.icon;icon.alt=data.title;icon.style.display='block'}else{icon.removeAttribute('src');icon.alt='';icon.style.display='none'}setProductLang(currentLang);productModal.classList.add('open');document.body.classList.add('modal-open');await buildGallery(data)}'''
s, n = re.subn(r"async function openProduct\(id\)\{.*?\}\nfunction setSupportLang", new_open + '\nfunction setSupportLang', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not patch openProduct()')

p.write_text(s, encoding='utf-8')
print('ARVION catalog product images cleared; placeholders enabled.')
