import datetime
import logging
from logging.handlers import RotatingFileHandler

import psutil

import py_config


def getLogger():
    cfg = py_config.getCfg()
    log = logging.getLogger(cfg.get('logging', 'name'))
    cfgDict = {'filename': cfg.get('logging', 'filename'),
               'mode': cfg.get('logging', 'mode'),
               'maxBytes': cfg.getint('logging', 'maxBytes'),
               'backupCount': cfg.getint('logging', 'backupCount'),
               'encoding': cfg.get('logging', 'encoding'),
               'delay': cfg.getboolean('logging', 'delay')
               }
    fileHandler = RotatingFileHandler(**cfgDict)
    # formatter = logging.Formatter('%(name)-12s-%(levelname)-8s %(message)s')
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s", "%Y%b%d-%H:%M:%S")
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)
    log.setLevel(logging.DEBUG)
    return log


if __name__ == '__main__':
    log = getLogger()
    for i in range(1000):
        cpuper = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        line = f'{ts} cpu:{cpuper}% mem:{mem} '
        log.debug(line)
