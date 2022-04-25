class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def __str__(self):
        return f"Název titulu je \"{self.nazev}\", žánr je {self.zanr}."
         
class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def __str__(self):
        return (super()).__str__() + f" Délka filmu je {self.delka} minut."

    def get_celkova_delka(self):
        celkova_delka = self.delka
        return celkova_delka

class Serial(Polozka):
    def __init__(self, nazev,zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
    def __str__(self): 
        return (super()).__str__() + f" Seriál má {self.pocet_epizod} epizod."

    def get_celkova_delka(self):
        celkova_delka = self.pocet_epizod * self.delka_epizody
        return celkova_delka

class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
        self.shlednute_tituly = []

    def pripocti_shlednuti(self, celkova_delka):
        self.delka_sledovani = int(self.delka_sledovani) + int(celkova_delka)
        return self.delka_sledovani

    def pridej_titul(self, titul):
        self.shlednute_tituly.append(titul)

    def vypis_shlednute(self):
        for titul in self.shlednute_tituly:
            print(titul.zanr)       # pro variantu, kdy byl titul pridan jako objekt a muzu si zvolit, jaky atribut chci u objektu vypsat, musi to byt atribut zdedeny z Polozka
            #print(titul)           # pro variantu, kdy byl titul pridan do listu jako str

    def __str__(self):
        return f"Uživatel {self.uzivatelske_jmeno} má celkovou dobu sledování {self.delka_sledovani} minut."


film_1 = Film("Amélie z Monmartru", "komedie", 123)
film_2 = Film("Forrest Gump", "drama", 144)
film_3_ = Film("Pulp Fiction", "akční", 153)
serial_1 = Serial("Simpsnovi","animovaný", 30, 26)
serial_2 = Serial("Teorie velkého třesku", "komedie", 23, 32)
serial_3 = Serial("Červený trpaslík", "sci-fi", 44, 43)
pepa = Uzivatel("pepa")
zuza = Uzivatel("zuza")

print(pepa)
print(zuza)
celkova_delka =int(serial_1.get_celkova_delka())
pepa.pripocti_shlednuti(celkova_delka)
print(pepa)
print(zuza)
celkova_delka = int(film_2.get_celkova_delka())
pepa.pripocti_shlednuti(celkova_delka)
zuza.pripocti_shlednuti(celkova_delka)
print(pepa)
print(zuza)
print()

# print(pepa.shlednute_tituly)       
# pepa.pridej_titul(film_1.nazev)     #pridani titulu do prazdneho seznamu Shlednune.tituly jako str - neumozni pak dale pracovat s atributy titulu
# pepa.pridej_titul(serial_1.nazev)
# print(pepa.shlednute_tituly)
# pepa.vypis_shlednute()
# print()

zuza.pridej_titul(film_1)   #pridani titulu do prazdneho seznamu Shlednune.tituly jako objekt, umozni dale pracovat s atributy - zanr, delka..
zuza.pridej_titul(serial_1)
print(zuza.shlednute_tituly)
print(zuza.shlednute_tituly[0].nazev) #takhle mi to vrati nazev objetu na prvni pozici
zuza.vypis_shlednute()


