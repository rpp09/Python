def esta_ordenada():
    """
    Demana a l'usuari una llista de números i indica si està ordenada
    de forma ascendent, descendent o no està ordenada.
    """
    # Demanar els números a l'usuari separats per espais
    entrada = input("Introdueix els números separats per espais: ")
    
    # Convertir la cadena d'entrada en una llista d'enters
    llista = [int(num) for num in entrada.split()]
    
    # Comprovació de l'ordre
    if llista == sorted(llista):
        print("Està ordenada de forma ascendent")
    elif llista == sorted(llista, reverse=True):
        print("Està ordenada de forma descendent")
    else:
        print("No està ordenada")

# Cridem la funció
esta_ordenada()

