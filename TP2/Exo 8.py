def intervalle ():
    NbReel = int(input("Entrer un nombre réel : "))
    if (NbReel < 3 and NbReel > 2) or NbReel == 2 or (NbReel > 0 and NbReel < 1) or NbReel==1 or (NbReel < -2 and NbReel > -10) or NbReel == -2 or NbReel == -10:
        print("appartien a I")
    else:
        print("appartien pas a I")

intervalle()