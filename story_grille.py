from grille import Grille

#créer une grille à 5 lignes et 8 colonnes
grille = Grille(5,8)

#afficher la grille à l'écran
print(grille)

#demande à l'utilisateur de rentrer deux coordonnées x et y
coords_x = int(input('Rentrez la coordonnée x : '))
coords_y = int(input('Rentrez la coordonnée y : '))

#tirer à l'endroit indiqué sur la grille
grille.tirer(coords_x, coords_y)

#afficher la grille
print(grille)