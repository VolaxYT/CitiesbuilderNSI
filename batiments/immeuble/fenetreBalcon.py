# module porte-fenêtre

import turtle
from utils.trait import trait
from utils.rectangle import rectangle


def fenetreBalcon(x ,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre


    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    rectangle(x,y,30, 50)
    turtle.end_fill()

    # balcon
    turtle.pensize(3)
    rectangle(x,y, 40, 30)
    trait(x - 15, y, x - 15, y+30)
    trait(x - 10, y, x - 10, y+30)
    trait(x - 5, y, x - 5, y+30)
    trait(x, y, x, y+30)
    trait(x + 15, y, x + 15, y+30)
    trait(x + 10, y, x + 10, y+30)
    trait(x + 5, y, x + 5, y+30)
    turtle.pensize(1)


'''
if __name__ == '__main__':
    fenetreBalcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''