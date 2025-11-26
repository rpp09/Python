def invertir(cadena):
    """
    Retorna la inversa de la cadena donada.
    """
    return cadena[::-1]  # Tall amb pas -1 per invertir

# Exemple de prova
text = "Soc del Ramis"
text_invertit = invertir(text)
print("Original:", text)
print("Invertit:", text_invertit)

