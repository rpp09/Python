def main():
    try:
        n = int(input("Introdueix un número entre 1 i 20: "))
    except ValueError:
        print("Has d'introduir un número vàlid.")
        return

    if n < 1 or n > 20:
        print("El número ha d'estar entre 1 i 20.")
        return

    print(f"Taula de multiplicar del {n}:")
    for i in range(1, 11):  # Multiplicarem del 1 al 10
        resultat = n * i
        print(f"{n} x {i} = {resultat}")

if __name__ == "__main__":
    main()
