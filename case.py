class Case ():
    # x:position_lignes
    # y:position_colonnes

    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y

    def adjacentes(self, jeu):

        listeCases=list(jeu.listeDesCases.values())
        num_rows, num_cols = jeu.taille
        champ_x=[indice for indice in range(self.x-1,self.x+2) if 0<=indice<=num_rows]
        champ_y=[indice for indice in range(self.x-1,self.x+2) if 0<=indice<=num_cols]
        
        tri=lambda c_test: (c_test.x in champ_x) & (c_test.y in champ_y)
        casesAdjacents=[case_temp for case_temp in listeCases if tri(case_temp)]
        if self in casesAdjacents:
            casesAdjacents.remove(self)
        return casesAdjacents

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"