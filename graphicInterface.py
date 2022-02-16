import pygame
import logHandler

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
        
        self.images = {
            "homeMenu": "Graphics/graphicalMenu.png",    
            "aboutMenu": "Graphics/aboutMenu.png",
            "shipMenu": None,
            "debugMenu": "Graphics/debugMenuNW2D.png" # Top Min = 60.7 || BOTTOM Min = 839.3
        }
        self.originalMenu = self.images["homeMenu"]
        self.active = False

        self.currentSelection = "Main"

        self.image = pygame.image.load(self.originalMenu)
        self.image = pygame.transform.scale(self.image, (900, 900))

        self.rect = self.image.get_rect()
        self.rect.center = (900/2, 900/2)

        self.buttonRegions = {
            "MAIN": {
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
            },

            "ABOUT": {
                "Return": {
                    "top-left": (294.9, 750),
                    "bottom-right": (605, 833.8),
                    "center": (450, 791.9)
                 }
            },
        }

        def changeMenu(self):
            pass

         # Values will be as tuple x,y) within a multidimensional array

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
    print(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][0])
    #print(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0])
    if mainMenu.currentSelection == "Main":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0]))): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1] <= mousePosition[1]):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1]))):
                print("Square one!")
                return "PLAY"
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-two"]["bottom-right"][1]))):
                print("Square two!")
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-three"]["bottom-right"][1]))):
                print("Square three!")
                mainMenu.currentSelection = "Debug"
                mainMenu.originalMenu = mainMenu.images["debugMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        elif (mousePosition[0] >= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["bottom-right"][1]))):
                print("Square one!")
                mainMenu.currentSelection = "About"
                mainMenu.originalMenu = mainMenu.images["aboutMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-two"]["bottom-right"][1]))):
                print("Square two!")
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-three"]["bottom-right"][1]))):
                print("Square three!")
                return "STOP"
        else:
            print("not quite...")

    elif mainMenu.currentSelection == "About":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["bottom-right"][1]))):
                print("Square one!")
                mainMenu.currentSelection = "Main"
                mainMenu.originalMenu = mainMenu.images["homeMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))

    elif mainMenu.currentSelection == "Debug":
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))