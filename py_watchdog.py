import multiprocessing
import os
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver as Observer

import py_config
import py_logging
import py_pandas as pandas

cfg = py_config.getCfg(config='py_watchdog.ini')
logger = py_logging.getLogger(config='py_watchdog.ini')


# pandas._log = logger


def _router(event):
    pandas.startProcess(event)


def on_created(event):
    pandas.startProcess(event)


def on_modified(event):
    _router(event=event)


def startObserver():
    patterns = cfg.get('watchdog', 'patterns').split(';')
    path = cfg.get('watchdog', 'path')
    recursive = cfg.getboolean('watchdog', 'recursive')
    ignore_directories = cfg.getboolean('watchdog', 'ignore_directories')
    case_sesitive = cfg.getboolean('watchdog', 'case_sesitive')
    event_handler = PatternMatchingEventHandler(patterns=patterns,
                                                ignore_directories=ignore_directories,
                                                case_sensitive=case_sesitive)
    event_handler.on_created = on_created
    event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler=event_handler,
                      path=path, recursive=recursive)
    observer.start()
    logger.debug('WatchDog is startting......')
    logger.debug('path=%s' % path)
    logger.debug('patterns=%s' % patterns)
    try:
        while observer.is_alive():
            time.sleep(1)
    except  KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if (os.sys.platform.startswith('win')):
        multiprocessing.freeze_support()
    startObserver()
