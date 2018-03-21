"""
Module principal du package pydomino. C'est ce module que nous allons exécuter pour démarrer votre jeu.
"""

from pydomino.partie import Partie
from pydomino.partie_avec_pioche import PartieAvecPioche


if __name__ == '__main__':
    """
    Point d'entrée de votre programme pydomino. Dans cette fonction, il faut d'abord demander quel type de partie de
    dominos l'utilisateur veut jouer. L'entrée de l'utilisateur doit être validée. Ensuite, le programme demande à
    l'utilisateur à combien de joueur il veut jouer une partie. Un objet de la classe Partie ou de la classe 
    PartieAvecPioche est ensuite instancié. Finalement, la partie est démarrée en appelant la méthode jouer().
    """
    print("Jouons une partie de pydomino!\n")
    # TODO: À compléter
    # choix du type de partie
    entree = True
    while entree:
        print("Voulez-vous jouer ?")
        print("\t1. une partie de dominos sans pioche?")
        print("\t2. une partie de dominos avec pioche?")
        choix = input("Entre une chiffre (entre 1 ou 2)")
        if  choix.isnumeric():
            if 1 <= int(choix) <= 2:
                entree = False
            else:
                print("_____________  E r r e u r ______________")
                print(" Devez entre une chiffre  (entre 1 ou 2)  ")
                entree = True
        else:
            print("_____________  E r r e u r ______________")
            print("| Devez entre une chiffre  (entre 1 ou 2) |")


    # choix du nombre de joueurs
    # instanciation d'un objet partie
    # démarrage de la partie


    input('Appuyer sur ENTER pour quitter.')
