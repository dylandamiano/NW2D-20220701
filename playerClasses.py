import pygame
import warshipClonkses

import gameSettings

import math, random
import logHandler

from pygame.locals import *

'''

    Player class will be used for creating the player which will house a pointer variable to
    the ship currently being used (self.ship)

    To create a ship, call self.createShip()
    To retrieve stats, call self.get_stats()
    To damage or destroy, call self.destroy() // This may or may not include more variables later on

'''

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.username = name
        self.ship = "Carrier" # Default selection
        self.type = "sea" # Default selection

        self.last_fired = 0

        self.player_owned = False
        self.player_sel = None

        self.AI = False
        
        self.health = 100
          
        print("New class initialized...")

    def createShip(self, ship_type, x = 450, y = 450):
        print("Creating ship...")
        if (ship_type == "Fighter"):
            self.ship = warshipClonkses.Fighter(self, x, y)
            #self.ship.owner = self.username
        elif (ship_type == "Carrier"):
            self.ship = warshipClonkses.Carrier(self, x, y)
            print(self.ship.owner)
        elif (ship_type == "Frigate"):
            self.ship = warshipClonkses.Destroyer(self, x, y)
            print(self.ship.owner)
        elif (ship_type == "Destroyer"):
            self.ship = warshipClonkses.Destroyer(self, x, y)
            print(self.ship.owner)

    def destroy(self):
        self.health = 0

    def get_stats(self, stat):
        if (stat == "username"):
            print(self.username)
            return self.username
        elif (stat == "ship"):
            if (self.ship != None):
                print(self.ship.shipName)
                return self.ship.shipName
            else:
                print("No ship was found...")

class computerEntity(Player):
    def __init__(self, name, owner = None):
        pygame.sprite.Sprite.__init__(self)
        Player.__init__(self, name)

        self.AI = True
        self.reverse = False

        self.last_move = 0
        self.last_rotate = 0
        
        self.rotate_direction = 0
        self.move_direction = 1

        print("New class initialized...")
        logHandler.createLog("Dumb-AI Entity created!")

'''

    The Map Object is currently meant to be static but is subject to change.

    There may or may not be a DAY/NIGHT cycle however, this is not
    going to be guaranteed as of right now.

    In the future, there will be a DAY/NIGHT cycle and there will
    be map rotations.

'''

class islandMap(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Maps\\mapDesign2.png")
        self.image = pygame.transform.scale(self.image, (900, 900))

        self.rect = self.image.get_rect()
        self.rect.center = (450, 450)

        self.sun = True;

    def changeLighting(self):
        if (self.sun == True):
            print("Day time!")
        else:
            print("Night time!")


'''

    The Cloud Object currently has 5 different clouds to choose from;
    each of which is currently chosen at random.

    The Clouds will spawn at a random location on the screen
    and will vary in movement speed and spawn intervals.

'''

cloudCount = 0
class Cloud(pygame.sprite.Sprite):
    def __init__(self, cloudDes, cloudDims, cloudSpeed = None):
        global cloudCount

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(gameSettings.cloudChart[cloudDes]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (cloudDims[cloudDes][0], cloudDims[cloudDes][1]))

        self.rect = self.image.get_rect()
        self.rect.center = (-100, 450)

        self.posX = -100

        self.moveSpeed = cloudSpeed
        self.moveInt = 0
        self.lastMove = 0
    
        cloudCount += 1
        logHandler.createLog("Cloud created! ID: #" + str(cloudCount))

    def __del__(self):
        #print("Cloud removed!")
        logHandler.createLog("Cloud removed! ID: #" + str(cloudCount))
        del self

    def createLocation(self):
        randomY = math.floor(random.randrange(0, 900))
        self.rect.center = (-100, randomY)

        self.moveInt = random.randrange(2, 3)
        #print(self.moveInt)