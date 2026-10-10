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