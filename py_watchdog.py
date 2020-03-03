from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver as Observer
import time

import py_config
import py_logging
import py_pandas as pandas

config = py_config.getCfg('py_watchdog.ini')
logger = py_logging.getLogger(config='py_watchdog.ini')


def on_created(event):
    logger.debug(event.src_path)
    pandas.startProcess(event.src_path)


def on_modified(event):
    logger.debug(event)
    pandas.startProcess(event.src_path)


def on_any_event(event):
    logger.debug(event)


def createObserver():
    patterns = config.get('watchdog', 'patterns').split(';')
    path = config.get('watchdog', 'path')
    recursive = config.getboolean('watchdog', 'recursive')
    event_handler = PatternMatchingEventHandler(patterns=patterns,
                                                ignore_directories=True,
                                                case_sensitive=False)
    event_handler.on_created = on_created
    event_handler.on_modified = on_modified
    # event_handler.on_any_event=on_any_event

    observer = Observer()
    observer.schedule(event_handler=event_handler,
                      path=path, recursive=recursive)
    observer.start()
    logger.debug("WatchDog is startting...")
    logger.debug('path=%s' % path)
    return observer


if __name__ == "__main__":
    observer = createObserver()
    try:
        while observer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("WatchDog is stopped.")
    observer.join()
