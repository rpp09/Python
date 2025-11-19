def noms_que_comencen_per(llista_noms, lletra='a'):
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


# --- Proves de la funció ---

llista1 = ["Anna", "Albert", "Marta", "Adrià", "Pau"]
llista2 = ["Joan", "Marc", "Aina", "aureli", "Nil"]
llista3 = ["Bea", "Clara", "David"]

noms_que_comencen_per(llista1)
noms_que_comencen_per(llista2)
noms_que_comencen_per(llista3)

