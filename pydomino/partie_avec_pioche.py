import pydomino
import random


def distribuer_dominos_avec_pioche(nombre_joueurs):
    """
        Méthode pour créer les donnes des joueurs et la pioche. Pour une partie à 2 joueurs, 7 dominos sont distribués
        aux joueurs. Pour une partie à 3 ou 4 joueurs, 6 dominos sont distribués aux joueurs. Pour cette fonction, nous
        vous suggérons de générer tous les dominos de l'ensemble 'double-six', ensuite de les brasser aléatoirement
        (voir la fonction shuffle du module random), et de retourner le nombre de donnes demandé. Dans tous les cas,
        les jetons restants forment la pioche.
        :param nombre_joueurs: (int) Nombre de joueurs de la partie.
        :returns: (list) La liste des donnes de dominos des joueurs.
                (Pioche) L'objet pioche.
        """
    # créer domino complet
    serie = [x for x in range(7)]
    domino_melange = []
    for i in serie:
        for j in range(i + 1):
            domino_melange.append([j, i])
    random.shuffle(domino_melange)

    # dominos distribués aux joueurs
    if nombre_joueurs == 2:
        donnes= [domino_melange[0:7], domino_melange[7:14], domino_melange[14:28]]
        return donnes
    elif nombre_joueurs == 3:
        donnes = [domino_melange[0:6], domino_melange[6:12], domino_melange[12:18], domino_melange[18:28]]
        return donnes
    elif nombre_joueurs == 4:
        donnes = [domino_melange[0:6], domino_melange[6:12], domino_melange[12:18], domino_melange[18:24], domino_melange[24:28]]
        return donnes

class PartieAvecPioche(pydomino.Partie):
    """
        Documentation de la classe PartieAvecPioche. Cette classe hérite de la classe Partie.
        Attributs:
            pioche (Pioche): Pioche contenant une liste de dominos.
        """

    def __init__(self, plateau, donnes, pioche):

        self.pioche = pioche
        super().__init__(plateau, donnes)

    @classmethod
    def nouvelle_partie(cls, nombre_joueurs):
        """
        Méthode de classe pour créer une nouvelle partie avec pioche. Cette méthode instancie le plateau de jeu, crée
        les donnes des joueurs (selon le nombre de joueurs reçu en argument), la pioche et instancie l'objet partie.
        :param nombre_joueurs: (int) nombre de joueurs de la partie
        :return: (Partie) objet de la classe Partie
        """
        plateau = pydomino.Plateau()

        donnes, pioche = distribuer_dominos_avec_pioche(nombre_joueurs)

        partie = cls(plateau, donnes, pioche)

        return partie

    @staticmethod
    def afficher_instructions():
        """
        Méthode statique qui affiche les instructions du jeu

        """
        # TODO À compléter
        pass

    def afficher_etat_donnes(self):
        """
        Méthode qui affiche l'état des donnes des joueurs de la partie avec pioche.
        L'information affichée doit contenir le numéro du joueur et le nombre de dominos de sa donne, ainsi que le
        nombre de dominos dans la pioche.
        """
        # TODO À compléter
        pass

    def faire_passer_joueur(self):
        """
        Méthode qui contient les instructions à exécuter lorsqu'un joueur doit passer son tour. Cette méthode devrait
        d'abord afficher des informations. Ensuite le joueur courant pige un domino dans la pioche. S'il peut jouer le
         domino, il le joue et son tour ce termine. S'il ne peut pas jouer, il pige un autre domino. Le joueur pigera
         des dominos tant qu'il ne pourra pas jouer le domino. Si jamais la pioche est vide, le programme affiche un
         message d'information et le joueur passe son tour.
        """
        # TODO: À compléter
        pass
