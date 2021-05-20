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
        x_max, y_max = jeu.taille
        delta = range(-1, 2)
        x, y = [], []
        for i in delta:
            x_cpt = self.x + i
            if x_cpt < 0:
                x.append(x_max + x_cpt)
            elif x_cpt > x_max:
                x.append(0 + (x_cpt - x_max))
            else:
                x.append(x_cpt)
            y_cpt = self.y + i
            if y_cpt < 0:
                y.append(y_max + y_cpt)
            elif y_cpt > y_max:
                y.append(0 + (y_cpt - y_max))
            else:
                y.append(y_cpt)
        casesAdjacentes = list(filter(lambda case: case.x in x and case.y in y, listeCases))
        if self in casesAdjacentes:
            casesAdjacentes.remove(self)
        return casesAdjacentes

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"