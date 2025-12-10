def elevar_numeros(potencia):
    """
    Retorna una llista amb els 10 primers números elevats a la potència donada.
    """
    return [i**potencia for i in range(10)]

# Exemple d'ús
quadrats = elevar_numeros(2)
cub = elevar_numeros(3)

print("Quadrats:", quadrats)
print("Cubs:", cub)
