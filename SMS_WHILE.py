
#s WHILE CYKLEM
def overeni_cisla():
    """ bezparametrova funkce, s While cyklem - Overi spravnost delky telefoniho cisla zadaneho uzivatelem a vrati text zadane sms"""
    while True:
        cislo = input("Zadej cislo: ")
        if " " in cislo:
            cislo_bezmezer = cislo.replace(" ", "")
        else:
            cislo_bezmezer = cislo
        kontrola_delky = len(cislo_bezmezer) == 9 or (len(cislo_bezmezer) == 13 and cislo_bezmezer[0:4] == "+420")
        if kontrola_delky == True:
            text_sms = input("Zadej text zprávy: ")
            return text_sms
        else:
            print("Špatný formát čísla, zkus to znovu.")
   
def cena_zpravy(text_sms: str):
    """ na zaklade delky sms spocita jeji cenu"""
    delka_zpravy = len(text_sms)
    cena_zpravy = 3
    pocet_znaku = 180
    if delka_zpravy % pocet_znaku == 0:
        return (delka_zpravy // pocet_znaku) * cena_zpravy
    elif delka_zpravy % pocet_znaku != 0:
        return ((delka_zpravy // pocet_znaku) + 1) * cena_zpravy


text_sms = overeni_cisla()
print("Cena sms je " + str(cena_zpravy(text_sms)) + " czk.")
