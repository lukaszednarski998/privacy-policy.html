/* ARVION: consent-based, site-wide Google Analytics 4 tracking.
   Set window.ARVION_GA4_ID to your own G-XXXXXXXXXX measurement ID.
   No analytics cookies, requests or events are sent before visitor consent. */
(()=>{
'use strict';
const GA_ID=(window.ARVION_GA4_ID||'').trim();
const KEY='arvion_analytics_consent_v1';
const lang=(document.documentElement.lang||'en').toLowerCase();
const pl=lang.startsWith('pl');
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
 consent=value;
 try{localStorage.setItem(KEY,value)}catch(e){}
 document.getElementById('arvion-analytics-consent')?.remove();
 if(value==='yes')start();
}
function banner(){
 if(consent==='yes'||consent==='no'||document.getElementById('arvion-analytics-consent'))return;
 const el=document.createElement('aside');
 el.id='arvion-analytics-consent';
 el.setAttribute('aria-label',pl?'Zgoda na analitykę':'Analytics consent');
 el.style.cssText='position:fixed;z-index:2147483000;bottom:12px;left:12px;right:12px;max-width:620px;margin:auto;box-sizing:border-box;background:#171717;color:#fff;border:1px solid #666;border-radius:12px;padding:15px 18px;box-shadow:0 4px 25px #0009;font:14px/1.5 system-ui,sans-serif';
 const desc=document.createElement('p');desc.style.margin='0 0 10px';
 desc.textContent=pl?'Czy zgadzasz się na anonimowe statystyki odwiedzin i kliknięć w Google Play (Google Analytics)? Możesz odmówić.':'Allow optional visit and Google Play click analytics (Google Analytics)? You may decline.';
 const buttons=document.createElement('div');buttons.style.cssText='display:flex;gap:10px;justify-content:flex-end;flex-wrap:wrap';
 for(const [value,label] of [['no',pl?'Odmów':'Decline'],['yes',pl?'Akceptuję':'Accept']]){
  const b=document.createElement('button');b.type='button';b.textContent=label;
  b.style.cssText='padding:8px 16px;border-radius:7px;border:1px solid #777;background:'+(value==='yes'?'#a02736':'#303030')+';color:white;cursor:pointer;font:inherit';
  b.addEventListener('click',()=>notifyConsent(value));buttons.appendChild(b);
 }
 el.append(desc,buttons);document.body.appendChild(el);
}
function storeClick(e){
 const a=e.target.closest?.('a[href]');if(!a)return;
 let u;try{u=new URL(a.href,location.href)}catch(err){return}
 if(u.hostname!=='play.google.com')return;
 let app='unknown';try{app=u.searchParams.get('id')||u.searchParams.get('q')||'unknown'}catch(err){}
 const card=a.closest('[data-product],article,.card,.modal');
 if(card?.dataset?.product)app=card.dataset.product;
 else if(card?.querySelector('h1,h2,h3'))app=card.querySelector('h1,h2,h3').textContent.trim().slice(0,95);
 event('google_play_click',{app_name:app,link_url:u.origin+u.pathname,link_type:u.pathname.includes('/details')?'app_detail':'store_search',page_path:location.pathname});
}
document.addEventListener('click',storeClick,true);
document.addEventListener('DOMContentLoaded',()=>{if(consent===null)banner();else start()});
if(document.readyState!=='loading'){if(consent===null)banner();else start()}
window.ARVION_ANALYTICS={track:event,configure:()=>{try{localStorage.removeItem(KEY)}catch(e){}consent=null;banner()}};
})();