import pygame

# Buttons have to be drawn manually
# Each graphical button has a width of 309.1px and a height of 125.2 px

'''
    1st Cent. - (125.2, 196.8)             2nd Cent. - (125.2, 298)                3rd Cent. - (125.2, 399.2)
    4th Cent. - (464.7, 196.8)             4th Cent. - (464.7, 298)                6th Cent. - (464.7, 399.2)
'''

'''
    Each button in order to find the corners thus accurately creating a rect tangle
    will require that you divide the width and height by 2 then add/subtract to get the endpoints as needed.
    Relatively easy.
'''

'''
    The initialization of the classes will also occur in this file
    to ensure that everything is in one spot.
'''

userInterfaces = []


class menuInterface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.originalMenu = "graphicalMenu.png"
        self.active = False

        self.image = pygame.image.load(self.originalMenu)
        self.image = pygame.transform.scale(self.image, (900, 900))

        self.rect = self.image.get_rect()
        self.rect.center = (900/2, 900/2)

        self.buttonRegions = {
            "left-one": {
                "top-left": (125.2, 196.8),
                "bottom-right": (125.2 + 309.1, 196.8 + 125.2/(3/2)),
                "center": (125.2, 196.8)
             },

            "left-two": {
                "top-left": (125.2, 298),
                "bottom-right": (125.2 + 309.1, 298 + (125.2/(3/2))),
                "center": (125.2, 298)
             },

            "left-three": {
                "top-left": (125.2, 399.2),
                "bottom-right": (125.2 + 309.1, 399.2 + (125.2/(3/2))),
                "center": (125.2, 399.2)
             },

            "right-one": {
                "top-left": (464.7, 196.8),
                "bottom-right": (464.7 + 309.1, 196.8 + (125.2/(3/2))),
                "center": (464.7, 196.8)
             },

            "right-two": {
                "top-left": (464.7, 298),
                "bottom-right": (464.7 + 309.1, 298 + (125.2/(3/2))),
                "center": (464.7, 298)
             },

            "right-three": {
                "top-left": (464.7, 399.2),
                "bottom-right": (464.7 + 309.1, 399.2 + (125.2/(3/2))),
                "center": (464.7, 399.2)
             }
        }; # Values will be as tuple (x,y) within a multidimensional array

class headsUpDisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init(self)
        
        self.active = False
        self.originalMenu = None
        self.currentMenu = None


mainMenu = menuInterface()

def checkMouseInput():
    mousePosition = pygame.mouse.get_pos() # Returns as tuple (x, y)
    print(mousePosition[0])
    print(mainMenu.buttonRegions["left-one"]["top-left"][0])
    #print(mainMenu.buttonRegions["left-one"]["bottom-right"][0])
    if (mousePosition[0] >= abs(mainMenu.buttonRegions["left-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["left-one"]["bottom-right"][0]))): #and (mainMenu.buttonRegions["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["left-one"]["bottom-right"][1] <= mousePosition[1]):
        if (mousePosition[1] >= abs(mainMenu.buttonRegions["left-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["left-one"]["bottom-right"][1]))):
            print("Square one!")
        elif (mousePosition[1] >= abs(mainMenu.buttonRegions["left-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["left-two"]["bottom-right"][1]))):
            print("Square two!")
        elif (mousePosition[1] >= abs(mainMenu.buttonRegions["left-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["left-three"]["bottom-right"][1]))):
            print("Square three!")
    elif (mousePosition[0] >= abs(mainMenu.buttonRegions["right-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["right-one"]["bottom-right"][0]))):
        if (mousePosition[1] >= abs(mainMenu.buttonRegions["right-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["right-one"]["bottom-right"][1]))):
            print("Square one!")
        elif (mousePosition[1] >= abs(mainMenu.buttonRegions["right-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["right-two"]["bottom-right"][1]))):
            print("Square two!")
        elif (mousePosition[1] >= abs(mainMenu.buttonRegions["right-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["right-three"]["bottom-right"][1]))):
            print("Square three!")
    else:
        print("not quite...")