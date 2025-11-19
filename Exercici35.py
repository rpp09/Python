def comptar_vocals(paraula):
    """
    Rep una paraula i retorna un diccionari amb el nombre de vegades
    que apareix cada vocal (a, e, i, o, u).
    """
    vocals = 'aeiou'
    comptador = {v: 0 for v in vocals}  # Inicialitzar totes a 0
    
    for car in paraula.lower():  # Convertir a minúscula per no diferenciar majúscules
        if car in vocals:
            comptador[car] += 1
    
    return comptador


# --- Proves de la funció ---

paraula1 = "HolaMón"
paraula2 = "Programació"
paraula3 = "Python"
paraula4 = "Educació"

print(f"Paraula: {paraula1} -> Vocals:", comptar_vocals(paraula1))
print(f"Paraula: {paraula2} -> Vocals:", comptar_vocals(paraula2))
print(f"Paraula: {paraula3} -> Vocals:", comptar_vocals(paraula3))
print(f"Paraula: {paraula4} -> Vocals:", comptar_vocals(paraula4))
