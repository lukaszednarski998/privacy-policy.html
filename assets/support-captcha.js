/* ARVION support: public static site, no private banking/address data in client code. */
(function () {
  'use strict';
  if (typeof supportCopy === 'undefined' || typeof setSupportLang !== 'function') return;
  const PAYPAL_URL = 'https://paypal.me/lukaszbednarski998';
  const PAYPAL_UI = {"en":["Support via PayPal","Voluntary support for app development. Choose your amount in PayPal."],"pl":["Wesprzyj przez PayPal","Dobrowolne wsparcie rozwoju aplikacji. Kwotę wybierasz w PayPal."],"de":["Mit PayPal unterstützen","Freiwillige Unterstützung der App-Entwicklung. Wählen Sie den Betrag bei PayPal."],"fr":["Soutenir avec PayPal","Soutien volontaire au développement des applications. Choisissez le montant sur PayPal."],"es":["Apoyar con PayPal","Apoyo voluntario al desarrollo de las aplicaciones. Elige el importe en PayPal."],"it":["Sostieni con PayPal","Sostegno volontario allo sviluppo delle app. Scegli l'importo su PayPal."],"pt-BR":["Apoiar pelo PayPal","Apoio voluntário ao desenvolvimento dos aplicativos. Escolha o valor no PayPal."],"ja":["PayPalで支援","アプリ開発への任意の支援です。金額はPayPalで選べます。"],"ko":["PayPal로 후원하기","앱 개발을 위한 자발적인 후원입니다. PayPal에서 금액을 선택하세요."],"zh-CN":["通过 PayPal 支持","自愿支持应用开发。请在 PayPal 中选择金额。"],"tr":["PayPal ile destekleyin","Uygulama geliştirmeye gönüllü destek. Tutarı PayPal'da seçin."],"id":["Dukung melalui PayPal","Dukungan sukarela untuk pengembangan aplikasi. Pilih jumlahnya di PayPal."],"ru":["Поддержать через PayPal","Добровольная поддержка разработки приложений. Выберите сумму в PayPal."],"uk":["Підтримати через PayPal","Добровільна підтримка розробки застосунків. Виберіть суму в PayPal."]};
  const LANGUAGE_LABELS = {"en":"English","pl":"Polski","de":"Deutsch","fr":"Français","es":"Español","it":"Italiano","pt-BR":"Português (BR)","ja":"日本語","ko":"한국어","zh-CN":"简体中文","tr":"Türkçe","id":"Bahasa Indonesia","ru":"Русский","uk":"Українська"};
  const PRIVATE_CONTACT = {"en":"Bank transfer and BLIK details are not published on this website. To ask for them, use the Contact button in the main menu.","pl":"Dane do przelewu i BLIK nie są publikowane na tej stronie. Aby je uzyskać, skontaktuj się prywatnie przez przycisk Contact w menu.","de":"Bank- und BLIK-Daten werden auf dieser Website nicht veröffentlicht. Bitte nutze Kontakt im Menü, um sie privat anzufragen.","fr":"Les coordonnées bancaires et BLIK ne sont pas publiées sur ce site. Demandez-les en privé via Contact dans le menu.","es":"Los datos bancarios y de BLIK no se publican aquí. Solicítalos de forma privada mediante Contact en el menú.","it":"I dati bancari e BLIK non sono pubblicati sul sito. Per richiederli in privato usa Contact nel menu.","pt-BR":"Dados bancários e BLIK não são publicados neste site. Para solicitá-los em privado, use Contact no menu.","ja":"銀行振込やBLIKの情報はサイトに公開していません。必要な場合はメニューの Contact から個別にお問い合わせください。","ko":"은행 송금 및 BLIK 정보는 이 사이트에 공개되지 않습니다. 필요한 경우 메뉴의 Contact로 개별 문의해 주세요.","zh-CN":"本站不公开银行转账及 BLIK 信息。如需获取，请通过菜单中的 Contact 私下联系。","tr":"Banka ve BLIK bilgileri bu sitede yayımlanmaz. Bu bilgileri özel olarak istemek için menüdeki Contact seçeneğini kullanın.","id":"Detail transfer bank dan BLIK tidak dipublikasikan di situs ini. Mintalah secara pribadi melalui Contact pada menu.","ru":"Банковские реквизиты и данные BLIK на сайте не публикуются. Запросите их лично через Contact в меню.","uk":"Банківські реквізити та дані BLIK на сайті не публікуються. Запитайте їх особисто через Contact у меню."};
  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  }
  function supportHtml(lang) {
    const copy = PAYPAL_UI[lang] || PAYPAL_UI.en;
    return '<div class="eyebrow">ARVION</div><h2>'+escapeHtml(copy[0])+'</h2>' +
      '<p>'+escapeHtml(copy[1])+'</p><div class="support-highlight">' +
      '<a class="store-button support-paypal-button" href="'+PAYPAL_URL+'" target="_blank" rel="noopener noreferrer">'+escapeHtml(copy[0])+'</a>' +
      '</div><p class="privacy-note">'+escapeHtml(PRIVATE_CONTACT[lang] || PRIVATE_CONTACT.en)+'</p>';
  }
  for (const lang of Object.keys(PAYPAL_UI)) supportCopy[lang] = supportHtml(lang);
  const switcher = document.querySelector('#supportModal .lang-switch');
  if (!switcher) return;
  switcher.replaceChildren();
  for (const [lang,label] of Object.entries(LANGUAGE_LABELS)) {
    const button=document.createElement('button');
    button.type='button';button.className='lang-btn support-lang-btn';
    button.dataset.supportLang=lang;button.textContent=label;
    button.addEventListener('click',()=>{supportLang=lang;setSupportLang(lang);});
    switcher.appendChild(button);
  }
  const locale=(document.documentElement.lang||'en').toLowerCase();
  const lang=Object.keys(PAYPAL_UI).find(k=>k.toLowerCase()===locale) ||
    Object.keys(PAYPAL_UI).find(k=>k.split('-')[0]===locale.split('-')[0]) || 'en';
  supportLang=lang;
  setSupportLang(lang);
})();
