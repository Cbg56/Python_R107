def test(split):
    try:
        int(split)
        return True
    except ValueError:
        return False

def notes():
    nb_coeff = 0
    coeff = 0
    note_min = True
    for loop in range(5):
        lst_notes = str(input(f"Veuillez entrer la note du module {loop} et le coefficient correspondant : "))
        split = lst_notes.split()
        if test(split[0]) == False or test(split[1]) == False:
            while test(split[0]) == False or test(split[1]) == False:
                lst_notes = str(input())
                split = lst_notes.split()
        coeff += (int(split[0]) * int(split[1]))
        nb_coeff +=  int(split[1])
        if int(split[0]) < 8:
            note_min = False
    if note_min:
        coeff /= nb_coeff
        if coeff < 10:
            print("Non admis suite à une moyenne trop basse.")
        else:
            print("Admis")
    else:
        print("Non admis suite à une note inferieur à 8")

notes()