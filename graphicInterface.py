import pygame
import logging

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
            "shipMenu": "Graphics/shipSelection.png",
            "debugMenu": "Graphics/debugMenuNW2D.png", # Top Min = 60.7 || BOTTOM Min = 839.3
            "deathMenu": "Graphics/game_over.png"
        }

        self.selection = 0
        self.chosen = 0

        self.originalMenu = self.images["shipMenu"]
        self.active = False

        self.currentSelection = "shipMenu"

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

            "SHIP_SELECT": {
                "arrow-left": {
                    "top-left": (108, 309),
                    "bottom-right": (191.4, 450),
                 },

                "arrow-right": {
                    "top-left": (708.4, 309),
                    "bottom-right": (792, 450),
                },

                "select": {
                    "top-left": (124, 755.4),
                    "bottom-right": (434.1, 839.2),
                },

                "return": {
                    "top-left": (465.9, 755.4),
                    "bottom-right": (776, 839.2),
                },
            },
        }

    def changeMenu(self):
        pass

    def currentMenu(self):
        return self.currentSelection

    def setDeath(self):
        self.originalMenu = self.images["deathMenu"]
        self.currentSelection = "Death"

        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        logging.debug("Death menu active!")

class headsUpDisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init(self)
        
        self.active = False
        self.originalMenu = None
        self.currentMenu = None


mainMenu = menuInterface()

def checkShip():
    if mainMenu.selection == 0:
        return "Graphics/ship_select_icons/CARRIER.png"
    elif mainMenu.selection == 1:
        return "Graphics/ship_select_icons/Destroyer.png"
    elif mainMenu.selection == 2:
        return "Graphics/ship_select_icons/jet.png"
    


def checkMouseInput():
    mousePosition = pygame.mouse.get_pos() # Returns as tuple (x, y)
    logging.debug(mousePosition[0])
    logging.debug(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][0])
    #logging.debug(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0])
    if mainMenu.currentSelection == "Main":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0]))): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1] <= mousePosition[1]):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1]))):
                logging.debug("Square one!")
                logging.debug("Game resumed!")
                return "PLAY"
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-two"]["bottom-right"][1]))):
                logging.debug("Square two!")
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["left-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["left-three"]["bottom-right"][1]))):
                logging.debug("Square three!")
                mainMenu.currentSelection = "Debug"
                mainMenu.originalMenu = mainMenu.images["debugMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                logging.debug("Opened Debug Menu!")
        elif (mousePosition[0] >= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-one"]["bottom-right"][1]))):
                logging.debug("Square one!")
                mainMenu.currentSelection = "About"
                mainMenu.originalMenu = mainMenu.images["aboutMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                logging.debug("Opened about menu!")
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-two"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-two"]["bottom-right"][1]))):
                logging.debug("Square two!")

                mainMenu.currentSelection = "shipMenu"

                mainMenu.originalMenu = mainMenu.images["shipMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                logging.debug("Returning to menu!")

                return "RESTART"
            elif (mousePosition[1] >= abs(mainMenu.buttonRegions["MAIN"]["right-three"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["MAIN"]["right-three"]["bottom-right"][1]))):
                logging.debug("Square three!")
                return "STOP"
        else:
            logging.debug("not quite...")

    elif mainMenu.currentSelection == "About":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["ABOUT"]["Return"]["bottom-right"][1]))):
                logging.debug("Square one!")
                mainMenu.currentSelection = "Main"
                mainMenu.originalMenu = mainMenu.images["homeMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                logging.debug("Returning to menu!")

    elif mainMenu.currentSelection == "Debug":
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        logging.debug("Returning to menu!")

    elif mainMenu.currentSelection == "shipMenu":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["bottom-right"][1]))):
                logging.debug("L!") # RETURNS TO MENU
                mainMenu.currentSelection = "Main"
                mainMenu.originalMenu = mainMenu.images["homeMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                logging.debug("Returning to menu!")

                return "Menu"

        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["bottom-right"][1]))):
                logging.debug("Ship changed!")
                pass # Will be determined later!

                if mainMenu.selection > 0:
                   mainMenu.selection -= 1
                elif mainMenu.selection == 0: 
                    mainMenu.selection = 2

        elif (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["bottom-right"][1]))):
                logging.debug("Ship changed!")
                pass # Will be determined later!

                if mainMenu.selection < 2:
                    mainMenu.selection += 1
                elif mainMenu.selection == 2:
                    mainMenu.selection = 0

        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["bottom-right"][1]))):
                logging.debug("R!") # SELECTS SHIP
                #mainMenu.currentSelection = "Main"
                #mainMenu.originalMenu = mainMenu.images["homeMenu"]
                #mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                #mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logging.debug("Returning to menu!")

                mainMenu.chosen = mainMenu.selection

                return "Select"

    elif mainMenu.currentSelection == "Death":
        mainMenu.currentSelection = "shipMenu"
        mainMenu.originalMenu = mainMenu.images["shipMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        logging.debug("Returning to menu!")

        return "fix_death"


logging.debug("Initialized GUI handler...")