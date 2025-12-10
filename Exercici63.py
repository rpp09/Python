def paraules_amb_lletra(llista, lletra):
    """
    Retorna una llista amb les paraules que comencen per la lletra donada.
    """
    return list(filter(lambda paraula: paraula.startswith(lletra), llista))

# Exemple amb altres noms
noms = ["Anna", "Pedro", "Paula", "Joan", "Pere", "Laura"]
resultat = paraules_amb_lletra(noms, "P")
print(resultat)
