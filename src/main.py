import pygame 
from sys import exit
from player import Floppy
from obstacle import Usb

# Method to check collisions
def collision():
    # If usb group is not empty and the collision mask is true gameover
    # Collision mask is preferred to make the space between usb available
    if usb.sprites() and pygame.sprite.collide_mask(floppy.sprite,usb.sprites()[0]):
        pygame.QUIT
        exit()

pygame.init()
screen = pygame.display.set_mode((400,700))
pygame.display.set_caption('Floppy bird')
clock = pygame.time.Clock()
score = 0

# Sky and Ground surface
sky = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()

# Initializing the floppy Sprite Group
floppy = pygame.sprite.GroupSingle()
floppy.add(Floppy())

# Initializing the Sprite Group
usb = pygame.sprite.Group()

# Timer to render multiple usb
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,4000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()

        if event.type == obstacle_timer:
            usb.add(Usb())

    # Sky and Ground on screen
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,600))

    # Drawing and updating the Floppy on the screen
    floppy.draw(screen)
    floppy.update()

    # Drawing and updating the usb on the screen
    usb.draw(screen)
    usb.update()

    # Drawing and Updating the score 
    collision()

    pygame.display.update()
    clock.tick(60)