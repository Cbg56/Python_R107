def tri_fct():
    lst = [5, 2, 4, 8, 1, 3]
    print(sorted(lst))

#tri_fct()

def tri_insertion():
    lst = [5, 2, 4, 8, 1, 3]
    for i in range(1, len(lst)):
        elem = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > elem:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = elem
        print(lst)
#tri_insertion()
