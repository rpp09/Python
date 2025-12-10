def dividir(a, b):
    """
    Retorna el resultat de a / b si b no és zero.
    Si b és zero, mostra un missatge d'avís.
    """
    if b == 0:
        print("Error: no es pot dividir per zero!")
        return None
    return a / b

# Exemple d'ús
resultat1 = dividir(10, 2)  # 5.0
print("10 / 2 =", resultat1)

resultat2 = dividir(10, 0)  # Avís
print("10 / 0 =", resultat2)
