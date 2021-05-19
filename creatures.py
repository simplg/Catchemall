class Creatures():
     def __init__(self, nom, position):
        self.nom =nom.upper()
        self.position =position()

    def _get_nom(self):
        print(self._nom)
        return self._nom
    
    def _set_nom(self,nom):
        self._nom = nom
    nom = property(_get_nom,_set_nom)
        
    def _get_posotion(self):
        print(self._position)
        return self.position
    
    def _set_prenom(self,position):
        self._position = position
    position = property(_get_position,_set_position)
        
    