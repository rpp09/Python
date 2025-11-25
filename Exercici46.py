def main():
    try:
        n = int(input("Introdueix un número: "))
    except ValueError:
        print("Has d'introduir un número vàlid.")
        return

    digits_parells = [d for d in str(abs(n)) if int(d) % 2 == 0]

    if digits_parells:
        print("Dígits parells:", " ".join(digits_parells))
    else:
        print("No hi ha dígits parells.")

if __name__ == "__main__":
    main()
