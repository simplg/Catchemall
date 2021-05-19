import random

class Creature():
   """Une créature du jeu
   """
   def __init__(self, nom, position = None):
      """Construit une créature du jeu avec un nom donné et une position

      Args:
          nom (str): Le nom de la créature
          position (Case, optional): La case sur laquelle la créature est positionnée. Defaults to None.
      """
      self.nom = nom
      self.position = position

   def _get_nom(self):
      return self._nom

   def _set_nom(self,nom):
      self._nom = nom
   nom = property(_get_nom,_set_nom)

   def _get_position(self):
      return self._position

   def _set_position(self,position):
      self._position = position
   position = property(_get_position,_set_position)

   def __str__(self):
      return str(self.nom,self.position)   

   def choisirCible(self, jeu):
      """Retourne une case parmis les cases adjacentes de la créature. Si une case adjacente est 
      occupée, elle la retourne. Sinon elle retourne aléatoirement parmis celles aléatoires.

      Args:
          jeu (Jeu): L'instance du jeu auquel appartient la créature

      Returns:
          Case: La case cible que doit viser la créature
      """
      for case in self.position.adjacentes(jeu):
         if jeu.estOccupee(case):
            return case
      return random.choice(self.position.adjacentes(jeu))



        
    
## coucou marie

## Code a fond et je ne te unfollow
