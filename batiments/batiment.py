# Objet mère de tout les batiments avec les variables communes à tout les batiments
class Batiment:
    def __init__(self, nom, position, x, ySol):
        self.nomBatiment = nom
        self.batimentPosition = position
        self.batimentXBase = x
        self.batimentYSol = ySol