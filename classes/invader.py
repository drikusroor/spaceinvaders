import pygame

class Invader(pygame.sprite.Sprite):
    
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

       self.counter = 0
       self.counter_max = 10
       self.flip = 0

    def incrementCounter(self):
        self.counter += 1
        if self.counter == self.counter_max:
            self.counter = 0

    def move(self, pixels):
        if(self.counter < self.counter_max / 2):
            self.moveRight(pixels)
        else:
            self.moveLeft(pixels)
        self.incrementCounter()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels