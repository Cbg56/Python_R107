def compte_ocu():
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    lst = []
    nb = []
    for i in range(len(L1)):
        nombre = L1[i]
        if not nombre in lst:
            lst.append(nombre)
            nb.append(1)
        else:
            for j in range(len(lst)):
                if nombre == lst[j]:
                    nb[j] += 1
    max_lst = 0
    max_nb = 0
    for loop in range(len(nb)):
        if nb[loop] > max_nb:
            max_lst = lst[loop]
            max_nb = nb[loop]
    print(f"Il y a {max_nb} fois {max_lst}")

compte_ocu()