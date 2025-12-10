def llista_a_diccionari(llista):
    """
    Retorna un diccionari amb els elements de la llista com a clau
    i el seu índex com a valor.
    """
    return {valor: idx for idx, valor in enumerate(llista)}

# Exemple d'ús
elements = ['casa', 'cotxe', 'cadira', 'taula']
resultat = llista_a_diccionari(elements)
print(resultat)
