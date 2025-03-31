import unicodedata
import locale
locale.setlocale(locale.LC_COLLATE, 'spanish')

def eliminar_acentos(name):
    return ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')

def clear_names(clients):
    """esta funcion ejecuta operaciones de limpieza de nombres y retorna una nueva lista"""
    #declaro un conjunto para agregar los nombres y que no haya repetidos
    clean_names = set()
    
    for name in clients:
        if name: #elimino espacios y convierto a formato titulo
            name = " ".join(word.title() for word in name.split())
            name = eliminar_acentos(name)
            if name:#si el nombre existe lo agrego al conjunto
                clean_names.add(name)
    
    sorted(clean_names) #convierto el conjunto en una lista
    
    return clean_names