from __future__ import annotations
import abc
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from case import Case
    from jeu import Jeu
    from creature import Creature

class Behavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def choisirCible(self, creature: Creature, jeu: Jeu) -> Case:
        return None
    
class RandomBehavior(Behavior):
    def choisirCible(self, creature: Creature, jeu: Jeu) -> Case:
        caseAdjacentes = creature.position.adjacentes(jeu)
        for case in caseAdjacentes:
         if jeu.estOccupee(case):
            return case
        return random.choice(caseAdjacentes)