class Auto:
    def __init__(self, reg_znacka, typ_vozidla, najete_km):
        self.reg_znacka = reg_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True

    def pujc_auto(self):
        """zmeni stav dostupnosti a potvrdi uspesne zapujceni"""
        if self.dostupnost == True:
            self.dostupnost = False
            return f"Potvrzuji zapůjčení vozidla {self.reg_znacka} {self.typ_vozidla}."
        else:
            return f"Vozidlo {self.reg_znacka} {self.typ_vozidla} není k dispozici."
    
    def vrat_auto(self, najeto_po_vraceni, pocet_dni):
        """zkontroluje a prepise stav tachometru pri vraceni, spocita cenu za pocet pujcenych dnu"""
        if int(pocet_dni) < 7:
            cena_pujceni = pocet_dni * 400
        else:
            cena_pujceni = pocet_dni * 300
        if self.dostupnost == False:
            self.dostupnost = True
            if najeto_po_vraceni < self.najete_km:
                return "Chybně zadaný stav tachometru." 
            else:
                self.najete_km = najeto_po_vraceni
                return f"Vozidlo {self.reg_znacka} {self.typ_vozidla} bylo vráceno. Cena za půjčení je {cena_pujceni} czk."
        else:
            return "Error. Vozidlo nelze vrátit."

    def __str__(self):
        return f"Registrační značka vozidla je {self.reg_znacka}, typ vozidla je {self.typ_vozidla}, stav tachometru {self.najete_km} km."

auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)

print()

print(auto1.pujc_auto())
print(auto1)
print(auto1.pujc_auto())
print(auto1.vrat_auto(77777,3))
print(auto1)

print()

def uzivatel_pujceni_auta():
    """zepta se uzivatele, jake auto chce pujcit a v pripade, ze je auto volne, pujceni potvrdi, nedovoli pujcit stejne auto 2x"""
    vyber_auta = input("Jaký typ vozidla chcete půjčit: Škoda nebo Peugeot? ")
    if vyber_auta == "Škoda":
        print(auto2)
        return auto2.pujc_auto()
    elif vyber_auta == "Peugeot":
        print(auto1)
        return auto1.pujc_auto()
    else:
        return "Zadané vozidlo není v databázi."

print(uzivatel_pujceni_auta())
print(uzivatel_pujceni_auta())
print(uzivatel_pujceni_auta())
    

