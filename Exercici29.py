def comptar_majuscules(cadena):
    """
    Rep una cadena, mostra la cadena i retorna el nombre de lletres majúscules que conté.
    """
    print("Cadena original:", cadena)
    
    comptador = 0
    for car in cadena:
        if car.isupper():
            comptador += 1
    return comptador


# --- Proves de la funció ---

print("Nombre de majúscules:", comptar_majuscules("HolaMón"))          
print("Nombre de majúscules:", comptar_majuscules("Python és Genial")) 
print("Nombre de majúscules:", comptar_majuscules("abcde"))            
print("Nombre de majúscules:", comptar_majuscules("123ABCdef"))        
print("Nombre de majúscules:", comptar_majuscules(""))                 

