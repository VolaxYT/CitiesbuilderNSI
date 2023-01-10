# module rdc

import turtle
from random import randint
from batiments.immeuble.facade import facade
from batiments.immeuble.porte import porte
from batiments.immeuble.fenetre import fenetre

def customRDC(x, ySol, c_facade, emplacementObjetImportant, c_porte):
    # Dessine la facade
    facade(x, ySol, c_facade, 0)

    # Construit les 3 éléments (1 porte et 2 fenetres)
    L = [0, 1, 2]
    coos = [x - 40, x, x + 40]

    porte(coos[emplacementObjetImportant], ySol, c_porte)
    L.remove(emplacementObjetImportant)

    for i in L:
        fenetre(coos[i], ySol + 20)


def rdc(x, ySol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        ySol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    facade(x, ySol, c_facade, 0)

    # Construit les 3 éléments (1 porte et 2 fenetres)
    rdmPorte = randint(0, 2)
    L = [0, 1, 2]
    coos = [x - 40, x, x + 40]

    porte(coos[rdmPorte], ySol, c_porte)
    L.remove(rdmPorte)

    for i in L:
        fenetre(coos[i], ySol + 20)

    return rdmPorte

if __name__ == '__main__':
    rdc(0, 0, "red", "green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()