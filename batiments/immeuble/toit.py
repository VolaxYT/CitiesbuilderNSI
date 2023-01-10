# module toit aléatoire

from batiments.immeuble.toit1 import toit1
from batiments.immeuble.toit2 import toit2

def toit(immeuble):
    '''
    Paramètres
        immeuble : Objet immeuble qui permet de récupérer les variables de l'immeuble
    Cette fonction dessine le toit correspondant à self.typeToit
    '''
    if immeuble.typeToit == 1:
        toit1(immeuble.batimentXBase, immeuble.batimentYSol, immeuble.nombreEtages)
    else:
        toit2(immeuble.batimentXBase, immeuble.batimentYSol, immeuble.nombreEtages)