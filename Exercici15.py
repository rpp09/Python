def gran(a, b):
    """
    Retorna el nombre més gran entre a i b.
    """
    if a > b:
        return a
    else:
        return b


# --- Proves de la funció ---

print("Prova 1: gran(5, 3) =", gran(5, 3))          # 5
print("Prova 2: gran(10, 20) =", gran(10, 20))      # 20
print("Prova 3: gran(-4, -9) =", gran(-4, -9))      # -4
print("Prova 4: gran(7.5, 7.2) =", gran(7.5, 7.2))  # 7.5
print("Prova 5: gran(8, 8) =", gran(8, 8))          # 8
