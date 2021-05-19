class Case ():
    """ Une case du jeu video
    """
    def __init__(self, x: int, y: int):
        """Construit une classe Case à une position (x, y)

        Args:
            x (int): la position sur l'axe horizontal x
            y (int): la position sur l'axe vertical y
        """
        self.x = x
        self.y = y

    def adjacentes(self, jeu):
        """Retourne les cases adjacentes à la case

        Args:
            jeu (Jeu): une instance du jeu auquelle la case appartient

        Returns:
            list[Case]: liste des cases adjacentes
        """
        listeCases = list(jeu.listeDesCases.values())
        num_rows, num_cols = jeu.taille
        champ_x = [indice for indice in range(self.x-1,self.x+2) if 0<=indice<=num_rows]
        champ_y = [indice for indice in range(self.x-1,self.x+2) if 0<=indice<=num_cols]
        
        tri = lambda c_test: (c_test.x in champ_x) & (c_test.y in champ_y)
        casesAdjacentes = [case_temp for case_temp in listeCases if tri(case_temp)]
        if self in casesAdjacentes:
            casesAdjacentes.remove(self)
        return casesAdjacentes

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"