import pygame
from classes.block import Block

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

blocks_group = pygame.sprite.Group()

block1 = Block( (100,100,0), 100, 100)
block1.rect.x = 100
block1.rect.y = 100

blocks_group.add(block1)

# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here
    blocks_group.update()
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    blocks_group.draw(screen)
 
    # display what has been drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()