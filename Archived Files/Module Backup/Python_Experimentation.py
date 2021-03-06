'''
    NAVAL Warfare 2D

    Quick Overview:
        This game will be turn based and will allow up to 2 players to compete with AI based entities (up to 4 max for now)

'''


# Basic Module Initialization
import datetime
import math, random
import threading

import cairo
import logHandler as log

import time

import gameCalculations
import gameSettings
import graphicInterface

import pygame, sys
from pygame.locals import *

import projectileClasses

import warshipClonkses
import playerClasses

import os
from os import path


'''
    As you see below,
    we are calling the pygame framework and initializing it.

    To simplify:
        - The window is being created at a scale of 900 x 900 pixels (tall and wide)      - Wasky was here
        - Capping the framerate to 60 FPS to limit system resources
        - Setting the window title to inform the user on which one they have open
'''
log.createLog("Starting Naval Warfare 2D...")

pygame.init()

DISPLAYSURF = pygame.display.set_mode(size=(900,900))

size_x = 0
size_y = 0

DISPLAYSURF_PRI = pygame.Surface((size_x, size_y))
FPSClock = pygame.time.Clock()
FPS = 100

icon = "Graphics\\NW2DLogo.png"
icon_img = pygame.image.load(icon)

pygame.display.set_icon(icon_img)   

pygame.display.set_caption("NAVAL Warfare 2d")

'''
    Going on below:
        - The image for the map is being PLACED upon the screen at the scale defined in the previous commentary above.
        - The Player / AI character objects are being initialized
'''

mapInit = playerClasses.islandMap()

friendlyAI_1 = playerClasses.Player("AI Entity #1")
friendlyAI_1.createShip("Carrier")
friendlyAI_1.type = "sea"

log.createLog("Created Sprite for Player!")

'''
    The function below will do the following:
        - Create cloud objects
        - Set a movement interval for clouds after an "x" period of time
        - Randomize the location of said cloud in question
'''
# 937-776-9122
# 23hallg@gmail.com
a = 5
def createCloud():
    t = time.time()
    randBreak = math.floor(random.randrange(1, 10))
    #print(randBreak)

    if ( (t - gameSettings.cloudLast) >= randBreak):
        gameSettings.cloudLast = t

        sel = math.floor(random.randrange(0, len(gameSettings.cloudChart)))

        #print(sel)
        cloudObj = playerClasses.Cloud(sel, gameSettings.cloudDims, random.randrange(1, 4))
        cloudObj.createLocation()

        #DISPLAYSURF.blit(cloudObj.image, cloudObj.rect)
        gameSettings.activeClouds.insert(len(gameSettings.activeClouds) + 1, cloudObj)

'''
    As seen below:
        - The game loop is going to run infinitely until a certain criteria is met (in this case, the player will be required to close the game!)
        - Everything that is critical to the functionality of the game will be called in this loop such as moving characters (clouds, and other things alike) around the viewport.
'''

running = True
pause = True

# pygame.display.toggle_fullscreen()

#pygame.mixer.music.load('HaloMjolnirMix.mp3')
#pygame.mixer.music.play(-1)

def drawLogs():
    logHistory = log.getDisplayLog()


log.createLog("Finished initalizingw!")

def updateProjectiles():
    projectileClasses.updateProjectiles()

    for projectile in projectileClasses.activeProjectiles:
        DISPLAYSURF.blit(projectile.image, projectile.rect)

pregame = False

while running == True:

    if (pause == True) and (pregame == False):
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        
        DISPLAYSURF.blit(graphicInterface.mainMenu.image, graphicInterface.mainMenu.rect)

        #print(pause)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_m):
                    if (pause == True):
                        pause = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    gui_return = graphicInterface.checkMouseInput()

                    if gui_return == "PLAY":
                        pause = False
                    if gui_return == "STOP":
                        running = False
                        pygame.display.quit()

                        log.createLog("Naval Warfare 2D Closed...")
                        log.writeFile()

            if event.type == pygame.QUIT:
                    pause = True
                    running = False
                    pygame.display.quit()

            if event.type == pygame.KEYUP:
                    gameSettings.setKeyStatus(event, "UP")

                    #pygame.mouse.get_pos()
                    #pygame.draw.line(DISPLAYSURF,(0,0,255),(450,450),(0,0),5)

    if (pause == False) and (pregame == False):
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

        DISPLAYSURF.blit(mapInit.image, mapInit.rect)
        DISPLAYSURF.blit(friendlyAI_1.ship.image, friendlyAI_1.ship.rect)
        #pygame.draw.rect(DISPLAYSURF, (0, 0, 255), (125.2, 196.8, 309.1/2, 125.2/2))

        updateProjectiles()
       

        for i in range (0, math.floor(random.randrange(0, 5))):
            createCloud()

        #t = time.time()

        for x in range(0, len(gameSettings.activeClouds)):

            #if ((t - gameSettings.activeClouds[x].lastMove) >= gameSettings.activeClouds[x].moveInt):
                #gameSettings.activeClouds[x].lastMove = t
            gameSettings.activeClouds[x].rect.move_ip(gameSettings.activeClouds[x].moveSpeed, 0)
            gameSettings.activeClouds[x].posX += gameSettings.activeClouds[x].moveSpeed
            DISPLAYSURF.blit(gameSettings.activeClouds[x].image, gameSettings.activeClouds[x].rect)
                #pygame.draw.rect(DISPLAYSURF, "Blue", friendlyAI_1.ship.rect)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = True
                running = False

                log.createLog("Naval Warfare 2D Closed...")
                log.writeFile()

                pygame.display.quit()
            elif event.type == pygame.KEYDOWN:
                gameCalculations.key_PressedEvent(event, friendlyAI_1.ship)
                gameSettings.setKeyStatus(event, "DOWN")

                if (event.key == pygame.K_m):
                    if (pause == False):
                        pause = True
                        gameSettings.resetKeyStatus()

            elif event.type == pygame.KEYUP:
                gameSettings.setKeyStatus(event, "UP")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                angleGiven = gameCalculations.get_angle(friendlyAI_1.ship.v2Pos, mouse_pos)
                print("CALCULATED ANGLE OF THETA: " + str(angleGiven))
                print(friendlyAI_1.ship.localOrientation)

                pygame.draw.line(DISPLAYSURF,(0,0,255), mouse_pos, (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)
                projectileClasses.mouseFired(angleGiven, friendlyAI_1)
    
        for k in gameSettings.playerOneKeys:
            if (gameSettings.playerOneKeys[k] == True):
                if k == "W_Hold":
                    gameCalculations.key_held("W", friendlyAI_1.ship)
                elif k == "A_Hold":
                    gameCalculations.key_held("A", friendlyAI_1.ship)
                elif k == "S_Hold":
                    gameCalculations.key_held("S", friendlyAI_1.ship)
                elif k == "D_Hold":
                    gameCalculations.key_held("D", friendlyAI_1.ship)

                if k == "Q_Hold":
                    gameCalculations.key_held("Q", friendlyAI_1.ship)
                elif k == "E_Hold":
                    gameCalculations.key_held("E", friendlyAI_1.ship)

        gameSettings.checkClouds()

        pygame.draw.line(DISPLAYSURF,(255,0,0), (friendlyAI_1.ship.v2Pos.x + 900,friendlyAI_1.ship.v2Pos.y), (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)
        pygame.draw.line(DISPLAYSURF,(255,0,0), (friendlyAI_1.ship.v2Pos.x,friendlyAI_1.ship.v2Pos.y + 900), (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)
        pygame.draw.line(DISPLAYSURF,(255,0,0), (friendlyAI_1.ship.v2Pos.x,friendlyAI_1.ship.v2Pos.y - 900), (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)
        pygame.draw.line(DISPLAYSURF,(255,0,0), (friendlyAI_1.ship.v2Pos.x - 900,friendlyAI_1.ship.v2Pos.y), (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)

        pygame.draw.line(DISPLAYSURF,(255,0,0), (friendlyAI_1.ship.v2Pos.x + 900,friendlyAI_1.ship.v2Pos.y - 900), (friendlyAI_1.ship.v2Pos.x, friendlyAI_1.ship.v2Pos.y), 2)


log.createLog("Cleaning up for close...")