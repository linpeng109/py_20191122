import logging
import sys
from logging.handlers import RotatingFileHandler

import py_config


def getLogger(config):
    cfg = py_config.getCfg(config=config)
    logger = logging.getLogger(cfg.get('default', 'name'))

    fileHandlerDict = dict(cfg.items('logger'))
    fileHandlerDict['maxBytes'] = int(fileHandlerDict['maxBytes'])
    fileHandlerDict['backupCount'] = int(fileHandlerDict['backupCount'])
    fileHandler = RotatingFileHandler(**fileHandlerDict)
    formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%Y%b%d-%H:%M:%S")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger = getLogger(config='py_watchdog.ini')
    for i in range(10000):
        cpuper = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        line = f'cpu:{cpuper}% mem:{mem} '
        logger.info(line)
