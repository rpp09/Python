def rimen(p1, p2):
    # Ens assegurem que totes dues paraules tinguin mínim 2 o 3 lletres
    if len(p1) < 2 or len(p2) < 2:
        return "Les paraules són massa curtes per comparar."

    # Comprovar si coincideixen les 3 darreres lletres (rima completa)
    if len(p1) >= 3 and len(p2) >= 3 and p1[-3:] == p2[-3:]:
        return "Rimen!"

    # Comprovar si coincideixen només les 2 darreres (rima parcial)
    if p1[-2:] == p2[-2:]:
        return "Rimen un poc."

    # Si no coincideixen
    return "No rimen."


def main():
    paraula1 = input("Introdueix la primera paraula: ").strip().lower()
    paraula2 = input("Introdueix la segona paraula: ").strip().lower()

    resultat = rimen(paraula1, paraula2)
    print(resultat)


if __name__ == "__main__":
    main()
