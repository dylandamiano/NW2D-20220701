import os
from os import path
import datetime as dt
import time

fullTime = dt.datetime.now()
timeAsString = str(fullTime.year) + str(fullTime.month) + str(fullTime.day) + "_" + str(int(time.time()))

fileName = timeAsString + ".log"

currentCount = 0

logHistory = [];
logDisplay = [];

logPath = "LogFiles"

if os.path.exists(os.path.join(logPath, fileName)) == True:
        pass
elif os.path.exists(os.path.join(logPath, fileName)) == False:
    with open(os.path.join(logPath, fileName), "x") as f:
        f.write("Log for Naval Warfare 2D, intended for debugging purposes only! \n\n")

print(os.listdir(logPath))

def getDisplayLog() -> list:
    return logDisplay

def writeFile():
    if os.path.exists(os.path.join(logPath, fileName)) == True:
        with open(os.path.join(logPath, fileName), "a") as f:
            for i in range(0, len(logHistory)):
                f.write(logHistory[i].formatOutput() + "\n")
    else:
        print("File does not exist!")

def getTime() -> dt.datetime:
    return dt.datetime.now()

class logObject():
    def __init__(self, currentTime, content):
        self.occurenceTime = currentTime
        self.logEntry = "(ENTRY #" + str(currentCount) + ") " + str(self.occurenceTime) + " >> " + content
        self.logNumber = currentCount
        self.Position = [0, 0]

    def __del__(self):
        print("Log #" + str(self.logNumber) + " has been removed from debug console!")

    def formatOutput(self):
        return self.logEntry

def createLog(content):
    global currentCount
    global logHistory

    currentCount += 1

    currentTime = dt.datetime.now()
    newLog = logObject(currentTime, content)

    logHistory.append(newLog)
    print(logHistory[currentCount-1].formatOutput())

createLog("Initialized Log handler...")