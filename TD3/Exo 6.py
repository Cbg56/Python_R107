def velo ():
    debut = int (input ("Donnez l’heure de début de la location (un entier) :"))
    fin = int (input ("Donnez l’heure de fin de la location (un entier) :"))
    if debut < 0 or debut > 23 or fin < 0 or fin > 23:
        velo()
    else:
        if fin < 7 or debut > 16:
            print(f"Vous avez loué votre vélo pendant \n {fin-debut} heure(s) au tarif horaire de 1.0 euro (s) \n Le montant total à payer est de {fin-debut} euro (s).")
        else:
            prix = 0
            coutant = 0
            peu_coutant = 0
            while debut != fin:
                if debut == 7 or debut ==8 or debut ==9 or debut ==0 or debut ==11 or debut ==12 or debut ==13 or debut ==14 or debut ==15 or debut ==16 or debut ==17:
                    prix += 2
                    coutant += 1
                else:
                    prix += 1
                    peu_coutant +=1
                debut += 1
            print(f"Vous avez loué votre vélo pendant \n {peu_coutant} heure(s) au tarif horaire de 1.0 euro(s) \n {coutant} heure(s) au tarif horaire de 2.0 euro(s) \n Le montant total à payer est de {prix} euro(s).")


def velo_V2 ():
    debut = int (input ("Quel heure ?"))
    fin = int (input ("Quel fin ?"))
    if debut < 0 or debut > 23 or fin < 0 or fin > 23:
        velo()
    else:
        if fin < 7 or debut > 16:
            print(fin-debut)
        else:
            heure_coutant = [i for i in range (7,18)]
            coutant = 0
            peu_coutant = 0
            test = False
            for a in range(debut, fin+1):
                test = False
                for b in range(len(heure_coutant)):
                    if debut == heure_coutant[b]:
                        coutant += 1
                        test = True
                        if test:
                            break
                if not test:
                    peu_coutant += 1
                debut += 1
            prix = peu_coutant * 1 + coutant * 2
            print(f"Le prix est de {prix} euro \n avec {peu_coutant} d'heure de location a 1 euro \n et {coutant} d'heure de location a 2 euro")

velo()
#velo_V2()