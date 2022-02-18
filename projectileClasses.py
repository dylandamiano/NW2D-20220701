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

lightRound = "Graphics\\HeavyRound.png"
heavyRound = "Graphics\\LightRound.png"

lightDimensions = (3, 7)
heavyDimensions (3, 10)

projectileCount = 0

activeProjectiles = []

class projectile(pygame.sprite.Sprite):
    def __init__(self, orientation, owner, dimensions, imageRestore, damage):
        pygame.sprite.Sprite.__init__(self)

        self.TTL = 5

        self.localOrientation = orientation
        self.lastMove = 0

        self.damage = damage

        self.v2Pos = pygame.Vector2(owner.v2Pos.x, owner.v2Pos.y)
        self.v2Vel = pygame.Vector2(0, 1)

        self.v2Vel.rotate_ip(orientation)

        self.imageRestore = imageRestore
        self.dims = (dimensions[0], dimensions[1])

        self.image = self.imageRestore
        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, (20, 41))
        self.image = pygame.transform.rotate(self.image, self.localOrientation)

    def __del__(self):
        logHandler.createLog("Projectile has been removed!")

    def findNearestTarget(self):
        pass

    def update(self, picture):

        if (self.v2Pos.x <= 900) and (self.v2Pos.x >= 0) and (self.v2Pos.y <= 900) and self.v2Pos.y >= 0):
            self.v2Pos += self.v2Vel
            self.image = self.imageRestore
            self.image = pygame.transform.scale(self.image, (20, 41))
            self.image = pygame.transform.rotate(self.image, self.localOrientation)

    def countDown(self):
        if self.TTL > 0:
            self.TTL -= 1

    def __del__(self, entityName):
        print("Projectile has been removed! Originating entity: " + entityName)
        logHandler.createLog("Projectile removed!")        

class lightRound(projectile):
    def __init__(self, orientation, owner):
        logHandler.createLog("Object lightRound has been created!")

        self.image = "Graphics\\LightRound.png"
        self.damage = 2.5

        super().__init__(orientation, owner, lightDimensions, self.iamge, self.damage)

test = lightRound(0, None, )

class heavyRound(projectile):
    pass

def createProjectile(type, orientation, owner):
    global projectileCount
    global heavyDimensions
    global lightDimensions

    projectileCount += 1
    tempObj = None

    if type == "heavy":
        tempObj = projectile(heavyDimensions, orientation, owner)
        activeProjectiles.append(tempObj)
        logHandler.createLog("Protectile #" + projectileCount + " has been created! Type: Heavy")
        
    elif type == "light":
        tempObj = projectile(lightDimensions, orientation, owner)
        activeProjectiles.append(tempObj)
        logHandler.createLog("Protectile #" + projectileCount + " has been created! Type: Light")

logHandler.createLog("Initialized Projectile handler...")