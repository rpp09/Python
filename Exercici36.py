def es_de_traspas(any):
    """
    Rep un any i retorna True si és de traspàs, False en cas contrari.
    Un any és de traspàs si és divisible per 4,
    excepte si és divisible per 100, llevat que sigui divisible per 400.
    """
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)


# --- Programa principal ---

any = int(input("Introdueix un any: "))

if es_de_traspas(any):
    print(f"L'any {any} és de traspàs.")
else:
    print(f"L'any {any} no és de traspàs.")
