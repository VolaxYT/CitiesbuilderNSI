# programme principal (dessine une rue)

import turtle
import random

import param
from param import *
from sol import sol
from batiments.immeuble.immeuble import immeuble
from lampadaire import lampadaire
from soleil import soleil

# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(param.getWidth(), param.getHeight())
    turtle.Screen().title("Dessine ta rue")
    turtle.speed(100)

    nbConstructions = (param.getWidth() - 120) // 210
    posConstruction = []

    # On définit la hauteur du sol
    y_sol = -(param.getHeight() / 4)
    # Dessin du sol de la rue
    sol(y_sol)

    #Dessin du soleil si allowSoleil est à True
    if getAllowSoleil():
        soleil(param.getWidth() / 2 - 80, param.getHeight() / 2 - 170, 110)

    for i in range(0, nbConstructions):
        posConstruction.append(-(param.getWidth() / 2) + 130 + i*210)

    # Dessin des immeubles
    for i in posConstruction:
        immeuble(i, y_sol)

    # Dessin des lampadaires si allowLampadaires est à True
    if getAllowLampadaires():
        for i in range(0, len(posConstruction) - 1):
            # Dessin du lampadaire aléatoire si un nombre aléatoire est en dessous de lampadairesChance%
            if random.randint(0, 100) <= getLampadairesChance():
                lampadaire(posConstruction[i] + 105, y_sol)



    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

'''
if __name__ == '__main__':
    main()
    '''