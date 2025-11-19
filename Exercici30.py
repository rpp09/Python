# Funció per convertir un número binari a enter
def binari_a_enter(binari):
    """
    Rep una cadena representant un número binari i retorna el seu valor enter.
    """
    try:
        enter = int(binari, 2)
        return enter
    except ValueError:
        print("Error: la cadena no és un número binari vàlid.")
        return None


# --- Programa principal ---

binari = input("Introdueix un número binari: ")
enter = binari_a_enter(binari)

if enter is not None:
    print(f"El número binari {binari} en enter és: {enter}")
