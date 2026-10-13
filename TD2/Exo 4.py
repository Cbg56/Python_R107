def fondue():
    BASE = 4
    fromage = 800.0
    eau = 2
    ail = 2
    pain = 400
    NbConvives = int(input("Entrez lz nombre de personne : "))
    fromage = fromage * NbConvives/ BASE
    eau = eau * NbConvives/ BASE
    ail = ail * NbConvives/ BASE
    pain = pain * NbConvives/ BASE
    print(f"Pour {NbConvives} personne il faut: \n - {fromage} de fromage \n - {eau} de eau \n - {ail} de ail \n - {pain} de pain")

fondue()