# Demanar els dos números a l'usuari
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Assegurar que comencem pel menor
inici = min(num1, num2)
final = max(num1, num2)

# Calcular la suma
suma = 0
for i in range(inici, final + 1):
    suma += i

# Mostrar resultat
print(f"La suma dels números entre {num1} i {num2} és: {suma}")
