import pygame 
from random import randint, choice

class Usb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Importing all the images to randomize the configuration
        usb1 = pygame.image.load('Assets/usb/usb1.png').convert_alpha()
        usb2 = pygame.image.load('Assets/usb/usb2.png').convert_alpha()
        usb3 = pygame.image.load('Assets/usb/usb3.png').convert_alpha()
        usb4 = pygame.image.load('Assets/usb/usb4.png').convert_alpha()
        usb5 = pygame.image.load('Assets/usb/usb5.png').convert_alpha()
        usb6 = pygame.image.load('Assets/usb/usb6.png').convert_alpha()
        usb7 = pygame.image.load('Assets/usb/usb7.png').convert_alpha()
        self.configuration = [usb1,usb2,usb3,usb4,usb5,usb6,usb7]

        # The image will be randomly decided at the creation of a new istance
        self.image = self.configuration[randint(0,6)]
        self.rect = self.image.get_rect(topleft = (randint(450,550),0))
        self.mask = pygame.mask.from_surface(self.image)

    # Method to destroy the usb if it goes too far 
    def destroy(self):
        if self.rect.x <= -200:
            self.kill() 

    def update(self):
        self.rect.x -= 5
        self.destroy()