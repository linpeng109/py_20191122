from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver as Observer

import py_config
import py_logging
import py_pandas as pandas
import py_path as path
import time

cfg = py_config.getCfg(config='py_watchdog.ini')
logger = py_logging.getLogger(config='py_watchdog.ini')


def on_created(event):
    file = event.src_path
    if (path.filenameIsContains(file, ['AAS.txt'])):
        pandas.convertAASTxt(file)
    if (path.filenameIsContains(file, ['HCS.txt'])):
        pandas.convertHCSTxt(file)
    if (path.filenameIsContains(file, ['AFS', '.xlsx'])):
        pandas.convertAFSExcel(file)


def on_modified(event):
    file = event.src_path
    if (path.filenameIsContains(file, ['AAS.txt'])):
        pandas.convertAASTxt(file)
    if (path.filenameIsContains(file, ['HCS.txt'])):
        pandas.convertHCSTxt(file)
    if (path.filenameIsContains(file, ['AFS', '.xlsx'])):
        pandas.convertAFSExcel(file)


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
    logger.debug("WatchDog is startting...")
    logger.debug('path=%s' % path)
    logger.debug('patterns=%s' % patterns)
    try:
        while observer.is_alive:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.debug("WatchDog is stopped.")
    observer.join()


if __name__ == "__main__":
    startObserver()
