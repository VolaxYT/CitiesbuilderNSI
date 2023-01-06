# module générer une couleur aléatoire

import turtle
from random import randint

def couleurAleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''

    couleur = (randint(0,255), randint(0,255), randint(0,255))
    return couleur    

'''
if __name__ == '__main__':
    turtle.colormode(255)
    for i in range (15):
        col=couleurAleatoire()
        turtle.pencolor(col)
        turtle.forward(150)
        turtle.right(180-12)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
'''