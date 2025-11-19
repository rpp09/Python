def noms_que_comencen_per(llista_noms, lletra):
    """
    Rep una llista de noms, mostra tots els noms,
    i retorna els noms que comencen per la lletra donada.
    També mostra el nombre de noms trobats.
    """
    # Mostrar tota la llista
    print("Llista completa de noms:", llista_noms)
    
    # Filtrar noms que comencen per la lletra indicada
    noms_trobats = [nom for nom in llista_noms if nom.lower().startswith(lletra.lower())]
    
    print(f"Noms que comencen per '{lletra}':", noms_trobats)
    print(f"Total de noms que comencen per '{lletra}': {len(noms_trobats)}")
    
    return noms_trobats


# --- Programa principal ---

# Noms ja triats
noms = ["Anna", "Albert", "Marta", "Adrià", "Pau", "Joan", "Aina"]

# L’usuari escull la lletra inicial
lletra = input("Introdueix la lletra inicial per filtrar els noms: ").strip()

# Aplicar la funció
noms_que_comencen_per(noms, lletra)
