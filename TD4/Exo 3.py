def scalaire():
    nMax = 3
    ttl = 0
    lstu = []
    lstd = []
    nombre = int(input("Entrer la taille des vecteurs : "))
    while nombre > nMax or nombre <= 0:
        nombre = int(input("Entrer un nombre de vecteurs correct: "))
    print("Saisie du 1er vecteur:")
    for loop in range(nombre):
        saisie = int(input(f"V1{loop} : "))
        lstu.append(saisie)
    print("Saisie du 2nd vecteur:")
    for loop in range(nombre):
        saisie = int(input(f"V2[{loop}]"))
        lstd.append(saisie)
    for loop in range(nombre):
        ttl += lstd[loop] * lstu[loop]
    print(f"Le produit scalaire est de :{ttl}")

scalaire()
