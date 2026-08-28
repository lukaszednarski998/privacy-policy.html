from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old_en = '''<p>My name is <strong>Łukasz, I am 40 years old</strong>. For more than 20 years I have worked in the <strong>Polish State Fire Service</strong>. It is a job that has taught me responsibility, patience, teamwork and the importance of finding a solution even when the situation is difficult.</p><p>Public service is meaningful work, but the salary is modest, so I also work in distribution. I drive trucks and deliver goods to stores including <strong>Dino and Biedronka</strong>.'''
new_en = '''<p>My name is <strong>Łukasz, I am 40 years old</strong>. For more than 20 years I have worked in distribution. I drive trucks and deliver goods to stores including <strong>Dino and Biedronka</strong>.'''

old_pl = '''<p>Mam na imię <strong>Łukasz, mam 40 lat</strong>. Od ponad 20 lat pracuję w <strong>Państwowej Straży Pożarnej</strong>. To praca, która nauczyła mnie odpowiedzialności, cierpliwości, pracy zespołowej i tego, że nawet w trudnej sytuacji zawsze trzeba szukać rozwiązania.</p><p>Służba daje mi ogromną satysfakcję, jednak ze względu na niewysokie wynagrodzenie pracuję również dodatkowo w dystrybucji. Jeżdżę samochodami ciężarowymi i rozwożę towary między innymi do marketów <strong>Dino i Biedronka</strong>.'''
new_pl = '''<p>Mam na imię <strong>Łukasz, mam 40 lat</strong>. Od ponad 20 lat pracuję w dystrybucji. Jeżdżę samochodami ciężarowymi i rozwożę towary między innymi do marketów <strong>Dino i Biedronka</strong>.'''

if old_en not in s:
    raise SystemExit('English support text not found')
if old_pl not in s:
    raise SystemExit('Polish support text not found')

s = s.replace(old_en, new_en, 1)
s = s.replace(old_pl, new_pl, 1)
p.write_text(s, encoding='utf-8')
