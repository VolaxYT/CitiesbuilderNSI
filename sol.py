# module sol

import turtle
from utils.trait import trait
import param

def sol(y_sol, width):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    turtle.pensize(3)
    trait(-(width/2), y_sol, width/2, y_sol)
    turtle.pensize(1)

if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
