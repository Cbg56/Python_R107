from random import randint as rt

def alea ():
    rdm = rt(0,100)
    rep = -1
    essai = 0
    while rep != rdm:
        rep = int(input("Entrer un nombre : "))
        essai += 1
        if rep == rdm:
            print(f"Bien jouer, tu l'a trouver en {essai} essai")
        elif rep < rdm:
            print("Le nombre est plus grand")
        else:
            print("Le nombre est plus petit")

alea()