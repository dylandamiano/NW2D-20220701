import pygame
#import logHandler

import credit_handler
import computer_movement

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
            "deathMenu": "Graphics/game_over.png",
            "statMenu": "Graphics/stat_menu.png",
            "controlMenu": "Graphics/controls_nw2d.png",
            "shopMenu": "Graphics/shop_menu.png"
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
        #logHandler.createLog("Death menu active!")

class headsUpDisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init(self)
        
        self.active = False
        self.originalMenu = None
        self.currentMenu = None


mainMenu = menuInterface()

def multiple_lines(surface, *args):
    font = pygame.font.SysFont("Segoe UI Light", 32)
    skip = 0

    for i in range(0, len(args)):
        text = pygame.font.Font.render(font, str(args[i]), 1, (0,0,0))
        surface.blit(text, (150, 520 + skip))
        skip += 24

def update_text(surface):
    font = pygame.font.SysFont("Segoe UI Light", 16)
    if mainMenu.selection == 0:
        multiple_lines(surface, "1x Carrier", "Comes with 2 Jets", "10 Damage p/Shot", "Project firepower from afar")
    elif mainMenu.selection == 1:
        multiple_lines(surface, "1x Destroyer", "No jets", "20 Damage p/Shot", "Protects the battlegroup")
    elif mainMenu.selection == 2:
        multiple_lines(surface, "1x Fighter", "You are not the A-10 Brrt Hog", "10 Damage p/Shot", "Bring the fight to the enemy from the skies!")

def checkShip():
    if mainMenu.selection == 0:
        return "Graphics/ship_select_icons/CARRIER.png"
    elif mainMenu.selection == 1:
        return "Graphics/ship_select_icons/Destroyer.png"
    elif mainMenu.selection == 2:
        return "Graphics/ship_select_icons/jet.png"

def checkMouseInput(player = None, DISPLAYSURF = None):
    mousePosition = pygame.mouse.get_pos() # Returns as tuple (x, y)
    print(mousePosition[0])
    print(mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][0])
    #print(mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0])
    if mainMenu.currentSelection == "Main":
        if (mousePosition[0] >= 26.3) and (mousePosition[0] <= 26.3 + 222.4): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1] <= mousePosition[1]):
            if (mousePosition[1] >= 262.2) and (mousePosition[1] <= 262.2+65.9): # start game
                #logHandler.createLog("Game resumed!")
                return "PLAY"
            elif (mousePosition[1] >= 370.4) and (mousePosition[1] <= 370.4+58): # debug
                mainMenu.currentSelection = "Debug"
                mainMenu.originalMenu = mainMenu.images["debugMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Opened Debug Menu!")
            elif (mousePosition[1] >= 436.3) and (mousePosition[1] <= 436.3+58): # about
                mainMenu.currentSelection = "About"
                mainMenu.originalMenu = mainMenu.images["aboutMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Opened about menu!")
            elif (mousePosition[1] >= 494.5) and (mousePosition[1] <= 494.5+58): # plr stat
                mainMenu.currentSelection = "statMenu"
                
                mainMenu.originalMenu = mainMenu.images["statMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Returning to menu!")
            elif (mousePosition[1] >= 552.3) and (mousePosition[1] <= 552.3+58): # controls
                mainMenu.currentSelection = "controlMenu"
                
                mainMenu.originalMenu = mainMenu.images["controlMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Returning to menu!")
            elif (mousePosition[1] >= 668.3) and (mousePosition[1] <= 668.3+58): # restart
                mainMenu.currentSelection = "shipMenu"
                
                mainMenu.originalMenu = mainMenu.images["shipMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Returning to menu!")

                return "RESTART"
            elif (mousePosition[1] >= 726.7) and (mousePosition[1] <= 726.7+58): # exit
                return "STOP"
        else:
            print("not quite...")

    elif mainMenu.currentSelection == "About":
        if (mousePosition[0] >= 0) and (mousePosition[0] <= 900):
            if (mousePosition[1] >= 0) and (mousePosition[1] <= 900):
                #print("Square one!")
                mainMenu.currentSelection = "Main"
                mainMenu.originalMenu = mainMenu.images["homeMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Returning to menu!")

    elif mainMenu.currentSelection == "Debug":
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Returning to menu!")

    elif mainMenu.currentSelection == "statMenu":
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Returning to menu!")

    elif mainMenu.currentSelection == "controlMenu":
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Returning to menu!")

    elif mainMenu.currentSelection == "shipMenu":
        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["select"]["bottom-right"][1]))):
                print("L!") # RETURNS TO MENU
                mainMenu.currentSelection = "Main"
                mainMenu.originalMenu = mainMenu.images["homeMenu"]
                mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                #logHandler.createLog("Returning to menu!")

                return "Menu"

        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-left"]["bottom-right"][1]))):
                print("Ship changed!")
                pass # Will be determined later!

                if mainMenu.selection > 0:
                   mainMenu.selection -= 1
                elif mainMenu.selection == 0: 
                    mainMenu.selection = 2

        elif (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["arrow-right"]["bottom-right"][1]))):
                print("Ship changed!")
                pass # Will be determined later!

                if mainMenu.selection < 2:
                    mainMenu.selection += 1
                elif mainMenu.selection == 2:
                    mainMenu.selection = 0

        if (mousePosition[0] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["top-left"][0])) and ((mousePosition[0] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["bottom-right"][0]))):
            if (mousePosition[1] >= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["top-left"][1])) and ((mousePosition[1] <= abs(mainMenu.buttonRegions["SHIP_SELECT"]["return"]["bottom-right"][1]))):
                print("R!") # SELECTS SHIP
                #mainMenu.currentSelection = "Main"
                #mainMenu.originalMenu = mainMenu.images["homeMenu"]
                #mainMenu.image = pygame.image.load(mainMenu.originalMenu)
                #mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
                ##logHandler.createLog("Returning to menu!")

                mainMenu.chosen = mainMenu.selection

                return "Select"

    elif mainMenu.currentSelection == "Death":
        mainMenu.currentSelection = "shipMenu"
        mainMenu.originalMenu = mainMenu.images["shipMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Returning to menu!")

        return "fix_death"

    elif (mainMenu.currentSelection == "shopMenu") and (player != None):
        if (mousePosition[1] >= 348.8) and (mousePosition[1] <= 348.8 + 230.8): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1] <= mousePosition[1]):
            if (mousePosition[0] >= 86) and (mousePosition[0] <= 86+222.4): # Friendly JETS
                if credit_handler.purchase_item("Jets") == True:
                    computer_movement.summon_player_entities(player, True, "Fighter")
            elif (mousePosition[0] >= 370.4) and (mousePosition[0] <= 370.4+222.4): # Friendly CARRIER
                if credit_handler.purchase_item("Carrier") == True:
                    computer_movement.summon_player_entities(player, True, "Carrier")
            elif (mousePosition[0] >= 591.6) and (mousePosition[0] <= 591.6+222.4): # Friendly Destroyer
                if credit_handler.purchase_item("Destroyer") == True:
                    computer_movement.summon_player_entities(player, True, "Destroyer")
                    print("Region 1")
            else:
                return "PLAY"

        elif (mousePosition[1] >= 609.3) and (mousePosition[1] <= 609.3 + 230.8): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][0] <= mousePosition[0]): #and (mainMenu.buttonRegions["MAIN"]["left-one"]["top-left"][1] >= mousePosition[1]) and (mainMenu.buttonRegions["MAIN"]["left-one"]["bottom-right"][1] <= mousePosition[1]):
            if (mousePosition[0] >= 86) and (mousePosition[0] <= 86+222.4): # Self Heal
                if credit_handler.purchase_item("Heal") == True:
                    player.ship.health = player.ship.max_health
            elif (mousePosition[0] >= 370.4) and (mousePosition[0] <= 370.4+222.4): # Battlegroup
                if credit_handler.purchase_item("Battlegroup") == True:
                    computer_movement.summon_player_entities(player, True, "Group")
            elif (mousePosition[0] >= 591.6) and (mousePosition[0] <= 591.6+222.4): # Clear Wave
                print("TEST 2")
            else:
                return "PLAY"
            print("Region 2")

        else:
            return "PLAY"

def display_Shop(activate: bool) -> None:
    if activate == True:
        mainMenu.currentSelection = "shopMenu"
        mainMenu.originalMenu = mainMenu.images["shopMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Activating shop!")
    elif activate == False:
        mainMenu.currentSelection = "Main"
        mainMenu.originalMenu = mainMenu.images["homeMenu"]
        mainMenu.image = pygame.image.load(mainMenu.originalMenu)
        mainMenu.image = pygame.transform.scale(mainMenu.image, (900, 900))
        #logHandler.createLog("Returning to game!")

#logHandler.createLog("Initialized GUI handler...")