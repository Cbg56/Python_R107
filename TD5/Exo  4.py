def porte_monai():
    monai = [100,50,10,2,1,]
    total = [0 for i in range(len(monai))]
    argent = int(input("Entrer une somme d'argent positive : "))
    if argent < 0:
        while (argent < 0):
            argent = int(input("Entrer VRAIMENT une somme d'argent positive : "))
    aff_argt = argent
    for i in range(len(monai)):
        while monai[i] <= argent:
            argent -= monai[i]
            total[i] += 1
    print(f"{aff_argt} euros, c'est donc {total[0]} billets de 100, {total[1]} de 50, {total[2]} billets de 10, {total[3]} pièces de 2 et {total[4]} pieces de 1")

porte_monai()