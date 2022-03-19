import os
import datetime as dt
import logging
import time

fullTime = dt.datetime.now()
timeAsString = str(fullTime.year) + str(fullTime.month) + str(fullTime.day) + "_" + str(int(time.time()))

fileName = timeAsString + ".log"
fontSize = 18
logPath = "LogFiles"

# create log dir if it doesnt exist
try:
    os.mkdir(logPath)
except OSError:
    pass

logging.basicConfig(
    datefmt='%m/%d/%Y %I:%M:%S %p',
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(f'{logPath}/{timeAsString}.log'),
        logging.StreamHandler()
    ],
    level=logging.DEBUG
)

logging.info("Initialized Log handler...")