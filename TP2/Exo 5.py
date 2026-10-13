def parité ():
    Nb = int(input("Entrer un numero: "))
    if Nb % 2 == 0:
        print("Pair")
    else:
        print("impaire")
    if Nb == 0:
        print("Egal a 0")
    elif Nb < 0:
        print("negatif")
    else:
        print("positif")

parité()