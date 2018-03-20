"""Lorsqu'un dossier contient un module __init__.py, c'est que nous le considérons comme
un "package", qui est une collection de modules regroupés dans un même projet.

Ce module spécial permet de faire:
from pydomino.partie import ...

Aucun code n'est nécessaire dans ce module spécial, sa présence est suffisante.
Si vous créez un package python dans Pycharm, vous obtiendrez automatiquement ce fichier.

"""
from pydomino.plateau import Plateau
from pydomino.domino import Domino
from pydomino.partie import Partie
from pydomino.donne import Donne
from pydomino.partie_avec_pioche import PartieAvecPioche
from pydomino.pioche import Pioche
