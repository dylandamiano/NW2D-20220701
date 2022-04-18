'''
    This module (gameCalculations.py) will handle player-based movement.

    For this module, we are going to utilize Vector2, which is a representation of
    Vectors and Points given on the their respective X and Y axis.
'''

import pygame
import math
import warshipClonkses
import playerClasses
import logHandler
import projectileClasses
import credit_handler
import computer_movement
import spilled_oil

import random

import time

from pygame.locals import *

# Defines map borders by using their coordinate position [x or y]
mapBorders = {
    "LEFT": 0 + 20,
    "RIGHT": 900 - 20,
    "TOP": 0 + 20,
    "BOTTOM": 900 - 20
}


# Defines the calculations for determining where the terrain is **** NEEDS TO BE DONE ****
terrainBorder = {

    # First value is "m", next value is "b." M is for slope and B is for y-intercept
    # Y indicates an f(x) equation whereas X will indicate an equation that is not a function
    # As far as "X" goes, the value that follows is the x location on the cartesian plane
    
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

    "ISLAND_Two": {
        "LINE1": ["y", 5, 5 * -500 + 800], # For "b" we're basically multiplying everything down to where it is not an "x"
        "LINE2": ["y", (2/3), (2/3) * -520 + 760],
        "LINE3": ["x", 520],
        "LINE4": ["y", -1, -1 * -520 + 720],
        "LINE5": ["y", (1/2), (1/2) * -560 + 680],
        "LINE6": ["y", (-2/3), (-2/3) * -700 + 700],
        "LINE7": ["x", 760],
        "LINE8": ["y", (-1.5), (-1.5) * -760 + 580],
        "LINE9": ["y", (-1/5), (-1/5) * -800 + 520]
    },

    "ISLAND_Three": {
        "LINE1": ["y", (-46/129), (-46/129) * 0 + 345],
        "LINE2": ["y", (-14/11), (-14/11) * -129 + 299],
        "LINE3": ["y", (-83/22), (-83/22) * -151 + 271],
        "LINE4": ["y", (-10/21), (-10/21) * -173 + 188],
        "LINE5": ["y", (20/71), (20/71) * -194 + 178],
        "LINE6": ["y", (-18/101), (-18/101) * -265 + 198],
        "LINE7": ["y", (40/57), (40/57) * -366 + 180],
        "LINE8": ["y", 680],
        "LINE9": ["y", (-20/57), (-20/57) * -486 + 220],
        "LINE10": ["y", (-57/55), (-57/55) * -543 + 200],
        "LINE11": ["y", (-3/8), (-3/8) * -598 + 143],
        "LINE12": ["y", (-18/11), (-18/11) * -686 + 110],
        "LINE13": ["y", (-56/17), (-56/17) * -719 + 56],
    },
    
}

def linearEquation(m, b, x): # DESMOS -> PYGAME, TO MAKE IT RELATIVE TO PYGAME, SUBTRACT 900 - (RETURN VAL)
    return 900 - ( (m * x) + b )

# Will handle the movement of the Ship/Sprite itself, needs some minor touch up
def move(x, y, character, direction):
    character.setLocation(direction)

def rotateChar(character, direction):
    character.setRotation(direction)

def check_ai(character):
    if character.owner.AI == True:
        character.owner.last_move = time.time()
        character.owner.last_rotate = time.time()

        rot_dir = random.randint(0, 1)

        if rot_dir == 1:
            pass

        if character.owner.move_direction == 1:
            character.owner.move_direction = -1
            character.owner.reverse = True
        elif character.owner.move_direction == -1:
            character.owner.move_direction = 1
            character.owner.reverse = False

def checkIslandBorders(character, moveDir):
    
    nextX = 0
    nextY = 0

    if moveDir == "Forward":
            nextX = (character.v2Pos + character.v2Vel).x
            nextY = (character.v2Pos + character.v2Vel).y
    elif moveDir == "Backwards":
            nextX = (character.v2Pos - character.v2Vel).x
            nextY = (character.v2Pos - character.v2Vel).y

    #print(nextX, nextY)

    if character.owner.type == "sea":
        if (nextX <= 100) and (nextY < 20) and (nextY >= 0):
            #print("<= bounds")
            move(0, 0, character, moveDir)
        elif (nextX > 100) and (nextX < 380) and (nextY > 0) and (nextY < 180): # ISLAND ONE, REGIONAL DEFINITIONS
            #print("Within Island One!")
            if (nextX > 100) and (nextX < 120) and (nextY < 20) and (nextY > 0): # REGION 1, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE1"][1], terrainBorder["ISLAND_One"]["LINE1"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX < 120) and (nextY < 40) and (nextY > 20): # REGION 2, LEFT
                #print("Left of bounds!")
                move(0, 0, character, moveDir)    
            elif (nextX > 100) and (nextX < 120) and (nextY > 40) and (nextY < 90): # REGION 3, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_One"]["LINE3"][1], terrainBorder["ISLAND_One"]["LINE3"][2], nextX)):
                    #print("Above bounds")
                    move(0, 0, character, moveDir)  
                else:
                    check_ai(character)
            elif (nextX > 100) and (nextX < 111) and (nextY > 90) and (nextY < 109): # Region 4, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE4"][1], terrainBorder["ISLAND_One"]["LINE4"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir) 
                else:
                    check_ai(character)
            elif (nextX > 111) and (nextX < 155) and (nextY > 109) and (nextY < 116): # Region 5, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE5"][1], terrainBorder["ISLAND_One"]["LINE5"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 155) and (nextX < 223) and (nextY > 116) and (nextY < 181): # Region 6, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE6"][1], terrainBorder["ISLAND_One"]["LINE6"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 223) and (nextX < 265) and (nextY > 181): # Region 7, UNDER
                #print("Below bounds")
                move(0, 0, character, moveDir)
            elif (nextX > 265) and (nextX < 313) and (nextY < 181) and (nextY > 154): # Region 8, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE8"][1], terrainBorder["ISLAND_One"]["LINE8"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 313) and (nextX < 333) and (nextY < 154) and (nextY > 117): # Region 9, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE9"][1], terrainBorder["ISLAND_One"]["LINE9"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 333) and (nextX < 351) and (nextY < 117) and (nextY > 72): # Region 10, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE10"][1], terrainBorder["ISLAND_One"]["LINE10"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 351) and (nextX < 380) and (nextY < 72) and (nextY > 48): # Region 11, UNDER
                if (nextY > linearEquation(terrainBorder["ISLAND_One"]["LINE11"][1], terrainBorder["ISLAND_One"]["LINE11"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX >= 380) and (nextY <= 48) and (nextY >= 0): # Region 12, RIGHT
                #print("Right of bounds!")
                move(0, 0, character, moveDir)
            elif (nextX >= 100) and (nextX <= 111) and (nextY >= 109): # BOX ONE
                #print("IN SUB-REGION 1")
                move(0, 0, character, moveDir)
            elif (nextX >= 111) and (nextX < 155) and (nextY >= 116): # BOX TWO
                #print("IN SUB-REGION 2")
                move(0, 0, character, moveDir)
            elif (nextX >= 313) and (nextX < 333) and (nextY >= 154): # BOX THREE
                #print("IN SUB-REGION 3")
                move(0, 0, character, moveDir)
            elif (nextX >= 333) and (nextX < 351) and (nextY >= 116): # BOX FOUR
                #print("IN SUB-REGION 4")
                move(0, 0, character, moveDir)
            elif (nextX >= 351) and (nextX < 380) and (nextY >= 72): # BOX FIVE
                #print("IN SUB-REGION 5")
                move(0, 0, character, moveDir)

        elif (nextX >= 520) and (nextX <= 900) and (nextY >= 0) and (nextY <= 400): # ISLAND TWO, REGIONAL DEFINITIONS
            #print("Within Island TWO")
            if (nextX > 580) and (nextX < 600) and (nextY > 0) and (nextY < 100): # REGION 1, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Two"]["LINE1"][1], terrainBorder["ISLAND_Two"]["LINE1"][2], nextX)):
                    #print("Above bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 520) and (nextX < 580) and (nextY > 100) and (nextY < 140): # REGION 2, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Two"]["LINE2"][1], terrainBorder["ISLAND_Two"]["LINE2"][2], nextX)):
                    #print("Above bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX < 520) and (nextY > 140) and (nextY < 180): # REGION 3, LEFT
                #print("Left of bounds")
                move(0, 0, character, moveDir)
            elif (nextX > 520) and (nextX < 560) and (nextY > 180) and (nextY < 220): # REGION 4, BELOW
                if (nextY > linearEquation(terrainBorder["ISLAND_Two"]["LINE4"][1], terrainBorder["ISLAND_Two"]["LINE4"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 560) and (nextX < 700) and (nextY > 200) and (nextY < 220): # REGION 5, BELOW
                if (nextY > linearEquation(terrainBorder["ISLAND_Two"]["LINE5"][1], terrainBorder["ISLAND_Two"]["LINE5"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 700) and (nextX < 760) and (nextY > 200) and (nextY < 240): # REGION 6, BELOW
                if (nextY > linearEquation(terrainBorder["ISLAND_Two"]["LINE6"][1], terrainBorder["ISLAND_Two"]["LINE6"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX < 760) and (nextY > 240) and (nextY < 320): # BOX THREE
                #print("IN SUB-REGION 3")
                move(0, 0, character, moveDir)
            elif (nextX > 760) and (nextX < 800) and (nextY > 320) and (nextY < 380): # REGION 8, BELOW
                if (nextY > linearEquation(terrainBorder["ISLAND_Two"]["LINE8"][1], terrainBorder["ISLAND_Two"]["LINE8"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 800) and (nextX < 900) and (nextY > 380) and (nextY < 400): # REGION 9, BELOW
                if (nextY > linearEquation(terrainBorder["ISLAND_Two"]["LINE9"][1], terrainBorder["ISLAND_Two"]["LINE9"][2], nextX)):
                    #print("Below bounds")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 520) and (nextX < 580) and (nextY > 0) and (nextY < 100): # BOX ONE
                #print("IN SUB-REGION 1")
                move(0, 0, character, moveDir)
            elif (nextX > 520) and (nextX < 700) and (nextY > 220) and (nextY < 240): # BOX TWO
                #print("IN SUB-REGION 2")
                move(0, 0, character, moveDir)
            elif (nextX > 520) and (nextX < 760) and (nextY > 320) and (nextY < 380): # BOX FOUR
                #print("IN SUB-REGION 4")
                move(0, 0, character, moveDir)
            elif (nextX > 520) and (nextX < 800) and (nextY > 380) and (nextY < 400): # BOX FIVE
                #print("IN SUB-REGION 5")
                move(0, 0, character, moveDir)
            '''
            else:
                print("reverse!")
                print(character.owner.AI)
                if character.owner.AI == True:
                    move(0,0, character, "Backwards")
                    print("reverse!")
                    return "reverse"
            '''

        elif (nextX >= 0) and (nextX <= 736) and (nextY >= 555) and (nextY <= 900): # ISLAND THREE, REGIONS
            if (nextX > 0) and (nextX < 129) and (nextY > 555) and (nextY < 601): # REGION 1, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE1"][1], terrainBorder["ISLAND_Three"]["LINE1"][2], nextX)):
                    #print("Above bounds1")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 129) and (nextX < 151) and (nextY > 601) and (nextY < 629): # REGION 2, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE2"][1], terrainBorder["ISLAND_Three"]["LINE2"][2], nextX)):
                    #print("Above bounds 2")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 151) and (nextX < 173) and (nextY > 629) and (nextY < 712): # REGION 3, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE3"][1], terrainBorder["ISLAND_Three"]["LINE3"][2], nextX)):
                    #print("Above bounds 3")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 173) and (nextX < 194) and (nextY > 712) and (nextY < 722): # REGION 4, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE4"][1], terrainBorder["ISLAND_Three"]["LINE4"][2], nextX)):
                    #print("Above bounds 4")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 194) and (nextX < 265) and (nextY > 702) and (nextY < 722): # REGION 5, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE5"][1], terrainBorder["ISLAND_Three"]["LINE5"][2], nextX)):
                    #print("Above bounds 5")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 265) and (nextX < 366) and (nextY > 702) and (nextY < 720): # REGION 6, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE6"][1], terrainBorder["ISLAND_Three"]["LINE6"][2], nextX)):
                    #print("Above bounds 6")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 366) and (nextX < 423) and (nextY > 680) and (nextY < 720): # REGION 7, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE7"][1], terrainBorder["ISLAND_Three"]["LINE7"][2], nextX)):
                    #print("Above bounds 7")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 487) and (nextX < 543) and (nextY > 680) and (nextY < 700): # REGION 9, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE9"][1], terrainBorder["ISLAND_Three"]["LINE9"][2], nextX)):
                    #print("Above bounds 9")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 543) and (nextX < 598) and (nextY > 700) and (nextY < 757): # REGION 10, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE10"][1], terrainBorder["ISLAND_Three"]["LINE10"][2], nextX)):
                    #print("Above bounds 10")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 598) and (nextX < 686) and (nextY > 757) and (nextY < 790): # REGION 11, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE11"][1], terrainBorder["ISLAND_Three"]["LINE11"][2], nextX)):
                    #print("Above bounds 11")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 686) and (nextX < 719) and (nextY > 790) and (nextY < 844): # REGION 12, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE12"][1], terrainBorder["ISLAND_Three"]["LINE12"][2], nextX)):
                    #print("Above bounds 12")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX > 719) and (nextX < 736) and (nextY > 844) and (nextY < 900): # REGION 13, ABOVE
                if (nextY < linearEquation(terrainBorder["ISLAND_Three"]["LINE13"][1], terrainBorder["ISLAND_Three"]["LINE13"][2], nextX)):
                    #print("Above bounds 13")
                    move(0, 0, character, moveDir)
                else:
                    check_ai(character)
            elif (nextX >= 129) and (nextX <= 151) and (nextY <= 900-299) and (nextY >= 900-345):
                #print("IN SUB-REGION 1")
                move(0, 0, character, moveDir)
            elif (nextX >= 151) and (nextX <= 173) and (nextY <= 900-271) and (nextY >= 900-345):
                #print("IN SUB-REGION 2")
                move(0, 0, character, moveDir)
            elif (nextX >= 173) and (nextX <= 194) and (nextY <= 900-188) and (nextY >= 900-345):
                #print("IN SUB-REGION 3")
                move(0, 0, character, moveDir)
            elif (nextX >= 194) and (nextX <= 366) and (nextY <= 900-198) and (nextY >= 900-345):
                #print("IN SUB-REGION 4")
                move(0, 0, character, moveDir)
            elif (nextX >= 366) and (nextX <= 543) and (nextY < 900-220) and (nextY >= 900-345): # EXCP.
                #print("IN SUB-REGION 5")
                move(0, 0, character, moveDir)
            elif (nextX >= 543) and (nextX <= 598) and (nextY <= 900-200) and (nextY >= 900-345):
                #print("IN SUB-REGION 6")
                move(0, 0, character, moveDir)
            elif (nextX >= 598) and (nextX <= 686) and (nextY <= 900-143) and (nextY >= 900-345):
                #print("IN SUB-REGION 7")
                move(0, 0, character, moveDir)
            elif (nextX >= 686) and (nextX <= 719) and (nextY <= 900-110) and (nextY >= 900-345):
                #print("IN SUB-REGION 8")
                move(0, 0, character, moveDir)
            elif (nextX >= 719) and (nextX <= 736) and (nextY <= 900-56) and (nextY >= 900-345):
                #print("IN SUB-REGION 9")
                move(0, 0, character, moveDir)
            '''
            else:
                print("reverse!")
                print(character.owner.AI)
                if character.owner.AI == True:
                    move(0,0, character, "Backwards")
                    return "reverse"
            '''
        else:
            #print("Else executed!")
            move(0, 0, character, moveDir)
    else:
        move(0, 0, character, moveDir)
        

# Will check to see if the Ship/Sprite is moving within the boundaries, it if is not within bounds then the function will not fire
def checkBorder(character, moveDir):
    nextX = 0
    nextY = 0

    if moveDir == "Forward":
            nextX = (character.v2Pos + character.v2Vel).x
            nextY = (character.v2Pos + character.v2Vel).y
    elif moveDir == "Backwards":
            nextX = (character.v2Pos - character.v2Vel).x
            nextY = (character.v2Pos - character.v2Vel).y

    ##print(nextX, nextY) # Intended for debugging

    if ( ( nextX > (mapBorders["LEFT"] )) and ( nextX < (mapBorders["RIGHT"] ) ) and ( nextY > (mapBorders["TOP"] ) ) and ( nextY < (mapBorders["BOTTOM"] ) )): # Handles the horizontal movement of the Ship
        checkIslandBorders(character, moveDir);
    else:
        check_ai(character)
            

    ##print(character.getLocation("x"), character.getLocation("y"))

# Detects which key was/is being pressed
def key_PressedEvent(eventFired, character = None):

    # Print functions below intended for debugging
    ##print("Key pressed, running event!")
    ##print(eventFired.key)
    ##print(character.owner)

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

'''

    The player's coordinate system for projectile casting will be broken into
    four primary quadrants.

    However, while the need for 8 sub-quadrants currently does not exist, I am going to
    make room for it incase there is a need for it in the future, that way the work is already done.

'''
def get_angle(origin, mousePos):
    logHandler.createLog("MOUSEPOS: " + str(mousePos))
    slope = None
    theta_rad = None
    theta_deg = None

    try:
        change_y =  origin[1] - mousePos[1]
        change_x = origin[0] - mousePos[0]

        theta_rad = math.atan(change_y / change_x)
        theta_deg = math.degrees(theta_rad) # Or (theta_rad) * (180/pi)
    except ZeroDivisionError:
        #print("Cannot divide by zero!")

        # RETURN TO!
        pass

    logHandler.createLog("SLOPE CALC:" + str(slope))
    # referenceY = linearEquation(1, (origin[0] + origin[1]), mousePos[0]) -- SOMETHING LIKE THIS!

    if (mousePos[0] > origin[0]) and (mousePos[1] < origin[1]): # If the player is aiming mouse RIGHT of CENTER, QUADRANT 1
        if mousePos[1] < 900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Above!")
            return 270 - theta_deg
        elif mousePos[1] > 900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Below!")
            return 270 - theta_deg

    elif (mousePos[0] < origin[0]) and (mousePos[1] < origin[1]): # If the player is aiming mouse LEFT of CENTER, QUADRANT 2
        if mousePos[1] < 900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Above!")
            return 90 - theta_deg
        elif mousePos[1] > 900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Below!")
            return 90 - theta_deg

    elif (mousePos[0] < origin[0]) and (mousePos[1] > origin[1]): # If the player is aiming mouse LEFT of CENTER, QUADRANT 3
        if mousePos[1] < 900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Above!")
            return 90 + abs(theta_deg)
        elif mousePos[1] > 900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(-1, (origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Below!")
            return 90 + abs(theta_deg)

    elif (mousePos[0] > origin[0]) and (mousePos[1] > origin[1]): # If the player is aiming mouse RIGHT of CENTER, QUADRANT 4
        if mousePos[1] < 900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Above!")
            return 270 - theta_deg
        elif mousePos[1] > 900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0]):
            logHandler.createLog("LIN CALC FIN: " + str(900 - linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("LIN CALC RAW: " + str(linearEquation(1, (-origin[0] + origin[1]), mousePos[0])))
            logHandler.createLog("Below!")
            return 270 - theta_deg

    elif (mousePos[0] == origin[0]) and (mousePos[1] < origin[1]):
        return 0
    elif (mousePos[0] == origin[0]) and (mousePos[1] > origin[1]):
        return 180
    elif (mousePos[0] <= origin[0]) and (mousePos[1] == origin[1]):
        return 90
    elif (mousePos[0] >= origin[0]) and (mousePos[1] == origin[1]):
        return 270

def cleanup_projectiles(projectiles):
    to_remove = []

    for i in range(0, len(projectiles)):
        if projectiles[i].remove == True:
            to_remove.append(i)

    for rm in reversed(to_remove):
        del projectileClasses.activeProjectiles[rm]

def cleanup_npc(entities):
    to_remove = []

    for i in range(0, len(entities)):
        if entities[i].ship.health <= 0:
            to_remove.append(i)

            if (entities[i].player_owned == False):
                credit_handler.destroyed_ships += 1
            if (entities[i].player_owned == True) and (entities[i].AI == True):
                computer_movement.friendly_count -= 1


    for rm in reversed(to_remove):
        spilled_oil.create_spill(computer_movement.active_entities[rm])
        del computer_movement.active_entities[rm]

def garbage_collect(projectiles, entities):
    cleanup_npc(entities)
    cleanup_projectiles(projectiles)

def checkCollisions(entity_list, player, projectiles): # Tends to degrade performance when all sprites are in one spot, we have to avoid this by spreading them out
    combined_entities = [player]
    toDelete = []

    for entity in entity_list:
        combined_entities.append(entity)

    for entity in combined_entities:
        for other in combined_entities:
            if (entity.ship.rect.colliderect(other.ship.rect) == True) and (other.username != entity.username):
                if (entity.type != "air") and (other.type != "air") and (( (entity.player_owned == True) and (other.player_owned == False) ) or ( (entity.player_owned == False) and (other.player_owned == True) )):
                    entity.ship.health = 0
                    other.ship.health = 0
                    logHandler.createLog(entity.username + " and " + other.username + " have collided!")

    for projectile in projectiles:
        for entity in combined_entities:
            if (projectile.rect.colliderect(entity.ship.rect) == True) and (projectile.owner.username != entity.username):
                if (projectile.owner.player_owned == True) and (entity.player_owned == True):
                    pass
                elif (projectile.owner.player_owned == False) and (entity.player_owned == False):
                    pass
                else:
                    entity.ship.health -= projectile.damage
                    projectile.remove = True
                    logHandler.createLog("Projectile has hit!")

def render_health(surface, player):

    player_pos = player.ship.v2Pos
    player_health = player.ship.health / player.ship.max_health

    pygame.draw.rect(surface, (255, 0, 0), (player_pos.x - 11, player_pos.y + 25, 25, 3))
    pygame.draw.rect(surface, (0, 255, 0), (player_pos.x - 11, player_pos.y + 25, 25 * player_health, 3))

    for entity in computer_movement.active_entities:
        entity_pos = entity.ship.v2Pos
        entity_health = entity.ship.health / entity.ship.max_health

        pygame.draw.rect(surface, (255, 0, 0), (entity_pos.x - 11, entity_pos.y + 25, 25, 3))
        pygame.draw.rect(surface, (0, 255, 0), (entity_pos.x - 11, entity_pos.y + 25, 25 * entity_health, 3))

def render_friendly(surface, player):
    player_pos = player.ship.v2Pos

    pygame.draw.rect(surface, (0, 0, 255), (player_pos.x - 11 + 25/3, player_pos.y - 25, 25/2, 3))

    for entity in computer_movement.active_entities:
        if entity.player_owned == True:
            entity_pos = entity.ship.v2Pos

            pygame.draw.rect(surface, (0, 0, 255), (entity_pos.x - 11 + 25/3, entity_pos.y - 25, 25/2, 3))