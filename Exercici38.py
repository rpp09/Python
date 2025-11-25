import random

def generar_codi():
    # Genera un codi de 4 xifres entre 0 i 9
    return [random.randint(0, 9) for _ in range(4)]

def avaluar_intent(codi, intent):
    # Comptar encerts (xifra i posició correcta)
    encerts = sum(codi[i] == intent[i] for i in range(4))
    
    # Comptar coincidències (xifra correcta però posició incorrecta)
    # Cal comptar coincidències sense sumar els encerts
    codi_rest = []
    intent_rest = []
    
    for i in range(4):
        if codi[i] != intent[i]:
            codi_rest.append(codi[i])
            intent_rest.append(intent[i])

    coincidencies = 0
    for x in intent_rest:
        if x in codi_rest:
            coincidencies += 1
            codi_rest.remove(x)

    return encerts, coincidencies

def main():
    codi = generar_codi()
    # Per provar, pots mostrar-lo:
    # print("Codi secret:", codi)

    print("Benvingut al MasterMind! Endevina el codi de 4 xifres (0-9).")

    while True:
        entrada = input("Introdueix un codi de 4 xifres: ")

        if len(entrada) != 4 or not entrada.isdigit():
            print("Si us plau, introdueix exactament 4 xifres.")
            continue

        intent = [int(x) for x in entrada]
        encerts, coincidencies = avaluar_intent(codi, intent)

        print(f"Encerts (posició correcta): {encerts}")
        print(f"Coincidències (xifra correcta però posició incorrecta): {coincidencies}")

        if encerts == 4:
            print("Has encertat el codi! Felicitats!")
            break

if __name__ == "__main__":
    main()
