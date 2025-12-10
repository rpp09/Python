def elimina_duplicats():
    """
    Demana a l'usuari una llista de números i retorna una nova llista
    sense elements duplicats, mantenint l'ordre original.
    """
    # Demanar números a l'usuari separats per espais
    entrada = input("Introdueix els números separats per espais: ")
    
    # Convertir la cadena a una llista d'enters
    llista = [int(num) for num in entrada.split()]
    
    # Crear la nova llista sense duplicats
    nova_llista = []
    for elem in llista:
        if elem not in nova_llista:
            nova_llista.append(elem)
    
    print("Llista sense duplicats:", nova_llista)
    return nova_llista

# Cridem la funció
elimina_duplicats()
