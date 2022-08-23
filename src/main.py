import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400,700))
clock = pygame.time.Clock()

# Sky and Ground surface
sky = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

    # Sky and Ground on screen
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,600))

    pygame.display.update()
    clock.tick(60)