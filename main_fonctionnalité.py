import random

from termcolor import colored, cprint


from bateau import Bateau, Porte_avion, Croiseur, Sous_marin, Torpilleur

texte_ligne = colored("ligne de la case tirée : ", 'blue', "on_white")
nb = int(input(texte_ligne))
bateau = Porte_avion(2,1,True)
cprint(f'{bateau.nom} coulé', 'light_yellow')
cprint("erreur : l'entrée doit être un entier", "white", "on_red")
nombre_tirs = 45
texte_réussite = colored(f'Bien joué, vous avez gagné en {nombre_tirs} coups', 'green', attrs=['bold','blink'])
print(texte_réussite)