/* ARVION latest catalog additions - 2026-09-03 */
(() => {
  const B = 'assets/latest-site-upload/DO STRONY INTERNETOWEJ/';
  const playSearch = q => 'https://play.google.com/store/search?q=' + encodeURIComponent(q) + '&c=apps';

  const addCard = item => {
    if (!products.some(p => p.id === item.id)) products.push(item);
  };

  addCard({id:'arvion-moto-speed',name:'ARVION Moto Speed',type:'watch',tag:'Phone · Wear OS',img:B+'ARVION MOTO SPEED/ARVION MOTO SPEED 1.png',desc:'GPS motorcycle speedometer with ride data and Wear OS support.',details:true});
  addCard({id:'arvion-pdf',name:'ARVION PDF Toolbox Offline',type:'phone',tag:'Android App',img:B+'ARVION PDF/ARVION PDF 1.jpeg',desc:'Offline PDF, OCR and document toolbox with powerful local processing.',details:true});
  addCard({id:'arvion-phone-diagnostics',name:'ARVION Phone Diagnostics',type:'phone',tag:'Android App',img:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 1.jpeg',desc:'Offline diagnostics, benchmarks and device performance tools.',details:true});
  addCard({id:'battery-guard',name:'ARVION Battery Guard',type:'phone',tag:'Android App',img:B+'BATTERY GUARD/BATTERY GUARD 01.jpeg',desc:'Battery monitoring, charging history, temperature alerts and battery-care tools.',details:true});
  addCard({id:'arvion-calculator',name:'ARVION Calculator',type:'phone',tag:'Android App',img:B+'CALCULATOR/CALCULATOR 1.png',desc:'A practical collection of calculators with scan-assisted input and clear results.',details:true});
  addCard({id:'private-iptv',name:'Private IPTV',type:'phone',tag:'Android App',img:B+'IP TV/IP TV 1.png',desc:'Private IPTV player for user-provided playlists and compatible streaming sources.',details:true});
  addCard({id:'kids-time',name:'Kids Time',type:'phone',tag:'Android App',img:B+'KIDS TIME/KIDS TIME 1.png',desc:'Simple parental time control with PIN protection, alerts and emergency access.',details:true});

  productData['arvion-moto-speed']=mkProduct({
    title:'ARVION Moto Speed',
    icon:B+'ARVION MOTO SPEED/ARVION MOTO SPEED 1.png',
    enSub:'GPS motorcycle speedometer for Android and compatible Wear OS watches.',
    plSub:'Motocyklowy licznik GPS na Androida i kompatybilne zegarki Wear OS.',
    en:'Turn your phone or compatible Wear OS watch into a clear motorcycle speedometer. ARVION Moto Speed uses GPS to show current and maximum speed, distance, ride time, GPS accuracy and related ride information, with phone-and-watch synchronization where supported.',
    pl:'Zmień telefon lub kompatybilny zegarek Wear OS w czytelny licznik motocyklowy. ARVION Moto Speed wykorzystuje GPS do prezentowania aktualnej i maksymalnej prędkości, dystansu, czasu jazdy, dokładności GPS i powiązanych danych przejazdu, a na zgodnych urządzeniach umożliwia synchronizację telefonu z zegarkiem.',
    gallery:[1,2,3,4,5].map(n=>({src:B+`ARVION MOTO SPEED/ARVION MOTO SPEED ${n}.png`,alt:`ARVION Moto Speed ${n}`})).concat([{src:B+'ARVION MOTO SPEED/ARVION MOTO SPEED 6.jpg',alt:'ARVION Moto Speed 6'}]),
    play:playSearch('ARVION Moto Speed')
  });

  productData['arvion-pdf']=mkProduct({
    title:'ARVION PDF Toolbox Offline',
    icon:B+'ARVION PDF/ARVION PDF 1.jpeg',
    enSub:'A complete offline PDF, OCR and document toolbox.',
    plSub:'Kompletny zestaw narzędzi PDF, OCR i dokumentów działający offline.',
    en:'Work with documents directly on your Android device without sending files to a developer cloud. Convert and edit PDFs, use OCR, export recognized content to DOCX, merge and split pages, compress files, add annotations and signatures, manage metadata and use other everyday document tools in one application.',
    pl:'Pracuj z dokumentami bezpośrednio na urządzeniu z Androidem bez wysyłania plików do chmury dewelopera. Konwertuj i edytuj PDF-y, korzystaj z OCR, eksportuj rozpoznaną treść do DOCX, łącz i dziel strony, kompresuj pliki, dodawaj adnotacje i podpisy, zarządzaj metadanymi oraz korzystaj z innych codziennych narzędzi dokumentowych w jednej aplikacji.',
    gallery:[{src:B+'ARVION PDF/ARVION PDF 1.jpeg',alt:'ARVION PDF 1'},{src:B+'ARVION PDF/ARVION PDF 2.jpeg',alt:'ARVION PDF 2'},{src:B+'ARVION PDF/ARVION PDF 3.jpeg',alt:'ARVION PDF 3'},{src:B+'ARVION PDF/ARVION PDF 4.png',alt:'ARVION PDF 4'},{src:B+'ARVION PDF/ARVION PDF 5.png',alt:'ARVION PDF 5'}],
    play:playSearch('ARVION PDF Toolbox Offline')
  });

  productData['arvion-phone-diagnostics']=mkProduct({
    title:'ARVION Phone Diagnostics',
    icon:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 1.jpeg',
    enSub:'Offline phone diagnostics, benchmarks and performance tools.',
    plSub:'Diagnostyka telefonu, benchmarki i narzędzia wydajności działające offline.',
    en:'Check the condition and performance of your Android device in one place. ARVION Phone Diagnostics presents storage, RAM, battery, temperature and system information, includes CPU, memory and storage performance tests, keeps local test history and provides practical recovery and management shortcuts.',
    pl:'Sprawdź kondycję i wydajność urządzenia z Androidem w jednym miejscu. ARVION Phone Diagnostics pokazuje informacje o pamięci, RAM, baterii, temperaturze i systemie, oferuje testy CPU, pamięci RAM i pamięci masowej, przechowuje lokalną historię wyników oraz udostępnia praktyczne narzędzia i skróty do zarządzania wydajnością.',
    gallery:[{src:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 1.jpeg',alt:'ARVION Phone Diagnostics 1'},{src:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 2.jpeg',alt:'ARVION Phone Diagnostics 2'},{src:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 3.jpeg',alt:'ARVION Phone Diagnostics 3'},{src:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics 5.jpeg',alt:'ARVION Phone Diagnostics 5'},{src:B+'ARVION PHONE DIAGNOSTIC/ARVION Phone Diagnostics.jpeg',alt:'ARVION Phone Diagnostics'}],
    play:playSearch('ARVION Phone Diagnostics')
  });

  productData['battery-guard']=mkProduct({
    title:'ARVION Battery Guard',
    icon:B+'BATTERY GUARD/BATTERY GUARD 01.jpeg',
    enSub:'Battery monitoring and charging-care tools for Android.',
    plSub:'Monitorowanie baterii i narzędzia dbania o ładowanie na Androidzie.',
    en:'Monitor battery level, charging status, temperature and other information available from your device. Battery Guard adds charging history, charge-limit and temperature alerts, battery-care analytics, local statistics and reports to help you better understand everyday charging.',
    pl:'Monitoruj poziom baterii, stan ładowania, temperaturę i inne informacje udostępniane przez urządzenie. Battery Guard oferuje historię ładowania, alerty limitu naładowania i temperatury, analizę dbania o baterię, lokalne statystyki oraz raporty pomagające lepiej kontrolować codzienne ładowanie.',
    gallery:[1,2,3,4,5].map(n=>({src:B+`BATTERY GUARD/BATTERY GUARD 0${n}.jpeg`,alt:`ARVION Battery Guard ${n}`})),
    play:playSearch('ARVION Battery Guard')
  });

  productData['arvion-calculator']=mkProduct({
    title:'ARVION Calculator',
    icon:B+'CALCULATOR/CALCULATOR 1.png',
    enSub:'A practical multi-calculator toolbox with scan-assisted input.',
    plSub:'Praktyczny zestaw wielu kalkulatorów z możliwością wspomagania skanowaniem.',
    en:'Keep useful calculations in one clear application. ARVION Calculator combines multiple calculator tools with simple input, translated results and scan-assisted workflows that can help read values before calculation. It is designed for fast everyday use without unnecessary complexity.',
    pl:'Miej przydatne obliczenia w jednej czytelnej aplikacji. ARVION Calculator łączy wiele narzędzi kalkulatora z prostym wprowadzaniem danych, przetłumaczonymi wynikami oraz funkcjami wspomaganymi skanowaniem, które mogą pomóc odczytać wartości przed wykonaniem obliczenia. Aplikacja została zaprojektowana do szybkiego, codziennego użycia.',
    gallery:[{src:B+'CALCULATOR/CALCULATOR 1.png',alt:'ARVION Calculator 1'},{src:B+'CALCULATOR/CALCULATOR 2 (1).png',alt:'ARVION Calculator 2'},{src:B+'CALCULATOR/CALCULATOR 2 (2).png',alt:'ARVION Calculator 3'},{src:B+'CALCULATOR/CALCULATOR 2 (4).png',alt:'ARVION Calculator 4'}],
    play:playSearch('ARVION Calculator')
  });

  productData['private-iptv']=mkProduct({
    title:'Private IPTV',
    icon:B+'IP TV/IP TV 1.png',
    enSub:'A private IPTV player for playlists and sources supplied by the user.',
    plSub:'Prywatny odtwarzacz IPTV dla list i źródeł dodawanych przez użytkownika.',
    en:'Play IPTV content from compatible playlists and streaming addresses that you add yourself. Private IPTV focuses on a clean TV-style interface, playlist handling and playback controls. The application does not provide channel lists or access rights to third-party content; the user is responsible for the sources they add.',
    pl:'Odtwarzaj treści IPTV z kompatybilnych list i adresów strumieniowych, które dodajesz samodzielnie. Private IPTV oferuje czytelny interfejs telewizyjny, obsługę list oraz sterowanie odtwarzaniem. Aplikacja nie dostarcza list kanałów ani praw dostępu do treści podmiotów trzecich — za dodawane źródła odpowiada użytkownik.',
    gallery:[1,2,3,4,5].map(n=>({src:B+`IP TV/IP TV ${n}.png`,alt:`Private IPTV ${n}`})),
    play:playSearch('Private IPTV ARVION')
  });

  productData['kids-time']=mkProduct({
    title:'Kids Time',
    icon:B+'KIDS TIME/KIDS TIME 1.png',
    enSub:'Simple parental time control with PIN protection and emergency access.',
    plSub:'Prosta kontrola czasu dziecka z ochroną PIN i dostępem awaryjnym.',
    en:'A straightforward parental-control utility focused on ease of use. Set protected time limits with PIN confirmation, use an alarm after repeated incorrect PIN attempts and keep a separate emergency access procedure for situations when normal unlocking is not possible.',
    pl:'Proste narzędzie kontroli rodzicielskiej, w którym najważniejsza jest łatwość obsługi. Ustawiaj chronione limity czasu z potwierdzeniem PIN, korzystaj z alarmu po kolejnych błędnych próbach wpisania kodu oraz z osobnej procedury awaryjnego dostępu, gdy standardowe odblokowanie nie jest możliwe.',
    gallery:[{src:B+'KIDS TIME/KIDS TIME 1.png',alt:'Kids Time 1'},{src:B+'KIDS TIME/KIDS TIME 02.png',alt:'Kids Time 2'},{src:B+'KIDS TIME/KIDS TIME 04.png',alt:'Kids Time 3'},{src:B+'KIDS TIME/KIDS TIME 93.png',alt:'Kids Time 4'},{src:B+'KIDS TIME/KIEDS TIME 05.png',alt:'Kids Time 5'}],
    play:playSearch('Kids Time ARVION')
  });

  // Exact OBD Active Exhaust Pro store link supplied by the developer.
  const oldObd='https://play.google.com/store/search?q=OBD%20Active%20Exhaust%20Pro&c=apps';
  const newObd='https://play.google.com/store/apps/details?id=com.obdactiveeeexhaust.pro';
  if (productData.obd && productData.obd.copy) {
    ['en','pl'].forEach(lang => productData.obd.copy[lang] = productData.obd.copy[lang].replace(oldObd,newObd));
  }

  // Support section: creator photo and transfer title are revealed by the same button as payment details.
  const supportPhoto=B+'DO WSTAWIENIA DO KONT BANKOWYCH.png';
  if (!supportCopy.en.includes('support-photo-wrap')) {
    supportCopy.en=supportCopy.en.replace('<h3>International bank transfer details</h3>',`<div class="support-photo-wrap hidden-data"><img src="${supportPhoto}" alt="Łukasz — creator of ARVION"><span>Łukasz — creator of ARVION</span></div><div class="support-value hidden-data transfer-title"><span>Transfer title</span><strong>Creator support</strong></div><h3>International bank transfer details</h3>`);
    supportCopy.pl=supportCopy.pl.replace('<h3>Dane do przelewu międzynarodowego</h3>',`<div class="support-photo-wrap hidden-data"><img src="${supportPhoto}" alt="Łukasz — twórca ARVION"><span>Łukasz — twórca ARVION</span></div><div class="support-value hidden-data transfer-title"><span>Tytuł przelewu</span><strong>Wsparcie twórców</strong></div><h3>Dane do przelewu międzynarodowego</h3>`);
  }

  const style=document.createElement('style');
  style.textContent=`
    .support-photo-wrap{margin:20px auto;max-width:300px;text-align:center;border:1px solid var(--line);border-radius:18px;background:#080808;padding:12px;transition:.25s ease}
    .support-photo-wrap img{display:block;width:100%;height:auto;border-radius:12px}
    .support-photo-wrap span{display:block;margin-top:9px;color:#bba66f;font-size:12px;font-weight:800}
    .support-photo-wrap.hidden-data{filter:none;opacity:0;max-height:0;margin-top:0;margin-bottom:0;padding-top:0;padding-bottom:0;border-width:0;overflow:hidden;pointer-events:none}
    .support-photo-wrap.hidden-data.revealed{opacity:1;max-height:520px;margin-top:20px;margin-bottom:20px;padding:12px;border-width:1px;pointer-events:auto}
    .transfer-title{margin:16px 0}
  `;
  document.head.appendChild(style);

  render();
  setSupportLang(supportLang);
})();
