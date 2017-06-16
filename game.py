import pygame
from classes.player import Player
from classes.invader import Invader
from classes.colors import Colors
import noise
from noise import pnoise2

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

def InitTileMap(width, height):
    rows = [None] * height
    for idx, val in enumerate(rows):
        rows[idx] = [None] * width
    return rows

def GetTileMap(seed=1):
    tile_array = InitTileMap(MAP_WIDTH, MAP_HEIGHT)
    octaves = 1
    freq = 16.0 / octaves
    half_size = 128.0
    half_min_one = 127.0

    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            noise = int(pnoise2(
                x / freq, 
                y / freq, 
                octaves,
                # 0.5,  # persistence
                # 2.0,  # lacunarity
                # 1024, # repeatx
                # 1024, # repeaty
                base=seed # base
                ) * half_min_one + half_size)
            tile_array[y][x] = noise
    
    return tile_array

DRAW_MODE = 'tiles'
tilemap = GetTileMap(1)

def GetNoiseTile(nn):
    if nn < 100:
        return WATER
    elif nn < 170:
        return GRASS
    else:
        return DIRT

def GetNoiseColor(nn):
    if nn > 255:
        nn = 255
    elif nn < 0:
        nn = 0
    return (nn, nn, nn)

def GetTileColor(noise):
    if DRAW_MODE == 'tiles':
        noise = GetNoiseTile(noise)
        return RESOURCE_COLORS[noise]
    else:
        return GetNoiseColor(noise)
    return

def DrawMap(rect_map):
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            color = GetTileColor(tilemap[row][column])
            pygame.draw.rect(screen, color, (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

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
INVADER_ROW_SPACE = PLAYER_HEIGHT
invader_amount = 1

# create event types
move_side_event = pygame.USEREVENT + 1
move_down_event = pygame.USEREVENT + 2
reloaded_event  = pygame.USEREVENT + 3

def AddNewInvaders(amount):
    
    global invader_amount

    rows = []

    for i in range(1, amount + 1):
        rows.append(i)

    for row in rows:
        for x in range(0, 6):
            invader = Invader(INVADER_COLOR, INVADER_WIDTH, INVADER_HEIGHT)
            invader.rect.x = INVADER_WIDTH * x * 2 + INVADER_WIDTH / 2
            invader.rect.y = (INVADER_HEIGHT + INVADER_ROW_SPACE) * row
            print row
            invaders_group.add(invader)
    
    invader_amount += 1

AddNewInvaders(invader_amount)

player = Player( PLAYER_COLOR, PLAYER_WIDTH, PLAYER_HEIGHT)
player.rect.x = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
player.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT * 2

player_group.add(player)

# Score
myfont = pygame.font.SysFont("Helvetica", 15, bold=True)
score = 0

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == reloaded_event:
            # when the reload timer runs out, reset it
            player.reloaded = True
            pygame.time.set_timer(reloaded_event, 0)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(8)
    if keys[pygame.K_RIGHT]:
        player.moveRight(8)
    if keys[pygame.K_SPACE]:
        if player.reloaded == True:
            player.shoot(bullet_group, BULLET_WIDTH, BULLET_HEIGHT)
            pygame.time.set_timer(reloaded_event, 250)

    if(frame % 4 == 0):
        for invader in invaders_group.sprites():
            invader.move(INVADER_WIDTH / FPS * 5)

    for bullet in bullet_group.sprites():
        bullet.moveUp(BULLET_SPEED)
        for invader in invaders_group.sprites():
            if pygame.sprite.collide_rect(bullet, invader):
                invader.removeSelf(invaders_group)
                score += 1
    
    if not invaders_group:
        AddNewInvaders(invader_amount)
                    

    # write game logic here
    player_group.update()
    bullet_group.update()
    invaders_group.update()
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 

    # draw tile map
    # loop through each row
    DrawMap(tilemap)

    # write draw code here
    player_group.draw(screen)
    bullet_group.draw(screen)
    invaders_group.draw(screen)

    # lastly draw score and HUD
    label = myfont.render("Score: " + str(score), 1, (255,255,255))
    screen.blit(label, (20, 20))
 
    # display what has been drawn. this might change.
    pygame.display.update()
    # run at 10 fps
    frame += 1
    if(frame == FPS):
        frame = 0

    clock.tick(FPS)
 
# close the window and quit
pygame.quit()