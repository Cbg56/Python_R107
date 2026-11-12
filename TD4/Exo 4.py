def compte_ocu():
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    dico = {}
    for i in range(len(L1)):
        if not L1[i] in dico:
            dico.append({L1[i]: 1})
        else:
            for key in dico:
                if L1[i] == dico[key]:
                    dico[i].value += 1
    max_item = 0
    max_value = 0
    for key in dico:
        if dico[key] > max:
            max_item = dico[key]
            max_value = key
    print(f"Il y a {max_value} fois {max_item}")

#compte_ocu()

def compte_ocu2():
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    lst = []
    for i in range(len(L1)):
        if not L1[i] in lst:
            lst.append(L1[i])
