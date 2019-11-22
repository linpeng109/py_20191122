import datetime
import logging
import time
from logging.handlers import RotatingFileHandler

import psutil


def MonitorSystem(logger=None):
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}% mem:{mem} '
    print(line)
    if logger:
        logger.debug(line)


def loopMonitor():
    # logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logger = logging.getLogger('monitor')
    fileHandler = RotatingFileHandler(filename='app.log',
                                      maxBytes=10 * 1024,
                                      backupCount=10)
    fileHandler.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    while True:
        MonitorSystem(logger)
        time.sleep(3)


loopMonitor()
