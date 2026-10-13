def facto_add ():
    result = 0
    N = int(input("Entrer un nombre : "))
    if N == 0:
        print("0")
    else:
        if N < 0:
            while N != 0:
                result += N
                N += 1
        else:
            while N != 0:
                result += N
                N -= 1
        print(result)

def boucle_attente():
    N = int(input("Entrer le nombre 100 pour arreter : "))
    if N != 100:
        print("Et c'est repartie pour un tour !!!! C'est partie, c'est partie, c'est partie !!!!!!!")
        boucle_attente()
    else:
        print("Sortie")

def verif_inter():
    lst = []
    for loop in range(10):
        lst.append(0)
    interu = 0
    interd = 0
    intert = 0
    for loop in range(10):
        Nb = int(input("Entrer un nombre : "))
        if Nb >= 0 and Nb <= 20:
            lst[loop] = Nb
            print("ici")
        else:
            while (Nb < 0 or Nb > 20):
                Nb = int(input("Erreur. Entrer un nombre : "))
            lst.append(Nb)
    for loop in range(10):
        if lst[loop] < 10:
            interu += 1
        elif lst[loop] >= 10 and lst[loop] < 15:
            interd += 1
        else:
            intert += 1
    print(f"Il y a {interu} nombres dans le 1er interval et {interd} nombres dans le 2nd interval et {intert} nombres dans le 3rd interval")

def pgnb ():
    N = int(input("Entrer un nombre : "))
    if N < 0:
        pgnb()
    elif N == 0:
        print("0")
    else:
        indx = 0
        Nb = 0
        while Nb < N:
            indx += 1
            Nb += indx
        if Nb > N:
            indx -= 1
        print(indx)

# facto_add()
# boucle_attente()
# verif_inter()
#pgnb()
