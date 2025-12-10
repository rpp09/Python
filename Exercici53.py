def index_paraula(llista, paraula):
    esquerra = 0
    dreta = len(llista) - 1
    
    while esquerra <= dreta:
        mig = (esquerra + dreta) // 2
        if llista[mig] == paraula:
            return mig
        elif llista[mig] < paraula:
            esquerra = mig + 1
        else:
            dreta = mig - 1
            
    return -1

# Exemple d'ús
paraules = ["aigua", "arbre", "casa", "cotxe", "llibre"]
print(index_paraula(paraules, "casa"))  # Output: 2
print(index_paraula(paraules, "gat"))   # Output: -1
    