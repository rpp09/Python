def paraula_mes_llarga(llista_paraules):
    """
    Rep una llista de paraules, mostra la llista i retorna la que té més caràcters.
    Si hi ha diverses amb la mateixa longitud, retorna la primera trobada.
    Si la llista és buida, retorna None.
    """
    print("Llista de paraules:", llista_paraules)  # Mostrar la llista
    
    if not llista_paraules:
        return None
    
    paraula_llarga = llista_paraules[0]
    for paraula in llista_paraules[1:]:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    return paraula_llarga


# --- Proves de la funció ---

llista1 = ["casa", "ordinador", "gat", "automòbil"]
llista2 = ["hola", "adéu", "sí", "programació"]
llista3 = ["a", "ab", "abc", "abcd", "abcde"]
llista4 = []

print("Paraula més llarga:", paraula_mes_llarga(llista1))  # "ordinador"
print("Paraula més llarga:", paraula_mes_llarga(llista2))  # "programació"
print("Paraula més llarga:", paraula_mes_llarga(llista3))  # "abcde"
print("Paraula més llarga:", paraula_mes_llarga(llista4))  # None

