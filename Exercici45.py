def main():
    try:
        n = int(input("Introdueix un número: "))
    except ValueError:
        print("Has d'introduir un número vàlid.")
        return

    suma = sum(int(digit) for digit in str(abs(n)))  # Suma dels dígits

    print(f"La suma dels dígits és: {suma}")

    if suma % 2 == 0:
        print("La suma és parell.")
    else:
        print("La suma és senar.")

if __name__ == "__main__":
    main()
