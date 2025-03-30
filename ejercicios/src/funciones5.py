
def process_time(time):
    if time < 200:
        return 'Rápido'
    elif time >= 200 and time <= 500:
        return 'Normal'
    else: return 'Lento'