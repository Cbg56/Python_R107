import re

def grand_remplacement(chaine):
    caracteres_a_remplacer = "àáâçèéêëìíîïñòóôùúûüý"
    caracteres_resultat = "aaaceeeeiiiinooouuuuy"
    for i in range(len(chaine)):
        for j in range(len(caracteres_a_remplacer)):
            if chaine[i] == caracteres_a_remplacer[j]:
                chaine[i] = caracteres_resultat[j]
    return chaine

def suppr(chaine):
    caractere_a_supprimer = "&~#'{([-|`_\^@)°]=+}$¤£*µ%§!:/;.,?<>"
    for i in range(len(chaine)):
        for j in range(len(caractere_a_supprimer)):
            if chaine[i] == caractere_a_supprimer[j]:
                chaine[i].pop()
    return chaine

def palindrome():
    str = input("Entrer le nom du palindrome : ")
    print(str)
    str = re.sub(r'[^a-zA-Z]',"",str).lower()
    print(str)
    deb = 0
    fin = len(str)
    palin = True
    str = grand_remplacement(str)
    str = suppr(str)
    for loop in range(fin):
        while deb < fin:
            if str[deb] != str[fin-1]:
                palin = False
                break
            deb += 1
            fin -= 1
    if palin:
        print("La phrase est un palindrome.")
    else:
        print("La phrase n'est pas un palindrome.")

palindrome()