def coincidir_valor_index(llista):
    """
    Retorna el nombre d'elements on el valor coincideix amb l'índex.
    """
    count = 0
    for idx, valor in enumerate(llista):
        if idx == valor:
            count += 1
    return count

# Exemple d'ús
numeros = [0, 2, 3, 3, 4]  # Aquí pots posar els teus números
resultat = coincidir_valor_index(numeros)
print("Nombre d'elements que coincideixen valor i índex:", resultat)
