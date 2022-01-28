'''
    NAVAL Warfare 2D

    Quick Overview:
        This game will be turn based and will allow up to 2 players to compete with AI based entities (up to 4 max for now)

'''


# Basic Module Initialization
import datetime
import math, random
import time

import gameCalculations
import gameSettings
import graphicInterface

import pygame, sys
from pygame.locals import *

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
pygame.init()

DISPLAYSURF = pygame.display.set_mode(size=(900,900))
FPSClock = pygame.time.Clock()
FPS = 100

pygame.display.set_caption("NAVAL Warfare 2d")


'''
    Going on below:
        - The image for the map is being PLACED upon the screen at the scale defined in the previous commentary above.
        - The Player / AI character objects are being initialized
'''

mapInit = playerClasses.islandMap()

friendlyAI_1 = playerClasses.Player("AI Entity #1")
friendlyAI_1.createShip("Carrier")

'''
    The function below will do the following:
        - Create cloud objects
        - Set a movement interval for clouds after an "x" period of time
        - Randomize the location of said cloud in question
'''

def createCloud():
    t = time.time()
    randBreak = math.floor(random.randrange(1, 10))
    #print(randBreak)

    if ( (t - gameSettings.cloudLast) >= randBreak):
        gameSettings.cloudLast = t

        sel = math.floor(random.randrange(0, len(gameSettings.cloudChart)))

        #print(sel)
        cloudObj = playerClasses.Cloud(sel, gameSettings.cloudDims)
        cloudObj.createLocation()

        #DISPLAYSURF.blit(cloudObj.image, cloudObj.rect)
        gameSettings.activeClouds.insert(len(gameSettings.activeClouds) + 1, cloudObj)

'''
    As seen below:
        - The game loop is going to run infinitely until a certain criteria is met (in this case, the player will be required to close the game!)
        - Everything that is critical to the functionality of the game will be called in this loop such as moving characters (clouds, and other things alike) around the viewport.
'''

running = True

# pygame.display.toggle_fullscreen()

pygame.draw.rect(DISPLAYSURF, (0, 0, 255), (125.2, 196.8, 309.1/2, 125.2/2))

#pygame.mixer.music.load('HaloMjolnirMix.mp3')
#pygame.mixer.music.play(-1)

while running == True:
    
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

    DISPLAYSURF.blit(mapInit.image, mapInit.rect)
    DISPLAYSURF.blit(friendlyAI_1.ship.image, friendlyAI_1.ship.rect)
    pygame.draw.rect(DISPLAYSURF, (0, 0, 255), (125.2, 196.8, 309.1/2, 125.2/2))
    #DISPLAYSURF.blit(graphicInterface.mainMenu.image, graphicInterface.mainMenu.rect)

    for i in range (0, math.floor(random.randrange(0, 5))):
        createCloud()

    #t = time.time()

    for x in range(0, len(gameSettings.activeClouds)):

        #if ((t - gameSettings.activeClouds[x].lastMove) >= gameSettings.activeClouds[x].moveInt):
            #gameSettings.activeClouds[x].lastMove = t
        gameSettings.activeClouds[x].rect.move_ip(1, 0)
        gameSettings.activeClouds[x].posX += 1
        DISPLAYSURF.blit(gameSettings.activeClouds[x].image, gameSettings.activeClouds[x].rect)
            #pygame.draw.rect(DISPLAYSURF, "Blue", friendlyAI_1.ship.rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        elif event.type == pygame.KEYDOWN:
            gameCalculations.key_PressedEvent(event, friendlyAI_1.ship)
            gameSettings.setKeyStatus(event, "DOWN")
        elif event.type == pygame.KEYUP:
            gameSettings.setKeyStatus(event, "UP")
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            graphicInterface.checkMouseInput()
    
    for k in gameSettings.playerOneKeys:
        if (gameSettings.playerOneKeys[k] == True):
            gameCalculations.key_held("W", friendlyAI_1.ship)

print("Press <ENTER> to exit")