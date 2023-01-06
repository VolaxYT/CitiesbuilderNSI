# module rectangle

import turtle
from trait import trait

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    trait(x, y, x + w/2, y)
    trait(x + w/2, y, x + w/2, y + h)
    trait(x + w/2, y + h, x - w/2, y + h)
    trait(x - w/2, y + h, x - w/2, y)
    trait(x - w/2, y, x, y)

'''
if __name__ == '__main__':
    rectangle(0,0,150,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''