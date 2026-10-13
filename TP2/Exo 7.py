from random import randint as rt

def lancer_de_dés ():
    Nb = rt(1,3)
    if Nb == 3:
        print("face")
    else:
        print("pile")

lancer_de_dés()
