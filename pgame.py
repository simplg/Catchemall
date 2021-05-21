import random
from typing import Tuple
from jeu import Jeu
import sys, pygame


class WindowSize():
    width: int = 1080
    height: int = 720

class Game2D():
    def __init__(self, jeu: Jeu, window_size: WindowSize = WindowSize(), grid_colors = [(0, 0, 0), (255, 255, 255)]) -> None:
        self.__jeu = jeu
        self.__window_size = window_size
        self.__sprites = {}
        self.__grid_colors = grid_colors
        self.__screen = pygame.display.set_mode([window_size.width, window_size.height])
        self.__winner_sprite = None
        self.generateCreatures()

    @property
    def grid_size(self):
        return self.__jeu.taille
    
    @property
    def cell_size(self) -> Tuple[int, int]:
        x_max, y_max = self.grid_size
        return (int(self.__window_size.width/x_max), int(self.__window_size.height/y_max))

    def redraw(self):
        self.__screen.fill(grey)
        self.createGrid()
        for creature in self.__jeu.playing:
            sprite = self.__sprites[creature.nom]
            self.__screen.blit(sprite['image'], sprite['rect'])

    def createGrid(self):
        x_max, y_max = self.grid_size
        wsize, hsize = self.cell_size
        for i in range(x_max):
            for j in range(y_max):
                ind = (i + j) % 2
                start_x, start_y = wsize * i, hsize * j
                pygame.draw.rect(self.__screen, self.__grid_colors[ind], [start_x, start_y, wsize, hsize])

    def resizeToCell(self, obj):
        height = self.__window_size.height
        _, y_max = self.grid_size
        return pygame.transform.scale(obj, (int(height/y_max), int(height/y_max)))

    def move(self, sprite, to):
        wsize, hsize = self.cell_size
        to_x, to_y = to
        sprite.x = to_x * wsize
        sprite.y = to_y * hsize
        self.redraw()
    
    def generateCreatures(self):
        wsize, hsize = self.cell_size
        for creature in self.__jeu.listeDesCreatures:
            sprite = pygame.image.load(f"{creature.nom.lower()}.png").convert_alpha()
            sprite = self.resizeToCell(sprite)
            spriterect = sprite.get_rect()
            spriterect.x = creature.position.x * wsize
            spriterect.y = creature.position.y * hsize
            self.__sprites[creature.nom] = { 'image': sprite, 'rect': spriterect}
    
    def next_frame(self):
        if self.__jeu.winner == None:
            prev_x, prev_y = self.__jeu.current_creature.position.x, self.__jeu.current_creature.position.y
            creature = self.__jeu.deplacer(self.__jeu.current_creature.choisirCible(self.__jeu))
            self.move(self.__sprites[creature.nom]['rect'], (creature.position.x,  creature.position.y))
            pygame.display.flip()
            pygame.time.delay(400)
        else:
            if not self.__winner_sprite:
                red_audio.stop()
                win_audio = pygame.mixer.Sound("win.mp3")
                win_audio.play()
                self.__winner_sprite = pygame.image.load(f"{self.__jeu.winner.nom.lower()}.png").convert_alpha()
                self.__winner_sprite = pygame.transform.smoothscale(self.__winner_sprite, (int(self.__window_size.height/2), int(self.__window_size.width/2)))

            self.__screen.fill((255, 0, 0))
            rect = self.__winner_sprite.get_rect()
            rect.centerx = int(self.__window_size.width/2)
            rect.centery = int(self.__window_size.height/2 + random.randint(-5, 5))
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(f'{self.__jeu.winner.nom} a gagné !', False, (255, 255, 255))
            self.__screen.blit(self.__winner_sprite, rect)
            self.__screen.blit(textsurface,(self.__window_size.width/2,0))
            pygame.display.flip()
            pygame.time.delay(100)


pygame.init()
pygame.font.init()

game2d = Game2D(Jeu(8, 8, 2))
grey = 150, 150, 150

red_audio = pygame.mixer.Sound("red-vs-gold-theme.mp3")
red_audio.play()
is_win_playing = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    game2d.next_frame()