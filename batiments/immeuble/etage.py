# module étage

from batiments.immeuble.facade import facade
from random import randint
from batiments.immeuble.fenetre import fenetre
from batiments.immeuble.fenetreBalcon import fenetreBalcon

def customEtage(x, ySol, couleur, emplacementObjetImportant, niveau):
    # dessin des murs
    facade(x, ySol + niveau * 60, couleur, 0)

    # Construit les 3 éléments (1 porte-fenetre et 2 fenetres)
    L = [0, 1, 2]
    coos = [x - 40, x, x + 40]

    fenetreBalcon(coos[emplacementObjetImportant], ySol + niveau * 60)
    L.remove(emplacementObjetImportant)

    for i in L:
        fenetre(coos[i], ySol + niveau * 60 + 20)

def etage(x, ySol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x, ySol + niveau * 60, couleur, 0)

    # Construit les 3 éléments (1 porte-fenetre et 2 fenetres)
    rdmPorteFenetre = randint(0, 2)
    L = [0, 1, 2]
    coos = [x - 40, x, x + 40]

    fenetreBalcon(coos[rdmPorteFenetre], ySol + niveau * 60)
    L.remove(rdmPorteFenetre)

    for i in L:
        fenetre(coos[i], ySol + niveau * 60 + 20)

    return rdmPorteFenetre

'''
if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
'''