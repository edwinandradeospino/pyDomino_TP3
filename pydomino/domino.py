"""
Module contenant la description de la classe Domino. Un domino contient deux chiffres.
"""


class Domino:
    """
    Documentation de la classe Domino
    Attributs:
        premier_chiffre (int): Premier chiffre du domino (entier entre 0 et 6)
        deuxiement_chiffre (int): Deuxieme chiffre du domino (entier entre 0 et 6)
    """

    def __init__(self, premier_chiffre, deuxieme_chiffre):
        self.premier_chiffre = premier_chiffre
        self.deuxieme_chiffre = deuxieme_chiffre

    def inverser(self):
        # Cette méthode retourne un objet domino où les chiffres ont été inversés.
        return self.deuxieme_chiffre, self.premier_chiffre

    def __str__(self):
        # Cette méthode retourne une chaîne de caractère qui représente l'objet domino.
        return "[{}|{}]".format(self.premier_chiffre,self.deuxieme_chiffre)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Cette méthode spécifie le test d'équivalence entre deux objets de la classe domino.
        :param other: Autre objet à comparer avec celui-ci
        """
        if not isinstance(other, type(self)):
            return False
        else:
            return sorted((self.premier_chiffre, self.deuxieme_chiffre)) == \
                   sorted((other.premier_chiffre, other.deuxieme_chiffre))

    def __hash__(self):
        """
        Cette méthode spécifie la fonction de hachage pour les objets de la classe domino. Ceci permet de créer des
        ensembles d'objets de cette classe
        """
        return hash(tuple(sorted((self.premier_chiffre, self.deuxieme_chiffre))))

    def __contains__(self, key):
        """
        Cette méthode spécifie le test d'appartenance pour un entier dans un objet de la classe domino
        :param key (int): Chiffre dont on vérifier l'appartenance dans l'objet domino
        :return (bool): True si le chiffre key est présent dans les attributs du domino, False autrement
        """
        return key == self.premier_chiffre or key == self.deuxieme_chiffre
