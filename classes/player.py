import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.color = color

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def shoot(self, bullet_group, width, height):
        bullet = Bullet((255, 200, 50), width, height)
        bullet.rect.x = self.rect.x + self.rect.width / 2 - width / 2
        bullet.rect.y = self.rect.y - self.rect.height - height / 2
        bullet_group.add(bullet)