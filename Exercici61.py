def lenp(frase):
    """
    Retorna una llista amb la longitud de cada paraula de la frase.
    """
    # Separa la frase en paraules i aplica len() a cada paraula amb map
    return list(map(len, frase.split()))

# Exemple d'ús
frase = "Hola com estàs avui"
longituds = lenp(frase)
print(longituds)
