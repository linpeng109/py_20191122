import datetime
import logging
from logging.handlers import RotatingFileHandler

import psutil

import py_config


def getLogger(filename):
    cfg = py_config.getCfg(filename)
    logger = logging.getLogger(cfg.get('default', 'name'))
    rotatingFileHanglerDict = dict(cfg.items('logging'))
    rotatingFileHanglerDict['backupCount'] = 5
    rotatingFileHanglerDict['maxBytes'] = 1024000
    rotatingFileHangler = RotatingFileHandler(**rotatingFileHanglerDict)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s", "%Y%m%d-%H:%M:%S")
    rotatingFileHangler.setFormatter(formatter)

    logger.addHandler(rotatingFileHangler)
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger = getLogger('py_watchdog.ini')
    for i in range(1000):
        cpuper = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        now = datetime.datetime.now()
        line = f'cpu:{cpuper}% mem:{mem}'
        logger.debug(line)
