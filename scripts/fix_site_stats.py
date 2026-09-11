from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
start = s.index('// ARVION SITE STATS START')
end = s.index('// ARVION SITE STATS END', start) + len('// ARVION SITE STATS END')

new = r'''// ARVION SITE STATS START
const arvionCounterBase='https://countapi.mileshilliard.com/api/v1';
const arvionViewKey='arvion_lukaszednarski998_site_views_v1';
const arvionHeartKey='arvion_lukaszednarski998_site_hearts_v1';
const visitCountEl=document.getElementById('visitCount'),heartCountEl=document.getElementById('heartCount'),heartButton=document.getElementById('heartButton');

async function arvionCounter(key,mode='get'){
  const controller=new AbortController();
  const timeout=setTimeout(()=>controller.abort(),8000);
  try{
    const r=await fetch(`${arvionCounterBase}/${mode}/${encodeURIComponent(key)}?t=${Date.now()}`,{
      cache:'no-store',
      signal:controller.signal
    });
    if(!r.ok){
      if(mode==='get'&&r.status===404)return 0;
      throw new Error('counter '+r.status);
    }
    const d=await r.json();
    const value=Number(d.value);
    return Number.isFinite(value)?value:0;
  }catch(e){
    console.warn('ARVION counter unavailable',e);
    return null;
  }finally{
    clearTimeout(timeout);
  }
}

function formatStat(n){return n===null?'—':new Intl.NumberFormat().format(n)}

async function initArvionStats(){
  let alreadyCounted=false;
  try{alreadyCounted=sessionStorage.getItem('arvionVisitCountedV2')==='1'}catch(e){}

  let views;
  if(alreadyCounted){
    views=await arvionCounter(arvionViewKey,'get');
  }else{
    views=await arvionCounter(arvionViewKey,'hit');
    if(views!==null){
      try{sessionStorage.setItem('arvionVisitCountedV2','1')}catch(e){}
    }else{
      views=await arvionCounter(arvionViewKey,'get');
    }
  }

  visitCountEl.textContent=formatStat(views);
  visitCountEl.closest('.site-stat').classList.toggle('stats-offline',views===null);

  let liked=false;
  try{liked=localStorage.getItem('arvionHeartGivenV2')==='1'}catch(e){}

  const hearts=await arvionCounter(arvionHeartKey,'get');
  heartCountEl.textContent=formatStat(hearts);
  heartButton.classList.toggle('stats-offline',hearts===null);

  if(liked){
    heartButton.classList.add('liked');
    heartButton.setAttribute('aria-label','Heart already added / Serduszko już dodane');
    heartButton.title='Thank you! / Dziękujemy!';
  }
}

heartButton.addEventListener('click',async()=>{
  let liked=false;
  try{liked=localStorage.getItem('arvionHeartGivenV2')==='1'}catch(e){}
  if(liked){
    heartButton.classList.add('liked');
    return;
  }

  heartButton.disabled=true;
  const hearts=await arvionCounter(arvionHeartKey,'hit');

  if(hearts!==null){
    heartCountEl.textContent=formatStat(hearts);
    heartButton.classList.add('liked');
    heartButton.classList.remove('stats-offline');
    heartButton.title='Thank you! / Dziękujemy!';
    heartButton.setAttribute('aria-label','Heart added / Serduszko dodane');
    try{localStorage.setItem('arvionHeartGivenV2','1')}catch(e){}
  }else{
    const current=await arvionCounter(arvionHeartKey,'get');
    heartCountEl.textContent=formatStat(current);
    heartButton.classList.toggle('stats-offline',current===null);
    heartButton.title='Counter temporarily unavailable — try again / Licznik chwilowo niedostępny — spróbuj ponownie';
  }

  heartButton.disabled=false;
});

initArvionStats();
// ARVION SITE STATS END'''

s = s[:start] + new + s[end:]
s = s.replace('content="2026-09-11-ony-phone-menu"','content="2026-09-11-stats-fix"',1)
p.write_text(s, encoding='utf-8')
