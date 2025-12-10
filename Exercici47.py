def eliminarcapicua(llista):
    """
    Aquesta funció elimina el primer i l'últim element d'una llista
    i retorna una nova llista amb els elements restants.
    """
    if len(llista) <= 2:
        # Si la llista té dos o menys elements, el resultat és una llista buida
        return []
    else:
        return llista[1:-1]

# Prova de la funció
llista_original = [1, 2, 3, 4, 5]
llista_modificada = eliminarcapicua(llista_original)

print("Llista original:", llista_original)
print("Llista modificada:", llista_modificada)
