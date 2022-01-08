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

        self.orientation = 0

        self.vec2 = pygame.math.Vector2

        self.v2Pos = self.vec2(450, 450)
        self.v2Rot = self.vec2(0, 0)
        self.v2Vel = self.vec2(0, 0)

        self.owner = player.username # will include the player's object
        self.health = 100
        self.smoked = True
        self.shipName = None

        self.TlastMove = 0

        self.shipCoords = {
            "x": 450,
            "y": 450,
            }

    def shipStatus(self):
        print(self.health)

    def getLocation(self, req):
        if (req == "x"):
            return self.shipCoords["x"]
        elif (req == "y"):
            return self.shipCoords["y"]

    def setLocation(self, posX, posY):
        self.shipCoords["x"] += posX
        self.shipCoords["y"] += posY

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