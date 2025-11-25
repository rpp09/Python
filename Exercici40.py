def main():
    print("Calculadora de capital final amb interès compost")

    # Demanar capital inicial
    while True:
        try:
            capital = float(input("Introdueix el capital inicial (50.000€ - 800.000€): "))
            if 50000 <= capital <= 800000:
                break
            else:
                print("Valor incorrecte. Ha d'estar entre 50.000€ i 800.000€.")
        except ValueError:
            print("Introdueix un número vàlid.")

    # Demanar interès
    while True:
        try:
            interes = float(input("Introdueix l'interès (0.5% - 13%): "))
            if 0.5 <= interes <= 13:
                break
            else:
                print("Valor incorrecte. Ha d'estar entre 0.5% i 13%.")
        except ValueError:
            print("Introdueix un número vàlid.")

    # Demanar anys
    while True:
        try:
            anys = int(input("Introdueix el nombre d'anys (3 - 40): "))
            if 3 <= anys <= 40:
                break
            else:
                print("Valor incorrecte. Ha d'estar entre 3 i 40 anys.")
        except ValueError:
            print("Introdueix un número vàlid.")

    # Càlcul
    capital_final = capital * (1 + interes / 100) ** anys

    print(f"\nCapital final després de {anys} anys: {capital_final:.2f}€")


if __name__ == "__main__":
    main()
