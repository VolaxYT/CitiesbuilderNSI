# dessine la rue

import random

from param import *
import param
from batiments.immeuble.immeuble import *
from utils.manageSave import *
from utils.couleurAleatoire import couleurAleatoire

# ------------------------------
# ------------------------------
# ------------------------------

elementsList = []

def main():
    turtle.Screen().title("Dessine ta rue")
    turtle.speed(100)
    nbConstructions = (param.getWidth() - 120) // 210
    posConstruction = []
    if isRandomSteet():
        turtle.setup(param.getWidth(), param.getHeight())

        # On définit la hauteur du sol
        y_sol = -(param.getHeight() / 4)
        # Dessin du sol de la rue
        sol(y_sol, param.getWidth())

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().tracer(0)


        for i in range(0, nbConstructions):
            posConstruction.append(-(param.getWidth() / 2) + 130 + i * 210)

        # Dessin des immeubles
        for i in range(0, len(posConstruction)):
            bat = Immeuble("Default", i, posConstruction[i], y_sol,randint(1, param.getMaxEtages()), couleurAleatoire(), couleurAleatoire(), randint(1,2), [])
            bat.draw()
            elementsList.append(bat)

        # Dessin des lampadaires si allowLampadaires est à True
        if isAllowLampdaires():
            for i in range(0, len(posConstruction) - 1):
                # Dessin du lampadaire aléatoire si un nombre aléatoire est en dessous de lampadairesChance
                if random.randint(0, 100) <= getLampadairesChance():
                    lamp = Lampadaire("Default", posConstruction[i] + 105, y_sol)
                    lamp.draw()
                    elementsList.append(lamp)

        # Dessin du soleil si allowSoleil est à True
        if isAllowSoleil():
            soleil = Star("Soleil", "yellow", param.getWidth() / 2 - 80, param.getHeight() / 2 - 170, 110)
            soleil.draw()
            elementsList.append(soleil)

        # Dessiner toute la ville instantanément
        if isInstantDrawing():
            turtle.Screen().update()
    else:
        # Import à partir du fichier tout les élements de la ville
        importFile(getImportFileName())

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()


if __name__ == '__main__':
    main()
