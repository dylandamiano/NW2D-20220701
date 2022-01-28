'''
    This module (gameCalculations.py) will handle player-based movement.

    For this module, we are going to utilize Vector2, which is a representation of
    Vectors and Points given on the their respective X and Y axis.
'''

import pygame
import warshipClonkses
import playerClasses

from pygame.locals import *

# Defines map borders by using their coordinate position [x or y]
mapBorders = {
    "LEFT": 0,
    "RIGHT": 900,
    "TOP": 0,
    "BOTTOM": 900
}

# Defines the calculations for determining where the terrain is **** NEEDS TO BE DONE ****
terrainBorder = {
    
}

# Will handle the movement of the Ship/Sprite itself, needs some minor touch up
def move(x, y, character, direction):
    character.setLocation(direction)

def rotateChar(character, direction):
    character.setRotation(direction)

# Will check to see if the Ship/Sprite is moving within the boundaries, it if is not within bounds then the function will not fire
def checkBorder(nextX, nextY, incrX, incrY, character, moveDir):
    if ( ( (nextX + incrX) > (mapBorders["LEFT"] ) ) and ( (nextX + incrX) <= (mapBorders["RIGHT"] ) ) ): # Handles the horizontal movement of the Ship
        #print("moving player...")
        move(incrX, 0, character, moveDir)
    elif ( ( (nextX + incrX) >= (mapBorders["LEFT"] ) ) and ( (nextX + incrX) < (mapBorders["RIGHT"]) ) ): # Handles the horizontal movement of the Ship
        #print("moving player...")
        move(incrX, 0, character, moveDir)

    if ( ( (nextY + incrY ) > (mapBorders["TOP"] ) ) and ( (nextY + incrY ) <= (mapBorders["BOTTOM"] ) ) ): # Handles the vertical movement of the Ship
            #print("moving player...")
            move(0, incrY, character, moveDir)
    elif ( ( (nextY + incrY ) >= (mapBorders["TOP"] ) ) and ( (nextY + incrY ) < (mapBorders["BOTTOM"]) ) ): # Handles the vertical movement of the Ship
            #print("moving player...")
            move(0, incrY, character, moveDir)

    #print(character.getLocation("x"), character.getLocation("y"))

# Detects which key was/is being pressed
def key_PressedEvent(eventFired, character = None):

    # Print functions below intended for debugging
    #print("Key pressed, running event!")
    #print(eventFired.key)
    #print(character.owner)

    # Primary movement keybinds initially intended for Player1.
    if (eventFired.key == pygame.K_w):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, -10, character, "Forward")
    elif (eventFired.key == pygame.K_s):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, 10, character, "Backwards")
    elif (eventFired.key == pygame.K_q):
        rotateChar(character, "Left")
    elif (eventFired.key == pygame.K_e):
        rotateChar(character, "Right")

    # Will be setup for a second player in the future, not at this moment though. Will currently be 'alternative keybinds' for the time being
    if (eventFired.key == pygame.K_UP):
         checkBorder(character.getLocation("x"), character.getLocation("y"), 0, -10, character, "Forward")
    elif (eventFired.key == pygame.K_DOWN):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, 10, character, "Backwards")
    elif (eventFired.key == pygame.K_RALT):
        rotateChar(character, "Left")
    elif (eventFired.key == pygame.K_RCTRL):
        rotateChar(character, "Right")

def key_held(keyHeld, character):
    if (keyHeld == "W"):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, -10, character, "Forward")
    if (keyHeld == "S"):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, 10, character, "Backwards")
    if (keyHeld == "Q"):
        pass
    if (keyHeld == "E"):
        pass