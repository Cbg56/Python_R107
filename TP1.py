from random import randint

def NbMinutes ():
    jour = int(input("Entrer les jours : "))
    heure = int(input("Entrer les heures : "))
    minute = int(input("Entrer les minutes : "))
    TtlMinutes = None
    if jour < 1 or heure < 0 or heure > 23 or minute < 0 or minute > 59:
        NbMinutes()
    else:
        TtlMinutes = (jour - 1) * 24 * 60 + heure * 60 + minute
    return TtlMinutes

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

def tp1exo8():
    return randint(0,100)

print(tp1exo8())