import playerClasses
import pygame

import gameSettings

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
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)

        self.localOrientation = 0
        self.vec2 = pygame.math.Vector2

        self.v2Pos = self.vec2(450, 450)
        self.v2Vel = self.vec2(0, -.5)

        self.v2Rot = 0

        self.owner = player.username # will include the player's object
        self.health = 100
        self.smoked = True
        self.shipName = None

        self.TlastMove = 0

        self.shipCoords = {
            "x": self.v2Pos.x,
            "y": self.v2Pos.y,
            }

    def shipStatus(self):
        print(self.health)

    def getLocation(self, req):
        if (req == "x"):
            return self.shipCoords["x"]
        elif (req == "y"):
            return self.shipCoords["y"]

class Battleship(Ship):
    def __init__(self, player):
        super().__init__(player)
        self.shipName == "Battleship"

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        
        pass # Will be defined in more detail later once I get the core program setup

    def getHealth(self):
        print("Your health is at " + self.health + "%")

class Frigate(Ship):
    def __init__(self, player):
        super().__init__(player)

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        pass # Will be defined in more detail later once I get the core program setup

class Destroyer(Ship):
    def __init__(self, player):
        super().__init__(player)

    def fireCannons():
        print("Firing cannons!")

    def takeDamage(self, attackingShip):
        pass # Will be defined in more detail later once I get the core program setup

class Carrier(Ship):
    def __init__(self, player):
        super().__init__(player)
        self.airWing = 5

        self.imageRestore = "Ships\\CarrierConcept.png"

        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.scale(self.image, (20, 41))

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def test(self):
        print("Yes")


    def setRotation(self, rotDir):
        if (self.localOrientation <= 0):
            self.localOrientation = 360
        elif (self.localOrientation >= 360):
            self.localOrientation = 0

        if (rotDir == "Left"):
            self.v2Vel.rotate_ip(-1)
            self.localOrientation += 1
        elif (rotDir == "Right"):
            self.v2Vel.rotate_ip(1)
            self.localOrientation -= 1

        #print(self.localOrientation)

        self.image = pygame.image.load(self.imageRestore)
        self.image = pygame.transform.rotate(self.image, self.localOrientation)

        self.rect = self.image.get_rect()
        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

        self.rect.center = (self.v2Pos.x, self.v2Pos.y)

    def setLocation(self, moveDir):
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