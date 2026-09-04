from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

support_en = '''<div class="eyebrow">Support ARVION</div><h2>Independent Android development</h2><p>ARVION is an independent project creating Android and Wear OS applications, games and practical tools. The goal is simple: useful software without advertising and without mandatory recurring subscriptions.</p><div class="support-highlight"><h3>Buy once. Keep it.</h3><p>ARVION products are designed around one-time purchases with future improvements and updates included whenever they are released for that product.</p></div><h3>Want to help ARVION grow?</h3><p>If you would like to support future development, please use the <strong>Contact</strong> button in the top menu. Current support details can be provided privately when needed.</p><p class="privacy-note"><strong>Security:</strong> bank account numbers, BLIK phone numbers and private address details are not stored in the public source code of this website.</p><h3>Your feedback matters</h3><p>Bug reports, ideas and suggestions for new Android or Wear OS projects are always welcome. Thank you for every download, purchase, message and recommendation.</p>'''

support_pl = '''<div class="eyebrow">Wesprzyj ARVION</div><h2>Niezależne tworzenie aplikacji</h2><p>ARVION to niezależny projekt tworzący aplikacje, gry i praktyczne narzędzia dla Androida oraz Wear OS. Zasada jest prosta: użyteczne oprogramowanie bez reklam i bez obowiązkowych cyklicznych subskrypcji.</p><div class="support-highlight"><h3>Kupujesz raz. Korzystasz dalej.</h3><p>Produkty ARVION są projektowane jako jednorazowy zakup, a przyszłe poprawki i aktualizacje są wliczone, gdy są wydawane dla danego produktu.</p></div><h3>Chcesz pomóc rozwijać ARVION?</h3><p>Jeżeli chcesz dobrowolnie wesprzeć dalszy rozwój, użyj przycisku <strong>Contact</strong> w górnym menu. Aktualne dane do wsparcia mogą zostać przekazane prywatnie, gdy będą potrzebne.</p><p class="privacy-note"><strong>Bezpieczeństwo:</strong> numery kont bankowych, numer telefonu BLIK i prywatny adres nie są przechowywane w publicznym kodzie źródłowym tej strony.</p><h3>Twoja opinia ma znaczenie</h3><p>Zgłoszenia błędów, pomysły i propozycje nowych projektów na Androida lub Wear OS są zawsze mile widziane. Dziękuję za każde pobranie, zakup, wiadomość i polecenie.</p>'''

replacement = 'const supportCopy={en:`' + support_en + '`,pl:`' + support_pl + '`};'
pattern = r"const supportCopy=\{en:`.*?`,pl:`.*?`\};"
s, count = re.subn(pattern, lambda m: replacement, s, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Expected exactly one Support block, found {count}')

# Remove the later code that injects the creator photo/payment-only elements.
obsolete = r"\n  // Support section: creator photo and transfer title are revealed by the same button as payment details\..*?\n  render\(\);\n  setSupportLang\(supportLang\);"
s, count2 = re.subn(obsolete, '\n  render();\n  setSupportLang(supportLang);', s, count=1, flags=re.S)
if count2 not in (0, 1):
    raise SystemExit('Unexpected Support extension count')

sensitive = [
    '+48 797 053 984',
    '91 1050 0145 1000 0097 0803 3007',
    'PL91105001451000009708033007',
    'ul. Oławska 17/3',
]
remaining = [item for item in sensitive if item in s]
if remaining:
    raise SystemExit('Sensitive Support data still present: ' + ', '.join(remaining))

# Guard the working page structure before writing.
required = ['const products=[', 'DOSTĘPNA TERAZ', 'render();setSupportLang', '</html>']
missing = [item for item in required if item not in s]
if missing:
    raise SystemExit('Page structure guard failed: ' + ', '.join(missing))

p.write_text(s, encoding='utf-8')
print('Support section secured without changing the catalog layout.')
