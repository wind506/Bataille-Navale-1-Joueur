from bateau import Bateau
from grille import Grille

def test_init():
    assert isinstance(Bateau(3,4), Bateau)
    assert Bateau(3,4).longueur == 1
    assert not Bateau(3,4).vertical

def test_positions():
    assert Bateau(2, 3, 3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, 3, True).positions() == [(2, 3), (3, 3), (4, 3)]

def test_coulé():
    grille = Grille(2,3)
    b1 = Bateau(1,0,2)
    cases = b1.positions()
    for case in cases:
        grille.tirer(case[0],case[1])
    assert b1.coulé(grille)

    b2 = Bateau(0,0,2)
    assert not b2.coulé(grille)
