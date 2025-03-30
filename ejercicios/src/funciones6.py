def process_descriptions (descriptions):
    """esta función retorna un diccionario con cada palabra junto a la cantidad de veces que aparecen"""
    dict = {"música": 0, "charla":0, "entretenimiento": 0}
    
    for description in descriptions:
        for word in dict:
            dict[word] += description.lower().split().count(word)
    
    return dict
        