def dico_def():
    dico = {'firstname','name','promo','group'}
    dico['firstname'] = str(input('Entrer votre nom : '))
    dico['name'] = str(input('Entrer votre nom : '))
    dico['promo'] = str(input('Entrer votre promo : '))
    dico['group'] = str(input('Entrer votre group : '))
    print(f"votre nom est {dico['name']}, prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")
dico_def()