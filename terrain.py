from __future__ import annotations
import abc
from typing import TYPE_CHECKING, Tuple
from case import Case

class Terrain(metaclass=abc.ABCMeta):
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
    
    @property
    def size(self):
        return (self.__x, self.__y)
    
    @abc.abstractmethod
    def generateCases(self) -> dict[Tuple[int, int], Case]:
        return None

class BasicTerrain(Terrain):
    def generateCases(self) -> dict[Tuple[int, int], Case]:
        num_rows, num_cols = self.size
        liste_cases: dict[Tuple[int, int], Case] = {}
        for i in range(num_rows):
            for j in range(num_cols):
                liste_cases[(i, j)] = Case(i, j)
        return liste_cases