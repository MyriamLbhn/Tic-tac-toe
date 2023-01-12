#Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
    
# Fonction pour aficher la grille :
def afficher_grille(grille):
    for line in grille:
        print(line)
 
# Fonction pour choisir où jouer :
def choisir_case(ligne, col, joueur):
    grille[ligne][col] = joueur
    
# Fonction pour vérifier si un joueur a gagné
def victoire_jeu(grille, joueur):
    # Lignes
    for i in range(3):
        victoire = True
        for j in range(3):
            if grille[i][j] != joueur:
                victoire = False
                break
        if victoire:
            return victoire
    # Colonnes
    for i in range(3):
        victoire = True
        for j in range(3):
            if grille[j][i] != joueur:
                victoire = False
                break
        if victoire:
            return victoire
    # Diagonale 1
    for i in range(3):
        victoire = True
        if grille[i][2-i] != joueur:
            victoire = False
            break
        if victoire:
            return victoire
    # Diagonale 2
    for i in range(3):
        victoire = True
        if grille[i][i] != joueur:
            victoire = False
            break
        if victoire:
            return victoire
    
# Fonction pour vérifier si le coup est possible 
def coup_possible(ligne, col, joueur):
    possible = False
    if grile[ligne][col]==0:
        possible = True
        return possible

        
        
