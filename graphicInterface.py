import pygame

# Buttons have to be drawn manually

'''
    The initialization of the classes will also occur in this file
    to ensure that everything is in one spot.
'''

userInterfaces = []

class menuInterface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.originalMenu = None
        self.currentMenu = None
        self.active = False

        self.image = pygame.image.load(self.currentMenu)
        self.image = pygame.transform.scale(self.image, (900, 900))

        self.rect = self.image.get_rect()
        self.rect.center = (900/2, 900/2)

        self.buttonLocations = []; # Values will be as tuple (x,y) within a multidimensional array

class headsUpDisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init(self)
        
        self.active = False
        self.originalMenu = None
        self.currentMenu = None

def checkMouseInput():
    mousePosition = pygame.mouse.get_pos() # Returns as tuple (x, y)

    for i in userInterfaces:
        if (userInterfaces[i].active == False):
            pass
        elif (userInterfaces[i].active == True):
            print("This UI module is currently active!")
