import pydomino


class Plateau:
    """
        Documentation de la classe Plateau
        Attributs:
            plateau (list): Liste de dominos contenant les dominos qui ont été joués.
        """

    def __init__(self):
        self.plateau = []

    def cote_gauche(self):
        """
        Méthode qui retourne la valeur numérique à gauche du plateau
        :return: La valeur extérieure du domino de gauche.
        """

        # TODO À compléter
        pass

    def cote_droit(self):
        """
        Méthode qui retourne la valeur numérique à droite du plateau
        :return: La valeur extérieure du domino de droite.
        """
        # TODO À compléter
        pass

    def ajouter_a_gauche(self, domino):
        """
        Méthode qui ajoute le domino reçu en argument à gauche du plateau. Le domino devra peut-être être inversé pour
        que les chiffres qui se touchent soient identiques.
        :param domino: (Domino) Le domino à ajouter à gauche.
        """

        # TODO À compléter
        pass

    def ajouter_a_droite(self, domino):
        """
        Méthode qui ajoute le domino reçu en argument à gauche du plateau. Le domino devra peut-être être inversé pour
        que les chiffres qui se touchent soient identiques.
        :param domino: (Domino) Le domino à ajouter à droite.
        """

        # TODO À compléter
        pass

    def ajouter(self, domino, gauche):
        """
        Méthode qui ajoute le domino reçu en argument à gauche ou à droite du plateau.
        :param domino: (Domino) Le domino à ajouter à droite.
        :param gauche: (bool) True si le domino doit être ajouté gauche, False autrement
        """

        # TODO À compléter
        pass

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self.plateau)

    def __str__(self):
        """
        Méthode qui retourne une chaîne de caractères qui représente la liste de dominos sur le plateay en une ligne.
        :return: str: liste des dominos du plateau
        """
        # TODO: À compléter
        pass

    def __repr__(self):
        return str(self)
