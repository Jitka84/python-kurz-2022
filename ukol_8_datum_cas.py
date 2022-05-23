from datetime import datetime
from time import strptime

    # listky_datum = input("Zadejte datum promítání (DD.MM.RRRR): ")
    # listky_datum = datetime.strptime(listky_datum, "%d.%m.%Y")
    # zacatek_sezony = datetime(2022, 7, 1)
    # konec_sezony = datetime(2022, 8, 31)

    # if listky_datum > zacatek_sezony and listky_datum < konec_sezony:
    #     pocet_listku = int(input("Zadejte počet lístků: "))
    #     if listky_datum <= datetime(2022, 8, 10):
    #         cena_listku = pocet_listku * 250
    #         print(f"Celková cena za lístky je {cena_listku} czk.")
    #     elif listky_datum <= konec_sezony:
    #         cena_listku = pocet_listku * 180
    #         print(f"Celková cena za lístky je {cena_listku} czk.")
    # else:
    #     zacatek_sezony = zacatek_sezony.strftime("%d.%m.%Y")
    #     konec_sezony = konec_sezony.strftime("%d.%m.%Y")
    #     print(f"Mimo letní sezónu od {zacatek_sezony} do {konec_sezony} je kino uzavřené.")

def cena_listku_letni_kino():
    """vypocita cenu listku do letniho kina"""
    listky_datum = input("Zadejte datum promítání (DD.MM.RRRR): ")
    listky_datum = datetime.strptime(listky_datum, "%d.%m.%Y")
    zacatek_sezony = datetime(2022, 7, 1)
    konec_sezony = datetime(2022, 8, 31)

    if listky_datum > zacatek_sezony and listky_datum < konec_sezony:
        pocet_listku = int(input("Zadejte počet lístků: "))
        if listky_datum <= datetime(2022, 8, 10):
            cena_listku = pocet_listku * 250
            return f"Celková cena za lístky je {cena_listku} czk."
        elif listky_datum <= konec_sezony:
            cena_listku = pocet_listku * 180
            return f"Celková cena za lístky je {cena_listku} czk."
    else:
        zacatek_sezony = zacatek_sezony.strftime("%d.%m.%Y")
        konec_sezony = konec_sezony.strftime("%d.%m.%Y")
        return f"Mimo letní sezónu od {zacatek_sezony} do {konec_sezony} je kino uzavřené."

print(cena_listku_letni_kino())
