import pygame
from pygame.locals import *

playerOneKeys = {
    "W_Hold": False,
    "A_Hold": False,
    "S_Hold": False,
    "D_Hold": False,
    "Q_Hold": False,
    "E_Hold": False
}

maxPlayers = 2
playerCount = 0

cloudLast = 0

'''

    The list listed below contains up to five clouds.
    These clouds are not randomly generated but rather created
    through a graphical application called 'Affinity Designer'

'''

cloudChart = [
    "CloudFiles\\Cloud1.png",
    "CloudFiles\\Cloud2.png",
    "CloudFiles\\Cloud3.png",
    "CloudFiles\\Cloud4.png",
    "CloudFiles\\Cloud5.png"
]

# The list below contains the required size for the cloud upon generation
cloudDims = [
    [143, 85], 
    [113, 66],
    [73, 34],
    [114, 117],
    [96, 68]
]

def resetKeyStatus():
    for key in playerOneKeys:
        playerOneKeys[key] = False

def getKeyStatus():
    return playerOneKeys

def setKeyStatus(regKey = None, eventType = None):
    if (eventType == "UP"):
        if (regKey.key == pygame.K_w):
            playerOneKeys["W_Hold"] = False
            print("W lifted")
        elif (regKey.key == pygame.K_a):
            playerOneKeys["A_Hold"] = False
        elif (regKey.key == pygame.K_s):
            playerOneKeys["S_Hold"] = False
        elif (regKey.key == pygame.K_d):
            playerOneKeys["D_Hold"] = False
        elif (regKey.key == pygame.K_q):
            playerOneKeys["Q_Hold"] = False
        elif (regKey.key == pygame.K_e):
            playerOneKeys["E_Hold"] = False
    elif (eventType == "DOWN"):
        if (regKey.key == pygame.K_w): 
            playerOneKeys["W_Hold"] = True
            print("W pressed")
        elif (regKey.key == pygame.K_a):
            playerOneKeys["A_Hold"] = True
        elif (regKey.key == pygame.K_s):
            playerOneKeys["S_Hold"] = True
        elif (regKey.key == pygame.K_d):
            playerOneKeys["D_Hold"] = True
        elif (regKey.key == pygame.K_q):
            playerOneKeys["Q_Hold"] = True
        elif (regKey.key == pygame.K_e):
            playerOneKeys["E_Hold"] = True
    elif (regKey == None and eventType == None):
        pass

    print(getKeyStatus())

'''

    The list below will contain clouds
    that are currently present in memory.
    
    When the cloud runs off the viewport,
    the overall goal will be to get it's position
    and determine whether it should be removed or not.
    
    If the cloud is not removed, it will cause what is
    essentially known as a 'memory-leak' which will
    cause data-stored in ram temporarily to stay until the
    computer shuts down.

'''

activeEntities = []
activeClouds = []

# \\ IGNORE THE FUNCTIONS BELOW! THESE ARE FOR DEBUGGING! // #
def test():
    print("new")

def playerCount():
    '''
        Function will not output a debug line out to the console.

        Instead, try to capture the player count which should be stored in a variable...
    '''
    return playerCount