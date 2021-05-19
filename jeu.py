from __future__ import annotations
from creature import Creature
import random
from typing import Tuple
from case import Case

CREATURE_NAMES = ["Pikachu", "Reptincel", "Carapuce", "Bulbizarre"]

class Jeu():
    """Un jeu de créature sur une grille
    """
    def __init__(self, num_rows: int = 4, num_cols: int = 4, nb_creatures: int = 2) -> None:
        """Construit un jeu d'une taille num_rows x num_cols avec un nombre de créatures

        Args:
            num_rows (int, optional): Le nombre de lignes sur la grille du jeu. Defaults to 4.
            num_cols (int, optional): Le nombre de colonnes sur la grille du jeu. Defaults to 4.
            nb_creatures (int, optional): Le nombre de créatures dans le jeu. Defaults to 2.
        """
        self.__num_cols = num_cols
        self.__num_rows = num_rows
        self.__nb_creatures = nb_creatures
        self.__tour = 0
        self.current_c_index = 0
        self.winner = None
        self.listeDesCases = self.generateCases(num_rows, num_cols)
        self.listeDesCreatures: list[Creature] = self.generateCreatures()
    
    @property
    def current_creature(self) -> Creature:
        """Retourne la créature active pour ce tour

        Returns:
            Creature: la créature active
        """
        return self.listeDesCreatures[self.current_c_index]

    @property
    def taille(self) -> Tuple[int, int]:
        """Retourne la taille de la grille de jeu

        Returns:
            Tuple[int, int]: Un tuple (x, y)
        """
        return self.__num_rows, self.__num_cols
    
    @property
    def tour(self) -> int:
        """Retourne le tour actuel 

        Returns:
            int: tour actif
        """
        return self.__tour

    def generateCases(self, num_rows: int, num_cols: int) -> dict[Tuple[int, int], Case]:
        """Génère un dictionnaire de cases selon une taille défini

        Args:
            num_rows (int): Nombre de ligne dans la grille du jeu
            num_cols (int): Nombre de colonnes dans la grille du jeu

        Returns:
            dict[Tuple[int, int], Case]: un dictionnaire de case avec un tuple (x, y) comme clé
        """
        liste_cases: dict[Tuple[int, int], Case] = {}
        for i in range(num_rows):
            for j in range(num_cols):
                liste_cases[(i, j)] = Case(i, j)
        return liste_cases
    
    def generateCreatures(self) -> list[Creature]:
        """Génère une liste de créatures selon le nombre défini dans la classe

        Returns:
            list[Creature]: une liste de créature
        """
        liste_creatures = []
        for i in range(self.__nb_creatures):
            name = random.choice(CREATURE_NAMES)
            CREATURE_NAMES.remove(name)
            liste_creatures.append(Creature(name, self.randomPos()))
        return liste_creatures

    def randomPos(self) -> Case:
        """Retourne une case aléatoire du jeu

        Returns:
            Case: une case aléatoire
        """
        return random.choice(list(self.listeDesCases.values()))

    def estOccupee(self, case: Case):
        """Retourne un boolean sur la présence d'une creature sur une case

        Args:
            case (Case): la case pour laquelle l'on veut savoir si une creature l'occupe

        Returns:
            Boolean: True si une creature occupe la case, False autrement. 
        """
        for creature in self.listeDesCreatures:
            if creature.position.x == case.x and creature.position.y == case.y:
                return True
        return False 


        ## Méthode pour Check l'occupation de la case          

    def deplacer(self, case):
        """Méthode qui déplace la créature de case. 
        Affichage du nom du vainqueur si la case était occupée

        Args:
            case ([Case]): la case vers laquelle doit se déplacer la créature
        """
        if not self.estOccupee(case):
            # pas de creature sur la nouvelle case
            # incrément du tour 
            self.__tour += 1
            # on deplace la creature
            self.current_creature.position = case
            print(f"{self.current_creature.nom} se déplace vers ({self.current_creature.position})")
            # on change la creature
            self.current_c_index = (self.current_c_index + 1)%len(self.listeDesCreatures)
        else:
            # creature presente sur la case
            # on deplace la creature
            self.current_creature.position = case
            print(f"{self.current_creature.nom} se déplace vers ({self.current_creature.position})")
            # on met la creature gagnante
            self.winner = self.current_creature
            print("Le gagnant est :", self.winner.nom)  
        
    def __str__(self):
        output_game = "Taille du plateau : " + str(self.__num_cols) + "x" + str(self.__num_rows) + "\n"
        output_game += "Le nombre de joueur est de : " + str(self.__nb_creatures)
        output_game += "Les noms des joueur sont : " + str(self.current_creature.nom)
        return output_game


        
game = Jeu()
while game.winner == None:
    game.deplacer(game.current_creature.choisirCible(game))
print(f"Jeu terminé avec {game.tour} tours")
