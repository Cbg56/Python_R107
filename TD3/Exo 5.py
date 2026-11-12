def facto_choice():
    N = int(input("Entrer 1 pour for et 2 pour while "))
    if N == 2:
        facto_while()
    if N == 1:
        facto_iter()

def facto_iter():
    N = int(input("Entrer nombre : "))
    if N == 0:
        print("0")
    elif N < 0:
        facto_iter()
    else:
        facto = 1
        for i in range(2,(N+2)):
            print(facto, end=" ")
            facto *= i

def facto_while():
    N = int(input("Entrer nombre : "))
    if N == 0:
        print("0")
    elif N < 0:
        facto_while()
    else:
        res = 1
        comp = 2
        while comp != (N+2):
            print(res, end=" ")
            res *= comp
            comp+=1



facto_choice()