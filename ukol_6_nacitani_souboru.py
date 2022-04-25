nacteny_soubor = input("Zadej název souboru: ")
if ".txt" not in nacteny_soubor:
    nacteny_soubor = nacteny_soubor + ".txt"
else:
    nacteny_soubor = nacteny_soubor

with open(nacteny_soubor, encoding="utf-8") as vstup:
    nacteny_soubor = vstup.readlines()

znacky_split = [znacka.split() for znacka in nacteny_soubor]

# for znacka in znacky_split:
#     if "." in znacka[1]:
#         znacka = [znacka[0], znacka[1].replace(".",",")]
#         print(znacka)
#     print(znacka)

znacky_split = [[znacka[0], float(znacka[1].replace(",","."))] for znacka in znacky_split]

#celkem_najeto = []

# for znacka in znacky_split:
#     najeto = znacka[1]
#     celkem_najeto.append(najeto)

celkem_najeto = [znacka[1] for znacka in znacky_split]

print(f"Celkem bylo najeto {sum(celkem_najeto)} km.")
