import pygame
from classes.player import Player

# initialize game engine
pygame.init()
# set screen width/height and caption
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 32

BULLET_WIDTH = 16
BULLET_HEIGHT = 32
BULLET_SPEED = 32

player = Player( (100,100,0), PLAYER_WIDTH, PLAYER_HEIGHT)
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
        player.moveLeft(32)
    if keys[pygame.K_RIGHT]:
        player.moveRight(32)
    if keys[pygame.K_SPACE]:
        player.shoot(bullet_group, BULLET_WIDTH, BULLET_HEIGHT)

    for bullet in bullet_group.sprites():
        bullet.moveUp(BULLET_SPEED)

    # write game logic here
    player_group.update()
    bullet_group.update()
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    player_group.draw(screen)
    bullet_group.draw(screen)
 
    # display what has been drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(10)
 
# close the window and quit
pygame.quit()