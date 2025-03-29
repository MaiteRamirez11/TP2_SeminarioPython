
def starts_with_vowels(palabra):
    """Esta funcion verifica si la palabra comienza con vocal"""
    vocales = "aeiouAeiou"
    return len(palabra) > 0 and palabra[0] in vocales

def process_text(text):
    """Convierte el texto en una lista de lineas e imprimime las cuya 
    segunda palabra comience con vocal"""
    lineas = text.splitlines()
    for linea in lineas:
        palabras = linea.split()
        if len(palabras) > 1 and starts_with_vowels(palabras[1]):
            print(linea)    