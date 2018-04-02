import pydomino
import random
from pydomino.donne import *
import codecs
from pydomino.partie import *
from pydomino.pioche import *


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
        return [Donne(domino_melange[0:7]), Donne(domino_melange[7:14]), Donne(domino_melange[14:28])]
    elif nombre_joueurs == 3:
        return [Donne(domino_melange[0:6]), Donne(domino_melange[6:12]), Donne(domino_melange[12:18]), Donne(domino_melange[18:28])]
    elif nombre_joueurs == 4:
        return [Donne(domino_melange[0:6]), Donne(domino_melange[6:12]), Donne(domino_melange[12:18]),
                Donne(domino_melange[18:24]), Donne(domino_melange[24:28])]

class PartieAvecPioche(pydomino.Partie):
    """
        Documentation de la classe PartieAvecPioche. Cette classe hérite de la classe Partie.
        Attributs:
            pioche (Pioche): Pioche contenant une liste de dominos.
        """

    def __init__(self, plateau, donnes, pioche):
        super().__init__(plateau, donnes)
        self.pioche = pioche


    @classmethod
    def nouvelle_partie(cls, nombre_joueurs):
        """
        Méthode de classe pour créer une nouvelle partie avec pioche. Cette méthode instancie le plateau de jeu, crée
        les donnes des joueurs (selon le nombre de joueurs reçu en argument), la pioche et instancie l'objet partie.
        :param nombre_joueurs: (int) nombre de joueurs de la partie
        :return: (Partie) objet de la classe Partie
        """
        plateau = pydomino.Plateau()

        donnes = distribuer_dominos_avec_pioche(nombre_joueurs)[:-1]

        p_pioche = distribuer_dominos_avec_pioche(nombre_joueurs)[-1]

        partie = PartieAvecPioche(plateau, donnes, p_pioche)

        return partie

    @staticmethod
    def afficher_instructions():
        """
        Méthode statique qui affiche les instructions du jeu

        """
        fichier = codecs.open("instruction_avec_pioche.txt", "r", "utf-8")
        while True:
            ligne = fichier.readline()
            if not ligne:
                break
            print(ligne)
        fichier.close()

    def afficher_etat_donnes(self):
        """
        Méthode qui affiche l'état des donnes des joueurs de la partie avec pioche.
        L'information affichée doit contenir le numéro du joueur et le nombre de dominos de sa donne, ainsi que le
        nombre de dominos dans la pioche.
        """
        # le numéro du joueur qui doit jouer
        print("c'est au tour du joueur {} \n".format(self.tour))

        # l'état des donnes de tous les joueurs (nombre de dominos en main)
        for joueur in range(len(self.donnes)):
            print("le joueur {} a {} dominos en main et la pioche est composée de {} ".
                  format(joueur + 1, len(self.donnes[joueur]), self.pioche ))

    def faire_passer_joueur(self):
        """
        Méthode qui contient les instructions à exécuter lorsqu'un joueur doit passer son tour. Cette méthode devrait
        d'abord afficher des informations. Ensuite #le joueur courant pige un domino dans la pioche. #S'il peut jouer
        #le domino, il le joue et son tour ce termine. #S'il ne peut pas jouer, il pige un autre domino. Le joueur pigera
         des dominos tant qu'il ne pourra pas jouer le domino. Si jamais la pioche est vide, le programme affiche un
         message d'information et le joueur passe son tour.
        """
        # le joueur courant pige un domino dans la pioche
        obj_pioche = Pioche(self.donnes[-1])


        # la pioches est vide
        if self.donnes[-1] != []:

            # S'il peut #jouer le domino, il le joue et son tour ce termine
            while True:
                # prendre un domino dans la pioche
                nouvelle_domino_pioche = obj_pioche.prendre_dans_la_pioche()

                # 3) s'il peut jouer, on réinitialise l'attribut passe,le joueur joue un domino, eton vérifie s'il y a un gagnant
                if Partie.determiner_si_domino_peut_etre_joue(self, nouvelle_domino_pioche):
                    # 3.1 s'il peut jouer, on réinitialise l'attribut passe
                    self.passe = 0

                    #3.2 le joueur joue un domino
                    Partie.jouer_un_domino(self)

                    # 3.3. retirer le domino de la pioche
                    self.donnes[-1].jouer(self, nouvelle_domino_pioche)

                    # 3.4. sortir de la boucle
                    break
                else:
                # S'il ne peut pas jouer, il pige un autre domino
                    # ajouter pioche à la donne du joueur
                    obj_pioche.piger(nouvelle_domino_pioche, 0)

                    # retirer le domino de la pioche
                    self.donnes[-1].jouer(self, nouvelle_domino_pioche)

                    #si la pioche est vide, termine le boucle
                    if self.donnes[-1] == []:
                        # modifier l'attribut passe
                        self.passe += 1

                        # afficher des informations
                        print("Le joueur {} ne peut poser aucun domino et doit passer son tour".format(self.tour))
                        input("Appuyer sur ENTER pour passer ou jouer suivant")
                        break

        else:
            self.passe += 1
            print("Le joueur {} ne peut poser aucun domino et doit passer son tour".format(self.tour))
            input("Appuyer sur ENTER pour passer ou jouer suivant")



