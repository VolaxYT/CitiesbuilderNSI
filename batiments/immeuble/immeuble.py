# module immeuble

import turtle
from utils.couleurAleatoire import couleurAleatoire
from batiments.immeuble.rdc import *
from batiments.immeuble.etage import *
from batiments.immeuble.toit import *
import param
from batiments.batiment import Batiment

class Immeuble(Batiment):
    def draw(self):
        turtle.colormode(255)

        #Si c'est un immeuble aléatoire
        if len(list(self.etages)) == 0:
            # Dessin du RDC
            self.etages.append(rdc(self.batimentXBase, self.batimentYSol, self.couleurFacade, self.couleurPorte))
            # Dessin des étages
            for i in range(1, self.nombreEtages):
                self.etages.append(etage(self.batimentXBase, self.batimentYSol, self.couleurFacade, i))

        # Si c'est un immeuble prégénéré
        else:
            # Dessin du RDC
            customRDC(self.batimentXBase, self.batimentYSol, self.couleurFacade, int(self.etages[0]), self.couleurPorte)
            for i in range(1, self.nombreEtages):
                customEtage(self.batimentXBase, self.batimentYSol, self.couleurFacade, int(self.etages[i]), i)

        # Si c'est un immeuble aléatoire
        if self.typeToit == "":
            self.typeToit = toit(self.batimentXBase, self.batimentYSol, self.nombreEtages)
        else:
            self.typeToit = customToit(self.batimentXBase, self.batimentYSol, self.typeToit, self.nombreEtages)

    def __init__(self, nom: str, position: int, x, ySol, nombreEtages, couleurFacade, couleurPorte, typeToit, etages):
        super().__init__(nom, position, x, ySol)

        # Nombre d'étage (aléatoire)
        if nombreEtages == 0:
            self.nombreEtages = randint(1, param.getMaxEtages())
        else:
            self.nombreEtages = nombreEtages

        # Couleurs des éléments (aléatoire)
        if couleurFacade == 0:
            self.couleurFacade = couleurAleatoire()
        else:
            self.couleurFacade = couleurFacade

        if couleurPorte == 0:
            self.couleurPorte = couleurAleatoire()
        else:
            self.couleurPorte = couleurPorte

        if etages == 0:
            self.etages = []
        else:
            self.etages = etages

        if typeToit == 0:
            self.typeToit = ""
        else:
            self.typeToit = typeToit

    def __repr__(self):
        return repr(self.toString())

    def toString(self) -> str:
        return f"Immeuble;'{self.nomBatiment}';{self.batimentPosition};{self.batimentXBase};{self.batimentYSol};{self.nombreEtages};{self.couleurFacade};{self.couleurPorte};{self.typeToit};{self.etages}"
'''
if __name__ == '__main__':
    immeuble(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''