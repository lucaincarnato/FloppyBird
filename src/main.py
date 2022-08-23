import pygame 
from sys import exit
from player import Floppy
from obstacle import Usb

# Method to check collisions
def collision():
    # If usb group is not empty and the collision mask is true gameover
    # Collision mask is preferred to make the space between usb available
    if usb.sprites():
        if pygame.sprite.collide_mask(floppy.sprite,usb.sprites()[0]):
            usb.empty()
            return False
    return True

# Function to detect the score 
def score_detection():
    # Score for the game
    score_font = pygame.font.Font('Assets/scorefont.ttf',90)
    score_surf = score_font.render(f'{score}',False,(0,0,0))
    score_rect = score_surf.get_rect(center = (200,75))
    screen.blit(score_surf,score_rect)
    if pygame.sprite.spritecollide(floppy.sprite,usb,False):
        return 1
    return 0


pygame.init()
screen = pygame.display.set_mode((400,700))
pygame.display.set_caption('Floppy bird')
clock = pygame.time.Clock()
score = 0
game_state = False

# Sky and Ground surface
sky = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()

# Messages for the main page
title_font = pygame.font.Font('Assets/titlefont.ttf',90)
title_surf = title_font.render('Floppy Bird',False,(31,30,30))
title_rect = title_surf.get_rect(center = (200,120))

# Icon of the game
icon_surface = pygame.image.load('Assets/floppy/floppy1.png').convert_alpha()
icon_surface = pygame.transform.rotozoom(icon_surface,0,2)
icon_rectangle = icon_surface.get_rect(center = (200,300))

# Score for the main page's message
score_message_surf = title_font.render(f'{score}',False,(0,0,0))
score_message_rect = score_message_surf.get_rect(center = (200,470))

# Istruction in case score != 0
istruction_font = pygame.font.Font('Assets/titlefont.ttf',50)
istruction_surf = istruction_font.render('Press space to play',False,(0,0,0))
istruction_rect = istruction_surf.get_rect(center = (200,450))

# Credits
credit_font = pygame.font.Font('Assets/titlefont.ttf',30)
credit_surf = credit_font.render('Made by Luca Maria Incarnato',False,(0,0,0))
credit_rect = credit_surf.get_rect(midbottom = (200,670))


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

        if game_state:
            # Render a new usb if the timer ticks
            if event.type == obstacle_timer:
                usb.add(Usb())
        else:
            # It should be mouse 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = True


    if game_state:
        # Sky and Ground on screen
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,600))

        # Drawing and updating the Floppy on the screen
        floppy.draw(screen)
        floppy.update()

        # Drawing and updating the usb on the screen
        usb.draw(screen)
        usb.update()

        # Updating the score 
        score += score_detection()

        # Changing the game state depending on collisions
        game_state = collision()
    else: 
        screen.fill((192,203,220))
        screen.blit(title_surf,title_rect)
        screen.blit(icon_surface,icon_rectangle)
        screen.blit(istruction_surf,istruction_rect)
        screen.blit(credit_surf,credit_rect)
        score = 0

    pygame.display.update()
    clock.tick(60)

# ! The score does not increment correctly