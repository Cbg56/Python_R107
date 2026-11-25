def MON_ARGENT():
    heure = int(input("Combien d'heure avez vous vraiment travaillé : "))
    salaire_de_reference = int(input("Combien vaux le salaire de reference : "))
    if heure <= 160:
        print(heure*salaire_de_reference)
    elif heure <= 161 and heure <= 200:
        print((160*salaire_de_reference) + ((heure - 160)*(1.25*salaire_de_reference)))
    else:
        print((160*salaire_de_reference)+(40*(salaire_de_reference*1.25))+((heure - 200)*(salaire_de_reference*1.5)))

MON_ARGENT()