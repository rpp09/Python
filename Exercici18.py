def es_vocal(caracter):
    """
    Rep un caràcter i retorna True si és una vocal (a, e, i, o, u), 
    i False en cas contrari. Considera majúscules i minúscules.
    """
    if len(caracter) != 1:
        return False  # No és un únic caràcter
    return caracter.lower() in 'aeiou'


# --- Proves de la funció ---

print("Prova 1: es_vocal('a') =", es_vocal('a'))    # True
print("Prova 2: es_vocal('E') =", es_vocal('E'))    # True
print("Prova 3: es_vocal('b') =", es_vocal('b'))    # False
print("Prova 4: es_vocal('O') =", es_vocal('O'))    # True
print("Prova 5: es_vocal('z') =", es_vocal('z'))    # False
print("Prova 6: es_vocal('ae') =", es_vocal('ae'))  # False (més d’un caràcter)
