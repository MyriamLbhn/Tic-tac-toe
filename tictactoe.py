#Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
    
# Fonction pour aficher la grille :
def afficher_grille(grille: list)-> list:
    """Fonction qui affiche la grille 3x3 du Tic-tac-toe

    Args:
        grille (list): Une liste de 3 éléments

    Returns:
        list: Une liste composée de 3 liste, affichée les unes en dessous des autres
    """
    for line in grille:
        print(line)
 
# Fonction pour choisir où jouer :
def choisir_case()-> int:
    """Fonction qui permet à l'utilisateur de choisir où il souhaite jouer sur la grille

    Returns:
        int: Indice de la ligne, et de la colonne (1, 2 ou 3)
    """
    print("Choissisez la ligne puis la colonne sur laquelle vous souhaitez jouer")    
    ligne = eval(input("l= "))
    col = eval(input("c= "))
    return(ligne, col)
    
# Fonction pour vérifier si un joueur a gagné :
def est_gagnee(grille: list, joueur: int)-> bool:
    """Fonction qui vérifie sur la partie est gagnée par un des joueurs

    Args:
        grille (list): la grille du jeu
        joueur (int): le numéro du joueur (1 ou 2)

    Returns:
        bool: Retourne "True" en cas de victoire
    """
    # Lignes
    for ligne in grille:
        if ligne[0]==ligne[1]==ligne[2]==joueur:
            return True
    # Colonne
    for i in range(3):
        if grille[0][i]==grille[1][i]==grille[2][i]==joueur:
            return True
    # Diagonale 1
    if grille[0][0]==grille[1][1]==grille[2][2]==joueur:
        return True
    # Diagonale 2
    if grille[0][2]==grille[1][1]==grille[2][0]== joueur:
         return True
    return False
    
# Fonction pour vérifier si le coup est possible 
def coup_possible(ligne: int,col: int)-> bool:
    """Fonction qui indique si le coup est possible. C'est-à-dire si la ligne et la colonne choisies par l'utilisateur\n
    correspond à une case non jouée de la grille.

    Args:
        ligne (int): Indice de la ligne (1, 2 ou 3)
        col (int): Indice de la colonne (1, 2 ou 3)
    Returns:
        bool: Retourne "True" si le coup est possible.
    """
    possible = None
    if ligne in (1,2,3) and col in (1,2,3):
        if grille[ligne-1][col-1]==0:
            possible = True
    return possible
     
# Jeu
afficher_grille(grille)
tour=0
joueur = 0
while True:
    tour+=1
    if tour>9:
        print("Fin de la partie, égalité !")
        break 
    if tour%2!=0:
        joueur = 1
    else:
        joueur = 2
    #print(tour)
    print("JOUEUR "+str(joueur))  
    ligne, col=choisir_case()
    while not coup_possible(ligne, col):
        print("Vous devez choisir une case vide existante !")
        ligne, col=choisir_case()
        afficher_grille(grille)
    grille[ligne-1][col-1]= joueur
    afficher_grille(grille)
    if est_gagnee(grille, joueur):
        print("Victoire du Joueur "+ str(joueur))
        break

        

    
    
        
        
