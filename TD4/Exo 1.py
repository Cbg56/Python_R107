def table_de_multi():
    nb = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
    lst = []
    for i in range(10):
        print(f"{i} * {nb} = {round(i*nb,2)}")
        lst.append(i*nb)
    return lst
table_de_multi()