import random

class Creatures():
   def __init__(self, nom, position = None):
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
      for case in self.case.adjacentes(jeu):
         if jeu.estOccupee(case):
            return case
      random.choice(self.case.adjacentes(jeu))



        
    
## coucou marie

## Code a fond et je ne te unfollow
