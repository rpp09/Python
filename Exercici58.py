def elements_parells(llista):
    """
    Retorna els elements que es troben en posicions parells d'una llista.
    """
    return [llista[i] for i in range(len(llista)) if i % 2 == 0]

# Exemple d'ús
paraules = ["aigua", "arbre", "casa", "cotxe", "llibre", "gat"]
resultat = elements_parells(paraules)
print("Elements en posicions parells:", resultat)
