import pygame
from classes.player import Player
from classes.invader import Invader
from classes.colors import Colors

# initialize game engine
pygame.init()
TILE_SIZE = 16
MAP_WIDTH = 24
MAP_HEIGHT = 18

# set screen width/height based on MAP_WIDTH/HEIGHT and TILE_SIZE 
SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE
SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(SIZE)

# set caption
pygame.display.set_caption('Space Invaders')

# creating instance of Color class, which contains colors
colors = Colors()

# constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# a dictionary linking resources to colors
RESOURCE_COLORS = {
    DIRT: colors.brown,
    GRASS: colors.grass,
    WATER: colors.blue,
    COAL: colors.black
}

# a list representing our tile map
tilemap = [
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, DIRT,  GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, DIRT,  DIRT, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, DIRT, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL],
    [GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL, GRASS, GRASS, GRASS, GRASS, COAL, COAL]
]

# initialize clock. used later in the loop.
clock = pygame.time.Clock()
FPS = 16
frame = 0

player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
invaders_group = pygame.sprite.Group()

PLAYER_COLOR = (200, 50, 50)
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 16

BULLET_WIDTH = 16
BULLET_HEIGHT = 32
BULLET_SPEED = FPS / 2

INVADER_COLOR = (50, 255, 50)
INVADER_WIDTH = PLAYER_WIDTH / 2
INVADER_HEIGHT = PLAYER_HEIGHT / 2

for x in range(0, 8):
    invader = Invader(INVADER_COLOR, INVADER_WIDTH, INVADER_HEIGHT)
    invader.rect.x = INVADER_WIDTH * x * 2 + INVADER_WIDTH / 2
    invader.rect.y = INVADER_HEIGHT
    invaders_group.add(invader)


player = Player( PLAYER_COLOR, PLAYER_WIDTH, PLAYER_HEIGHT)
player.rect.x = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
player.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT * 2

player_group.add(player)

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(8)
    if keys[pygame.K_RIGHT]:
        player.moveRight(8)
    if keys[pygame.K_SPACE]:
        player.shoot(bullet_group, BULLET_WIDTH, BULLET_HEIGHT)

    if(frame % 4 == 0):
        for invader in invaders_group.sprites():
            invader.move(INVADER_WIDTH / FPS * 5)

    for bullet in bullet_group.sprites():
        bullet.moveUp(BULLET_SPEED)
        for invader in invaders_group.sprites():
            if pygame.sprite.collide_rect(bullet, invader):
                invader.removeSelf(invaders_group)

    # write game logic here
    player_group.update()
    bullet_group.update()
    invaders_group.update()
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 

    # draw tile map
    # loop through each row
    for row in range(MAP_HEIGHT):
        # loop through each column
        for column in range(MAP_WIDTH):
            # draw the resource at that position
            pygame.draw.rect(screen, RESOURCE_COLORS[tilemap[row][column]], (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # write draw code here
    player_group.draw(screen)
    bullet_group.draw(screen)
    invaders_group.draw(screen)
 
    # display what has been drawn. this might change.
    pygame.display.update()
    # run at 10 fps
    frame += 1
    if(frame == FPS):
        frame = 0

    clock.tick(FPS)
 
# close the window and quit
pygame.quit()