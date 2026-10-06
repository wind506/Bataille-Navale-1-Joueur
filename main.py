import random
from termcolor import colored, cprint

from grille import Grille, calcul_cases
from bateau import Porte_avion, Croiseur, Sous_marin, Torpilleur

#création de la grille de jeu
grille_jeu = Grille(8,10)
liste_bateaux = []
cases_occupées = []

for classe, longueur in [(Porte_avion, 4), (Croiseur, 3), (Torpilleur, 2), (Sous_marin, 3)]:
    cases_possibles = calcul_cases(cases_occupées, 8, 10, longueur)
    ligne, colonne, vertical = random.choice(cases_possibles)
    bateau = classe(ligne, colonne, vertical)
    liste_bateaux.append(bateau)
    cases_occupées += bateau.positions()

#déroulement de la partie
nombre_tirs = 0
nombre_bateaux_coulées = 0
texte_ligne = colored("ligne de la case tirée :", 'white')
texte_colonne = colored("colonne de la case tirée :", 'white')

while nombre_bateaux_coulées < 4:
    grille_jeu.afficher()

    while True:
        try:
            tir_ligne = int(input(texte_ligne))
            tir_colonne = int(input(texte_colonne))
            if tir_ligne > 7 or tir_colonne > 9 :
                cprint('erreur : case non présente sur la grille', 'white', 'on_red')
                break
            if grille_jeu.matrice[tir_ligne * grille_jeu.nombre_colonnes + tir_colonne] in ['💥','🚣','⛴','🐟','🚢','💣']:
                cprint('vous avez déja tiré sur cette case, essayez en une autre', 'white', 'on_red')
                break
            grille_jeu.tirer(tir_ligne, tir_colonne)
            if (tir_ligne, tir_colonne) in cases_occupées:
                grille_jeu.matrice[tir_ligne * grille_jeu.nombre_colonnes + tir_colonne] = '💣'
            for bateau in liste_bateaux:
                if bateau.coulé(grille_jeu):
                    nombre_bateaux_coulées += 1
                    grille_jeu.ajoute(bateau)
                    cprint(f'{bateau.nom} coulé', 'light_yellow')
            nombre_tirs += 1
            break
        except ValueError:
            cprint("erreur : l'entrée doit être un entier", "white", "on_red")

texte_réussite = colored(f'Bien joué, vous avez gagné en {nombre_tirs} coups', 'green', attrs=['bold','blink'])
print(texte_réussite)