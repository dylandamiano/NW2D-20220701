import playerClasses
import warshipClonkses

import pygame
import time

import gameSettings
import logHandler

from pygame.locals import *

pygame.init()

'''

    As of right now, the projectile class
    has no real function. The class created below
    is just a place holder and will be filled in with methods, and variables
    once the time comes.

'''

'''
    Projectile hit-boundaries will be based upon either a circle or square.
    I have not decided on which to do yet
'''

'''
    Projectile sizes are divisible by five! (or simply size / (1/5))
'''

lightImg = "Graphics\\LightRound.png"
heavyImg = "Graphics\\HeavyRound.png"

lightDimensions = (3, 7)
heavyDimensions = (3, 10)

projectileCount = 0

activeProjectiles = []

class projectile(pygame.sprite.Sprite):
    def __init__(self, orientation, owner, dimensions, imageRestore, damage):

        pygame.sprite.Sprite.__init__(self)

        self.TTL = 5

        self.localOrientation = orientation or 0
        self.lastMove = 0
        self.owner = owner

        self.remove = False

        self.damage = damage

        self.v2Pos = pygame.Vector2(owner.ship.v2Pos.x, owner.ship.v2Pos.y)
        self.v2Vel = pygame.Vector2(0, -2.5)

        self.v2Vel.rotate_ip(-self.localOrientation)

        self.imageRestore = imageRestore
        self.dimensions = dimensions

        self.image = self.imageRestore
        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, self.dimensions)
        self.image = pygame.transform.rotate(self.image, self.localOrientation)

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def __del__(self):
        logHandler.createLog("Projectile has been removed!")

    def findNearestTarget(self):
        pass

    def update(self):

        #if (self.v2Pos.x <= 1000) and (self.v2Pos.x >= -100) and (self.v2Pos.y <= 1000) and (self.v2Pos.y >= -100):
        self.v2Pos += self.v2Vel
        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, self.dimensions)
        self.image = pygame.transform.rotate(self.image, self.localOrientation)

        self.rect.center = self.v2Pos

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

        #else:
            #return 'remove'



    def countDown(self):
        if self.TTL > 0:
            self.TTL -= 1

    def __del__(self,):
        #print("Projectile has been removed!")
        logHandler.createLog("Projectile removed!")        

class lightRound(projectile):
    def __init__(self, orientation, owner):
        logHandler.createLog("Object lightRound has been created!")

        self.image = lightImg
        self.damage = 100/10

        super().__init__(orientation, owner, lightDimensions, self.image, self.damage)

class heavyRound(projectile):
    def __init__(self, orientation, owner):
        logHandler.createLog("Object lightRound has been created!")

        self.image = heavyImg
        self.damage = 100/5
         
        super().__init__(orientation, owner, heavyDimensions, self.image, self.damage)

def createProjectile(orientation, owner):
    global projectileCount
    global heavyDimensions
    global lightDimensions

    projectileCount += 1
    tempObj = None

    if owner.ship.round_type == "light":
        tempObj = lightRound(orientation, owner)
        activeProjectiles.append(tempObj)
        logHandler.createLog("Protectile #" + str(projectileCount) + " has been created! Type: Light")
    elif owner.ship.round_type == "heavy":
        tempObj = heavyRound(orientation, owner)
        activeProjectiles.append(tempObj)
        logHandler.createLog("Protectile #" + str(projectileCount) + " has been created! Type: Light")

logHandler.createLog("Initialized Projectile handler...")

def mouseFired(orientation, owner):
    global projectileCount
    projectileCount += 1

    createProjectile(orientation, owner)

    #print("Mouse clicked, firing projectile!")
    logHandler.createLog("Projectile created! ID: #" + str(projectileCount))

def updateProjectiles():
    global activeProjectiles
    toDelete = []

    for index in range(0, len(activeProjectiles)):
        activeProjectiles[index].update()

        if (activeProjectiles[index].v2Pos.x <= 1000) and (activeProjectiles[index].v2Pos.x >= -100) and (activeProjectiles[index].v2Pos.y <= 1000) and (activeProjectiles[index].v2Pos.y >= -100):
            pass
        else:
            toDelete.append(index)

    for index in reversed(toDelete):
        del activeProjectiles[index]