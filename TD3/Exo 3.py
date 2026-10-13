import time
def compte_a_rebour_for():
    N = int(input("entrer un nombre entier positif : "))
    if N < 0:
        compte_a_rebour_for()
    else:
        for i in range(N,0,-1):
            print(i)
            time.sleep(0.5)

def compte_a_rebour_while():
    N = int(input("entrer un nombre entier positif : "))
    if N < 0:
        compte_a_rebour_while()
    else:
        idx = 0
        while N != idx:
            print(N-idx)
            time.sleep(0.5)
            idx += 1

#compte_a_rebour_for()
compte_a_rebour_while()