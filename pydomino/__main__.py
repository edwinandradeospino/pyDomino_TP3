"""
Module principal du package pydomino. C'est ce module que nous allons exécuter pour démarrer votre jeu.
"""

from pydomino.partie import *
from pydomino.partie_avec_pioche import *


def type_de_partie():
    """
        Méthode pour
        :param
        :return:
    """
    entree = True
    while entree:
        print("Voulez-vous jouer ?")
        print("\t1. une partie de dominos sans pioche?")
        print("\t2. une partie de dominos avec pioche?")
        choix = input("Entre une chiffre (entre 1 ou 2)")

        if choix.isnumeric():
            if 1 <= int(choix) <= 2:
                entree = False
                return int(choix)
            else:
                print("_____________  E r r e u r ______________")
                print(" Devez entre une chiffre  (entre 1 ou 2)  ")
                entree = True
        else:
            print("_____________  E r r e u r ______________")
            print("| Devez entre une chiffre (entre 1 ou 2) |")

def nombre_de_parties():
    """
        Méthode pour
        :param
        :return:
    """
    nom_joueurs_in = True
    while nom_joueurs_in:
        nombre_joueurs = input("À combien de joueurs voulez-vous jouer une partie de domino (entre 2 et 4)? ")
        if nombre_joueurs.isnumeric():
            if 2 <= int(nombre_joueurs) <= 4:
                if int(nombre_joueurs) == 2:
                    nom_joueurs_in = False
                    return int(nombre_joueurs)
                if 3 <= int(nombre_joueurs) <= 4:
                    nom_joueurs_in = False
                    return int(nombre_joueurs)
            else:
                print("_____________  E r r e u r ______________")
                print(" Devez entre une chiffre  (entre 2 et 4)  ")
                nom_joueurs_in = True
        else:
            print("_____________  E r r e u r ______________")
            print("| Devez entre une chiffre  (entre 2 ou 4) |")

def cree_joueurs_partie(nombre_joueurs, list_donne_joueurs):
    """
        Méthode pour cree_joueurs
        :param
        :return:
    """
    if nombre_joueurs == 2:
        joueur1 = Partie(Plateau(), Donne(list_donne_joueurs[0]))
        joueur2 = Partie(Plateau(), Donne(list_donne_joueurs[1]))
        return [joueur1, joueur2]
    if nombre_joueurs == 3:
        joueur1 = Partie(Plateau(), Donne(list_donne_joueurs[0]))
        joueur2 = Partie(Plateau(), Donne(list_donne_joueurs[1]))
        joueur3 = Partie(Plateau(), Donne(list_donne_joueurs[2]))
        return [joueur1, joueur2, joueur3]
    if nombre_joueurs == 4:
        joueur1 = Partie(Plateau(), Donne(list_donne_joueurs[0]))
        joueur2 = Partie(Plateau(), Donne(list_donne_joueurs[1]))
        joueur3 = Partie(Plateau(), Donne(list_donne_joueurs[2]))
        joueur4 = Partie(Plateau(), Donne(list_donne_joueurs[3]))
        return [joueur1, joueur2, joueur3, joueur4]


def cree_joueurs_partie_avec_pioche(nombre_joueurs, list_donne_joueurs):
    """
        Méthode pour cree_joueurs
        :param
        :return:
    """
    if nombre_joueurs == 2:
        pioche = list_donne_joueurs[2]
        joueur1 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[0]),pioche)
        joueur2 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[1]),pioche)
        return [joueur1, joueur2, pioche]
    if nombre_joueurs == 3:
        pioche = list_donne_joueurs[3]
        joueur1 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[0]),pioche)
        joueur2 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[1]),pioche)
        joueur3 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[2]),pioche)
        return [joueur1, joueur2, joueur3, pioche]
    if nombre_joueurs == 4:
        pioche = list_donne_joueurs[4]
        joueur1 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[0]),pioche)
        joueur2 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[1]),pioche)
        joueur3 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[2]),pioche)
        joueur4 = PartieAvecPioche(Plateau(), Donne(list_donne_joueurs[3]),pioche)
        return [joueur1, joueur2, joueur3, joueur4, pioche]

def cree_objets():
    if type_de_partie() == 1:
        list_donne_joueurs = distribuer_dominos(nombre_de_parties())
        list_joueurs = cree_joueurs_partie(nombre_de_parties(), list_donne_joueurs)
        return list_joueurs
    if type_de_partie() == 2:
        list_donne_joueurs = distribuer_dominos_avec_pioche(nombre_de_parties())
        list_joueurs = cree_joueurs_partie_avec_pioche(nombre_de_parties(), list_donne_joueurs)
        return list_joueurs

if __name__ == '__main__':
    """
    Point d'entrée de votre programme pydomino. Dans cette fonction, il faut d'abord demander quel type de partie de
    dominos l'utilisateur veut jouer. L'entrée de l'utilisateur doit être validée. Ensuite, le programme demande à
    l'utilisateur à combien de joueur il veut jouer une partie. Un objet de la classe Partie ou de la classe 
    PartieAvecPioche est ensuite instancié. Finalement, la partie est démarrée en appelant la méthode jouer().
    """
    print("Jouons une partie de pydomino!\n")

    # choix du type de partie
    type_partie = type_de_partie()

    # combien de joueur il veut jouer une partie
    nombre_joueurs = nombre_de_parties()

    # créer les donnes des joueurs et instancier les objets
    list_objets_joueur = cree_objets(type_partie, nombre_joueurs)

    # démarrage de la partie
    Partie.jouer()

    input('Appuyer sur ENTER pour quitter.')
