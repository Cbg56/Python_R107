def NbMinutes():
    jour = int(input("Entrer les jours : "))
    heure = int(input("Entrer les heures : "))
    minute = int(input("Entrer les minutes : "))
    TtlMinutes = None
    if jour < 1 or heure < 0 or heure > 23 or minute < 0 or minute > 59:
        NbMinutes()
    else:
        TtlMinutes = (jour - 1) * 24 * 60 + heure * 60 + minute
    return TtlMinutes

NbMinutes()
