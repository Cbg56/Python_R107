def test_bisect(annee):

    if ((annee % 4) == 0 and (annee % 100) !=0) or ((annee % 400) == 0):
        return True
    else:
        return False

def verif_date ():
    date = str(input("Entrer la date :"))
    bis = [31,29,31,30,31,30,31,31,30,31,30,31]
    if len(date) != 8:
        print("La date est erroné")
        verif_date()
    j, m, a = date[0]+date[1], date[2]+date[3], date[4]+date[5]+date[6]+date[7]
    j,m,a = int(j), int(m), int(a)
    bisectile = test_bisect(j)
    if not(m <= 12 and m >=1) or not(j>=1 and j <=31):
        print("La date n'est pas valide")
        verif_date()
    if m == 2:
        if not bisectile and j == 29:
            print("La date n'est pas valide")
            verif_date()
    if j > bis[m-1]:
        print("La date n'est pas valide")
        verif_date()
    print("correct")
verif_date()

