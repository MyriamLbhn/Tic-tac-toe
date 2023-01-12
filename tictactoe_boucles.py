 #Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
for line in grille:
    print(line)
      
while True:
    # Tour Joueur 1
    print("JOUEUR 1")
    print("Choissisez la ligne puis la colonne sur laquelle vous souhaitez jouer")    
    while True:
        print("l doit être un entier entre 1 et 3")
        user_input_l = input("l= ")
        if user_input_l == "1" or user_input_l == "2" or user_input_l == "3" :
            break
    while True:
        print("c doit être un entier entre 1 et 3")
        user_input_c = input("c= ")
        if user_input_c == "1" or user_input_c == "2" or user_input_c == "3" :
            break
    while grille[int(user_input_l)-1][int(user_input_c)-1]==1 or grille[int(user_input_l)-1][int(user_input_c)-1]==2:
        print("Vous ne pouvez jouer sur une case du joueur adverse, réessayez !")
        while True:
            print("l doit être un entier entre 1 et 3")
            user_input_l = input("l= ")
            if user_input_l == "1" or user_input_l == "2" or user_input_l == "3" :
                break
        while True:
            print("c doit être un entier entre 1 et 3")
            user_input_c = input("c= ")
            if user_input_c == "1" or user_input_c == "2" or user_input_c == "3" :
                break      
    grille[int(user_input_l)-1][int(user_input_c)-1]=1
    for line in grille:
        print(line)
    
    # On verifie si un des joueurs a gagné
    if all(i[0]==1 for i in grille) or all(i[1]==1 for i in grille) or all(i[2]==1 for i in grille) :
        print("Joueur 1 a gagné")
        break
    if all(x == 1 for x in grille[0]) or all(x == 1 for x in grille[1]) or all(x == 1 for x in grille[2]):
        print("Joueur 1 a gagné")
        break
    if grille[0][0]==1 and grille[1][1]==1 and grille[2][2]==1:
        print("Joueur 1 a gagné")
        break
    if all(i[0]==2 for i in grille) or all(i[1]==2 for i in grille) or all(i[2]==2 for i in grille) :
        print("Joueur 2 a gagné")
        break
    if all(x == 2 for x in grille[0]) or all(x == 2 for x in grille[1]) or all(x == 2 for x in grille[2]):
        print("Joueur 2 a gagné")
        break
    if grille[0][0]==2 and grille[1][1]==2 and grille[2][2]==2:
        print("Joueur 2 a gagné")
        break
        
    # Tour joueur 2
    print("JOUEUR 2")
    print("Entrez la valeur des coordonnées l et c, où vous souhaitez jouer, la postion en haut à gauche correspond au couple suivant (0;0)")    
    while True:
        print("l doit être un entier entre 1 et 3")
        user_input_l = input("l= ")
        if user_input_l == "1" or user_input_l == "2" or user_input_l == "3" :
            break
    while True:
        print("c doit être un entier entre 1 et 3")
        user_input_c = input("c= ")
        if user_input_c == "1" or user_input_c == "2" or user_input_c == "3" :
            break
    while grille[int(user_input_l)-1][int(user_input_c)-1]==1 or grille[int(user_input_l)-1][int(user_input_c)-1]==2:
        print("Vous ne pouvez jouer sur une case du joueur adverse, réessayez !")
        while True:
            print("l doit être un entier entre 1 et 3")
            user_input_l = input("l= ")
            if user_input_l == "1" or user_input_l == "2" or user_input_l == "3" :
                break
        while True:
            print("c doit être un entier entre 1 et 3")
            user_input_c = input("c= ")
            if user_input_c == "1" or user_input_c == "2" or user_input_c == "3" :
                break
    grille[int(user_input_l)-1][int(user_input_c)-1]=2
    for line in grille:
        print(line)
    
    # On vérifie si un des joueurs a gagné
    if all(i[0]==1 for i in grille) or all(i[1]==1 for i in grille) or all(i[2]==1 for i in grille) :
        print("Joueur 1 a gagné")
        break
    if all(x == 1 for x in grille[0]) or all(x == 1 for x in grille[1]) or all(x == 1 for x in grille[2]):
        print("Joueur 1 a gagné")
        break
    if grille[0][0]==1 and grille[1][1]==1 and grille[2][2]==1:
        print("Joueur 1 a gagné")
        break
    if all(i[0]==2 for i in grille) or all(i[1]==2 for i in grille) or all(i[2]==2 for i in grille) :
        print("Joueur 2 a gagné")
        break
    if all(x == 2 for x in grille[0]) or all(x == 2 for x in grille[1]) or all(x == 2 for x in grille[2]):
        print("Joueur 2 a gagné")
        break
    if grille[0][0]==2 and grille[1][1]==2 and grille[2][2]==2:
        print("Joueur 2 a gagné")
        break