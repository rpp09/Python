def gran_llista(llista):
    """
    Rep una llista de nombres, mostra la llista i retorna el més gran.
    Si la llista és buida, retorna None.
    """
    print("Llista de nombres:", llista)  # Mostrar la llista
    if not llista:
        return None  # No hi ha elements
    maximo = llista[0]
    for num in llista[1:]:
        if num > maximo:
            maximo = num
    return maximo


# --- Proves de la funció ---

print("El nombre més gran és:", gran_llista([1, 2, 3, 4, 5]))       # 5
print("El nombre més gran és:", gran_llista([10, 20, 5, 15]))       # 20
print("El nombre més gran és:", gran_llista([-5, -1, -10, -3]))     # -1
print("El nombre més gran és:", gran_llista([7.5, 3.2, 9.8, 1.1]))  # 9.8
print("El nombre més gran és:", gran_llista([]))                    # None
