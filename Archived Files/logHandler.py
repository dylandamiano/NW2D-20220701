import os
from os import path
import datetime as dt
import time

fullTime = dt.datetime.now()
timeAsString = str(fullTime.year) + str(fullTime.month) + str(fullTime.day) + "_" + str(int(time.time()))

fileName = timeAsString + ".log"

currentCount = 0

maxDisplay = 44
fontSize = 18

logHistory = [];
logDisplay = [];

logPath = "LogFiles"

if os.path.exists(os.path.join(logPath, fileName)) == True:
        pass
elif os.path.exists(os.path.join(logPath, fileName)) == False:
    with open(os.path.join(logPath, fileName), "x") as f:
        f.write("Log for Naval Warfare 2D, intended for debugging purposes only! \n\n")

print(os.listdir(logPath))

log_to_dist_index = 0

def update_display_log() -> None:
    global logHistory
    global logDisplay
    global log_to_dist_index

    if len(logDisplay) == 44:
        if logDisplay[len(logDisplay)-1].formatOutput() != logHistory[len(logHistory)-1].formatOutput():
            logDisplay.pop(0)
            logDisplay.append(logHistory[len(logHistory)-1])
    elif len(logDisplay) < 44:
        for i in range(log_to_dist_index, len(logHistory)):
            if len(logDisplay) < 44:
                logDisplay.append(logHistory[log_to_dist_index])
                log_to_dist_index += 1


def getDisplayLog() -> list:
    return logDisplay

def writeFile():
    if os.path.exists(os.path.join(logPath, fileName)) == True:
        with open(os.path.join(logPath, fileName), "a") as f:
            for i in range(0, len(logHistory)):
                f.write(logHistory[i].formatOutput() + "\n")
    else:
        #print("File does not exist!")
        pass

def getTime() -> dt.datetime:
    return dt.datetime.now()

class logObject():
    def __init__(self, currentTime, content):
        self.occurenceTime = currentTime
        self.logEntry = "(ENTRY #" + str(currentCount) + ") " + str(self.occurenceTime) + " >> " + content
        self.logNumber = currentCount
        self.Position = [0, 0]

    def __del__(self):
        #print("Log #" + str(self.logNumber) + " has been removed from debug console!")
        pass

    def formatOutput(self):
        return self.logEntry

def createLog(content):
    global currentCount
    global logHistory

    currentCount += 1

    currentTime = dt.datetime.now()
    newLog = logObject(currentTime, content)

    logHistory.append(newLog)
    #print(logHistory[currentCount-1].formatOutput())

    update_display_log()

createLog("Initialized Log handler...")