def superposicio(llista1, llista2):
    """
    Rep dues llistes i retorna True si hi ha algun element en comú,
    False en cas contrari.
    """
    for element in llista1:
        if element in llista2:
            return True
    return False


# Proves de la funció 

print("Prova 1:", superposicio([1, 2, 3], [3, 4, 5]))    # True, 3 està en comú
print("Prova 2:", superposicio([10, 20], [30, 40]))      # False, no hi ha elements comuns
print("Prova 3:", superposicio(['a', 'b'], ['c', 'a'])) # True, 'a' està en comú
print("Prova 4:", superposicio([], [1, 2]))             # False, llista buida
print("Prova 5:", superposicio([1, 2, 3], []))          # False, llista buida
