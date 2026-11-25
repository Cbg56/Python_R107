def grand_remplacement():
    caracteres_a_remplacer = "ÀÁÂÇÈÉÊËÌÍÎÏÑÒÓÔÙÚÛÜÝŸàáâçèéêëìíîïñòóôùúûüý"
    caracteres_resultat = "aaaceeeeiiiinooouuuuyyaaaceeeeiiiinooouuuuy"

def palindrome():
    str = input("Entrer le nom du palindrome : ")
    deb = 0
    fin = len(str)
    palin = True
    for loop in range(fin):
        while deb > fin:
            if str[deb] != str[fin-1]:
                palin = False
                break
            deb += 1
            fin -= 1

