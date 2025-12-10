def es_primer(n):
    """Comprova si un número és primer."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Llista per guardar els nombres primers
primers = []

# Recorrem els números del 1 al 100
for num in range(1, 101):
    if es_primer(num):
        primers.append(num)

# Mostrar resultats
print("Nombres primers entre 1 i 100:")
print(primers)
print(f"Hi ha {len(primers)} nombres primers entre 1 i 100.")
                                                                                                                                         