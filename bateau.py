class Bateau:

    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        cases = []
        if not self.vertical:
            for i in range(self.longueur):
                cases.append((self.ligne, self.colonne + i))
        else:
            for i in range(self.longueur):
                cases.append((self.ligne + i, self.colonne))
        return cases

    def coulé(self, grille):
        cases = self.positions()
        for case in cases:
            if grille.matrice[case[0]*grille.nombre_colonnes + case[1]] != '💣':
                return False
        return True

class Porte_avion(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne, colonne,4, vertical)
        self.nom = 'Porte avion'


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne, colonne,3, vertical)
        self.nom ='Croiseur'

class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne, colonne,2, vertical)
        self.nom ='Torpilleur'

class Sous_marin(Bateau):
    def __init__(self, ligne, colonne, vertical = False):
        super().__init__(ligne, colonne,2, vertical)
        self.nom ='Sous marin'



