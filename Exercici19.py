# Funció per sumar tots els elements d'una llista
def sumar_llista(llista):
    """
    Rep una llista de nombres i retorna la suma de tots els elements.
    """
    suma = 0
    for x in llista:
        suma += x
    return suma

# Funció per multiplicar tots els elements d'una llista
def multiplicar_llista(llista):
    """
    Rep una llista de nombres i retorna el producte de tots els elements.
    """
    if not llista:
        return 0  # Considerem que el producte d'una llista buida és 0
    producte = 1
    for x in llista:
        producte *= x
    return producte

# Funció per invertir una llista o cadena
def invertir(element):
    """
    Rep una llista o cadena i retorna la seva inversa.
    """
    return element[::-1]


# --- Proves de les funcions ---

# Proves sumar_llista
print("sumar_llista([1, 2, 3, 4]) =", sumar_llista([1, 2, 3, 4]))        # 10
print("sumar_llista([5, 10, -3]) =", sumar_llista([5, 10, -3]))          # 12
print("sumar_llista([]) =", sumar_llista([]))                              # 0

# Proves multiplicar_llista
print("multiplicar_llista([1, 2, 3, 4]) =", multiplicar_llista([1, 2, 3, 4]))  # 24
print("multiplicar_llista([5, 10, -3]) =", multiplicar_llista([5, 10, -3]))    # -150
print("multiplicar_llista([]) =", multiplicar_llista([]))                          # 0

# Proves invertir
print("invertir([1, 2, 3, 4]) =", invertir([1, 2, 3, 4]))           # [4, 3, 2, 1]
print("invertir('Python') =", invertir("Python"))                     # 'nohtyP'
print("invertir([]) =", invertir([]))                                 # []
