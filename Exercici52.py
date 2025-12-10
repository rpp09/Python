def crear_llista_fitxer(nom_fitxer):
    """
    Llegeix un fitxer i retorna una llista amb cada paraula del fitxer com a element.
    """
    llista_paraules = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer:
                # Separem la línia en paraules i afegim a la llista
                paraules = linia.split()
                llista_paraules.extend(paraules)
        return llista_paraules
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer: {nom_fitxer}")
        return []

# Prova de la funció
nom_fitxer = "exemple.txt"  # Canvia-ho pel nom del teu fitxer
llista = crear_llista_fitxer(nom_fitxer)
print("Llista de paraules:", llista)
