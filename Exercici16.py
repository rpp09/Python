def gran_de_tres(a, b, c):
    """
    Retorna el nombre més gran entre a, b i c.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# --- Proves de la funció ---

print("Prova 1: gran_de_tres(5, 3, 9) =", gran_de_tres(5, 3, 9))        # 9
print("Prova 2: gran_de_tres(10, 20, 15) =", gran_de_tres(10, 20, 15))  # 20
print("Prova 3: gran_de_tres(-4, -9, -1) =", gran_de_tres(-4, -9, -1))  # -1
print("Prova 4: gran_de_tres(7.5, 7.2, 7.5) =", gran_de_tres(7.5, 7.2, 7.5))  # 7.5
print("Prova 5: gran_de_tres(8, 8, 8) =", gran_de_tres(8, 8, 8))        # 8
