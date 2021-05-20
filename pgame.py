from jeu import Jeu
import sys, pygame, math

# window
size = width, height = 1080, 720
jeu = Jeu(8, 8, 2)
x_max, y_max = jeu.taille
wsize, hsize = int(width/x_max), int(height/y_max)
sprites = {}

def redraw(screen, jeu):
    screen.fill(grey)
    createGrid(screen)
    for creature in jeu.playing:
        sprite = sprites[creature.nom]
        screen.blit(sprite['image'], sprite['rect'])

def resizeToCell(obj):
    return pygame.transform.scale(obj, (int(height/y_max), int(height/y_max)))

def createGrid(screen):
    grid_colors = [(0, 0, 0), (255, 255, 255)]
    for i in range(x_max):
        for j in range(y_max):
            ind = (i + j) % 2
            start_x, start_y = wsize * i, hsize * j
            pygame.draw.rect(screen, grid_colors[ind], [start_x, start_y, wsize, hsize])
        
def move(screen, sprite, to, jeu):
    to_x, to_y = to
    sprite.x = to_x * wsize
    sprite.y = to_y * hsize
    redraw(screen, jeu)

pygame.init()
pygame.font.init()

speed = [2, 2]
grey = 150, 150, 150

screen = pygame.display.set_mode(size)

for creature in jeu.listeDesCreatures:
    sprite = pygame.image.load(f"{creature.nom.lower()}.png").convert_alpha()
    sprite = resizeToCell(sprite)
    spriterect = sprite.get_rect()
    spriterect.x = creature.position.x * wsize
    spriterect.y = creature.position.y * hsize
    sprites[creature.nom] = { 'image': sprite, 'rect': spriterect}

while jeu.winner == None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    prev_x, prev_y = jeu.current_creature.position.x, jeu.current_creature.position.y
    creature = jeu.deplacer(jeu.current_creature.choisirCible(jeu))
    move(screen, sprites[creature.nom]['rect'], (creature.position.x,  creature.position.y), jeu)
    pygame.display.flip()
    pygame.time.delay(200)

for i in range(1000):
    redraw(screen, jeu)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(f'{jeu.winner.nom} a gagné !', False, (255, 0, 0))
    screen.blit(textsurface,(0,0))
    pygame.display.flip()
    pygame.time.delay(100)
