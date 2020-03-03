import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver as Observer

import py_logging
import py_config
import py_pandas as pandas


# def __init__(self, config=None, patterns=None, ignore_patterns=None,
#              ignore_directories=False, case_sensitive=False):
#     super(MyHandler, self).__init__()
#     # self.logger = py_logging.getLogger(config=config)

def on_created(event):
    # self.logger.debug(event.src_path)
    pandas.startProcess(event.src_path)


def on_modified(event):
    # self.logger.debug(event)
    pandas.startProcess(event.src_path)


# def on_any_event(self, event):
# self.logger.debug(event)


def startObserver(config):
    cfg = py_config.getCfg(config=config)
    logger = py_logging.getLogger(config=config)
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
    logger.debug("WatchDog is startting...")
    logger.debug('path=%s' % path)
    logger.debug('patterns=%s' % patterns)
    try:
        while 1:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        logger.debug("WatchDog is stopped.")
    observer.join()
    # return observer


if __name__ == "__main__":
    startObserver(config='py_watchdog.ini')
