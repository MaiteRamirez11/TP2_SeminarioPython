
def process_keyword(keyword, rules):
    """Esta funcion genera una lista de las reglas e imprime las reglas cuya palabra clave se encuentra en ella."""
    lines = rules.splitlines()
    keyword.lower()
    for line in lines:
        rule = line.lower()
        if keyword in rule:
            print(line)