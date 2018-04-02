import pydomino
from random import randint


class Pioche(pydomino.Donne):
    """
    Documentation de la classe Pioche. Cette classe hérite de la classe Donne
    Attributs:
        Aucun attribut spécifique autre que ceux de la classe Donne.
    """

    def prendre_dans_la_pioche(self):
        """
        Méthode pour prendre un domino dans la pioche.
        :return:
            (domino): le domino pris dans la pioche
        """
        if len(self.dominos) == 0:
            return []
        else:
            return self.dominos[randint(0, (len(self.dominos) - 1))]


