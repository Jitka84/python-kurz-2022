def nasobeni(a,b):
    return a*b

print(nasobeni(2,5))

#hotel
def total_price(persons, breakfast = False):
    noc = 10
    snidane = 5
    if breakfast == True:
        vysledek = (noc * persons) + (snidane * persons)
    else:
        vysledek = (noc * persons)
    return vysledek

print(total_price(3,True))




def month_of_birth(rodne_cislo):
    #rodne_cislo = str(input("zadej rodné číslo: "))
    rodne_cislo = str(rodne_cislo)
    mesic_narozeni = rodne_cislo[2:4]
    mesic_int = int(mesic_narozeni)
    if mesic_int > 50:
        mesic_int = mesic_int - 50
    return mesic_int

print(month_of_birth(8455044609))

def ukaz_priklad():
    """Spočítá ukázkový příklad a výsledek vypíše (nevrátí!)"""
    vysledek_ = podel_nulou(3)       # řádek 13
    print(vysledek_)

ukaz_priklad()    

