# class Balik:

#     def ___init___(self, adresa, hmotnost, doruceno=False):
#         self.adresa = adresa
#         self.hmotnost = hmotnost
#         self.doruceno = doruceno

#     def deliver(self):
#         deliver = True

#     def ___str___(self) -> str:
#         return f'adresa: {self.adresa}\nHmotnost: {self.hmotnost}\nDoruceno: {"ano" if self.doruceno else "ne"}\n


# def ___init___(self) doplnime atributy adresa, hmot, doruc
#init je inicializece, konstruktor - je to zacatek tridy
#tim ze je nastaveno doruceno na false, tak se u baliku nemusi uvadet, neni to povinne

class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno=False
    def deliver(self):
        self.doruceno = True
    def __str__(self) -> str:
        return f'Adresa: {self.adresa}\nHmotnost: {self.hmotnost}\nDoruceno: {"Ano" if self.doruceno else "Ne"}\n'

muj_balik = Balik(adresa='Praha', hmotnost='50')
print(str(muj_balik))
muj_balik.deliver()
print(str(muj_balik))