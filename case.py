from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from jeu import Jeu

class Case ():
    """ Une case du jeu video
    """
    def __init__(self, x: int, y: int, is_active: bool = True):
        """Construit une classe Case à une position (x, y)

        Args:
            x (int): la position sur l'axe horizontal x
            y (int): la position sur l'axe vertical y
        """
        self.x = x
        self.y = y
        self.__active = is_active
    
    @property
    def active(self):
        return self.__active

    def adjacentes(self, jeu: Jeu):
        """Retourne les cases adjacentes à la case

        Args:
            jeu (Jeu): une instance du jeu auquelle la case appartient

        Returns:
            list[Case]: liste des cases adjacentes
        """
        x_max, y_max = jeu.taille
        delta = range(-1, 2)
        # utilisation d'un modulo comme conseillé par Valerio
        casesAdjacentes = [ jeu.listeDesCases[((self.x + i)%x_max, (self.y + j)%y_max)] for i in delta for j in delta if jeu.listeDesCases[((self.x + i)%x_max, (self.y + j)%y_max)].active ]
        # normalement la case courante se retrouve dans la liste, on peut la supprimer si on veut forcer un déplacement
        if self in casesAdjacentes:
            casesAdjacentes.remove(self)
        return casesAdjacentes

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"