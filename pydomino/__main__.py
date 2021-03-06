"""
Module principal du package pydomino. C'est ce module que nous allons exécuter pour démarrer votre jeu.
"""

from pydomino.partie import *
from pydomino.partie_avec_pioche import *
from pydomino.donne import *



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

def cree_donnes(type_partie, nombre_joueurs):
    """
     Méthode pour
     :param
     :return:
    """
    if type_partie == 1:
        une_partie = Partie.nouvelle_partie(nombre_joueurs)
        return une_partie

    if type_partie == 2:
        une_partie = PartieAvecPioche.nouvelle_partie(nombre_joueurs)
        return une_partie


if __name__ == '__main__':
    """
    Point d'entrée de votre programme pydomino. Dans cette fonction, il faut d'abord demander quel type de partie de
    dominos l'utilisateur veut jouer. L'entrée de l'utilisateur doit être validée. Ensuite, le programme demande à
    l'utilisateur à combien de joueur il veut jouer une partie. Un objet de la classe Partie ou de la classe 
    PartieAvecPioche est ensuite instancié. Finalement, la partie est démarrée en appelant la méthode jouer().
    """


    while True:
        print("Jouons une partie de pydomino!\n")
        # choix du type de partie
        type_partie = type_de_partie()

        # combien de joueur il veut jouer une partie
        nombre_joueurs = nombre_de_parties()

        # créer les donnes des joueurs et instancier les objets
        une_parties = cree_donnes(type_partie, nombre_joueurs)
        # démarrage de la partie
        une_parties.jouer()

        nouvelle = input("Voulez vous jouer une nouvelle partie (y/n) ?")
        if nouvelle in "yY":
            pass
        else:
            input('Appuyer sur ENTER pour quitter.')
            break


