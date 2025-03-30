import random
import string

def create_code(usser, date):
    """esta función procesa el usuario y fecha, genera un string aleatorio de caracteres y retorna el codigo de descuento"""

    characters = string.ascii_uppercase + string.digits
    #genera una cadena de caracteres aleatorios de longitud (30 - long de usuario - long de fecha)
    aux = ''.join(random.choice(characters) for _ in range(30-len(usser)-len(date))) 
    #replace() reemplaza los guiones por un string vacío
    code = f"{usser.upper()}-{date.replace("-","")}-{aux} "
    
    return code