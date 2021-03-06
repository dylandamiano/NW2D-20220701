import playerClasses
import pygame

import gameSettings
import logHandler

import threading

from pygame.locals import *

pygame.init()

'''

    As of right now, the damageCalc() function has no intended purpose.
    
    However, once development does start on this function, then the
    damage will be determined by distance, and warship in question.

'''
def damageCalc(attacker):
    pass

'''
    
    The ship class below will house the default variables that determine
    ship health, and provide functions to return position, status, and to also
    set values for child classes.

    The following child classes are as follows [in the order that they are presented]:
        - Battleship
        - Frigate
        - Aircraft Carrier

    Positioning and movement uses the Vector2 system

'''

class Ship(pygame.sprite.Sprite):
    def __init__(self, player, x = 450, y = 450):
        pygame.sprite.Sprite.__init__(self)

        self.localOrientation = 0
        self.vec2 = pygame.math.Vector2

        self.v2Pos = self.vec2(x, y)
        self.v2Vel = self.vec2(0, -.25)

        self.health = 100
        self.max_health = 100

        self.v2Rot = 0

        self.min_x = 0
        self.min_y = 0

        self.owner = player # Will include the player's object
        self.smoked = True
        self.shipName = None

        self.TlastMove = 0

        #self.shipCoords = {
         #   "x": self.v2Pos.x,
          #  "y": self.v2Pos.y,
           # }
           
    def shipStatus(self):
        print(self.health)

    def getLocation(self, req):
        if (req == "x"):
            return self.v2Pos.x
        elif (req == "y"):
            return self.v2Pos.y

    def setRotation(self, rotDir):
        if self.owner.health != -1:
            if (self.localOrientation <= 0):
                self.localOrientation = 360
            elif (self.localOrientation >= 360):
                self.localOrientation = 0

            if (rotDir == "Left"):
                self.v2Vel.rotate_ip(-.25)
                self.localOrientation += .25
            elif (rotDir == "Right"):
                self.v2Vel.rotate_ip(.25)
                self.localOrientation -= .25

            #print(self.localOrientation)

            self.image = pygame.image.load(self.imageRestore)
            self.image = pygame.transform.scale(self.image, (self.min_x, self.min_y))
            self.image = pygame.transform.rotate(self.image, self.localOrientation)

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def setLocation(self, moveDir):
        if self.owner.health != -1:
            if (moveDir == "Forward"):
                self.v2Pos += self.v2Vel
                pass
            elif (moveDir == "Backwards"):
                self.v2Pos -= self.v2Vel
                pass
            #self.v2Pos += self.v2Vel
            self.rect.center = self.v2Pos

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

class Battleship(Ship):
    def __init__(self, player):
        super().__init__(player)
        self.shipName == "Battleship"

        self.round_type = "heavy"

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        
        pass # Will be defined in more detail later once I get the core program setup

    def getHealth(self):
        print("Your health is at " + self.health + "%")

class Frigate(Ship):
    def __init__(self, player):
        super().__init__(player)

        self.round_type = "heavy"

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        pass # Will be defined in more detail later once I get the core program setup

class Destroyer(Ship):
    def __init__(self, player, x = 450, y = 450):
        super().__init__(player, x, y)

        self.round_type = "heavy"

        self.imageRestore = "Ships\\DestroyerConcept.png" # "Ships\\CarrierConcept.png"

        self.min_x = 9
        self.min_y = 34

        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, (self.min_x, self.min_y)) # (self.image, (20, 41))

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        pass # Will be defined in more detail later once I get the core program setup

class Carrier(Ship):
    def __init__(self, player, x = 450, y = 450):
        super().__init__(player, x, y)
        self.airWing = 5

        self.imageRestore = "Ships\\CarrierConcept.png" # "Ships\\CarrierConcept.png"

        self.min_x = 20
        self.min_y = 41

        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, (self.min_x, self.min_y)) # (self.image, (20, 41))

        self.round_type = "light"

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def test(self):
        print("Yes")

    '''
    def setRotation(self, rotDir):
        if self.owner.health != -1:
            if (self.localOrientation <= 0):
                self.localOrientation = 360
            elif (self.localOrientation >= 360):
                self.localOrientation = 0

            if (rotDir == "Left"):
                self.v2Vel.rotate_ip(-.25)
                self.localOrientation += .25
            elif (rotDir == "Right"):
                self.v2Vel.rotate_ip(.25)
                self.localOrientation -= .25

            #print(self.localOrientation)

            self.image = pygame.image.load(self.imageRestore)
            self.image = pygame.transform.scale(self.image, (20, 41))
            self.image = pygame.transform.rotate(self.image, self.localOrientation)

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def setLocation(self, moveDir):
        if self.owner.health != -1:
            if (moveDir == "Forward"):
                self.v2Pos += self.v2Vel
                pass
            elif (moveDir == "Backwards"):
                self.v2Pos -= self.v2Vel
                pass
            #self.v2Pos += self.v2Vel
            self.rect.center = self.v2Pos

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)
    '''


class Aircraft(pygame.sprite.Sprite):
    def __init__(self, player, x = 450, y = 450):
        pygame.sprite.Sprite.__init__(self)

        self.localOrientation = 0
        self.vec2 = pygame.math.Vector2

        self.v2Pos = self.vec2(x, y)
        self.v2Vel = self.vec2(0, -1)

        self.health = 100
        self.max_health = 100

        self.v2Rot = 0

        self.owner = player # Will include the player's object
        self.health = 100
        self.smoked = True
        self.shipName = None

        self.TlastMove = 0

        #self.shipCoords = {
         #   "x": self.v2Pos.x,
          #  "y": self.v2Pos.y,
           # }
           
    def shipStatus(self):
        print(self.health)

    def getLocation(self, req):
        if (req == "x"):
            return self.v2Pos.x
        elif (req == "y"):
            return self.v2Pos.y

class Fighter(Aircraft):
    def __init__(self, player, x = 450, y = 450):
        super().__init__(player, x, y)
        self.airWing = 5

        self.imageRestore = "Ships\\Fighter.png"

        self.round_type = "light"

        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, (25, 26))

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

        self.max_health = 50
        self.health = 50

    def test(self):
        print("Yes")


    def setRotation(self, rotDir):
        if self.owner.health != -1:
            if (self.localOrientation <= 0):
                self.localOrientation = 360
            elif (self.localOrientation >= 360):
                self.localOrientation = 0

            if (rotDir == "Left"):
                self.v2Vel.rotate_ip(-.5)
                self.localOrientation += .5
            elif (rotDir == "Right"):
                self.v2Vel.rotate_ip(.5)
                self.localOrientation -= .5

            #print(self.localOrientation)

            self.image = pygame.image.load(self.imageRestore)
            self.image = pygame.transform.scale(self.image, (25, 26))
            self.image = pygame.transform.rotate(self.image, self.localOrientation)

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def setLocation(self, moveDir):
        if self.owner.health != -1:
            if (moveDir == "Forward"):
                self.v2Pos += self.v2Vel
                pass
            elif (moveDir == "Backwards"):
                self.v2Pos -= self.v2Vel
                pass
            #self.v2Pos += self.v2Vel
            self.rect.center = self.v2Pos

            self.rect = self.image.get_rect()
            self.rect.center = (self.v2Pos.x, self.v2Pos.y)

logHandler.createLog("Initialized Warship handler...")