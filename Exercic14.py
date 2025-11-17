opcio=float(input("""Elegeix una opció:
                  1. Suma
                  2. resta
                  3 multiplicació
                  4. divisió
                  0. sortir
                  """))
A= float(input("Insereix el primer nombre"))
B= float(input("Insereix el segon nombre"))
C= A + B
D= A * B
E= A / B
F= A - B
G= A % B
H= A // B
I= A ** B
print("La suma de {} + {} és igual a {}".format(A, B, C))
print("La multiplicació de {} * {} és igual a {}".format(A, B, D))
print("La divisió de {} i {} és igual a {}".format(A, B, E))
print("La resta de {} i {} és igual a {}".format(A, B, F))
print("El reste de {} i {} és {}".format(A, B, G))
print("El coecient de {} i {} és {}".format(A, B, H))
print("La potencia de {} ** {} és {}".format(A, B, I))
