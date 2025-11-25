def main():
    try:
        n = int(input("Introdueix un número entre 1 i 900000: "))
    except ValueError:
        print("Has d'introduir un número vàlid.")
        return

    if n < 1 or n > 900000:
        print("El número ha d'estar entre 1 i 900000.")
        return

    digits = len(str(n))
    print(f"El número {n} té {digits} dígits.")

if __name__ == "__main__":
    main()
