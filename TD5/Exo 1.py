def nom_prenom():
    lst = str(input("Entrer votre nom puis votre prenom : "))
    prenom, nom = lst.split()
    print(f"{prenom.capitalize()} {nom.upper()}")


nom_prenom()