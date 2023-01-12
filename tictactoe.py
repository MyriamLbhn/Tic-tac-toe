#Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
    
# Fonction pour aficher la grille :
def afficher_grille(grille):
    for line in grille:
        print(line)
 
# Fonction pour choisir où jouer :
def choisir_case():
    print("Choissisez la ligne puis la colonne sur laquelle vous souhaitez jouer")    
    ligne = eval(input("l= "))
    col = eval(input("c= "))
    return(ligne, col)
    
# Fonction pour vérifier si un joueur a gagné :
def est_gagnee(grille, joueur):
    # victoire = None
    # # Lignes
    # for i in range(3):
    #     victoire = True
    #     for j in range(3):
    #         if grille[i][j] != joueur:
    #             victoire = False
    #             break
    #     if victoire:
    #         return victoire
    # # Colonnes
    # for i in range(3):
    #     victoire = True
    #     for j in range(3):
    #         if grille[j][i] != joueur:
    #             victoire = False
    #             break
    #     if victoire:
    #         return victoire
    # # Diagonale 1
    # for i in range(3):
    #     victoire = True
    #     if grille[i][2-i] != joueur:
    #         victoire = False
    #         break
    #     if victoire:
    #         return victoire
    # # Diagonale 2
    # for i in range(3):
    #     victoire = True
    #     if grille[i][i] != joueur:
    #         victoire = False
    #         break
    #     if victoire:
    #         return victoire

    # Lignes
    for ligne in grille:
        if ligne[0]==ligne[1]==ligne[2]==joueur:
            return True
    # Colonne
    for i in range(3):
        if grille[0][i]==grille[1][i]==grille[2][i]==joueur:
            return True
    # Diagonale 1
    for i in range(3):
        if grille[0][0]==grille[1][1]==grille[2][2]==joueur:
            return True
    # Diagonale 2
    for i in range(3):
        if grille[0][2]==grille[1][1]==grille[2][0]== joueur:
            return True
    return False
    
# Fonction pour vérifier si le coup est possible 
def coup_possible(ligne,col):
    possible = None
    if ligne in (1,2,3) and col in (1,2,3):
        if grille[ligne-1][col-1]==0:
            possible = True
    return possible
     
# Jeu
afficher_grille(grille)

joueur = 1
print("JOUEUR "+str(joueur))
while True:    
    ligne, col=choisir_case()
    if coup_possible(ligne, col):
        grille[ligne-1][col-1]= joueur
        afficher_grille(grille)
    else:
        print("Vous devez choisir une case vide existante !")
    if est_gagnee(grille, joueur):
        print(est_gagnee(grille, joueur))
        print("Victoire")
        break
    
    
        
        
