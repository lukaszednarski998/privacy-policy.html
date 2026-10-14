/* ARVION SOCIAL CHANNELS: display below each language selector. */
(()=>{
  'use strict';
  const MARKER='arvion-social-links';
  const channels=[
    {name:'TikTok',url:'https://www.tiktok.com/@new_apps_new_games?_r=1&_t=ZN-9AYDhIeKPzC',icon:'M16.7 1.5c.5 2.6 2 4.1 4.8 4.3v4a9.5 9.5 0 0 1-4.8-1.4v8a6.8 6.8 0 1 1-5.9-6.7v4a2.9 2.9 0 1 0 1.9 2.7V1.5z'},
    {name:'YouTube',url:'https://youtube.com/@official_skitella?si=WZI39L_slQlZ7Ly3',icon:'M23 7s-.2-1.7-1-2.5c-1-.9-2-.9-2.5-1C16 3.3 12 3.3 12 3.3s-4 0-7.5.2c-.5.1-1.5.1-2.5 1C1.2 5.3 1 7 1 7S.8 9 .8 11v2C.8 15 1 17 1 17s.2 1.7 1 2.5c1 .9 2.3.9 3 1 2.3.2 7 .2 7 .2s4 0 7.5-.3c.5 0 1.5-.1 2.5-1 .8-.8 1-2.5 1-2.5s.2-2 .2-4v-2C23.2 9 23 7 23 7z M9.5 16V8l7 4z'}
  ];
  const selectors=[
    '.site-language-switch','.lang-switch','nav.lang','nav.langs','nav.languages',
    '.language-switcher','.language-selector','.language-switch','.language-bar',
    '.language-nav','.lang-nav','.language-tabs','.langbar','.langnav','.langs'
  ].join(',');
  function button(channel){
    const link=document.createElement('a');
    link.className='arvion-social-link arvion-social-'+channel.name.toLowerCase();
    link.href=channel.url;link.target='_blank';link.rel='noopener noreferrer';
    link.setAttribute('aria-label',channel.name+' — '+(channel.name==='TikTok'?'@new_apps_new_games':'@official_skitella'));
    const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('viewBox','0 0 24 24');svg.setAttribute('width','22');svg.setAttribute('height','22');
    svg.setAttribute('aria-hidden','true');svg.setAttribute('focusable','false');
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('d',channel.icon);path.setAttribute('fill','currentColor');path.setAttribute('fill-rule','evenodd');
    svg.appendChild(path);link.append(svg,document.createTextNode(channel.name));
    return link;
  }
  function install(){
    const candidates=new Set(document.querySelectorAll(selectors));
    // Cover older pages whose language navigation has no common class.
    document.querySelectorAll('body a[hreflang],body a.lang-btn,body button.lang-btn,body button[data-lang],body button[data-language]').forEach(control=>{
      const nav=control.closest('nav');
      if(nav)candidates.add(nav);
      else if(control.parentElement)candidates.add(control.parentElement);
    });
    document.querySelectorAll('nav').forEach(nav=>{
      const flags=[...nav.querySelectorAll('a,button')].filter(control=>/[\u{1F1E6}-\u{1F1FF}]{2}/u.test(control.textContent));
      if(flags.length>=2)candidates.add(nav);
    });
    const containers=[...candidates].filter(el=>
      !el.closest('.'+MARKER) &&
      (el.querySelectorAll('a[hreflang],a.lang-btn,button.lang-btn,button[data-lang],button[data-language],button[data-support-lang],a.site-lang-btn').length>=2 || [...el.querySelectorAll('a,button')].filter(control=>/[\u{1F1E6}-\u{1F1FF}]{2}/u.test(control.textContent)).length>=2)
    );
    for(const container of containers){
      // Use the innermost group so links remain immediately below its flags.
      if(containers.some(other=>other!==container&&container.contains(other)))continue;
      if(container.nextElementSibling?.classList.contains(MARKER))continue;
      const group=document.createElement('div');group.className=MARKER;
      group.setAttribute('role','group');group.setAttribute('aria-label','TikTok / YouTube');
      channels.forEach(channel=>group.appendChild(button(channel)));
      container.insertAdjacentElement('afterend',group);
    }
  }
  function start(){
    if(document.getElementById('arvion-social-styles'))return;
    const css=document.createElement('style');css.id='arvion-social-styles';
    css.textContent=`
      .arvion-social-links{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;clear:both;margin:14px 0 20px;width:100%;box-sizing:border-box}
      .arvion-social-links .arvion-social-link{display:inline-flex;align-items:center;justify-content:center;gap:9px;min-height:44px;padding:10px 20px;box-sizing:border-box;border:1px solid #706044;border-radius:12px;background:linear-gradient(180deg,#211e19,#101010);color:#f5e2bb;font:700 14px/1.25 Inter,Arial,sans-serif;text-decoration:none;box-shadow:0 4px 12px #0003;transition:transform .15s,border-color .15s,background .15s}
      .arvion-social-links .arvion-social-link:hover{border-color:#e5bb60;background:#292318;transform:translateY(-1px);color:#fff}
      .arvion-social-links .arvion-social-link:focus-visible{outline:3px solid #e5bb60;outline-offset:3px}
      .arvion-social-links .arvion-social-link:active{transform:translateY(1px)}
      .arvion-social-link svg{flex:0 0 22px;display:block}
      .arvion-social-youtube svg{color:#ff5264}.arvion-social-tiktok svg{color:#75e4e0}
      @media(max-width:480px){.arvion-social-links{gap:8px;margin:12px 0 16px}.arvion-social-links .arvion-social-link{padding:10px 14px;min-width:112px;font-size:13px}}
      @media(prefers-reduced-motion:reduce){.arvion-social-links .arvion-social-link{transition:none}}
    `;
    document.head.appendChild(css);install();
    let scheduled=false;
    const observer=new MutationObserver(records=>{
      if(!records.some(record=>record.addedNodes.length))return;
      if(scheduled)return;
      scheduled=true;requestAnimationFrame(()=>{scheduled=false;install();});
    });
    observer.observe(document.body,{childList:true,subtree:true});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});
  else start();
})();

/* ARVION DIRECT PLAY BUTTONS: available apps, all localized catalog/detail pages. */
(()=>{
  'use strict';
  const store={
    'obd-active-exhaust-pro':'https://play.google.com/store/apps/details?id=com.obdactiveeeexhaust.pro',
    'pixel-critters':'https://play.google.com/store/apps/details?id=pl.pixelcritters.game',
    'media-player':'https://play.google.com/store/apps/details?id=com.obdactiveexhaust.mediapro',
    'snake-classic':'https://play.google.com/store/apps/details?id=pl.obdstudio.retrosnakeclassic',
    'kalendarz-zmianowy':'https://play.google.com/store/apps/details?id=com.kalendarzzmianowy.psp.pro',
    'arvion-calculator':'https://play.google.com/store/apps/details?id=com.aplikacjeandroid.arvioncalculator',
    'private-iptv':'https://play.google.com/store/apps/details?id=pl.privateiptv.app',
    'arvion-moto-speed':'https://play.google.com/store/apps/details?id=com.aplikacjeandroid.arvionmotospeed'
  };
  const labels={
    en:'OPEN IN GOOGLE PLAY',pl:'OTWÓRZ W GOOGLE PLAY',de:'IN GOOGLE PLAY ÖFFNEN',
    fr:'OUVRIR SUR GOOGLE PLAY',es:'ABRIR EN GOOGLE PLAY',it:'APRI SU GOOGLE PLAY',
    pt:'ABRIR NO GOOGLE PLAY',ja:'GOOGLE PLAYで開く',ko:'GOOGLE PLAY에서 열기',
    zh:'在 GOOGLE PLAY 中打开',tr:"GOOGLE PLAY'DE AÇ",id:'BUKA DI GOOGLE PLAY',
    ru:'ОТКРЫТЬ В GOOGLE PLAY',uk:'ВІДКРИТИ В GOOGLE PLAY'
  };
  const suffixes=['en','pl','de','fr','es','it','pt-br','ja','ko','zh-cn','tr','id','ru','uk'];
  function destination(path){
    if(!path)return null;
    let name=path.split(/[?#]/)[0].split('/').pop();
    try{name=decodeURIComponent(name)}catch(_){}
    for(const [slug,url] of Object.entries(store)){
      if(name===slug+'.html'||suffixes.some(l=>name===slug+'-'+l+'.html'))return url;
    }
    return null;
  }
  function makeButton(url,compact){
    const a=document.createElement('a');
    const lang=(document.documentElement.lang||'en').toLowerCase().split('-')[0];
    a.className='arvion-store-direct';
    a.textContent=labels[lang]||labels.en;
    a.href=url;a.target='_blank';a.rel='noopener noreferrer';
    a.style.cssText='display:inline-flex;align-items:center;justify-content:center;border:1px solid #e5bb60;border-radius:12px;background:#dfae47;color:#101010;text-decoration:none;font-weight:800;text-align:center;line-height:1.3;'+(compact?'font-size:13px;padding:10px 12px;margin:10px 0 4px':'font-size:16px;padding:14px 22px;margin:6px 0 12px');
    return a;
  }
  function install(){
    if(!location.pathname.includes('/apps/'))return;
    const name=location.pathname.split('/').pop()||'';
    const main=document.querySelector('main');
    if(!main)return;
    if(/^index(?:-(?:en|pl|de|fr|es|it|pt-br|ja|ko|zh-cn|tr|id|ru|uk))?\.html$/.test(name)||!name){
      main.querySelectorAll('a.product[href]').forEach(a=>{
        const url=destination(a.getAttribute('href'));
        if(!url)return;
        const card=a.closest('li')||a.parentElement;
        if(card&&!card.querySelector('.arvion-store-direct'))card.appendChild(makeButton(url,true));
      });
      return;
    }
    const url=destination(name);
    if(!url)return;
    const h1=main.querySelector('h1');
    if(!h1||main.querySelector('[data-arvion-store-primary]'))return;
    const wrap=document.createElement('p');
    wrap.setAttribute('data-arvion-store-primary','true');
    wrap.style.cssText='margin:12px 0 24px';
    wrap.appendChild(makeButton(url,false));
    h1.insertAdjacentElement('afterend',wrap);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',install,{once:true});
  else install();
})();

/* ARVION: consent-based, site-wide Google Analytics 4 tracking.
   Set window.ARVION_GA4_ID to your own G-XXXXXXXXXX measurement ID.
   No analytics cookies, requests or events are sent before visitor consent. */
(()=>{
'use strict';
const GA_ID=(window.ARVION_GA4_ID||'').trim();
const KEY='arvion_analytics_consent_v1';
const lang=(document.documentElement.lang||'en').toLowerCase();
const pl=lang.startsWith('pl');
/* Visible feedback for the existing shared public heart counter. */
(function heartFeedback(){
 const heart=document.getElementById('heartButton');
 if(!heart)return;
 heart.addEventListener('click',function(){
  if(heart.classList.contains('liked')){
   heart.title=pl?'Serduszko zostało już dodane.':'Heart already added.';
   return;
  }
  setTimeout(function(){
   if(heart.classList.contains('liked'))return;
   if(heart.disabled)return;
   const count=document.getElementById('heartCount');
   const failed=heart.classList.contains('stats-offline') ||
     (count&&count.textContent.trim()==='—');
   if(failed){
    const message=pl?'Serduszko nie zostało zapisane: zewnętrzny licznik jest niedostępny. Spróbuj ponownie później.':'Heart not saved: external counter unavailable. Try again later.';
    heart.title=message;
    heart.setAttribute('aria-label',message);
    const node=document.createElement('div');
    node.setAttribute('role','status');node.textContent=message;
    node.style.cssText='position:fixed;bottom:15px;left:50%;transform:translateX(-50%);max-width:min(95vw,420px);padding:12px 16px;background:#242020;color:white;border:1px solid #b84b5a;border-radius:10px;z-index:99999;font:14px system-ui';
    document.body.appendChild(node);setTimeout(()=>node.remove(),5500);
   }
  },11500);
 });
})();

if(!/^G-[A-Z0-9]+$/.test(GA_ID))return;
let consent=null, initialized=false;
try{consent=localStorage.getItem(KEY)}catch(e){}
function start(){
 if(initialized||!/^G-[A-Z0-9]+$/.test(GA_ID)||consent!=='yes')return;
 initialized=true;
 window.dataLayer=window.dataLayer||[];
 window.gtag=window.gtag||function(){dataLayer.push(arguments)};
 const sc=document.createElement('script');sc.async=true;
 sc.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA_ID);
 document.head.appendChild(sc);
 window.gtag('js',new Date());
 window.gtag('config',GA_ID,{anonymize_ip:true});
}
function event(name,params){if(consent==='yes'){start();if(initialized)window.gtag('event',name,params)}}
function notifyConsent(value){
 const wasInitialized=initialized;
 consent=value;
 try{localStorage.setItem(KEY,value)}catch(e){}
 document.getElementById('arvion-analytics-consent')?.remove();
 if(value==='yes')start();
 else if(wasInitialized){
  if(window.gtag)window.gtag('consent','update',{analytics_storage:'denied',ad_storage:'denied'});
  location.reload();
 }
}
function banner(){
 if(consent==='yes'||consent==='no'||document.getElementById('arvion-analytics-consent'))return;
 const el=document.createElement('aside');
 el.id='arvion-analytics-consent';
 el.setAttribute('aria-label',pl?'Zgoda na analitykę':'Analytics consent');
 el.style.cssText='position:fixed;z-index:2147483000;bottom:12px;left:12px;right:12px;max-width:620px;margin:auto;box-sizing:border-box;background:#171717;color:#fff;border:1px solid #666;border-radius:12px;padding:15px 18px;box-shadow:0 4px 25px #0009;font:14px/1.5 system-ui,sans-serif';
 const desc=document.createElement('p');desc.style.margin='0 0 10px';
 desc.textContent=pl?'Czy zgadzasz się na anonimowe statystyki odwiedzin i kliknięć w Google Play (Google Analytics)? Możesz odmówić.':'Allow optional visit and Google Play click analytics (Google Analytics)? You may decline.';
 const link=document.createElement('a');link.href=location.pathname.startsWith('/privacy-policy.html/apps/')?'../site-privacy.html':'site-privacy.html';link.textContent=pl?'Prywatność i statystyki':'Privacy and analytics';link.style.cssText='color:#ffc4ca;text-decoration:underline;display:inline-block;margin-bottom:10px';
 const buttons=document.createElement('div');buttons.style.cssText='display:flex;gap:10px;justify-content:flex-end;flex-wrap:wrap';
 for(const [value,label] of [['no',pl?'Odmów':'Decline'],['yes',pl?'Akceptuję':'Accept']]){
  const b=document.createElement('button');b.type='button';b.textContent=label;
  b.style.cssText='padding:8px 16px;border-radius:7px;border:1px solid #777;background:'+(value==='yes'?'#a02736':'#303030')+';color:white;cursor:pointer;font:inherit';
  b.addEventListener('click',()=>notifyConsent(value));buttons.appendChild(b);
 }
 el.append(desc,link,buttons);document.body.appendChild(el);
}
function storeClick(e){
 const a=e.target.closest?.('a[href]');if(!a)return;
 let u;try{u=new URL(a.href,location.href)}catch(err){return}
 if(u.hostname!=='play.google.com')return;
 let app='unknown';try{app=u.searchParams.get('id')||u.searchParams.get('q')||'unknown'}catch(err){}
 const card=a.closest('[data-product],article,.card,.modal');
 if(card?.dataset?.product)app=card.dataset.product;
 else if(card?.querySelector('h1,h2,h3'))app=card.querySelector('h1,h2,h3').textContent.trim().slice(0,95);
 const appId=u.searchParams.get('id');
 const safeUrl=u.origin+u.pathname+(appId?'?id='+encodeURIComponent(appId):'');
 event('google_play_click',{app_name:app,link_url:safeUrl,link_type:u.pathname.includes('/details')?'app_detail':'store_search',page_path:location.pathname});
}
document.addEventListener('click',storeClick,true);
function settings(){if(!/^G-[A-Z0-9]+$/.test(GA_ID))return;const b=document.createElement('button');b.type='button';b.textContent=pl?'Ustawienia statystyk':'Analytics settings';b.style.cssText='margin:12px;padding:8px 12px;border:1px solid #777;border-radius:8px;background:#222;color:#fff;cursor:pointer';b.addEventListener('click',()=>{try{localStorage.removeItem(KEY)}catch(e){}consent=null;banner()});(document.querySelector('footer')||document.body).appendChild(b)}
document.addEventListener('DOMContentLoaded',()=>{settings();if(consent===null)banner();else start()});
if(document.readyState!=='loading'){settings();if(consent===null)banner();else start()}
window.ARVION_ANALYTICS={track:event,configure:()=>{try{localStorage.removeItem(KEY)}catch(e){}consent=null;banner()}};
})();
