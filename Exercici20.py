def es_palindrom(paraula):
    """
    Rep una paraula i retorna True si és un palíndrom,
    és a dir, si es llegeix igual d'esquerra a dreta i de dreta a esquerra.
    Ignorem majúscules/minúscules.
    """
    # Convertim la paraula a minúscules per comparar sense diferenciar majúscules
    paraula = paraula.lower()
    # Comprovem si és igual a la seva inversa
    return paraula == paraula[::-1]


# --- Proves de la funció ---

print("Prova 1: es_palindrom('radar') =", es_palindrom('radar'))  # True
print("Prova 2: es_palindrom('ara') =", es_palindrom('ara'))      # True
print("Prova 3: es_palindrom('civic') =", es_palindrom('civic'))  # True
print("Prova 4: es_palindrom('rallar') =", es_palindrom('rallar'))# True
print("Prova 5: es_palindrom('Python') =", es_palindrom('Python'))# False
print("Prova 6: es_palindrom('Simis') =", es_palindrom('Simis'))  # True
print("Prova 7: es_palindrom('refer') =", es_palindrom('refer'))  # True
print("Prova 8: es_palindrom('hola') =", es_palindrom('hola'))    # False

