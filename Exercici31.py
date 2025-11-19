# Programa per calcular l'edat de 4 persones i mostrar-ho tabulat

# Demanar l'any actual
any_actual = int(input("Introdueix l'any actual: "))

# Llistes per guardar noms i anys de naixement
noms = []
anys_naixement = []

# Demanar dades de 4 persones
for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    any_naix = int(input(f"Introdueix l'any de naixement de {nom}: "))
    noms.append(nom)
    anys_naixement.append(any_naix)

# Calcular edats
edats = []
for any_naix in anys_naixement:
    edats.append(any_actual - any_naix)

# Mostrar dades tabulades
print("\nDades de les persones:")
print("{:<15} {:<15} {:<10}".format("Nom", "Any de Naixement", "Edat"))
print("-"*40)
for i in range(4):
    print("{:<15} {:<15} {:<10}".format(noms[i], anys_naixement[i], edats[i]))
