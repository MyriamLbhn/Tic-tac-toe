#Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
for line in grille:
    print(line)
 
# Fonction pour vérifier si le coup est possible
def choisir_case(ligne, col, joueur):
    grille[ligne][col] = joueur
    

# Fonction pour vérifier si le joueur à gagné
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
    