import random

def llista_20_elements():
    """
    Retorna una llista de 20 elements aleatoris entre 1 i 100.
    """
    return [random.randint(1, 100) for _ in range(20)]

# Generem la llista
llista = llista_20_elements()
print("Llista generada:", llista)

# Funció per comprovar duplicats (sense demanar input)
def hi_ha_duplicats_llista(llista):
    return len(llista) != len(set(llista))

# Comprovem si hi ha duplicats
if hi_ha_duplicats_llista(llista):
    print("Hi ha duplicats a la llista")
else:
    print("No hi ha duplicats a la llista")
