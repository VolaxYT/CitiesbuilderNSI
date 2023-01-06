# module sol

import turtle
from utils.trait import trait
import param

def sol(y_sol):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''
    turtle.pensize(3)
    trait(-(param.getWidth()/2), y_sol, param.getWidth()/2, y_sol)
    turtle.pensize(1)

'''
if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''
