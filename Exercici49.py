def hi_ha_duplicats():
    """
    Demana a l'usuari una llista de números i indica si hi ha duplicats.
    La llista original no es modifica.
    """
    # Demanar els números a l'usuari separats per espais
    entrada = input("Introdueix els números separats per espais: ")
    
    # Convertir la cadena en una llista d'enters
    llista = [int(num) for num in entrada.split()]
    
    # Comprovar duplicats
    if len(llista) != len(set(llista)):
        print("Hi ha duplicats")
    else:
        print("No hi ha duplicats")

# Cridem la funció
hi_ha_duplicats()

