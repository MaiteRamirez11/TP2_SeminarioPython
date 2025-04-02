def calcular(kills, assists, deaths):
    """Esta funcion retorna los puntos totales del jugador segun la cantidad de kills, asistencias y muertes."""
    return kills * 3 + assists - (1 if deaths else 0)


def contabilizar_puntos(puntajes):
    """esta funcion almacena los kills, assists, deaths y puntos totales de un jugador"""
    puntos = {'kills': puntajes['kills'],
                'assists': puntajes['assists'],
                'deaths': 1 if puntajes['deaths'] else 0,
                'puntos totales': calcular(puntajes['kills'], puntajes['assists'], puntajes['deaths'])}
    return puntos


def actualizar_ranking(ranking, jugador, puntos, mvp):
    """Esta función actualiza el ranking de la ronda"""
    for j in ranking:
        if j['nombre'] == jugador:
            j['kills'] += puntos['kills'] 
            j['assists'] += puntos['assists'] 
            j['deaths'] += puntos['deaths']
            j['puntos totales'] += puntos['puntos totales']
            if jugador == mvp: 
                j['MVPs'] += 1
            break


def imprimir_ranking(ranking):
    """Esta función imprime el ranking actualizado y ordenado de las estadisticas de cada jugador"""
    print('Jugador    Kills    Asistencias    Muertes    MVPs    Puntos')
    for j in ranking:
        print('-' * 68)
        print(f'{j['nombre']}        {j['kills']}        {j['assists']}           {j['deaths']}           {j['MVPs']}           {j['puntos totales']}')
        print('-' * 68)


def procesar_rondas(rounds):
    """Esta funcion pasa por cada ronda, contabiliza los puntajes a cada jugador, determina el MVP y genera un ranking. 
        En el final de cada ronda lo imprime en orden decreciente en base a los puntajes totales."""
    ranking = [
        {'nombre': 'Shadow','kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0,'puntos totales': 0},
        {'nombre': 'Blaze','kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0,'puntos totales': 0},
        {'nombre': 'Viper','kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0,'puntos totales': 0},
        {'nombre': 'Frost', 'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0,'puntos totales': 0},
        {'nombre': 'Reaper', 'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0,'puntos totales': 0}]

    #enumerate() recorre las rondas y cuenta el numero/posicion de cada una
    for i, ronda in enumerate(rounds, start = 1):
        
        #diccionario que guarda cada jugador y un diccionario con sus puntajes de la ronda
        puntos_jugadores = {} 
        
        #items() retorna una lista de pares claves-valor de las rondas, sirve para recorrer el diccionario de manera eficiente
        #se lee cada jugador y se almacenan sus puntos de la ronda en el diccionario:
        for jugador, puntajes in ronda.items():
            puntos = contabilizar_puntos(puntajes)
            puntos_jugadores[jugador] = puntos
        
        #se determina el mvp y sus puntos de la ronda actual
        #la funcion lambda devuelve el valor de los puntos totales de cada jugador y max() hace la comparacion para encontrar el mvp
        mvp = max(puntos_jugadores, key=lambda jugador: puntos_jugadores[jugador]['puntos totales'])
        mvp_puntos = puntos_jugadores[mvp]['puntos totales']
        
        #se actualiza el ranking de puntos de cada jugador
        for jugador, puntos in puntos_jugadores.items():  
            actualizar_ranking(ranking, jugador, puntos, mvp)
        
        #Ordenar lista de mayor a menor en base a los puntos totales de los jugadores
        #la funcion lambda toma un jugador de la lista y retorna el valor de sus puntos totales
        ranking.sort(key=lambda x: x['puntos totales'], reverse=True)
        
        #imprimir MVP de la ronda actual 
        print(f'<<<MVP de la ronda {i}: {mvp} con {mvp_puntos} puntos>>>') 
        
        #imprimir ranking de la ronda actual
        print(f'Ranking actualizado en la ronda {i}:')
        imprimir_ranking(ranking)
        print()
        print('*' * 68)
        print()
        
