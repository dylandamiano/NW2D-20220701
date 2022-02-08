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
        "LINE5": ["y", (-7/44), (-7/44) * -111 + 791],
        "LINE6": ["y", (-65/80), (-65/80) * -155 + 784],
        "LINE7": ["y", 719],
        "LINE8": ["y", (9/16), (9/16) * -265 + 719],
        "LINE9": ["y", (37/20), (37/20) * -313 + 746],
        "LINE10": ["y", (5/2), (5/2) * -351 + 828],
        "LINE11": ["y", (24/29), (24/29) * -380 + 852],
        "LINE12": ["x", 380]
    },

    "ISLAND_Two": {},
    
}

def linearEquation(m, b, x):
    return 900 - ( (m * x) + b )

# Will handle the movement of the Ship/Sprite itself, needs some minor touch up
def move(x, y, character, direction):
    character.setLocation(direction)

def rotateChar(character, direction):
    character.setRotation(direction)

def checkIslandBorders(character, moveDir):
    
    nextX = (character.v2Pos + character.v2Vel).x
    nextY = (character.v2Pos + character.v2Vel).y
    print(nextX, nextY)

    if (nextX > 100) and (nextX < 380) and (nextY > 0) and (nextY < 180):
        print("Within Island One!")
        if (nextX > 100) and (nextX < 120) and (nextY < 20) and (nextY > 0): # REGION 1, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE1"][1], terrainBorder["ISLAND_One"]["LINE1"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX < 120) and (nextY < 40) and (nextY > 20): # REGION 2, LEFT
            print("Left of bounds!")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 100) and (nextX < 120) and (nextY > 40) and (nextY < 90): # REGION 3, ABOVE
            if (nextY < linearEquation(terrainBorder["ISLAND_One"]["LINE3"][1], terrainBorder["ISLAND_One"]["LINE3"][2], nextX)):
                print("Above bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 100) and (nextX < 111) and (nextY > 90) and (nextY < 109): # Region 4, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE4"][1], terrainBorder["ISLAND_One"]["LINE4"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 111) and (nextX < 155) and (nextY > 109) and (nextY < 116): # Region 5, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE5"][1], terrainBorder["ISLAND_One"]["LINE5"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 155) and (nextX < 223) and (nextY > 116) and (nextY < 181): # Region 6, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE6"][1], terrainBorder["ISLAND_One"]["LINE6"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 223) and (nextX < 265) and (nextY > 181): # Region 7, UNDER
            print("Below bounds")
            move(0, 0, character, moveDir)
        elif (nextX > 265) and (nextX < 313) and (nextY < 181) and (nextY > 154): # Region 8, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE8"][1], terrainBorder["ISLAND_One"]["LINE8"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 313) and (nextX < 333) and (nextY < 154) and (nextY > 117): # Region 9, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE9"][1], terrainBorder["ISLAND_One"]["LINE9"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 333) and (nextX < 351) and (nextY < 117) and (nextY > 72): # Region 10, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE10"][1], terrainBorder["ISLAND_One"]["LINE10"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 351) and (nextX < 380) and (nextY < 72) and (nextY > 48): # Region 11, UNDER
            if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE11"][1], terrainBorder["ISLAND_One"]["LINE11"][2], nextX)):
                print("Below bounds")
                move(0, 0, character, moveDir)
                pass
        elif (nextX > 380) and (nextY < 48) and (nextY > 0): # Region 12, RIGHT
            print("Right of bounds!")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 100) and (nextX < 111) and (nextY > 109): # BOX ONE
            print("IN SUB-REGION 1")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 111) and (nextX < 155) and (nextY > 116): # BOX TWO
            print("IN SUB-REGION 2")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 313) and (nextX < 333) and (nextY > 154): # BOX THREE
            print("IN SUB-REGION 3")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 333) and (nextX < 351) and (nextY > 116): # BOX FOUR
            print("IN SUB-REGION 4")
            move(0, 0, character, moveDir)
            pass
        elif (nextX > 351) and (nextX < 380) and (nextY > 72): # BOX FIVE
            print("IN SUB-REGION 5")
            move(0, 0, character, moveDir)
    else:
        print("Else executed!")
        move(0, 0, character, moveDir)
        

# Will check to see if the Ship/Sprite is moving within the boundaries, it if is not within bounds then the function will not fire
def checkBorder(character, moveDir):
    nextX = (character.v2Pos + character.v2Vel).x
    nextY = (character.v2Pos + character.v2Vel).y

    #print(nextX, nextY) # Intended for debugging

    if ( ( nextX > (mapBorders["LEFT"] )) and ( nextX < (mapBorders["RIGHT"] ) ) ): # Handles the horizontal movement of the Ship
        if ( ( nextY > (mapBorders["TOP"] ) ) and ( nextY < (mapBorders["BOTTOM"] ) ) ): # Handles the vertical movement of the Ship
            #print(( nextY > (mapBorders["TOP"] ) ) and ( nextY < (mapBorders["BOTTOM"] ) ))
            checkIslandBorders(character, moveDir);
            

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
    '''
    if (eventFired.key == pygame.K_UP):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, -10, character, "Forward")
    elif (eventFired.key == pygame.K_DOWN):
        checkBorder(character.getLocation("x"), character.getLocation("y"), 0, 10, character, "Backwards")
    elif (eventFired.key == pygame.K_RALT):
        rotateChar(character, "Left")
    elif (eventFired.key == pygame.K_RCTRL):
        rotateChar(character, "Right")
    '''

def key_held(keyHeld, character):
    if (keyHeld == "W"):
        checkBorder(character, "Forward")
    if (keyHeld == "S"):
        checkBorder(character, "Backwards")
    if (keyHeld == "Q"):
        rotateChar(character, "Left")
    if (keyHeld == "E"):
        rotateChar(character, "Right")