def crear_punts(llista):
    """
    Rep una llista de nombres i mostra per pantalla tants punts com el valor de cada nombre.
    Cada element de la llista es mostra en una línia nova.
    """
    for n in llista:
        print('.' * n)


def dibuixar_piramide(alçada):
    """
    Dibuixa una piràmide simètrica de punts amb una alçada donada.
    Utilitza crear_punts() per imprimir cada línia.
    """
    for i in range(1, alçada + 1):
        # Nombre de punts: 2*i - 1 per formar piràmide
        punts = 2 * i - 1
        # Espais per centrar
        espais = alçada - i
        print(' ' * espais + '.' * punts)


# --- Cridar la funció per veure la piràmide ---
dibuixar_piramide(5)

