import datetime
import mylogging
import time
from mylogging.handlers import RotatingFileHandler

import psutil

def loopMonitor():
    # logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logger = mylogging.getLogger('monitor')
    fileHandler = RotatingFileHandler(filename='app.log',
                                      maxBytes=10 * 1024,
                                      backupCount=10)
    fileHandler.setLevel(level=mylogging.DEBUG)
    formatter = mylogging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    for _ in range(10):
        cpuper = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        line = f'{ts} cpu:{cpuper}% mem:{mem} '
        logger.debug("Success!")
        time.sleep(3)
loopMonitor()
