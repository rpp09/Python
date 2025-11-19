import random
import time

# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
""")

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot):
    print ("T'estas apropant al talaiot...")
    time.sleep(1)
    print ("Està fosc i és tenebrós...")
    time.sleep(1)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(1)
    gegantamic = random.randint(1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar! Has guanyat 1 punt.\n")
        return True  # Ha encertat
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM\n")
        return False  # Ha perdut

# Funció principal del joc amb sistema de punts
puntuar = 0  # Inicialitzar punts
partidaNova = "si"

while partidaNova.lower() in ["s", "si"]:
    intro()
    nTalaiot = canviTalaiot()
    encert = trobada(nTalaiot)
    
    if encert:
        puntuar += 1
        print(f"Punts actuals: {puntuar}\n")
        partidaNova = input("Vols continuar menjant (jugar)? Introdueixi si o no: ")
        print("\n")
    else:
        print(f"Partida acabada! Has aconseguit {puntuar} punts.")
        puntuar = 0  # Reiniciar punts
        partidaNova = input("Vols començar una nova partida? Introdueixi si o no: ")
        print("\n")

