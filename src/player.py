import pygame

class Floppy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Importing all the images and store them in a list to pick them gradually and make an animation
        floppy1 = pygame.image.load('Assets/floppy/floppy1.png').convert_alpha()
        floppy2 = pygame.image.load('Assets/floppy/floppy2.png').convert_alpha()
        floppy3 = pygame.image.load('Assets/floppy/floppy3.png').convert_alpha()
        floppy4 = pygame.image.load('Assets/floppy/floppy4.png').convert_alpha()
        self.floppy = [floppy1,floppy2,floppy3,floppy4]

        # Indexes for the animation and gravity
        self.floppy_index = 0
        self.gravity = 0

        self.image = self.floppy[self.floppy_index]
        self.rect = self.image.get_rect(center = (100,300))
        self.mask = pygame.mask.from_surface(self.image)

    # Method to enable jumping and gravity
    def motion(self):
        # If mouse pressed floppy jumps
        if pygame.mouse.get_pressed()[0] and self.rect.bottom <= 600:
            self.gravity = -5
        
        # The gravity will increment at each update, changing the y pos of the flappy and falling faster the more we fall
        self.gravity += 0.3
        self.rect.y += self.gravity
        # If floppy touches ground it stops
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        # If floppy touches ceiling it stops
        elif self.rect.top <= 0:
            self.rect.top = 0

    # Method to update the images of the surface to make the motion animation
    def animation(self):
        self.floppy_index += 0.1
        if self.floppy_index >= len(self.floppy):
            self.floppy_index = 0
        self.image = self.floppy[int(self.floppy_index)]
        

    def update(self):
        self.animation()
        self.motion()

