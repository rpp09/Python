def llegir_fitxer(nom_fitxer):
    """
    Llegeix el contingut d'un fitxer i el retorna com a llista de línies.
    Controla errors si el fitxer no existeix o hi ha problemes en obrir-lo.
    """
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.readlines()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except IOError:
        print(f"Error: No s'ha pogut obrir el fitxer '{nom_fitxer}'.")
        return None

# Exemple d'ús
nom = "exemple.txt"
linies = llegir_fitxer(nom)

if linies is not None:
    print(f"Contingut de {nom}:")
    for linia in linies:
        print(linia.strip())
