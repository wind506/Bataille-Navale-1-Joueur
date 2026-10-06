from bateau import Bateau

#créer un bateau b1 et un bateau b2 qui se chevauchent
b1 = Bateau(2, 3,3, False)
b2 = Bateau(2, 4,3, True)

#affiche les cases occupées par les bateaux
print(b1.positions())
print(b2.positions())

#vérification du chevauchement
chevauchement  = any(element in b1.positions() for element in b2.positions())
if chevauchement:
    print('il y a chevauchement des deux bateaux')
else:
    print("il n'y a pas chevauchement des bateaux")