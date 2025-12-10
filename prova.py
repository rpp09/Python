def sumaun(l):
    for i,e in enumerate(l):
        l[i]=e +1

#Programa principal
l=[5, 6, 7, 10]
print(l)
sumaun(l)
print(l)     
sumaun(l)
print(l)  
sumaun(l)
print(l)  

  
"""
 #Prec: donat dos numeros
    #Post: retorna el menor i despres major
    if x>y:
        return y, x
    elif y>x:
        return x, y
    else:
        return x, y
    
#Prgrama principal    
a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
b, a= ordenar(a, b)
for e in range(b, a+1):
    if e%2==1:
       print(e)
"""





















"""
r= (a*b) // 2
for i in range(r, -1, -1):
    print(i)
"""

















"""
a = int(input("Introdueix el primer número: "))
b = int(input("Introdueix el segon número: "))
r = a * b
print("Resultat:", r)
if (r>=25 and r<=35) or (r>=105 and r<=125):
    print("A")
elif (r>=45 and r<=65) or (r>=145 and r<=165):
    print("B")
else:
    print("C")
"""