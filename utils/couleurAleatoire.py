# module générer une couleur aléatoire

import turtle
from rectangle import rectangle
from random import randint

def gen_col_grey():
    col = randint(0,200)
    return col, col, col

def gen_col_red():
    col = randint(0,255)
    return 255, col, col

def gen_col_green():
    col = randint(0,255)
    return col, 255, col

def gen_col_blue():
    col = randint(0,255)
    return col, col, 255

def couleurAleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''

    couleur = (randint(0,255), randint(0,255), randint(0,255))
    return couleur    

if __name__ == '__main__':
    turtle.colormode(255)
    col = gen_col_green()
    turtle.pencolor(col)
    turtle.begin_fill()
    turtle.fillcolor(col)
    rectangle(100, 100, 100, 100)
    turtle.end_fill()
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()