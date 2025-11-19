def filtrar_paraules(llista_paraules, x):
    """
    Rep una llista de paraules i un nombre x,
    mostra la llista original i retorna una nova llista amb
    les paraules que tinguin més de x caràcters.
    """
    print("Llista original:", llista_paraules)
    
    resultat = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat


# --- Proves de la funció ---

llista1 = ["casa", "ordinador", "gat", "automòbil"]
llista2 = ["hola", "adéu", "sí", "programació", "Python"]

print("Paraules amb més de 4 caràcters:", filtrar_paraules(llista1, 4))
print("Paraules amb més de 5 caràcters:", filtrar_paraules(llista2, 5))
print("Paraules amb més de 10 caràcters:", filtrar_paraules(llista2, 10))
print("Paraules amb més de 0 caràcters:", filtrar_paraules(["a", "bb", "ccc"], 0))

