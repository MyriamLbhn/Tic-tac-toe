#Grille vide 3 par 3
grille = []
for i in range(3):
    grille.append([0 for j in range(3)])
for line in grille:
    print(line)
 
# Fonction pour vérifier si le coup est possible
def choisir_case(ligne, col, player):
    grille[ligne][col] = player