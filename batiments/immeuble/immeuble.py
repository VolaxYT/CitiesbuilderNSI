# module immeuble

from batiments.immeuble.rdc import *
from batiments.immeuble.etage import *
from batiments.immeuble.toit import *
from batiments.batiment import Batiment

# Objet pour pouvoir stocker l'immeuble plus facilement (+ hérite de l'objet Batiment)
class Immeuble(Batiment):
    # Fonction pour dessiner l'immeuble
    def draw(self):
        turtle.colormode(255)

        #Si c'est un immeuble aléatoire
        if len(list(self.etages)) == 0:
            # Dessin du RDC
            self.etages.append(rdc(self.batimentXBase, self.batimentYSol, self.couleurFacade, self.couleurPorte))
            # Dessin des étages
            for i in range(1, self.nombreEtages):
                self.etages.append(etage(self.batimentXBase, self.batimentYSol, self.couleurFacade, i))

        # Si c'est un immeuble pré-généré
        else:
            # Dessin du RDC
            customRDC(self.batimentXBase, self.batimentYSol, self.couleurFacade, int(self.etages[0]), self.couleurPorte)
            for i in range(1, self.nombreEtages):
                # Dessin de chaque étage de l'immeuble avec ses paramètres prédéfinies d'entrées
                customEtage(self.batimentXBase, self.batimentYSol, self.couleurFacade, int(self.etages[i]), i)

        # Dessiner le toit de l'immeuble
        toit(self)

    # Fonction pour initialiser l'objet Immeuble et lui attribuer ses variables
    def __init__(self, nom, position, x, ySol, nombreEtages, couleurFacade, couleurPorte, typeToit, etages):
        #Attribut les valeurs de l'objet Batiment
        super().__init__(nom, position, x, ySol)

        # Nombre d'étage de l'immeuble
        self.nombreEtages = nombreEtages

        # Couleur de de la facade de l'immeuble
        self.couleurFacade = couleurFacade

        # Couleur de de la porte de l'immeuble
        self.couleurPorte = couleurPorte

        # Type de toit pour l'immeuble
        self.typeToit = typeToit

        # Si l'immeuble est pré-fait, permet de définir les informations importantes de chaque étage de l'immeuble (emplacement porte ou porte-fenêtre)
        self.etages = etages

    # Permet quand l'objet est appelé de renvoyer par défaut l'objet en chaîne de caractères
    def __repr__(self):
        return repr(self.toString())

    # Convertie l'objet Immeuble en une chaîne de caractères avec toute les informations relatives à l'immeuble
    def toString(self) -> str:
        return f"Immeuble;'{self.nomBatiment}';{self.batimentPosition};{self.batimentXBase};{self.batimentYSol};{self.nombreEtages};{self.couleurFacade};{self.couleurPorte};{self.typeToit};{self.etages}"