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

    # First value is "m", next value is "b." M is for slope and B is for y-intercept
    # Y indicates an f(x) equation whereas X will indicate an equation that is not a function
    "ISLAND_One": {
        "LINE1": ["y", -1, 1000],
        "LINE2": ["x", 120],
        "LINE3": ["y", (50/20), 560],
        "LINE4": ["y", (-19/11), (1900/11) + 810],
        "LINE5": ["y", (-7/44), (-7/44) * -111 + 791]
        #"LINE6": [""]
    },
    
}

def linearEquation(m, b, x):
    return 900 - ( (m * x) + b )

def rangeBetween(y1, y2):
    pass

# Will handle the movement of the Ship/Sprite itself, needs some minor touch up
def move(x, y, character, direction):
    character.setLocation(direction)

def rotateChar(character, direction):
    character.setRotation(direction)

def checkIslandBorders(character, moveDir):
    nextX = (character.v2Pos + character.v2Vel).x
    nextY = (character.v2Pos + character.v2Vel).y

    if (nextX > 100) and (nextX < 120) and (nextY < 20) and (nextY > 0):
        print(linearEquation(terrainBorder["ISLAND_One"]["LINE1"][1], terrainBorder["ISLAND_One"]["LINE1"][2], nextX))
        if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE1"][1], terrainBorder["ISLAND_One"]["LINE1"][2], nextX)):
            print("Below bounds")
            return True
    elif (nextX < 120) and (nextY < 40) and (nextY > 20):
        pass
    elif (nextX > 100) and (nextX < 120) and (nextY < 90) and (nextY > 40):
        if (nextY < linearEquation(terrainBorder["ISLAND_One"]["LINE3"][1], terrainBorder["ISLAND_One"]["LINE3"][2], nextX)):
            print("Above the line!")
            return True

# Will check to see if the Ship/Sprite is moving within the boundaries, it if is not within bounds then the function will not fire
def checkBorder(character, moveDir):
    nextX = (character.v2Pos + character.v2Vel).x
    nextY = (character.v2Pos + character.v2Vel).y

    checkIslandBorders(character, moveDir);

    #print(nextX, nextY) # Intended for debugging

    if ( ( nextX > (mapBorders["LEFT"] )) and ( nextX < (mapBorders["RIGHT"] ) ) ): # Handles the horizontal movement of the Ship
        if ( ( nextY > (mapBorders["TOP"] ) ) and ( nextY < (mapBorders["BOTTOM"] ) ) ): # Handles the vertical movement of the Ship
            #print(( nextY > (mapBorders["TOP"] ) ) and ( nextY < (mapBorders["BOTTOM"] ) ))
            move(0, 0, character, moveDir)

    #print(character.getLocation("x"), character.getLocation("y"))

# Detects which key was/is being pressed
def key_PressedEvent(eventFired, character = None):

    # Print functions below intended for debugging
    #print("Key pressed, running event!")
    #print(eventFired.key)
    #print(character.owner)

    # Primary movement keybinds initially intended for Player1.
    if (eventFired.key == pygame.K_w):
        checkBorder(character, "Forward")
    elif (eventFired.key == pygame.K_s):
        checkBorder(character, "Backwards")
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
        checkBorder(character, "Forward")
    if (keyHeld == "S"):
        checkBorder(character, "Backwards")
    if (keyHeld == "Q"):
        rotateChar(character, "Left")
    if (keyHeld == "E"):
        rotateChar(character, "Right")