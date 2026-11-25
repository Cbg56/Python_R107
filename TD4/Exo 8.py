
def dico_def():
    dico = {}
    dico['firstname'] = str(input('Entrer votre nom : '))
    dico['name'] = str(input('Entrer votre nom : '))
    dico['promo'] = str(input('Entrer votre promo : '))
    dico['group'] = str(input('Entrer votre group : '))
    print(f"votre nom est {dico['name']}, prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")
    return dico

def affichage():
    dico = dico_def()
    print("Les clés du dictionnaire sont :")
    for key in dico:
        print(f"- {key}")
    print("Les valeurs du dictionnaire sont : ")
    for value in dico.values():
        print(f"- {value}")
    print("Les tuplets du dictionnaire sont : ")
    for item in dico.items():
        print(f"- {item}")

#affichage()

def dico_def_bin():
    dico = dico_def()
    dico_toto = {}
    dico_toto['firstname'] = str(input(f'Entrer votre nom  : '))
    dico_toto['name'] = str(input(f'Entrer votre nom, {dico_toto["firstname"]} : '))
    dico_toto['promo'] = str(input('Entrer votre promo : '))
    dico_toto['group'] = str(input('Entrer votre group : '))
    print(f"votre nom est {dico['name']}, prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")
    return dico, dico_toto

def dico_ensemble():
    dico_sec, dico_toto = dico_def_bin()
    dico = {}
    lst_name = [dico_sec['name'] , dico_toto['name']]
    lst_pro = [dico_sec['promo'], dico_toto['promo']]
    lst_group = [dico_sec['group'], dico_toto['group']]
    lst_first = [dico_sec['firstname'], dico_toto['firstname']]
    dico['firstname'] = lst_first
    dico['name'] = lst_name
    dico['promo'] = lst_pro
    dico['group'] = lst_group
    return(dico)

def affichage_ensemble():
    dico = dico_ensemble()
    for key in dico:
        print(f"- {key}")

