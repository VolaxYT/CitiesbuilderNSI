# programme principal (dessine une rue)

import random
import turtle

from param import *
from sol import sol
from batiments.immeuble.immeuble import *
from others.lampadaire import lampadaire
from others.soleil import soleil
from utils.manageSave import *


# ------------------------------
# ------------------------------
# ------------------------------

batimentsList = []

def main():
    turtle.setup(param.getWidth(), param.getHeight())
    turtle.Screen().title("Dessine ta rue")
    turtle.speed(100)

    nbConstructions = (param.getWidth() - 120) // 210
    posConstruction = []

    if isRandomSteet():
        # On définit la hauteur du sol
        y_sol = -(param.getHeight() / 4)
        # Dessin du sol de la rue
        sol(y_sol)

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().tracer(0)

        # Dessin du soleil si allowSoleil est à True
        if isAllowSoleil():
            soleil(param.getWidth() / 2 - 80, param.getHeight() / 2 - 170, 110)

        for i in range(0, nbConstructions):
            posConstruction.append(-(param.getWidth() / 2) + 130 + i * 210)


        # Dessin des immeubles
        for i in range(0, len(posConstruction)):
            bat = Immeuble("Default", i, posConstruction[i], y_sol,0,0,0,0,0)
            bat.draw()
            batimentsList.append(bat)

        for bat in batimentsList:
            print(bat)

        # Dessin des lampadaires si allowLampadaires est à True
        if isAllowLampdaires():
            for i in range(0, len(posConstruction) - 1):
                # Dessin du lampadaire aléatoire si un nombre aléatoire est en dessous de lampadairesChance%
                if random.randint(0, 100) <= getLampadairesChance():
                    lampadaire(posConstruction[i] + 105, y_sol)

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().update()
    else:
        # On définit la hauteur du sol
        y_sol = -(param.getHeight() / 4)
        # Dessin du sol de la rue
        sol(y_sol)

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().tracer(0)

        # Dessin du soleil si allowSoleil est à True
        if isAllowSoleil():
            soleil(param.getWidth() / 2 - 80, param.getHeight() / 2 - 170, 110)

        for i in range(0, nbConstructions):
            posConstruction.append(-(param.getWidth() / 2) + 130 + i * 210)

        # Dessin des immeubles
        importFile(getImportFileName())

        for bat in batimentsList:
            print(bat)

        # Dessin des lampadaires si allowLampadaires est à True
        if isAllowLampdaires():
            for i in range(0, len(posConstruction) - 1):
                # Dessin du lampadaire aléatoire si un nombre aléatoire est en dessous de lampadairesChance%
                if random.randint(0, 100) <= getLampadairesChance():
                    lampadaire(posConstruction[i] + 105, y_sol)

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().update()

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()


'''
if __name__ == '__main__':
    main()
    '''
