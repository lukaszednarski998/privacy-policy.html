from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

START = '/* ARVION AVAILABILITY START */'
END = '/* ARVION AVAILABILITY END */'

css = r'''
/* ARVION AVAILABILITY START */
.availability-status{display:flex;align-items:center;gap:8px;margin:12px 0 0;padding:9px 11px;border-radius:12px;font-size:11px;font-weight:900;letter-spacing:.035em;line-height:1.35}.availability-status:before{content:'';width:8px;height:8px;border-radius:50%;flex:0 0 8px}.availability-status.available{color:#bff5c9;border:1px solid rgba(73,190,96,.55);background:rgba(36,125,54,.13)}.availability-status.available:before{background:#49d66a;box-shadow:0 0 10px rgba(73,214,106,.75)}.availability-status.soon{color:#f2d99d;border:1px solid rgba(216,170,67,.42);background:rgba(216,170,67,.07)}.availability-status.soon:before{background:#d8aa43}.modal-availability{margin:8px 0 14px;max-width:520px}
/* ARVION AVAILABILITY END */
'''

if START not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

# The store listing currently uses the older working title in the catalog.
# Show the public product name requested by the owner.
s = s.replace("name:'OBD Active Exhaust Pro'", "name:'OBD Active Sound'", 1)
s = s.replace("title:'OBD Active Exhaust Pro'", "title:'OBD Active Sound'", 1)

js_start = '<!-- ARVION AVAILABILITY SCRIPT START -->'
js_end = '<!-- ARVION AVAILABILITY SCRIPT END -->'
script = r'''<!-- ARVION AVAILABILITY SCRIPT START -->
<script>
(function(){
  const AVAILABLE_NAMES=['obd active sound','obd active exhaust pro'];
  const statusFor=(name)=>AVAILABLE_NAMES.some(x=>(name||'').toLowerCase().includes(x))
    ? {cls:'available',text:'DOSTĘPNA TERAZ · AVAILABLE NOW'}
    : {cls:'soon',text:'DOSTĘPNA WKRÓTCE · COMING SOON'};
  function applyCardStatus(){
    document.querySelectorAll('.card').forEach(card=>{
      const h=card.querySelector('h3');
      if(!h||card.querySelector('.availability-status')) return;
      const st=statusFor(h.textContent);
      const el=document.createElement('div');
      el.className='availability-status '+st.cls;
      el.textContent=st.text;
      const body=card.querySelector('.body')||card;
      body.appendChild(el);
    });
  }
  function applyModalStatus(){
    const modal=document.querySelector('#productModal');
    if(!modal) return;
    const h=modal.querySelector('.product-head h2, h2');
    if(!h) return;
    let el=modal.querySelector('.modal-availability');
    if(!el){el=document.createElement('div');el.className='availability-status modal-availability';h.insertAdjacentElement('afterend',el);}
    const st=statusFor(h.textContent);el.className='availability-status modal-availability '+st.cls;el.textContent=st.text;
  }
  function run(){applyCardStatus();applyModalStatus();}
  document.addEventListener('DOMContentLoaded',()=>{run();setTimeout(run,250);setTimeout(run,1000);});
  document.addEventListener('click',()=>setTimeout(run,40));
  new MutationObserver(run).observe(document.documentElement,{childList:true,subtree:true});
})();
</script>
<!-- ARVION AVAILABILITY SCRIPT END -->'''
if js_start not in s:
    s = s.replace('</body>', script + '\n</body>', 1)

p.write_text(s, encoding='utf-8')
