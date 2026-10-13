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

facto_iter()