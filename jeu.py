from __future__ import annotations
from behavior import Behavior, RandomBehavior
from creature import Creature
import random
from typing import Tuple, Union
from case import Case
from terrain import BasicTerrain, Terrain

CREATURE_NAMES = ["Pikachu", "Salameche", "Carapuce", "Bulbizar"]

class Jeu():
    """Un jeu de créature sur une grille
    """
    def __init__(self, nb_creatures: int = 2, terrain: Terrain = BasicTerrain(4, 4), behavior: Union[Behavior, list[Behavior]] = RandomBehavior()) -> None:
        """Construit un jeu d'une taille num_rows x num_cols avec un nombre de créatures

        Args:
            nb_creatures (int, optional): Le nombre de créatures dans le jeu. Defaults to 2.
            terrain (Terrain, optional): La map du jeu. Defaults to BasicTerrain(4, 4).
            behavior (Behavior, optional): Le comportement de déplacement de chaque créatures.
        """
        self.__terrain = terrain
        self.__tour = 0
        self.listeDesCases = self.generateCases()
        self.listeDesCreatures: list[Creature] = self.generateCreatures(nb_creatures, behavior)
        self.current_c_index = 0
    
    @property
    def nb_creatures(self):
        return len(self.listeDesCreatures)

    @property
    def winner(self):
        return self.playing[0] if len(self.playing) == 1 else None
    
    @property
    def current_creature(self) -> Creature:
        """Retourne la créature active pour ce tour

        Returns:
            Creature: la créature active
        """
        return self.playing[self.current_c_index]

    @property
    def taille(self) -> Tuple[int, int]:
        """Retourne la taille de la grille de jeu

        Returns:
            Tuple[int, int]: Un tuple (x, y)
        """
        return self.__terrain.size
    
    @property
    def tour(self) -> int:
        """Retourne le tour actuel 

        Returns:
            int: tour actif
        """
        return self.__tour
    
    @property
    def listeDesCreatures(self):
        return self.__listeDesCreatures
    
    @listeDesCreatures.setter
    def listeDesCreatures(self, creatures: list[Creature]):
        self.__listeDesCreatures = creatures
        self.playing = self.listeDesCreatures.copy()


    def generateCases(self) -> dict[Tuple[int, int], Case]:
        """Génère un dictionnaire de cases selon une taille défini

        Args:
            num_rows (int): Nombre de ligne dans la grille du jeu
            num_cols (int): Nombre de colonnes dans la grille du jeu

        Returns:
            dict[Tuple[int, int], Case]: un dictionnaire de case avec un tuple (x, y) comme clé
        """
        return self.__terrain.generateCases()
    
    def generateCreatures(self, nb_creatures: int = 2, behavior: Union[Behavior, list[Behavior]] = RandomBehavior()) -> list[Creature]:
        """Génère une liste de créatures selon le nombre défini dans la classe
        
        Args:
            nb_creatures (int, optional): Le nombre de créatures dans le jeu. Defaults to 2.
            behavior (Behavior, optional): Le comportement de déplacement de chaque créatures.

        Returns:
            list[Creature]: une liste de créature
        """
        liste_creatures = []
        for i in range(nb_creatures):
            name = random.choice(CREATURE_NAMES)
            CREATURE_NAMES.remove(name)
            creature = Creature(name, self.randomPos())
            b = behavior
            if isinstance(b, list):
                b = b[i%len(b)]
            creature.behavior = b
            liste_creatures.append(creature)
        return liste_creatures

    def randomPos(self) -> Case:
        """Retourne une case aléatoire du jeu

        Returns:
            Case: une case aléatoire
        """
        return random.choice(list(self.listeDesCases.values()))

    def estOccupee(self, case: Case) -> Creature:
        """Retourne un boolean sur la présence d'une creature sur une case

        Args:
            case (Case): la case pour laquelle l'on veut savoir si une creature l'occupe

        Returns:
            Creature: une creature qui occupe la case, None autrement. 
        """
        for creature in self.playing:
            if creature.position.x == case.x and creature.position.y == case.y:
                return creature
        return None 

        ## Méthode pour Check l'occupation de la case          

    def deplacer(self, case) -> Creature:
        """Méthode qui déplace la créature de case. 
        Affichage du nom du vainqueur si la case était occupée

        Args:
            case ([Case]): la case vers laquelle doit se déplacer la créature
        """
        creature = self.estOccupee(case)
        current_creature = self.current_creature
        if creature is None:
            # pas de creature sur la nouvelle case
            # incrément du tour 
            self.__tour += 1
            # on deplace la creature
            current_creature.position = case
            print(f"{current_creature.nom} se déplace vers ({current_creature.position})")
            # on change la creature
        else:
            # creature presente sur la case
            # on deplace la creature
            current_creature.position = case
            print(f"{current_creature.nom} se déplace vers ({current_creature.position})")
            print(f"{current_creature.nom} tue ({creature.nom})")
            self.playing.remove(creature)
            if len(self.playing) == 1:
                # on met la creature gagnante
                print("Le gagnant est :", self.winner.nom)  
        self.current_c_index = (self.playing.index(current_creature) + 1)%len(self.playing)
        return current_creature
        
    def __str__(self):
        output_game = "Taille du plateau : " + str(self.__num_cols) + "x" + str(self.__num_rows) + "\n"
        output_game += "Le nombre de joueur est de : " + str(self.__nb_creatures)
        output_game += "Les noms des joueur sont : " + str(self.current_creature.nom)
        return output_game


"""
game = Jeu(8, 8, 2)
while game.winner == None:
    game.deplacer(game.current_creature.choisirCible(game))
print(f"Jeu terminé avec {game.tour} tours")
"""
