baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

balik_predan = input("Zadejte číslo baliku: ")

if balik_predan not in baliky:      
    print("Balík není v evidenci.")
elif baliky[balik_predan] == True:
    print("Balík " + balik_predan + " byl předán kurýrovi.")
elif baliky[balik_predan] == False:
    print("Balík " + balik_predan + " zatím nebyl předán kurýrovi.")
#else:     #chtela jsem moznost, ze se zada neexistujici cislo baliku resit pres  ELSE: ale nefungovalo mi to - nevypsala print hlaska, ale Keyerror
#    print("Balík není v evidenci")
print()

if balik_predan in baliky:
    if baliky[balik_predan] :           # to same jako baliky[balik_predan] == True
      print(f"Balík {balik_predan} byl předán kurýrovi.")
    else:
      print(f"Balík {balik_predan} nebyl dosud předán kurýrovi.")
else:
    print(f"Balík {balik_predan} není v evidenci.")

zvirata = ["lev", "pes", "kun"]
print("peäs" in zvirata)