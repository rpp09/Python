def crear_repetits(n, caracter):
    """
    Rep un nombre enter n i un caràcter, 
    i retorna el caràcter repetit n vegades.
    """
    if n <= 0:
        return ""  # Si n és 0 o negatiu, retorna cadena buida
    return caracter * n


# --- Proves de la funció ---

print("Prova 1:", crear_repetits(5, "a"))   # "aaaaa"
print("Prova 2:", crear_repetits(3, "b"))   # "bbb"
print("Prova 3:", crear_repetits(0, "c"))   # ""
print("Prova 4:", crear_repetits(7, "*"))   # "*******"
print("Prova 5:", crear_repetits(1, "z"))   # "z"
