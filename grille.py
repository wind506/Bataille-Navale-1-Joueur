from prettytable import PrettyTable

from bateau import Porte_avion,Sous_marin,Croiseur,Torpilleur

class Grille:
    vide = '~'
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes
        self.matrice = [Grille.vide] * nombre_colonnes*nombre_lignes

    def tirer(self, ligne, colonne, touche='💥'):
        self.matrice[ligne * self.nombre_colonnes+colonne] = touche

    def __str__(self):
        i = 0
        lignes = ''
        for chr in self.matrice:
            lignes += chr
            i += 1
            if i % self.nombre_colonnes == 0 and i < len(self.matrice):
                lignes += ('\n')
        return lignes

    def ajoute(self, bateau):
        cases = bateau.positions()

        if isinstance(bateau, Porte_avion):
            marque = '🚢'
        elif isinstance(bateau, Sous_marin):
            marque = '🐟'
        elif isinstance(bateau, Croiseur):
            marque = '⛴'
        elif isinstance(bateau, Torpilleur):
            marque = '🚣'
        else:
            marque = '⛵'

        if cases[-1][0] < self.nombre_lignes and cases[-1][1] < self.nombre_colonnes:
            for case in cases:
                ligne = case[0]
                colonne = case[1]
                self.matrice[ligne * self.nombre_colonnes+colonne] = marque

    def afficher(self):
        table = PrettyTable()
        table.field_names = [""] + [str(c) for c in range(self.nombre_colonnes)]
        for l in range(self.nombre_lignes):
            debut = l * self.nombre_colonnes
            table.add_row([l] + self.matrice[debut:debut + self.nombre_colonnes])
        table.align = "c"  # centré
        print(table)


def calcul_cases(cases_occupées, lignes, colonnes, longueur_bateau):
    occupées = set(cases_occupées)
    départs = []
    for ligne in range(lignes):
        for colonne in range(colonnes):

            # Horizontal
            if colonne + longueur_bateau <= colonnes and all(
                    (ligne, colonne + i) not in occupées for i in range(longueur_bateau)
            ):
                départs.append((ligne, colonne, False))

            # Vertical
            if ligne + longueur_bateau <= lignes and all(
                    (ligne + i, colonne) not in occupées for i in range(longueur_bateau)
            ):
                départs.append((ligne, colonne, True))

    return départs

