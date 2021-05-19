from __future__ import annotations
from creatures import Creatures
import random
from typing import Any, Tuple
from case import Case

CREATURE_NAMES = ["Pikachu", "Reptincel", "Carapuce", "Bulbizarre"]

class Jeu():
    def __init__(self, num_rows = 4, num_cols = 4, nb_creatures: int = 2) -> None:
        self.__num_cols = num_cols
        self.__num_rows = num_rows
        self.__nb_creatures = nb_creatures
        self.__tour = 0
        self.current_c_index = 0
        self.winner = None
        self.listeDesCases = self.generateCases(num_rows, num_cols)
        self.listeDesCreatures: list[Creatures] = self.generateCreatures()
    
    @property
    def current_creature(self):
        return self.listeDesCreatures[self.current_c_index]

    @property
    def taille(self):
        return self.__num_rows, self.__num_cols

    def generateCases(self, num_rows: int, num_cols: int) -> dict(Tuple(int, int), Case):
        liste_cases: dict(Tuple(int, int), Case) = {}
        for i in range(num_rows):
            for j in range(num_cols):
                liste_cases[(i, j)] = Case(i, j)
        return liste_cases
    
    def generateCreatures(self) -> list[Creatures]:
        liste_creatures = []
        for i in range(self.__nb_creatures):
            liste_creatures.append(Creatures(random.choice(CREATURE_NAMES), self.randomPos()))
        return liste_creatures

    def randomPos(self):
        return random.choice(list(self.listeDesCases.values()))

    def estOccupee(self, case):
        for creature in self.listeDesCreatures:
            if creature.position == case:
                return True
        return False 


        ## Méthode pour Check l'occupation de la case          

    def deplacer(self,case):
        ## Méthode qui déplace la créature de case 
        ## Affichage nom du vainqueur si la case etais occuper
        ## Avec incrément du tour 
        if not self.estOccupee(case):
            self.__tour += 1
            print(f"{self.current_creature.nom} se déplace vers ({self.current_creature.position})")
            self.current_creature.position = case
            self.current_c_index = (self.current_c_index + 1)%len(self.listeDesCreatures)

        else:
            print(f"{self.current_creature.nom} se déplace vers ({self.current_creature.position})")
            self.current_creature.position = case
            self.winner = self.current_creature
            print("Le gagnant est :",self.winner.nom)  
        
    def __str__(self):
        
        output_game = "Taille du plateau : " + str(self.__num_cols) + "x" + str(self.__num_rows) + "\n"
        output_game += "Le nombre de joueur est de : " + str(self.__nb_creatures)
        output_game += "Les noms des joueur sont : " + str(self.current_creature.name)
        return output_game


        
game = Jeu()
while game.winner == None:
    game.deplacer(random.choice(game.current_creature.position.adjacentes(game)))
print("Game finish")
