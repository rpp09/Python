def main():
    n = int(input("Introdueix un número menor de 100: "))

    if n >= 100:
        print("El número ha de ser menor de 100.")
        return

    suma = 0
    print("Càlcul:", end=" ")

    primer = True
    for x in range(n - 4, -1, -4):
        if not primer:
            print(" + ", end="")
        print(f"{x}**2", end="")
        suma += x * x
        primer = False

    print(f"\nResultat: {suma}")

if __name__ == "__main__":
    main()
