from functools import reduce

def Passar_a_Numero(llista):
    """
    Retorna el número que correspon als dígits d'una llista.
    """
    return reduce(lambda acc, x: acc * 10 + x, llista)

# Exemple d'ús
digits = [3, 4, 1, 5]
numero = Passar_a_Numero(digits)
print(numero)
