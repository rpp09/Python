def longitud(element):
    """
    Rep una llista o una cadena i retorna la seva longitud.
    """
    comptador = 0
    for _ in element:
        comptador += 1
    return comptador


# --- Proves de la funció ---

# Proves amb cadenes
print("Longitud de 'Hola' =", longitud("Hola"))              # 4
print("Longitud de 'Python' =", longitud("Python"))          # 6

# Proves amb llistes
print("Longitud de [1, 2, 3] =", longitud([1, 2, 3]))        # 3
print("Longitud de ['a', 'b', 'c', 'd'] =", longitud(['a','b','c','d']))  # 4

# Prova amb una llista buida
print("Longitud de [] =", longitud([]))                      # 0
