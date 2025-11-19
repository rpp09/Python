def menu_principal():
      opcio=0
      while opcio<1 or opcio>4:
            opcio = int(input(""" Eligeix una opció:
                              1. Calculadora decimal
                              2. Calculadora real (floats)
                              3. Sortir
                              4. Conversió de bases \n"""))
            if 1 <= opcio <= 4:
                  return opcio
            else:
                  print("L'opció seleccionada no és correcta, torna-ho a provar! \n")


def menu_calculadora():
    opcio=0
    while opcio<0 or opcio>4:
         opcio=int(input("""Escriu una opció:
                    1. Suma
                    2. Resta
                    3. Multiplicació
                    4. Divisió
                    0. Sortir
                    """))
         if 0 <= opcio <= 4:
               return opcio
         else:
               print("L'opció seleccionada no és correcta, torna-ho a provar!! \n")


def calculadora_decimal(opcio):
        if 1 <= opcio <= 4:
              a = int(input("Introdueix el primer nombre: "))
              b = int(input("Introdueix el segon nombre: "))

        match(opcio):
              case 1:
                    print("Estic fent la suma! \n")
                    c= a + b
                    print(f"El resultat de la operació {a} + {b} és {c}")
              case 2:
                    print("Estic fent la resta! \n")
                    c= a - b
                    print(f"El resultat de la operació {a} - {b} és {c}")
              case 3:
                    print("Estic fent la multiplicació \n")
                    c= a * b
                    print(f"El resultat de la operació {a} * {b} és {c}")
              case 4:
                    print("Estic fent la divisió! \n")
                    c= a // b
                    print(f"El resultat de la operació {a} // {b} és {c}")
              case _:
                    print("Gràcies, fins aviat!")


def calculadora_real(opcio):
        if 1 <= opcio <= 4:
              a = float(input("Introdueix el primer nombre: "))
              b = float(input("Introdueix el segon nombre: "))

        match(opcio):
              case 1:
                    print("Estic fent la suma! \n")
                    c= a + b
                    print(f"El resultat de la operació {a} + {b} és {c}")
              case 2:
                    print("Estic fent la resta! \n")
                    c= a - b
                    print(f"El resultat de la operació {a} - {b} és {c}")
              case 3:
                    print("Estic fent la multiplicació \n")
                    c= a * b
                    print(f"El resultat de la operació {a} * {b} és {c}")
              case 4:
                    print("Estic fent la divisió! \n")
                    c= a / b
                    print(f"El resultat de la operació {a} / {b} és {c}")
              case _:
                    print("Gràcies, fins aviat!")


# -----------------------------
# NOVA FUNCIONALITAT: CANVIS DE BASE
# -----------------------------

def menu_bases():
    print("""
   Conversió de bases:
   1. Decimal a Binari
   2. Decimal a Octal
   3. Decimal a Hexadecimal
   4. Binari a Decimal
   5. Octal a Decimal
   6. Hexadecimal a Decimal
   0. Sortir
    """)
    opcio = int(input("Escull una opció: "))
    return opcio


def conversions_bases():
    opcio = menu_bases()

    match(opcio):
        case 1:
            n = int(input("Introdueix un nombre decimal: "))
            print("Resultat:", bin(n)[2:])
        case 2:
            n = int(input("Introdueix un nombre decimal: "))
            print("Resultat:", oct(n)[2:])
        case 3:
            n = int(input("Introdueix un nombre decimal: "))
            print("Resultat:", hex(n)[2:].upper())
        case 4:
            s = input("Introdueix un nombre binari: ")
            print("Resultat:", int(s, 2))
        case 5:
            s = input("Introdueix un nombre octal: ")
            print("Resultat:", int(s, 8))
        case 6:
            s = input("Introdueix un nombre hexadecimal: ")
            print("Resultat:", int(s, 16))
        case _:
            print("Sortint del menú de conversions...")


# Programa principal

op=1
while op!=0:
        op = menu_principal()
        if op==1:
              print("Estic passant per la calculadora decimal! \n")
              calculadora_decimal(menu_calculadora())
        elif op==2:
              print("Estic passant per la calculadora real! \n")
              calculadora_real(menu_calculadora())
        elif op==4:
              print("Estic passant per les conversions de bases! \n")
              conversions_bases()
        else:
            print("Gràcies per utilitzar la meva calculadora, fins un altre dia!")
            op=0
