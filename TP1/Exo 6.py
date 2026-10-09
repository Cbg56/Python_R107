def tp1exo6():
    minutes = int(input("Entrer les minutes : "))
    jour = None
    heure = None
    while minutes >= 1440:
        minutes -= 1440
        jour += 1
    while minutes >= 60:
        minutes -= 60
        heure += 1
    return (f'on est le {jour} et il est actuellement {heure} : {minutes}')