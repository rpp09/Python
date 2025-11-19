def mostrar_majors_que(tupla_nums, x):
    """
    Rep una tupla de nombres enters i un número x,
    i imprimeix tots els elements de la tupla que són majors que x.
    """
    print(f"Elements superiors a {x}:")
    for num in tupla_nums:
        if num > x:
            print(num, end=' ')
    print()  # Salt de línia al final


# --- Programa principal ---

# Demanar a l'usuari els valors de la tupla
valors = []
n = int(input("Quants nombres vols introduir a la tupla? "))
for i in range(n):
    valor = int(input(f"Introdueix el nombre {i+1}: "))
    valors.append(valor)

# Convertir la llista a tupla
tupla_valors = tuple(valors)

# Mostrar els valors majors de 18
mostrar_majors_que(tupla_valors, 18)
