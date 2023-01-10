# module toit aléatoire

from random import randint
from batiments.immeuble.toit1 import toit1
from batiments.immeuble.toit2 import toit2

def customToit(x, ySol, typeToit, niveau):
    if typeToit == "toit1":
        toit1(x, ySol, niveau)
    else:
        toit2(x, ySol, niveau)

def toit(x, ySol, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    if randint(0, 1) == 0:
        toit1(x, ySol, niveau)
        return "toit1"
    else:
        toit2(x, ySol, niveau)
        return "toit2"

if __name__ == '__main__':
    toit(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()