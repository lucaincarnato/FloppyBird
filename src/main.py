import pygame 
from sys import exit
from player import Floppy

pygame.init()
screen = pygame.display.set_mode((400,700))
clock = pygame.time.Clock()

# Sky and Ground surface
sky = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()

# Initializing the floppy Sprite Group
floppy = pygame.sprite.GroupSingle()
floppy.add(Floppy())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

    # Sky and Ground on screen
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,600))

    # Drawing and updating the Floppy on the disk
    floppy.draw(screen)
    floppy.update()

    pygame.display.update()
    clock.tick(60)