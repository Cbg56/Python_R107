from random import randint as rt

def lancer_de_dés ():
    Nb = rt(0,100)
    if Nb <50:
        print("pile")
    else:
        print("face")

lancer_de_dés()
