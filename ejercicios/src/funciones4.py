def five_characters(user_name):
    """esta funcion retorna si el nombre de usuario tiene al menos 5 caracteres."""
    return not len(user_name) < 5


def contains_number(user_name):
    """esta funcion retorna si el nombre de usuario contiene al menos un numero."""
    return any(char.isdigit() for char in user_name)


def contains_uppercase(user_name):
    "esta funcion retorna si el nombre de usuario contiene al menos una letra mayuscula."
    return any(char.isupper() for char in user_name)

    
def process_username(user_name):
    if not(five_characters(user_name) and contains_number(user_name) and contains_uppercase(user_name) and user_name.isalnum()):
        print('El nombre de usuario no cumple con los requisitos.')
    else: print('usuario valido')