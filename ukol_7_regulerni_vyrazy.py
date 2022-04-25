import re

posta_navod = "posta.html"

with open(posta_navod, encoding="utf-8") as vstup:
    posta_navod = vstup.readlines()

#print(posta_navod)

posta_navod = [i.replace('\n', " ") for i in posta_navod]

#print(posta_navod)

posta_navod = " ".join(posta_navod)

#print(posta_navod)

posta_navod = re.sub('  +', ' ', posta_navod)

#print(posta_navod)

reg_vyraz_psc_mesto = re.compile("\d{3} \d{2} [\w ]+\d*")
psc_mesto = reg_vyraz_psc_mesto.findall(posta_navod)

for dvojice in psc_mesto:
    print(dvojice)



