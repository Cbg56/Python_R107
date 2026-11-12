def moyenne():
    nbetud = int(input("Entrer le nombre d'etudiant : "))
    moyenne = 0.0
    notes = []
    for i in range (nbetud):
        nt = float(input(f"Entrer la note de l'eleve n°{i}: "))
        notes.append(nt)
        moyenne += notes[i]
    moyenne = moyenne / nbetud
    print(f"La moyenne de classe est de : {moyenne}")
    print("Numero de l'etudiant | note | ecart a la moyenne")
    for loop in range(nbetud):
        print(f"{loop} | {notes[loop]} | {notes[loop]-moyenne}")

moyenne()