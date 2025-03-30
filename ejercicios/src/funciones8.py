def anagram(word_1, word_2):
    """esta funcion retorna si las palabras son iguales, utiliza sorted para ordenarlas"""
    return sorted(word_1) == sorted(word_2)

def process_words(word_1, word_2):
    """esta funcion informa si las palabras son anagramas"""
    print("Son anagramas." if anagram(word_1, word_2) else "No son anagramas.")
