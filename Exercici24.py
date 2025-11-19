def crear_punts(llista):
    """
    Rep una llista de nombres i mostra per pantalla tants punts com el valor de cada nombre.
    Cada element de la llista es mostra en una línia nova.
    """
    for n in llista:
        print('.' * n)


# --- Proves de la funció ---

print("Prova 1: crear_punts([2, 3, 4])")
crear_punts([2, 3, 4])
# Sortida esperada:
# ..
# ...
# ....

print("\nProva 2: crear_punts([1, 5, 2])")
crear_punts([1, 5, 2])
# Sortida esperada:
# .
# .....
# ..

print("\nProva 3: crear_punts([0, 3, 1])")
crear_punts([0, 3, 1])
# Sortida esperada:
#
# ...
# .
