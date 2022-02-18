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
        self.ship = None
        self.type = ""
        
        self.health = 100
          
        print("New class initialized...")

    def createShip(self, type):
        print("Creating ship...")
        if (type == "Fighter"):
            self.ship = warshipClonkses.Fighter(self)
            #self.ship.owner = self.username
        elif (type == "Carrier"):
            self.ship = warshipClonkses.Carrier(self)
            print(self.ship.owner)
        elif (type == "Frigate"):
            pass
        elif (type == "Destroyer"):
            pass

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

class computerEntity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        pass

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
        self.rect.center = (-10, 450)

        self.posX = 0

        self.moveSpeed = cloudSpeed
        self.moveInt = 0
        self.lastMove = 0
    
        cloudCount += 1
    def __del__(self):
        print("Cloud removed!")
        logHandler.createLog("Cloud removed! ID: #" + str(cloudCount))
        del self

    def createLocation(self):
        randomY = math.floor(random.randrange(0, 900))
        self.rect.center = (-10, randomY)

        self.moveInt = random.randrange(2, 3)
        #print(self.moveInt)