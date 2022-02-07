import playerClasses
import warshipClonkses

import pygame

import gameSettings

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

class projectile(pygame.sprite.Sprite):
    def __init__(self):
        TTL = 5

        v2Pos = pygame.Vector2(0, 0)
        v2Vel = pygame.Vector2(0, 1)

    def findNearestTarget(self):
        pass

    def countDown():
        TTL -= 1

        if TTL <= 0:
            del self

    def __del__(self, entityName):
        #print("Projectile has been removed! Originating entity: " + entityName)