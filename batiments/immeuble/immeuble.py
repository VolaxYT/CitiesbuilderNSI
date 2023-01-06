# module immeuble

import turtle
from utils.couleurAleatoire import couleurAleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit
import param


def immeuble(x, ySol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)
    nb = randint(1, param.getMaxEtages())

    #Couleurs des éléments (aléatoire)
    couleur = couleurAleatoire()

    turtle.colormode(255)

    # Dessin du RDC
    rdc(x, ySol, couleur, couleurAleatoire())

    # Dessin des étages
    for i in range(1, nb):
        etage(x ,ySol, couleur, i)

    toit(x, ySol, nb)

    pass

'''
if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''