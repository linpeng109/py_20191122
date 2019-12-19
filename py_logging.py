import datetime
import logging
from logging.handlers import RotatingFileHandler

import psutil

log = logging.getLogger('logger')
fileHandler = RotatingFileHandler(filename='mylogging.log',
                                  mode='a',
                                  maxBytes=1024 * 10,
                                  backupCount=5,
                                  encoding=None,
                                  delay=True)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
fileHandler.setFormatter(formatter)
log.addHandler(fileHandler)
log.setLevel(logging.DEBUG)

for i in range(1000):
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}% mem:{mem} '
    log.debug(line)
