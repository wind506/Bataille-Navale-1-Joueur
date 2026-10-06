from grille import Grille, calcul_cases
from bateau import Bateau

def test_init():
    assert isinstance(Grille(4,5), Grille)


def test_tirer():
    grille = Grille(4,5)
    grille.tirer(1,1)
    assert grille.matrice[6] == 'x'

def test_str():
    grille = Grille(5,8)
    assert str(grille) == '~~~~~~~~\n~~~~~~~~\n~~~~~~~~\n~~~~~~~~\n~~~~~~~~'

def test_ajoute():
    g1 = Grille(2,3)
    g1.ajoute(Bateau(1, 0, 2, False))
    assert g1.matrice == ["~", "~", "~", "⛵", "⛵", "~"]

    g2 = Grille(2,3)
    g2.ajoute(Bateau(1, 0, 2, True))
    g2.ajoute(Bateau(1, 0, 4, True))
    assert g2.matrice == ['~','~','~','~','~','~']


def test_calcul_cases():
    assert calcul_cases([],2,3,2) == [(0, 0, False), (0, 0, True), (0, 1, False), (0, 1, True), (0, 2, True), (1, 0, False), (1, 1, False)]