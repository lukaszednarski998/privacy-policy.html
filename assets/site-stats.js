/* ARVION shared site counters. */
(function () {
  'use strict';
  const visits=document.getElementById('visitCount');
  const hearts=document.getElementById('heartCount');
  const button=document.getElementById('heartButton');
  if (!visits || !hearts || !button) return;
  const base='https://countapi.mileshilliard.com/api/v1';
  const viewsKey='arvion_lukaszednarski998_site_views_v1';
  const heartsKey='arvion_lukaszednarski998_site_hearts_v1';
  const sessionKey='arvionVisitCountedV2';
  const likedKey='arvionHeartGivenV2';
  const pl=(document.documentElement.lang||'').toLowerCase().startsWith('pl');
  const copy=pl ? {
    success:'Dziękujemy! Twoje serduszko zostało dodane.',
    already:'Serduszko zostało już dodane z tej przeglądarki.',
    offline:'Nie można połączyć się z licznikiem. Spróbuj ponownie później.'
  } : {
    success:'Thank you! Your heart has been counted.',
    already:'You have already added a heart from this browser.',
    offline:'The counter is temporarily unavailable. Please try again later.'
  };
  function get(store,key){try{return store.getItem(key)}catch(e){return null}}
  function set(store,key,value){try{store.setItem(key,value)}catch(e){}}
  function showCount(el,value){
    el.textContent=value===null?'—':Number(value).toLocaleString(document.documentElement.lang||'en');
    const parent=el.closest('.site-stat');
    if(parent)parent.classList.toggle('stats-offline',value===null);
    if(value===null)el.title=copy.offline;else el.removeAttribute('title');
  }
  let toast,timer;
  function notice(message){
    if(!toast){
      toast=document.createElement('div');
      toast.setAttribute('role','status');
      toast.setAttribute('aria-live','polite');
      toast.style.cssText='position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:100000;max-width:min(90vw,460px);padding:12px 18px;border-radius:12px;background:#201218;color:#fff;border:1px solid #da6378;box-shadow:0 8px 32px #000a;font:600 14px/1.45 system-ui,sans-serif;text-align:center;display:none;';
      document.body.appendChild(toast);
    }
    toast.textContent=message;
    toast.style.display='block';
    clearTimeout(timer);
    timer=setTimeout(function(){toast.style.display='none'},4300);
  }
  async function query(key,method){
    const controller=new AbortController();
    const timer=setTimeout(function(){controller.abort()},10000);
    try{
      const response=await fetch(base+'/'+method+'/'+encodeURIComponent(key)+'?t='+Date.now(),{
        cache:'no-store',credentials:'omit',mode:'cors',signal:controller.signal
      });
      if(method==='get' && response.status===404)return 0;
      if(!response.ok)throw new Error('HTTP '+response.status);
      const data=await response.json();
      const value=Number(data.value);
      if(!Number.isFinite(value)||value<0)throw new Error('Invalid counter value');
      return value;
    }catch(e){
      console.warn('ARVION public count service unavailable',method,e);
      return null;
    }finally{clearTimeout(timer)}
  }
  function markLiked(){
    button.classList.add('liked');
    button.setAttribute('aria-pressed','true');
    button.setAttribute('aria-label',copy.already);
    button.title=copy.already;
  }
  button.setAttribute('aria-pressed',get(localStorage,likedKey)==='1'?'true':'false');
  if(get(localStorage,likedKey)==='1')markLiked();
  button.addEventListener('click',async function(){
    if(get(localStorage,likedKey)==='1'){markLiked();notice(copy.already);return}
    if(button.disabled)return;
    button.disabled=true;
    button.setAttribute('aria-busy','true');
    try{
      const value=await query(heartsKey,'hit');
      if(value===null){
        showCount(hearts,await query(heartsKey,'get'));
        button.title=copy.offline;
        notice(copy.offline);
      }else{
        set(localStorage,likedKey,'1');
        showCount(hearts,value);
        markLiked();
        notice(copy.success);
      }
    }finally{
      button.disabled=false;
      button.removeAttribute('aria-busy');
    }
  });
  async function init(){
    const counted=get(sessionStorage,sessionKey)==='1';
    const [viewsValue,heartsValue]=await Promise.all([
      query(viewsKey,counted?'get':'hit'),query(heartsKey,'get')
    ]);
    if(!counted&&viewsValue!==null)set(sessionStorage,sessionKey,'1');
    showCount(visits,viewsValue);
    showCount(hearts,heartsValue);
    if(get(localStorage,likedKey)==='1')markLiked();
  }
  init();
})();