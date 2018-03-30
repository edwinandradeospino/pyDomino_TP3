"""
Module contenant la description de la classe Partie. Cette contient toutes les méthodes pour jouer une partie de
domino sans pioche.
"""

import pydomino
import random
from pydomino.plateau import *
from pydomino.donne import *
import codecs
from pydomino.domino import *


def distribuer_dominos(nombre_joueurs):
    """
    Méthode pour créer les donnes des joueurs. Pour une partie à 2 joueurs, 7 dominos sont distribués aux joueurs. Pour
    une partie à 3 ou 4 joueurs, 6 dominos sont distribués aux joueurs. Pour cette fonction, nous vous suggérons de
    générer tous les dominos de l'ensemble 'double-six', ensuite de les brasser aléatoirement (voir la fonction shuffle
    du module random), et de retourner le nombre de donnes demandé.
    :param nombre_joueurs: (int) Nombre de joueurs de la partie.
    :return: (list) La liste des donnes de dominos des joueurs.
    """
    #créer domino complet
    serie = [x for x in range(7)]
    domino_melange = []
    for i in serie:
        for j in range(i + 1):
            domino_melange.append([j, i])
    random.shuffle(domino_melange)

    # dominos distribués aux joueurs
    if nombre_joueurs == 2:
        return [Donne(domino_melange[0:7]), Donne(domino_melange[7:14])]
    elif nombre_joueurs == 3:
        return [Donne(domino_melange[0:6]), Donne(domino_melange[6:12]), Donne(domino_melange[12:18])]
    elif nombre_joueurs == 4:
        return [Donne(domino_melange[0:6]), Donne(domino_melange[6:12]), Donne(domino_melange[12:18]),
                Donne(domino_melange[18:24])]

class Partie:
    """
    Documentation de la classe Partie
    Attributs:
        plateau (Plateau): Objet qui contiendra les dominos qui seront joués par les joueurs
        donnes (list): Liste des donnes des joueurs. Les donnes sont des objets de la classe Donne
        tour (int): Nombre qui représente le joueur dont c'est le tour de jouer
        passe (int): Nombre de joueurs consécutifs qui passent leur tour.
        gagnant (int): Nombre qui représente le joueur gagnant lorsqu'on joueur gagne la partie
    """

    def __init__(self, plateau, donnes):
        self.plateau = plateau
        self.donnes = donnes
        self.tour = None
        self.passe = 0
        self.gagnant = None

    @classmethod
    def nouvelle_partie(cls, nombre_joueurs):
        """
        Méthode de classe pour créer une nouvelle partie. Cette méthode instancie le plateau de jeu, crée les donnes
        des joueurs (selon le nombre de joueurs reçu en argument) et instancie l'objet partie.
        :param nombre_joueurs: (int) nombre de joueurs de la partie
        :return: (Partie) objet de la classe Partie
        """

        plateau = pydomino.Plateau()

        donnes = distribuer_dominos(nombre_joueurs)

        partie = pydomino.Partie(plateau, donnes)

        return partie

    @staticmethod
    def afficher_instructions():
        """
        Méthode statique qui affiche les instructions du jeu
        """
        fichier = codecs.open("instruction_sans_pioche.txt", "r","utf-8")
        while True:
            ligne = fichier.readline()
            if not ligne:
                break
            print(ligne)
        fichier.close()

    def afficher_etat_donnes(self):
        """
        Méthode qui affiche l'état des donnes des joueurs de la partie.
        L'information affichée doit contenir le numéro du joueur et le nombre de dominos de sa donne.
        """
        # TODO: À compléter
        pass

    def trouver_premier_joueur(self):
        """
        Méthode qui détermine le premier joueur à déposer un domino sur le plateau. Ce joueur est celui qui a le domino
        le plus élevé ([6,6], [5,6], [5,5], ou moins).
        :return:
            int: le numéro du joueur ayant le domino le plus élevé
            domino: le domino le plus élevé de ce joueur
        """
        # trouver joueur avec le domino le plus haut

        domino_organise = sorted(zip(sorted([[[x + y], sorted([x, y], reverse=False)] for x in range(7) for y in range(x + 1)],
                           reverse=True), sorted([i for i in range(28)], reverse=True)), reverse=True)

        # chercher les dominos le plus hauts dans chaque donne
        domino_plus_haut_chaque_donne = []
        for donne in self.donnes:
            domino_plus_haut_chaque_donne.append((sorted(donne, reverse=True))[0])

        # chercher les indices de chaque donne
        domino_indice = []
        domino_joueur = []
        for indice in range(len(domino_plus_haut_chaque_donne)):
            for i in range(len(domino_organise)):
                if domino_organise[i][0][1] == domino_plus_haut_chaque_donne[indice]:
                    domino_indice.append(domino_organise[i][1])
                    domino_joueur.append(indice + 1)

        # agrouper les indices et les dominos et choisir le domino le plus haut
        domino_le_plus_haut = sorted(zip(domino_indice, domino_plus_haut_chaque_donne, domino_joueur), reverse=True)[0]

        # registre le tour du premier joueur
        self.tour = domino_le_plus_haut[2]

        #retourner la valeur du indice(joueur) et le domino le plus haut
        return (domino_le_plus_haut[2], domino_le_plus_haut[1])


    def passer_au_prochain_joueur(self):
        """
        Méthode qui modifie l'attribut self.tour pour passer au joueur suivant.
        """
        self.tour += 1
        if self.tour % self.donnes.__len__() == 0:
            self.tour = self.donnes.__len__()
        else:
            self.tour = self.tour % self.donnes.__len__()


    def tour_du_premier_joueur(self):
        """
        Méthode qui complète les étapes du tour du premier joueur.
        """

        # Trouver le joueur avec le domino le plus élevé.
        Partie.trouver_premier_joueur(self)

        # Afficher les informations sur le mouvement du premier joueur
        print("Le joueur {} joue en premier puisqu'il a le domino le plus fort {}"
              .format(Partie.trouver_premier_joueur(self)[0],
                      Partie.trouver_premier_joueur(self)[1]))

        # Placer ce domino sur le plateau de jeu (en utilisant la méthode appropriée)
        self.plateau.ajouter_a_gauche(Partie.trouver_premier_joueur(self)[1])

        # Retirer ce domino de la donne du joueur (en utilisant la méthode appropriée)
        self.donnes[Partie.trouver_premier_joueur(self)[0]-1].\
            jouer(Partie.trouver_premier_joueur(self)[1])

        # Passer au joueur suivant (en utilisant la méthode appropriée)
        Partie.passer_au_prochain_joueur(self)

    def determiner_si_domino_peut_etre_joue(self, domino):
        """
        Méthode qui détermine si un domino peut être joué sur le plateau de jeu.
        :param domino: (Domino) Domino dont on veut savoir s'il peut être posé à une des deux extrémités du plateau
        :return: (bool) True, si le domino peut être joué, False autrement.
        """
        un_domino = Domino(domino[0],domino[1])
        if (un_domino.__contains__(self.plateau[0][0]) or  un_domino.__contains__(self.plateau[-1][-1])):
            return True
        else:
            return False

    def determiner_si_joueur_joue_ou_passe(self):
        """
        Méthode qui détermine si le joueur courant peut jouer un domino ou s'il doit passer son tour.
        :return: (bool) True, si au moins un domino de la donne du joueur courant peut être joué sur le plateau. False,
        autrement.
        """
        # Dans la donne du joueur, y a-t-il un domino que le joueur peut joueur?
        for domino in self.donnes[self.tour - 1]:
            if (self.plateau.cote_gauche() == domino[0]) or (self.plateau.cote_droit() == domino[1]):
                return True
        return False


    def afficher_informations_debut_tour(self):
        """
        Méthode qui affiche les informations données à chaque début de tour: le numéro du joueur qui doit jouer, l'état
        du plateau de jeu, l'état des donnes de tous les joueurs (nombre de dominos en main) et la donne du joueur qui
        doit jouer.
        """
        # le numéro du joueur qui doit jouer
        print("c'est au tour du joueur {} ".format(self.tour))

        #l'état du plateau de jeu
        print("Plateau {} ".format(self.plateau))

        # l'état des donnes de tous les joueurs (nombre de dominos en main)
        for joueur in range(len(self.donnes)):
            print("le joueur {} a {} dominos en main ".format(joueur+1, len(self.donnes[joueur])))

        #la donne du joueur qui doit jouer
        print("Donne du jouer {} : {}".format(self.tour, self.donnes[self.tour - 1].__str__()))

    def demander_numero_domino_a_jouer(self):
        """
        Méthode qui demande le numéro du domino que le joueur veut jouer. En posant la question, le programme affiche la
        liste des dominos dans la donne du joueur. Le numéro est validé et le programme redemande un numéro de domino
        tant que le numéro fourni n'est pas valide.
        :return: (Domino) L'objet domino associé au numéro de domino choisi.
        """
        print("Quel domino voulez-vous jouer ?\n")
        for i in range(self.donnes[self.tour - 1].__len__()):
            print("{} : {}".format(i, self.donnes[self.tour - 1][i]))

        domino = []
        entree = True
        while entree:
            choix = input("Entre le nombre du domino (entre 0 et {})".format(len(self.donnes[self.tour]) - 1))
            if choix.isnumeric():
                if 0 <= int(choix) <= len(self.donnes[self.tour]) - 1:
                    entree = False
                    return self.donnes[self.tour - 1].__getitem__(int(choix))
                else:
                    print(" Entrée invalidée essayez à nouveau ")
                    entree = True
            else:
                print(" Entrée invalidée essayez à nouveau ")
                entree = True

    def jouer_a_gauche_ou_a_droite(self, domino_joue):
        """
        Méthode qui est invoquée lorsque le domino choisi par le joueur peut être joué à gauche ou à droite. On demande
        ce que veut le joueur et le domino est joué selon son choix. Ce choix doit être validé par le programme.
        :param domino_joue: (Domino) Le domino à jouer
        :return: bool
        """
        un_domino = Domino(domino_joue[0], domino_joue[1])
        autre_domino = Domino(self.plateau.cote_gauche(), self.plateau.cote_droit())
        if un_domino.__eq__(autre_domino):
            return True
        return False

    def jouer_a_gauche(self, domino_joue):
        """
        Méthode invoquée pour joueur un domino à gauche du plateau.
        :param domino_joue: (Domino) Le domino à jouer à gauche du plateau.
        """
        # Afficher l'information sur le mouvement du joueur.
        # Ajouter le domino sur le plateau.
        # Retirer le domino de la donne du joueur.
        # TODO: À compléter
        pass

    def jouer_a_droite(self, domino_joue):
        """
        Méthode invoquée pour joueur un domino à droite du plateau.
        :param domino_joue: (Domino) Le domino à jouer à droite du plateau.
        """
        # Afficher l'information sur le mouvement du joueur.
        # Ajouter le domino sur le plateau.
        # Retirer le domino de la donne du joueur.
        # TODO: À compléter
        pass

    def jouer_un_domino(self):
        """
        Méthode pour jouer un domino. Cette méthode demande au joueur le numéro du domino qu'il souhaite jouer. Elle
        vérifie ensuite si le domino peut être joué à gauche ou à droite du plateau. Si le domino peut être joué d'un
        seul côté, alors le domino est joué de ce côté-là. Si le domino peut être joué des deux côtés, alors on
        demande à l'utilateur le côté où il souhaite jouer le domino (en utilisant les méthodes appropriées).
        """
        domino_joue = Partie.demander_numero_domino_a_jouer(self)

        if Partie.jouer_a_gauche_ou_a_droite(self, domino_joue) == True:

            cote = input("Le domino {} peut être jouer à gauche ou à droite. Quel côté choisissez vous (g ou d) ?".
                         format(domino_joue))
            while True:
                if cote in "gdGD":
                    if cote == "g" or cote == "G":
                        Partie.jouer_a_gauche(self, domino_joue)
                        break
                    elif cote == "d" or cote == "D":
                        Partie.jouer_a_droite(self, domino_joue)
                        break
                else:
                    print("Devez entrer une lettre (g ou d)")
        else:
            un_domino = Domino(domino_joue[0], domino_joue[1])
            if un_domino.__contains__(self.plateau.cote_droit()):
                Partie.jouer_a_droite(self, domino_joue)
            elif un_domino.__contains__(self.plateau.cote_gauche()):
                Partie.jouer_a_gauche(self, domino_joue)

    def tour_du_prochain_joueur(self):
        """
        Méthode qui exécute les étapes de jeu pour le tour d'un joueur (à l'exception du premier tour qui a une
        méthode dédiée). Dans cette méthode: 1) on affiche les informations de début de tour, ensuite 2) on teste si
        le joueur courant peut jouer ou s'il doit passer son tour, #3) s'il peut jouer, on réinitialise l'attribut passe,
        le joueur joue un domino, et on vérifie s'il y a un gagnant, #4) s'il ne peut pas joueur, on fait passer son tour
        au joueur, finalement 4) on passe au prochain joueur (en utilisant la méthode appropriée).
        """
        #1) affiche les informations de début de tour
        Partie.afficher_informations_debut_tour(self)

        #2)(bool) le joueur courant peut jouer ou s'il doit passer son tour
        if Partie.determiner_si_joueur_joue_ou_passe(self) == True:
            #3) s'il peut jouer, on réinitialise l'attribut passe,le joueur joue un domino, eton vérifie s'il y a un gagnant
            self.passe = 0
            Partie.jouer_un_domino(self)
            if Partie.verifier_gagnant(self):
                self.gagnant = True
        #4)s'il ne peut pas joueur, on fait passer son tour au joueur, finalement
        else:
            self.passe += 1

        #5)on passe au prochain joueur


    def faire_passer_joueur(self):
        """
        Méthode qui contient les instructions à exécuter lorsqu'un joueur doit passer son tour. Cette méthode devrait
        afficher des informations et modifier l'attribut passe.
        """
        # TODO: À compléter
        pass

    def verifier_gagnant(self):
        """
        Méthode qui vérifie si le joueur courant est le gagnant (condition: il doit avoir vidé sa donne). Cette méthode
        modifie l'attibut gagnant si le joueur courant gagne la partie.
        """
        if self.donnes[self.tour - 1].__len__() == 0:
            self.gagnant = True
            return True


    def trouver_joueurs_avec_moins_de_dominos(self):
        """
        Méthode qui détermine le ou les joueurs qui ont la plus petite donne.
        :return: (list) Liste contenant les numéros des joueurs ayant le moins de dominos dans leur donne. Ce nombre
        peut varier entre 1 et len(self.donnes)
        """
        # TODO: À compléter
        pass

    def afficher_message_egalite(self, indices):
        """
        Méthode qui affiche un message en cas d'égalité en fin de partie. Ce message doit indiquer quels sont les joueurs
        qui ont le moins de dominos dans leur donne.
        :param indices: (list) Liste qui contient les numéros des joueurs ayant le moins de dominos dans leur donne.
        """
        # TODO: À compléter
        pass

    def afficher_message_victoire(self):
        """
        Méthode qui affiche le message de victoire. Il informe l'usager de l'identité du joueur gagnant.
        """
        # TODO: À compléter
        pass

    def jouer(self):
        """
        Méthode principale de la classe qui spécifie le déroulement d'une partie. Les étapes sont: 1) affichage des
        instructions, 2) premier tour de jeu, 3) boucle pour les tours suivants, cette boucle vérifie les conditions de
        fin de partie, 4) affichages de fin de partie (état des donnes, message en cas de victoire ou d'égalité)
        """

        #1) affichage des instructions
        Partie.afficher_instructions()

        #2) premier tour de jeu
        Partie.tour_du_premier_joueur(self)

        #3) boucle pour les tours suivants, cette boucle vérifie les conditions de fin de partie
        Partie.tour_du_prochain_joueur(self)



        #4) affichages de fin de partie (état des donnes, message en cas de victoire ou d'égalité)

          #      afficher_etat_donnes(self)
          #     afficher_message_egalite(self, indices)
          #      afficher_message_victoire

