def llegir_frases(n):
# Prec: donat un numero
# Post: Retorna una llista de n-element llegits del teclat    
    llista=list()
    for i in range(n):
        llista.append(input(""))
    return llista    

def escriure_frases(llista):
# Prec: donada una llista d'element
# Post: imprimeix cada element de la llista
    for e in llista:
        print(e)

def convertir_majuscules(s):
    vocal="aeiouAEIOU"
    llista=list(s)
    for i,e in enumerate(llista):
        if e not in vocal:
            llista[i]=e.upper()
    return"".join(llista)

#Programa Principal
n = int(input("escriu una frase:  "))
print(n)
llista= llegir_frases(n)
for e in enumerate(llista):
    llista[i]=convertir_majuscules(e)
escriure_frases(llista)    







"""
numero = 3
while numero!=0:
    numero= int(input("introdueix un nombre: "))
    if numero!=0:
        print("El nombre que ve després és {}".format(numero+1))
"""
    