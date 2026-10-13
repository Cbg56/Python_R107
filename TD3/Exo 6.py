def velo ():
    debut = int (input ("Quel heure ?"))
    fin = int (input ("Quel fin ?"))
    if debut < 0 or debut > 23 or fin < 0 or fin > 23:
        velo()
    else:
        if fin < 7 or debut > 16:
            print(fin-debut)
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
            print(f"Le prix est de {prix} euro \n avec {peu_coutant} d'heure de location a 1 euro \n et {coutant} d'heure de location a 2 euro")

velo()