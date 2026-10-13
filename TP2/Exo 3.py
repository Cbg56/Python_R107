a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

a=int(a)
b=int(b)
c=int(c)

a += b
b = a-b
a = a-b
b += c
c = b-c
b = b-c

a=str(a)
b=str(b)
c=str(c)

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)